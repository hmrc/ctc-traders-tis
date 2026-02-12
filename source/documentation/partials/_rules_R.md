## R0003

**Functional Description**

Each &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Reference number&gt; is unique throughout the<br>
declaration.

**Technical Description**

Each /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is unique throughout the declaration.


## R0004

**Functional Description**

The value of &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; field<br>
is considered valid only if it is not LESS than or EQUAL to &lt;TRANSIT OPERATION.Release date&gt;

**Technical Description**

The value of /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated field is considered valid<br>
only if it is not LESS than or EQUAL to /<span>&#42;</span>/TransitOperation/releaseDate


## R0005

**Functional Description**

The value of &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; field<br>
is considered valid only if it is not LESS than or EQUAL to &lt;MESSAGE. Preparation date and time&gt;

**Technical Description**

The value of /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated field is considered valid<br>
only if it is not LESS than or EQUAL to /<span>&#42;</span>/Message/preparationDateAndTime


## R0006

**Functional Description**

IF the first two characters of &lt;CUSTOMS OFFICE OF DESTINATION (DECLARED).Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&gt; is in set CL112 (CountryCodesCTC)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the first two characters of at least one instance of &lt;CUSTOMS OFFICE OF TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; shall be EQUAL to the first two characters of &lt;CUSTOMS OFFICE<br>
&nbsp;&nbsp;&nbsp;&nbsp;OF DESTINATION (DECLARED).Reference number&gt;;<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in set<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CL112 (CountryCodesCTC) AND If the first two characters of &lt;CUSTOMS OFFICE OF DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is in set CL010 (CountryCodesCommunity)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN the first two characters of at least one instance of &lt;CUSTOMS OFFICE OF TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; shall be in set CL010 (CountryCodesCommunity).

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in set CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the first two characters of at least one instance of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber shall be EQUAL to the first two characters of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber;<br>
&nbsp;&nbsp;&nbsp;&nbsp;If the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in set CL112 AND If the<br>
&nbsp;&nbsp;&nbsp;&nbsp;first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in set CL010<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the first two characters of at least one instance of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber shall be in SET CL010.


## R0007

**Functional Description**

Each &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration goods item<br>
number&gt; is unique throughout the declaration. The items shall be numbered in a sequential fashion,<br>
starting from '1' for the first item and increment the numbering by '1' for each following item.

**Technical Description**

Each /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationGoodsItemNumber is unique<br>
throughout the declaration. The items shall be numbered in a sequential fashion, starting from '1' for<br>
the first item and increment the numbering by '1' for each following item.


## R0008

**Functional Description**

&lt;Correlation identifier&gt; shall be EQUAL to the &lt;Message identification&gt; of the request/rejected<br>
message.

**Technical Description**

/<span>&#42;</span>/correlationIdentifier shall be EQUAL to the /<span>&#42;</span>/messageIdentification of the request/rejected message.


## R0010

**Functional Description**

IF &lt;CONSIGNMENT.Container indicator&gt; is EQUAL to '1' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Specific circumstance indicator&gt; is in SET {F50, F51}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN each iteration of &lt; CONSIGNMENT - TRANSPORT EQUIPMENT&gt; must contain<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT - HOUSE CONSIGNMENT – CONSIGNMENT ITEM&gt; from the same<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT - HOUSE CONSIGNMENT&gt;

**Technical Description**

IF /<span>&#42;</span>/Consignment/containerIndicator is EQUAL to '1' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/specificCircumstanceIndicator is in SET {F50, F51}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN each iteration of /<span>&#42;</span>/Consignment/TransportEquipment must contain<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem from the same<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment


## R0020

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F} AND the first two characters of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in SET CL112 (CountryCodesCTC)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;(at least one &lt;CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; is in SET CL178<br>
&nbsp;&nbsp;&nbsp;&nbsp;(PreviousDocumentUnionGoods)) OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;(at least one &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT.Type&gt; is in SET CL178 (PreviousDocumentUnionGoods))<br>
&nbsp;&nbsp;&nbsp;&nbsp;for each and every Consignment Item;<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{T2, T2F}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AND the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number&gt; is in SET CL112 (CountryCodesCTC)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(at least one &lt;CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; is in SET CL178<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(PreviousDocumentUnionGoods)) OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(at least one &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT.Type&gt; is in SET CL178 (PreviousDocumentUnionGoods)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for this ‘Consignment item’)

**Technical Description**

IF /<span>&#42;</span>/Transit Operation/declarationType is in SET {T2, T2F}<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;(at least one /<span>&#42;</span>/Consignment/PreviousDocument/type is in SET CL178) OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;(at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/type is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL178) for each and every Consignment Item;<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2, T2F}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(at least one /<span>&#42;</span>/Consignment/PreviousDocument/type is in SET CL178) OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/type is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CL178 for this ‘Consignment item’)


## R0023

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;REFERENCE.Type&gt; is in SET CL234 (DocumentTypeExcise)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;REFERENCE.Reference number&gt; shall not be '0' (zero)

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/type is in SET CL234<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/referenceNumber<br>
&nbsp;&nbsp;&nbsp;&nbsp;shall not be '0' (zero)


## R0028

**Functional Description**

The structure of this Data Item is validated as specified in DDCOM. The check digit must follow the<br>
ISO 6346 standard.

**Technical Description**

The structure of this Data Item is validated as specified in DDCOM. The check digit must follow the<br>
ISO 6346 standard.


## R0054

**Functional Description**

