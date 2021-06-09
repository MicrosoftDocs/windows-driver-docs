---
title: KSCATEGORY_TOPOLOGY
description: KSCATEGORY_TOPOLOGY
keywords: ["KSCATEGORY_TOPOLOGY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_TOPOLOGY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_TOPOLOGY


The KSCATEGORY_TOPOLOGY [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for the internal topology of an audio device.

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
<td align="left"><p>KSCATEGORY_TOPOLOGY</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{DDA54A40-1E4C-11D1-A050-405705C10000}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS audio adapter devices register instances of KSCATEGORY_TOPOLOGY to indicate to the operating system that the devices support the KSCATEGORY_TOPOLOGY functional category.

For information about device interface classes for audio adapters, see [Installing Device Interfaces for an Audio Adapter](../audio/installing-device-interfaces-for-an-audio-adapter.md).

The [AC'97 sample driver](/samples/browse/) that is provided in the WDK enumerates instances of the KSCATEGORY_TOPOLOGY device interface class.

The sysfx sample in the WDK registers instances of this device interface class. The sysfx sample is located in the *src\\audio\\sysfx directory* of the WDK.

## Requirements

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

