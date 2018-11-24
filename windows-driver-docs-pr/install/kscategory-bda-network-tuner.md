---
title: KSCATEGORY_BDA_NETWORK_TUNER
description: KSCATEGORY_BDA_NETWORK_TUNER
ms.assetid: d3f9d393-c8a1-4280-8796-a1de755f9508
keywords: ["KSCATEGORY_BDA_NETWORK_TUNER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_BDA_NETWORK_TUNER
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_BDA_NETWORK_TUNER


The KSCATEGORY_BDA_NETWORK_TUNER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for a network tuner in the [broadcast driver architecture](https://msdn.microsoft.com/library/windows/hardware/ff556573) (BDA).

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
<td align="left"><p>KSCATEGORY_BDA_NETWORK_TUNER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{71985F48-1CA1-11d3-9CC8-00C04F7971E0}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for BDA devices register instances of KSCATEGORY_BDA_NETWORK_TUNER to indicate to the operating system that the devices support a BDA network tuner filter.

For an example of how to register this functional category in an INF file, see the INF file *BDASwTunerATSC.inf*. *BDASwTunerATSC.inf* is included with the BDA sample generic tuner in the *src\\swtuner\\BDAtuner\\gentuner* subdirectory of the WDK.

For more information about the KS functional category for the network tuner filters, see [Common Control Nodes and Filters](https://msdn.microsoft.com/library/windows/hardware/ff557718) and [BDA Filter Category GUIDs](https://msdn.microsoft.com/library/windows/hardware/ff556521).

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
<td align="left"><p>Available in Windows XP, Windows 2000 with DirectX 9.0A installed, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

 

 





