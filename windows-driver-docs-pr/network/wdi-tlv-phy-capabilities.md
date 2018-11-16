---
title: WDI_TLV_PHY_CAPABILITIES
description: WDI_TLV_PHY_CAPABILITIES is a TLV that contains PHY capabilities.
ms.assetid: 8F482ED6-6594-4DB5-B53B-4424DAD32D36
ms.date: 07/18/2017
keywords:
 - WDI_TLV_PHY_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PHY\_CAPABILITIES


WDI\_TLV\_PHY\_CAPABILITIES is a TLV that contains PHY capabilities.

## TLV Type


0x1B

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                        | Description                                        |
|---------------------------------------------|----------------------------------------------------|
| [**WDI\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926105) | Specifies the PHY types.                           |
| UINT8                                       | Specifies whether or not the PHY supports CF Poll. |
| UINT32                                      | Specifies the MPDU maximum length.                 |
| UINT32                                      | Specifies the operating temperature class.         |
| UINT32                                      | Specifies the antenna diversity support.           |

 

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

 

 




