---
title: Tuner Properties
description: Tuner Properties
keywords:
- tuner properties WDK video capture
- PROPSETID_TUNER
- radio tuner properties WDK video capture
- TV tuner properties WDK video capture
ms.date: 04/20/2017
---

# Tuner Properties


The [PROPSETID\_TUNER](./propsetid-tuner.md) property set contains properties related to radio and TV tuners. The following tables describe the properties that are part of the PROPSETID\_TUNER property set. The second table describes properties that are implemented for an AVStream minidriver that runs on Windows Vista and later.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_TUNER KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-caps" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_CAPS&lt;/strong&gt;](./ksproperty-tuner-caps.md)"><strong>KSPROPERTY_TUNER_CAPS</strong></a></p></td>
<td><p>Returns information on the capabilities of the tuner hardware, including the tuning modes that are supported, such as TV and radio tuning.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-frequency" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_FREQUENCY&lt;/strong&gt;](./ksproperty-tuner-frequency.md)"><strong>KSPROPERTY_TUNER_FREQUENCY</strong></a></p></td>
<td><p>Controls the current TV channel or radio frequency.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-input" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_INPUT&lt;/strong&gt;](./ksproperty-tuner-input.md)"><strong>KSPROPERTY_TUNER_INPUT</strong></a></p></td>
<td><p>Controls the input to the tuner device, such as coaxial cable or antenna tuner input.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-mode" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_MODE&lt;/strong&gt;](./ksproperty-tuner-mode.md)"><strong>KSPROPERTY_TUNER_MODE</strong></a></p></td>
<td><p>Controls the tuning device mode, such as analog TV, digital TV, radio, or DSS.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-mode-caps" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_MODE_CAPS&lt;/strong&gt;](./ksproperty-tuner-mode-caps.md)"><strong>KSPROPERTY_TUNER_MODE_CAPS</strong></a></p></td>
<td><p>Returns the capabilities for each individual tuning mode. Analog TV tuner capabilities that are returned can be different than radio tuning capabilities that are returned.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-standard" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_STANDARD&lt;/strong&gt;](./ksproperty-tuner-standard.md)"><strong>KSPROPERTY_TUNER_STANDARD</strong></a></p></td>
<td><p>Returns an analog tuner's standard, such as NTSC, PAL, or SECAM.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-status" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_STATUS&lt;/strong&gt;](./ksproperty-tuner-status.md)"><strong>KSPROPERTY_TUNER_STATUS</strong></a></p></td>
<td><p>Returns the current status of a tuner process, including current frequency, PLL offset, and signal strength.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-if-medium" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_IF_MEDIUM&lt;/strong&gt;](./ksproperty-tuner-if-medium.md)"><strong>KSPROPERTY_TUNER_IF_MEDIUM</strong></a></p></td>
<td><p>Returns the pin medium for the intermediate frequency pin for tuner devices that support digital TV.</p></td>
</tr>
</tbody>
</table>

 

The following table describes the PROPSETID\_TUNER properties that are new for Windows Vista.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_TUNER KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-scan-caps" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_SCAN_CAPS&lt;/strong&gt;](./ksproperty-tuner-scan-caps.md)"><strong>KSPROPERTY_TUNER_SCAN_CAPS</strong></a></p></td>
<td><p>Returns the supported broadcast network types and whether the tuning device can support signal scans and notifications about the scan results.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-scan-status" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_SCAN_STATUS&lt;/strong&gt;](./ksproperty-tuner-scan-status.md)"><strong>KSPROPERTY_TUNER_SCAN_STATUS</strong></a></p></td>
<td><p>Returns the status of a signal scan.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-standard-mode" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_STANDARD_MODE&lt;/strong&gt;](./ksproperty-tuner-standard-mode.md)"><strong>KSPROPERTY_TUNER_STANDARD_MODE</strong></a></p></td>
<td><p>Controls whether the tuner can automatically detect the tuner's standard from the signal.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-tuner-networktype-scan-caps" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS&lt;/strong&gt;](./ksproperty-tuner-networktype-scan-caps.md)"><strong>KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS</strong></a></p></td>
<td><p>Returns the scanning capabilities of a particular broadcast network type that the tuning device supports.</p></td>
</tr>
</tbody>
</table>

 

