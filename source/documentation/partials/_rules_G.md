## G0001

**Functional Description**

If at least one &lt;CONSIGNMENT-HOUSE CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; is<br>
EQUAL to ’30600’ in the declaration, then for the specific &lt;CONSIGNMENT-HOUSE<br>
CONSIGNMENT&gt; the Data Group CONSIGNEE shall not be used AND &lt;CONSIGNMENT-<br>
CONSIGNEE&gt; shall not be used. For the rest of the repetitions of &lt;CONSIGNMENT-HOUSE<br>
CONSIGNMENT&gt; the specific IF statement [If at least one &lt;CONSIGNMENT-HOUSE<br>
CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; is EQUAL to ’30600’] shall be re-validated.<br>
During the NCTS-P4/NCTS-P5 Transitional Period same approach shall be followed for the<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br>
INFORMATION.Code&gt;.

**Technical Description**

N/A


## G0002

**Functional Description**

XSD contains a non-standard regular expression for this data item.

**Technical Description**

N/A

## G0005

**Functional Description**

The maximum value is 1999 as defined in the XSD pattern.

**Technical Description**

N/A

## G0006

**Functional Description**

&lt;TRANSPORT EQUIPMENT-GOODS REFERENCE.Declaration goods item number&gt; is filled in with<br>
the item number of the goods concerned as provided in Declaration goods item number.

**Technical Description**

N/A


## G0009

**Functional Description**

IF &lt;FUNCTIONAL ERROR.Error code&gt; is in SET {90, 93}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;FUNCTIONAL ERROR.Error pointer&gt; shall include the &lt;TRANSIT OPERATION.MRN&gt; of the<br>
&nbsp;&nbsp;&nbsp;&nbsp;rejected message<br>
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is in SET {92, 51, 52}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;FUNCTIONAL ERROR.Error pointer&gt; shall include the &lt;Root Element&gt;<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;FUNCTIONAL ERROR.Error pointer&gt; shall include the XPath location to point to the Data Item<br>
&nbsp;&nbsp;&nbsp;&nbsp;or the Data Group that caused the error.

**Technical Description**

N/A


## G0010

**Functional Description**

IF &lt;FUNCTIONAL ERROR.Error code&gt; is EQUAL to '12'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;FUNCTIONAL ERROR.Error reason&gt; shall point to the Codelist number against which<br>
&nbsp;&nbsp;&nbsp;&nbsp;validation failed (ie CLxxx)<br>
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is in SET {13, 15}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;FUNCTIONAL ERROR.Error reason&gt; shall point to the Condition/Technical Rule number<br>
&nbsp;&nbsp;&nbsp;&nbsp;against which validation failed (ie Cxxxx or Txxxx),<br>
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is EQUAL to '14'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;FUNCTIONAL ERROR.Error reason&gt; shall point to the Rules/Technical Rule number against<br>
&nbsp;&nbsp;&nbsp;&nbsp;which validation failed (ie Rxxxx or Txxxx)<br>
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is EQUAL to '50'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;FUNCTIONAL ERROR.Error reason&gt; shall point to the Transitional Constraint number against<br>
&nbsp;&nbsp;&nbsp;&nbsp;which validation failed (ie Exxxx or Bxxxx),<br>
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is in SET {51, 52}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the &lt;FUNCTIONAL ERROR.Error reason&gt; shall be:<br>
&nbsp;&nbsp;&nbsp;&nbsp;• 'ieCAvB' if exception is thrown by ieCA<br>
&nbsp;&nbsp;&nbsp;&nbsp;• 'NCAvB' if exception is thrown by NTA/NECA,<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the &lt;FUNCTIONAL ERROR.Error reason&gt; shall have the value 'N/A'

**Technical Description**

N/A


## G0014

**Functional Description**

Eastern longitude and Northern latitude will use the optional '+' sign.<br>
Western longitude and Southern latitude will use the '-' sign.

**Technical Description**

N/A


## G0015

**Functional Description**

In case of Incident information received via one or multiple CD180C, all the information received shall<br>
be included in the D.G. &lt;CONSIGNMENT-INCIDENT&gt;.

**Technical Description**

N/A


## G0016

**Functional Description**

