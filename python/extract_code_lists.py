import os
import re
import sys
import csv
from PyPDF2 import PdfReader

def extract_cl_references(search_dir):
    pattern = re.compile(r"CL[0-9]{3}", re.IGNORECASE)
    found_refs = set()

    for root, dirs, files in os.walk(search_dir):
        for filename in files:
            if filename.endswith(".md"):
                path = os.path.join(root, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    found_refs.update(m.upper() for m in matches)

    return sorted(found_refs, key=lambda x: int(x[2:]))

def extract_bracketed_from_pdf(pdf_path, cl_codes):
    results = {}

    if not os.path.exists(pdf_path):
        print(f"Warning: PDF not found: {pdf_path}")
        return results

    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return results

    print(f"Scanning PDF for {len(cl_codes)} missing CL codes…")

    full_text = ""
    for page in reader.pages:
        text = page.extract_text() or ""
        full_text += "\n" + text

    pattern_template = r"({})\s*\(([^)]+)\)"

    for cl in cl_codes:
        pattern = pattern_template.format(re.escape(cl))
        match = re.search(pattern, full_text)

        if match:
            bracket_value = match.group(2).strip()
            results[cl] = bracket_value

    return results

def extract_mappings(cl_list, csv_file, pdf_file, output_file):
    ENTITY_COLUMN = "ENTITY_NAME"
    cl_column = None
    found_csv = {}

    with open(csv_file, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for field in reader.fieldnames:
            if field.lower().startswith("cl"):
                cl_column = field
                break

        if not cl_column:
            print("Error: CSV missing CL column.")
            sys.exit(1)

        if ENTITY_COLUMN not in reader.fieldnames:
            print(f"Error: CSV missing required column: {ENTITY_COLUMN}")
            sys.exit(1)

        print(f"Using CSV CL column: {cl_column}")
        print(f"Using CSV ENTITY_NAME column: {ENTITY_COLUMN}")

        for row in reader:
            cl_value = row[cl_column].strip()
            if cl_value in cl_list:
                found_csv[cl_value] = row[ENTITY_COLUMN].strip()

    # Determine missing CL codes
    missing_codes = [cl for cl in cl_list if cl not in found_csv]

    print(f"Found {len(found_csv)} matches in CSV.")
    print(f"{len(missing_codes)} missing CL codes will be searched in the PDF.")

    # ---- PDF fallback search ----
    pdf_results = extract_bracketed_from_pdf(pdf_file, missing_codes)

    # ---- Write final output CSV specified by the user ----
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Code List", "Title"])

        for cl in cl_list:
            csv_value = found_csv.get(cl)
            pdf_value = pdf_results.get(cl)

            # CSV first, PDF fallback
            entity_value = csv_value or pdf_value or ""

            writer.writerow([cl, entity_value])

    print(f"\nOutput saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python combined_cl_tool.py <markdown_dir> <csv_file> <pdf_file> <output_file>")
        sys.exit(1)

    md_dir = sys.argv[1]
    csv_file = sys.argv[2]
    pdf_file = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.exists(md_dir):
        print(f"Error: Directory not found: {md_dir}")
        sys.exit(1)

    if not os.path.exists(csv_file):
        print(f"Error: CSV file not found: {csv_file}")
        sys.exit(1)

    # Step 1: Extract CL codes
    cl_list = extract_cl_references(md_dir)
    print(f"Extracted {len(cl_list)} CL codes.")

    # Step 2 & 3: Create output file with CSV + PDF fallback values
    extract_mappings(cl_list, csv_file, pdf_file, output_file)

    print("\nAll tasks complete.")
