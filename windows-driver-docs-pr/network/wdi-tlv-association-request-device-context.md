---
title: WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT
ms.topic: reference
description: WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT is a TLV that contains vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ASSOCIATION\_REQUEST\_DEVICE\_CONTEXT

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_ASSOCIATION\_REQUEST\_DEVICE\_CONTEXT is a TLV that contains vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request.

## TLV Type


0x72

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                           |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | Vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request. |

 

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

 

 




