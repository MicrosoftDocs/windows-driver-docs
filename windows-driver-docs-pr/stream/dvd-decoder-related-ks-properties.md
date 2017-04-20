---
title: DVD Decoder Related KS Properties
author: windows-driver-content
description: DVD Decoder Related KS Properties
ms.assetid: 97ce831e-429b-4097-a9f4-625315fe1247
keywords:
- DVD decoder minidrivers WDK , KS properties
- decoder minidrivers WDK DVD , KS properties
- KS properties WDK DVD decoder
- property sets WDK DVD decoder
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DVD Decoder Related KS Properties


## <a href="" id="ddk-dvd-decoder-related-ks-properties-ksg"></a>


The following tables describe the kernel streaming property sets and their respective properties that are related to DVD Decoders:

The [KSPROPSETID\_AudioDecoderOut](https://msdn.microsoft.com/library/windows/hardware/ff566531) property set groups all kernel streaming properties that are related to audio output from the DVD decoder hardware.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSPROPSETID_AudioDecoderOut KS Properties</th>
<th>Property Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_AUDDECOUT_MODES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564284)</p></td>
<td><p>Specifies a bitwise combination of all the potential audio output modes supported by the decoder hardware, such as PCM 5.1, and S/PDIF.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_AUDDECOUT_CUR_MODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564283)</p></td>
<td><p>Specifies the current audio output mode of the decoder hardware, such as stereo analog or S/PDIF.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_DvdSubPic](https://msdn.microsoft.com/library/windows/hardware/ff566573) property set groups all kernel streaming properties that are related to DVD subpicture display.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSPROPSETID_DvdSubPic KS Properties</th>
<th>Property Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_DVDSUBPIC_PALETTE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565151)</p></td>
<td><p>Specifies the 16 YUV color palette entries for the subpicture display.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_DVDSUBPIC_HLI</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565150)</p></td>
<td><p>Specifies the rectangle of the subpicture whose color or contrast is to be changed.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_DVDSUBPIC_COMPOSIT_ON</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565149)</p></td>
<td><p>Specifies whether to enable or disable the display of the DVD subpicture.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_CopyProt](https://msdn.microsoft.com/library/windows/hardware/ff566572) property set groups all kernel streaming properties that are related to Macrovision copy protection of DVD content.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSPROPSETID_CopyProt KS Properties</th>
<th>Property Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_DVDCOPY_CHLG_KEY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565140)</p></td>
<td><p>Specifies the bus challenge key for between the decoder hardware and the DVD drive.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_DVDCOPY_DVD_KEY1</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565145)</p></td>
<td><p>Specifies the first bus key for the decoder as part of the copy protection mechanism.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_DVDCOPY_DEC_KEY2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565142)</p></td>
<td><p>Specifies the second bus key for the decoder as part of the copy protection mechanism.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_DVDCOPY_TITLE_KEY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565148)</p></td>
<td><p>Specifies the title key from the current DVD content as part of the copy protection mechanism.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_COPY_MACROVISION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565114)</p></td>
<td><p>Specifies the Macrovision level of the data stream.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_DVDCOPY_REGION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565146)</p></td>
<td><p>Specifies the current region according to language restrictions as part of the copy protection mechanism.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_DVDCOPY_SET_COPY_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565147)</p></td>
<td><p>Specifies the copy state of the hardware DVD decoder's stream.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_DVDCOPY_DISC_KEY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565144)</p></td>
<td><p>Specifies the disc key for decoder as part of the copy protection mechanism.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_TSRateChange](https://msdn.microsoft.com/library/windows/hardware/ff566700) property set groups all kernel streaming properties that are related to time stamp rate changes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSPROPSETID_TSRateChange KS Properties</th>
<th>Property Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KS_AM_RATE_SimpleRateChange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567288)</p></td>
<td><p>Specifies a start time to begin a new time stamp rate.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KS_AM_RATE_ExactRateChange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567280)</p></td>
<td><p>Specifies an &quot;input&quot; time stamp to begin a new time stamp rate. This property is not yet implemented.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KS_AM_RATE_MaxFullDataRate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567284)</p></td>
<td><p>Specifies the maximum full data rate.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KS_AM_RATE_Step</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567289)</p></td>
<td><p>This property is not yet implemented.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_VPConfig and KSPROPSETID\_VPVBIConfig](https://msdn.microsoft.com/library/windows/hardware/ff566703) property sets group all kernel streaming properties that are related to video port configuration and video port vertical blanking interval configuration. Both property sets contain the same properties.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSPROPSETID_VPConfig and KSPROPSETID_VPVBIConfig KS Properties</th>
<th>Property Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VPCONFIG_NUMCONNECTINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566497)</p></td>
<td><p>Specifies the maximum number of electrical connections to the video port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VPCONFIG_GETCONNECTINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566483)</p></td>
<td><p>Specifies an array of possible video port configurations.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VPCONFIG_SETCONNECTINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566504)</p></td>
<td><p>Specifies a particular video port configuration from the array of possible configurations.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VPCONFIG_VPDATAINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566513)</p></td>
<td><p>Specifies the initial video port configuration, such as pixel aspect ration and field polarity.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VPCONFIG_MAXPIXELRATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566494)</p></td>
<td><p>Specifies the maximum pixel rate of the video port with a particular dimension.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VPCONFIG_NUMVIDEOFORMAT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566500)</p></td>
<td><p>Specifies the maximum number of pixel formats.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VPCONFIG_GETVIDEOFORMAT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566485)</p></td>
<td><p>Specifies an array of possible pixel formats.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VPCONFIG_SETVIDEOFORMAT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566506)</p></td>
<td><p>Specifies a particular pixel format from the array of possible pixel formats..</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VPCONFIG_INVERTPOLARITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566487)</p></td>
<td><p>Specifies whether to invert the polarity of the video port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VPCONFIG_DECIMATIONCAPABILITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566478)</p></td>
<td><p>Specifies whether the hardware can reduce the image size.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VPCONFIG_SCALEFACTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566502)</p></td>
<td><p>Specifies user-defined video port dimensions, including width and height.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VPCONFIG_DDRAWHANDLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566101)</p></td>
<td><p>Specifies the DirectDraw handle information.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VPCONFIG_VIDEOPORTID</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566511)</p></td>
<td><p>Specifies the video port ID information.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VPCONFIG_DDRAWSURFACEHANDLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566471)</p></td>
<td><p>Specifies the DirectDraw surface handle information.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VPCONFIG_SURFACEPARAMS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566509)</p></td>
<td><p>Specifies the surface parameters, such as x and y origins and pitch of the surface.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_Wave](https://msdn.microsoft.com/library/windows/hardware/ff566715) property set groups all kernel streaming properties that are related to controlling the output volume of DVD decoder hardware, or analog TV tuner adapters that possess an audio loop-back cable to a sound adapter.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSPROPSETID_Wave KS Properties</th>
<th>Property Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566516)</p></td>
<td><p>Specifies a device's wave compatible capabilities, such whether the device accepts input and produces output.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_WAVE_INPUT_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566521)</p></td>
<td><p>Specifies the wave input capabilities of the device hardware, such as sampling frequency and bits per sample.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_WAVE_OUTPUT_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566523)</p></td>
<td><p>Specifies the wave output capabilities of the device hardware, such as bits per sample and available sample memory.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_WAVE_BUFFER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566514)</p></td>
<td><p>Specifies the wave buffer settings of the device hardware, such as looping attributes, wave buffer size, and starting address of the wave buffer.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_WAVE_FREQUENCY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566519)</p></td>
<td><p>Specifies the frequency of the device hardware.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_WAVE_VOLUME</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566529)</p></td>
<td><p>Specifies the left and right volume attenuation of the device hardware.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_WAVE_PAN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566526)</p></td>
<td><p>Specifies the left and right pan level of the device hardware.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20DVD%20Decoder%20Related%20KS%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


