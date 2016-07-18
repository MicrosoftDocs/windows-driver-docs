---
title: Kernel Mode Hardware Acceleration DDI
description: Kernel Mode Hardware Acceleration DDI
ms.assetid: f3af3caa-0d1f-4da5-8756-ce71c66d5fb6
keywords: ["DirectMusic kernel-mode WDK audio", "kernel-mode synths WDK audio , hardware acceleration", "DirectMusic kernel-mode WDK audio , about kernel-mode", "kernel-mode synths WDK audio , about kernel-mode synths", "DirectMusic WDK audio , hardware acceleration", "hardware acceleration WDK audio", "miniport drivers WDK audio , kernel-mode hardware acceleration", "synthesizers WDK audio , kernel-mode hardware acceleration"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Kernel%20Mode%20Hardware%20Acceleration%20DDI%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


