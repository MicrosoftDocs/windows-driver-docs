---
title: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO
ms.topic: reference
description: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO is a TLV that contains information about the incoming association request.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


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

 

## Requirements

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

 

 