Numbering of items:<br>
IF a discrepancy is identified in the Data Group THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- 'Sequence number' shall be unique AND EQUAL to the sequence number of the Data<br>
&nbsp;&nbsp;&nbsp;&nbsp;Group defined in the declaration for which the discrepancy is reported.<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF a new Data Group is identified THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'Sequence number' shall be unique AND EQUAL to the number of the last sequence<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of the Data Group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ 1 and the rest of the Data Items contained in the Data Group and all sub–Data Groups<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shall be filled in except for the Data Elements that are defined as optional or dependent<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in the declaration.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the information related to a Data Group is missing<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'Sequence number' shall be unique AND EQUAL to the sequence number of the Data<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group defined in the declaration<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and the rest of the Data Items contained in the Data Group and all sub–Data Groups<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shall not be filled.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: The Sequence number of a Data Group is unique if the XPath and the value of the sequence<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of this Data Item is unique in this message.

**Technical Description**

Numbering of items:<br>
IF a discrepancy is identified in the Data Group THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- 'Sequence number' shall be unique AND EQUAL to the sequence number of the Data<br>
&nbsp;&nbsp;&nbsp;&nbsp;Group defined in the declaration for which the discrepancy is reported.<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF a new Data Group is identified THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'Sequence number' shall be unique AND EQUAL to the number of the last sequence<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of the Data Group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ 1 and the rest of the Data Items contained in the Data Group and all sub–Data Groups<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shall be filled in except for the Data Elements that are defined as optional or dependent<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in the declaration.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the information related to a Data Group is missing<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'Sequence number' shall be unique AND EQUAL to the sequence number of the Data<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group defined in the declaration<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and the rest of the Data Items contained in the Data Group and all sub–Data Groups<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shall not be filled.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: The Sequence number of a Data Group is unique if the XPath and the value of the sequence<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of this Data Item is unique in this message.


## R0055

**Functional Description**

Numbering of items:<br>
IF a discrepancy is identified in the Data Group THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- ‘Declaration goods item number' shall be unique AND EQUAL to the declaration goods item<br>
&nbsp;&nbsp;&nbsp;&nbsp;number defined in the declaration for which the discrepancy is reported AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;- 'Goods item number’ shall be unique AND EQUAL to the goods item number defined in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;declaration for which the discrepancy is reported.<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF a new Data Group is identified THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ‘Declaration goods item number' shall be unique AND EQUAL to the last declaration goods item<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number defined in the declaration + 1 AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'Goods item number’ shall be unique AND EQUAL to the last goods item number defined in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;declaration + 1 AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the rest of the Data Items contained in the Data Group and all sub–Data Groups shall be<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filled in except for the Data Elements that are defined as optional or dependent in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;declaration.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF a Goods item is missing THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ‘Declaration goods item number' shall be unique AND EQUAL to the number of the declaration<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;goods item number defined in the declaration AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'Goods item number’ shall be unique AND EQUAL to the item number defined in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;declaration AND the rest of the Data Items contained in the Data Group and all sub–Data Groups<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shall not be filled.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: The Sequence number of a Data Group is unique if the XPath and the value of the sequence<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of this Data Item is unique in this message.

**Technical Description**

Numbering of items:<br>
IF a discrepancy is identified in the Data Group THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- ‘Declaration goods item number' shall be unique AND EQUAL to the declaration goods item<br>
&nbsp;&nbsp;&nbsp;&nbsp;number defined in the declaration for which the discrepancy is reported AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;- 'Goods item number’ shall be unique AND EQUAL to the goods item number defined in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;declaration for which the discrepancy is reported.<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF a new Data Group is identified THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ‘Declaration goods item number' shall be unique AND EQUAL to the last declaration goods item<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number defined in the declaration + 1 AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'Goods item number’ shall be unique AND EQUAL to the last goods item number defined in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;declaration + 1 AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the rest of the Data Items contained in the Data Group and all sub–Data Groups shall be<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filled in except for the Data Elements that are defined as optional or dependent in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;declaration.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF a Goods item is missing THEN:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ‘Declaration goods item number' shall be unique AND EQUAL to the number of the declaration<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;goods item number defined in the declaration AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'Goods item number’ shall be unique AND EQUAL to the item number defined in the<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;declaration AND the rest of the Data Items contained in the Data Group and all sub–Data Groups<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shall not be filled.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: The Sequence number of a Data Group is unique if the XPath and the value of the sequence<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of this Data Item is unique in this message.


## R0060

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY<br>
&nbsp;&nbsp;&nbsp;&nbsp;CODE.Combined nomenclature code&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the concatenation of the Data Items &lt;CONSIGNMENT-HOUSE CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT ITEM-COMMODITY-COMMODITY CODE.Harmonized System sub-heading code&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;(an6) and &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY CODE.Combined nomenclature code&gt; (an2) must be a valid code in the TARIC<br>
&nbsp;&nbsp;&nbsp;&nbsp;database (validated only by the EU countries).

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br>
&nbsp;&nbsp;&nbsp;&nbsp;CommodityCode/combinedNomenclatureCode is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the concatenation of the Data Items /<span>&#42;</span>/Consignment/HouseConsignment/<br>
&nbsp;&nbsp;&nbsp;&nbsp;ConsignmentItem/Commodity/CommodityCode/harmonizedSystemSubHeadingCode (an6) and<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br>
&nbsp;&nbsp;&nbsp;&nbsp;CommodityCode/combinedNomenclatureCode (an2) must be a valid code in the TARIC database<br>
&nbsp;&nbsp;&nbsp;&nbsp;(validated only by the EU countries).


## R0076

**Functional Description**

IF &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Type of identification&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;{10,21,30,40,41,80}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Identification number&gt; shall not<br>
&nbsp;&nbsp;&nbsp;&nbsp;contain lowercase letters.

**Technical Description**

IF /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/typeOfIdentification is in SET {10,21,30,40,41,80}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/identificationNumber shall not contain lowercase<br>
&nbsp;&nbsp;&nbsp;&nbsp;letters.


## R0093

**Functional Description**

IF the last two characters of &lt;Message recipient&gt; are NOT in SET CL147<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryCustomsSecurityAgreementArea)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; shall NOT be EQUAL to 'N355' (ENS)<br>
ELSE IF &lt;TRANSIT OPERATION.Security&gt; is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one iteration of &lt;CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; must be EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'N355' (ENS)

