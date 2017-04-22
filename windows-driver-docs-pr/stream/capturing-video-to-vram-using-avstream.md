---
title: Capturing Video to VRAM using AVStream
author: windows-driver-content
description: Capturing Video to VRAM using AVStream
ms.assetid: c4ca4a67-83cb-4a89-bc84-e06b1dc67b66
keywords:
- AVStream WDK , VRAM capture
- VRAM capture WDK AVStream
- capturing video to VRAM WDK AVStream
- video capture to VRAM WDK AVStream
- audio capture to VRAM WDK AVStream
- data capture to VRAM WDK AVStream
- display minidrivers WDK VRAM capture
- minidrivers WDK VRAM capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Capturing Video to VRAM using AVStream


Beginning in Windows Vista, AVStream drivers can capture video and audio directly to the graphics adapter's VRAM. AVStream drivers that existed prior to Windows Vista must first place data in VRAM, transfer it to system memory, and then finally back to VRAM for display.

The new VRAM capture support takes advantage of the GPU scheduling and VRAM virtualization offered by the [Windows Vista Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570593).

To capture to VRAM, a device must include capture and display functionality on the same video card.

The following sections describe how to add VRAM capture support to a new or existing driver:

[Overview of VRAM Capture in AVStream](overview-of-vram-capture-in-avstream.md)

[VRAM Capture Properties](vram-capture-properties.md)

[Capturing Uncompressed Data to VRAM](capturing-uncompressed-data-to-vram.md)

[Adding VRAM Capture Support to Existing AVStream Drivers](adding-vram-capture-support-to-existing-avstream-drivers.md)

You can find sample code showing VRAM capture in the MSDN Code Gallery's [AVStream Simulated Hardware Sample Driver (AVSHwS)](http://go.microsoft.com/fwlink/p/?linkid=256083).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Capturing%20Video%20to%20VRAM%20using%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


