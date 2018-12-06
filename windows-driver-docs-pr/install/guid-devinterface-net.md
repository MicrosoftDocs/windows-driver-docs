---
title: GUID_DEVINTERFACE_NET
description: GUID_DEVINTERFACE_NET
ms.assetid: e1cdda95-1915-4bbc-86e9-dff99b7fcc7b
keywords: ["GUID_DEVINTERFACE_NET Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_NET
api_location:
- Ndisguid.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_NET


The GUID_DEVINTERFACE_NET [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [network devices](https://msdn.microsoft.com/library/windows/hardware/ff568356).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>GUID_DEVINTERFACE_NET</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{CAC88484-7515-4C03-82E6-71A87ABAC361}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers of network devices register instances of this device interface class to notify other network components and applications of the presence of network devices.

NDIS registers instances of this interface class for NDIS miniport drivers.

For information about network devices and drivers, see [Network Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff568356).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista, Windows Server 2003 Scalable Networking Pack (SNP), and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ndisguid.h (include Ndisguid.h)</td>
</tr>
</tbody>
</table>

 

 





