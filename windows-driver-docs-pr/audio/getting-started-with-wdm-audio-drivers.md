---
title: WDM Audio Drivers Overview
description: Windows Driver Model (WDM) audio drivers make use of the kernel streaming (KS) components, which operate in kernel mode and are part of the operating system.
ms.assetid: 573a9b6d-6c50-40a6-9241-470ab418eb66
keywords: ["WDM audio drivers WDK", "audio drivers WDK , about audio drivers", "WDM audio drivers WDK , about WDM audio drivers", "vendor-supplied drivers WDK audio", "custom audio drivers WDK"]
---

# WDM Audio Drivers Overview


[Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM) audio drivers make use of the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff560842) (KS) components, which operate in kernel mode and are part of the operating system.

Hardware vendors should make several design decisions before beginning development of a Windows-based audio hardware device.

The first decision is whether to design an audio device that requires a vendor-supplied custom driver. Windows contains operating-system support for PCI, USB, and IEEE 1394 devices that conform to the Microsoft [Universal Audio Architecture](universal-audio-architecture.md) (UAA) guidelines. The vendor does not need to provide a custom driver for a UAA-compatible audio device.

However, if a vendor-supplied custom audio driver is necessary, the vendor must choose whether the driver should be designed to work in conjunction with the PortCls system driver (Portcls.sys) or the AVStream class system driver (Ks.sys). Both PortCls and AVStream are part of the Windows operating system. PortCls is the correct choice for most audio adapters. For more information about PortCls, see [Introduction to Port Class](introduction-to-port-class.md). For more information about AVStream, see [AVStream Overview](https://msdn.microsoft.com/library/windows/hardware/ff554240).

When designing a custom adapter driver that uses PortCls, the devices on the audio adapter are made available to applications using WaveRT. For more information, see [Introducing the WaveRT Port Driver](introducing-the-wavert-port-driver.md).

Two additional decisions involve how to present the adapter topology and pin data ranges to audio applications. The topology is a logical map of the data paths and control nodes in the adapter circuitry. The data ranges specify the data formats that the devices can support in their wave and MIDI streams. Both decisions affect how the devices on the audio adapter appear to applications.

In making all of the previously mentioned decisions, the hardware vendor must weigh the value of performance enhancements against the cost of implementing them. Another consideration is whether a particular solution can be made to work on a number of products in the Windows family. This section provides an overview of these issues as well as references to more detailed documentation about specific topics.

This section includes the following topics:

[Universal Audio Architecture](universal-audio-architecture.md)

[Audio Signal Processing Modes](audio-signal-processing-modes.md)

[Custom Audio Drivers](custom-audio-drivers.md)

[Specifying the Topology](specifying-the-topology.md)

[Specifying Pin Data Ranges](specifying-pin-data-ranges.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20WDM%20Audio%20Drivers%20Overview%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




