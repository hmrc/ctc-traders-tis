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
<tr class="parent-row" data-level="IE013_0" >
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong>MESSAGE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message sender</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message recipient</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message type</td>
    <td>R</td>
    <td>an6</td>
    <td>CL060</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0511">C0511</a><br /><a href="phase-6-rules.html#r0008">R0008</a></td>
</tr><tr class="parent-row" data-level="IE013_1" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LRN</td>
    <td>D</td>
    <td>an..22</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0467">C0467</a></td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MRN</td>
    <td>D</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0467">C0467</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration type</td>
    <td>R</td>
    <td>an..5</td>
    <td>CL231</td>
    <td><a href="phase-6-rules.html#r0601">R0601</a><br /><a href="phase-6-rules.html#r0909">R0909</a><br /><a href="phase-6-rules.html#r0911">R0911</a></td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Additional declaration type</td>
    <td>R</td>
    <td>a1</td>
    <td>CL042</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TIR Carnet number</td>
    <td>D</td>
    <td>an..12</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0411">C0411</a><br /><a href="phase-6-rules.html#r0990">R0990</a></td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Presentation of the goods date and time</td>
    <td>O</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Security</td>
    <td>R</td>
    <td>n1</td>
    <td>CL217</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduced dataset indicator</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#r0849">R0849</a></td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Specific circumstance indicator</td>
    <td>O</td>
    <td>an3</td>
    <td>CL296</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Communication language at departure</td>
    <td>O</td>
    <td>a2</td>
    <td>CL192</td>
    <td><a href="phase-6-rules.html#g0100">G0100</a></td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Binding itinerary</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amendment type flag</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#r0520">R0520</a></td>
</tr><tr data-parent="IE013_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Limit date</td>
    <td>D</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0839">C0839</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE013_2" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> AUTHORISATION</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0101">C0101</a><br /><a href="phase-6-rules.html#g0102">G0102</a><br /><a href="phase-6-rules.html#g0167">G0167</a></td>
</tr><tr data-parent="IE013_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an..4</td>
    <td>CL235</td>
    <td><a href="phase-6-rules.html#g0114">G0114</a><br /><a href="phase-6-rules.html#g0117">G0117</a><br /><a href="phase-6-rules.html#r0350">R0350</a><br /><a href="phase-6-rules.html#r0859">R0859</a></td>
</tr><tr data-parent="IE013_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0033">G0033</a><br /><a href="phase-6-rules.html#r0352">R0352</a></td>
</tr><tr class="parent-row" data-level="IE013_3" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td><a href="phase-6-rules.html#r0901">R0901</a></td>
</tr><tr class="parent-row" data-level="IE013_4" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DESTINATION (DECLARED)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0034">G0034</a></td>
</tr><tr data-parent="IE013_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td><a href="phase-6-rules.html#r0901">R0901</a><br /><a href="phase-6-rules.html#r0904">R0904</a><br /><a href="phase-6-rules.html#r0905">R0905</a></td>
</tr><tr class="parent-row" data-level="IE013_5" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF TRANSIT (DECLARED)</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0030">C0030</a><br /><a href="phase-6-rules.html#g0030">G0030</a></td>
</tr><tr data-parent="IE013_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL173</td>
    <td><a href="phase-6-rules.html#g0142">G0142</a><br /><a href="phase-6-rules.html#r0003">R0003</a><br /><a href="phase-6-rules.html#r0006">R0006</a><br /><a href="phase-6-rules.html#r0906">R0906</a></td>
</tr><tr data-parent="IE013_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arrival date and time (estimated)</td>
    <td>D</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0598">C0598</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#r0005">R0005</a></td>
</tr><tr class="parent-row" data-level="IE013_6" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0587">C0587</a><br /><a href="phase-6-rules.html#g0587">G0587</a></td>
</tr><tr data-parent="IE013_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL175</td>
    <td><a href="phase-6-rules.html#r0103">R0103</a></td>
</tr><tr class="parent-row" data-level="IE013_7" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0120">G0120</a><br /><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE013_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0904">C0904</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE013_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE013_8" data-parent="IE013_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE013_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE013_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_9" data-parent="IE013_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr data-parent="IE013_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE013_10" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> REPRESENTATIVE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0850">G0850</a></td>
</tr><tr data-parent="IE013_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE013_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Status</td>
    <td>R</td>
    <td>n1</td>
    <td>CL094</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_11" data-parent="IE013_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr data-parent="IE013_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE013_12" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GUARANTEE</strong></td>
    <td>R</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Guarantee type</td>
    <td>R</td>
    <td>an1</td>
    <td>CL251</td>
    <td><a href="phase-6-rules.html#r0900">R0900</a></td>
