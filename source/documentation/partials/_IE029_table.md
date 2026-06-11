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
</tr><tr class="parent-row" data-level="IE029_0" >
    <td><span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;LRN</td>
    <td>R</td>
    <td>an..22</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Declaration type</td>
    <td>R</td>
    <td>an..5</td>
    <td>CL231</td>
    <td><a href="../phase-6-rules/R0601.html">R0601</a><br /><a href="../phase-6-rules/R0909.html">R0909</a><br /><a href="../phase-6-rules/R0911.html">R0911</a></td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Additional declaration type</td>
    <td>R</td>
    <td>a1</td>
    <td>CL042</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;TIR Carnet number</td>
    <td>D</td>
    <td>an..12</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0411.html">C0411</a><br /><a href="../phase-6-rules/R0990.html">R0990</a></td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Declaration acceptance date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Release date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Security</td>
    <td>R</td>
    <td>n1</td>
    <td>CL217</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reduced dataset indicator</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Specific circumstance indicator</td>
    <td>O</td>
    <td>an3</td>
    <td>CL296</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Communication language at departure</td>
    <td>O</td>
    <td>a2</td>
    <td>CL192</td>
    <td><a href="../phase-6-rules/G0100.html">G0100</a></td>
</tr><tr data-parent="IE029_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Binding itinerary</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_1" >
    <td><span class="toggle-icon">▾</span> <strong> AUTHORISATION</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0101.html">C0101</a><br /><a href="../phase-6-rules/G0102.html">G0102</a></td>
</tr><tr data-parent="IE029_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an..4</td>
    <td>CL235</td>
    <td><a href="../phase-6-rules/G0117.html">G0117</a><br /><a href="../phase-6-rules/R0350.html">R0350</a></td>
</tr><tr data-parent="IE029_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0033.html">G0033</a><br /><a href="../phase-6-rules/R0352.html">R0352</a></td>
</tr><tr class="parent-row" data-level="IE029_2" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_3" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DESTINATION (DECLARED)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td><a href="../phase-6-rules/R0871.html">R0871</a></td>
</tr><tr class="parent-row" data-level="IE029_4" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF TRANSIT (DECLARED)</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0030.html">C0030</a><br /><a href="../phase-6-rules/G0030.html">G0030</a></td>
</tr><tr data-parent="IE029_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL173</td>
    <td><a href="../phase-6-rules/G0142.html">G0142</a><br /><a href="../phase-6-rules/R0003.html">R0003</a><br /><a href="../phase-6-rules/R0006.html">R0006</a><br /><a href="../phase-6-rules/R0871.html">R0871</a></td>
</tr><tr data-parent="IE029_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Arrival date and time (estimated)</td>
    <td>D</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0598.html">C0598</a><br /><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/R0004.html">R0004</a></td>
</tr><tr class="parent-row" data-level="IE029_5" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0587.html">C0587</a></td>
</tr><tr data-parent="IE029_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL175</td>
    <td><a href="../phase-6-rules/R0103.html">R0103</a><br /><a href="../phase-6-rules/R0871.html">R0871</a></td>
</tr><tr class="parent-row" data-level="IE029_6" >
    <td><span class="toggle-icon">▾</span> <strong> HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0120.html">G0120</a><br /><a href="../phase-6-rules/R0850.html">R0850</a></td>
</tr><tr data-parent="IE029_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0904.html">C0904</a><br /><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE029_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr class="parent-row" data-level="IE029_7" data-parent="IE029_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr data-parent="IE029_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0505.html">C0505</a></td>
</tr><tr data-parent="IE029_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_8" data-parent="IE029_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0105.html">G0105</a></td>
</tr><tr data-parent="IE029_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr class="parent-row" data-level="IE029_9" >
    <td><span class="toggle-icon">▾</span> <strong> REPRESENTATIVE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0860.html">G0860</a></td>
</tr><tr data-parent="IE029_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0850.html">R0850</a></td>
</tr><tr data-parent="IE029_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Status</td>
    <td>R</td>
    <td>n1</td>
    <td>CL094</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_10" data-parent="IE029_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0105.html">G0105</a></td>
</tr><tr data-parent="IE029_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr class="parent-row" data-level="IE029_11" >
    <td><span class="toggle-icon">▾</span> <strong> CONTROL RESULT</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0160.html">G0160</a></td>
