---
title: KSCATEGORY_DATATRANSFORM
description: KSCATEGORY_DATATRANSFORM
keywords: ["KSCATEGORY_DATATRANSFORM Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_DATATRANSFORM
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_DATATRANSFORM


The KSCATEGORY_DATATRANSFORM [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that transforms audio data streams.

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
<td align="left"><p>KSCATEGORY_DATATRANSFORM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{2EB07EA0-7E70-11D0-A5D6-28DB04C10000}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of KSCATEGORY_DATATRANSFORM to indicate to the operating system that the devices support the KSCATEGORY_DATATRANSFORM functional category.

For an example of how to register this functional category in an INF file, see the *Ddksynth.inf* INF file that is included with the software synthesizer sample in the *src\\audio\\ddksynth* directory of the WDK.

For more information about this functional category, see [Installing Device Interfaces for an Audio Adapter](../audio/installing-device-interfaces-for-an-audio-adapter.md), [**KSPROPERTY_TOPOLOGY_CATEGORIES**](../stream/ksproperty-topology-categories.md), and [Requirements for a GFX Filter Factory](../audio/index.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

 