&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Container identification number&gt; is filled in<br>
case of incident with the new Container identification number amending initial declaration or with the<br>
existing Container identification number if DI Number of seals is greater than 0.

**Technical Description**

N/A


## G0017

**Functional Description**

'State of seals' = '0' in case that the seals are not in good state (i.e. expected but not present OR<br>
damaged OR present with discrepancies found). In this case, the &lt;CD018C-CONTROL<br>
RESULT.Code&gt; is 'A5' (or 'B1' if more (major) discrepancies are identified) as defined in the Transit<br>
Manual.<br>
'State of seals' = '1' in case that the seals are in good state (present and not damaged, with no<br>
discrepancies found) OR [applicable for the CD018C only] not present as expected based on<br>
information received from other Customs Offices.

**Technical Description**

N/A


## G0020

**Functional Description**

Refers to the mode of transport corresponding to the active means of transport which is expected to be<br>
used on exit from or entry into the Safety and Security area.

**Technical Description**

N/A


## G0021

**Functional Description**

The value '0' (zero) is a valid number in this Data Item, as per applicable XSD pattern.

**Technical Description**

N/A

## G0023

**Functional Description**

The D.I. will be filled in with new value amending initial declaration in case of incident

**Technical Description**

N/A

## G0024

**Functional Description**

D.I. will be filled if the value is provided.

**Technical Description**

N/A

## G0025

**Functional Description**

The value of D.I. &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Security indicator from export<br>
declaration&gt; will be equal to D.I. &lt;CC191C-AES RESULTS-EXPORT OPERATION.Security&gt;.

**Technical Description**

N/A


## G0026

**Functional Description**

The multiplicity of this D.G. at House Consignment level is defined as 99x for homogeneity with the<br>
multiplicity of the same D.G. at other levels.<br>
If this D.G. is used, it should be present only ONCE.<br>
This D.G. can be used only in case of standard customs declaration (Additional Declaration Type = 'A')<br>
with Export followed by Transit (Previous Document Export Type = 'N830')<br>
(There should be maximum one export MRN included per one House Consignment, no groupage of<br>
export declaration should be applied within one HC).

**Technical Description**

N/A


## G0029

**Functional Description**

The D.I. will be filled in with new value amending initial declaration in case of incident. In case goods<br>
were initially not containerized and are placed in a container, or the initial container is replaced by<br>
another container then &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is equal<br>
to '1' else &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is equal to '0'.

**Technical Description**

N/A


## G0030

**Functional Description**

If a consignment is moving from one Member State to another Member State via a third country which<br>
is not in set of CL009 (CountryCodesCommonTransit) then a &lt;CUSTOMS OFFICE OF TRANSIT<br>
(DECLARED)&gt; shall be declared and located in the specific Member States.

**Technical Description**

N/A


## G0033

**Functional Description**

The Data Item &lt;AUTHORISATION.Reference number&gt; must be valid in CDMS or in the National<br>
Decision Management System.

**Technical Description**

N/A


## G0034

**Functional Description**

In case of Export followed by Transit and whenever the internal transit procedure is applied, the<br>
Declared Office of Destination needs to be ‘appropriate’, otherwise the initial submission and/or<br>
subsequent amendment requests of the transit declaration data as submitted by the Holder of the<br>
Transit Procedure to the Office of Departure has to be rejected.  This can be validated as follows:<br>
A/ In case the Declared Office of Destination belongs to EU MS (CL010- CountryCodesCommunity),<br>
and its Custom Office Reference Number is included in both CL172- CustomsOfficeDestination and<br>
CL294-CustomsOfficeExitDeclared, then it is considered ‘appropriate’ (otherwise is considered not<br>
‘appropriate’);<br>
B/ In case the Declared Office of Destination belongs to CTC (CL112- CountryCodesCTC), it is<br>
considered by default ‘appropriate’.<br>
For Opt-in NA’s, when the Declared Office of Destination is considered as not ‘appropriate’, the<br>
messages CCA13D or CCA15D will be responded with CC056D that will report the error code '12-<br>
Codelist violation'.<br>
For Opt-out NA’s, when the Declared Office of Destination is considered as not ‘appropriate’, the<br>
messages CC013C or CC015C will be responded with CC056C that will report the error code '12-<br>
Codelist violation'.

