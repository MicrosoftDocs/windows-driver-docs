---
title: Tuner Properties
description: Tuner Properties
ms.assetid: 43a0c018-fb0e-4a45-9c9a-5896f1e728ac
keywords:
- tuner properties WDK video capture
- PROPSETID_TUNER
- radio tuner properties WDK video capture
- TV tuner properties WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tuner Properties


The [PROPSETID\_TUNER](https://msdn.microsoft.com/library/windows/hardware/ff567800) property set contains properties related to radio and TV tuners. The following tables describe the properties that are part of the PROPSETID\_TUNER property set. The second table describes properties that are implemented for an AVStream minidriver that runs on Windows Vista and later.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565825" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565825)"><strong>KSPROPERTY_TUNER_CAPS</strong></a></p></td>
<td><p>Returns information on the capabilities of the tuner hardware, including the tuning modes that are supported, such as TV and radio tuning.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565833" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_FREQUENCY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565833)"><strong>KSPROPERTY_TUNER_FREQUENCY</strong></a></p></td>
<td><p>Controls the current TV channel or radio frequency.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565851" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_INPUT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565851)"><strong>KSPROPERTY_TUNER_INPUT</strong></a></p></td>
<td><p>Controls the input to the tuner device, such as coaxial cable or antenna tuner input.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565862" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_MODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565862)"><strong>KSPROPERTY_TUNER_MODE</strong></a></p></td>
<td><p>Controls the tuning device mode, such as analog TV, digital TV, radio, or DSS.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565865" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_MODE_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565865)"><strong>KSPROPERTY_TUNER_MODE_CAPS</strong></a></p></td>
<td><p>Returns the capabilities for each individual tuning mode. Analog TV tuner capabilities that are returned can be different than radio tuning capabilities that are returned.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565907" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_STANDARD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565907)"><strong>KSPROPERTY_TUNER_STANDARD</strong></a></p></td>
<td><p>Returns an analog tuner&#39;s standard, such as NTSC, PAL, or SECAM.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565921" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565921)"><strong>KSPROPERTY_TUNER_STATUS</strong></a></p></td>
<td><p>Returns the current status of a tuner process, including current frequency, PLL offset, and signal strength.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565842" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_IF_MEDIUM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565842)"><strong>KSPROPERTY_TUNER_IF_MEDIUM</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565887" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_SCAN_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565887)"><strong>KSPROPERTY_TUNER_SCAN_CAPS</strong></a></p></td>
<td><p>Returns the supported broadcast network types and whether the tuning device can support signal scans and notifications about the scan results.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565893" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_SCAN_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565893)"><strong>KSPROPERTY_TUNER_SCAN_STATUS</strong></a></p></td>
<td><p>Returns the status of a signal scan.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565909" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_STANDARD_MODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565909)"><strong>KSPROPERTY_TUNER_STANDARD_MODE</strong></a></p></td>
<td><p>Controls whether the tuner can automatically detect the tuner&#39;s standard from the signal.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565881" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565881)"><strong>KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS</strong></a></p></td>
<td><p>Returns the scanning capabilities of a particular broadcast network type that the tuning device supports.</p></td>
</tr>
</tbody>
</table>

 

 

 




