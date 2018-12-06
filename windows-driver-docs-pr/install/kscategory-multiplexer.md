---
title: KSCATEGORY_MULTIPLEXER
description: KSCATEGORY_MULTIPLEXER
ms.assetid: 3023769a-9b98-4c12-90b1-f83294a45ab0
keywords: ["KSCATEGORY_MULTIPLEXER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_MULTIPLEXER
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_MULTIPLEXER


The KSCATEGORY_MULTIPLEXER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for a multiplexer device.

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
<td align="left"><p>KSCATEGORY_MULTIPLEXER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{7A5DE1D3-01A1-452c-B481-4FA2B96271E8}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY_MULTIPLEXER to indicate to the operating system that the devices support the KSCATEGORY_MULTIPLEXER functional category.

For an example of how to register this functional category in an INF file, see the *Bdan.inf* INF file that is included with the software tuner sample in the *src/swtuner/algtuner* directory of the WDK.

For information about multiplexers, see [Topology Filters](https://msdn.microsoft.com/library/windows/hardware/ff538552).

For more information about the KSCATEGORY_MULTIPLEXER functional category, see [Encoder Installation and Registration](https://msdn.microsoft.com/library/windows/hardware/ff559551).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 





