---
title: KS Data Formats and Data Ranges
description: KS Data Formats and Data Ranges
ms.assetid: 44b55a5a-ec58-4c1e-b780-e20829fe3edf
keywords:
- data formats WDK kernel streaming
- formats WDK kernel streaming
- ranges WDK kernel streaming
- data ranges WDK kernel streaming
- KS data formats WDK kernel streaming
- KS data ranges WDK kernel streaming
- KSDATARANGE
- KSDATAFORMAT
- kernel streaming WDK , data ranges
- KS WDK , data ranges
- kernel streaming WDK , data formats
- KS WDK , data formats
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Data Formats and Data Ranges





KS pins specify data formats and ranges using the [**KSDATAFORMAT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) and [**KSDATARANGE**](https://docs.microsoft.com/previous-versions/ff561658(v=vs.85)) structures. A data format specifies a single attribute of a data stream, for example an audio sampling size of 16 bits. A data range specifies multiple formats, for example an audio sampling range of 16-24 bits.

A minidriver includes an array of KSDATARANGE structures in each [**KSPIN\_DESCRIPTOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structure that it provides. Microsoft-provided formats are enumerated in *ksmedia.h*.

A KSDATARANGE structure has the same members as a KSDATAFORMAT structure; however, the minidriver can specify wildcard values for the major format, subformat, and specifier members of KSDATARANGE.

Minidrivers use extended versions of these structures to define media-specific values. To read about how this works in audio and video capture, see: [Audio Data Formats and Data Ranges](https://docs.microsoft.com/windows-hardware/drivers/audio/audio-data-formats-and-data-ranges) and [Selecting a Stream Format](selecting-a-stream-format.md).

Clients use the following properties to query data format support of pins instantiated by a given pin factory on the filter:

-   [**KSPROPERTY\_PIN\_DATARANGES**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-pin-dataranges). The KS filter reports all data ranges supported by pins instantiated by the pin factory. This includes every data format the pin can *ever* support.

-   [**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-pin-constraineddataranges). The KS filter reports all data ranges supported by pins instantiated by the pin factory, given the current internal driver state.

-   [**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-pin-proposedataformat). Clients can use this property to query if pins instantiated by the pin factory support a specific data format.

-   [**KSPROPERTY\_PIN\_DATAINTERSECTION**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-pin-dataintersection). Clients can use this property to offer a range of data formats.

Once a pin is instantiated, a user-mode client can determine the current data format or requests a change of data format through [KSPROPSETID\_Connection](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropsetid-connection) property requests. For example, the client uses [**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-connection-proposedataformat) to determine if a pin supports a given data format. The client uses [**KSPROPERTY\_CONNECTION\_DATAFORMAT**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-connection-dataformat) to change the data format.

KS minidrivers and clients can dynamically negotiate data formats. When the data format of a stream changes, the minidriver specifies the KSSTREAM\_HEADER\_OPTIONSF\_DATADISCONTINUITY flag in the **OptionsFlags** member of a KSSTREAM\_HEADER. The minidriver passes the new data format itself, described in a [**KSDATAFORMAT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structure, in the corresponding data buffer.

 

 




