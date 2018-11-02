---
title: Subformat GUIDs for Compressed Audio Formats
description: Subformat GUIDs for Compressed Audio Formats
ms.assetid: f9595d6c-952c-4266-8eb5-5c8581051d28
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Subformat GUIDs for Compressed Audio Formats


For Windows 7, new subformat GUIDs have been added to the Ksmedia.h header file to provide support for compressed audio formats. Subformat GUIDs indicate the specific subformat of a data format. These formats are defined by the Consumer Electronics Association (CEA) standard for uncompressed audio.

As a result of the CEA-861-D standard, you must ensure that audio formats that are not supported by a CEA device are not transmitted to such a device. High definition multimedia interface (HDMI) and [DisplayPort](https://www.displayport.org/) are examples of CEA devices.

For user-mode access, the GUIDs are specified in the **SubFormat** member of [WAVEFORMATEXTENSIBLE](https://go.microsoft.com/fwlink/p/?linkid=142020) and in the **FormatExt** member of [WAVEFORMATEXTENSIBLE\_IEC61937](https://go.microsoft.com/fwlink/p/?linkid=142021). For kernel-mode access for audio drivers, the GUIDs are specified in the **DataRange** member of the [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure,

The GUIDs for the available compressed audio formats are listed in the following table.

**Note**   Not all the available formats are supported by the Windows 7 HD audio class driver. The formats supported by Windows 7 are indicated in the tables with an asterisk (\*).

 

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CEA 861 type</th>
<th align="left">SubFormat GUID</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00</p></td>
<td align="left"></td>
<td align="left"><p>Refer to the stream.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x01</p></td>
<td align="left"><p>00000000-0000-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_WAVEFORMATEX</p></td>
<td align="left"><p>IEC 60958 PCM<em></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x02</p></td>
<td align="left"><p>00000092-0000-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL</p></td>
<td align="left"><p>AC-3</em></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x03</p></td>
<td align="left"><p>00000003-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_MPEG1</p></td>
<td align="left"><p>MPEG-1 (Layer1 &amp; 2)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x04</p></td>
<td align="left"><p>00000004-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_MPEG3</p></td>
<td align="left"><p>MPEG-3 (Layer 3)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x05</p></td>
<td align="left"><p>00000005-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_MPEG2</p></td>
<td align="left"><p>MPEG-2 (Multichanel)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x06</p></td>
<td align="left"><p>00000006-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_AAC</p></td>
<td align="left"><p>Advanced audio coding* (MPEG-2/4 AAC in ADTS)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x07</p></td>
<td align="left"><p>00000008-0000-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_DTS</p></td>
<td align="left"><p>Digital Theater Sound (DTS)<em></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0a</p></td>
<td align="left"><p>0000000a-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS</p></td>
<td align="left"><p>Dolby Digital Plus</em></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0f</p></td>
<td align="left"><p>Unused.</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

The GUIDs for audio formats that are transmitted in high bit-rate audio sample packets are listed in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CEA 861 type</th>
<th align="left">SubFormat GUID</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0b</p></td>
<td align="left"><p>0000000b-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_DTS_HD</p></td>
<td align="left"><p>DTS-HD (24-bit, 95KHz)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0c</p></td>
<td align="left"><p>0000000c-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MLP</p></td>
<td align="left"><p>MAT(MLP)<em>- Meridian Lossless Packing (Dolby Digital True HD - 24-bit 196KHz/up to 18M bps, 8 channels)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0e</p></td>
<td align="left"><p>00000164-0000-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_WMA_PRO</p></td>
<td align="left"><p>Windows Media Audio (WMA) Pro</em></p></td>
</tr>
</tbody>
</table>

 

The GUIDs for compressed audio formats that can be implemented by third-party solutions are listed in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CEA 861 type</th>
<th align="left">SubFormat GUID</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x08</p></td>
<td align="left"><p>00000008-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_ATRAC</p></td>
<td align="left"><p>Adaptive Transform Acoustic Coding (ATRAC)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x09</p></td>
<td align="left"><p>00000009-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_ONE_BIT_AUDIO</p></td>
<td align="left"><p>One-bit audio</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0d</p></td>
<td align="left"><p>0000000d-0cea-0010-8000-00aa00389b71</p>
<p>KSDATAFORMAT_SUBTYPE_IEC61937_DST</p></td>
<td align="left"><p>Direct Stream Transport (DST)</p></td>
</tr>
</tbody>
</table>

 

The following code example shows how an audio miniport driver defines and initializes a [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure for use with an HDMI sink that has a fully functional Dolby Digital Plus decoder. A sink of this type supports transfer rates of 44.1 and 48 KHz.

For a sampling rate of 48 KHz, an audio miniport driver uses the following code to define and initialize a [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure. This code shows the data ranges that the audio miniport driver exposes:

```cpp
//Define and initialize KSDATARANGE_AUDIO structure
// for use with a sample rate of 48 KHz.
KSDATARANGE_AUDIO drDDPlus48;
drDDPlus48.DataRange.FormatSize = sizeof(KSDATARANGE_AUDIO);
drDDPlus48.DataRange.Flags = 0; // Ignored.
drDDPlus48.DataRange.SampleSize = 0; // Ignored.
drDDPlus48.DataRange.Reserved = 0;
drDDPlus48.DataRange.MajorFormat = KSDATAFORMAT_TYPE_AUDIO;
drDDPlus48.DataRange.SubFormat = KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS;
drDDPlus48.DataRange.Specifier = KSDATAFORMAT_SPECIFIER_WAVEFORMATEX;
drDDPlus48.MaximumChannels = 2
drDDPlus48.MinimumBitsPerSample = 16; // All encoded data is transmitted at
drDDPlus48.MaximumBitsPerSample = 16; // 16 bits over IEC 60958.
drDDPlus48.MinimumSampleFrequency = 192000; // 48 KHz * 4.
drDDPlus48.MaximumSampleFrequency = 192000;
```

For a sampling rate of 44.1 KHz, an audio miniport driver uses the following code to define and initialize a [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure:

```cpp
//Define and initialize KSDATARANGE_AUDIO structure
// for use with a sample rate of 41.1 KHz.
KSDATARANGE_AUDIO drDDPlus44;
drDDPlus44.DataRange.FormatSize = sizeof(KSDATARANGE_AUDIO);
drDDPlus44.DataRange.Flags = 0 // Ignored.
drDDPlus44.DataRange.SampleSize = 0 // Ignored.
drDDPlus44.DataRange.Reserved = 0; 
drDDPlus44.DataRange.MajorFormat = KSDATAFORMAT_TYPE_AUDIO;
drDDPlus44.DataRange.SubFormat = KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS;
drDDPlus44.DataRange.Specifier = KSDATAFORMAT_SPECIFIER_WAVEFORMATEX;
drDDPlus44.MaximumChannels = 2
drDDPlus44.MinimumBitsPerSample = 16; // All encoded data is transmitted at
drDDPlus44.MaximumBitsPerSample = 16; // 16 bits over IEC 60958.
drDDPlus44.MinimumSampleFrequency = 176400; // 44.1 KHz * 4
drDDPlus44.MaximumSampleFrequency = 176400;
```

 

 