</tr><tr data-parent="IE013_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Other guarantee reference</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0130">C0130</a></td>
</tr><tr class="parent-row" data-level="IE013_13" data-parent="IE013_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GUARANTEE REFERENCE</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0085">C0085</a></td>
</tr><tr data-parent="IE013_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GRN</td>
    <td>D</td>
    <td>an..24</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0086">C0086</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#r0318">R0318</a></td>
</tr><tr data-parent="IE013_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Access code</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0086">C0086</a></td>
</tr><tr data-parent="IE013_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amount to be covered</td>
    <td>R</td>
    <td>n..16,2</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a></td>
</tr><tr data-parent="IE013_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Currency</td>
    <td>R</td>
    <td>a3</td>
    <td>CL048</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_14" data-parent="IE013_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0909">C0909</a><br /><a href="phase-6-rules.html#g0988">G0988</a></td>
</tr><tr data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0343">C0343</a><br /><a href="phase-6-rules.html#g0113">G0113</a></td>
</tr><tr data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container indicator</td>
    <td>D</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#c0822">C0822</a><br /><a href="phase-6-rules.html#g0332">G0332</a></td>
</tr><tr data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Inland mode of transport</td>
    <td>O</td>
    <td>n1</td>
    <td>CL218</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mode of transport at the border</td>
    <td>D</td>
    <td>n1</td>
    <td>CL218</td>
    <td><a href="phase-6-rules.html#c0599">C0599</a><br /><a href="phase-6-rules.html#g0020">G0020</a><br /><a href="phase-6-rules.html#g0115">G0115</a></td>
</tr><tr data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0994">R0994</a></td>
</tr><tr data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0502">C0502</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE013_15" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CARRIER</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0090">G0090</a></td>
</tr><tr data-parent="IE013_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0201">G0201</a><br /><a href="phase-6-rules.html#r0840">R0840</a></td>
</tr><tr class="parent-row" data-level="IE013_16" data-parent="IE013_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr data-parent="IE013_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE013_17" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0542">C0542</a><br /><a href="phase-6-rules.html#g0123">G0123</a></td>
</tr><tr data-parent="IE013_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE013_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE013_18" data-parent="IE013_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE013_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE013_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_19" data-parent="IE013_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr data-parent="IE013_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE013_20" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0001">C0001</a><br /><a href="phase-6-rules.html#g0001">G0001</a></td>
</tr><tr data-parent="IE013_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0851">R0851</a></td>
</tr><tr data-parent="IE013_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE013_21" data-parent="IE013_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE013_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE013_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_22" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Role</td>
    <td>R</td>
    <td>a..3</td>
    <td>CL704</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0201">G0201</a><br /><a href="phase-6-rules.html#r0840">R0840</a></td>
</tr><tr class="parent-row" data-level="IE013_23" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0823">C0823</a><br /><a href="phase-6-rules.html#g0103">G0103</a></td>
</tr><tr data-parent="IE013_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0055">C0055</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE013_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of seals</td>
    <td>R</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#r0106">R0106</a><br /><a href="phase-6-rules.html#r0165">R0165</a><br /><a href="phase-6-rules.html#r0448">R0448</a></td>
</tr><tr class="parent-row" data-level="IE013_24" data-parent="IE013_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0569">C0569</a></td>
</tr><tr data-parent="IE013_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0107">R0107</a></td>
</tr><tr class="parent-row" data-level="IE013_25" data-parent="IE013_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS REFERENCE</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0670">C0670</a><br /><a href="phase-6-rules.html#g0670">G0670</a></td>
</tr><tr data-parent="IE013_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#g0006">G0006</a></td>
</tr><tr class="parent-row" data-level="IE013_26" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> LOCATION OF GOODS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0710">C0710</a></td>
</tr><tr data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of location</td>
    <td>R</td>
    <td>a1</td>
    <td>CL347</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td>CL326</td>
    <td><a href="phase-6-rules.html#g0500">G0500</a></td>