</tr><tr data-parent="IE029_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an2</td>
    <td>CL196</td>
    <td><a href="../phase-6-rules/G0126.html">G0126</a><br /><a href="../phase-6-rules/R0910.html">R0910</a><br /><a href="../phase-6-rules/R0912.html">R0912</a></td>
</tr><tr data-parent="IE029_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/G0127.html">G0127</a></td>
</tr><tr data-parent="IE029_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Controlled by</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_12" >
    <td><span class="toggle-icon">▾</span> <strong> GUARANTEE</strong></td>
    <td>R</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Guarantee type</td>
    <td>R</td>
    <td>an1</td>
    <td>CL251</td>
    <td><a href="../phase-6-rules/R0900.html">R0900</a></td>
</tr><tr data-parent="IE029_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Other guarantee reference</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0130.html">C0130</a></td>
</tr><tr class="parent-row" data-level="IE029_13" data-parent="IE029_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GUARANTEE REFERENCE</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0085.html">C0085</a></td>
</tr><tr data-parent="IE029_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GRN</td>
    <td>D</td>
    <td>an..24</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0086.html">C0086</a><br /><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/R0318.html">R0318</a></td>
</tr><tr data-parent="IE029_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Access code</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0086.html">C0086</a></td>
</tr><tr data-parent="IE029_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amount to be covered</td>
    <td>R</td>
    <td>n..16,2</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0021.html">G0021</a></td>
</tr><tr data-parent="IE029_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Currency</td>
    <td>R</td>
    <td>a3</td>
    <td>CL048</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_14" >
    <td><span class="toggle-icon">▾</span> <strong> CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="../phase-6-rules/C0909.html">C0909</a><br /><a href="../phase-6-rules/G0988.html">G0988</a></td>
</tr><tr data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="../phase-6-rules/C0343.html">C0343</a><br /><a href="../phase-6-rules/G0113.html">G0113</a></td>
</tr><tr data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Container indicator</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Inland mode of transport</td>
    <td>O</td>
    <td>n1</td>
    <td>CL218</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Mode of transport at the border</td>
    <td>D</td>
    <td>n1</td>
    <td>CL218</td>
    <td><a href="../phase-6-rules/C0029.html">C0029</a><br /><a href="../phase-6-rules/G0020.html">G0020</a><br /><a href="../phase-6-rules/G0115.html">G0115</a></td>
</tr><tr data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0994.html">R0994</a></td>
</tr><tr data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0502.html">C0502</a><br /><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr class="parent-row" data-level="IE029_15" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CARRIER</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0090.html">G0090</a></td>
</tr><tr data-parent="IE029_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/G0201.html">G0201</a><br /><a href="../phase-6-rules/R0840.html">R0840</a></td>
</tr><tr class="parent-row" data-level="IE029_16" data-parent="IE029_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0105.html">G0105</a></td>
</tr><tr data-parent="IE029_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr class="parent-row" data-level="IE029_17" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNOR</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0850.html">R0850</a></td>
</tr><tr data-parent="IE029_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr class="parent-row" data-level="IE029_18" data-parent="IE029_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr data-parent="IE029_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0505.html">C0505</a></td>
</tr><tr data-parent="IE029_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_19" data-parent="IE029_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0105.html">G0105</a></td>
</tr><tr data-parent="IE029_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr class="parent-row" data-level="IE029_20" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0001.html">C0001</a><br /><a href="../phase-6-rules/G0001.html">G0001</a></td>
</tr><tr data-parent="IE029_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0851.html">R0851</a></td>
</tr><tr data-parent="IE029_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr class="parent-row" data-level="IE029_21" data-parent="IE029_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr data-parent="IE029_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0505.html">C0505</a></td>
</tr><tr data-parent="IE029_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_22" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Role</td>
    <td>R</td>
    <td>a..3</td>
    <td>CL704</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/G0201.html">G0201</a><br /><a href="../phase-6-rules/R0840.html">R0840</a></td>
</tr><tr class="parent-row" data-level="IE029_23" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0872.html">C0872</a><br /><a href="../phase-6-rules/G0103.html">G0103</a></td>
</tr><tr data-parent="IE029_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0055.html">C0055</a><br /><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE029_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of seals</td>
    <td>R</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0021.html">G0021</a><br /><a href="../phase-6-rules/R0106.html">R0106</a><br /><a href="../phase-6-rules/R0165.html">R0165</a><br /><a href="../phase-6-rules/R0448.html">R0448</a></td>
