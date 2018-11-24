---
title: Kernel Mode Hardware Acceleration DDI
description: Kernel Mode Hardware Acceleration DDI
ms.assetid: f3af3caa-0d1f-4da5-8756-ce71c66d5fb6
keywords:
- DirectMusic kernel-mode WDK audio
- kernel-mode synths WDK audio , hardware acceleration
- DirectMusic kernel-mode WDK audio , about kernel-mode
- kernel-mode synths WDK audio , about kernel-mode synths
- DirectMusic WDK audio , hardware acceleration
- hardware acceleration WDK audio
- miniport drivers WDK audio , kernel-mode hardware acceleration
- synthesizers WDK audio , kernel-mode hardware acceleration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel Mode Hardware Acceleration DDI


## <span id="kernel_mode_hardware_acceleration_ddi"></span><span id="KERNEL_MODE_HARDWARE_ACCELERATION_DDI"></span>


This portion of the design guide contains information necessary to write a kernel-mode DMus miniport driver for DirectMusic-enabled hardware or a software synthesizer. The features described here are optional and can be implemented in addition to the base-level MIDI miniport driver, which supports the **midiOut** and **midiIn** APIs under Microsoft Windows 95/98/Me, Windows NT 4.0, Windows 2000, and later.

Implementing kernel-mode components entails making additions to the miniport device driver interface (DDI) that allow WDM MIDI drivers to support DirectMusic hardware acceleration. A good design strategy is to begin by implementing a user-mode version of your driver and then converting it to kernel mode (see [User Mode Versus Kernel Mode](user-mode-versus-kernel-mode.md)).

If you have not written a user-mode version before doing your kernel-mode implementation, read the user-mode sections of this document to become familiar with the concepts, which apply to kernel mode as well. Kernel-mode discussions build on common concepts that are introduced in the user-mode examples.

The next two sections give a brief background of WDM kernel streaming and an overview of how to implement a miniport-driver for a synthesizer:

[DirectMusic WDM Kernel Streaming Background](directmusic-wdm-kernel-streaming-background.md)

[Synthesizer Miniport Driver Overview](synthesizer-miniport-driver-overview.md)

This section also includes:

[DirectMusic Miniport Driver Interface](directmusic-miniport-driver-interface.md)

[Voice Allocation](voice-allocation.md)

[Default Sound Sample Sets](default-sound-sample-sets.md)

[Support for DirectMusic Properties](support-for-directmusic-properties.md)

 

 