</tr><tr data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authorisation number</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Additional identifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0671">C0671</a></td>
</tr><tr data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td>CL244</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr class="parent-row" data-level="IE013_27" data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE013_27">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_28" data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE013_28">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr data-parent="IE013_28">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr class="parent-row" data-level="IE013_29" data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ECONOMIC OPERATOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE013_29">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr class="parent-row" data-level="IE013_30" data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE013_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE013_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL009</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_31" data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> POSTCODE ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE013_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;House number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0382">C0382</a></td>
</tr><tr data-parent="IE013_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL190</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_32" data-parent="IE013_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a><br /><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr data-parent="IE013_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE013_33" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0826">C0826</a><br /><a href="phase-6-rules.html#g0088">G0088</a><br /><a href="phase-6-rules.html#g0119">G0119</a><br /><a href="phase-6-rules.html#r0855">R0855</a></td>
</tr><tr data-parent="IE013_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#g0112">G0112</a><br /><a href="phase-6-rules.html#r0472">R0472</a><br /><a href="phase-6-rules.html#r0474">R0474</a><br /><a href="phase-6-rules.html#r0476">R0476</a></td>
</tr><tr data-parent="IE013_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0473">R0473</a></td>
</tr><tr data-parent="IE013_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_34" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COUNTRY OF ROUTING OF CONSIGNMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0586">C0586</a><br /><a href="phase-6-rules.html#g0061">G0061</a></td>
</tr><tr data-parent="IE013_34">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_34">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL008</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_35" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ACTIVE BORDER TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0806">C0806</a><br /><a href="phase-6-rules.html#g0118">G0118</a><br /><a href="phase-6-rules.html#r0789">R0789</a></td>
</tr><tr data-parent="IE013_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Customs office at border reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL141</td>
    <td><a href="phase-6-rules.html#g0789">G0789</a></td>
</tr><tr data-parent="IE013_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL219</td>
    <td><a href="phase-6-rules.html#g0112">G0112</a></td>
</tr><tr data-parent="IE013_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0076">R0076</a></td>
</tr><tr data-parent="IE013_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conveyance reference number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0531">C0531</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#r0315">R0315</a></td>
</tr><tr class="parent-row" data-level="IE013_36" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PLACE OF LOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0409">C0409</a></td>
</tr><tr data-parent="IE013_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td>CL244</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0387">C0387</a></td>
</tr><tr data-parent="IE013_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0387">C0387</a></td>
</tr><tr class="parent-row" data-level="IE013_37" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PLACE OF UNLOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0191">C0191</a></td>
</tr><tr data-parent="IE013_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td>CL244</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0387">C0387</a></td>
</tr><tr data-parent="IE013_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0387">C0387</a></td>
</tr><tr class="parent-row" data-level="IE013_38" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL214</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r0020">R0020</a></td>
</tr><tr data-parent="IE013_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE013_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_39" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE013_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE013_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_40" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE013_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE013_41" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE013_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE013_42" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r3060">R3060</a></td>
</tr><tr data-parent="IE013_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_43" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT CHARGES</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0186">C0186</a></td>
</tr><tr data-parent="IE013_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td>CL116</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_44" data-parent="IE013_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0909">C0909</a><br /><a href="phase-6-rules.html#g0988">G0988</a><br /><a href="phase-6-rules.html#r0506">R0506</a></td>
</tr><tr data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0343">C0343</a><br /><a href="phase-6-rules.html#g0062">G0062</a><br /><a href="phase-6-rules.html#g0113">G0113</a><br /><a href="phase-6-rules.html#r0506">R0506</a></td>
</tr><tr data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0983">R0983</a></td>
</tr><tr data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0502">C0502</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#r0506">R0506</a></td>
</tr><tr class="parent-row" data-level="IE013_45" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0542">C0542</a><br /><a href="phase-6-rules.html#g0123">G0123</a><br /><a href="phase-6-rules.html#r0506">R0506</a></td>
</tr><tr data-parent="IE013_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE013_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE013_46" data-parent="IE013_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE013_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE013_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_47" data-parent="IE013_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr data-parent="IE013_47">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_47">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_47">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE013_48" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0001">C0001</a><br /><a href="phase-6-rules.html#g0001">G0001</a><br /><a href="phase-6-rules.html#r0506">R0506</a></td>
</tr><tr data-parent="IE013_48">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0851">R0851</a></td>
</tr><tr data-parent="IE013_48">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE013_49" data-parent="IE013_48">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE013_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE013_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_50" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Role</td>
    <td>R</td>
    <td>a..3</td>
    <td>CL704</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0201">G0201</a><br /><a href="phase-6-rules.html#r0840">R0840</a></td>
</tr><tr class="parent-row" data-level="IE013_51" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0826">C0826</a><br /><a href="phase-6-rules.html#g0088">G0088</a><br /><a href="phase-6-rules.html#g0119">G0119</a><br /><a href="phase-6-rules.html#r0506">R0506</a><br /><a href="phase-6-rules.html#r0855">R0855</a></td>
</tr><tr data-parent="IE013_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#g0112">G0112</a><br /><a href="phase-6-rules.html#r0472">R0472</a><br /><a href="phase-6-rules.html#r0474">R0474</a><br /><a href="phase-6-rules.html#r0476">R0476</a></td>
</tr><tr data-parent="IE013_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0473">R0473</a></td>
</tr><tr data-parent="IE013_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_52" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0026">G0026</a></td>
</tr><tr data-parent="IE013_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL228</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0416">R0416</a></td>
</tr><tr data-parent="IE013_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_53" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE013_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE013_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_54" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE013_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE013_55" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE013_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE013_56" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_56">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_56">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r3062">R3062</a></td>
</tr><tr data-parent="IE013_56">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_57" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT CHARGES</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0186">C0186</a><br /><a href="phase-6-rules.html#c0337">C0337</a><br /><a href="phase-6-rules.html#r0506">R0506</a></td>
</tr><tr data-parent="IE013_57">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td>CL116</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_58" data-parent="IE013_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT ITEM</strong></td>
    <td>R</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0071">G0071</a></td>
