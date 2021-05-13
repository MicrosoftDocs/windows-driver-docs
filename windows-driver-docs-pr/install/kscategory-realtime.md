---
title: KSCATEGORY_REALTIME
description: KSCATEGORY_REALTIME
keywords: ["KSCATEGORY_REALTIME Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_REALTIME
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_REALTIME


The KSCATEGORY_REALTIME [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for an audio device that is connected to a system bus (for example, the PCI bus) and that plays back or captures wave data in real time.

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
<td align="left"><p>KSCATEGORY_REALTIME</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{EB115FFC-10C8-4964-831D-6DCB02E6F23F}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of KSCATEGORY_REALTIME to indicate to the operating system that the devices support the KSCATEGORY_REALTIME functional category.

Devices that register this functional category are operated by the system-supplied [WaveRT port driver](/previous-versions/ff538837(v=vs.85)).

For information about how to register this functional category in an INF file, see the INF file *Ac97smpl.inf* that is included with the [AC'97 sample driver](/samples/browse/) in the WDK.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