**Technical Description**

N/A


## G0042

**Functional Description**

This D.G./D.I. is not used to report discrepancies. The Control Message always reports back D.G./D.I<br>
as at declaration message.

**Technical Description**

N/A


## G0045

**Functional Description**

The information in this Data Group/Data Item will override the information included in the CC015C or<br>
CCA15D (or in the latest CC013C or CCA13D, if any).

**Technical Description**

N/A


## G0050

**Functional Description**

The Reference number shall include the ARC number or the fallback eAD reference number when the<br>
‘Type’ of the ‘Additional reference’ is C651 or C658 respectively.

**Technical Description**

N/A


## G0057

**Functional Description**

Common Code List can be extended or restricted at national level. Purely national codes are not<br>
included in Common Domain messages.

**Technical Description**

N/A


## G0058

**Functional Description**

When &lt;CONSIGNMENT - HOUSE CONSIGNMENT - CONSIGNMENT ITEM - PREVIOUS<br>
DOCUMENT.Type&gt; is in SET {C651, C658} the Unique Body Reference (UBR) is required to be<br>
recorded in this field.

**Technical Description**

N/A


## G0061

**Functional Description**

The information presented in this D.G. is related to Safety & Security and to the Binding Itinerary. In<br>
case of Binding itinerary, the information entered must include the list of codes of the countries<br>
between the Office of Departure and the Office of Destination. If more information is available about<br>
the countries visited by the means of transport since its first place of loading until the last place of<br>
unloading, it should also be added for Safety & Security purpose only.

**Technical Description**

N/A


## G0062

**Functional Description**

The rules R0506 and R0507 are applied on CC015C, CCA15D,CC013C and CCA13D to ensure that<br>
the declaration does not include unnecessary and repetitive information. They must be enforced by all<br>
NTA. Considering the possibility that one Goods Item is taken out from the declaration during the<br>
control, the message CC029C, CCA29D and CD001C may have different content from CC015C,<br>
CCA15D (or CC013C, CCA13D or CC170C). Consequently, those rules R0506 and R0507 shall not be<br>
strictly enforced on the Common Domain messages. Certainly not by the recipient of the CD message,<br>
likely not by the sender of the CD message.

**Technical Description**

N/A


## G0068

**Functional Description**

'The Data Group &lt;CONSIGNMENT- HOUSE CONSIGNMENT- CONSIGNMENT ITEM- ADDITIONAL<br>
REFERENCE&gt; will be also used to include the information of EMCS consignment exported from one<br>
EU member state into a Non-EU-Member state, in case of Export Followed by Transit (where in<br>
messages CC013C or CCA13D or CC015C or CCA15D the &lt;CONSIGNMENT- HOUSE<br>
CONSIGNMENT- PREVIOUS<br>
DOCUMENT.Type&gt; = 'N830' AND &lt;CONSIGNMENT- HOUSE CONSIGNMENT- CONSIGNMENT<br>
ITEM-  ADDITIONAL REFERENCE. Type&gt; is in SET CL234 (DocumentTypeExcise)).<br>
In this case, the Data Group &lt;GOODS SHIPMENT- GOODS ITEM- PREVIOUS DOCUMENT&gt; of the<br>
Export declaration, will be mapped with the Data Group &lt;CONSIGNMENT- HOUSE CONSIGNMENT-<br>
CONSIGNMENT ITEM- ADDITIONAL REFERENCE&gt; of the Transit declaration.

**Technical Description**

N/A


## G0069

**Functional Description**

The Data Group &lt;CONSIGNMENT- HOUSE CONSIGNMENT- CONSIGNMENT ITEM- SUPPORTING<br>
DOCUMENT&gt;, can be also used to include the information related to EMCS consignment (where<br>
&lt;CONSIGNMENT- HOUSE CONSIGNMENT- CONSIGNMENT ITEM- SUPPORTING<br>
DOCUMENT.Type&gt; is in SET CL234 (DocumentTypeExcise)), transported from one EU member state<br>
into another EU member state via a CTC country.

**Technical Description**

N/A


## G0071

