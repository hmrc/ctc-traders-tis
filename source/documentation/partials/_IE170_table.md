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
<tr class="parent-row" data-level="IE170_0" >
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong>MESSAGE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message sender</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message recipient</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message type</td>
    <td>R</td>
    <td>an6</td>
    <td>CL060</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0511">C0511</a><br /><a href="phase-6-rules.html#r0008">R0008</a></td>
</tr><tr class="parent-row" data-level="IE170_1" data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LRN</td>
    <td>R</td>
    <td>an..22</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Limit date</td>
    <td>D</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0840">C0840</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE170_2" data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE170_3" data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0120">G0120</a><br /><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE170_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0904">C0904</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE170_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr class="parent-row" data-level="IE170_4" data-parent="IE170_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0250">C0250</a></td>
</tr><tr data-parent="IE170_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE170_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE170_5" data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> REPRESENTATIVE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0850">G0850</a></td>
</tr><tr data-parent="IE170_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr data-parent="IE170_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Status</td>
    <td>R</td>
    <td>n1</td>
    <td>CL094</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE170_6" data-parent="IE170_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr data-parent="IE170_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE170_7" data-parent="IE170_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0045">G0045</a></td>
</tr><tr data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container indicator</td>
    <td>D</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#c0824">C0824</a><br /><a href="phase-6-rules.html#g0332">G0332</a></td>
</tr><tr data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Inland mode of transport</td>
    <td>D</td>
    <td>n1</td>
    <td>CL218</td>
    <td><a href="phase-6-rules.html#c0170">C0170</a></td>
</tr><tr data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mode of transport at the border</td>
    <td>D</td>
    <td>n1</td>
    <td>CL218</td>
    <td><a href="phase-6-rules.html#c0600">C0600</a><br /><a href="phase-6-rules.html#g0020">G0020</a><br /><a href="phase-6-rules.html#g0115">G0115</a></td>
</tr><tr class="parent-row" data-level="IE170_8" data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0823">C0823</a><br /><a href="phase-6-rules.html#g0103">G0103</a><br /><a href="phase-6-rules.html#g0196">G0196</a></td>
</tr><tr data-parent="IE170_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE170_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0055">C0055</a><br /><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE170_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of seals</td>
    <td>R</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0165">G0165</a><br /><a href="phase-6-rules.html#r0106">R0106</a><br /><a href="phase-6-rules.html#r0448">R0448</a></td>
</tr><tr class="parent-row" data-level="IE170_9" data-parent="IE170_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0569">C0569</a></td>
</tr><tr data-parent="IE170_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE170_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0107">R0107</a></td>
</tr><tr class="parent-row" data-level="IE170_10" data-parent="IE170_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS REFERENCE</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0670">C0670</a><br /><a href="phase-6-rules.html#g0670">G0670</a><br /><a href="phase-6-rules.html#r0010">R0010</a></td>
</tr><tr data-parent="IE170_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE170_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#g0006">G0006</a></td>
</tr><tr class="parent-row" data-level="IE170_11" data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> LOCATION OF GOODS</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of location</td>
    <td>R</td>
    <td>a1</td>
    <td>CL347</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td>CL326</td>
    <td><a href="phase-6-rules.html#g0500">G0500</a></td>
</tr><tr data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authorisation number</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Additional identifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0671">C0671</a></td>
</tr><tr data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td>CL244</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr class="parent-row" data-level="IE170_12" data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE170_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL171</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE170_13" data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE170_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr data-parent="IE170_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr class="parent-row" data-level="IE170_14" data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ECONOMIC OPERATOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE170_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr class="parent-row" data-level="IE170_15" data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE170_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr data-parent="IE170_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL009</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE170_16" data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> POSTCODE ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr data-parent="IE170_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;House number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0382">C0382</a></td>
</tr><tr data-parent="IE170_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postcode</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL190</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE170_17" data-parent="IE170_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONTACT PERSON</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a><br /><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr data-parent="IE170_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr class="parent-row" data-level="IE170_18" data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0833">C0833</a><br /><a href="phase-6-rules.html#g0088">G0088</a><br /><a href="phase-6-rules.html#g0119">G0119</a><br /><a href="phase-6-rules.html#g0196">G0196</a><br /><a href="phase-6-rules.html#r0855">R0855</a></td>
</tr><tr data-parent="IE170_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE170_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#r0472">R0472</a><br /><a href="phase-6-rules.html#r0474">R0474</a><br /><a href="phase-6-rules.html#r0476">R0476</a></td>
</tr><tr data-parent="IE170_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0473">R0473</a></td>
</tr><tr data-parent="IE170_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE170_19" data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ACTIVE BORDER TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0807">C0807</a><br /><a href="phase-6-rules.html#r0790">R0790</a></td>
</tr><tr data-parent="IE170_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE170_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Customs office at border reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL141</td>
    <td><a href="phase-6-rules.html#g0789">G0789</a></td>
</tr><tr data-parent="IE170_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL219</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0076">R0076</a></td>
</tr><tr data-parent="IE170_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conveyance reference number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0808">C0808</a><br /><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#r0315">R0315</a></td>
</tr><tr class="parent-row" data-level="IE170_20" data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PLACE OF LOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0412">C0412</a></td>
</tr><tr data-parent="IE170_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td>CL244</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>D</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#c0387">C0387</a></td>
</tr><tr data-parent="IE170_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0387">C0387</a></td>
</tr><tr class="parent-row" data-level="IE170_21" data-parent="IE170_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1999x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE170_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr class="parent-row" data-level="IE170_22" data-parent="IE170_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0833">C0833</a><br /><a href="phase-6-rules.html#g0088">G0088</a><br /><a href="phase-6-rules.html#g0119">G0119</a><br /><a href="phase-6-rules.html#g0196">G0196</a><br /><a href="phase-6-rules.html#r0506">R0506</a><br /><a href="phase-6-rules.html#r0855">R0855</a></td>
</tr><tr data-parent="IE170_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr data-parent="IE170_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#r0472">R0472</a><br /><a href="phase-6-rules.html#r0474">R0474</a><br /><a href="phase-6-rules.html#r0476">R0476</a></td>
</tr><tr data-parent="IE170_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0473">R0473</a></td>
</tr><tr data-parent="IE170_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td>CL165</td>
    <td>&nbsp;</td>
</tr></table>