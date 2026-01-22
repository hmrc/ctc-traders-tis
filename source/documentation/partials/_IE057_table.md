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
</tr><tr class="parent-row" data-level="IE057_0" >
    <td><span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE057_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE057_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Business rejection type</td>
    <td>R</td>
    <td>an3</td>
    <td>CL560</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE057_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Rejection date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE057_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Rejection code</td>
    <td>R</td>
    <td>n..2</td>
    <td>CL227</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE057_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Rejection reason</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#c0492">C0492</a></td>
</tr><tr class="parent-row" data-level="IE057_1" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE057_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE057_2" >
    <td><span class="toggle-icon">▾</span> <strong> TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0868">G0868</a></td>
</tr><tr data-parent="IE057_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#r0850">R0850</a></td>
</tr><tr class="parent-row" data-level="IE057_3" >
    <td><span class="toggle-icon">▾</span> <strong> FUNCTIONAL ERROR</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0217">G0217</a></td>
</tr><tr data-parent="IE057_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Error pointer</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0009">G0009</a></td>
</tr><tr data-parent="IE057_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Error code</td>
    <td>R</td>
    <td>n2</td>
    <td>CL180</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE057_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Error reason</td>
    <td>R</td>
    <td>an..7</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules.html#g0010">G0010</a></td>
</tr><tr data-parent="IE057_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Original attribute value</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>