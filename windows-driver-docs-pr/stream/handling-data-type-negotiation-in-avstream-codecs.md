---
title: Handling Data Type Negotiation in AVStream Codecs
description: Handling Data Type Negotiation in AVStream Codecs
keywords:
- hardware codec support WDK AVStream , data type negotiation
- data type negotiation WDK AVStream
- AVStream hardware codec support WDK , handling data type negotiation
ms.date: 04/20/2017
---

# Handling Data Type Negotiation in AVStream Codecs

When a device is initialized, the system-supplied Device Proxy (Devproxy) module parses the filter descriptors that are provided by the driver. Additionally, Devproxy exposes the driver-supported data ranges on the input and output pins of the corresponding MFT (Media Foundation Transform).

When streaming begins, the MF pipeline and user-mode applications use these ranges to perform data type negotiation with the driver.

The following interactions occur during a data type negotiation:

1. Devproxy retrieves the data ranges that are supplied by the minidriver in each pin descriptor of the hardware codec filters.

1. Devproxy issues a data intersection request to the driver.

1. Devproxy exposes fully formed types to MF.

1. MF Topology Builder (the MF equivalent of DirectShow graph builder) constructs streaming topology.

1. After the MF Topology builder finalizes a data type for a Devproxy input/output pin, it sets the data type on the pin by calling the minidriver's [*AVStrMiniPinSetDataFormat*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdataformat) callback function. If the KS pin does not exist, Devproxy calls [**KsCreatePin**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatepin).

To enable successful data type negotiation, the minidriver must follow these steps:

1. Supply a list of supported data ranges in the **DataRanges** member of [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) for each exposed pin included in the hardware codec filters. For example:

    ```cpp
    const PKSDATARANGE VideoDecoderInputPinDataRanges[8] = {
        (PKSDATARANGE)&H264DataFormat,
        (PKSDATARANGE)&VC_1DataFormat,
        (PKSDATARANGE)&VC_1DataFormatVIH2,
        (PKSDATARANGE)&WMV9DataFormat,
        (PKSDATARANGE)&WMV9DataFormatVIH2,
        (PKSDATARANGE)&DX50DataFormat,
        (PKSDATARANGE)&DX50DataFormatVIH2,
        (PKSDATARANGE)&MPEG2DataFormat
    };
    ```

    In this case, the specified ranges are of wrapper types such as [**KS\_DATARANGE\_MPEG2\_VIDEO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_mpeg2_video), [**KS\_DATARANGE\_VIDEO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_video), and [**KS\_DATARANGE\_VIDEO2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_video2). In the code example listed previously, each range is typecast to [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)).

    The last member of the wrapper structures is known as the format block structure, for example, KS\_DATARANGE\_MPEG2\_VIDEO.**VideoInfoHeader**.

    A driver that supports continuous data ranges should specify the maximum values in the format block structure. A driver that supports discrete data ranges should specify an array that contains the discrete values in the format block structures.

    If a driver that claims to support a given format later fails a set format request to that format, performance may be reduced. Only list formats for which you guarantee support.

1. Drivers should allow a media type to be set on a pin while in KSSTATE\_STOP/KSSTATE\_RUN. No action is required here other than to make sure that the driver does not disallow this.

1. The driver should supply an intersect handler in [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex).**IntersectHandler** for each pin.

1. The minidriver should supply a handler for the [**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](./ksproperty-connection-proposedataformat.md) property.

1. If the output media type is set, an encoder should report possible input types (by using a pin descriptor) based on the specified output media type. If an output media type is not set, encoders should not report any input media type.

1. If the input media type is set, decoders should report possible output types based on the specified input media type.

1. If the input media type is set, Video Processors should report their output types based on the specified input media type.

1. The driver should support the [ICodecAPI](/previous-versions/ms784893(v=vs.85)) interface. User-mode components can then obtain codec configuration information by using this user-mode interface.

1. During setup of an encoder, first the ICodecAPI properties are set, followed by the output media type. Following this, the encoder should only provide input types that it can support with the current configuration.

1. **ICodecAPI** properties and Codec API media type properties overlap in some areas, for example, profile and level. In these cases, Codec API properties that are related to media type override ICodecAPI properties. After the media type is set, the minidriver should not allow modification of these overlapping properties.

1. During setup of a decoder, the input type is set first. Following this, the decoder should provide only output types that it can support with its current input type.

1. The expected input to an encoder should be 4:2:0 and at least NV12 interlace/progressive. The expected output is a compressed elementary stream in format MPEG2 PS / TS or H.264 Annex B.

1. The expected input to a decoder is an elementary stream. The expected output is the unscaled version of the source stream as uncompressed NV12.

1. Pins on an AVStream driver should have states that are independent of one another. This means an input pin can transition from the **KSSTATE\_STOP** up to the **KSSTATE\_RUN** while the output pin remains at the **KSSTATE\_STOP** state.

1. When the minidriver receives property GET requests with variable data buffer sizes, the minidriver should interpret a **NULL** buffer as a query for size of the buffer required. In this case, the driver should specify the required length in the Irp-&gt;IoStatus.Information field and return STATUS\_BUFFER\_OVERFLOW. In addition, the minidriver should set the return code to be a warning and not an error. For example, follow this guidance with data intersection handlers.