</tr><tr class="parent-row" data-level="IE029_24" data-parent="IE029_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0569.html">C0569</a></td>
</tr><tr data-parent="IE029_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0107.html">R0107</a></td>
</tr><tr class="parent-row" data-level="IE029_25" data-parent="IE029_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS REFERENCE</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0670.html">C0670</a><br /><a href="../phase-6-rules/G0670.html">G0670</a></td>
</tr><tr data-parent="IE029_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0005.html">G0005</a><br /><a href="../phase-6-rules/G0006.html">G0006</a></td>
</tr><tr class="parent-row" data-level="IE029_26" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> LOCATION OF GOODS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0489.html">C0489</a></td>
</tr><tr data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of location</td>
    <td>R</td>
    <td>a1</td>
    <td>CL347</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td>CL326</td>
    <td><a href="../phase-6-rules/G0500.html">G0500</a></td>
</tr><tr data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authorisation number</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0394.html">C0394</a></td>
</tr><tr data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Additional identifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0671.html">C0671</a></td>
</tr><tr data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td>CL244</td>
    <td><a href="../phase-6-rules/C0394.html">C0394</a></td>
</tr><tr class="parent-row" data-level="IE029_27" data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0394.html">C0394</a></td>
</tr><tr data-parent="IE029_27">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_28" data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0394.html">C0394</a></td>
</tr><tr data-parent="IE029_28">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/G0014.html">G0014</a></td>
</tr><tr data-parent="IE029_28">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/G0014.html">G0014</a></td>
</tr><tr class="parent-row" data-level="IE029_29" data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ECONOMIC OPERATOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0394.html">C0394</a></td>
</tr><tr data-parent="IE029_29">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0850.html">R0850</a></td>
</tr><tr class="parent-row" data-level="IE029_30" data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0394.html">C0394</a></td>
</tr><tr data-parent="IE029_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0505.html">C0505</a></td>
</tr><tr data-parent="IE029_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_30">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL009</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_31" data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> POSTCODE ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0394.html">C0394</a></td>
</tr><tr data-parent="IE029_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;House number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0382.html">C0382</a></td>
</tr><tr data-parent="IE029_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_31">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL190</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_32" data-parent="IE029_26">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0394.html">C0394</a><br /><a href="../phase-6-rules/G0105.html">G0105</a></td>
</tr><tr data-parent="IE029_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_32">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr class="parent-row" data-level="IE029_33" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0339.html">C0339</a><br /><a href="../phase-6-rules/G0119.html">G0119</a><br /><a href="../phase-6-rules/R0855.html">R0855</a></td>
</tr><tr data-parent="IE029_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="../phase-6-rules/G0112.html">G0112</a><br /><a href="../phase-6-rules/R0472.html">R0472</a><br /><a href="../phase-6-rules/R0474.html">R0474</a><br /><a href="../phase-6-rules/R0476.html">R0476</a></td>
</tr><tr data-parent="IE029_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0473.html">R0473</a></td>
</tr><tr data-parent="IE029_33">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_34" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COUNTRY OF ROUTING OF CONSIGNMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0586.html">C0586</a><br /><a href="../phase-6-rules/G0061.html">G0061</a></td>
</tr><tr data-parent="IE029_34">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_34">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL008</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_35" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ACTIVE BORDER TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0908.html">C0908</a></td>
</tr><tr data-parent="IE029_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Customs office at border reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL141</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL219</td>
    <td><a href="../phase-6-rules/G0112.html">G0112</a></td>
