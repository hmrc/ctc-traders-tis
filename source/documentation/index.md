---
title: NCTS Technical Interface Specification
weight: 1
description: Software developers, designers, product owners or business analysts. Learn about the processes involved in the exchange of messages between traders and phase 6 of the NCTS at departure and arrival of transit movements, and about the definitions, formats and validations of those messages.
---

# NCTS Technical Interface Specification


Last updated: 27 June 2025 update to todays date


| NCTS Phase | DDNTA Version                            | 
|------------|------------------------------------------|
| Phase 5    | 5.15.2-v2.00 issue date 01 December 2023 |
| Phase 6    | 6.4.1-v1.00 and issue date 27 June 2025  |

## Introduction

### Document summary

This document is the first part of the Technical Interface Specification (TIS) for Direct Trader Input (DTI) to the New Computerised Transit System (NCTS). 

It shows the processes involved in the exchange of messages between traders and the NCTS at departure and arrival of transit movements, and provides definitions, formats and validations of those messages.

### Important NCTS terms

The following terms are important to understand in NCTS:

- **Consignment:** The header information is provided and applies to the whole transit declaration (up to 1 Consignment level per declaration).

- **House consignment:** The lowest transport information is provided, and this applies to all its Consignment Items (each Consignment can contain up to 1999 House Consignments).
  The House Consignment level covers information relating to all goods that are subject to the same consignor to consignee itinerary. Information relevant to all goods moving from one consignor to one consignee can be input at this level and will be considered applicable to all goods items attributed to this house consignment.The new House Consignment level is introduced to give more flexibility to the Economic Operators, allowing them to lodge one declaration with several Consignors/Consignees without specifying consignor/nee at goods item level. It also aims to align NCTS data structure with that of other EU systems for better cross communication and integration.

- **Multiple House Consignments:** This is the terminology often used to describe a transit declaration (IE015) containing more than one House Consignment data group. Multiple House Consignments are used when the declaration contains movements of goods from multiple consignors to a single consignee, a single consignor to multiple consignees, or multiple consignors to multiple consignees. The rules applicable to the data group and data elements must be considered to ensure proper use and avoid declaration rejection. If goods are moving from a single consignor to a single consignee, multiple house consignments cannot be used.

- **Consignment item:** The items information is provided (each House Consignment can contain up to 999 Consignment Items, to a declaration maximum of 1999 goods items).


### Scope

This document provides an overview of the processes involved in the exchange of NCTS messages with traders and defines the messages associated with the NCTS, in particular:

- the trader’s declaration for Transit and the associated Customs response
- control and release of the movement at departure 
- the trader’s notification of arrival and the associated Customs response
- control and release of the goods at destination
- registration of any incidents that may occur during transit

These messages comply with the Functional Transit System Specification (FTSS) and Design Documentation for National Transit Application (DDNTA) documents, which are distributed by the EU Commission to National Administrations.