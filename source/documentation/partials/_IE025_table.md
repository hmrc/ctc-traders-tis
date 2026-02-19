<table cellspacing="0" style="table-layout: fixed; width: 100%;">
<colgroup>
    <col style="width: 40%;">
    <col style="width: 10%;">
    <col style="width: 20%;">
    <col style="width: 15%;">
    <col style="width: 15%;">
</colgroup>
<tr>
<th>
   Field Name
  </th>
<th>
   Priority
  </th>
<th>
   Format / Max Repeat
  </th>
<th>
   Code Lists
  </th>
<th>
   Rules
  </th>
</tr>
<tr>
    <td>Message sender</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>Message recipient</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr>
    <td>Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>Message type</td>
    <td>R</td>
    <td>an6</td>
    <td>CL060</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0511.html">C0511</a><br /><a href="../phase-6-rules/R0008.html">R0008</a></td>
</tr><tr class="parent-row" data-level="IE025_0" >
    <td><span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE025_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE025_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Release date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE025_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Release indicator</td>
    <td>R</td>
    <td>n1</td>
    <td>CL164</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE025_1" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE025_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE025_2" >
    <td><span class="toggle-icon">▾</span> <strong> TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE025_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0850.html">R0850</a></td>
</tr><tr class="parent-row" data-level="IE025_3" >
    <td><span class="toggle-icon">▾</span> <strong> CONSIGNMENT</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0352.html">C0352</a></td>
</tr><tr class="parent-row" data-level="IE025_4" data-parent="IE025_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE025_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0054.html">R0054</a></td>
</tr><tr data-parent="IE025_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Release type</td>
    <td>R</td>
    <td>n1</td>
    <td>CL163</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE025_5" data-parent="IE025_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT ITEM</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0353.html">C0353</a></td>
</tr><tr data-parent="IE025_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0055.html">R0055</a></td>
</tr><tr data-parent="IE025_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0005.html">G0005</a><br /><a href="../phase-6-rules/R0055.html">R0055</a></td>
</tr><tr data-parent="IE025_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Release type</td>
    <td>R</td>
    <td>n1</td>
    <td>CL163</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE025_6" data-parent="IE025_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0131.html">G0131</a></td>
</tr><tr data-parent="IE025_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description of goods</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE025_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td>CL016</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE025_7" data-parent="IE025_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY CODE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE025_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td>CL152</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE025_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combined nomenclature code</td>
    <td>O</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0060.html">R0060</a></td>
</tr><tr class="parent-row" data-level="IE025_8" data-parent="IE025_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DANGEROUS GOODS</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0300.html">G0300</a></td>
</tr><tr data-parent="IE025_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0054.html">R0054</a></td>
</tr><tr data-parent="IE025_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN Number</td>
    <td>R</td>
    <td>an4</td>
    <td>CL101</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE025_9" data-parent="IE025_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS MEASURE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE025_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0021.html">G0021</a><br /><a href="../phase-6-rules/R0221.html">R0221</a></td>
</tr><tr data-parent="IE025_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Net mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0844.html">C0844</a><br /><a href="../phase-6-rules/R0223.html">R0223</a></td>
</tr><tr class="parent-row" data-level="IE025_10" data-parent="IE025_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PACKAGING</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0131.html">G0131</a></td>
</tr><tr data-parent="IE025_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0054.html">R0054</a></td>
</tr><tr data-parent="IE025_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of packages</td>
    <td>R</td>
    <td>an2</td>
    <td>CL017</td>
    <td><a href="../phase-6-rules/R0220.html">R0220</a></td>
</tr><tr data-parent="IE025_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of packages</td>
    <td>D</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0060.html">C0060</a><br /><a href="../phase-6-rules/G0021.html">G0021</a><br /><a href="../phase-6-rules/R0219.html">R0219</a><br /><a href="../phase-6-rules/R0364.html">R0364</a></td>
</tr><tr data-parent="IE025_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shipping marks</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0060.html">C0060</a><br /><a href="../phase-6-rules/G0024.html">G0024</a></td>
</tr></table>