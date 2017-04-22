---
title: Installing an AVStream-based Hardware Codec Driver
author: windows-driver-content
description: Installing an AVStream-based Hardware Codec Driver
ms.assetid: 7b3bbff7-c8e7-47ea-a455-66f01a552e3b
keywords:
- hardware codec support WDK AVStream , installing a driver
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing an AVStream-based Hardware Codec Driver


An AVStream-based driver that has hardware codec support should supply an INF file that resembles that of other AVStream minidrivers. However, there are two specific entries that a hardware vendor can include to facilitate a particular driver behavior:

1.  To specify that your decoder should be used only in a transcode topology and not in a playback topology, add the following to the decoder's AddReg section in the driver's INF file:

    ```
    [shedVideoDecoder.Reader.AddReg]
    HKR,,CLSID,,%Proxy.CLSID%
    HKR,,FriendlyName,,%shedVideoDecoder.Reader.FriendlyName%
    HKR,,MFTMerit,0x00010001,7
    HKR,Capabilities,"{111EA8CD-B62A-4bdb-89F6-67FFCDC2458B}",0x00010001,1
    ```

    The previous code example excludes the decoder in playback topology. This might be a requirement for hardware vendors who have optimized their decoder to work with their encoder.

2.  To enable a decoder, encoder, or video processor to be selected by Windows Media Player (WMP) and Windows 7 transcode functionality in the shell, the following registry keys should be set to 1:
    ```
    HKLM\Software\Microsoft\WindowsMediaFoundation\HardwareMFT\EnableDecoders
    HKLM\Software\Microsoft\WindowsMediaFoundation\HardwareMFT\EnableEncoders
    HKLM\Software\Microsoft\WindowsMediaFoundation\HardwareMFT\EnableVideoProcessors
    ```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Installing%20an%20AVStream-based%20Hardware%20Codec%20Driver%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


