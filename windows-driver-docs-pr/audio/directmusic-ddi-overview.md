---
title: DirectMusic DDI Overview
description: DirectMusic DDI Overview
ms.assetid: 95870103-197c-4b7c-b6ee-cac176b62dfc
keywords: ["DirectMusic WDK audio , about DirectMusic DDI", "user-mode synths WDK audio", "kernel-mode synths WDK audio", "user-mode interface WDK audio", "DMus port drivers WDK audio", "kernel-mode interfaces WDK audio", "custom synths WDK audio", "DMus miniport drivers WDK audio"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DirectMusic%20DDI%20Overview%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