**Technical Description**

IF the last two characters of /<span>&#42;</span>/messageRecipient are NOT in SET CL147<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/PreviousDocument/type shall NOT be EQUAL to 'N355' (ENS)<br>
ELSE IF /<span>&#42;</span>/TransitOperation/security is in SET {1, 3}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one iteration of /<span>&#42;</span>/Consignment/PreviousDocument/type must be EQUAL to 'N355'<br>
&nbsp;&nbsp;&nbsp;&nbsp;(ENS)


## R0102

**Functional Description**

Data item &lt;INVALIDATION.Decision&gt; can contain 2 valid values:<br>
- '0' = 'No': Invalidation refused by Customs: Decision<br>
- '1' = 'Yes': Invalidation accepted by Customs: Decision

**Technical Description**

Data item /<span>&#42;</span>/Invalidation/decision can contain 2 valid values:<br>
- '0' = 'No': Invalidation refused by Customs: Decision<br>
- '1' = 'Yes': Invalidation accepted by Customs: Decision


## R0103

**Functional Description**

IF &lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED). Reference number&gt; is NOT EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CUSTOMS OFFICE TRANSIT (DECLARED).Reference number&gt; AND is NOT EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CUSTOMS OFFICE OF DESTINATION (DECLARED).Reference number&gt;

**Technical Description**

IF /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared/referenceNumber is NOT EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber AND is NOT EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber


## R0106

**Functional Description**

&lt;TRANSPORT EQUIPMENT.Number of seals&gt; is EQUAL to the ‘maximum value of &lt;TRANSPORT<br>
EQUIPMENT-SEAL.Sequence number&gt;’ for THIS instance of Transport Equipment.

**Technical Description**

/<span>&#42;</span>/TransportEquipment/numberOfSeals is EQUAL to the ‘maximum value of<br>
/<span>&#42;</span>/TransportEquipment/Seal/sequenceNumber’ for THIS instance of Transport Equipment.


## R0107

**Functional Description**

&lt;TRANSPORT EQUIPMENT-SEAL.Identifier&gt; is unique in the whole declaration.

**Technical Description**

/<span>&#42;</span>/TransportEquipment/Seal/identifier is unique in the whole declaration.

## R0165

**Functional Description**

IF the declaration is submitted under simplified procedure AND the authorisation of which foresees the<br>
&nbsp;&nbsp;&nbsp;&nbsp;use of seals<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'.

**Technical Description**

IF the declaration is submitted under simplified procedure AND the authorisation of which foresees the<br>
&nbsp;&nbsp;&nbsp;&nbsp;use of seals<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/TransportEquipment/numberOfSeals&gt; is GREATER than '0'.


## R0219

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt; is EQUAL to '0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN in this &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt; any other<br>
&nbsp;&nbsp;&nbsp;&nbsp;occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-<br>
&nbsp;&nbsp;&nbsp;&nbsp;PACKAGING.Number of packages&gt; shall be EQUAL to '0' (zero).

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN in this /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem any other occurrence of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging /numberOfPackages shall be<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to '0' (zero).


## R0220

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt; is EQUAL to '0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Type of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt; shall not be in SET CL182 (KindOfPackagesUnpacked) for this data group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages shall not be<br>
&nbsp;&nbsp;&nbsp;&nbsp;in SET CL182 for this data group /<span>&#42;</span>/ Consignment/HouseConsignment/ConsignmentItem.


## R0221

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br>
&nbsp;&nbsp;&nbsp;&nbsp;packages&gt; is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;for THIS CONSIGNMENT ITEM<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Gross mass&gt; is EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;for THIS HOUSE CONSIGNMENT at least one other CONSIGNMENT ITEM must exist with<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Gross mass&gt; having a value different from '0'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;for THIS CONSIGNMENT ITEM<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Gross mass&gt; must be different from '0'.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;for THIS CONSIGNMENT ITEM<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass is<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to '0'<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;for THIS HOUSE CONSIGNMENT at least one other CONSIGNMENT ITEM must exist with<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass having<br>
&nbsp;&nbsp;&nbsp;&nbsp;a value different from '0'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;for THIS CONSIGNMENT ITEM<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass<br>
&nbsp;&nbsp;&nbsp;&nbsp;must be different from '0'.


## R0223

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Gross mass&gt; is GREATER THAN '0' (zero).<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEASURE.Net mass&gt; must be LESS THAN OR EQUAL to &lt;CONSIGNMENT-HOUSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS MEASURE.Gross mass&gt;.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass is<br>
&nbsp;&nbsp;&nbsp;&nbsp;GREATER THAN '0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass<br>
&nbsp;&nbsp;&nbsp;&nbsp;must be LESS THAN OR EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass.


## R0315

**Functional Description**

Where &lt;CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '4' the (IATA/ICAO) flight<br>
number shall be indicated and shall have a format an..8:<br>
- an..3: mandatory prefix identifying the airline/operator<br>
- n..4: mandatory number of the flight<br>
- a1: optional suffix

**Technical Description**

Where /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '4' the (IATA/ICAO) flight number<br>
shall be indicated and shall have a format an..8:<br>
- an..3: mandatory prefix identifying the airline/operator<br>
- n..4: mandatory number of the flight<br>
- a1: optional suffix


## R0318

**Functional Description**

IF &lt;GUARANTEE.Guarantee type&gt; is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the format of &lt;GUARANTEE-GUARANTEE REFERENCE.GRN&gt; is 'an24'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the format of &lt;GUARANTEE-GUARANTEE REFERENCE.GRN&gt; is 'an17'

**Technical Description**

IF /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to '4'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the format of /<span>&#42;</span>/Guarantee/GuaranteeReference/GRN is 'an24'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the format of /<span>&#42;</span>/Guarantee/GuaranteeReference/GRN is 'an17'


