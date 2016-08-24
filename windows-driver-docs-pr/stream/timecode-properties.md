---
title: Timecode Properties
author: windows-driver-content
description: Timecode Properties
MS-HAID:
- 'vidcapds\_bc993933-10ec-4130-bf69-bf8037a7c6b6.xml'
- 'stream.timecode\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e8359778-8cc6-4f19-b869-f9597dae0502
keywords: ["timecode properties WDK video capture", "PROPSETID_TIMECODE_READER", "tape timecode properties WDK video capture"]
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Timecode%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


