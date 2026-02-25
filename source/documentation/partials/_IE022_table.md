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
    <td><a href="../phase-6-rules.html#g0002">G0002</a></td>
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
    <td><a href="../phase-6-rules.html#c0511">C0511</a><br /><a href="../phase-6-rules.html#r0008">R0008</a></td>
</tr><tr class="parent-row" data-level="IE022_0" >
    <td><span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE022_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE022_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Amendment notification date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE022_1" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE022_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE022_2" >
    <td><span class="toggle-icon">▾</span> <strong> HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE022_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0120">G0120</a><br /><a href="../phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE022_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#c0904">C0904</a><br /><a href="../phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE022_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE022_3" data-parent="IE022_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE022_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- -  Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE022_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- -  Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE022_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- -  City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE022_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- -  Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE022_4" >
    <td><span class="toggle-icon">▾</span> <strong> FUNCTIONAL ERROR</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0217">G0217</a></td>
</tr><tr data-parent="IE022_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE022_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Error pointer</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE022_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Error code</td>
    <td>R</td>
    <td>n2</td>
    <td>CL180</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE022_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Error reason</td>
    <td>O</td>
    <td>an..7</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE022_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-  Original attribute value</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>