## R0350

**Functional Description**

IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT.Inland mode of transport&gt; is in SET {1, 2, 4}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;at least one &lt;AUTHORISATION.Type&gt; is EQUAL to 'C524'

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/inlandModeOfTransport is in SET {1, 2, 4}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;at least one /<span>&#42;</span>/Authorisation/type is EQUAL to 'C524'


## R0352

**Functional Description**

IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT.Inland mode of transport&gt; is in SET {1, 2, 4}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;this Data Item includes at least one &lt;Authorisation number&gt; for a valid Authorisation for Reduced Data<br>
&nbsp;&nbsp;&nbsp;&nbsp;Set owned by the Holder of the Transit Procedure

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator&gt; is EQUAL to '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/inlandModeOfTransport is in SET {1, 2, 4}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;this Data Item includes at least one &lt;Authorisation number&gt; for a valid Authorisation for Reduced Data<br>
&nbsp;&nbsp;&nbsp;&nbsp;Set owned by the Holder of the Transit Procedure


## R0364

**Functional Description**

IF&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of<br>
&nbsp;&nbsp;&nbsp;&nbsp;Packages&gt; is EQUAL to '0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN for THIS HOUSE CONSIGNMENT at least one other CONSIGNMENT ITEM must exist with (the<br>
&nbsp;&nbsp;&nbsp;&nbsp;same &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Shipping<br>
&nbsp;&nbsp;&nbsp;&nbsp;marks&gt; AND with &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-<br>
&nbsp;&nbsp;&nbsp;&nbsp;PACKAGING.Number of packages&gt; having a value GREATER than '0' (zero) AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Type of packages&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;having a value NOT IN SET {CL181(KindOfPackagesBulk), CL182(KindOfPackagesUnpacked)}).

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'0' (zero)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN for THIS HOUSE CONSIGNMENT at least one other CONSIGNMENT ITEM must exist with (the<br>
&nbsp;&nbsp;&nbsp;&nbsp;same /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks AND with<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages having a value<br>
&nbsp;&nbsp;&nbsp;&nbsp;GREATER than '0' zero) AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages having a value<br>
&nbsp;&nbsp;&nbsp;&nbsp;NOT IN SET {CL181, CL182}).


## R0410

**Functional Description**

IF (&lt;CC015C-TRANSIT OPERATION.Security&gt; (the transit declaration includes ENS data for safety<br>
&nbsp;&nbsp;&nbsp;&nbsp;and security purposes [only]) is EQUAL to '1' OR &lt;CCA15D-TRANSIT OPERATION.Security&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to '1')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the 17th character of MRN is EQUAL to 'L'<br>
ELSE IF &lt;TRANSIT OPERATION.Security&gt; (the transit declaration includes EXS data for safety and<br>
&nbsp;&nbsp;&nbsp;&nbsp;security purposes [only]) is EQUAL to '2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the 17th character of MRN is EQUAL to 'K'<br>
ELSE IF &lt;TRANSIT OPERATION.Security&gt; (the transit declaration includes ENS and EXS data for<br>
&nbsp;&nbsp;&nbsp;&nbsp;safety and security purposes [only]) is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the 17th character of MRN is EQUAL to 'M'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the 17th character of MRN is EQUAL to 'J'

**Technical Description**

IF (/CC015C/TransitOperation/security (the transit declaration includes ENS data for safety and<br>
&nbsp;&nbsp;&nbsp;&nbsp;security purposes [only]) is EQUAL to '1' OR CCA15D/TransitOperation/security is EQUAL to '1')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the 17th character of MRN is EQUAL to 'L'<br>
ELSE IF /<span>&#42;</span>/TransitOperation/security (the transit declaration includes EXS data for safety and security<br>
&nbsp;&nbsp;&nbsp;&nbsp;purposes [only]) is EQUAL to '2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the 17th character of MRN is EQUAL to 'K'<br>
ELSE IF <span>&#42;</span>/TransitOperation/security (the transit declaration includes ENS and EXS data for safety and<br>
&nbsp;&nbsp;&nbsp;&nbsp;security purposes [only]) is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the 17th character of MRN is EQUAL to 'M'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the 17th character of MRN is EQUAL to 'J'


## R0416

**Functional Description**

The Data Item &lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT. Reference<br>
Number&gt; must include a valid ‘Export declaration’ or an ‘Export and exit summary declaration’ or a<br>
‘Dispatch of goods in relation with special fiscal territories’.

**Technical Description**

The Data Item /<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/referenceNumber must include<br>
a valid export MRN. The 17th character must be in SET {A, B, E}.


## R0437

**Functional Description**

IF the last two characters of &lt;Message sender&gt; is in SET CL167 (CountryCodesOptout)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the value &lt;FUNCTIONAL ERROR.Error code&gt; must be in SET CL180<br>
&nbsp;&nbsp;&nbsp;&nbsp;(AES/NCTSP5FunctionalErrorCodes)

**Technical Description**

IF the last two characters of /<span>&#42;</span>/messageSender is in SET CL167<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the value of /<span>&#42;</span>/FunctionalError/errorCode must be in SET CL180


## R0448

**Functional Description**

IF &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Container identification number&gt; is NOT PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the value '0' (zero) is not valid for &lt;CONSIGNMENT-TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUIPMENT.Number of seals&gt;

**Technical Description**

IF /<span>&#42;</span>/Consignment/TransportEquipment/containerIdentificationNumber is NOT PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the value '0' (zero) is not valid for<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/TransportEquipment/numberOfSeals


## R0472

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is in SET {1,2,3,4,8}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the first digit of &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Type of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identification&gt; shall be EQUAL to &lt;CONSIGNMENT.Inland mode of transport&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MEANS&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the first digit of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRANSPORT MEANS.Type of identification&gt; shall be EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT.Inland mode of transport&gt;

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is in SET {1,2,3,4,8}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/DepartureTransportMeans is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the first digit of /<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification shall be<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to /<span>&#42;</span>/Consignment/inlandModeOfTransport<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the first digit of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/typeOfIdentification<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shall be EQUAL to /<span>&#42;</span>/Consignment/inlandModeOfTransport


