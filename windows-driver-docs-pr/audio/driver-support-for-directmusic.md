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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




