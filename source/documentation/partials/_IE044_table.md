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
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
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
    <td><a href="phase-6-rules.html#c0511">C0511</a><br /><a href="phase-6-rules.html#r0008">R0008</a></td>
</tr><tr class="parent-row" data-level="IE044_0" >
    <td><span class="toggle-icon">▾</span> <strong> TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE044_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE044_0">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Other things to report</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE044_1" >
    <td><span class="toggle-icon">▾</span> <strong> CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0042">G0042</a></td>
</tr><tr data-parent="IE044_1">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE044_2" >
    <td><span class="toggle-icon">▾</span> <strong> TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0042">G0042</a></td>
</tr><tr data-parent="IE044_2">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr class="parent-row" data-level="IE044_3" >
    <td><span class="toggle-icon">▾</span> <strong> UNLOADING REMARK</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE044_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Conform</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#g0205">G0205</a></td>
</tr><tr data-parent="IE044_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Unloading completion</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#g0186">G0186</a></td>
</tr><tr data-parent="IE044_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Unloading date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr data-parent="IE044_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;State of seals</td>
    <td>D</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="phase-6-rules.html#c0440">C0440</a><br /><a href="phase-6-rules.html#g0017">G0017</a></td>
</tr><tr data-parent="IE044_3">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Unloading remark</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE044_4" >
    <td><span class="toggle-icon">▾</span> <strong> CONSIGNMENT</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_5" data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT EQUIPMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0103">G0103</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Container identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of seals</td>
    <td>O</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_6" data-parent="IE044_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SEAL</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_6">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identifier</td>
    <td>O</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE044_7" data-parent="IE044_5">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS REFERENCE</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_7">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#g0006">G0006</a></td>
</tr><tr class="parent-row" data-level="IE044_8" data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_8">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td>CL165</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_9" data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COUNTRY OF ROUTING OF CONSIGNMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_9">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Country</td>
    <td>O</td>
    <td>a2</td>
    <td>CL008</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_10" data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_10">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE044_11" data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_11">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_12" data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_12">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_13" data-parent="IE044_4">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> HOUSE CONSIGNMENT</strong></td>
    <td>O</td>
    <td>1999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_14" data-parent="IE044_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> DEPARTURE TRANSPORT MEANS</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_14">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td>CL165</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_15" data-parent="IE044_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_15">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE044_16" data-parent="IE044_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_16">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_17" data-parent="IE044_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_17">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_18" data-parent="IE044_13">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> CONSIGNMENT ITEM</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0055">R0055</a></td>
</tr><tr data-parent="IE044_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0005">G0005</a><br /><a href="phase-6-rules.html#r0055">R0055</a></td>
</tr><tr data-parent="IE044_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number UCR</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_19" data-parent="IE044_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description of goods</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td>CL016</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_20" data-parent="IE044_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> COMMODITY CODE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td>CL152</td>
    <td>&nbsp;</td>
</tr><tr data-parent="IE044_20">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combined nomenclature code</td>
    <td>D</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0816">C0816</a><br /><a href="phase-6-rules.html#g0360">G0360</a><br /><a href="phase-6-rules.html#r0060">R0060</a></td>
</tr><tr class="parent-row" data-level="IE044_21" data-parent="IE044_19">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> GOODS MEASURE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_21">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Net mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_22" data-parent="IE044_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> PACKAGING</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type of packages</td>
    <td>O</td>
    <td>an2</td>
    <td>CL017</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of packages</td>
    <td>O</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0021">G0021</a><br /><a href="phase-6-rules.html#g0139">G0139</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_22">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shipping marks</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_23" data-parent="IE044_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_23">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr class="parent-row" data-level="IE044_24" data-parent="IE044_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a><br /><a href="phase-6-rules.html#g0989">G0989</a></td>
</tr><tr data-parent="IE044_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_24">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr class="parent-row" data-level="IE044_25" data-parent="IE044_18">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="toggle-icon">▾</span> <strong> ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0054">R0054</a></td>
</tr><tr data-parent="IE044_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="phase-6-rules.html#g0057">G0057</a><br /><a href="phase-6-rules.html#g0360">G0360</a></td>
</tr><tr data-parent="IE044_25">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0321">G0321</a><br /><a href="phase-6-rules.html#g0360">G0360</a><br /><a href="phase-6-rules.html#r0023">R0023</a></td>
</tr></table>