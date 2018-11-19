---
title: WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_PARAMETERS
description: WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_PARAMETERS is a TLV that contains incoming GO Negotiation Confirmation parameters.
ms.assetid: 69A20B64-C2B9-4C96-8119-EE64E80201EB
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_CONFIRMATION\_PARAMETERS


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_CONFIRMATION\_PARAMETERS is a TLV that contains incoming GO Negotiation Confirmation parameters.

## TLV Type


0xAA

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | The Wi-Fi Direct Status Code, as defined by the Wi-Fi Direct specification.                                                                                          |
| UINT8 | Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi Direct technical specification. |
| UINT8 | The bits in the Group capability bitmap above that are set by the operating system.                                                                                  |

 

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

 

 




