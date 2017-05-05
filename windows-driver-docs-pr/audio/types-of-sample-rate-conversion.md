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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Types%20of%20Sample%20Rate%20Conversion%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