## R0473

**Functional Description**

IF &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Type of identification&gt; is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;{10,20,21,30,31,40,41,80}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt; CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Identification number&gt; shall not<br>
&nbsp;&nbsp;&nbsp;&nbsp;contain lowercase letters<br>
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT AND &lt;CONSIGNMENT- HOUSE CONSIGNMENT-DEPARTURE TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEANS.Type of identification&gt; is in SET {10,20,21,30,31,40,41,80}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt; CONSIGNMENT- HOUSE CONSIGNMENT-DEPARTURE TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;MEANS.Identification number&gt; shall not contain lowercase letters

**Technical Description**

IF /<span>&#42;</span>/Consignment/DepartureTransportMeans is PRESENT AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/DepartureTransportMeans/typeofIdentification is in SET {10,20,21,30,31,40,41,80}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/DepartureTransportMeans/IdentificationNumber shall not contain lowercase<br>
&nbsp;&nbsp;&nbsp;&nbsp;letters<br>
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/typeofIdentification is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;{10,20,21,30,31,40,41,80}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/IdentificationNumber shall not<br>
&nbsp;&nbsp;&nbsp;&nbsp;contain lowercase letters


## R0474

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the first data group iteration &lt;Consignment-Departure Transport Means.Type of identification&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;must be EQUAL to '30';<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AND &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN for THIS House Consignment, the first data group iteration &lt;CONSIGNMENT-HOUSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Type of identification&gt; must be EQUAL to '30'

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the first data group iteration /<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification must<br>
&nbsp;&nbsp;&nbsp;&nbsp;be EQUAL to '30';<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AND /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN for THIS HouseConsignment, the first data group iteration<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/typeOfIdentification must be EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'30'.


## R0476

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the multiplicity of the data group &lt;CONSIGNMENT-DEPARTURE TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MEANS&gt; is more than 1x<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN the iteration 2 and the iteration 3 (if present) of the data group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; must include<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Type of identification&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;that is EQUAL to '31'<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE IF the multiplicity of the data group &lt;CONSIGNMENT-HOUSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT- DEPARTURE TRANSPORT MEANS&gt; is more than 1x<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN the iteration 2 and the iteration 3 (if present) of the data group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT- HOUSE CONSIGNMENT-DEPARTURE TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MEANS&gt; must include &lt;CONSIGNMENT-HOUSE CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE TRANSPORT MEANS.Type of identification&gt; that is EQUAL to '31'

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the multiplicity of the data group /<span>&#42;</span>/Consignment/DepartureTransportMeans is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;more than 1x<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN the iteration 2 and the iteration 3 (if present) of the data group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/DepartureTransportMeans must include<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification that is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'31'<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE IF the multiplicity of the data group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is more than 1x<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN the iteration 2 and the iteration 3 (if present) of the data group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans must include<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/typeOfIdentification<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;that is EQUAL to '31'


## R0506

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; is PRESENT for all &lt;CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;HOUSE CONSIGNMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; must be<br>
&nbsp;&nbsp;&nbsp;&nbsp;different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; is PRESENT for all &lt;CONSIGNMENT-<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HOUSE CONSIGNMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; must be<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for all &lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRANSPORT MEANS&gt; must be different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT- TRANSPORT CHARGES&gt; is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT- TRANSPORT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHARGES&gt; must be different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Reference number UCR&gt; is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Reference number<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UCR&gt; must be different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt; is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;must be different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of destination&gt; is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of destination&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;must be different from the others.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignor is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/Consignor must be different from<br>
&nbsp;&nbsp;&nbsp;&nbsp;the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignee is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/Consignee must be different<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans must<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;be different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges must be<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/referenceNumberUCR is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/referenceNumberUCR must be<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch must be<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDestination is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDestination must be<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;different from the others.


## R0507

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of dispatch&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;ITEM.Country<br>
&nbsp;&nbsp;&nbsp;&nbsp;of dispatch&gt; must be different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRESENT for<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ITEM.Country<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;of destination&gt; must be different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Reference number UCR&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRESENT for<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ITEM.Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number UCR&gt; must be different from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM. Declaration type &gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ITEM.Declaration type&gt; must be different from the others.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch must be different from<br>
&nbsp;&nbsp;&nbsp;&nbsp;the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination must be different<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR must be different<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from the others;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is PRESENT for all<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one occurrence of<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType must be different from the<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;others


## R0520

**Functional Description**

IF ( the Data Item &lt;CC013C-TRANSIT OPERATION.Amendment type flag&gt; is EQUAL to '1' and the<br>
&nbsp;&nbsp;&nbsp;&nbsp;movement is in state “Guarantee under amendment”)<br>
&nbsp;&nbsp;&nbsp;&nbsp;(i.e. the message CC013C is used for amending the Guarantee previously declared while the<br>
&nbsp;&nbsp;&nbsp;&nbsp;movement is in   state “Guarantee under amendment”)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;the only difference between this CC013C and the CC015C (or the previous CC013C) shall be located<br>
&nbsp;&nbsp;&nbsp;&nbsp;in the Data Group &lt;GUARANTEE&gt;<br>
ELSE<br>
IF (the Data Item &lt;TRANSIT OPERATION.Amendment type flag&gt; is EQUAL to '0' AND the<br>
&nbsp;&nbsp;&nbsp;&nbsp;movement IS NOT IN STATE “Guarantee under amendment”)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;all Data Groups and Data Items of the original declaration can be amended, with the exception of<br>
&nbsp;&nbsp;&nbsp;&nbsp;the following Data Groups:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;HOLDER OF THE TRANSIT PROCEDURE&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;REPRESENTATIVE&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;CUSTOMS OFFICE OF DEPARTURE&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;and the exception of the following Data Items:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;TRANSIT OPERATION.Additional declaration type&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;TRANSIT OPERATION.Declaration type&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;TRANSIT OPERATION.MRN&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;TRANSIT OPERATION.LRN&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-<br>
&nbsp;&nbsp;&nbsp;&nbsp;COMMODITY<br>
&nbsp;&nbsp;&nbsp;&nbsp;CODE. Harmonized System sub-heading code&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;- &lt;TRANSIT OPERATION.Security&gt;

