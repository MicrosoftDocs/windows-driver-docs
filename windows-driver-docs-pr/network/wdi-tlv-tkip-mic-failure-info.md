---
title: WDI_TLV_TKIP_MIC_FAILURE_INFO
description: WDI_TLV_TKIP_MIC_FAILURE_INFO is a TLV that contains TKIP-MIC failure information.
ms.assetid: BBF168BE-6223-4C54-AFF5-17878D07EFBD
ms.date: 07/18/2017
keywords:
 - WDI_TLV_TKIP_MIC_FAILURE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_TKIP\_MIC\_FAILURE\_INFO


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
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Specifies the MAC address of the peer that transmitted the packet that failed MIC verification.                                                                                                                                                          |

 

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

 

 




