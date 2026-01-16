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
<tr class="parent-row" data-level="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong>MESSAGE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message sender</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message recipient</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message type</td>
    <td>R</td>
    <td>an6</td>
    <td>CL060</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0511">C0511</a><br /><a href="phase-6-rules.html#r0008">R0008</a></td>
</tr><tr class="parent-row" data-level="IE043_1" data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE043_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration type</td>
    <td>D</td>
    <td>an..5</td>
    <td>CL231</td>
    <td><a href="phase-6-rules.html#c0027">C0027</a><br /><a href="phase-6-rules.html#r0601">R0601</a><br /><a href="phase-6-rules.html#r0909">R0909</a><br /><a href="phase-6-rules.html#r0911">R0911</a></td>
</tr><tr data-parent="IE043_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration acceptance date</td>
    <td>D</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0027">C0027</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE043_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Security</td>
    <td>R</td>
    <td>n1</td>
    <td>CL217</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduced dataset indicator</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_2" data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_3" data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0027">C0027</a></td>
</tr><tr data-parent="IE043_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0120">G0120</a><br /><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE043_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0904">C0904</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE043_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_4" data-parent="IE043_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE043_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_5" data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr class="parent-row" data-level="IE043_6" data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CTL_CONTROL</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Continue unloading</td>
    <td>R</td>
    <td>n1</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0510">G0510</a></td>
</tr><tr class="parent-row" data-level="IE043_7" data-parent="IE043_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0027">C0027</a></td>
</tr><tr data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0343">C0343</a><br /><a href="phase-6-rules.html#g0113">G0113</a></td>
</tr><tr data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container indicator</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Inland mode of transport</td>
    <td>O</td>
    <td>n1</td>
    <td>CL218</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0027">C0027</a><br /><a href="phase-6-rules.html#r0994">R0994</a></td>
</tr><tr data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0502">C0502</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE043_8" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNOR</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE043_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE043_9" data-parent="IE043_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE043_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE043_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_10" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0003">C0003</a><br /><a href="phase-6-rules.html#g0001">G0001</a></td>
</tr><tr data-parent="IE043_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0851">R0851</a></td>
</tr><tr data-parent="IE043_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE043_11" data-parent="IE043_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE043_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE043_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_12" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0872">C0872</a><br /><a href="phase-6-rules.html#g0103">G0103</a></td>
</tr><tr data-parent="IE043_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0055">C0055</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE043_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of seals</td>
    <td>R</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0165">G0165</a><br /><a href="phase-6-rules.html#r0106">R0106</a><br /><a href="phase-6-rules.html#r0448">R0448</a></td>
</tr><tr class="parent-row" data-level="IE043_13" data-parent="IE043_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0569">C0569</a></td>
</tr><tr data-parent="IE043_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0107">R0107</a></td>
</tr><tr class="parent-row" data-level="IE043_14" data-parent="IE043_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS REFERENCE</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0670">C0670</a><br /><a href="phase-6-rules.html#g0670">G0670</a></td>
</tr><tr data-parent="IE043_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#g0006">G0006</a></td>
</tr><tr class="parent-row" data-level="IE043_15" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0339">C0339</a><br /><a href="phase-6-rules.html#r0855">R0855</a></td>
</tr><tr data-parent="IE043_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#r0472">R0472</a><br /><a href="phase-6-rules.html#r0474">R0474</a><br /><a href="phase-6-rules.html#r0476">R0476</a></td>
</tr><tr data-parent="IE043_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0473">R0473</a></td>
</tr><tr data-parent="IE043_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_16" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COUNTRY OF ROUTING OF CONSIGNMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0586">C0586</a><br /><a href="phase-6-rules.html#g0079">G0079</a></td>
</tr><tr data-parent="IE043_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL008</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_17" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL214</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r0020">R0020</a><br /><a href="phase-6-rules.html#r0093">R0093</a></td>
</tr><tr data-parent="IE043_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE043_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_18" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE043_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_19" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE043_20" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE043_21" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r3060">R3060</a></td>
</tr><tr data-parent="IE043_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_22" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> INCIDENT</strong></td>
    <td>O</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0015">G0015</a></td>
</tr><tr data-parent="IE043_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>n1</td>
    <td>CL019</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_23" data-parent="IE043_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ENDORSEMENT</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE043_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Place</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL009</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_24" data-parent="IE043_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> LOCATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td>CL038</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td>CL244</td>
    <td><a href="phase-6-rules.html#c0460">C0460</a></td>
</tr><tr data-parent="IE043_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL009</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_25" data-parent="IE043_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0460">C0460</a></td>
</tr><tr data-parent="IE043_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr data-parent="IE043_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr class="parent-row" data-level="IE043_26" data-parent="IE043_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0460">C0460</a></td>
</tr><tr data-parent="IE043_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE043_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_27" data-parent="IE043_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#s1023">S1023</a><br /><a href="phase-6-rules.html#c0040">C0040</a><br /><a href="phase-6-rules.html#c0240">C0240</a><br /><a href="phase-6-rules.html#g0103">G0103</a></td>
</tr><tr data-parent="IE043_27">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_27">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0820">C0820</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0016">G0016</a></td>
</tr><tr data-parent="IE043_27">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of seals</td>
    <td>D</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0396">C0396</a><br /><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0023">G0023</a><br /><a href="phase-6-rules.html#r0106">R0106</a></td>