**Functional Description**

In case of Export Followed by Transit (i.e. &lt;CONSIGNMENT-HOUSE CONSIGNMENT- PREVIOUS<br>
DOCUMENT.Type&gt; = 'N830'), all and only the goods items declared in &lt;GOODS SHIPMENT-GOODS<br>
ITEM&gt; as defined in the related Export declaration (identified by the MRN) must be included in<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT- CONSIGNMENT ITEM&gt; Data Group.

**Technical Description**

N/A


## G0072

**Functional Description**

In case of Export Followed By Transit (&lt;CONSIGNMENT-HOUSE CONSIGNMENT- PREVIOUS<br>
DOCUMENT.Type&gt; = 'N830'),<br>
-   all the goods items declared in &lt;GOODS SHIPMENT-GOODS ITEM&gt; as defined in the related Export<br>
declaration (identified by the MRN) and<br>
-   all the goods items declared in the &lt;CONSIGNMENT-HOUSE CONSIGNMENT- CONSIGNMENT<br>
ITEM&gt; defined in the transit declaration<br>
must be listed in the same order (with &lt;GOODS SHIPMENT-GOODS ITEM.Declaration goods item<br>
number&gt; = &lt;CONSIGNMENT-HOUSE CONSIGNMENT- CONSIGNMENT ITEM.Goods item<br>
number&gt;). Keeping the order of the goods item is required to enable the automatic validation of the<br>
matching of the goods in the context of Export followed by Transit.

**Technical Description**

N/A


## G0079

**Functional Description**

The information presented in in this D.G. is related to Safety & Security and to the Binding Itinerary.<br>
In case of Binding itinerary, the information entered must include the list of codes of the countries<br>
between the Office of Departure and the Office of Destination.<br>
In case of combined transit declaration with ENS data, the list of countries visited by the means of<br>
transport between the first place of loading until the last place of unloading shall be included.

**Technical Description**

N/A


## G0088

**Functional Description**

When &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3', the identification number of the<br>
trailer must also be provided (where applicable).

**Technical Description**

N/A


## G0090

**Functional Description**

The Data Group ‘Carrier’ shall be provided if the value is different from the ‘Holder of the transit<br>
procedure’.<br>
The Data Group ‘Carrier’ should not be present if the ‘Holder of the transit procedure’ is also the<br>
‘Carrier’.

**Technical Description**

N/A


## G0100

**Functional Description**

If &lt;TRADER AT DESTINATION.Communication language at destination&gt; is PRESENT, then the<br>
indicated language is used as the basic language in any further communication between the Trader<br>
and the Customs system. If &lt;TRADER AT DESTINATION.Communication language at destination&gt; is<br>
not PRESENT then the Customs system will use the default language of the Office concerned;<br>
If &lt;TRANSIT OPERATION.Communication language at transit&gt; is PRESENT, then the indicated<br>
language is used as the basic language in any further communication between the Trader and the<br>
Customs system. If &lt;TRANSIT OPERATION.Communication language at transit&gt; is not PRESENT<br>
then the Customs system will use the default language of the Office concerned;<br>
If &lt;TRANSIT OPERATION.Communication language at departure&gt; is PRESENT, then the indicated<br>
language is used as the basic language in any further communication between the Trader and the<br>
Customs system. If &lt;TRANSIT OPERATION.Communication language at departure&gt; is not PRESENT<br>
then the Customs system will use the default language of the Office concerned.

**Technical Description**

N/A


## G0101

**Functional Description**

The value of the Data Item &lt;INVALIDATION.Initiated by customs&gt; is<br>
‘0’ ('No') when the request to invalidate is initiated by the trader;<br>
The value of the Data Item &lt;INVALIDATION.Initiated by customs&gt; is<br>
‘1’ ('Yes') when the request to invalidate is initiated by the customs.

**Technical Description**

N/A


## G0102

**Functional Description**

For each type of authorisation, the authorisation is valid for the whole declaration (i.e. for the different<br>
HOUSE CONSIGNMENTS).

**Technical Description**

N/A


## G0103

**Functional Description**

