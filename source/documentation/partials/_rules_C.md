## C0001

**Functional Description**

IF &lt;CONSIGNMENT.Country of destination&gt; is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; ="R"<br>
ELSE IF at least one iteration of &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of destination&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "R" for THIS House<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Consignment<br>
ELSE IF at least one iteration of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "R" for THIS House<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Consignment that includes THIS Consignment Item<br>
ELSE IF &lt;TRANSIT OPERATION.Security&gt; is in SET {0,1}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT -CONSIGNEE&gt;= "O"<br>
ELSE IF at least one instance of &lt;CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'30600'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N" AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF at least one instance of &lt;CONSIGNMENT-HOUSE CONSIGNMENT- ADDITIONAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;INFORMATION.Code&gt; is EQUAL to '30600'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN  &lt;CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N" AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"R"<br>
ELSE IF at least one iteration of /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDestination is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"R" for THIS House Consignment<br>
ELSE IF at least one iteration of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"R" for THIS House Consignment that includes<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THIS Consignment Item<br>
ELSE IF /<span>&#42;</span>/TransitOperation/security is in SET {0,1}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"O"<br>
ELSE IF at least one instance of /<span>&#42;</span>/Consignment/AdditionalInformation/code is EQUAL to '30600'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Consignee&nbsp;=&nbsp;"N" AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
ELSE IF at least one instance of /<span>&#42;</span>/Consignment/HouseConsignment/AdditionalInformation/code IS<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to '30600'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Consignee&nbsp;=&nbsp;"N" AND THIS /<span>&#42;</span>/Consignment/HouseConsignment/Consignee =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"N"<br>
ELSE<br>
IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"O"