</tr><tr class="parent-row" data-level="IE043_28" data-parent="IE043_27">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0569">C0569</a></td>
</tr><tr data-parent="IE043_28">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_28">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0107">R0107</a></td>
</tr><tr class="parent-row" data-level="IE043_29" data-parent="IE043_27">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS REFERENCE</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0670">G0670</a></td>
</tr><tr data-parent="IE043_29">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_29">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#g0006">G0006</a></td>
</tr><tr class="parent-row" data-level="IE043_30" data-parent="IE043_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSHIPMENT</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0240">C0240</a></td>
</tr><tr data-parent="IE043_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container indicator</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#g0029">G0029</a></td>
</tr><tr class="parent-row" data-level="IE043_31" data-parent="IE043_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT MEANS</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#g0023">G0023</a></td>
</tr><tr data-parent="IE043_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0023">G0023</a></td>
</tr><tr data-parent="IE043_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td><a href="phase-6-rules.html#g0023">G0023</a></td>
</tr><tr class="parent-row" data-level="IE043_32" data-parent="IE043_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0343">C0343</a></td>
</tr><tr data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0983">R0983</a></td>
</tr><tr data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0502">C0502</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Security indicator from export declaration</td>
    <td>O</td>
    <td>n1</td>
    <td>CL217</td>
    <td><a href="phase-6-rules.html#g0025">G0025</a><br /><a href="phase-6-rules.html#g0026">G0026</a></td>
</tr><tr class="parent-row" data-level="IE043_33" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0349">C0349</a></td>
</tr><tr data-parent="IE043_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE043_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE043_34" data-parent="IE043_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE043_34">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_34">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE043_34">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_34">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_35" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0003">C0003</a><br /><a href="phase-6-rules.html#g0001">G0001</a></td>
</tr><tr data-parent="IE043_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE043_36" data-parent="IE043_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE043_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE043_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_37" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0339">C0339</a><br /><a href="phase-6-rules.html#r0855">R0855</a></td>
</tr><tr data-parent="IE043_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#r0472">R0472</a><br /><a href="phase-6-rules.html#r0474">R0474</a><br /><a href="phase-6-rules.html#r0476">R0476</a></td>
</tr><tr data-parent="IE043_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0473">R0473</a></td>
</tr><tr data-parent="IE043_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_38" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0026">G0026</a></td>
</tr><tr data-parent="IE043_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL228</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0416">R0416</a></td>
</tr><tr data-parent="IE043_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_39" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE043_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_40" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE043_41" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE043_42" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r3062">R3062</a></td>
</tr><tr data-parent="IE043_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_43" data-parent="IE043_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT ITEM</strong></td>
    <td>R</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0988">R0988</a></td>
</tr><tr data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#r0007">R0007</a></td>
</tr><tr data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration type</td>
    <td>D</td>
    <td>an..5</td>
    <td>CL232</td>
    <td><a href="phase-6-rules.html#c0045">C0045</a><br /><a href="phase-6-rules.html#r0601">R0601</a><br /><a href="phase-6-rules.html#r0909">R0909</a></td>
</tr><tr data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0343">C0343</a><br /><a href="phase-6-rules.html#g0113">G0113</a></td>
</tr><tr data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0502">C0502</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0062">G0062</a></td>
</tr><tr class="parent-row" data-level="IE043_44" data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNEE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0001">G0001</a><br /><a href="phase-6-rules.html#g0989">G0989</a></td>
</tr><tr data-parent="IE043_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0851">R0851</a></td>
</tr><tr data-parent="IE043_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_45" data-parent="IE043_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0989">G0989</a></td>
</tr><tr data-parent="IE043_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL199</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_46" data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description of goods</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td>CL016</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_47" data-parent="IE043_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY CODE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0154">C0154</a></td>
</tr><tr data-parent="IE043_47">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td>CL152</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_47">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combined nomenclature code</td>
    <td>O</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0060">R0060</a></td>
</tr><tr class="parent-row" data-level="IE043_48" data-parent="IE043_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DANGEROUS GOODS</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0300">G0300</a></td>
</tr><tr data-parent="IE043_48">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_48">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN Number</td>
    <td>R</td>
    <td>an4</td>
    <td>CL101</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_49" data-parent="IE043_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS MEASURE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#r0221">R0221</a></td>
</tr><tr data-parent="IE043_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Net mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0837">C0837</a><br /><a href="phase-6-rules.html#r0223">R0223</a></td>
</tr><tr class="parent-row" data-level="IE043_50" data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PACKAGING</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of packages</td>
    <td>R</td>
    <td>an2</td>
    <td>CL017</td>
    <td><a href="phase-6-rules.html#r0220">R0220</a></td>
</tr><tr data-parent="IE043_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of packages</td>
    <td>D</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0060">C0060</a><br /><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#r0219">R0219</a><br /><a href="phase-6-rules.html#r0364">R0364</a></td>
</tr><tr data-parent="IE043_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shipping marks</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0060">C0060</a><br /><a href="phase-6-rules.html#g0024">G0024</a></td>
</tr><tr class="parent-row" data-level="IE043_51" data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL214</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r0020">R0020</a></td>
</tr><tr data-parent="IE043_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE043_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goods item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE043_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_52" data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr data-parent="IE043_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE043_53" data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a><br /><a href="phase-6-rules.html#g0989">G0989</a></td>
</tr><tr data-parent="IE043_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a></td>
</tr><tr class="parent-row" data-level="IE043_54" data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a></td>
</tr><tr data-parent="IE043_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0015">C0015</a><br /><a href="phase-6-rules.html#g0050">G0050</a><br /><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#r0023">R0023</a></td>
</tr><tr class="parent-row" data-level="IE043_55" data-parent="IE043_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0825">G0825</a></td>
</tr><tr data-parent="IE043_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE043_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#r3061">R3061</a></td>
</tr><tr data-parent="IE043_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>

