---
title: AV/C Streaming Format GUIDs
description: AV/C Streaming Format GUIDs
ms.date: 07/26/2021
---

# AV/C Streaming Format GUIDs

Like any kernel streaming driver, an AV/C Streaming subunit driver specifies the range of data formats that it supports for each pin by using format GUIDs. A kernel streaming application then uses these format GUIDs to perform a data range intersection for a particular data format. The result is a filled-in [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structure. Data intersection is described further in [Data Range Intersections in AVStream](./data-range-intersections-in-avstream.md).

A KSDATAFORMAT structure specifies GUIDs for its major format, format subtype, and specifier. The specifier designates the extended-data structure that follows the KSDATAFORMAT structure in memory. For example, suppose that a data format has a major format of KSDATAFORMAT_TYPE_INTERLEAVED, a format subtype of KSDATAFORMAT_SUBTYPE_DVSD, and a specifier of KSDATAFORMAT_SPECIFIER_DVINFO. In this case, the extended-data structure is the [**DVINFO**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_dvinfo) structure.

The *avcstrm.h* header file defines the following streaming format GUIDs:

| GUID | Description |
|--|--|
| KSDATAFORMAT_TYPE_INTERLEAVED | Designates an interleaved audio and video signal. Any video stream that contains audio should specify this GUID as the stream's type. |
| KSDATAFORMAT_TYPE_MPEG2_TRANSPORT_STRIDE | Designates an MPEG2 stream type that deviates from the normal 188-byte MPEG2 packet size. The KSDATAFORMAT_TYPE_MPEG2_TRANSPORT_STRIDE type is used with streams that conform to the IEC 61883-4 specification. These streams use the [**MPEG2_TRANSPORT_STRIDE**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_mpeg2_transport_stride) structure that allows for the stream to describe the format that is different than the typical 188 byte packet. For example, the dwOffset member of the MPEG2_TRANSPORT_STRIDE would be set to 4, the dwPacketLength member to 188, and the dwStride member to 192. |
| KSDATAFORMAT_SUBTYPE_DVSD | Designates an IEC 61883-2 standard-definition 25-Mbps DV signal that uses a 4:1:1 sampling structure for NTSC signals or that uses a 4:2:0 sampling structure for PAL signals. This format subtype uses the DVINFO structure as the data format's extended-data structure. |
| KSDATAFORMAT_SUBTYPE_DVSL | Designates an IEC 61883-3 long-play 12.5-Mbps DVSD signal, which has the same number of lines as the NTSC or PAL signal but implements a higher compression ratio. This format subtype uses the DVINFO structure as the data format's extended-data structure. |
| KSDATAFORMAT_SUBTYPE_DVHD | Designates an IEC 61883-3 high-definition DV signal, such as a 1125-line 60-Hz NTSC signal or a 1250-line 50-Hz PAL signal. This format subtype is not currently supported. |
| KSDATAFORMAT_SUBTYPE_DV25 | Designates an SMPTE 314M 25-Mbps DVCPRO video signal that uses a 4:1:1 sampling structure for both NTSC and PAL signals. This format subtype uses the DVINFO structure as the data format's extended-data structure. |
| KSDATAFORMAT_SUBTYPE_DV50 | Designates an SMPTE 314M 50-Mbps DVCPRO50 video signal that uses a 4:2:2 sample structure for both NTSC and PAL signals. This format subtype uses the DVINFO structure as the data format's extended-data structure. |
| KSDATAFORMAT_SUBTYPE_DVH1 | Designates an SMPTE 370M 100-Mbps high-definition DV video signal, such as a 720p (progressive) or a 1080i (interlaced) signal. This format subtype uses the DVINFO structure as the data format's extended-data structure. |
| KSDATAFORMAT_SPECIFIER_DVINFO | Designates the DVINFO structure as the extended-data structure following the KSDATAFORMAT in memory. |
| KSDATAFORMAT_SPECIFIER_DV_AVC | Designates the DVINFO and AVCCONNECTINFO structures as the extended-data structures following the KSDATAFORMAT in memory. |
| KSDATAFORMAT_SPECIFIER_AVC | Designates the AVCCONNECTINFO structure as the extended-data structure following the KSDATAFORMAT in memory. This specifier may also be used with an MPEG2TS format, depending on the format's subtype. |
| KSDATAFORMAT_SPECIFIER_61883_4 | Designates an MPEG2-TS format that follows the IEC 61883-4 protocol. This specifier does not use any extended data structure to follow the KSDATAFORMAT in memory. |

## Comments

*Avcstrm.sys* and *Msdv.sys* support the KSDATAFORMAT_SUBTYPE_DV25, KSDATAFORMAT_SUBTYPE_DV50 and KSDATAFORMAT_SUBTYPE_DVH1 format subtypes in Windows Vista, Windows Server 2003 with Service Pack 1 (SP1), and Windows XP with Service Pack 2 (SP2) operating systems.

Note that the KSDATAFORMAT_SUBTYPE_DVSD and KSDATAFORMAT_SUBTYPE_DV25 format subtypes are compatible using 4:1:1 sampling for NTSC. However, the KSDATAFORMAT_SUBTYPE_DV25 for the PAL format uses 4:1:1 sampling but the KSDATAFORMAT_SUBTYPE_DVSD for the PAL format uses 4:2:0 sampling, thus the distinction between DVSD and DV25.

A subunit driver indicates the frame size (sample size) by the combination of its format subtype and its extended-data structure. For example, the combination of the KSDATAFORMAT_SUBTYPE_DVSD format subtype and the NTSC bit set in the DVINFO extended-data structure indicates a DV frame size of 120 KB.

The [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structure contains a **FormatSize** member that is used to validate the extended-data structure size. That is, in valid extended-data structure sizes FormatSize equals sizeof(KSDATAFORMAT) + sizeof(extended-data structure(s)).

The following table describes the KS data format specifier GUIDs and their corresponding extended-data structures.

| KS data format specifier | Extended-data structure |
|--|--|
| KSDATAFORMAT_SPECIFIER_DVINFO | [**DVINFO**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_dvinfo) |
| KSDATAFORMAT_SPECIFIER_DV_AVC | **DVINFO** and [**AVCCONNECTINFO**](/windows-hardware/drivers/ddi/avc/ns-avc-_avcconnectinfo) |
| KSDATAFORMAT_SPECIFIER_AVC | **AVCCONNECTINFO** |
| KSDATAFORMAT_SPECIFIER_61883_4 | No extended data structure is used |

Microsoft Corporation introduced the *msdv.sys* subunit driver with Windows 98 SE. This driver supports most MiniDV camcorders in both camera mode and VTR (Video Tape Recorder) mode.

Microsoft Corporation introduced the *mstape.sys* tape subunit driver with Windows Me. This driver supports D-VHS tape decks and MPEG camcorder devices.

> [!NOTE]
> Microsoft does not supply a codec to support DVCPro format decoding.
