---
title: Timecode Properties
description: Timecode Properties
ms.assetid: e8359778-8cc6-4f19-b869-f9597dae0502
keywords:
- timecode properties WDK video capture
- PROPSETID_TIMECODE_READER
- tape timecode properties WDK video capture
ms.date: 04/20/2017
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565776" data-raw-source="[&lt;strong&gt;KSPROPERTY_TIMECODE_READER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565776)"><strong>KSPROPERTY_TIMECODE_READER</strong></a></p></td>
<td><p>Returns the timecode for the current tape position.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564282" data-raw-source="[&lt;strong&gt;KSPROPERTY_ATN_READER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564282)"><strong>KSPROPERTY_ATN_READER</strong></a></p></td>
<td><p>Returns the absolute track number for the current tape position.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565215" data-raw-source="[&lt;strong&gt;KSPROPERTY_RTC_READER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565215)"><strong>KSPROPERTY_RTC_READER</strong></a></p></td>
<td><p>Returns the relative time counter for the current tape position.</p></td>
</tr>
</tbody>
</table>

 

 

 