**Technical Description**

IF (the Data Item /CC013C/TransitOperation/amendmentTypeFlag is EQUAL to '1' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;the movement is in state “Guarantee under amendment”)<br>
&nbsp;&nbsp;&nbsp;&nbsp;(i.e. the message CC013C is used for amending the Guarantee previously declared while the<br>
&nbsp;&nbsp;&nbsp;&nbsp;movement is in state “Guarantee under amendment”)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;the only difference between this CC013C and the CC015C (or the previous CC013C) shall be located<br>
&nbsp;&nbsp;&nbsp;&nbsp;in the Data Group /<span>&#42;</span>/Guarantee<br>
ELSE<br>
IF (the Data Item /<span>&#42;</span>/TransitOperation/amendmentTypeFlag is EQUAL to '0' AND the movement IS<br>
&nbsp;&nbsp;&nbsp;&nbsp;NOT IN STATE “Guarantee under amendment”)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;all Data Groups and Data Items of the original declaration can be amended, with the exception of<br>
&nbsp;&nbsp;&nbsp;&nbsp;the following Data Groups:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- /<span>&#42;</span>/HolderOfTheTransitProcedure<br>
&nbsp;&nbsp;&nbsp;&nbsp;- /<span>&#42;</span>/Representative<br>
&nbsp;&nbsp;&nbsp;&nbsp;- /<span>&#42;</span>/CustomsOfficeOfDeparture<br>
&nbsp;&nbsp;&nbsp;&nbsp;and the exception of the following Data Items:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- /<span>&#42;</span>/TransitOperation/additionalDeclarationType<br>
&nbsp;&nbsp;&nbsp;&nbsp;- /<span>&#42;</span>/TransitOperation/declarationType<br>
&nbsp;&nbsp;&nbsp;&nbsp;- /<span>&#42;</span>/TransitOperation/MRN<br>
&nbsp;&nbsp;&nbsp;&nbsp;- /<span>&#42;</span>/TransitOperation/LRN<br>
&nbsp;&nbsp;&nbsp;&nbsp;-  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br>
&nbsp;&nbsp;&nbsp;&nbsp;CommodityCode/harmonizedSystemSubHeadingCode<br>
&nbsp;&nbsp;&nbsp;&nbsp;- /<span>&#42;</span>/TransitOperation/security


## R0601

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;REFERENCE.Type&gt; is in SET CL234 (DocumentTypeExcise)<br>
&nbsp;&nbsp;&nbsp;&nbsp;(i.e. Export of excise goods followed by transit (EMCS&AES+NCTS))<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT–HOUSE CONSIGNMENT–PREVIOUS DOCUMENT.Type&gt; is EQUAL to 'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN (&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to 'T1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(&lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T1, TIR}<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-SUPPORTING<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOCUMENT.Type&gt; is in SET CL234 (DocumentTypeExcise)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(i.e. Transit movement of EU goods under excise suspension (EMCS+NCTS))<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM. Declaration type&gt; is in<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SET {T2, T2F}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F}

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/type is in SET CL234<br>
&nbsp;&nbsp;&nbsp;&nbsp;(i.e. Export of excise goods followed by transit (EMCS&AES+NCTS))<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/type is EQUAL to 'N830'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is EQUAL to 'T1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/declarationType is in SET {T1, TIR}<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/SupportingDocument/type is in SET CL234<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(i.e. Transit movement of EU goods under excise suspension (EMCS+NCTS))<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T2F}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F}


## R0789

**Functional Description**

IF &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is up to 9x<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the multiplicity of &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is 1x

**Technical Description**

IF/<span>&#42;</span>/CustomsOfficeOfTransitDeclared is PRESENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans is up to 9x<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the multiplicity of /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans is 1x


## R0790

**Functional Description**

