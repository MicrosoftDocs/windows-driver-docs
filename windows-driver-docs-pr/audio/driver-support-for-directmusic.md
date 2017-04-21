---
title: Driver Support for DirectMusic
description: Driver Support for DirectMusic
ms.assetid: 48f6245e-0911-46b6-9cf9-ea4db8875021
keywords:
- DirectMusic WDK audio
- audio drivers WDK , DirectMusic
- synthesizers WDK audio
- wave sinks WDK audio
- WDM audio drivers WDK , DirectMusic
- DMus WDK audio
- synth sink WDK audio
- render sink WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver Support for DirectMusic


## <span id="driver_support_for_directmusic"></span><span id="DRIVER_SUPPORT_FOR_DIRECTMUSIC"></span>


This document is a design guide for implementing drivers for Microsoft DirectMusic synthesizers (synths) and wave sinks:

-   A synthesizer is a device that inputs a stream of time-stamped MIDI messages and outputs an analog audio signal or a periodically sampled wave digital audio stream.

-   A wave sink is a streaming wave device that pulls wave audio samples from the synthesizer and feeds them to a target audio device.

Software synths and wave sinks can be implemented in user mode. Software or hardware components that provide the same functionality can be implemented in kernel mode. For more information about the relationship between synths and wave sinks, see [Synthesizers and Wave Sinks](synthesizers-and-wave-sinks.md). For information about the DirectMusic API, see the Microsoft Windows SDK documentation.

This design guide contains the following sections:

[DirectMusic DDI Overview](directmusic-ddi-overview.md)

[Custom Rendering in User Mode](custom-rendering-in-user-mode.md)

[Kernel Mode Hardware Acceleration DDI](kernel-mode-hardware-acceleration-ddi.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Driver%20Support%20for%20DirectMusic%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


