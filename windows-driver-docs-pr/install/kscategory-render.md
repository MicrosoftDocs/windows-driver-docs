---
title: KSCATEGORY_RENDER
description: KSCATEGORY_RENDER
ms.assetid: 467e3192-46c4-4ef4-88cf-0a870efc1725
keywords: ["KSCATEGORY_RENDER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_RENDER
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_RENDER


The KSCATEGORY_RENDER [device interface class](https://docs.microsoft.com/windows-hardware/drivers/install/device-interface-classes) is defined for the [kernel streaming](https://docs.microsoft.com/windows-hardware/drivers/stream/streaming-minidrivers2) (KS) functional category that renders wave and MIDI data streams.

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
<td align="left"><p>KSCATEGORY_RENDER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{65E8773E-8F56-11D0-A3B9-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS audio adapter devices register an instance of KSCATEGORY_RENDER to indicate that the devices support the KSCATEGORY_RENDER functional category.

For information about how to register this functional category in an INF file, see the INF file *Ac97smpl.inf* that is included with the [AC'97 sample driver](https://go.microsoft.com/fwlink/p/?linkid=256075) in the WDK.

For information about device interface classes for audio adapters, see [Installing Device Interfaces for an Audio Adapter](https://docs.microsoft.com/windows-hardware/drivers/audio/installing-device-interfaces-for-an-audio-adapter) and [**KSPROPERTY_TOPOLOGY_CATEGORIES**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-topology-categories).

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
<td align="left">Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

 

 





