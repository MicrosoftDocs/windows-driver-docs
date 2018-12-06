---
title: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS
description: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS is a TLV that contains association request parameters.
ms.assetid: DC3439A2-2221-4489-AB38-3752624EA4B2
ms.date: 07/18/2017
keywords:
 - WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_PARAMETERS


WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_PARAMETERS is a TLV that contains association request parameters.

## TLV Type


0x7D

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | The MAC address of the sender.                                                                                                |
| UINT8                                             | A bit that indicates whether or not it is a reassociation request. A value of 1 indicates that it is a reassociation request. |

 

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

 

 




