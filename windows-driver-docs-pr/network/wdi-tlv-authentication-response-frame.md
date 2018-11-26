---
title: WDI_TLV_AUTHENTICATION_RESPONSE_FRAME
description: WDI_TLV_ASSOCIATION_RESPONSE_FRAME is a TLV that contains an authentication response frame.
ms.assetid: 0BD8BDD9-7D51-413F-8740-FD49F71249B1
ms.date: 07/18/2017
keywords:
 - WDI_TLV_AUTHENTICATION_RESPONSE_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_AUTHENTICATION\_RESPONSE\_FRAME


WDI\_TLV\_ASSOCIATION\_RESPONSE\_FRAME is a TLV that contains an authentication response frame.

## TLV Type


0x124

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                              |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the authentication response that was received with a failure code. This does not include the 802.11 MAC header. |

 

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

 

 




