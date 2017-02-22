---
title: Migrating to the Windows Display Driver Model (WDDM)
description: Migrating to the Windows Display Driver Model (WDDM)
ms.assetid: 7f926aa7-1698-4a4e-a1ce-54a316bdc0cd
keywords: ["display driver model WDK Windows Vista , migrating", "Windows Vista display driver model WDK , migrating", "migrating display driver model WDK Windows Vista"]
---

# Migrating to the Windows Display Driver Model (WDDM)


## <span id="ddk_migrating_to_the_longhorn_display_driver_model_gg"></span><span id="DDK_MIGRATING_TO_THE_LONGHORN_DISPLAY_DRIVER_MODEL_GG"></span>


Migrating to the Windows Display Driver Model (WDDM)) requires driver writers to write completely different display and video miniport drivers. Similar to the [Windows 2000 display driver model (XDDM)](windows-2000-display-driver-model-design-guide.md), WDDM requires a paired display driver and display miniport driver. However, in WDDM, the display driver runs in user mode. Also, the model does not use services of the Windows Graphics Device Interface (GDI) engine; the model uses services of the Microsoft Direct3D runtime and Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys).

WDDM supports display and video miniport drivers written according to XDDM. However, new drivers should be written as WDDM drivers, whenever possible, to take advantage of software and hardware features available starting with Windows Vista.

Although driver writers can reuse low-level hardware-dependent code in their WDDM drivers, they should rewrite new device driver interface (DDI)-related code. When writing WDDMdrivers, consider these points:

-   The display miniport driver must implement a revised set of entry-point functions to interact with the operating system and the DirectX graphics kernel subsystem. For more information, see [**DriverEntry of Display Miniport Driver**](https://msdn.microsoft.com/library/windows/hardware/ff556157). The display miniport driver can call any documented kernel function.

-   The display miniport driver dynamically loads the appropriate DirectX graphics kernel subsystem. The display miniport driver and the DirectX graphics kernel subsystem call each other through interfaces.

-   The display miniport driver is no longer required to process most video I/O control codes (IOCTL). In XDDM, the kernel-mode display driver uses these codes to communicate with the video miniport driver. In WDDM, the user-mode display driver communicates with the Direct3D runtime; the WDDM graphics kernel subsystem, in turn, communicates with the display miniport driver.
    **Note**   The following IOCTLs are still used in WDDM, and the display miniport driver must process them:
    [**IOCTL\_VIDEO\_QUERY\_COLOR\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567817)
    [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567805)

     

<!-- -->

-   The user-mode display driver must implement and export an [**OpenAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff568601) function, which opens an instance of the graphics adapter. The user-mode display driver must also implement a [**CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540634) function, which creates representations of display devices that handle collections of rendering state.

-   The user-mode display driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function, along with the display miniport driver's [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function, replace the [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213), [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263), and [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) functions in XDDM.

-   Most of the remaining user-mode display driver functions implement the same functionality that the kernel-mode display driver for XDDM implemented in the following:
    -   The [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function and [**DP2**](https://msdn.microsoft.com/library/windows/hardware/ff545678) operation codes
    -   The [motion compensation callback functions](https://msdn.microsoft.com/library/windows/hardware/ff568441) and [DirectX Video Acceleration structures](https://msdn.microsoft.com/library/windows/hardware/ff553882)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Migrating%20to%20the%20Windows%20Display%20Driver%20Model%20%28WDDM%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




