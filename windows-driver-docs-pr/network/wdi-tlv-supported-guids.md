---
title: WDI_TLV_SUPPORTED_GUIDS
description: WDI_TLV_SUPPORTED_GUIDS is a TLV that contains a supported NDIS GUID.
ms.assetid: 957645EE-A6E3-402E-B18B-B2E7C73D6F6B
ms.date: 07/18/2017
keywords:
 - WDI_TLV_SUPPORTED_GUIDS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SUPPORTED\_GUIDS


WDI\_TLV\_SUPPORTED\_GUIDS is a TLV that contains a supported NDIS GUID.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x130

## Length


The size (in bytes) of a [NDIS\_GUID](https://msdn.microsoft.com/library/windows/hardware/ff549898) structure.

## Values


| Type       | Description            |
|------------|------------------------|
| NDIS\_GUID | A supported NDIS GUID. |

 

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


[OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/dn925838)

 

 




