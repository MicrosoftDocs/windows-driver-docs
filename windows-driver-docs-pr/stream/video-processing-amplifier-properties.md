---
title: Video Processing Amplifier Properties
description: Video Processing Amplifier Properties
ms.assetid: 1adc4fcc-c9a2-41a8-90db-1030ba7c257f
keywords:
- video processing amplifier properties WDK video capture
- amplification properties WDK video capture
- saturation WDK video capture
- contrast WDK video capture
- hue WDK video capture
- PROPSETID_VIDCAP_VIDEOPROCAMP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Processing Amplifier Properties


The [PROPSETID\_VIDCAP\_VIDEOPROCAMP](https://msdn.microsoft.com/library/windows/hardware/ff568122) property set contains properties related to video processing amplification, such as video attributes including hue, contrast, and saturation. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_VIDOPROCAMP property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_VIDEOPROCAMP KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566063" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_BACKLIGHT_COMPENSATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566063)"><strong>KSPROPERTY_VIDEOPROCAMP_BACKLIGHT_COMPENSATION</strong></a></p></td>
<td><p>Controls a camera&#39;s backlight compensation setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566065" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566065)"><strong>KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS</strong></a></p></td>
<td><p>Controls a camera&#39;s brightness.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566066" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_COLORENABLE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566066)"><strong>KSPROPERTY_VIDEOPROCAMP_COLORENABLE</strong></a></p></td>
<td><p>Controls a camera&#39;s color enable setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566070" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_CONTRAST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566070)"><strong>KSPROPERTY_VIDEOPROCAMP_CONTRAST</strong></a></p></td>
<td><p>Controls a camera&#39;s luminance setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566076" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_GAMMA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566076)"><strong>KSPROPERTY_VIDEOPROCAMP_GAMMA</strong></a></p></td>
<td><p>Controls a camera&#39;s gamut setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566078" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_HUE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566078)"><strong>KSPROPERTY_VIDEOPROCAMP_HUE</strong></a></p></td>
<td><p>Controls a camera&#39;s hue setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566092" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_SATURATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566092)"><strong>KSPROPERTY_VIDEOPROCAMP_SATURATION</strong></a></p></td>
<td><p>Controls a camera&#39;s chrominance setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566093" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_SHARPNESS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566093)"><strong>KSPROPERTY_VIDEOPROCAMP_SHARPNESS</strong></a></p></td>
<td><p>Controls a camera&#39;s sharpness setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566095" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566095)"><strong>KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE</strong></a></p></td>
<td><p>Controls a camera&#39;s white balance setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566074" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_GAIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566074)"><strong>KSPROPERTY_VIDEOPROCAMP_GAIN</strong></a></p></td>
<td><p>Controls a camera&#39;s gain setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566071" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566071)"><strong>KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER</strong></a></p></td>
<td><p>Controls a camera&#39;s digital zoom multiplier.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566072" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566072)"><strong>KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT</strong></a></p></td>
<td><p>Controls the upper limit of a camera&#39;s digital zoom.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566097" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE_COMPONENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566097)"><strong>KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE_COMPONENT</strong></a></p></td>
<td><p>Controls a camera&#39;s white balance setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566086" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_POWERLINE_FREQUENCY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566086)"><strong>KSPROPERTY_VIDEOPROCAMP_POWERLINE_FREQUENCY</strong></a></p></td>
<td><p>Controls the powerline frequency of a camera&#39;s operating environment.</p></td>
</tr>
</tbody>
</table>

 

 

 




