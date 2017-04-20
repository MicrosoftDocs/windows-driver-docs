---
title: KS Data Formats and Data Ranges
author: windows-driver-content
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KS Data Formats and Data Ranges


## <a href="" id="ddk-ks-data-formats-and-data-ranges-ksg"></a>


KS pins specify data formats and ranges using the [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) and [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures. A data format specifies a single attribute of a data stream, for example an audio sampling size of 16 bits. A data range specifies multiple formats, for example an audio sampling range of 16-24 bits.

A minidriver includes an array of KSDATARANGE structures in each [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure that it provides. Microsoft-provided formats are enumerated in *ksmedia.h*.

A KSDATARANGE structure has the same members as a KSDATAFORMAT structure; however, the minidriver can specify wildcard values for the major format, subformat, and specifier members of KSDATARANGE.

Minidrivers use extended versions of these structures to define media-specific values. To read about how this works in audio and video capture, see: [Audio Data Formats and Data Ranges](https://msdn.microsoft.com/library/windows/hardware/ff536189) and [Selecting a Stream Format](selecting-a-stream-format.md).

Clients use the following properties to query data format support of pins instantiated by a given pin factory on the filter:

-   [**KSPROPERTY\_PIN\_DATARANGES**](https://msdn.microsoft.com/library/windows/hardware/ff565199). The KS filter reports all data ranges supported by pins instantiated by the pin factory. This includes every data format the pin can *ever* support.

-   [**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](https://msdn.microsoft.com/library/windows/hardware/ff565195). The KS filter reports all data ranges supported by pins instantiated by the pin factory, given the current internal driver state.

-   [**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff565206). Clients can use this property to query if pins instantiated by the pin factory support a specific data format.

-   [**KSPROPERTY\_PIN\_DATAINTERSECTION**](https://msdn.microsoft.com/library/windows/hardware/ff565198). Clients can use this property to offer a range of data formats.

Once a pin is instantiated, a user-mode client can determine the current data format or requests a change of data format through [KSPROPSETID\_Connection](https://msdn.microsoft.com/library/windows/hardware/ff566568) property requests. For example, the client uses [**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff565107) to determine if a pin supports a given data format. The client uses [**KSPROPERTY\_CONNECTION\_DATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff565103) to change the data format.

KS minidrivers and clients can dynamically negotiate data formats. When the data format of a stream changes, the minidriver specifies the KSSTREAM\_HEADER\_OPTIONSF\_DATADISCONTINUITY flag in the **OptionsFlags** member of a KSSTREAM\_HEADER. The minidriver passes the new data format itself, described in a [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure, in the corresponding data buffer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Data%20Formats%20and%20Data%20Ranges%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


