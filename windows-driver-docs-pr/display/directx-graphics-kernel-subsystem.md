---
title: DirectX Graphics Kernel Subsystem
description: The Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) implements functions that are called by the display miniport driver.
keywords:
- DirectX graphics kernel subsystem
- Dxgkrnl.sys
ms.date: 06/26/2024
---

# DirectX Graphics Kernel Subsystem (*Dxgkrnl*)

This article describes kernel-mode interfaces that the Windows operating system implements through the DirectX graphics kernel subsystem (*Dxgkrnl.sys*).

The display port driver is one portion of *Dxgkrnl.sys*. A graphics/display hardware vendor implements the kernel-mode display miniport driver (KMD).

For descriptions of other functions implemented by *Dxgkrnl*, see articles such as:

[VidPN Objects and Interfaces](vidpn-objects-and-interfaces.md)

[Supporting Path-Independent Rotation](supporting-path-independent-rotation.md)

[Obtaining Additional Monitor Target Modes](obtaining-additional-monitor-target-modes.md)

## Dxgkrnl Interface

A KMD's [**DriverEntry**](driverentry-of-video-miniport-driver.md) function calls the operating system's [**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize) function, which causes *Dxgkrnl* to be loaded and initialized.

Once loaded, *Dxgkrnl.sys* provides the KMD with pointers to its functions by passing a [**DXGKRNL_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgkrnl_interface) structure to the KMD's [**DxgkDdiStartDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device) function. *Dxgkrnl*'s function pointers have a *DxgkCb* prefix.

The **DXGKRNL_INTERFACE** structure also contains a handle to a particular display adapter. The display port driver generates this handle. The KMD passes this handle as an argument each time it calls any of the functions in **DXGKRNL_INTERFACE**.

## Display port driver interfaces

The KMD gets the display port driver's interfaces by calling *Dxgkrnl*'s [**DxgkCbQueryServices**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_query_services) function with a [**DXGK_SERVICES**](/windows-hardware/drivers/ddi/dispmprt/ne-dispmprt-dxgk_services) value that specifies the type of interface that the KMD wants. Services that the display port driver provides include AGP (Accelerated Graphics Port) services, debug report services, timed operation services, and more.

## See also

[Windows Display Driver Model (WDDM) Architecture](windows-vista-and-later-display-driver-model-architecture.md)

[Initializing the Display Miniport Driver](initializing-the-display-miniport-driver.md)
