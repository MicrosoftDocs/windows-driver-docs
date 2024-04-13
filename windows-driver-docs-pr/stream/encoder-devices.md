---
title: Encoder Devices
description: Encoder devices
keywords:
- encoder devices WDK AVStream
- AVStream WDK , encoder devices
- uncompressed data streams WDK AVStream
- encoded streams WDK AVStream
- audio encoder devices WDK AVStream
- video encoder devices WDK AVStream
- software-based encoders WDK AVStream
- hardware-based encoders WDK AVStream
- integrated encoders WDK AVStream
- standalone encoders WDK AVStream
ms.date: 06/16/2020
---

# Encoder devices

Encoders are devices that receive as input an uncompressed data stream (video and/or audio), encode the stream into a specific format, such as MPEG2, and then output an encoded stream. Encoder devices may be a part of another device, such as a combination TV tuner/capture adapter, or they may be separate. For example, an integrated encoder receives a data stream from a capture device such as an analog TV tuner/decoder and then it produces an encoded stream. A standalone encoder may receive input data from an uncompressed file, process the data, and then output encoded data.

Microsoft provides support for hardware-based audio/video encoder devices in DirectX 9.0 and later.

To support audio/video encoder devices, you must implement support for Microsoft-defined encoder properties in a kernel streaming filter minidriver. Support may be added to an existing stream class or AVStream minidriver by implementing the encoder properties. Alternatively, if you are writing a new minidriver (either for a standalone encoder or an integrated one), Microsoft recommends following the AVStream architecture because the stream class is obsolete and no longer supported. You may use the [AVStream Simulated Hardware Sample Driver (Avshws)](/samples/microsoft/windows-driver-samples/avstream-simulated-hardware-sample-driver-avshws/) as a starting point. The Avshws driver is a pin-centric AVStream example that implements support for DMA transfers.

> [!NOTE]
> If you are writing a software-implemented encoder, then you should not write it as a kernel streaming filter. Instead, such filters should be written as Microsoft DirectShow filters or DirectX Media Objects. See the DirectShow SDK topic "Encoder API" for more information about software-based encoders.

Clients access encoder functionality through the [**ICodecAPI**](/previous-versions/ms784893(v=vs.85)) COM interface. You specify which interface KsProxy exposes in the driver's INF file depending on the properties your minidriver implements. See [Encoder Implementation and Support](encoder-implementation-and-support.md) for information about the Microsoft-defined kernel streaming properties and event. See [Encoder Code Examples](encoder-code-examples.md) for examples of how to implement them. See [Encoder Installation and Registration](encoder-installation-and-registration.md) for information about how to install an encoder filter, including how to specify which COM interface KsProxy should expose.

Encoder devices must conform to the Streaming Media and Broadcast requirements as described in the Windows Certification Program in addition to the generic logo requirements that cover all devices.
