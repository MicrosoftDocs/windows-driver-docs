---
title: AV/C Streaming Format GUIDs
description: AV/C Streaming Format GUIDs
ms.assetid: 60f1fd59-e760-4be4-8990-e49628b76d15
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AV/C Streaming Format GUIDs


## <span id="ddk_av_c_streaming_format_guids_ks"></span><span id="DDK_AV_C_STREAMING_FORMAT_GUIDS_KS"></span>


Like any kernel streaming driver, an AV/C Streaming subunit driver specifies the range of data formats that it supports for each pin by using format GUIDs. A kernel streaming application then uses these format GUIDs to perform a data range intersection for a particular data format. The result is a filled-in [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure. Data intersection is described further in [Data Range Intersections in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff558680).

A KSDATAFORMAT structure specifies GUIDs for its major format, format subtype, and specifier. The specifier designates the extended-data structure that follows the KSDATAFORMAT structure in memory. For example, suppose that a data format has a major format of KSDATAFORMAT\_TYPE\_INTERLEAVED, a format subtype of KSDATAFORMAT\_SUBTYPE\_DVSD, and a specifier of KSDATAFORMAT\_SPECIFIER\_DVINFO. In this case, the extended-data structure is the [**DVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff559517) structure.

The *avcstrm.h* header file defines the following streaming format GUIDs:

<span id="KSDATAFORMAT_TYPE_INTERLEAVED"></span><span id="ksdataformat_type_interleaved"></span>KSDATAFORMAT\_TYPE\_INTERLEAVED  
Designates an interleaved audio and video signal. Any video stream that contains audio should specify this GUID as the stream's type.

<span id="KSDATAFORMAT_TYPE_MPEG2_TRANSPORT_STRIDE"></span><span id="ksdataformat_type_mpeg2_transport_stride"></span>KSDATAFORMAT\_TYPE\_MPEG2\_TRANSPORT\_STRIDE  
Designates an MPEG2 stream type that deviates from the normal 188-byte MPEG2 packet size. The KSDATAFORMAT\_TYPE\_MPEG2\_TRANSPORT\_STRIDE type is used with streams that conform to the IEC 61883-4 specification. These streams use the [**MPEG2\_TRANSPORT\_STRIDE**](https://msdn.microsoft.com/library/windows/hardware/ff567742) structure that allows for the stream to describe the format that is different than the typical 188 byte packet. For example, the dwOffset member of the MPEG2\_TRANSPORT\_STRIDE would be set to 4, the dwPacketLength member to 188, and the dwStride member to 192.

<span id="KSDATAFORMAT_SUBTYPE_DVSD"></span><span id="ksdataformat_subtype_dvsd"></span>KSDATAFORMAT\_SUBTYPE\_DVSD  
Designates an IEC 61883-2 standard-definition 25-Mbps DV signal that uses a 4:1:1 sampling structure for NTSC signals or that uses a 4:2:0 sampling structure for PAL signals. This format subtype uses the DVINFO structure as the data format's extended-data structure.

<span id="KSDATAFORMAT_SUBTYPE_DVSL"></span><span id="ksdataformat_subtype_dvsl"></span>KSDATAFORMAT\_SUBTYPE\_DVSL  
Designates an IEC 61883-3 long-play 12.5-Mbps DVSD signal, which has the same number of lines as the NTSC or PAL signal but implements a higher compression ratio. This format subtype uses the DVINFO structure as the data format's extended-data structure.

<span id="KSDATAFORMAT_SUBTYPE_DVHD"></span><span id="ksdataformat_subtype_dvhd"></span>KSDATAFORMAT\_SUBTYPE\_DVHD  
Designates an IEC 61883-3 high-definition DV signal, such as a 1125-line 60-Hz NTSC signal or a 1250-line 50-Hz PAL signal. This format subtype is not currently supported.

<span id="KSDATAFORMAT_SUBTYPE_DV25"></span><span id="ksdataformat_subtype_dv25"></span>KSDATAFORMAT\_SUBTYPE\_DV25  
Designates an SMPTE 314M 25-Mbps DVCPRO video signal that uses a 4:1:1 sampling structure for both NTSC and PAL signals. This format subtype uses the DVINFO structure as the data format's extended-data structure.

<span id="KSDATAFORMAT_SUBTYPE_DV50"></span><span id="ksdataformat_subtype_dv50"></span>KSDATAFORMAT\_SUBTYPE\_DV50  
Designates an SMPTE 314M 50-Mbps DVCPRO50 video signal that uses a 4:2:2 sample structure for both NTSC and PAL signals. This format subtype uses the DVINFO structure as the data format's extended-data structure.

<span id="KSDATAFORMAT_SUBTYPE_DVH1"></span><span id="ksdataformat_subtype_dvh1"></span>KSDATAFORMAT\_SUBTYPE\_DVH1  
Designates an SMPTE 370M 100-Mbps high-definition DV video signal, such as a 720p (progressive) or a 1080i (interlaced) signal. This format subtype uses the DVINFO structure as the data format's extended-data structure.

<span id="KSDATAFORMAT_SPECIFIER_DVINFO"></span><span id="ksdataformat_specifier_dvinfo"></span>KSDATAFORMAT\_SPECIFIER\_DVINFO  
Designates the DVINFO structure as the extended-data structure following the KSDATAFORMAT in memory.

<span id="KSDATAFORMAT_SPECIFIER_DV_AVC"></span><span id="ksdataformat_specifier_dv_avc"></span>KSDATAFORMAT\_SPECIFIER\_DV\_AVC  
Designates the DVINFO and AVCCONNECTINFO structures as the extended-data structures following the KSDATAFORMAT in memory.

<span id="KSDATAFORMAT_SPECIFIER_AVC"></span><span id="ksdataformat_specifier_avc"></span>KSDATAFORMAT\_SPECIFIER\_AVC  
Designates the AVCCONNECTINFO structure as the extended-data structure following the KSDATAFORMAT in memory. This specifier may also be used with an MPEG2TS format, depending on the format's subtype.

<span id="KSDATAFORMAT_SPECIFIER_61883_4"></span><span id="ksdataformat_specifier_61883_4"></span>KSDATAFORMAT\_SPECIFIER\_61883\_4  
Designates an MPEG2-TS format that follows the IEC 61883-4 protocol. This specifier does not use any extended data structure to follow the KSDATAFORMAT in memory.

### Comments

*Avcstrm.sys* and *Msdv.sys* support the KSDATAFORMAT\_SUBTYPE\_DV25, KSDATAFORMAT\_SUBTYPE\_DV50 and KSDATAFORMAT\_SUBTYPE\_DVH1 format subtypes in Windows Vista, Windows Server 2003 with Service Pack 1 (SP1), and Windows XP with Service Pack 2 (SP2) operating systems.

Note that the KSDATAFORMAT\_SUBTYPE\_DVSD and KSDATAFORMAT\_SUBTYPE\_DV25 format subtypes are compatible using 4:1:1 sampling for NTSC. However, the KSDATAFORMAT\_SUBTYPE\_DV25 for the PAL format uses 4:1:1 sampling but the KSDATAFORMAT\_SUBTYPE\_DVSD for the PAL format uses 4:2:0 sampling, thus the distinction between DVSD and DV25.

A subunit driver indicates the frame size (sample size) by the combination of its format subtype and its extended-data structure. For example, the combination of the KSDATAFORMAT\_SUBTYPE\_DVSD format subtype and the NTSC bit set in the DVINFO extended-data structure indicates a DV frame size of 120 KB.

The [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure contains a **FormatSize** member that is used to validate the extended-data structure size. That is, in valid extended-data structure sizes FormatSize equals sizeof(KSDATAFORMAT) + sizeof(extended-data structure(s)).

The following table describes the KS data format specifier GUIDs and their corresponding extended-data structures.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KS data format specifier</th>
<th>Extended-data structure(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KSDATAFORMAT_SPECIFIER_DVINFO</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559517" data-raw-source="[&lt;strong&gt;DVINFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559517)"><strong>DVINFO</strong></a></p></td>
</tr>
<tr class="even">
<td><p>KSDATAFORMAT_SPECIFIER_DV_AVC</p></td>
<td><p>DVINFO and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554101" data-raw-source="[&lt;strong&gt;AVCCONNECTINFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554101)"><strong>AVCCONNECTINFO</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>KSDATAFORMAT_SPECIFIER_AVC</p></td>
<td><p>AVCCONNECTINFO</p></td>
</tr>
<tr class="even">
<td><p>KSDATAFORMAT_SPECIFIER_61883_4</p></td>
<td><p>No extended data structure is used</p></td>
</tr>
</tbody>
</table>

 

Microsoft Corporation introduced the *msdv.sys* subunit driver with Windows 98 SE. This driver supports most MiniDV camcorders in both camera mode and VTR (Video Tape Recorder) mode.

Microsoft Corporation introduced the *mstape.sys* tape subunit driver with Windows Me. This driver supports D-VHS tape decks and MPEG camcorder devices.

**Note** Microsoft does not supply a codec to support DVCPro format decoding.

 

 