Each iteration of this data group shall include:<br>
-Either the transport equipment information for the containerised goods with seals OR without seals<br>
with reference to those goods;<br>
-OR the transport equipment information for the non containerised but sealed goods (e.g. goods<br>
carried by truck with seals) with reference to those goods;<br>
Note: the non containerised and unsealed goods shall not be recorded under this data group.

**Technical Description**

N/A


## G0105

**Functional Description**

Information recorded under this data group is solely for communication purposes. No legal liabilities<br>
exist upon the specific contact person.

**Technical Description**

N/A


## G0112

**Functional Description**

If IMO ship identification number (type ‘10’) exists for that ship, it must be used and the Name of the<br>
sea-going vessel (type ‘11’) shall not be used.

**Technical Description**

N/A


## G0113

**Functional Description**

The country code used to define the ‘Country of destination’ can be different from the country code<br>
used in the data item ‘Country’ included in the address of the ‘Consignee’.

**Technical Description**

N/A


## G0114

**Functional Description**

The Data Item &lt;AUTHORISATION.Type&gt; shall include the value ‘C521’ when the transit declaration is<br>
submitted under simplified procedure (authorised consignor) and only in this case.

**Technical Description**

N/A


## G0115

**Functional Description**

This Data Item is required as per UCC-DA (Annex B) but may be waived for modes of transport other<br>
than rail in case the transit movement does not cross the external border of the Union.

**Technical Description**

N/A


## G0117

**Functional Description**

Common Code List can be extended at national level. Purely national codes are not included in<br>
Common Domain messages.

**Technical Description**

N/A


## G0118

**Functional Description**

IF the declaration is lodged without Safety and Security data then:<br>
&nbsp;&nbsp;&nbsp;&nbsp;-where goods are carried in multimodal transport units, such as containers, swap bodies and semi<br>
&nbsp;&nbsp;&nbsp;&nbsp;trailers, the customs authorities may authorise the holder of the transit procedure not to provide this<br>
&nbsp;&nbsp;&nbsp;&nbsp;information where the logistical pattern at the point of departure may prevent the identity and<br>
&nbsp;&nbsp;&nbsp;&nbsp;nationality of the means of transport from being provided at the time the goods are released for transit,<br>
&nbsp;&nbsp;&nbsp;&nbsp;providing multimodal transport units bear unique numbers and such numbers are indicated in D.E. 19<br>
&nbsp;&nbsp;&nbsp;&nbsp;07 063 000 Container identification number<br>
&nbsp;&nbsp;&nbsp;&nbsp;-In the following cases, Member States shall waive the obligation to enter this information on a transit<br>
&nbsp;&nbsp;&nbsp;&nbsp;declaration lodged at the office of departure in relation with the means of transport on which the goods<br>
&nbsp;&nbsp;&nbsp;&nbsp;are directly loaded:<br>
&nbsp;&nbsp;&nbsp;&nbsp;-where the logistical pattern does not allow this data element to be provided and the holder of the<br>
&nbsp;&nbsp;&nbsp;&nbsp;transit procedure has the AEOC status and<br>
&nbsp;&nbsp;&nbsp;&nbsp;-where the relevant information may be traced where needed by the customs authorities via the<br>
&nbsp;&nbsp;&nbsp;&nbsp;records of the holder of the transit procedure.

**Technical Description**

N/A


## G0119

**Functional Description**

This Data Group is “Required” except where one of the following conditions apply:<br>
-For the declaration that include Inland Mode Of Transport with the value ‘5’;<br>
-Where goods are carried in multimodal transport units, such as containers, swap bodies and semi<br>
trailers, the customs authorities may authorise the holder of the transit procedure not to provide this<br>
information where the logistical pattern at the point of departure may prevent the identity and<br>
nationality of the means of transport from being provided at the time the goods are released for transit,<br>
providing multimodal transport units bear unique numbers and such numbers are indicated in the Data<br>
Item ‘Container identification number’;<br>
-For the means of transport on which the goods are directly loaded:<br>
-the logistical pattern does not allow this data element to be provided and the holder of the transit<br>
procedure has the appropriate status (AEOC in EU) and<br>
-the relevant information may be traced where needed by the customs authorities via the records of<br>
the holder of the transit procedure.

**Technical Description**

N/A


