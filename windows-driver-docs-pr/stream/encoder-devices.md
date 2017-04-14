---
title: Encoder Devices
author: windows-driver-content
description: Encoder Devices
ms.assetid: 156b1d6d-c6f6-4ab3-a91e-3124351c6ae5
keywords: ["encoder devices WDK AVStream", "AVStream WDK , encoder devices", "uncompressed data streams WDK AVStream", "encoded streams WDK AVStream", "audio encoder devices WDK AVStream", "video encoder devices WDK AVStream", "software-based encoders WDK AVStream", "hardware-based encoders WDK AVStream", "integrated encoders WDK AVStream", "standalone encoders WDK AVStream"]
---

# Encoder Devices


## <a href="" id="ddk-encoder-minidrivers-ksg"></a>


Encoders are devices that receive as input an uncompressed data stream (video and/or audio), encode the stream into a specific format, such as MPEG2, and then output an encoded stream. Encoder devices may be a part of another device, such as a combination TV tuner/capture adapter, or they may be separate. For example, an integrated encoder receives a data stream from a capture device such as an analog TV tuner/decoder and then it produces an encoded stream. A standalone encoder may receive input data from an uncompressed file, process the data, and then output encoded data.

Microsoft provides support for hardware-based audio/video encoder devices in DirectX 9.0 and later. The DirectX 9.0 redistributable is available for the following Microsoft Windows platforms:

-   Windows Media Center Edition 2004

-   Windows Server 2003

-   Windows XP Home and Professional

-   Windows 2000 Professional and Server

-   Windows Millennium Edition

-   Windows 98 Second Edition

To support audio/video encoder devices, you must implement support for Microsoft-defined encoder properties in a kernel streaming filter minidriver. Support may be added to an existing stream class or AVStream minidriver by implementing the encoder properties. Alternatively, if you are writing a new minidriver (either for a standalone encoder or an integrated one), Microsoft recommends following the AVStream architecture because the stream class is obsolete and no longer supported. You may use the [AVStream Simulated Hardware Sample Driver (Avshws)](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the MSDN Code Gallery as a starting point. The Avshws driver is a pin-centric AVStream example that implements support for DMA transfers.

**Note**   If you are writing a software-implemented encoder, then you should not write it as a kernel streaming filter. Instead, such filters should be written as Microsoft DirectShow filters or DirectX Media Objects. See the DirectShow SDK topic "Encoder API" for more information about software-based encoders.

 

Clients access encoder functionality through the [**ICodecAPI**](https://msdn.microsoft.com/library/windows/desktop/dd311953) COM interface. You specify which interface KsProxy exposes in the driver's INF file depending on the properties your minidriver implements. See [Encoder Implementation and Support](encoder-implementation-and-support.md) for information about the Microsoft-defined kernel streaming properties and event. See [Encoder Code Examples](encoder-code-examples.md) for examples of how to implement them. See [Encoder Installation and Registration](encoder-installation-and-registration.md) for information about how to install an encoder filter, including how to specify which COM interface KsProxy should expose.

Encoder devices must conform to the Streaming Media and Broadcast requirements as described in the Windows Certification Program in addition to the generic logo requirements that cover all devices.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Encoder%20Devices%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


