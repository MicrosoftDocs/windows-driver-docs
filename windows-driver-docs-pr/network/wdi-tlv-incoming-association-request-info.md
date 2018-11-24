---
title: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO
description: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO is a TLV that contains information about the incoming association request.
ms.assetid: E36ADD95-1751-4FCE-9032-900968878DEE
ms.date: 07/18/2017
keywords:
 - WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO


WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO is a TLV that contains information about the incoming association request.

## TLV Type


0x8F

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                            | Multiple TLV instances allowed | Optional | Description                                                      |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------|
| [**WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_PARAMETERS**](wdi-tlv-incoming-association-request-parameters.md) |                                |          | The parameters for the incoming association request.             |
| [**WDI\_TLV\_ASSOCIATION\_REQUEST\_FRAME**](wdi-tlv-association-request-frame.md)                              |                                |          | The association request frame.                                   |
| [**WDI\_TLV\_ASSOCIATION\_REQUEST\_DEVICE\_CONTEXT**](wdi-tlv-association-request-device-context.md)           |                                | X        | The vendor-specific information that is passed down to the port. |

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




