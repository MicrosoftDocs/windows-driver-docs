---
title: Timecode Properties
author: windows-driver-content
description: Timecode Properties
ms.assetid: e8359778-8cc6-4f19-b869-f9597dae0502
keywords:
- timecode properties WDK video capture
- PROPSETID_TIMECODE_READER
- tape timecode properties WDK video capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Timecode Properties


The [PROPSETID\_TIMECODE\_READER](https://msdn.microsoft.com/library/windows/hardware/ff567798) property set contains properties related to timecode on a tape, such as a DVHS tape deck or a MiniDV camcorder. The following table describes the properties that are part of the PROPSETID\_TIMECODE\_READER property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_TIMECODE_READER KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_TIMECODE_READER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565776)</p></td>
<td><p>Returns the timecode for the current tape position.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_ATN_READER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564282)</p></td>
<td><p>Returns the absolute track number for the current tape position.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_RTC_READER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565215)</p></td>
<td><p>Returns the relative time counter for the current tape position.</p></td>
</tr>
</tbody>
</table>

 

 

 




