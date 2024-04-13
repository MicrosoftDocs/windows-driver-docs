---
title: KSCATEGORY_DRM_DESCRAMBLE
description: KSCATEGORY_DRM_DESCRAMBLE
keywords: ["KSCATEGORY_DRM_DESCRAMBLE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_DRM_DESCRAMBLE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# KSCATEGORY_DRM_DESCRAMBLE


The KSCATEGORY_DRM_DESCRAMBLE [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that unscrambles a DRM-protected wave stream.

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
<td align="left"><p>KSCATEGORY_DRM_DESCRAMBLE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{FFBB6E3F-CCFE-4D84-90D9-421418B03A8E}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of KSCATEGORY_DRM_DESCRAMBLE to indicate to the operating system that the devices support the KSCATEGORY_DRM_DESCRAMBLE functional category.

For more information about this functional category, see [Installing Device Interfaces for an Audio Adapter](../audio/installing-device-interfaces-for-an-audio-adapter.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista, Windows Server 2003, Windows XP, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

