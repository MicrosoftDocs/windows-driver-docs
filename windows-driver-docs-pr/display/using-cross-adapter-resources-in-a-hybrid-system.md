---
title: Using Cross-Adapter Resources in a Hybrid System
description: A Windows Display Driver Model (WDDM) driver can support a hybrid system, where cross-adapter resources are shared between an integrated GPU and a discrete GPU.
ms.date: 04/20/2017
---

# <span id="display.using_cross-adapter_resources_in_a_hybrid_system"></span>Using cross-adapter resources in a hybrid system


Starting in Windows 8.1, a Windows Display Driver Model (WDDM) driver can support a *hybrid system*, where *cross-adapter resources* are shared between an integrated GPU and a discrete GPU, and an application can be run on either GPU, depending on the needs of the application. The operating system and driver together determine which GPU an application should run on.

The display miniport driver should express support for cross-adapter resources by setting the **CrossAdapterResource** member of the [**DXGK\_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) structure.

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


-   A cross-adapter resource is available only starting in Windows 8.1.
-   It can be paged-in only to the aperture GPU memory segment.
-   It is allocated as a shared resource.
-   It has only one allocation, in a linear format.
-   It has a standard pitch alignment of 128 bytes (defined by the **D3DKMT\_CROSS\_ADAPTER\_RESOURCE\_PITCH\_ALIGNMENT** constant).
-   It has a standard height alignment of 4 rows (defined by the **D3DKMT\_CROSS\_ADAPTER\_RESOURCE\_HEIGHT\_ALIGNMENT** constant).
-   Its memory start address is aligned to a one-page boundary.
-   It might be created as a standard allocation from kernel mode by the display miniport driver and then be opened later by the user-mode display driver.
-   It might be created by the user-mode display driver.

 

