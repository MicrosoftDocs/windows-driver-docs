---
title: Using cross-adapter resources in a hybrid system
description: A Windows Display Driver Model (WDDM) driver can support a hybrid system, where cross-adapter resources are shared between an integrated GPU and a discrete GPU.
ms.assetid: ECBB0AA7-50C2-41C8-9DC6-6EEFC5CEEB15
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# <span id="display.using_cross-adapter_resources_in_a_hybrid_system"></span>Using cross-adapter resources in a hybrid system


Starting in Windows 8.1, a Windows Display Driver Model (WDDM) driver can support a *hybrid system*, where *cross-adapter resources* are shared between an integrated GPU and a discrete GPU, and an application can be run on either GPU, depending on the needs of the application. The operating system and driver together determine which GPU an application should run on.

The display miniport driver should express support for cross-adapter resources by setting the **CrossAdapterResource** member of the [**DXGK\_VIDMMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562072) structure.

Drivers get information in different ways depending on the type of allocation. If the allocation is a traditional full-screen primary, the user-mode display driver gets the information that's usually provided when the primary is created, such as the primary flag, the video present network (VidPN) source ID, the refresh rate, and rotation information. However, if the allocation is a direct flip primary, the cross-adapter allocation could be used as a primary, but the user-mode display driver won't get the usual information that's provided when the primary is created. Also, in this case the discrete user-mode display driver receives information about the primary but should not validate it. The integrated driver does not receive information that indicates that it's a primary.

These subsequent topics give more details on driver implementation for hybrid systems:

-   [Validating a hybrid system configuration](validating-a-hybrid-system-configuration.md)
-   [Rendering on a discrete GPU using cross-adapter resources](rendering-on-a-discrete-gpu-using-cross-adapter-resources.md)
-   [Hybrid system DDI](hybrid-system-ddi.md)

## <span id="definition_of_a_hybrid_system"></span><span id="DEFINITION_OF_A_HYBRID_SYSTEM"></span>Definition and properties of a hybrid system:


-   The system contains a single integrated GPU and a single discrete GPU:
    The *integrated GPU* is integrated into the CPU chipset and outputs to an integrated display panel such as an LCD panel.
    The *discrete GPU* is typically a removable card that connects to a motherboard chipset's north bridge through a bus such as PCI.
-   The discrete GPU has significantly higher performance than the integrated GPU.
-   The discrete GPU is a render-only device, and no display outputs are connected to it.
-   Both GPUs are physically enclosed in the same housing, and the discrete GPU can't be connected or disconnected while the computer is running.
-   The operating system detects the configuration of a hybrid system when it runs power-on self-test (POST) routines, when a new driver is installed, or when a display adapter is enabled or disabled.

## <span id="definition_of_a_cross_adapter_resource"></span><span id="DEFINITION_OF_A_CROSS_ADAPTER_RESOURCE"></span>Definition and properties of a cross-adapter resource:


-   A cross-adapter resource is available only starting in Windows 8.1.
-   It can be paged-in only to the aperture GPU memory segment.
-   It is allocated as a shared resource.
-   It has only one allocation, in a linear format.
-   It has a standard pitch alignment of 128 bytes (defined by the **D3DKMT\_CROSS\_ADAPTER\_RESOURCE\_PITCH\_ALIGNMENT** constant).
-   It has a standard height alignment of 4 rows (defined by the **D3DKMT\_CROSS\_ADAPTER\_RESOURCE\_HEIGHT\_ALIGNMENT** constant).
-   Its memory start address is aligned to a one-page boundary.
-   It might be created as a standard allocation from kernel mode by the display miniport driver and then be opened later by the user-mode display driver.
-   It might be created by the user-mode display driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20cross-adapter%20resources%20in%20a%20hybrid%20system%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