IF (&lt;CC015C-CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; is PRESENT OR &lt;CCA15D-<br>
&nbsp;&nbsp;&nbsp;&nbsp;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is up<br>
&nbsp;&nbsp;&nbsp;&nbsp;to 9x<br>
ELSE IF (&lt;CC013C-CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; is PRESENT OR &lt;CCA13D-<br>
&nbsp;&nbsp;&nbsp;&nbsp;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is up<br>
&nbsp;&nbsp;&nbsp;&nbsp;to 9x<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the multiplicity of &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is 1x

**Technical Description**

IF (/CC015C/CustomsOfficeOfTransitDeclared is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA15D/CustomsOfficeOfTransitDeclared is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of /CC170C/Consignment/ActiveBorderTransportMeans is up to 9x<br>
ELSE IF (/CC013C/CustomsOfficeOfTransitDeclared is PRESENT OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA13D/CustomsOfficeOfTransitDeclared is PRESENT)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of /CC170C/Consignment/ActiveBorderTransportMeans is up to 9x<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the multiplicity of /CC170C/Consignment/ActiveBorderTransportMeans is 1x


## R0840

**Functional Description**

Only a valid EORI or TCUIN shall be used. The EORI shall be validated only by EU MS. The TCUIN<br>
shall be validated by EU MS and by the country where the TCUIN is defined.

**Technical Description**

Only a valid EORI or TCUIN shall be used. The EORI shall be validated only by EU MS. The TCUIN<br>
shall be validated by EU MS and by the country where the TCUIN is defined.


## R0849

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; = '0' (zero)

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator = '0' (zero)


## R0850

**Functional Description**

IF sender is in EU (CL010 (CountryCodesCommunity))<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the value must be a valid EORI or TCUIN (validated by receiver, if located in EU),<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;(sender is not in EU) the value must be a TIN number (validated by the message sender only)<br>
&nbsp;&nbsp;&nbsp;&nbsp;The EORI/TCUIN values shall comply with the following pattern: &lt;xs:pattern value="[A-Z]{2}[\x21-<br>
&nbsp;&nbsp;&nbsp;&nbsp;\x7E]{1,15}"/&gt;

**Technical Description**

IF sender is in EU (CL010)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the value must be a valid EORI or TCUIN (validated by receiver, if located in EU),<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;(sender is not in EU) the value must be a TIN number (validated by the message sender only)<br>
&nbsp;&nbsp;&nbsp;&nbsp;The EORI/TCUIN values shall comply with the following pattern: &lt;xs:pattern value="[A-Z]{2}[\x21-<br>
&nbsp;&nbsp;&nbsp;&nbsp;\x7E]{1,15}"/&gt;


## R0851

**Functional Description**

The Identification number can be validated if the Consignee is located in the same contracting party as<br>
the Recipient.

**Technical Description**

The Identification number can be validated if the Consignee is located in the same contracting party as<br>
the Recipient.


## R0852

**Functional Description**

IF the last two characters of &lt;Message sender&gt; is in SET CL167 (CountryCodesOptout)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Business rejection type&gt; shall not be in SET {A13, A15, A71}

**Technical Description**

IF the last two characters of /<span>&#42;</span>/messageSender is in SET CL167<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/businessRejectionType shall not be in SET {A13, A15, A71}


## R0855

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; can be up to '3x'<br>
ELSE IF &lt; CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of &lt; CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; can be more than<br>
&nbsp;&nbsp;&nbsp;&nbsp;'1x'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the multiplicity of &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is '1x'

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '3'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of /<span>&#42;</span>/Consignment/DepartureTransportMeans AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans can be up to '3x'<br>
ELSE IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the multiplicity of /<span>&#42;</span>/Consignment/DepartureTransportMeans AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans can be more than '1x'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;the multiplicity of /<span>&#42;</span>/Consignment/DepartureTransportMeans AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is '1x'


## R0859

**Functional Description**

IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; = '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one &lt;AUTHORISATION. Type&gt; is EQUAL to 'C524'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;AUTHORISATION. Type&gt; shall not be EQUAL to 'C524'

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator = '1'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN at least one /<span>&#42;</span>/Authorisation/type is EQUAL to 'C524'<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Authorisation/type shall not be EQUAL to 'C524'


## R0860

**Functional Description**

IF sender is in EU (CL010 (CountryCodesCommunity)),<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the value must be a valid EORI or TCUIN,<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;(sender is not in EU) the value must be a valid TIN number.

**Technical Description**

IF sender is in EU (CL010)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the value must be a valid EORI or TCUIN<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;(sender is not in EU) the value must be a valid TIN number.


## R0871

**Functional Description**

Reference number assigned must be equal to the one included in CD001C, CD003C, CC013C,<br>
CC015C, CD050C, CD115C, CD160C, CD165C, CCA13D OR CCA15D.

**Technical Description**

Reference number assigned must be equal to the one included in CD001C, CD003C, CC013C,<br>
CC015C, CD050C, CD115C, CD160C, CD165C, CCA13D OR CCA15D.


## R0900

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTEE.Guarantee type&gt; is EQUAL to 'B'<br>
ELSE IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE.Reference number&gt; is in SET of CL010 (CountryCodesCommunity) OR is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'SM' OR is EQUAL to 'AD'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;GUARANTEE.Guarantee type&gt; must be in SET CL230 (GuaranteeTypeEUNonTIR)<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;GUARANTEE.Guarantee type&gt; must be in SET CL229 (GuaranteeTypeCTC)

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to 'B'<br>
ELSE IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL010<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR is EQUAL to 'SM' OR is EQUAL to 'AD'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Guarantee/guaranteeType must be in SET CL230<br>
ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Guarantee/guaranteeType must be in SET CL229


## R0901

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is in SET CL010 (CountryCodesCommunity)<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;number &gt; is in SET CL010 (CountryCodesCommunity).

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL010<br>
&nbsp;&nbsp;&nbsp;&nbsp;AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL010


## R0904

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&gt; is in SET {AD, SM}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is in SET CL553 (MSCountry)

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET {AD, SM}<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL553


## R0905

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&gt; is in SET CL112 (CountryCodesCTC)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is NOT in SET {AD, SM}

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL112<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is NOT in<br>
&nbsp;&nbsp;&nbsp;&nbsp;SET{AD, SM}


## R0906

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is EQUAL to 'AD'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is EQUAL to 'AD';<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference number&gt; is EQUAL to 'AD'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF TRANSIT<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(ACTUAL).Reference number&gt; is EQUAL to 'AD'

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'AD'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN the first two characters of /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'AD';<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'AD'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN the first two characters of /<span>&#42;</span>/CustomsOfficeOfTransitActual/referenceNumber is EQUAL to 'AD'


## R0909

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED) Reference number&gt; is EQUAL to 'SM'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE.Reference number&gt; is EQUAL to 'IT'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'T2SM'<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE.Reference number&gt; is in set CL010 (CountryCodesCommunity) AND NOT EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'IT'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F} OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in SET {T2,T2F};<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION (ACTUAL)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference number&gt; is EQUAL to 'SM'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE.Reference number&gt; is EQUAL to 'IT'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'T2SM'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DEPARTURE.Reference number&gt; is in set CL010 (CountryCodesCommunity) AND NOT EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'IT'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F} OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is in SET {T2,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T2F}

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to<br>
&nbsp;&nbsp;&nbsp;&nbsp;'SM'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'IT',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'T2SM'<br>
&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CL010<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AND NOT EQUAL to 'IT'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F} OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T2F};<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationActual/referenceNumber is EQUAL to 'SM'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'IT',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'T2SM'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET CL010<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AND NOT EQUAL to 'IT'<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F} OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T2F}


