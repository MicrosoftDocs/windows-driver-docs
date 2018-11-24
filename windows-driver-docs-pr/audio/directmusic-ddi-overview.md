---
title: DirectMusic DDI Overview
description: DirectMusic DDI Overview
ms.assetid: 95870103-197c-4b7c-b6ee-cac176b62dfc
keywords:
- DirectMusic WDK audio , about DirectMusic DDI
- user-mode synths WDK audio
- kernel-mode synths WDK audio
- user-mode interface WDK audio
- DMus port drivers WDK audio
- kernel-mode interfaces WDK audio
- custom synths WDK audio
- DMus miniport drivers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectMusic DDI Overview


## <span id="directmusic_ddi_overview"></span><span id="DIRECTMUSIC_DDI_OVERVIEW"></span>


The design principles that are needed to implement user-mode synths generally apply to kernel-mode synths as well. For this reason, this guide begins with a discussion of user-mode implementations and progresses to specific kernel-mode topics.

Typically, the best design strategy is to first write a software implementation of the DirectMusic [*device driver interface (DDI)*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss_device_driver_interface__ddi_) that runs in user mode. This approach is beneficial even if the final product is a kernel-mode implementation that uses hardware components. After the user-mode version is completed, the software can be converted to kernel mode and connections established with the hardware, one feature at a time. For more information, see [User Mode Versus Kernel Mode](user-mode-versus-kernel-mode.md).

DirectMusic uses the following user-mode interfaces to control user-mode synthesizers and communicate with kernel-streaming drivers:

[IDirectMusicSynth](https://msdn.microsoft.com/library/windows/hardware/ff536519)

This is the user-mode interface for implementing custom software synths.

[IDirectMusicSynthSink](https://msdn.microsoft.com/library/windows/hardware/ff536520)

This is the user-mode interface for implementing custom wave sinks in Microsoft DirectX 6.1 and DirectX 7. In DirectX 8 and later, DirectMusic always uses its private wave sink with a user-mode synth, and no public interface is supported for user-mode wave sinks.

[IKsControl](https://msdn.microsoft.com/library/windows/hardware/ff559766)

DirectMusic uses this interface to access the properties of kernel-streaming drivers from user mode in DirectX 6.1 and later.

Kernel-mode terminology differs slightly from user-mode because of the port-miniport driver model (see [Introduction to Port Class](introduction-to-port-class.md)), which delegates generic kernel-streaming tasks to the [DMus port driver](dmus-port-driver.md) and assigns hardware-specific functions to the DMus miniport driver. The port and miniport drivers share responsibilities for the synth. The kernel-mode wave sink is part of the kernel-resident port driver. Unlike the user-mode wave sink in DirectX 6.1 and DirectX 7, the kernel-mode wave sink is not replaceable. Most of the work that is required to build a custom kernel-mode driver is in the writing of the miniport driver. In most cases, the miniport driver is the only component that the driver writer needs to implement to support a piece of hardware, or to implement a custom software synth for DirectMusic.

Custom DMus miniport drivers use the following kernel-mode interfaces:

[IAllocatorMXF](https://msdn.microsoft.com/library/windows/hardware/ff536491)

[IMiniportDMus](https://msdn.microsoft.com/library/windows/hardware/ff536699)

[ISynthSinkDMus](https://msdn.microsoft.com/library/windows/hardware/ff537011)

[IMXF](https://msdn.microsoft.com/library/windows/hardware/ff536782)

[IMasterClock](https://msdn.microsoft.com/library/windows/hardware/ff536696)

[IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879)

DMus miniport drivers implement the **IMiniportDMus**, **ISynthSinkDMus**, and **IMXF** interfaces. The DMus port driver implements the **IAllocatorMXF**, **IMasterClock**, and **IPortDMus** interfaces and exposes them to miniport drivers.

 

 




