---
title: KSCATEGORY_ACOUSTIC_ECHO_CANCEL
description: KSCATEGORY_ACOUSTIC_ECHO_CANCEL
keywords: ["KSCATEGORY_ACOUSTIC_ECHO_CANCEL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_ACOUSTIC_ECHO_CANCEL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# KSCATEGORY_ACOUSTIC_ECHO_CANCEL


The KSCATEGORY_ACOUSTIC_ECHO_CANCEL [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that performs acoustic echo cancellation.

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
<td align="left"><p>KSCATEGORY_ACOUSTIC_ECHO_CANCEL</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{BF963D80-C559-11D0-8A2B-00A0C9255AC1}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS audio devices register instances of KSCATEGORY_ACOUSTIC_ECHO_CANCEL to indicate to the operating system that the devices support the KS functional category that performs acoustic echo cancellation.

For information about device interface classes for audio adapters, see [Installing Device Interfaces for an Audio Adapter](../audio/installing-device-interfaces-for-an-audio-adapter.md).

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

 

