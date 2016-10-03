---
title: Hardware Codec Support in AVStream
author: windows-driver-content
description: Hardware Codec Support in AVStream
MS-HAID:
- 'shed\_dg\_c3a6f179-ecb1-4d51-96c8-05ada4f0ba3f.xml'
- 'stream.hardware\_codec\_support\_in\_avstream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 19ffd906-e198-4ede-b132-45e53431603c
keywords: ["AVStream WDK , hardware codec support", "hardware codec support WDK AVStream", "AVStream hardware codec support WDK"]
---

# Hardware Codec Support in AVStream


In Windows 7 and later versions of Windows, AVStream-based media devices can be presented as Media Foundation Transform (MFT) filters to user-mode applications.

This feature enables the hardware vendor to present hardware-based decoders, encoders, and video processors as user-mode Media Foundation Transforms (MFTs).

Hardware-based encoding and decoding greatly improves the user experience.

To enable hardware codec support in AVStream, the vendor provides an AVStream-based minidriver that exposes decoding, encoding, and video processing, each as a separate AVStream filter. The operating system then creates a user-mode MFT that corresponds to each AVStream filter. User-mode applications can then submit transcoding requests to the MFTs by using IMFTransform interface functions that are defined in the [Media Foundation SDK](http://go.microsoft.com/fwlink/p/?linkid=144771).

This section describes the changes that are required for AVStream drivers to use this feature.

This section contains the following topics:

[Getting Started with Hardware Codec Support in AVStream](getting-started-with-hardware-codec-support-in-avstream.md)

[Handling Data Type Negotiation in AVStream Codecs](handling-data-type-negotiation-in-avstream-codecs.md)

[Using Hardware Mediums in AVStream Codecs](using-hardware-mediums-in-avstream-codecs.md)

[Specifying Allocator Framing in AVStream Codecs](specifying-allocator-framing-in-avstream-codecs.md)

[Describing Extended Sample Information in AVStream Codecs](describing-extended-sample-information-in-avstream-codecs.md)

[Supporting Dynamic Format Changes in AVStream Codecs](supporting-dynamic-format-changes-in-avstream-codecs.md)

[Handling End of Stream in AVStream Codecs](handling-end-of-stream-in-avstream-codecs.md)

[Resetting State in AVStream Codecs](resetting-state-in-avstream-codecs.md)

[Handling Stride in AVStream Codecs](handling-stride-in-avstream-codecs.md)

[Installing an AVStream-based Hardware Codec Driver](installing-an-avstream-based-hardware-codec-driver.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Hardware%20Codec%20Support%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


