<table cellspacing="0">
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
    <td><strong>MESSAGE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Message sender</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Message recipient</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp; Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Message type</td>
    <td>R</td>
    <td>an6</td>
    <td>CL060</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0511">C0511</a><br /><a href="phase-6-rules.html#r0008">R0008</a></td>
</tr><tr>
    <td><strong>-&nbsp; TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#r0028">R0028</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Arrival notification date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Simplified procedure</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; AUTHORISATION</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0102">C0102</a><br /><a href="phase-6-rules.html#g0102">G0102</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an..4</td>
    <td>CL236</td>
    <td><a href="phase-6-rules.html#g0117">G0117</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0033">G0033</a></td>
</tr><tr>
    <td><strong>-&nbsp; CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Communication language at destination</td>
    <td>O</td>
    <td>a2</td>
    <td>CL192</td>
    <td><a href="phase-6-rules.html#g0100">G0100</a></td>
</tr><tr>
    <td><strong>-&nbsp; CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; LOCATION OF GOODS</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type of location</td>
    <td>R</td>
    <td>a1</td>
    <td>CL347</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td>CL326</td>
    <td><a href="phase-6-rules.html#g0500">G0500</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Authorisation number</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Additional identifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0671">C0671</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td>CL244</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CUSTOMS OFFICE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a><br /><a href="phase-6-rules.html#g0014">G0014</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ECONOMIC OPERATOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#r0850">R0850</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0505">C0505</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL009</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; POSTCODE ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; House number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0382">C0382</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td>CL190</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONTACT PERSON</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#c0394">C0394</a><br /><a href="phase-6-rules.html#g0105">G0105</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="phase-6-rules.html#g0002">G0002</a></td>
</tr></table>