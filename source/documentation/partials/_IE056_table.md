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
</tr><tr class="parent-row" data-level="IE056_0" >
    <td><span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE056_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;LRN</td>
    <td>D</td>
    <td>an..22</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0467.html">C0467</a></td>
</tr><tr data-parent="IE056_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;MRN</td>
    <td>D</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0467.html">C0467</a><br /><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE056_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Business rejection type</td>
    <td>R</td>
    <td>an3</td>
    <td>CL560</td>
    <td><a href="../phase-6-rules/R0852.html">R0852</a></td>
</tr><tr data-parent="IE056_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Rejection date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE056_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Rejection code</td>
    <td>R</td>
    <td>n..2</td>
    <td>CL226</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE056_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Rejection reason</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0495.html">C0495</a></td>
</tr><tr class="parent-row" data-level="IE056_1" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE056_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE056_2" >
    <td><span class="toggle-icon">▾</span> <strong> HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0868.html">G0868</a></td>
</tr><tr data-parent="IE056_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0120.html">G0120</a><br /><a href="../phase-6-rules/R0850.html">R0850</a></td>
</tr><tr data-parent="IE056_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;TIR holder identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE056_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr class="parent-row" data-level="IE056_3" data-parent="IE056_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr data-parent="IE056_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE056_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0505.html">C0505</a></td>
</tr><tr data-parent="IE056_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE056_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE056_4" >
    <td><span class="toggle-icon">▾</span> <strong> REPRESENTATIVE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0860.html">G0860</a></td>
</tr><tr data-parent="IE056_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0850.html">R0850</a></td>
</tr><tr data-parent="IE056_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Status</td>
    <td>R</td>
    <td>n1</td>
    <td>CL094</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE056_5" >
    <td><span class="toggle-icon">▾</span> <strong> FUNCTIONAL ERROR</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0217.html">G0217</a></td>
</tr><tr data-parent="IE056_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Error pointer</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0009.html">G0009</a></td>
</tr><tr data-parent="IE056_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Error code</td>
    <td>R</td>
    <td>n2</td>
    <td>CL437</td>
    <td><a href="../phase-6-rules/R0437.html">R0437</a></td>
</tr><tr data-parent="IE056_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Error reason</td>
    <td>R</td>
    <td>an..7</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0010.html">G0010</a></td>
</tr><tr data-parent="IE056_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Original attribute value</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>