## C0003

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;TRANSIT OPERATION.Specific circumstance indicator&gt; is EQUAL to ' F34'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT - CONSIGNEE&gt;&nbsp;=&nbsp;"N" AND &lt;CONSIGNMENT - HOUSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT - CONSIGNEE&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT - CONSIGNEE&gt;&nbsp;=&nbsp;"R" AND &lt;CONSIGNMENT - HOUSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT - CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT.Country of destination&gt; is in SET CL009 (CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; ="R"<br>
ELSE IF at least one iteration of &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of destination&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is in SET CL009 (CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "R" for THIS House<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Consignment<br>
ELSE IF at least one iteration of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL009 (CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "R" for THIS House<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Consignment that includes THIS Consignment Item<br>
ELSE IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to '0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT -CONSIGNEE&gt;= "O"<br>
ELSE IF at least one instance of &lt;CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'30600'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N" AND THIS &lt;CONSIGNMENT-HOUSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF at least one instance of  &lt;CONSIGNMENT-HOUSE CONSIGNMENT- ADDITIONAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;INFORMATION.Code&gt; is EQUAL to '30600'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N" AND THIS &lt;CONSIGNMENT-HOUSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-CONSIGNEE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt;= "O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/TransitOperation/SpecificCircumstanceIndicator is EQUAL to 'F34'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Consignee&nbsp;=&nbsp;"N" AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignee&nbsp;=&nbsp;"R" AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
ELSE  IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"R"<br>
ELSE IF at least one iteration of /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDestination is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"R" for THIS House Consignment<br>
ELSE IF at least one iteration of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"R" for THIS House Consignment that<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;includes THIS Consignment Item<br>
ELSE IF /<span>&#42;</span>/TransitOperation/security is EQUAL to '0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"O"<br>
ELSE IF at least one instance of /<span>&#42;</span>/Consignment/AdditionalInformation/code is EQUAL to '30600'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Consignee&nbsp;=&nbsp;"N" AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
ELSE IF at least one instance of /<span>&#42;</span>/Consignment/HouseConsignment/AdditionalInformation/code is<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to '30600'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN  /<span>&#42;</span>/Consignment/Consignee&nbsp;=&nbsp;"N" AND THIS /<span>&#42;</span>/Consignment/HouseConsignment/Consignee =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/Consignee is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee&nbsp;=&nbsp;"O"


## C0015

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;REFERENCE.Type&gt; is in SET CL234 (DocumentTypeExcise)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;REFERENCE.Reference number&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;REFERENCE.Reference number&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/type is in SET CL234<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/referenceNumber =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/referenceNumber =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"O"


## C0027

**Functional Description**

IF &lt;CTL control&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC043C-HOLDER OF THE TRANSIT PROCEDURE&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC043C-CONSIGNMENT&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC043C-TRANSIT OPERATION.Declaration type&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC043C-TRANSIT OPERATION.Declaration acceptance date&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC043C-CONSIGNMENT.Gross mass&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC043C-HOLDER OF THE TRANSIT PROCEDURE&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC043C-CONSIGNMENT&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC043C-TRANSIT OPERATION.Declaration type&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC043C-TRANSIT OPERATION.Declaration acceptance date&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC043C-CONSIGNMENT.Gross mass&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/CTLControl is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC043C/HolderOfTheTransitProcedure&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/Consignment&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/TransitOperation/declarationType&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/TransitOperation/declarationAcceptanceDate&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/Consignment/grossMass&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/HolderOfTheTransitProcedure&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/ Consignment&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/TransitOperation/declarationType&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/TransitOperation/declarationAcceptanceDate&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC043C/Consignment/grossMass&nbsp;=&nbsp;"R"


## C0029

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT.Mode of transport at the border&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT.Mode of transport at the border&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder&nbsp;=&nbsp;"O"


## C0030

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {TIR, T2SM}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF (the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is in SET CL112 (CountryCodesCTC)) AND (the first two characters of &lt;CUSTOMS OFFICE<br>
&nbsp;&nbsp;&nbsp;&nbsp;OF DESTINATION (DECLARED). Reference number&gt; is in SET CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryCodesCTC)) AND (the first two characters of &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE.Reference number&gt; is EQUAL to the first two characters of CUSTOMS<br>
&nbsp;&nbsp;&nbsp;&nbsp;OFFICE OF DESTINATION (DECLARED). Reference number&gt;)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'T2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL 'T' AND at least one instance of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to 'T2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is in SET CL112 (CountryCodesCTC) OR the first two characters of &lt;CUSTOMS OFFICE<br>
&nbsp;&nbsp;&nbsp;&nbsp;OF DESTINATION (DECLARED). Reference number&gt; is in SET CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryCodesCTC)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF at least one instance of &lt;CONSIGNMENT-COUNTRY OF ROUTING OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT.Country&gt; is in<br>
&nbsp;&nbsp;&nbsp;&nbsp;SET CL112 (CountryCodesCTC)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is EQUAL to 'AD' OR IF the first two characters of &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;DESTINATION (DECLARED). Reference number&gt; is EQUAL to 'AD'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF &lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is in SET {TIR, T2SM}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF (the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL112) AND (the first two characters of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET CL112) AND (the first<br>
&nbsp;&nbsp;&nbsp;&nbsp;two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to the first two<br>
&nbsp;&nbsp;&nbsp;&nbsp;characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"O"<br>
ELSE<br>
IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'T2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL 'T' AND at least one instance of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is EQUAL to 'T2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL112 OR the first two characters of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF at least one instance of /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment/country is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'AD' OR IF the first two characters of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to 'AD'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfTransitDeclared&nbsp;=&nbsp;"O"


## C0035

**Functional Description**

IF (&lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL112 (CountryCodesCTC))<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-PREVIOUS DOCUMENT&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT&gt;&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for all Consignment Items<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS DOCUMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;= "O";<br>
IF (&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;{T2, T2F} AND the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is in SET CL112 (CountryCodesCTC))<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF &lt;CONSIGNMENT-PREVIOUS DOCUMENT&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT&gt;&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for this Consignment Item<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS DOCUMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;= "O" for this Consignment Item

**Technical Description**

IF (/<span>&#42;</span>/Transit Operation/declarationType is in SET {T2, T2F}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL112)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/PreviousDocument is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for all Consignment Items<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument&nbsp;=&nbsp;"O";<br>
IF (/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2, T2F} AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL112)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/Consignment/PreviousDocument is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for this Consignment Item<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;for this Consignment Item


## C0040

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT &gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/Transhipment/containerIndicator is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/TransportEquipment&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/TransportEquipment&nbsp;=&nbsp;"O"


## C0045

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'T'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'T'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType&nbsp;=&nbsp;"N"


## C0055

**Functional Description**

IF &lt;CONSIGNMENT.Container indicator&gt; is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Container identification number&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;at least one iteration of &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Container identification<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&gt;&nbsp;=&nbsp;"R" (for the rest of iterations is optional)

**Technical Description**

IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/TransportEquipment/containerIdentificationNumber&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;at least one iteration of /<span>&#42;</span>/Consignment/TransportEquipment/containerIdentificationNumber&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;(for the rest of iterations is optional)


## C0060

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Type of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt; is in SET CL181 (KindOfPackagesBulk)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Shipping marks&gt; =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Type of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt; is in SET CL182 (KindOfPackagesUnpacked)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Shipping marks&gt; =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Shipping marks&gt; =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages is in SET CL181<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL182<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks ="R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages&nbsp;=&nbsp;"R"


## C0085

**Functional Description**

IF &lt;GUARANTEE.Guarantee type&gt; is in SET CL076 (GuaranteeTypeWithReference)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTEE.GUARANTEE REFERENCE&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE.GUARANTEE REFERENCE&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Guarantee/guaranteeType is in SET CL076<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Guarantee/GuaranteeReference&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantee/GuaranteeReference&nbsp;=&nbsp;"N"


## C0086

**Functional Description**

IF &lt;GUARANTEE.Guarantee type&gt; is in SET CL286 (GuaranteeTypeWithGRN)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE.GUARANTEE REFERENCE.GRN&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE.GUARANTEE REFERENCE.Access code&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE.GUARANTEE REFERENCE.GRN&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE.GUARANTEE REFERENCE.Access code&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Guarantee/guaranteeType is in SET CL286<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Guarantee/GuaranteeReference/GRN&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantee/GuaranteeReference/accessCode&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantee/GuaranteeReference/GRN&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantee/GuaranteeReference/accessCode&nbsp;=&nbsp;"N"


## C0101

**Functional Description**

IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;AUTHORISATION&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;AUTHORISATION&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Authorisation&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Authorisation&nbsp;=&nbsp;"O"


## C0102

**Functional Description**

IF &lt;TRANSIT OPERATION.Simplified procedure&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC007C-AUTHORISATION&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC007C-AUTHORISATION&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/simplifiedProcedure is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC007C/Authorisation&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC007C/Authorisation&nbsp;=&nbsp;"N"


## C0128

**Functional Description**

IF the first three characters of &lt;Message recipient&gt; is EQUAL to 'NTA'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;INVALIDATION.Decision&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;INVALIDATION.Decision&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF the first three characters of /<span>&#42;</span>/messageRecipient is EQUAL to 'NTA'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Invalidation/decision&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Invalidation/decision&nbsp;=&nbsp;"R"


## C0129

**Functional Description**

IF &lt;INVALIDATION.Initiated by customs&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;INVALIDATION.Request date and time&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;INVALIDATION.Request date and time&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Invalidation/initiatedByCustoms is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Invalidation/requestDateAndTime&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Invalidation/requestDateAndTime&nbsp;=&nbsp;"R"


## C0130

**Functional Description**

IF &lt;GUARANTEE.Guarantee type&gt; is EQUAL to '8'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTEE.Other guarantee reference&gt;&nbsp;=&nbsp;"R"<br>
ELSE IF &lt;GUARANTEE.Guarantee type&gt; is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTEE.Other guarantee reference&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE.Other guarantee reference&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to '8'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Guarantee/otherGuaranteeReference&nbsp;=&nbsp;"R"<br>
ELSE IF /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Guarantee/otherGuaranteeReference&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantee/otherGuaranteeReference&nbsp;=&nbsp;"N"


## C0137

**Functional Description**

IF the first three characters of &lt;Message recipient&gt; is EQUAL to 'NTA'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;INVALIDATION.Justification&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;INVALIDATION.Justification&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF the first three characters of /<span>&#42;</span>/messageRecipient is EQUAL to 'NTA'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Invalidation/justification&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Invalidation/justification&nbsp;=&nbsp;"O"


## C0153

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL TO 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; IS NOT EQUAL TO<br>
&nbsp;&nbsp;&nbsp;&nbsp;'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY CODE&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY CODE&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL TO 'TIR' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/type IS NOT EQUAL to 'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode&nbsp;=&nbsp;"R"


## C0154

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY.Commodity code&gt;&nbsp;=&nbsp;"R"<br>
ELSE IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL TO 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; IS NOT EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'N830' (Goods declaration for exportation)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY.Commodity code&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY.Commodity code&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode&nbsp;=&nbsp;"R"<br>
ELSE IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/type IS NOT EQUAL to 'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode&nbsp;=&nbsp;"R"


## C0170

**Functional Description**

IF (&lt;CC015C-TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CCA15D-TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1' OR &lt;CC013C-<br>
&nbsp;&nbsp;&nbsp;&nbsp;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CCA13D-TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT.Inland mode of transport&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-CONSIGNMENT.Inland mode of transport&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF (/CC015C/TransitOperation/reducedDatasetIndicator is EQUAL to '1' OR /CCA15D/Transit<br>
&nbsp;&nbsp;&nbsp;&nbsp;Operation/reducedDatasetIndicator is EQUAL to '1' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC013C/TransitOperation/reducedDatasetIndicator is EQUAL to '1' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/TransitOperation/reducedDatasetIndicator is EQUAL to '1')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/inlandModeOfTransport&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/Consignment/inlandModeOfTransport&nbsp;=&nbsp;"O"


## C0186

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to ’0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-TRANSPORT CHARGES&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-TRANSPORT CHARGES&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/TransportCharges&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/TransportCharges&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges&nbsp;=&nbsp;"O"


## C0191

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF UNLOADING&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF UNLOADING&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF UNLOADING&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfUnloading&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF /<span>&#42;</span>/TransitOperation/security is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfUnloading&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfUnloading&nbsp;=&nbsp;"O"


## C0215

**Functional Description**

IF &lt;CC141C-ENQUIRY.Text&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CC141C-CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC141C-CONSIGNMENT&gt;&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC141C-CONSIGNMENT&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC141C-CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt;&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC141C-CONSIGNMENT&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /CC141C/Enquiry/text is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /CC141C/CustomsOfficeOfDestinationActual is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC141C/Consignment&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CC141C/Consignment&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC141C/CustomsOfficeOfDestinationActual&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /CC141C/Consignment&nbsp;=&nbsp;"N"


## C0220

**Functional Description**

IF &lt;CC141C-ENQUIRY.TC11 delivery date&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC141C-ENQUIRY.Text&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC141C-ENQUIRY.Text&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /CC141C/Enquiry/TC11DeliveryDate is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC141C/Enquiry/text&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC141C/Enquiry/text&nbsp;=&nbsp;"O"


## C0240

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT.Code&gt; is in SET {2, 4, 7}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-INCIDENT.Code&gt; is in SET {3, 6, 8}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/code is in SET {2, 4, 7}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Incident/TransportEquipment&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Transhipment&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/Incident/code is in SET {3, 6, 8}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Incident/TransportEquipment&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Transhipment&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/TransportEquipment&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/ Consignment/Incident/Transhipment&nbsp;=&nbsp;"N"


## C0250

**Functional Description**

IF &lt;HOLDER OF THE TRANSIT PROCEDURE.Identification number&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;HOLDER OF THE TRANSIT PROCEDURE.Identification number&gt; is a valid identifier in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;European EOS (Economic Operators Systems) verified by the EU Member State receiving or sending<br>
&nbsp;&nbsp;&nbsp;&nbsp;this message), OR is a valid identifier in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;HOLDER OF THE TRANSIT PROCEDURE.Name&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;HOLDER OF THE TRANSIT PROCEDURE.Name&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-CONSIGNOR.Identification number&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CONSIGNMENT-CONSIGNOR.Identification number&gt; is a valid identifier in the European EOS<br>
&nbsp;&nbsp;&nbsp;&nbsp;(Economic Operators Systems) verified by the EU Member State receiving or sending this message),<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR is a valid identifier in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNOR.Name&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNOR-ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNOR.Name&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNOR-ADDRESS&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-CONSIGNEE.Identification number&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CONSIGNMENT-CONSIGNEE.Identification number&gt; is a valid identifier in the European EOS<br>
&nbsp;&nbsp;&nbsp;&nbsp;(Economic Operators Systems) verified by the EU Member State receiving or sending this message),<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR is a valid identifier in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNEE.Name&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNEE-ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNEE.Name&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNEE-ADDRESS&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR.Identification number&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR.Identification number is a valid<br>
&nbsp;&nbsp;&nbsp;&nbsp;identifier in the European EOS (Economic Operators Systems) verified by the EU Member State<br>
&nbsp;&nbsp;&nbsp;&nbsp;receiving or sending this message), OR is a valid identifier in the DB of the CTC country receiving or<br>
&nbsp;&nbsp;&nbsp;&nbsp;sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR.Name&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR.Name&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE.Identification number&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE.Identification number&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is a valid identifier in the European EOS (Economic Operators Systems) verified by the EU Member<br>
&nbsp;&nbsp;&nbsp;&nbsp;State receiving or sending this message), OR is a valid identifier in the DB of the CTC country<br>
&nbsp;&nbsp;&nbsp;&nbsp;receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE.Name&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE.Name&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;GUARANTOR.Identification number&gt; is PRESENT AND &lt;GUARANTOR.Identification number&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is a valid identifier in the European EOS (Economic Operators Systems) verified by the EU Member<br>
&nbsp;&nbsp;&nbsp;&nbsp;State receiving or sending this message), OR is a valid identifier in the DB of the CTC country<br>
&nbsp;&nbsp;&nbsp;&nbsp;receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTOR.Name&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTOR-ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTOR.Name&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTOR-ADDRESS&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/HolderOfTheTransitProcedure/identificationNumber is PRESENT AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/HolderOfTheTransitProcedure/identificationNumber is a valid identifier in the European EOS<br>
&nbsp;&nbsp;&nbsp;&nbsp;(Economic Operators Systems) verified by the EU Member State receiving or sending this message),<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR is a valid identifier in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/HolderOfTheTransitProcedure/name="N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/HolderOfTheTransitProcedure/Address="N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/HolderOfTheTransitProcedure/name="R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/HolderOfTheTransitProcedure/Address="R";<br>
IF /<span>&#42;</span>/Consignment/Consignor/identificationNumber is PRESENT AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignor/identificationNumber is a valid identifier in the European EOS (Economic<br>
&nbsp;&nbsp;&nbsp;&nbsp;Operators Systems) verified by the EU Member State receiving or sending this message), OR is a valid<br>
&nbsp;&nbsp;&nbsp;&nbsp;identifier in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignor/name="N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignor/Address="N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignor/name="R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignor/Address="R";<br>
IF /<span>&#42;</span>/Consignment/Consignee/identificationNumber is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/Consignee/identificationNumber is a valid identifier in the European EOS<br>
&nbsp;&nbsp;&nbsp;&nbsp;(Economic Operators Systems) verified by the EU Member State receiving or sending this message),<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR is a valid identifier in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignee/name="N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignee/Address="N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignee/name="R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignee/Address="R";<br>
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/identificationNumber is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/identificationNumber is a valid identifier in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;European EOS (Economic Operators Systems) verified by the EU Member State receiving or sending<br>
&nbsp;&nbsp;&nbsp;&nbsp;this message), OR is a valid identifier in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignor/name="N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address="N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignor/name="R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address="R";<br>
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/identificationNumber is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/identificationNumber is a valid identifier in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;European EOS (Economic Operators Systems) verified by the EU Member State receiving or sending<br>
&nbsp;&nbsp;&nbsp;&nbsp;this message), OR is a valid identifier in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee/name="N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address="N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee/name="R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address="R";<br>
IF /<span>&#42;</span>/Guarantor/identificationNumber is PRESENT AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantor/identificationNumber is a valid identifier in the European EOS (Economic Operators<br>
&nbsp;&nbsp;&nbsp;&nbsp;Systems) verified by the EU Member State receiving or sending this message), OR is a valid identifier<br>
&nbsp;&nbsp;&nbsp;&nbsp;in the DB of the CTC country receiving or sending this message<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantor/name="N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantor/Address="N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantor/name="R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantor/Address="R";


