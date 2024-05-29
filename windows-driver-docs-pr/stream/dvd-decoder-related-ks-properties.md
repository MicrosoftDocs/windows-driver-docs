---
title: DVD Decoder Related KS Properties
description: DVD Decoder Related KS Properties
keywords:
- DVD decoder minidrivers WDK , KS properties
- decoder minidrivers WDK DVD , KS properties
- KS properties WDK DVD decoder
- property sets WDK DVD decoder
ms.date: 04/20/2017
---

# DVD Decoder Related KS Properties





The following tables describe the kernel streaming property sets and their respective properties that are related to DVD Decoders:

The [KSPROPSETID\_AudioDecoderOut](./kspropsetid-audiodecoderout.md) property set groups all kernel streaming properties that are related to audio output from the DVD decoder hardware.

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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-auddecout-modes" data-raw-source="[&lt;strong&gt;KSPROPERTY_AUDDECOUT_MODES&lt;/strong&gt;](./ksproperty-auddecout-modes.md)"><strong>KSPROPERTY_AUDDECOUT_MODES</strong></a></p></td>
<td><p>Specifies a bitwise combination of all the potential audio output modes supported by the decoder hardware, such as PCM 5.1, and S/PDIF.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-auddecout-cur-mode" data-raw-source="[&lt;strong&gt;KSPROPERTY_AUDDECOUT_CUR_MODE&lt;/strong&gt;](./ksproperty-auddecout-cur-mode.md)"><strong>KSPROPERTY_AUDDECOUT_CUR_MODE</strong></a></p></td>
<td><p>Specifies the current audio output mode of the decoder hardware, such as stereo analog or S/PDIF.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_DvdSubPic](./kspropsetid-dvdsubpic.md) property set groups all kernel streaming properties that are related to DVD subpicture display.

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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdsubpic-palette" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDSUBPIC_PALETTE&lt;/strong&gt;](./ksproperty-dvdsubpic-palette.md)"><strong>KSPROPERTY_DVDSUBPIC_PALETTE</strong></a></p></td>
<td><p>Specifies the 16 YUV color palette entries for the subpicture display.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdsubpic-hli" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDSUBPIC_HLI&lt;/strong&gt;](./ksproperty-dvdsubpic-hli.md)"><strong>KSPROPERTY_DVDSUBPIC_HLI</strong></a></p></td>
<td><p>Specifies the rectangle of the subpicture whose color or contrast is to be changed.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdsubpic-composit-on" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDSUBPIC_COMPOSIT_ON&lt;/strong&gt;](./ksproperty-dvdsubpic-composit-on.md)"><strong>KSPROPERTY_DVDSUBPIC_COMPOSIT_ON</strong></a></p></td>
<td><p>Specifies whether to enable or disable the display of the DVD subpicture.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_CopyProt](./kspropsetid-copyprot.md) property set groups all kernel streaming properties that are related to Macrovision copy protection of DVD content.

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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-chlg-key" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_CHLG_KEY&lt;/strong&gt;](./ksproperty-dvdcopy-chlg-key.md)"><strong>KSPROPERTY_DVDCOPY_CHLG_KEY</strong></a></p></td>
<td><p>Specifies the bus challenge key for between the decoder hardware and the DVD drive.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-dvd-key1" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_DVD_KEY1&lt;/strong&gt;](./ksproperty-dvdcopy-dvd-key1.md)"><strong>KSPROPERTY_DVDCOPY_DVD_KEY1</strong></a></p></td>
<td><p>Specifies the first bus key for the decoder as part of the copy protection mechanism.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-dec-key2" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_DEC_KEY2&lt;/strong&gt;](./ksproperty-dvdcopy-dec-key2.md)"><strong>KSPROPERTY_DVDCOPY_DEC_KEY2</strong></a></p></td>
<td><p>Specifies the second bus key for the decoder as part of the copy protection mechanism.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-title-key" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_TITLE_KEY&lt;/strong&gt;](./ksproperty-dvdcopy-title-key.md)"><strong>KSPROPERTY_DVDCOPY_TITLE_KEY</strong></a></p></td>
<td><p>Specifies the title key from the current DVD content as part of the copy protection mechanism.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-copy-macrovision" data-raw-source="[&lt;strong&gt;KSPROPERTY_COPY_MACROVISION&lt;/strong&gt;](./ksproperty-copy-macrovision.md)"><strong>KSPROPERTY_COPY_MACROVISION</strong></a></p></td>
<td><p>Specifies the Macrovision level of the data stream.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-region" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_REGION&lt;/strong&gt;](./ksproperty-dvdcopy-region.md)"><strong>KSPROPERTY_DVDCOPY_REGION</strong></a></p></td>
<td><p>Specifies the current region according to language restrictions as part of the copy protection mechanism.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-set-copy-state" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_SET_COPY_STATE&lt;/strong&gt;](./ksproperty-dvdcopy-set-copy-state.md)"><strong>KSPROPERTY_DVDCOPY_SET_COPY_STATE</strong></a></p></td>
<td><p>Specifies the copy state of the hardware DVD decoder's stream.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-dvdcopy-disc-key" data-raw-source="[&lt;strong&gt;KSPROPERTY_DVDCOPY_DISC_KEY&lt;/strong&gt;](./ksproperty-dvdcopy-disc-key.md)"><strong>KSPROPERTY_DVDCOPY_DISC_KEY</strong></a></p></td>
<td><p>Specifies the disc key for decoder as part of the copy protection mechanism.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_TSRateChange](./kspropsetid-tsratechange.md) property set groups all kernel streaming properties that are related to time stamp rate changes.

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
<td><p><a href="/windows-hardware/drivers/stream/ks-am-rate-simpleratechange" data-raw-source="[&lt;strong&gt;KS_AM_RATE_SimpleRateChange&lt;/strong&gt;](./ks-am-rate-simpleratechange.md)"><strong>KS_AM_RATE_SimpleRateChange</strong></a></p></td>
<td><p>Specifies a start time to begin a new time stamp rate.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ks-am-rate-exactratechange" data-raw-source="[&lt;strong&gt;KS_AM_RATE_ExactRateChange&lt;/strong&gt;](./ks-am-rate-exactratechange.md)"><strong>KS_AM_RATE_ExactRateChange</strong></a></p></td>
<td><p>Specifies an "input" time stamp to begin a new time stamp rate. This property is not yet implemented.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ks-am-rate-maxfulldatarate" data-raw-source="[&lt;strong&gt;KS_AM_RATE_MaxFullDataRate&lt;/strong&gt;](./ks-am-rate-maxfulldatarate.md)"><strong>KS_AM_RATE_MaxFullDataRate</strong></a></p></td>
<td><p>Specifies the maximum full data rate.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ks-am-rate-step" data-raw-source="[&lt;strong&gt;KS_AM_RATE_Step&lt;/strong&gt;](./ks-am-rate-step.md)"><strong>KS_AM_RATE_Step</strong></a></p></td>
<td><p>This property is not yet implemented.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_VPConfig and KSPROPSETID\_VPVBIConfig](./kspropsetid-vpconfig-and-kspropsetid-vpvbiconfig.md) property sets group all kernel streaming properties that are related to video port configuration and video port vertical blanking interval configuration. Both property sets contain the same properties.

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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-numconnectinfo" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_NUMCONNECTINFO&lt;/strong&gt;](./ksproperty-vpconfig-numconnectinfo.md)"><strong>KSPROPERTY_VPCONFIG_NUMCONNECTINFO</strong></a></p></td>
<td><p>Specifies the maximum number of electrical connections to the video port.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-getconnectinfo" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_GETCONNECTINFO&lt;/strong&gt;](./ksproperty-vpconfig-getconnectinfo.md)"><strong>KSPROPERTY_VPCONFIG_GETCONNECTINFO</strong></a></p></td>
<td><p>Specifies an array of possible video port configurations.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-setconnectinfo" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_SETCONNECTINFO&lt;/strong&gt;](./ksproperty-vpconfig-setconnectinfo.md)"><strong>KSPROPERTY_VPCONFIG_SETCONNECTINFO</strong></a></p></td>
<td><p>Specifies a particular video port configuration from the array of possible configurations.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-vpdatainfo" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_VPDATAINFO&lt;/strong&gt;](./ksproperty-vpconfig-vpdatainfo.md)"><strong>KSPROPERTY_VPCONFIG_VPDATAINFO</strong></a></p></td>
<td><p>Specifies the initial video port configuration, such as pixel aspect ratio and field polarity.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-maxpixelrate" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_MAXPIXELRATE&lt;/strong&gt;](./ksproperty-vpconfig-maxpixelrate.md)"><strong>KSPROPERTY_VPCONFIG_MAXPIXELRATE</strong></a></p></td>
<td><p>Specifies the maximum pixel rate of the video port with a particular dimension.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-numvideoformat" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_NUMVIDEOFORMAT&lt;/strong&gt;](./ksproperty-vpconfig-numvideoformat.md)"><strong>KSPROPERTY_VPCONFIG_NUMVIDEOFORMAT</strong></a></p></td>
<td><p>Specifies the maximum number of pixel formats.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-getvideoformat" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_GETVIDEOFORMAT&lt;/strong&gt;](./ksproperty-vpconfig-getvideoformat.md)"><strong>KSPROPERTY_VPCONFIG_GETVIDEOFORMAT</strong></a></p></td>
<td><p>Specifies an array of possible pixel formats.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-setvideoformat" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_SETVIDEOFORMAT&lt;/strong&gt;](./ksproperty-vpconfig-setvideoformat.md)"><strong>KSPROPERTY_VPCONFIG_SETVIDEOFORMAT</strong></a></p></td>
<td><p>Specifies a particular pixel format from the array of possible pixel formats..</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-invertpolarity" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_INVERTPOLARITY&lt;/strong&gt;](./ksproperty-vpconfig-invertpolarity.md)"><strong>KSPROPERTY_VPCONFIG_INVERTPOLARITY</strong></a></p></td>
<td><p>Specifies whether to invert the polarity of the video port.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-decimationcapability" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_DECIMATIONCAPABILITY&lt;/strong&gt;](./ksproperty-vpconfig-decimationcapability.md)"><strong>KSPROPERTY_VPCONFIG_DECIMATIONCAPABILITY</strong></a></p></td>
<td><p>Specifies whether the hardware can reduce the image size.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-scalefactor" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_SCALEFACTOR&lt;/strong&gt;](./ksproperty-vpconfig-scalefactor.md)"><strong>KSPROPERTY_VPCONFIG_SCALEFACTOR</strong></a></p></td>
<td><p>Specifies user-defined video port dimensions, including width and height.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-ddrawhandle" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_DDRAWHANDLE&lt;/strong&gt;](./ksproperty-vpconfig-ddrawhandle.md)"><strong>KSPROPERTY_VPCONFIG_DDRAWHANDLE</strong></a></p></td>
<td><p>Specifies the DirectDraw handle information.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-videoportid" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_VIDEOPORTID&lt;/strong&gt;](./ksproperty-vpconfig-videoportid.md)"><strong>KSPROPERTY_VPCONFIG_VIDEOPORTID</strong></a></p></td>
<td><p>Specifies the video port ID information.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-ddrawsurfacehandle" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_DDRAWSURFACEHANDLE&lt;/strong&gt;](./ksproperty-vpconfig-ddrawsurfacehandle.md)"><strong>KSPROPERTY_VPCONFIG_DDRAWSURFACEHANDLE</strong></a></p></td>
<td><p>Specifies the DirectDraw surface handle information.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-vpconfig-surfaceparams" data-raw-source="[&lt;strong&gt;KSPROPERTY_VPCONFIG_SURFACEPARAMS&lt;/strong&gt;](./ksproperty-vpconfig-surfaceparams.md)"><strong>KSPROPERTY_VPCONFIG_SURFACEPARAMS</strong></a></p></td>
<td><p>Specifies the surface parameters, such as x and y origins and pitch of the surface.</p></td>
</tr>
</tbody>
</table>

 

