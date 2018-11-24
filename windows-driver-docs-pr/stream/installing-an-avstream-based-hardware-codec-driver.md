---
title: Installing an AVStream-based Hardware Codec Driver
description: Installing an AVStream-based Hardware Codec Driver
ms.assetid: 7b3bbff7-c8e7-47ea-a455-66f01a552e3b
keywords:
- hardware codec support WDK AVStream , installing a driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing an AVStream-based Hardware Codec Driver


An AVStream-based driver that has hardware codec support should supply an INF file that resembles that of other AVStream minidrivers. However, there are two specific entries that a hardware vendor can include to facilitate a particular driver behavior:

1.  To specify that your decoder should be used only in a transcode topology and not in a playback topology, add the following to the decoder's AddReg section in the driver's INF file:

    ```INF
    [shedVideoDecoder.Reader.AddReg]
    HKR,,CLSID,,%Proxy.CLSID%
    HKR,,FriendlyName,,%shedVideoDecoder.Reader.FriendlyName%
    HKR,,MFTMerit,0x00010001,7
    HKR,Capabilities,"{111EA8CD-B62A-4bdb-89F6-67FFCDC2458B}",0x00010001,1
    ```

    The previous code example excludes the decoder in playback topology. This might be a requirement for hardware vendors who have optimized their decoder to work with their encoder.

2.  To enable a decoder, encoder, or video processor to be selected by Windows Media Player (WMP) and Windows 7 transcode functionality in the shell, the following registry keys should be set to 1:

    ```console
    HKLM\Software\Microsoft\WindowsMediaFoundation\HardwareMFT\EnableDecoders
    HKLM\Software\Microsoft\WindowsMediaFoundation\HardwareMFT\EnableEncoders
    HKLM\Software\Microsoft\WindowsMediaFoundation\HardwareMFT\EnableVideoProcessors
    ```
