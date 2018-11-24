---
title: Benefits of the Windows Display Driver Model (WDDM)
description: Benefits of the Windows Display Driver Model (WDDM)
ms.assetid: 0e8cd1a9-7137-4fd2-91ab-56768713c9f1
keywords:
- display driver model WDK Windows Vista , benefits
- Windows Vista display driver model WDK , benefits
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Benefits of the Windows Display Driver Model (WDDM)


## <span id="ddk_benefits_of_the_longhorn_display_driver_model_gg"></span><span id="DDK_BENEFITS_OF_THE_LONGHORN_DISPLAY_DRIVER_MODEL_GG"></span>


Creating display drivers is easier using the Windows Display Driver Model (WDDM), available starting with Windows Vista, as opposed to using the [Windows 2000 Display Driver Model (XDDM)](windows-2000-display-driver-model-design-guide.md), because of the following enhancements. In addition, WDDM drivers contribute to greater operating system stability and security because less driver code runs in kernel mode where it can access system address space and possibly cause crashes.

**Note**  XDDM and VGA drivers will not compile on Windows 8 and later versions. If display hardware is attached to a Windows 8 computer without a driver that is certified to support WDDM 1.2 or later, the system defaults to running the Microsoft Basic Display Driver.

 

-   The Microsoft Direct3D runtime and Microsoft DirectX graphics kernel subsystem perform more of the display processing (that is, more code is in the runtime and subsystem as opposed to the drivers). This includes code that manages video memory and schedules direct memory access (DMA) buffers for the GPU. For more information, see [Video Memory Management and GPU Scheduling](video-memory-management-and-gpu-scheduling.md).

-   Surface creation requires fewer kernel-mode stages.

    Surface creation on operating systems earlier than Windows Vista requires the following successive kernel-mode calls:

    1.  [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213)
    2.  [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263)
    3.  [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840)

    Surface creation in WDDM requires only the [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) user-mode display driver call, which in turn calls the [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893) function. A call to the kernel-mode [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function then occurs.

-   Calls that create and destroy surfaces and that lock and unlock resources are more evenly paired.

-   Video memory, system memory, and managed surfaces are handled identically in WDDM. Operating systems prior to Windows Vista handled these components in subtly different ways.

-   Shader translation is performed in the user-mode portion of the display drivers.

    This approach eliminates the following complexities that occur when shader translation is performed in kernel mode:

    -   Hardware models that do not match device driver interface (DDI) abstractions
    -   Complex compiler technology that is used in the translation

    Because the shader processing occurs completely per process and hardware access is not required, kernel-mode shader processing is not required. Therefore, shader translation code can be processed in user mode.

    You must write try/except code around user-mode translation code. Translation faults should cause a return to application processing.

    Background translation (that is, translation code that runs in a separate thread from other display-processing threads) is easier to write for user mode.

 

 