The [KSPROPSETID\_Wave](./kspropsetid-wave.md) property set groups all kernel streaming properties that are related to controlling the output volume of DVD decoder hardware, or analog TV tuner adapters that possess an audio loop-back cable to a sound adapter.

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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-wave-compatible-capabilities" data-raw-source="[&lt;strong&gt;KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES&lt;/strong&gt;](./ksproperty-wave-compatible-capabilities.md)"><strong>KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES</strong></a></p></td>
<td><p>Specifies a device's wave compatible capabilities, such whether the device accepts input and produces output.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-wave-input-capabilities" data-raw-source="[&lt;strong&gt;KSPROPERTY_WAVE_INPUT_CAPABILITIES&lt;/strong&gt;](./ksproperty-wave-input-capabilities.md)"><strong>KSPROPERTY_WAVE_INPUT_CAPABILITIES</strong></a></p></td>
<td><p>Specifies the wave input capabilities of the device hardware, such as sampling frequency and bits per sample.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-wave-output-capabilities" data-raw-source="[&lt;strong&gt;KSPROPERTY_WAVE_OUTPUT_CAPABILITIES&lt;/strong&gt;](./ksproperty-wave-output-capabilities.md)"><strong>KSPROPERTY_WAVE_OUTPUT_CAPABILITIES</strong></a></p></td>
<td><p>Specifies the wave output capabilities of the device hardware, such as bits per sample and available sample memory.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-wave-buffer" data-raw-source="[&lt;strong&gt;KSPROPERTY_WAVE_BUFFER&lt;/strong&gt;](./ksproperty-wave-buffer.md)"><strong>KSPROPERTY_WAVE_BUFFER</strong></a></p></td>
<td><p>Specifies the wave buffer settings of the device hardware, such as looping attributes, wave buffer size, and starting address of the wave buffer.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-wave-frequency" data-raw-source="[&lt;strong&gt;KSPROPERTY_WAVE_FREQUENCY&lt;/strong&gt;](./ksproperty-wave-frequency.md)"><strong>KSPROPERTY_WAVE_FREQUENCY</strong></a></p></td>
<td><p>Specifies the frequency of the device hardware.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-wave-volume" data-raw-source="[&lt;strong&gt;KSPROPERTY_WAVE_VOLUME&lt;/strong&gt;](./ksproperty-wave-volume.md)"><strong>KSPROPERTY_WAVE_VOLUME</strong></a></p></td>
<td><p>Specifies the left and right volume attenuation of the device hardware.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-wave-pan" data-raw-source="[&lt;strong&gt;KSPROPERTY_WAVE_PAN&lt;/strong&gt;](./ksproperty-wave-pan.md)"><strong>KSPROPERTY_WAVE_PAN</strong></a></p></td>
<td><p>Specifies the left and right pan level of the device hardware.</p></td>
</tr>
</tbody>
</table>

 