## G0120

**Functional Description**

The Data Item ‘Identification number’ is required for the Data Group ‘HOLDER OF THE TRANSIT<br>
PROCEDURE’, except for:<br>
- economic operators residing outside of the common transit countries (outside CL009<br>
(CountryCodesCommonTransit)), and<br>
- private individuals for which an identification number may be used but is not required.

**Technical Description**

N/A


## G0123

**Functional Description**

This Data Group must be provided when different from the ‘HOLDER OF THE TRANSIT<br>
PROCEDURE’.<br>
IF the unique ‘CONSIGNOR’ of the consignment is different from the ‘HOLDER OF THE TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;PROCEDURE’<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the Data Group &lt;CONSIGNMENT -CONSIGNOR&gt; must include this ‘CONSIGNOR’;<br>
IF the ‘CONSIGNOR’ of one or more house consignment(s) is different from the ‘HOLDER OF THE<br>
&nbsp;&nbsp;&nbsp;&nbsp;TRANSIT PROCEDURE’<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the Data Group &lt;CONSIGNMENT -HOUSE CONSIGNMENT -CONSIGNOR&gt; must include this<br>
&nbsp;&nbsp;&nbsp;&nbsp;‘CONSIGNOR’.

**Technical Description**

N/A


## G0126

**Functional Description**

The value of this Data Item should be:<br>
‘A1’ (Satisfactory): When the goods are released for transit after physical control (full or partial) and no<br>
discrepancies were detected;<br>
‘A2’ (Considered satisfactory): When the goods are released for transit after documentary control only<br>
(no physical control) and no discrepancies were detected or without any control;<br>
‘A3’ (Simplified procedure): In case of simplified procedure without control performed by the Customs<br>
Office of Departure (the goods are released for transit by an authorised consignor).

**Technical Description**

N/A


## G0127

**Functional Description**

The Data Item shall be filled, by using the information of the &lt;TRANSIT OPERATION. Limit date&gt;,<br>
included either:<br>
- in the initial declaration CC015C or CCA15D messages or<br>
- in any possible amendments CC013C or CCA13D or<br>
- using the revised expected arrival date entered by the Officer at the Office Of Departure when the<br>
movement is released for transit.

**Technical Description**

N/A


## G0131

**Functional Description**

IF discrepancies have been found the Data Group will be filled in with new values amending initial<br>
&nbsp;&nbsp;&nbsp;&nbsp;declaration.

**Technical Description**

N/A


## G0139

**Functional Description**

The ‘0’ (zero) value should only be used in cases where it has been identified that two or more goods<br>
items are packaged together but this was not declared correctly at first instance.

**Technical Description**

N/A


## G0142

**Functional Description**

&lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; shall be declared when switching from a<br>
contracting party to a different contracting party.

**Technical Description**

N/A


## G0160

**Functional Description**

If the declaration is submitted under simplified procedure then this D.G/D.I. must be present.

**Technical Description**

N/A

## G0165

**Functional Description**

IF the declaration is submitted under simplified procedure AND the authorisation of which foresees the<br>
&nbsp;&nbsp;&nbsp;&nbsp;use of seals,<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'.

**Technical Description**

N/A


## G0167

**Functional Description**

In case of pre-lodged declaration, the Authorisation should be still valid until the PRESENTATION<br>
NOTIFICATION FOR THE PRE-LODGED DECLARATION message (CC170C) is submitted when it<br>
will be revalidated.

**Technical Description**

N/A


## G0186

**Functional Description**

&lt;UNLOADING REMARK.Unloading completion&gt; is used as a flag and it can contain 2 possible values:<br>
'0' = 'NO' This means that the unloading of the goods is not yet completed;<br>
'1' = 'YES' This means that the goods are completely unloaded.

**Technical Description**

N/A


## G0196

**Functional Description**

This data group must contain the full transport equipment details and not only what is different<br>
compared to the data declared in the customs declaration.

**Technical Description**

N/A


## G0201

**Functional Description**

Rule R0840 shall be validated only by MS. IF the sender is a CTC country THEN the &lt;CUSTOMS<br>
OFFICE OF TRANSIT&gt; in MS, that detects the violation of R0840, should request a new ENS<br>
declaration before it authorizes the goods to enter the EU. The message IE050 or IE115 from a CTC<br>
country may not be rejected if R0840 is violated.

