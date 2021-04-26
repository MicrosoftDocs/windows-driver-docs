---
title: External Transport Properties
description: External Transport Properties
keywords:
- external transport properties WDK video capture
- transport properties WDK video capture
- PROPSETID_EXT_TRANSPORT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# External Transport Properties


The [PROPSETID\_EXT\_TRANSPORT](./propsetid-ext-transport.md) property set contains properties related to the control and transport of data from an external source, such as the type of signal that is transported and for searching to a specific location or timecode on the source's media. The following table describes the properties that are part of the PROPSETID\_EXT\_TRANSPORT property set.

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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-capabilities" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_CAPABILITIES&lt;/strong&gt;](./ksproperty-extxport-capabilities.md)"><strong>KSPROPERTY_EXTXPORT_CAPABILITIES</strong></a></p></td>
<td><p>Returns information on the capabilities of an external data transport, such as whether the device's media can be ejected, or the device can play backwards.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-input-signal-mode" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE&lt;/strong&gt;](./ksproperty-extxport-input-signal-mode.md)"><strong>KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE</strong></a></p></td>
<td><p>Controls the input signal mode of the transport, such as 525 lines, 60 hertz (NTSC) Standard Definition SD-DV, or MPEG2 transport stream.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-output-signal-mode" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_OUTPUT_SIGNAL_MODE&lt;/strong&gt;](./ksproperty-extxport-output-signal-mode.md)"><strong>KSPROPERTY_EXTXPORT_OUTPUT_SIGNAL_MODE</strong></a></p></td>
<td><p>Controls the output signal mode of the transport, such as 625 lines, 50 hertz (PAL) MPEG.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-load-medium" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_LOAD_MEDIUM&lt;/strong&gt;](./ksproperty-extxport-load-medium.md)"><strong>KSPROPERTY_EXTXPORT_LOAD_MEDIUM</strong></a></p></td>
<td><p>Controls the load medium of an external device, such as open tray, close tray, or eject.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-medium-info" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_MEDIUM_INFO&lt;/strong&gt;](./ksproperty-extxport-medium-info.md)"><strong>KSPROPERTY_EXTXPORT_MEDIUM_INFO</strong></a></p></td>
<td><p>Returns information about an external device's medium, such as whether it is a cassette tape or disc, and whether write protection is enabled.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-state" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_STATE&lt;/strong&gt;](./ksproperty-extxport-state.md)"><strong>KSPROPERTY_EXTXPORT_STATE</strong></a></p></td>
<td><p>Controls an external device's transport mode and state.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-state-notify" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_STATE_NOTIFY&lt;/strong&gt;](./ksproperty-extxport-state-notify.md)"><strong>KSPROPERTY_EXTXPORT_STATE_NOTIFY</strong></a></p></td>
<td><p>Controls notification of an external device's transport mode change or of its state change.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-timecode-search" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_TIMECODE_SEARCH&lt;/strong&gt;](./ksproperty-extxport-timecode-search.md)"><strong>KSPROPERTY_EXTXPORT_TIMECODE_SEARCH</strong></a></p></td>
<td><p>Specifies a timecode to search to, including frame, second, minute, and hour.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-atn-search" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_ATN_SEARCH&lt;/strong&gt;](./ksproperty-extxport-atn-search.md)"><strong>KSPROPERTY_EXTXPORT_ATN_SEARCH</strong></a></p></td>
<td><p>Specifies an absolute track number to search to on a tape.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-extxport-rtc-search" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_RTC_SEARCH&lt;/strong&gt;](./ksproperty-extxport-rtc-search.md)"><strong>KSPROPERTY_EXTXPORT_RTC_SEARCH</strong></a></p></td>
<td><p>Specifies a relative time counter to search to on a tape.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-raw-avc-cmd" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_RAW_AVC_CMD&lt;/strong&gt;](./ksproperty-raw-avc-cmd.md)"><strong>KSPROPERTY_EXTXPORT_RAW_AVC_CMD</strong></a></p></td>
<td><p>Controls a raw AV/C code to send to an external device.</p></td>
</tr>
</tbody>
</table>

 