## R0910

**Functional Description**

IF (&lt;CC013C-AUTHORISATION.Type&gt; is NOT EQUAL to 'C521' OR &lt;CCA13D-<br>
&nbsp;&nbsp;&nbsp;&nbsp;AUTHORISATION.Type&gt; is NOT EQUAL to 'C521' OR &lt;CC015C-AUTHORISATION.Type&gt; is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to 'C521' OR &lt;CCA15D-AUTHORISATION.Type&gt; is NOT EQUAL to 'C521')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONTROL RESULT.Code&gt; is in SET CL195<br>
&nbsp;&nbsp;&nbsp;&nbsp;(ControlResultCodeDepartureSimplifiedExcluded).

**Technical Description**

IF (/CC013C/Authorisation/type is NOT EQUAL to 'C521' OR /CCA13D/Authorisation/type is NOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to 'C521' OR /CC015C/Authorisation/type is NOT EQUAL to 'C521' OR<br>
&nbsp;&nbsp;&nbsp;&nbsp;/CCA15D/Authorisation/type is NOT EQUAL to 'C521')<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/ControlResult/code is in SET CL195.


## R0911

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;number&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to 'SM' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;(DECLARED).Reference&gt; is in SET CL010 (CountryCodesCommunity)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F};<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number&gt; is<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to 'SM' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the country code (first two characters) in the &lt;CUSTOMS OFFICE OF<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DESTINATION<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(ACTUAL).Reference&gt; is in SET CL010 (CountryCodesCommunity)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F}

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'SM' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL010<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F};<br>
&nbsp;&nbsp;&nbsp;&nbsp;IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'SM' AND<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationActual/referenceNumber is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CL010<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F}


## R0912

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONTROL RESULT.Code&gt; is in SET CL195<br>
&nbsp;&nbsp;&nbsp;&nbsp;(ControlResultCodeDepartureSimplifiedExcluded)

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/ControlResult/code is in SET CL195


## R0983

**Functional Description**

&lt;CONSIGNMENT-HOUSE CONSIGNMENT.Gross mass&gt; must be GREATER than OR EQUAL to the<br>
sum of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS<br>
MEASURE.Gross mass&gt; available for all Consignment Items included in that House Consignment

**Technical Description**

/<span>&#42;</span>/Consignment/HouseConsignment/grossMass must be GREATER than OR EQUAL to the sum of<br>
/<span>&#42;</span>/Consignment/HouseConsignmentConsignmentItem/Commodity/GoodsMeasure/grossMass available<br>
for all Consignment Items included in that House Consignment


## R0987

**Functional Description**

Each &lt;Sequence number&gt; is unique for the Data Group it belongs to. The sequence numbers shall be<br>
sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each<br>
iteration.

**Technical Description**

Each &lt;Sequence number&gt; is unique for the Data Group it belongs to. The sequence numbers shall be<br>
sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each<br>
iteration.


## R0988

**Functional Description**

Each &lt; Goods item number&gt; is unique for the Data Group it belongs to. The Goods item number shall<br>
be sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each<br>
iteration.

**Technical Description**

Each &lt; Goods item number&gt; is unique for the Data Group it belongs to. The Goods item number shall<br>
be sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each<br>
iteration.


## R0990

**Functional Description**

The &lt;TRANSIT OPERATION.TIR carnet number&gt; must have the format an10 or an11 and must follow<br>
the algorithm defined by IRU, see DDNTA Main Document.

**Technical Description**

The /<span>&#42;</span>/TransitOperation/TIRCarnetNumber must have the format an10 or an11 and must follow the<br>
algorithm defined by IRU, see DDNTA Main Document.


## R0994

**Functional Description**

The value of &lt;CONSIGNMENT.Gross mass&gt; must be GREATER than or EQUAL to the sum of<br>
&lt;CONSIGNMENT-HOUSE CONSIGNMENT.Gross mass&gt; for all house consignments.

**Technical Description**

The value of /<span>&#42;</span>/Consignment/grossMass must be GREATER than or EQUAL to the sum of<br>
/<span>&#42;</span>/Consignment/HouseConsignment/grossMass for all house consignments.


## R3060

**Functional Description**

IF &lt;CONSIGNMENT.Country Of Destination&gt; is in SET CL009 (CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR at least one &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of Destination&gt; is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR at least one &lt; CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of<br>
&nbsp;&nbsp;&nbsp;&nbsp;Destination&gt; is in SET CL009 (CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; shall not be EQUAL to '30600'

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR at least one /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDestination is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/AdditionalInformation/code shall not be EQUAL to '30600'


## R3061

**Functional Description**

The Data Item &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL<br>
INFORMATION.Code&gt; shall not be EQUAL to '30600'

**Technical Description**

The Data Item /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalInformation/code shall<br>
not be EQUAL to '30600'


## R3062

**Functional Description**

IF &lt;CONSIGNMENT.Country of Destination&gt; is in SET CL009 (CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR at least one &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country Of Destination&gt; is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;(CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR at least one &lt; CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of<br>
&nbsp;&nbsp;&nbsp;&nbsp;Destination&gt; is in SET CL009 (CountryCodesCommonTransit)<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT- ADDITIONAL INFORMATION.Code&gt; shall not be<br>
&nbsp;&nbsp;&nbsp;&nbsp;EQUAL to '30600'

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR at least one /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDestination is in SET CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;OR at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET<br>
&nbsp;&nbsp;&nbsp;&nbsp;CL009<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN /<span>&#42;</span>/Consignment/HouseConsignment/AdditionalInformation/code shall not be EQUAL to '30600'
