---
title: Capturing Video to VRAM using AVStream
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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

You can find sample code showing VRAM capture in the [AVStream Simulated Hardware Sample Driver (AVSHwS)](http://go.microsoft.com/fwlink/p/?linkid=256083).

 

 




