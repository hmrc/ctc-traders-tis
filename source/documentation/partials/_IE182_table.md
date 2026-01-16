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
<tr class="parent-row" data-level="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong>MESSAGE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message sender</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message recipient</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message type</td>
    <td>R</td>
    <td>an6</td>
    <td>CL060</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0511">C0511</a><br /><a href="phase-6-rules.html#r0008">R0008</a></td>
</tr><tr class="parent-row" data-level="IE182_1" data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE182_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Incident notification date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE182_2" data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE182_3" data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF INCIDENT REGISTRATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL141</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE182_4" data-parent="IE182_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE182_5" data-parent="IE182_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> INCIDENT</strong></td>
    <td>R</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE182_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>n1</td>
    <td>CL019</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE182_6" data-parent="IE182_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ENDORSEMENT</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE182_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Place</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL009</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE182_7" data-parent="IE182_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> LOCATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td>CL038</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td>CL244</td>
    <td><a href="phase-6-rules.html#c0460">C0460</a></td>
</tr><tr data-parent="IE182_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL009</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE182_8" data-parent="IE182_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0460">C0460</a></td>
</tr><tr data-parent="IE182_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr data-parent="IE182_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr class="parent-row" data-level="IE182_9" data-parent="IE182_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0460">C0460</a></td>
</tr><tr data-parent="IE182_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE182_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE182_10" data-parent="IE182_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#s1023">S1023</a><br /><a href="phase-6-rules.html#c0040">C0040</a><br /><a href="phase-6-rules.html#c0240">C0240</a><br /><a href="phase-6-rules.html#g0103">G0103</a></td>
</tr><tr data-parent="IE182_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE182_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0820">C0820</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0016">G0016</a></td>
</tr><tr data-parent="IE182_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of seals</td>
    <td>D</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0396">C0396</a><br /><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0023">G0023</a><br /><a href="phase-6-rules.html#r0106">R0106</a></td>
</tr><tr class="parent-row" data-level="IE182_11" data-parent="IE182_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0569">C0569</a></td>
</tr><tr data-parent="IE182_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE182_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0023">G0023</a><br /><a href="phase-6-rules.html#r0107">R0107</a></td>
</tr><tr class="parent-row" data-level="IE182_12" data-parent="IE182_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS REFERENCE</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0670">G0670</a></td>
</tr><tr data-parent="IE182_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE182_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#g0006">G0006</a></td>
</tr><tr class="parent-row" data-level="IE182_13" data-parent="IE182_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSHIPMENT</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0240">C0240</a></td>
</tr><tr data-parent="IE182_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container indicator</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#g0029">G0029</a></td>
</tr><tr class="parent-row" data-level="IE182_14" data-parent="IE182_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT MEANS</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE182_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#g0023">G0023</a></td>
</tr><tr data-parent="IE182_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0023">G0023</a></td>
</tr><tr data-parent="IE182_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td><a href="phase-6-rules.html#g0023">G0023</a></td>
</tr></table>

