---
title: KSMFT_CATEGORY_VIDEO_PROCESSOR
description: KSMFT_CATEGORY_VIDEO_PROCESSOR
keywords: ["KSMFT_CATEGORY_VIDEO_PROCESSOR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSMFT_CATEGORY_VIDEO_PROCESSOR
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSMFT_CATEGORY_VIDEO_PROCESSOR


The KSMFT_CATEGORY_VIDEO_PROCESSOR [device interface class](./overview-of-device-interface-classes.md) is defined for the [Kernel Streaming](../stream/kernel-streaming.md) (KS) functional category for a video device.

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
<td align="left"><p>KSMFT_CATEGORY_VIDEO_PROCESSOR</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{302ea3fc-aa5f-47f9-9f7a-c2188bb16302}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

AVStream drivers that have MFT codec support register instances of this device interface class to indicate to the operating system that the devices support the KSMFT_CATEGORY_VIDEO_PROCESSOR functional category.

For more information about device interface classes for AVStream devices with hardware codec support, see [Getting Started with Hardware Codec Support in AVStream](../stream/getting-started-with-hardware-codec-support-in-avstream.md).

For more information about how to register this functional category in an INF file, see the *Hiddigi.inf* file, which is included with the *src\\input\\hiddigi* sample drivers in the WDK.

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

 

