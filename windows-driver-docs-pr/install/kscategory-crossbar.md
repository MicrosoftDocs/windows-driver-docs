---
title: KSCATEGORY_CROSSBAR
description: KSCATEGORY_CROSSBAR
ms.assetid: 0a5edfd5-ad50-4402-8f6d-d6c5018d1ab2
keywords: ["KSCATEGORY_CROSSBAR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_CROSSBAR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_CROSSBAR


The KSCATEGORY_CROSSBAR [device interface class](https://docs.microsoft.com/windows-hardware/drivers/install/device-interface-classes) is defined for the [kernel streaming](https://docs.microsoft.com/windows-hardware/drivers/stream/streaming-minidrivers2) (KS) functional category for a crossbar device that routes video and audio streams.

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
<td align="left"><p>KSCATEGORY_CROSSBAR</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{A799A801-A46D-11D0-A18C-00A02401DCD4}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY_CROSSBAR to indicate to the operating system that the devices support the KSCATEGORY_CROSSBAR functional category.

For an example of how to register this functional category in an INF file, see the *Bdan.inf* INF file that is included with the software tuner sample in the *src\\swtuner\\algtuner* directory of the WDK.

For information about crossbar devices for audio and video, see [Filters Used with the Video Capture Devices](https://docs.microsoft.com/windows-hardware/drivers/stream/filters-used-with-the-video-capture-devices) and [Analog Video Category](https://docs.microsoft.com/windows-hardware/drivers/stream/analog-video-category).

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

 

 





