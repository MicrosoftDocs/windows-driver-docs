---
title: External Transport Properties
author: windows-driver-content
description: External Transport Properties
ms.assetid: e57e6c13-dfa3-4bec-9136-0e2bb2ffdd56
keywords:
- external transport properties WDK video capture
- transport properties WDK video capture
- PROPSETID_EXT_TRANSPORT
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# External Transport Properties


The [PROPSETID\_EXT\_TRANSPORT](https://msdn.microsoft.com/library/windows/hardware/ff567797) property set contains properties related to the control and transport of data from an external source, such as the type of signal that is transported and for searching to a specific location or timecode on the source's media. The following table describes the properties that are part of the PROPSETID\_EXT\_TRANSPORT property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_EXT_TRANSPORT KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_EXTXPORT_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565160)</p></td>
<td><p>Returns information on the capabilities of an external data transport, such as whether the device's media can be ejected, or the device can play backwards.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565161)</p></td>
<td><p>Controls the input signal mode of the transport, such as 525 lines, 60 hertz (NTSC) Standard Definition SD-DV, or MPEG2 transport stream.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_EXTXPORT_OUTPUT_SIGNAL_MODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565165)</p></td>
<td><p>Controls the output signal mode of the transport, such as 625 lines, 50 hertz (PAL) MPEG.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_EXTXPORT_LOAD_MEDIUM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565162)</p></td>
<td><p>Controls the load medium of an external device, such as open tray, close tray, or eject.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_EXTXPORT_MEDIUM_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565163)</p></td>
<td><p>Returns information about an external device's medium, such as whether it is a cassette tape or disc, and whether write protection is enabled.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_EXTXPORT_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565168)</p></td>
<td><p>Controls an external device's transport mode and state.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_EXTXPORT_STATE_NOTIFY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565169)</p></td>
<td><p>Controls notification of an external device's transport mode change or of its state change.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_EXTXPORT_TIMECODE_SEARCH</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565170)</p></td>
<td><p>Specifies a timecode to search to, including frame, second, minute, and hour.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_EXTXPORT_ATN_SEARCH</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565159)</p></td>
<td><p>Specifies an absolute track number to search to on a tape.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_EXTXPORT_RTC_SEARCH</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565166)</p></td>
<td><p>Specifies a relative time counter to search to on a tape.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_EXTXPORT_RAW_AVC_CMD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565214)</p></td>
<td><p>Controls a raw AV/C code to send to an external device.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20External%20Transport%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


