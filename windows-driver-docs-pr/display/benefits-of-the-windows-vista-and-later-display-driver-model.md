---
title: Benefits of the Windows Display Driver Model (WDDM)
description: Benefits of the Windows Display Driver Model (WDDM)
ms.assetid: 0e8cd1a9-7137-4fd2-91ab-56768713c9f1
keywords:
- display driver model WDK Windows Vista , benefits
- Windows Vista display driver model WDK , benefits
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Benefits%20of%20the%20Windows%20Display%20Driver%20Model%20%28WDDM%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