</tr><tr data-parent="IE029_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0076.html">R0076</a></td>
</tr><tr data-parent="IE029_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_35">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conveyance reference number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0531.html">C0531</a><br /><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/R0315.html">R0315</a></td>
</tr><tr class="parent-row" data-level="IE029_36" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PLACE OF LOADING</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0410.html">C0410</a></td>
</tr><tr data-parent="IE029_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td>CL244</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="../phase-6-rules/C0387.html">C0387</a></td>
</tr><tr data-parent="IE029_36">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0387.html">C0387</a></td>
</tr><tr class="parent-row" data-level="IE029_37" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PLACE OF UNLOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0191.html">C0191</a></td>
</tr><tr data-parent="IE029_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td>CL244</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="../phase-6-rules/C0387.html">C0387</a></td>
</tr><tr data-parent="IE029_37">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0387.html">C0387</a></td>
</tr><tr class="parent-row" data-level="IE029_38" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL214</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a><br /><a href="../phase-6-rules/R0020.html">R0020</a></td>
</tr><tr data-parent="IE029_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr data-parent="IE029_38">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_39" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a></td>
</tr><tr data-parent="IE029_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr data-parent="IE029_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_39">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_40" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a></td>
</tr><tr data-parent="IE029_40">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr class="parent-row" data-level="IE029_41" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a></td>
</tr><tr data-parent="IE029_41">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr class="parent-row" data-level="IE029_42" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a><br /><a href="../phase-6-rules/R3060.html">R3060</a></td>
</tr><tr data-parent="IE029_42">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_43" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT CHARGES</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0186.html">C0186</a></td>
</tr><tr data-parent="IE029_43">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td>CL116</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_44" data-parent="IE029_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="../phase-6-rules/C0909.html">C0909</a><br /><a href="../phase-6-rules/G0988.html">G0988</a></td>
</tr><tr data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="../phase-6-rules/C0343.html">C0343</a><br /><a href="../phase-6-rules/G0062.html">G0062</a><br /><a href="../phase-6-rules/G0113.html">G0113</a><br /><a href="../phase-6-rules/R0506.html">R0506</a></td>
</tr><tr data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0983.html">R0983</a></td>
</tr><tr data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0502.html">C0502</a><br /><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Security indicator from export declaration</td>
    <td>O</td>
    <td>n1</td>
    <td>CL217</td>
    <td><a href="../phase-6-rules/G0025.html">G0025</a><br /><a href="../phase-6-rules/G0026.html">G0026</a></td>
</tr><tr class="parent-row" data-level="IE029_45" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0349.html">C0349</a></td>
</tr><tr data-parent="IE029_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0850.html">R0850</a></td>
</tr><tr data-parent="IE029_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr class="parent-row" data-level="IE029_46" data-parent="IE029_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr data-parent="IE029_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0505.html">C0505</a></td>
</tr><tr data-parent="IE029_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_46">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_47" data-parent="IE029_45">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0105.html">G0105</a></td>
</tr><tr data-parent="IE029_47">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_47">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_47">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr class="parent-row" data-level="IE029_48" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0001.html">C0001</a><br /><a href="../phase-6-rules/G0001.html">G0001</a></td>
</tr><tr data-parent="IE029_48">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0851.html">R0851</a></td>
</tr><tr data-parent="IE029_48">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr class="parent-row" data-level="IE029_49" data-parent="IE029_48">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0250.html">C0250</a></td>
</tr><tr data-parent="IE029_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0505.html">C0505</a></td>
</tr><tr data-parent="IE029_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_49">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_50" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Role</td>
    <td>R</td>
    <td>a..3</td>
    <td>CL704</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_50">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/G0201.html">G0201</a><br /><a href="../phase-6-rules/R0840.html">R0840</a></td>
</tr><tr class="parent-row" data-level="IE029_51" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0339.html">C0339</a><br /><a href="../phase-6-rules/G0119.html">G0119</a><br /><a href="../phase-6-rules/R0855.html">R0855</a></td>
</tr><tr data-parent="IE029_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="../phase-6-rules/G0112.html">G0112</a><br /><a href="../phase-6-rules/R0472.html">R0472</a><br /><a href="../phase-6-rules/R0474.html">R0474</a><br /><a href="../phase-6-rules/R0476.html">R0476</a></td>
</tr><tr data-parent="IE029_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0473.html">R0473</a></td>
</tr><tr data-parent="IE029_51">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_52" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0026.html">G0026</a></td>
</tr><tr data-parent="IE029_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL228</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0416.html">R0416</a></td>
</tr><tr data-parent="IE029_52">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_53" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a></td>
</tr><tr data-parent="IE029_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr data-parent="IE029_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_53">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_54" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a></td>
</tr><tr data-parent="IE029_54">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr class="parent-row" data-level="IE029_55" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a></td>
</tr><tr data-parent="IE029_55">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr class="parent-row" data-level="IE029_56" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_56">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_56">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a><br /><a href="../phase-6-rules/R3062.html">R3062</a></td>
</tr><tr data-parent="IE029_56">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_57" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT CHARGES</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0186.html">C0186</a><br /><a href="../phase-6-rules/C0337.html">C0337</a></td>
</tr><tr data-parent="IE029_57">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td>CL116</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_58" data-parent="IE029_44">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT ITEM</strong></td>
    <td>R</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0071.html">G0071</a></td>
