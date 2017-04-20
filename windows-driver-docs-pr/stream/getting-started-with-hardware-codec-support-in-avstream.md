---
title: Getting Started with Hardware Codec Support in AVStream
author: windows-driver-content
description: Getting Started with Hardware Codec Support in AVStream
ms.assetid: f8335285-e74f-4600-aee9-7e2881cb0764
keywords:
- hardware codec support WDK AVStream , using
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Getting Started with Hardware Codec Support in AVStream


Starting in Windows 7, [Windows Media Foundation](http://go.microsoft.com/fwlink/p/?linkid=155069) represents AVStream-based media components as user-mode Media Foundation Transforms (MFTs).

By using this feature, vendors can present hardware-based decoders, encoders, and video processors as MFTs that can in turn be manipulated at the application level.

The AVStream model remains unchanged in Windows 7 and requires only a few additions to the minidriver to enable this functionality.

The transcoding topology is shown in the following diagram:

![diagram illustrating transcoding topology](images/hw-transcoding.png)

For best performance, the media processing that is shown in the bottom row of the diagram should occur in dedicated hardware. In this scenario, dedicated transcode hardware is known as Secured Hardware Encoder Decoder (SHED). SHED can be packaged either as a plug-in module for the motherboard or as an integrated feature on the display adapter.

Windows 7 still supports software-based transcoding. However, because the system performs the transcoding work on dedicated hardware instead of the CPU, a SHED-based solution improves the user experience significantly compared with a software-based solution.

As shown in the previous diagram, user-mode clients can access the user-mode transforms by using the IMFTransform interface that is exposed on each MFT. IMFTransform is available in Vista and later versions of Windows, but the mechanism to expose hardware-based media processing to user-mode applications is only available starting in Windows 7.

The system-supplied Device Proxy, or Devproxy, module serves the same role as KSProxy in the DirectShow streaming model. Devproxy brokers communication between *Ks.sys* in kernel-mode and MFT components in user-mode.

The resulting wrapped hardware media processing function is called a Device Proxy MFT. To take advantage of this mechanism, an AVStream minidriver should do the following:

-   Expose transform functions as individual KS filters that are part of the AVStream minidriver. For example, if the device has decode, encode, and video processing features, these functions should be represented as three distinct KS filters.
    -   **Encoder**: used to convert from an uncompressed format to a compressed format.
    -   **Decoder**: used to convert from a compressed format to an uncompressed format, which must include NV12.
    -   **Video Processor**: used to perform scaling, interlacing/de-interlacing, and format conversion. Do not include video processing support in the decoder or encoder filter.

        Microsoft strongly recommends that vendors provide hardware-based scaling support. However, if you choose not to provide hardware-based scaling support, you can use the system-supplied video processing MFT to perform scaling operations at a reduced level of performance. If you do not provide hardware-based scaling support, the Media Foundation topology builder automatically inserts the system-supplied scaling MFT into the topology.

-   Register its media processing KS filters under one of the following KS categories, available in Windows 7 and later versions of Windows:

    -   [**KSMFT\_CATEGORY\_VIDEO\_DECODER**](https://msdn.microsoft.com/library/windows/hardware/ff548602)
    -   [**KSMFT\_CATEGORY\_VIDEO\_ENCODER**](https://msdn.microsoft.com/library/windows/hardware/ff548611)
    -   [**KSMFT\_CATEGORY\_VIDEO\_PROCESSOR**](https://msdn.microsoft.com/library/windows/hardware/ff548613)
    -   [**KSMFT\_CATEGORY\_AUDIO\_DECODER**](https://msdn.microsoft.com/library/windows/hardware/ff548572)
    -   [**KSMFT\_CATEGORY\_AUDIO\_ENCODER**](https://msdn.microsoft.com/library/windows/hardware/ff548584)

    In addition, the following categories are also defined for use in other transcoding scenarios:

    -   [**KSMFT\_CATEGORY\_VIDEO\_EFFECT**](https://msdn.microsoft.com/library/windows/hardware/ff548607)
    -   [**KSMFT\_CATEGORY\_MULTIPLEXER**](https://msdn.microsoft.com/library/windows/hardware/ff548596)
    -   [**KSMFT\_CATEGORY\_DEMULTIPLEXER**](https://msdn.microsoft.com/library/windows/hardware/ff548594)
    -   [**KSMFT\_CATEGORY\_AUDIO\_EFFECT**](https://msdn.microsoft.com/library/windows/hardware/ff548578)
    -   [**KSMFT\_CATEGORY\_OTHER**](https://msdn.microsoft.com/library/windows/hardware/ff548601)
-   Media foundation applications can then use the [MFTEnumEx](http://go.microsoft.com/fwlink/p/?linkid=155058) function to enumerate the devices that are registered as MFTs by using the categories mentioned previously.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Getting%20Started%20with%20Hardware%20Codec%20Support%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


