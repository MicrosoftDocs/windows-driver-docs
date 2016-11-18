---
title: Handling Data Type Negotiation in AVStream Codecs
author: windows-driver-content
description: Handling Data Type Negotiation in AVStream Codecs
MS-HAID:
- 'shed\_dg\_c8c5541a-4ff6-48dd-b191-078dde404780.xml'
- 'stream.handling\_data\_type\_negotiation\_in\_avstream\_codecs'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b5212429-dbc8-4e9a-b5a9-2431f8a1eb2a
keywords: ["hardware codec support WDK AVStream , data type negotiation", "data type negotiation WDK AVStream", "AVStream hardware codec support WDK , handling data type negotiation"]
---

# Handling Data Type Negotiation in AVStream Codecs


When a device is initialized, the system-supplied Device Proxy (Devproxy) module parses the filter descriptors that are provided by the driver. Additionally, Devproxy exposes the driver-supported data ranges on the input and output pins of the corresponding MFT (Media Foundation Transform).

When streaming begins, the MF pipeline and user-mode applications use these ranges to perform data type negotiation with the driver.

The following interactions occur during a data type negotiation:

1.  Devproxy retrieves the data ranges that are supplied by the minidriver in each pin descriptor of the hardware codec filters.

2.  Devproxy issues a data intersection request to the driver.

3.  Devproxy exposes fully formed types to MF.

4.  MF Topology Builder (the MF equivalent of DirectShow graph builder) constructs streaming topology.

5.  After the MF Topology builder finalizes a data type for a Devproxy input/output pin, it sets the data type on the pin by calling the minidriver's [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355) callback function. If the KS pin does not exist, Devproxy calls [**KsCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff561652).

To enable successful data type negotiation, the minidriver must follow these steps:

1.  Supply a list of supported data ranges in the **DataRanges** member of [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) for each exposed pin included in the hardware codec filters. For example:

    ```
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

    In this case, the specified ranges are of wrapper types such as [**KS\_DATARANGE\_MPEG2\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/ff567362), [**KS\_DATARANGE\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/ff567628), and [**KS\_DATARANGE\_VIDEO2**](https://msdn.microsoft.com/library/windows/hardware/ff567629). In the code example listed previously, each range is typecast to [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658).

    The last member of the wrapper structures is known as the format block structure, for example, KS\_DATARANGE\_MPEG2\_VIDEO.**VideoInfoHeader**.

    A driver that supports continuous data ranges should specify the maximum values in the format block structure. A driver that supports discrete data ranges should specify an array that contains the discrete values in the format block structures.

    If a driver that claims to support a given format later fails a set format request to that format, performance may be reduced. Only list formats for which you guarantee support.

2.  Drivers should allow a media type to be set on a pin while in KSSTATE\_STOP/KSSTATE\_RUN. No action is required here other than to make sure that the driver does not disallow this.

3.  The driver should supply an intersect handler in [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534).**IntersectHandler** for each pin.

4.  The minidriver should supply a handler for the [**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff565107) property.

5.  If the output media type is set, an encoder should report possible input types (by using a pin descriptor) based on the specified output media type. If an output media type is not set, encoders should not report any input media type.

6.  If the input media type is set, decoders should report possible output types based on the specified input media type.

7.  If the input media type is set, Video Processors should report their output types based on the specified input media type.

8.  The driver should support the [ICodecAPI](http://go.microsoft.com/fwlink/p/?linkid=146348) interface. User-mode components can then obtain codec configuration information by using this user-mode interface.

9.  During setup of an encoder, first the ICodecAPI properties are set, followed by the output media type. Following this, the encoder should only provide input types that it can support with the current configuration.

10. **ICodecAPI** properties and Codec API media type properties overlap in some areas, for example, profile and level. In these cases, Codec API properties that are related to media type override ICodecAPI properties. After the media type is set, the minidriver should not allow modification of these overlapping properties.

11. During setup of a decoder, the input type is set first. Following this, the decoder should provide only output types that it can support with its current input type.

12. The expected input to an encoder should be 4:2:0 and at least NV12 interlace/progressive. The expected output is a compressed elementary stream in format MPEG2 PS / TS or H.264 Annex B.

13. The expected input to a decoder is an elementary stream. The expected output is the unscaled version of the source stream as uncompressed NV12.

14. Pins on an AVStream driver should have states that are independent of one another. This means an input pin can transition from the **KSSTATE\_STOP** up to the **KSSTATE\_RUN** while the output pin remains at the **KSSTATE\_STOP** state.

15. When the minidriver receives property GET requests with variable data buffer sizes, the minidriver should interpret a **NULL** buffer as a query for size of the buffer required. In this case, the driver should specify the required length in the Irp-&gt;IoStatus.Information field and return STATUS\_BUFFER\_OVERFLOW. In addition, the minidriver should set the return code to be a warning and not an error. For example, follow this guidance with data intersection handlers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Handling%20Data%20Type%20Negotiation%20in%20AVStream%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


