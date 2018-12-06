---
title: Hardware Codec Support in AVStream
description: Hardware Codec Support in AVStream
ms.assetid: 19ffd906-e198-4ede-b132-45e53431603c
keywords:
- AVStream WDK , hardware codec support
- hardware codec support WDK AVStream
- AVStream hardware codec support WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




