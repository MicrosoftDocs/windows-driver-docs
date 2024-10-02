---
title: WDDM Architecture
description: Windows Display Driver Model (WDDM) Architecture
keywords:
- display driver model WDK Windows Vista , architecture
- Windows Vista display driver model WDK , architecture
- architecture WDK display
- user-mode display drivers WDK Windows Vista , architecture
ms.date: 10/02/2024
---

# WDDM Architecture

The Windows Display Driver Model (WDDM) has user-mode and kernel-mode components. The following figure shows the various components of the WDDM architecture.

:::image type="content" source="images/wddm-architecture.png" alt-text="Diagram showing the WDDM architecture with user-mode and kernel-mode components.":::

System-supplied modules are shown in the figure as white boxes. Gray boxes represent modules that partner can provide. Applications can be system-supplied or developed by partners.

## System-supplied modules

The following system-supplied modules are part of the WDDM architecture:

* The Direct3D runtime is a user-mode component that provides an application API for applications. It provides various services and is responsible for managing the interaction between an application, the user-mode graphics driver (UMD), and *gdi32.dll*.

* *gdi32.dll* is a user-mode library that a D3D runtime or a partner graphics client links against. A runtime or client calls a *gdi32* "thunk" that routes the call to the appropriate kernel-mode function in the DirectX kernel subsystem (*Dxgkrnl*).

* [*Dxgkrnl*](directx-graphics-kernel-subsystem.md) is the core component of the Windows operating system's kernel-mode graphics subsystem. It facilitates communication between the operating system, the UMD, and the kernel-mode display miniport driver (KMD). *Dxgkrnl* includes subcomponents such as the display port driver, the memory manager (*VidMm*), and the scheduler (*VidSch*). *Dxgkrnl* consists of the following system files:
  * *dxgmms2.sys*, which implements the GPU/NPU scheduler and video memory manager for WDDM versions 2.0 and above.
  * *dxgmms1.sys*, which implements the GPU/NPU scheduler and video memory manager for WDDM versions before WDDM 2.0.
  * *dxgkrnl.sys*, which handles everything else in the DirectX kernel subsystem, including loading the needed *dxgmms.sys* file, initial processing of **D3DKMT*Xxx*** calls from user mode, display modes, GPU virtualization, power management, interface with the kernel executive, and so forth.

* Win32 GDI and *Win32k.sys* are legacy components that are still used by some applications.

## Third party-supplied modules

* The UMD is a dynamic-link library (DLL) that the Direct3D runtime loads.

* The KMD communicates with *Dxgkrnl* and the graphics hardware.

A graphics hardware vendor must supply both a UMD and KMD.

* A third-party partner graphics client is a user-mode component that has its own API and framework. It calls *gdi32* thunks to communicate with the kernel-mode graphics subsystem. The clients that Microsoft is aware of are listed in [**D3DKMT_CLIENTHINT**](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-_d3dkmt_clienthint).