</tr><tr data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0072.html">G0072</a><br /><a href="../phase-6-rules/R0988.html">R0988</a></td>
</tr><tr data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0005.html">G0005</a><br /><a href="../phase-6-rules/R0007.html">R0007</a></td>
</tr><tr data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration type</td>
    <td>D</td>
    <td>an..5</td>
    <td>CL232</td>
    <td><a href="../phase-6-rules/C0045.html">C0045</a><br /><a href="../phase-6-rules/R0601.html">R0601</a><br /><a href="../phase-6-rules/R0909.html">R0909</a></td>
</tr><tr data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="../phase-6-rules/C0909.html">C0909</a><br /><a href="../phase-6-rules/G0988.html">G0988</a></td>
</tr><tr data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="../phase-6-rules/C0343.html">C0343</a><br /><a href="../phase-6-rules/G0113.html">G0113</a></td>
</tr><tr data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0502.html">C0502</a><br /><a href="../phase-6-rules/G0002.html">G0002</a></td>
</tr><tr class="parent-row" data-level="IE029_59" data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_59">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_59">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Role</td>
    <td>R</td>
    <td>a..3</td>
    <td>CL704</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_59">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0002.html">G0002</a><br /><a href="../phase-6-rules/G0201.html">G0201</a><br /><a href="../phase-6-rules/R0840.html">R0840</a></td>
</tr><tr class="parent-row" data-level="IE029_60" data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description of goods</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td>CL016</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_61" data-parent="IE029_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY CODE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0153.html">C0153</a></td>
</tr><tr data-parent="IE029_61">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td>CL152</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_61">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combined nomenclature code</td>
    <td>O</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0060.html">R0060</a></td>
</tr><tr class="parent-row" data-level="IE029_62" data-parent="IE029_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DANGEROUS GOODS</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0300.html">G0300</a></td>
</tr><tr data-parent="IE029_62">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_62">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN Number</td>
    <td>R</td>
    <td>an4</td>
    <td>CL101</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_63" data-parent="IE029_60">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS MEASURE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_63">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0021.html">G0021</a><br /><a href="../phase-6-rules/R0221.html">R0221</a></td>
</tr><tr data-parent="IE029_63">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Net mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0837.html">C0837</a><br /><a href="../phase-6-rules/R0223.html">R0223</a></td>
</tr><tr class="parent-row" data-level="IE029_64" data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PACKAGING</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_64">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_64">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of packages</td>
    <td>R</td>
    <td>an2</td>
    <td>CL017</td>
    <td><a href="../phase-6-rules/R0220.html">R0220</a></td>
</tr><tr data-parent="IE029_64">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of packages</td>
    <td>D</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0060.html">C0060</a><br /><a href="../phase-6-rules/G0021.html">G0021</a><br /><a href="../phase-6-rules/R0219.html">R0219</a><br /><a href="../phase-6-rules/R0364.html">R0364</a></td>
</tr><tr data-parent="IE029_64">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shipping marks</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0060.html">C0060</a><br /><a href="../phase-6-rules/G0024.html">G0024</a></td>
</tr><tr class="parent-row" data-level="IE029_65" data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PREVIOUS DOCUMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0035.html">C0035</a><br /><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL214</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a><br /><a href="../phase-6-rules/R0020.html">R0020</a></td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goods item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0058.html">G0058</a></td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of packages</td>
    <td>O</td>
    <td>an2</td>
    <td>CL017</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of packages</td>
    <td>O</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Measurement unit and qualifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>CL349</td>
    <td><a href="../phase-6-rules/C0298.html">C0298</a></td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quantity</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_65">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_66" data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a></td>
</tr><tr data-parent="IE029_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0321.html">G0321</a></td>
</tr><tr data-parent="IE029_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE029_66">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE029_67" data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_67">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_67">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a></td>
</tr><tr data-parent="IE029_67">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/C0015.html">C0015</a><br /><a href="../phase-6-rules/G0050.html">G0050</a><br /><a href="../phase-6-rules/G0321.html">G0321</a><br /><a href="../phase-6-rules/R0023.html">R0023</a></td>
</tr><tr class="parent-row" data-level="IE029_68" data-parent="IE029_58">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/G0825.html">G0825</a></td>
</tr><tr data-parent="IE029_68">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="../phase-6-rules/R0987.html">R0987</a></td>
</tr><tr data-parent="IE029_68">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code</td>
    <td>R</td>
    <td>an5</td>
    <td>CL239</td>
    <td><a href="../phase-6-rules/G0057.html">G0057</a><br /><a href="../phase-6-rules/R3061.html">R3061</a></td>
</tr><tr data-parent="IE029_68">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr></table>