## C0298

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT.Quantity&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT.Measurement unit and qualifier&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT.Measurement unit and qualifier&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/quantity&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/measurementUnitAndQualifi<br>
&nbsp;&nbsp;&nbsp;&nbsp;er&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/measurementUnitAndQualifi<br>
&nbsp;&nbsp;&nbsp;&nbsp;er&nbsp;=&nbsp;"N"


## C0315

**Functional Description**

IF &lt;CC141C-ENQUIRY.TC11 delivery date&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC141C-CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC141C-CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /CC141C/ENQUIRY/TC11DeliveryDate is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC141C/CustomsOfficeOfDestinationActual&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC141C/CustomsOfficeOfDestinationActual= "O"


## C0337

**Functional Description**

IF &lt;CONSIGNMENT-TRANSPORT CHARGES&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT CHARGES&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;= "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/TransportCharges is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges&nbsp;=&nbsp;"O"


## C0339

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/DepartureTransportMeans&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF/<span>&#42;</span>/Consignment/DepartureTransportMeans is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"O"


## C0343

**Functional Description**

IF &lt;CONSIGNMENT.Country of destination&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of destination&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt; CONSIGNMENT-HOUSE CONSIGNMENT.Country of destination is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination&gt; =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination&gt; =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDestination is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDestination&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDestination is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination&nbsp;=&nbsp;"R"