**Technical Description**

N/A


## G0205

**Functional Description**

&lt;UNLOADING REMARK.Conform&gt; is used as a flag and it can contain 2 possible values:<br>
'0' = 'NO' there are unloading remarks;<br>
'1' = 'YES' no unloading remarks present.

**Technical Description**

N/A


## G0217

**Functional Description**

From the originally received IE, only the D.G./D.I. in error are transmitted back to the Trader, indicating<br>
whether the D.G./D.I. in question is (are) missing or incorrect.

**Technical Description**

N/A


## G0300

**Functional Description**

The UN Number must be present if the commodity includes dangerous goods that are listed in the<br>
United Nations Dangerous Goods Code (UNDG).

**Technical Description**

N/A


## G0301

**Functional Description**

The Data Item &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-<br>
COMMODITY.CUS code&gt; can be used when the CL016 (CUSCode) in CS/RD2 includes [CUS code &<br>
CN code] where the CN code matches with the &lt;CONSIGNMENT-HOUSE CONSIGNMENT-<br>
CONSIGNMENT ITEM-COMMODITY-COMMODITY CODE. Harmonized System sub-heading code&gt;<br>
& &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY<br>
CODE.Combined nomenclature code&gt;.

**Technical Description**

N/A


## G0321

**Functional Description**

This Data Item can take the value '0' (zero) in the following cases:<br>
a. a document number is missing (i.e. it shall not be filled in with a dummy number);<br>
b. the length of a document number exceeds the allowed 70 characters (i.e. it shall not be truncated).<br>
A missing document reference number (due to the above or any other case) is not a valid reason for<br>
the rejection of this message.

**Technical Description**

N/A


## G0332

**Functional Description**

IF &lt;Container indicator&gt; is NOT PRESENT then data group &lt;TRANSPORT EQUIPMENT&gt; shall NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;be PRESENT, too. &lt;Container indicator&gt; functions as the governing data item for data group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSPORT EQUIPMENT&gt;.

**Technical Description**

N/A


## G0360

**Functional Description**

IF discrepancies have been found in one or more Data Groups or Data Items<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;a new data element has been found during the control<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the D.G. / D.I.= "R" and is used to report these discrepancies<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the D.G. / D.I.&nbsp;=&nbsp;"N".

**Technical Description**

N/A


## G0414

**Functional Description**

In case of excise goods where &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT<br>
ITEM.SUPPORTING DOCUMENT.Type&gt; is EQUAL to 'C651 -AAD -Administrative Accompanying<br>
Document (EMCS)', the Administrative Reference Code (ARC number) shall be recorded in this field;<br>
In case of excise goods where &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT<br>
ITEM.SUPPORTING DOCUMENT.Type&gt; is EQUAL to 'C658 -FAD -Fallback e-AD (EMCS)', the<br>
national Fallback registration number shall be recorded in this field.

**Technical Description**

N/A


## G0424

**Functional Description**

In case of excise goods where &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT<br>
ITEM.ADDITIONAL REFERENCE.Type&gt; is EQUAL to 'C651 -AAD -Administrative Accompanying<br>
Document (EMCS)', the<br>
Administrative Reference Code (ARC number) shall be recorded in this field;<br>
In case of excise goods where &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT<br>
ITEM.ADDITIONAL REFERENCE.Type&gt; is EQUAL to 'C658C -FAD -Fallback e-AD (EMCS)’, the<br>
national Fallback registration number shall be recorded in this field.

**Technical Description**

N/A


## G0500

**Functional Description**

The exact content of the CL326 (QualifierOfTheIdentification) is defined nationally, considering -for<br>
example -that only in some NAs the value 'T' must only be used in case “House number” and<br>
“Postcode” or only “Postcode” define an exact and unique location.

**Technical Description**

N/A


## G0510

**Functional Description**

