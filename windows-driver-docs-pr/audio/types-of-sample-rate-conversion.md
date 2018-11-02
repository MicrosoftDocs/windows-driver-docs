---
title: Types of Sample Rate Conversion
description: Types of Sample Rate Conversion
ms.assetid: eaea0714-8167-4fbb-b630-0dce5e908cc2
keywords:
- SRC WDK audio , types
- sample-rate conversion WDK audio , types
- linear interpolation WDK audio
- multipoint interpolation WDK audio
- high-end multipoint interpolation WDK audio
- Add/Drop SRC WDK audio
- truncation SRC WDK audio
- nearest neighbor SRC WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Types of Sample Rate Conversion


## <span id="types_of_sample_rate_conversion"></span><span id="TYPES_OF_SAMPLE_RATE_CONVERSION"></span>


The different kinds of sample-rate conversion (SRC) that the KMixer system driver can perform are shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Type of Sample Rate Conversion</th>
<th align="left">Characteristics</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Linear interpolation</p></td>
<td align="left"><p>Uses linear interpolation to achieve reasonable accuracy if converting similar sampling rates; for example, converting a 12-kHz rate to a 13-kHz rate. DirectSound applications use linear interpolation by default.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Multipoint interpolation</p></td>
<td align="left"><p>Uses a simplified version of high-end multipoint interpolation to achieve a signal-to-noise ratio of approximately 70 decibels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>High-end multipoint interpolation</p></td>
<td align="left"><p>Uses oversampling to achieve a signal-to-noise ratio greater than or equal to 90 decibels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Add/Drop (also known as truncation or nearest neighbor)</p></td>
<td align="left"><p>Uses a simple replacement technique that minimizes system load, but achieves the lowest quality. This type of SRC is only used if system constraints prevent using one of the higher quality types of SRC.</p></td>
</tr>
</tbody>
</table>

 

KMixer uses software emulation to implement all the SRC techniques described in the preceding table.

 

 




