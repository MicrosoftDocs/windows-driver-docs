---
title: WDI_TLV_TKIP_MIC_FAILURE_INFO
ms.topic: reference
description: WDI_TLV_TKIP_MIC_FAILURE_INFO is a TLV that contains TKIP-MIC failure information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_TKIP_MIC_FAILURE_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_TKIP\_MIC\_FAILURE\_INFO

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_TKIP\_MIC\_FAILURE\_INFO is a TLV that contains TKIP-MIC failure information.

## TLV Type


0x57

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                             | Specifies which cipher key type detected that the TKIP-MIC failure occurred. If this value is 1, the TKIP-MIC failure was detected through a default cipher key. If this value is 0, the TKIP-MIC failure was detected through a key mapping cipher key. |
| UINT32                                            | Specifies the index of the cipher key in the default key array. Valid value range is from 0 through 3.                                                                                                                                                   |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | Specifies the MAC address of the peer that transmitted the packet that failed MIC verification.                                                                                                                                                          |

 

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

 