</tr><tr data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0072">G0072</a><br /><a href="phase-6-rules.html#r0988">R0988</a></td>
</tr><tr data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#r0007">R0007</a></td>
</tr><tr data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration type</td>
    <td>D</td>
    <td>an..5</td>
    <td>CL232</td>
    <td><a href="phase-6-rules.html#c0045">C0045</a><br /><a href="phase-6-rules.html#r0507">R0507</a><br /><a href="phase-6-rules.html#r0601">R0601</a><br /><a href="phase-6-rules.html#r0909">R0909</a></td>
</tr><tr data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0909">C0909</a><br /><a href="phase-6-rules.html#g0988">G0988</a><br /><a href="phase-6-rules.html#r0507">R0507</a></td>
</tr><tr data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0343">C0343</a><br /><a href="phase-6-rules.html#g0113">G0113</a><br /><a href="phase-6-rules.html#r0507">R0507</a></td>
</tr><tr data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0502">C0502</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#r0507">R0507</a></td>
</tr><tr class="parent-row" data-level="IE013_59" data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_59">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_59">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Role</td>
    <td>R</td>
    <td>a..3</td>
    <td>CL704</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_59">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0201">G0201</a><br /><a href="phase-6-rules.html#r0840">R0840</a></td>
</tr><tr class="parent-row" data-level="IE013_60" data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description of goods</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td>CL016</td>
    <td><a href="phase-6-rules.html#g0301">G0301</a></td>
</tr><tr class="parent-row" data-level="IE013_61" data-parent="IE013_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY CODE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0153">C0153</a></td>
</tr><tr data-parent="IE013_61">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td>CL152</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_61">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combined nomenclature code</td>
    <td>D</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0821">C0821</a><br /><a href="phase-6-rules.html#r0060">R0060</a></td>
</tr><tr class="parent-row" data-level="IE013_62" data-parent="IE013_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DANGEROUS GOODS</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0300">G0300</a></td>
</tr><tr data-parent="IE013_62">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_62">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN Number</td>
    <td>R</td>
    <td>an4</td>
    <td>CL101</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_63" data-parent="IE013_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS MEASURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_63">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#r0221">R0221</a></td>
</tr><tr data-parent="IE013_63">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Net mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0837">C0837</a><br /><a href="phase-6-rules.html#r0223">R0223</a></td>
</tr><tr data-parent="IE013_63">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Supplementary units</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_64" data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PACKAGING</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_64">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_64">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of packages</td>
    <td>R</td>
    <td>an2</td>
    <td>CL017</td>
    <td><a href="phase-6-rules.html#r0220">R0220</a></td>
</tr><tr data-parent="IE013_64">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of packages</td>
    <td>D</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0060">C0060</a><br /><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#r0219">R0219</a><br /><a href="phase-6-rules.html#r0364">R0364</a></td>
</tr><tr data-parent="IE013_64">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shipping marks</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0060">C0060</a><br /><a href="phase-6-rules.html#g0024">G0024</a></td>
</tr><tr class="parent-row" data-level="IE013_65" data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0035">C0035</a><br /><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL214</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r0020">R0020</a></td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goods item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0058">G0058</a></td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of packages</td>
    <td>O</td>
    <td>an2</td>
    <td>CL017</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of packages</td>
    <td>O</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Measurement unit and qualifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>CL349</td>
    <td><a href="phase-6-rules.html#c0298">C0298</a></td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quantity</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_66" data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0069">G0069</a><br /><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE013_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0414">G0414</a></td>
</tr><tr data-parent="IE013_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE013_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE013_67" data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0068">G0068</a><br /><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_67">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_67">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE013_67">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0015">C0015</a><br /><a href="phase-6-rules.html#g0050">G0050</a><br /><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0424">G0424</a><br /><a href="phase-6-rules.html#r0023">R0023</a></td>
</tr><tr class="parent-row" data-level="IE013_68" data-parent="IE013_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE013_68">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE013_68">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r3061">R3061</a></td>
</tr><tr data-parent="IE013_68">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>