## C0349

**Functional Description**

IF &lt;CONSIGNMENT-CONSIGNOR&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Consignor is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignor&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignor&nbsp;=&nbsp;"O"


## C0352

**Functional Description**

IF &lt;TRANSIT OPERATION.Release indicator&gt; is in SET {2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/releaseIndicator is in SET {2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment&nbsp;=&nbsp;"N"


## C0353

**Functional Description**

IF &lt;CONSIGNMENT.HOUSE CONSIGNMENT.Release type &gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT ITEM&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT ITEM&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/releaseType is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem&nbsp;=&nbsp;"N"


## C0382

**Functional Description**

IF &lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS.Country&gt; is in SET CL198<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryAddressPostcodeOnly)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-LOCATION OF GOODS- POSTCODE ADDRESS.House number&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS- POSTCODE ADDRESS.House number&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress/country is in SET CL198<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress/houseNumber&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress/houseNumber&nbsp;=&nbsp;"R"


## C0387

**Functional Description**

IF &lt;CONSIGNMENT-PLACE OF LOADING.UN LOCODE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-PLACE OF LOADING.Country&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF LOADING.Location&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF LOADING.Country&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF LOADING.Location&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-PLACE OF UNLOADING.UN LOCODE&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-PLACE OF UNLOADING.Country&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF UNLOADING.Location&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF UNLOADING.Country&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF UNLOADING.Location&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/PlaceOfLoading/UNLocode is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/PlaceOfLoading/country&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfLoading/location&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfLoading/country&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfLoading/location&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Consignment/PlaceOfUnloading/UNLocode is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/PlaceOfUnloading/country&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfUnloading/location&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfUnloading/country&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfUnloading/location&nbsp;=&nbsp;"R"


## C0394

**Functional Description**

IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'Z'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'X'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'Y'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'W'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'V'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'U'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-LOCATION OF GOODS.Qualifier of identification&gt; is EQUAL to 'T'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.UN LOCODE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CUSTOMS OFFICE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-GNSS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-CONTACT PERSON&gt;&nbsp;=&nbsp;"O" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-POSTCODE ADDRESS&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'Z'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/Address&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'X'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'Y'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'W'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/GNSS&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'V'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'U'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/Address&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/LocationOfGoods/qualifierOfIdentification is EQUAL to 'T'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/Address&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/UNLocode&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/CustomsOffice&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/GNSS&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/ContactPerson&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/LocationOfGoods/PostcodeAddress&nbsp;=&nbsp;"R"


## C0396

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT.Code&gt; is in SET {2, 7}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/code is in SET {2, 7}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Incident/TransportEquipment/numberOfSeals&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/TransportEquipment/numberOfSeals&nbsp;=&nbsp;"O"


## C0409

**Functional Description**

IF &lt;TRANSIT OPERATION.Additional declaration type&gt;&nbsp;=&nbsp;"D"<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT.Place of loading&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL289 (CountryPlaceOfLoadingNotRequired)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-PLACE OF LOADING&gt; &nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT.Place of loading&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/additionalDeclarationType&nbsp;=&nbsp;"D"<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/PlaceOfLoading&nbsp;=&nbsp;"O"<br>
ELSE<br>
IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL289<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/PlaceOfLoading&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfLoading&nbsp;=&nbsp;"R"


## C0410

**Functional Description**

IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL289 (CountryPlaceOfLoadingNotRequired)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-PLACE OF LOADING&gt; &nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF LOADING&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL289<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/PlaceOfLoading&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfLoading&nbsp;=&nbsp;"R"


## C0411

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.TIR carnet number&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.TIR carnet number&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/TIRCarnetNumber&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/TIRCarnetNumber&nbsp;=&nbsp;"N"


## C0412

**Functional Description**

IF (&lt;CC015C-CONSIGNMENT-PLACE OF LOADING&gt; is PRESENT OR &lt;CCA15D-CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;PLACE OF LOADING&gt; is PRESENT OR &lt;CC013C-CONSIGNMENT-PLACE OF LOADING&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT OR &lt;CCA13D-CONSIGNMENT-PLACE OF LOADING&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT-PLACE OF LOADING&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
IF (&lt;CCA15D-TRANSIT OPERATION.Security&gt; is in SET {0,2} OR &lt;CCA13D- TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OPERATION.Security&gt; is in SET {0,2}) AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL289(CountryPlaceOfLoadingNotRequired)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-PLACE OF LOADING&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-PLACE OF LOADING&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF (/CC015C/Consignment/PlaceOfLoading is PRESENT OR /CCA15D/Consignment/PlaceOfLoading<br>
&nbsp;&nbsp;&nbsp;&nbsp;is PRESENT OR /CC013C/Consignment/PlaceOfLoading is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/Consignment/PlaceOfLoading is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/PlaceOfLoading&nbsp;=&nbsp;"O"<br>
ELSE<br>
IF (/CCA15D/TransitOperation/security is in SET {0,2} OR /CCA13D/TransitOperation/security is in<br>
&nbsp;&nbsp;&nbsp;&nbsp;SET {0,2}) AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL289<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/PlaceOfLoading&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/PlaceOfLoading&nbsp;=&nbsp;"R"


## C0440

**Functional Description**

IF &lt;CC043C-CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is NOT EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR &lt;CC043C-CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals&gt; is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC044C-UNLOADING REMARK.State of seals&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC044C-UNLOADING REMARK.State of seals&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /CC043C/Consignment/TransportEquipment/numberOfSeals is NOT EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR /CC043C/Consignment/Incident/TransportEquipment/numberOfSeals is NOT EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC044C/UnloadingRemark/stateOfSeals&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC044C/UnloadingRemark/stateOfSeals&nbsp;=&nbsp;"N"


## C0451

**Functional Description**

IF &lt;MESSAGE-TYPE OF CONTROLS.Type&gt; is EQUAL to '50'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;MESSAGE-TYPE OF CONTROLS.Text&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;MESSAGE-TYPE OF CONTROLS.Text&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TypeOfControls/type is EQUAL to '50'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TypeOfControls/text&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TypeOfControls/text&nbsp;=&nbsp;"O"


## C0452

**Functional Description**

IF &lt;MESSAGE-TRANSIT OPERATION.Notification type&gt; is in SET {1, 2}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;MESSAGE-TYPE OF CONTROLS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;MESSAGE-TYPE OF CONTROLS&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/notificationType is in SET {1, 2}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TypeOfControls&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TypeOfControls&nbsp;=&nbsp;"R"


## C0455

**Functional Description**

IF &lt;MESSAGE-TransitOperation.Notification type&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;MESSAGE-REQUESTED DOCUMENT&gt;&nbsp;=&nbsp;"R"<br>
ELSE IF &lt;MESSAGE-TRANSIT OPERATION.Notification type&gt; is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;MESSAGE-REQUESTED DOCUMENT&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;MESSAGE-REQUESTED DOCUMENT&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/notificationType is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/RequestedDocument&nbsp;=&nbsp;"R"<br>
ELSE IF /<span>&#42;</span>/TransitOperation/notificationType is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/RequestedDocument&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/RequestedDocument&nbsp;=&nbsp;"N"


## C0460

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT-LOCATION.Qualifier of identification&gt; is EQUAL to 'W'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION-GNSS&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION.UN LOCODE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION -ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-INCIDENT-LOCATION.Qualifier of identification&gt; is EQUAL to 'U'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION.UN LOCODE&gt;= "R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION-GNSS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION-ADDRESS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-INCIDENT-LOCATION.Qualifier of identification&gt; is EQUAL to 'Z'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION-ADDRESS&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION.UN LOCODE&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION-GNSS&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'W'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/GNSS&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/UNLocode&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/Address&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'U'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/UNLocode&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/GNSS&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/Address&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/Incident/Location/qualifierOfIdentification is EQUAL to 'Z'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/Address&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/UNLocode&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/GNSS&nbsp;=&nbsp;"N"


## C0467

**Functional Description**

IF (&lt;CC028C-TRANSIT OPERATION.Declaration acceptance date&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR &lt;CC028D-TRANSIT OPERATION.Declaration acceptance date&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.MRN&gt;&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.LRN&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.MRN&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.LRN&gt;&nbsp;=&nbsp;"R"

**Technical Description**

'IF (/CC028C/TransitOperation/declarationAcceptanceDate&gt; is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC028D/TransitOperation/declarationAcceptanceDate&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/MRN&nbsp;=&nbsp;"R" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/LRN&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/MRN&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/LRN&nbsp;=&nbsp;"R"


## C0489

**Functional Description**

IF (the country code (first two characters) in the &lt;CCA29D-CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE.Reference number&gt; is in SET CL147<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryCustomsSecurityAgreementArea)) OR  (the country code (first two characters) in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC029C-CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in SET CL147<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryCustomsSecurityAgreementArea))<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC029C-CONSIGNMENT-LOCATION OF GOODS&gt;&nbsp;=&nbsp;"O" AND &lt;CCA29D-CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;LOCATION OF GOODS&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC029C-CONSIGNMENT-LOCATION OF GOODS&gt;&nbsp;=&nbsp;"R" AND &lt;CCA29D-CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;LOCATION OF GOODS&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF (the first two characters of the /CC029C/CustomsOfficeOfDeparture/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL147) OR (the first two characters of the /CCA29D/CustomsOfficeOfDeparture/referenceNumber is in<br>
&nbsp;&nbsp;&nbsp;&nbsp;SET CL147)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC029C/Consignment/LocationOfGoods&nbsp;=&nbsp;"O" AND /CCA29D/Consignment/LocationOfGoods<br>
&nbsp;&nbsp;&nbsp;&nbsp;= "O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC029C/Consignment/LocationOfGoods&nbsp;=&nbsp;"R" AND /CCA29D/Consignment/LocationOfGoods<br>
&nbsp;&nbsp;&nbsp;&nbsp;= "R"


## C0492

**Functional Description**

IF &lt;TRANSIT OPERATION.Rejection code&gt; is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Rejection reason&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Rejection reason&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/rejectionCode is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/rejectionReason&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/rejectionReason&nbsp;=&nbsp;"O"


## C0495

**Functional Description**

IF &lt;CCA15D - TRANSIT OPERATION.Security&gt; is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Rejection reason&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;TRANSIT OPERATION.Rejection code&gt; is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Rejection reason&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Rejection reason&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /CCA15D/TransitOperation/security is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/rejectionReason&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/TransitOperation/rejectionCode is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/rejectionReason&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/rejectionReason&nbsp;=&nbsp;"O"


## C0502

**Functional Description**

IF &lt;CONSIGNMENT.Reference number UCR&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Reference number<br>
&nbsp;&nbsp;&nbsp;&nbsp;UCR&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;ITEM.Reference number UCR&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Reference number UCR&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;ITEM.Reference number UCR&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF (&lt;CONSIGNMENT-TRANSPORT DOCUMENT&gt; is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT DOCUMENT&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;ITEM.Reference number UCR&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Reference number UCR&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/referenceNumberUCR is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/referenceNumberUCR&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/referenceNumberUCR is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;"N"<br>
ELSE IF (/<span>&#42;</span>/Consignment/TransportDocument is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/TransportDocument is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR= "R"


## C0505

**Functional Description**

IF &lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS.Country&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL505(CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;HOLDER OF THE TRANSIT PROCEDURE-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-CONSIGNOR-ADDRESS.Country&gt; is in SET CL505 (CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-CONSIGNOR-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNOR-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-CONSIGNEE-ADDRESS.Country&gt; is in SET CL505 (CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-CONSIGNEE-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNEE-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-INCIDENT-LOCATION.Country&gt; is in SET CL505 (CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-INCIDENT-LOCATION-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-LOCATION-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS.Country&gt; is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS.Country&gt; is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS.Country&gt; is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;GUARANTOR-ADDRESS.Country&gt; is in SET CL505 (CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTOR-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTOR-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;GUARANTEE REFERENCE-GUARANTOR-ADDRESS.Country&gt; is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTEE REFERENCE-GUARANTOR-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE REFERENCE-GUARANTOR-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;GUARANTEE REFERENCE-GUARANTOR-AGENT IN COUNTRY OF COMPETENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AUTHORITY-ADDRESS.Country&gt; is in SET CL505 (CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTEE REFERENCE-GUARANTOR-AGENT IN COUNTRY OF COMPETENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AYTHORITY-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE REFERENCE-GUARANTOR-AGENT IN COUNTRY OF COMPETENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AYTHORITY-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;GUARANTEE REFERENCE-OWNER-ADDRESS.Country&gt; is in SET CL505 (CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTEE REFERENCE-OWNER-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE REFERENCE-OWNER-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R";<br>
IF &lt;CONSIGNMENT-CONSIGNEE (ACTUAL)-ADDRESS.Country&gt; is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryWithoutZip)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-CONSIGNEE(ACTUAL)-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNEE(ACTUAL)-ADDRESS.Postcode&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/HolderOfTheTransitProcedure/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/HolderOfTheTransitProcedure/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/HolderOfTheTransitProcedure/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Consignment/Consignor/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Consignor/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignor/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Consignment/Consignee/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Consignee/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignee/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Consignment/Incident/Location/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/Incident/Location/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/Location/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Consignment/LocationOfGoods/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/LocationOfGoods/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignor/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignee/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Guarantor/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Guarantor/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantor/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/GuaranteeReference/Guarantor/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/GuaranteeReference/Guarantor/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/GuaranteeReference/Guarantor/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/GuaranteeReference/Guarantor/AgentInCountryOfCompetentAuthority/Address/country is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/GuaranteeReference/Guarantor/AgentInCountryOfCompetentAuthority/Address/postcode =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/GuaranteeReference/Guarantor/AgentInCountryOfCompetentAuthority/Address/postcode =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"R";<br>
IF /<span>&#42;</span>/GuaranteeReference/Owner/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/GuaranteeReference/Owner/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/GuaranteeReference/Owner/Address/postcode&nbsp;=&nbsp;"R";<br>
IF /<span>&#42;</span>/Consignment/ConsigneeActual/Address/country is in SET CL505<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/ConsigneeActual/Address/postcode&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/ConsigneeActual/Address/postcode&nbsp;=&nbsp;"R"


## C0511

**Functional Description**

IF &lt;Message type&gt; is in SET CL610 (MessageWithCorrelationIdentifier)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;Correlation identifier&gt;&nbsp;=&nbsp;"R"<br>
ELSE IF &lt;Message type&gt; is in SET CL385 (MessageTypeWithoutHeader)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;Correlation identifier&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;Correlation identifier&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/messageType is in SET CL610<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/correlationIdentifier&nbsp;=&nbsp;"R"<br>
ELSE IF /<span>&#42;</span>/messageType is in SET CL385<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/correlationIdentifier&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/correlationIdentifier&nbsp;=&nbsp;"O"


## C0531

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Conveyance reference number&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Conveyance reference number&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber&nbsp;=&nbsp;"O"


## C0542

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to '0' AND &lt;TRANSIT OPERATION.Reduced dataset<br>
&nbsp;&nbsp;&nbsp;&nbsp;indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-CONSIGNOR&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF &lt;CONSIGNMENT-CONSIGNOR&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is EQUAL to '0' AND /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator is<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Consignor&nbsp;=&nbsp;"N" AND /<span>&#42;</span>/Consignment/HouseConsignment/Consignor&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF /<span>&#42;</span>/Consignment/Consignor is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/Consignor&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/Consignor&nbsp;=&nbsp;"O"


## C0569

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT-SEAL&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT-SEAL&gt;&nbsp;=&nbsp;"N";<br>
IF &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT-SEAL&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-TRANSPORT EQUIPMENT-SEAL&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/TransportEquipment/numberOfSeals is GREATER than '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/TransportEquipment/Seal&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/TransportEquipment/Seal&nbsp;=&nbsp;"N";<br>
IF /<span>&#42;</span>/Consignment/TransportEquipment/numberOfSeals is GREATER than '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/TransportEquipment/Seal&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/TransportEquipment/Seal&nbsp;=&nbsp;"N"


## C0586

**Functional Description**

IF &lt;TRANSIT OPERATION.Binding itinerary&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-COUNTRY OF ROUTING OF CONSIGNMENT&gt;&nbsp;=&nbsp;"R"<br>
ELSE IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 2, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-COUNTRY OF ROUTING OF CONSIGNMENT&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-COUNTRY OF ROUTING OF CONSIGNMENT&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/bindingItinerary is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment&nbsp;=&nbsp;"R"<br>
ELSE IF /<span>&#42;</span>/Transit Operation/security is in SET {1, 2, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/CountryOfRoutingOfConsignment&nbsp;=&nbsp;"O"


## C0587

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND the first two characters of at least one iteration of the &lt;CUSTOMS OFFICE OF TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is NOT in SET CL147 (CountryCustomsSecurityAgreementArea)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND the first two characters of at least one iteration of the<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is NOT in SET CL147<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared&nbsp;=&nbsp;"N"


## C0598

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 3} AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;the country code (first two characters) in the &lt;CUSTOMS OFFICE OF TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is in SET CL147 (CountryCustomsSecurityAgreementArea)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is in SET {1, 3} AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;the first two characters of the /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is in SET CL147<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated ="R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated&nbsp;=&nbsp;"O"


## C0599

**Functional Description**

IF &lt;TRANSIT OPERATION.Security&gt; is EQUAL to '2' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to 'A'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT.Mode of transport at the border&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT.Mode of transport at the border&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/security is EQUAL to '2' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to 'A'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder&nbsp;=&nbsp;"O"


## C0600

**Functional Description**

IF &lt;CC015C-TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT.Mode of transport at the border&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-CONSIGNMENT.Mode of transport at the border&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /CC015C/TransitOperation/security is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/modeOfTransportAtTheBorder&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/Consignment/modeOfTransportAtTheBorder&nbsp;=&nbsp;"O"


## C0670

**Functional Description**

IF &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt; is PRESENT only once<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT-GOODS REFERENCE&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-TRANSPORT EQUIPMENT-GOODS REFERENCE&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/TransportEquipment is PRESENT only once<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/TransportEquipment/GoodsReference&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/TransportEquipment/GoodsReference&nbsp;=&nbsp;"R"


## C0671

**Functional Description**

IF &lt;CONSIGNMENT-LOCATION OF GOODS-ECONOMIC OPERATOR.Identification number&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR &lt;CONSIGNMENT-LOCATION OF GOODS.Authorisation number&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-LOCATION OF GOODS.Additional identifier&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS.Additional identifier&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/LocationOfGoods/EconomicOperator/identificationNumber is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR /<span>&#42;</span>/Consignment/LocationOfGoods/authorisationNumber is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/LocationOfGoods/additionalIdentifier&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods/additionalIdentifier&nbsp;=&nbsp;"N"


## C0710

**Functional Description**

IF &lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to 'D'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-LOCATION OF GOODS&gt;&nbsp;=&nbsp;"O"<br>
ELSE IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE.Reference number&gt; is in SET CL147(CountryCustomsSecurityAgreementArea)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-LOCATION OF GOODS&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-LOCATION OF GOODS&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/Additional declaration type is EQUAL to 'D'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/LocationOfGoods&nbsp;=&nbsp;"O"<br>
ELSE IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL147<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/LocationOfGoods&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/LocationOfGoods&nbsp;=&nbsp;"R"


## C0806

**Functional Description**

IF &lt;CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF (&lt;TRANSIT OPERATION.Security&gt; is EQUAL to '2' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to 'A')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; =  "O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF (/<span>&#42;</span>/TransitOperation/security is EQUAL to '2' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to 'A')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"O"


## C0807

**Functional Description**

IF &lt;CC170C-CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF &lt;CC015C-TRANSIT OPERATION.Security&gt; is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC013C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CC015C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /CC170C/Consignment/modeOfTransportAtTheBorder is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF /CC015C/TransitOperation/security is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /CC013C/Consignment/ActiveBorderTransportMeans is NOT PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /CC015C/Consignment/ActiveBorderTransportMeans is NOT PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"O"


## C0808

**Functional Description**

IF (&lt;CC015C-TRANSIT OPERATION.Security&gt; is in SET {1,2,3} OR &lt;CCA15D-TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OPERATION.Security&gt; is in SET {1,2,3})<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '4' (Air)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Conveyance reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Conveyance reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF (/CC015C/TransitOperation/security is in SET {1,2,3} OR /CCA15D/TransitOperation/security is in<br>
&nbsp;&nbsp;&nbsp;&nbsp;SET {1,2,3})<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/Consignment/modeOfTransportAtTheBorder is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/Consignment/ActiveBorderTransportMeans/conveyanceReferenceNumber&nbsp;=&nbsp;"O"


## C0816

**Functional Description**

IF the &lt;CUSTOMS OFFICE OF DEPARTURE&gt; (for the CC017C) or the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;DESTINATION (ACTUAL)&gt; [for the CD018C and CC044C] is located in a CTC country or AD or SM<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY<br>
&nbsp;&nbsp;&nbsp;&nbsp;CODE.Combined nomenclature code&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY<br>
&nbsp;&nbsp;&nbsp;&nbsp;CODE.Combined nomenclature code&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF the /<span>&#42;</span>/CustomsOfficeOfDeparture (for the CC017C) or the /<span>&#42;</span>/CustomsOfficeOfDestinationActual [for<br>
&nbsp;&nbsp;&nbsp;&nbsp;the CD018C and CC044C] is located in a CTC country or AD or SM<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl<br>
&nbsp;&nbsp;&nbsp;&nbsp;atureCode= "N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl<br>
&nbsp;&nbsp;&nbsp;&nbsp;atureCode= "O"


## C0820

**Functional Description**

IF &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one iteration of &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Container<br>
&nbsp;&nbsp;&nbsp;&nbsp;identification number&gt;&nbsp;=&nbsp;"R" (for the rest of iterations is optional)<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Container identification number&gt; =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/Incident/Transhipment/containerIndicator is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one iteration of /<span>&#42;</span>/ Consignment/<br>
&nbsp;&nbsp;&nbsp;&nbsp;Incident/TransportEquipment/containerIdentificationNumber&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;(for the rest of iterations is optional)<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/Incident/TransportEquipment/containerIdentificationNumber&nbsp;=&nbsp;"O"


## C0821

**Functional Description**

IF country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&gt; is in SET CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryCodesCTC)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY CODE.Combined nomenclature code&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY CODE.Combined nomenclature code&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl<br>
&nbsp;&nbsp;&nbsp;&nbsp;atureCode&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/CommodityCode/combinedNomencl<br>
&nbsp;&nbsp;&nbsp;&nbsp;atureCode&nbsp;=&nbsp;"O".


## C0822

**Functional Description**

IF &lt;TRANSIT OPERATION.Additional declaration type&gt; is EQUAL to 'D'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT.Container indicator&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT.Container indicator&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to 'D'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/containerIndicator&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/containerIndicator&nbsp;=&nbsp;"R"


## C0823

**Functional Description**

IF &lt;CONSIGNMENT.Container indicator&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT.Container indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/Consignment/containerIndicator is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/TransportEquipment&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/TransportEquipment&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/TransportEquipment&nbsp;=&nbsp;"N"


## C0824

**Functional Description**

IF (&lt;CC013C-TRANSIT OPERATION.Declaration type&gt; is PRESENT OR &lt;CCA13D-TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OPERATION.Declaration type&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF (&lt;CC013C-CONSIGNMENT.Container indicator&gt; is PRESENT or &lt;CCA13D-<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT.Container indicator&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT.Container indicator&gt;&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-CONSIGNMENT.Container indicator&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF (&lt;CC015C-CONSIGNMENT.Container indicator&gt; is PRESENT OR &lt;CCA15D-<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT.Container indicator&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT.Container indicator&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-CONSIGNMENT.Container indicator&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF (/CC013C/TransitOperation/declarationType is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/TransitOperation/declarationType is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF (/CC013C/Consignment/containerIndicator is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/Consignment/containerIndicator is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/containerIndicator&nbsp;=&nbsp;"O"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  /CC170C/Consignment/containerIndicator&nbsp;=&nbsp;"R"<br>
ELSE<br>
IF (/CC015C/Consignment/containerIndicator is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA15D/Consignment/containerIndicator is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/containerIndicator&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;  /CC170C/Consignment/containerIndicator&nbsp;=&nbsp;"R"


## C0826

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; = “N” AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/DepartureTransportMeans&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF /<span>&#42;</span>/Consignment/DepartureTransportMeans is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"O"


## C0833

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C -CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF (&lt;CC015C-CONSIGNMENT.DEPARTURE TRANSPORT MEANS&gt; is NOT PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CCA15D-CONSIGNMENT.DEPARTURE TRANSPORT MEANS&gt; is NOT PRESENT) AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;(&lt;CC015C-CONSIGNMENT.HOUSE CONSIGNMENT.DEPARTURE TRANSPORT MEANS&gt; is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT OR &lt;CCA15D-CONSIGNMENT.HOUSE CONSIGNMENT.DEPARTURE TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEANS&gt; is NOT PRESENT) AND (&lt;CC013C-CONSIGNMENT.DEPARTURE TRANSPORT MEANS&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;is NOT PRESENT OR &lt;CCA13D-CONSIGNMENT.DEPARTURE TRANSPORT MEANS&gt; is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT) AND (&lt;CC013C-CONSIGNMENT.HOUSE CONSIGNMENT. DEPARTURE TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEANS&gt; is NOT PRESENT OR &lt;CCA13D-CONSIGNMENT.HOUSE CONSIGNMENT. DEPARTURE<br>
&nbsp;&nbsp;&nbsp;&nbsp;TRANSPORT MEANS&gt; is NOT PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CC170C-CONSIGNMENT-DEPARTURE TRANSPORT   MEANS&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= "N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; =<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/Consignment/DepartureTransportMeans&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"N"<br>
ELSE IF (/CC015C/Consignment/DepartureTransportMeans is NOT PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA15D/Consignment/DepartureTransportMeans is NOT PRESENT) AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;(/CC015C/Consignment/HouseConsignment/DepartureTransportMeans is NOT PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA15D/Consignment/HouseConsignment/DepartureTransportMeans is NOT PRESENT) AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;(/CC013C/Consignment/DepartureTransportMeans is NOT PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/Consignment/DepartureTransportMeans is NOT PRESENT) AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;(/CC013C/Consignment/HouseConsignment/DepartureTransportMeans is NOT PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/Consignment/HouseConsignment/DepartureTransportMeans is NOT PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /CC170C/Consignment/DepartureTransportMeans is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"N"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/Consignment/HouseConsignment/DepartureTransportMeans&nbsp;=&nbsp;"O"


## C0837

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT. Type&gt; is EQUAL to 'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Net mass&gt;&nbsp;=&nbsp;"R"<br>
ELSE IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Net mass&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Net mass&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/type is EQUAL to 'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass&nbsp;=&nbsp;"R"<br>
ELSE IF /<span>&#42;</span>/ TransitOperation/reducedDatasetIndicator is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass&nbsp;=&nbsp;"O"


## C0839

**Functional Description**

IF &lt;AUTHORISATION.Type&gt; is NOT EQUAL to 'C521'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Limit date&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF &lt;Transit Operation/Additional declaration type&gt; is EQUAL to 'D'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Limit date&gt;&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Limit date&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Authorisation/type is NOT EQUAL to 'C521'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/limitDate&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF /<span>&#42;</span>/TransitOperation/additionalDeclarationType is EQUAL to 'D'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/limitDate&nbsp;=&nbsp;"O"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/limitDate&nbsp;=&nbsp;"R"


## C0840

**Functional Description**

IF (&lt;CC015C-AUTHORISATION.Type&gt; is NOT EQUAL to 'C521' OR &lt;CCA15D-<br>
&nbsp;&nbsp;&nbsp;&nbsp;AUTHORISATION.Type&gt; is NOT EQUAL to 'C521' OR &lt;CC013C-AUTHORISATION.Type&gt; is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to 'C521' OR &lt;CCA13D-AUTHORISATION.Type&gt; is NOT EQUAL to 'C521')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-TRANSIT OPERATION.Limit date&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF (&lt;CC015C-TRANSIT OPERATION.Limit date&gt; is NOT PRESENT OR &lt;CCA15D-TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OPERATION.Limit date&gt; is NOT PRESENT) AND (&lt;CC013C-TRANSIT OPERATION.Limit date&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;NOT PRESENT OR &lt;CCA13D-TRANSIT OPERATION.Limit date&gt; is NOT PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CC170C-TRANSIT OPERATION.Limit date&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC170C-TRANSIT OPERATION.Limit date&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF (/CC015C/Authorisation/type is NOT EQUAL to 'C521' OR /CCA15D/Authorisation/type is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to 'C521' OR /CC013C/Authorisation/type is NOT EQUAL to 'C521' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/Authorisation/type is NOT EQUAL to 'C521')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/TransitOperation/limitDate&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF (/CC015C/TransitOperation/limitDate is NOT PRESENT OR /CCA15D/TransitOperation/limitDate is<br>
&nbsp;&nbsp;&nbsp;&nbsp;NOT PRESENT) AND (/CC013C/TransitOperation/limitDate is NOT PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/TransitOperation/limitDate is NOT PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /CC170C/TransitOperation/limitDate&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC170C/TransitOperation/limitDate&nbsp;=&nbsp;"O"


## C0844

**Functional Description**

IF &lt;CD001C-CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT. Type&gt; OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CD003C-CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC025C -CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Net mass&gt;&nbsp;=&nbsp;"R"<br>
ELSE IF &lt;CD001C-TRANSIT OPERATION.Reduced dataset indicator&gt; OR &lt;CD003C-TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC025C -CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Net mass&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CC025C -CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Net mass&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /CD001C/Consignment/HouseConsignment/PreviousDocument/Type OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CD003C/Consignment/HouseConsignment/PreviousDocument/Type is EQUAL to 'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC025C/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass<br>
&nbsp;&nbsp;&nbsp;&nbsp;="R"<br>
ELSE IF /CD001C/TransitOperation/reducedDatasetIndicator OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CD003C/TransitOperation/reducedDatasetIndicator is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC025C/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass<br>
&nbsp;&nbsp;&nbsp;&nbsp;="N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC025C/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass<br>
&nbsp;&nbsp;&nbsp;&nbsp;="O"


## C0870

**Functional Description**

IF the first three characters of &lt;Message recipient&gt; is EQUAL to 'NTA'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;INVALIDATION.Decision date and time&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;INVALIDATION.Decision date and time&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF the first three characters of /<span>&#42;</span>/messageRecipient is EQUAL to 'NTA'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Invalidation/decisionDateAndTime&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Invalidation/decisionDateAndTime&nbsp;=&nbsp;"R"


## C0872

**Functional Description**

IF &lt;CONSIGNMENT.Container indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-TRANSPORT EQUIPMENT&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/TransportEquipment&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/TransportEquipment&nbsp;=&nbsp;"O"


## C0904

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;HOLDER OF THE TRANSIT PROCEDURE.TIR holder identification number&gt;&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;HOLDER OF THE TRANSIT PROCEDURE.TIR holder identification number&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF &lt;CC015C-TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR' OR &lt;CCA15D-TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;OPERATION.Declaration type&gt; is EQUAL to 'TIR' OR &lt;CC013C-TRANSIT OPERATION.Declaration<br>
&nbsp;&nbsp;&nbsp;&nbsp;type&gt; is EQUAL to 'TIR' OR &lt;CCA13D-TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;HOLDER OF THE TRANSIT PROCEDURE.TIR holder identification number&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;HOLDER OF THE TRANSIT PROCEDURE.TIR holder identification number&gt;&nbsp;=&nbsp;"N"

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber&nbsp;=&nbsp;"R"<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber&nbsp;=&nbsp;"N"<br>
ELSE IF /CC015C/TransitOperation/declarationType is EQUAL to 'TIR' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA15D/TransitOperation/declarationType is EQUAL to 'TIR' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CC013C/TransitOperation/declarationType is EQUAL to 'TIR' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/TransitOperation/declarationType is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/HolderOfTheTransitProcedure/TIRHolderIdentificationNumber&nbsp;=&nbsp;"N"


## C0908

**Functional Description**

IF &lt;CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt;&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF &lt;TRANSIT OPERATION.Security is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt;&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt;&nbsp;=&nbsp;"O"

**Technical Description**

IF /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '5'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"N"<br>
ELSE<br>
IF /<span>&#42;</span>/TransitOperation/security is in SET {1,2,3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"R"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/ActiveBorderTransportMeans&nbsp;=&nbsp;"O"


## C0909

**Functional Description**

IF &lt;CONSIGNMENT.Country of dispatch&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt;&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of<br>
&nbsp;&nbsp;&nbsp;&nbsp;dispatch&gt;&nbsp;=&nbsp;"N"<br>
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of dispatch&gt; =<br>
&nbsp;&nbsp;&nbsp;&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of dispatch&gt;&nbsp;=&nbsp;"R"

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDispatch is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch&nbsp;=&nbsp;"N" AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch&nbsp;=&nbsp;"N"<br>
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch&nbsp;=&nbsp;"N"<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch&nbsp;=&nbsp;"R"
