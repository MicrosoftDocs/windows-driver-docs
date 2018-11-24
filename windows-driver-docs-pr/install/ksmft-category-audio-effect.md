---
title: KSMFT_CATEGORY_AUDIO_EFFECT
description: KSMFT_CATEGORY_AUDIO_EFFECT
ms.assetid: a6747c99-3c16-4833-905a-52472a854f77
keywords: ["KSMFT_CATEGORY_AUDIO_EFFECT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSMFT_CATEGORY_AUDIO_EFFECT
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSMFT_CATEGORY_AUDIO_EFFECT


The KSMFT_CATEGORY_AUDIO_EFFECT [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [Kernel Streaming](https://msdn.microsoft.com/library/windows/hardware/ff560842) (KS) functional category for an audio device.

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
<td align="left"><p>KSMFT_CATEGORY_AUDIO_EFFECT</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{11064c48-3648-4ed0-932e-05ce8ac811b7}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

AVStream drivers that have MFT codec support register instances of this device interface class to indicate to the operating system that the devices support the KSMFT_CATEGORY_AUDIO_EFFECT functional category.

For more information about device interface classes for AVStream devices with hardware codec support, see [Getting Started with Hardware Codec Support in AVStream](https://msdn.microsoft.com/library/windows/hardware/gg299325).

For more information about how to register this functional category in an INF file, see the *Hiddigi.inf* file, which is included with the *src\\input\\hiddigi* sample drivers in the WDK.

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

 

 





