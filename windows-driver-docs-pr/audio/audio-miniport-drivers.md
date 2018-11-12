---
title: Audio Miniport Drivers
description: Audio Miniport Drivers
ms.assetid: cf52759e-5da6-41a2-994d-4be15de9ae3d
keywords:
- WDM audio drivers WDK , miniport drivers
- audio drivers WDK , miniport drivers
- audio miniport drivers WDK
- miniport drivers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Audio Miniport Drivers


## <span id="audio_miniport_drivers"></span><span id="AUDIO_MINIPORT_DRIVERS"></span>


This section describes audio miniport driver interfaces and explains how to develop adapter drivers for audio hardware whose registers are directly accessible to the system processor over a system bus. This class of hardware includes all ISA/DMA, PCMCIA, and PCI audio adapters.

This documentation does not discuss how to support audio devices that reside on an external bus. For information about supporting audio devices on external buses, see [USBAudio Class System Driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver) and [AVCAudio Class System Driver](kernel-mode-wdm-audio-components.md#avcaudio_class_system_driver).

The following discussion assumes that the reader is familiar with kernel streaming (KS) concepts. For background information, see [Kernel Streaming](https://msdn.microsoft.com/library/windows/hardware/ff560842).

The WDM audio driver model divides the implementation of a KS filter into port and miniport drivers that are complementary but separate. This division makes audio hardware drivers easier to write by isolating generic filter-implementation issues from device-specific hardware-interface issues. Hardware vendors write miniport drivers to directly control their hardware devices, but the port drivers that implement the KS filters are provided with the operating system. The port and miniport drivers communicate with each other through well-defined software interfaces.

Various aspects of miniport driver development are discussed in the following topics:

[Introduction to Port Class](introduction-to-port-class.md)

[Supporting a Device](supporting-a-device.md)

[COM in the Kernel](com-in-the-kernel.md)

[Adapter Driver Construction](adapter-driver-construction.md)

[Miniport Driver Types by Operating System](miniport-driver-types-by-operating-system.md)

[Miniport Interfaces](miniport-interfaces.md)

[Installing a Port Class Audio Adapter](installing-a-port-class-audio-adapter.md)

[Port Driver Helper Objects](port-driver-helper-objects.md)

[Power Management for Audio Devices](power-management-for-audio-devices.md)

[Version Numbers for Audio Drivers](version-numbers-for-audio-drivers.md)

[Other Implementation Issues for Audio Drivers](other-implementation-issues-for-audio-drivers.md)

 

 




