---
title: WDI_TLV_SET_ENCAPSULATION_OFFLOAD_V6_PARAMETERS
description: WDI_TLV_SET_ENCAPSULATION_OFFLOAD_V6_PARAMETERS is a TLV that is used by OID_WDI_SET_ENCAPSULATION_OFFLOAD to indicate if IPv6 offloading should be started.
ms.assetid: 7036AFD0-197E-4A94-8580-A42889BE6798
ms.date: 07/18/2017
keywords:
 - WDI_TLV_SET_ENCAPSULATION_OFFLOAD_V6_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SET\_ENCAPSULATION\_OFFLOAD\_V6\_PARAMETERS


WDI\_TLV\_SET\_ENCAPSULATION\_OFFLOAD\_V6\_PARAMETERS is a TLV that is used by [OID\_WDI\_SET\_ENCAPSULATION\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/dn925930) to indicate if IPv6 offloading should be started.

## TLV Type


0xFE

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | Specifies if IPv6 offloading should be started. This value is set to NDIS\_OFFLOAD\_SET\_ON if enabled, and set to NDIS\_OFFLOAD\_SET\_OFF if disabled. |

 

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

## See also


[**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706)

 

 