When the &lt;CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; indicates the permission to start the<br>
unloading, all the information about the Consignment is provided.<br>
When the &lt;CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; indicates the permission to continue<br>
the unloading, the information about the Consignment is not provided, and the Data Item<br>
&lt;CTL_CONTROL.Continue unloading&gt; shall be used with an incremental value ('1', '2', '3', etc ...) in<br>
the subsequent messages CC043C (one message for each authorisation to continue the unloading).

**Technical Description**

N/A


## G0587

**Functional Description**

The Customs Office of Exit for Transit shall be provided - in case of transit declaration combined with<br>
EXS - when the goods will exit the Security Area to enter (or re-enter) a CTC country that is not in the<br>
Security Area.

**Technical Description**

N/A


## G0670

**Functional Description**

If all goods items are related a single container, the data group can be omitted.<br>
Otherwise all the goods items related to this container (if present) must be declared.<br>
All the non-containerised goods items related to this seals information (if present) must be declared as<br>
well.

**Technical Description**

N/A


## G0789

**Functional Description**

The ’Customs office at border reference number’ identifies the border crossing point (BCP) where the<br>
‘Active border transport means’ will be present. It is either the ‘Reference number’ of one of the<br>
‘CUSTOMS OFFICE OF TRANSIT (DECLARED)’ or the ‘Reference number’ of one of the ‘CUSTOMS<br>
OFFICE OF EXIT FOR TRANSIT (DECLARED)’ or the ‘Reference number’ of the ‘CUSTOMS OFFICE<br>
OF DESTINATION (DECLARED)’. By using this Data Item, it is possible (after the end of the NCTS-<br>
P4/NCTS-P5 Transitional Period) to identify which transport means will be present at which border<br>
crossing point, in case of multiple BCP and multiple changes of active transport means.

**Technical Description**

N/A


## G0825

**Functional Description**

- Consignment related information shall be recorded under<br>
&lt;CONSIGNMENT-ADDITIONAL SUPPLY CHAIN ACTOR&gt;<br>
&lt;CONSIGNMENT-PREVIOUS DOCUMENT&gt;<br>
&lt;CONSIGNMENT-SUPPORTING DOCUMENT&gt;<br>
&lt;CONSIGNMENT-TRANSPORT DOCUMENT&gt;<br>
&lt;CONSIGNMENT-ADDITIONAL REFERENCE&gt;<br>
&lt;CONSIGNMENT-ADDITIONAL INFORMATION&gt;<br>
- House Consignment related information shall be recorded under+<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT- ADDITIONAL SUPPLY CHAIN ACTOR&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-SUPPORTING DOCUMENT&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT DOCUMENT&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-ADDITIONAL REFERENCE&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-ADDITIONAL INFORMATION&gt;<br>
- Goods item related information shall be recorded under<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL SUPPLY CHAIN<br>
ACTOR&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS DOCUMENT&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-SUPPORTING DOCUMENT&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL REFERENCE&gt;<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL INFORMATION&gt;

**Technical Description**

N/A


## G0850

**Functional Description**

This Data Group must be filled in if a &lt;REPRESENTATIVE&gt; is used by the &lt;HOLDER OF THE<br>
TRANSIT PROCEDURE&gt;.

**Technical Description**

N/A


## G0860

**Functional Description**

This Data Group must be filled in if the Data Group &lt;REPRESENTATIVE&gt; was used in the preceding<br>
message that was received by the &lt;CUSTOMS OFFICE OF DEPARTURE&gt;.

**Technical Description**

N/A


## G0868

**Functional Description**

The data recorded under this data group must be exactly the same as in the respective data group of<br>
the preceding message that is received.

**Technical Description**

N/A


## G0988

**Functional Description**

The Country of dispatch can be different from the Country defined in the address of the Consignor.

**Technical Description**

N/A

## G0989

**Functional Description**

This Data Group is inserted as transitional but without any transitional measure applied to it. The Data<br>
Group is present in this message, in order to ensure consistency of the structure across the lifecycle of<br>
the movements during the NCTS-P4/NCTS-P5 Transitional Period.<br>
This Guideline aims to draw the attention on the potential need for Technical Rules for Transition<br>
(Exxxx) or Business Rules for Transition (B1xxx and B2xxx) as defined in the section “1. Introduction”<br>
of DDNTA APPENDIX Q2.

**Technical Description**

N/A
