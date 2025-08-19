---
title: Using Cross-Adapter Resources in a Hybrid System
description: A Windows Display Driver Model (WDDM) driver can support a hybrid system, where cross-adapter resources are shared between an integrated GPU and a discrete GPU.
ms.date: 08/20/2024
ms.topic: concept-article
---

# Using cross-adapter resources in a hybrid system

This article describes hybrid systems and how to use cross-adapter resources in a hybrid system.

Starting in Windows 8.1, a Windows Display Driver Model (WDDM) driver can support a *hybrid system*, where:

* *Cross-adapter resources* are shared between an integrated GPU and a discrete GPU.
* An application can be run on either GPU, depending on the needs of the application.

On such a system, the operating system and driver together determine which GPU an application should run on.

## Definition and properties of a hybrid system

* The system contains a single integrated GPU and a single discrete GPU:
  * The *integrated GPU* is integrated into the CPU chipset and outputs to an integrated display panel such as an LCD panel.
  * The *discrete GPU* is typically a removable card that connects to a motherboard chipset's Northbridge through a bus such as PCI.
* The discrete GPU has higher performance than the integrated GPU.
* The discrete GPU is a render-only device, and no display outputs are connected to it.
* Both GPUs are physically enclosed in the same housing, and the discrete GPU can't be connected or disconnected while the computer is running.
* The OS detects the configuration of a hybrid system in the following situations:
  * When it runs power-on self-test (POST) routines
  * When a new driver is installed
  * When a display adapter is enabled or disabled

## Definition and properties of a cross-adapter resource

* A cross-adapter resource is available only starting in Windows 8.1.
* It can be paged-in only to the aperture GPU memory segment.
* It's allocated as a shared resource.
* It has only one allocation, in a linear format.
* It has a standard pitch alignment of 128 bytes (defined by the **D3DKMT_CROSS_ADAPTER_RESOURCE_PITCH_ALIGNMENT** constant).
* It has a standard height alignment of 4 rows (defined by the **D3DKMT_CROSS_ADAPTER_RESOURCE_HEIGHT_ALIGNMENT** constant).
* Its memory start address is aligned to a one-page boundary.
* The kernel-mode display driver (KMD) might create the cross-adapter resource as a standard allocation that the user-mode driver (UMD) can open later.
* The UMD might create it.

## Driver implementation for hybrid systems

The KMD can express support for cross-adapter resources by setting the **CrossAdapterResource** member of the [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) structure.

Drivers get information in different ways depending on the type of allocation.

* If the allocation is a traditional full-screen primary, the UMD gets the information typically provided when the primary is created. Such information includes the primary flag, the video present network (VidPN) source ID, the refresh rate, and rotation information.
* If, however, the allocation is a direct flip primary, the cross-adapter allocation could be used as a primary, but the UMD won't get the usual information provided when the primary is created. Also, in this case, the discrete UMD receives information about the primary but shouldn't validate it. The integrated driver doesn't receive information that indicates that it's a primary.

The following articles give more details on driver implementation for hybrid systems:

* [Validating a hybrid system configuration](validating-a-hybrid-system-configuration.md)
* [Rendering on a discrete GPU using cross-adapter resources](rendering-on-a-discrete-gpu-using-cross-adapter-resources.md)
* [Hybrid system DDI](hybrid-system-ddi.md)
* [Supporting cross-adapter resources in a hybrid system](supporting-caso.md)
