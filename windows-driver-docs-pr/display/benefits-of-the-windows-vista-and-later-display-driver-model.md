---
title: Benefits of the WDDM
description: Benefits of the Windows Display Driver Model (WDDM)
keywords:
- display driver model WDK Windows Vista , benefits
- Windows Vista display driver model WDK , benefits
ms.date: 03/20/2023
---

# Benefits of the WDDM

> [!NOTE]
> XDDM and VGA drivers will not compile on Windows 8 and later operating systems. If display hardware is attached to a Windows 8 computer without a driver that is certified to support WDDM 1.2 or later, the system defaults to running the Basic Display Driver.

Creating graphics/display drivers is easier using the WDDM as opposed to using the [Windows 2000 Display Driver Model (XDDM)](windows-2000-display-driver-model-design-guide.md), because of the following enhancements. In addition, WDDM drivers contribute to greater operating system stability and security. Less driver code runs in kernel mode where it can access system address space and possibly cause crashes.

- The Direct3D runtime and DirectX graphics kernel subsystem (*Dxgkrnl*) perform more of the display processing; that is, more code is in the runtime and subsystem as opposed to the drivers. This processing includes code that manages video memory and schedules direct memory access (DMA) buffers for the GPU. For more information, see [Video Memory Management and GPU Scheduling](video-memory-management-and-gpu-scheduling.md).

- Surface creation requires fewer kernel-mode stages.

  Surface creation on operating systems earlier than Windows Vista required the following successive kernel-mode calls:

  1. [*DdCanCreateSurface*](/previous-versions/windows/hardware/drivers/ff549213(v=vs.85))
  2. [*DdCreateSurface*](/previous-versions/windows/hardware/drivers/ff549263(v=vs.85))
  3. [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex)

  Surface creation in WDDM requires only the [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) user-mode display driver call, which in turn calls the runtime's [**pfnAllocateCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_allocatecb) function. This call causes *Dxgkrnl* to call to the kernel-mode driver's [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) function.

- Calls that create and destroy surfaces and that lock and unlock resources are more evenly paired.

- WDDM handles video memory, system memory, and managed surfaces identically. Operating systems prior to Windows Vista handled these components in subtly different ways.

- Shader translation is performed in the user-mode portion of the display drivers.

  This approach eliminates the following complexities that occur when shader translation is performed in kernel mode:

  - Hardware models that don't match device driver interface (DDI) abstractions
  - Complex compiler technology that is used in the translation

  Because the shader processing occurs completely per process and hardware access isn't required, kernel-mode shader processing isn't required. Therefore, shader translation code can be processed in user mode.

  You must write try/except code around user-mode translation code. Translation faults should cause a return to application processing.

  Background translation (that is, translation code that runs in a separate thread from other display-processing threads) is easier to write for user mode.
