---
title: Migrating to the Windows Display Driver Model (WDDM)
description: Migrating to the Windows Display Driver Model (WDDM)
keywords:
- display driver model WDK Windows Vista , migrating
- Windows Vista display driver model WDK , migrating
- migrating display driver model WDK Windows Vista
ms.date: 04/20/2017
---

# Migrating to the Windows Display Driver Model (WDDM)


## <span id="ddk_migrating_to_the_longhorn_display_driver_model_gg"></span><span id="DDK_MIGRATING_TO_THE_LONGHORN_DISPLAY_DRIVER_MODEL_GG"></span>


Migrating to the Windows Display Driver Model (WDDM)) requires driver writers to write completely different display and video miniport drivers. Similar to the [Windows 2000 display driver model (XDDM)](windows-2000-display-driver-model-design-guide.md), WDDM requires a paired display driver and display miniport driver. However, in WDDM, the display driver runs in user mode. Also, the model does not use services of the Windows Graphics Device Interface (GDI) engine; the model uses services of the Microsoft Direct3D runtime and Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys).

WDDM supports display and video miniport drivers written according to XDDM. However, new drivers should be written as WDDM drivers, whenever possible, to take advantage of software and hardware features available starting with Windows Vista.

Although driver writers can reuse low-level hardware-dependent code in their WDDM drivers, they should rewrite new device driver interface (DDI)-related code. When writing WDDMdrivers, consider these points:

-   The display miniport driver must implement a revised set of entry-point functions to interact with the operating system and the DirectX graphics kernel subsystem. For more information, see [**DriverEntry of Display Miniport Driver**](./driverentry-of-display-miniport-driver.md). The display miniport driver can call any documented kernel function.

-   The display miniport driver dynamically loads the appropriate DirectX graphics kernel subsystem. The display miniport driver and the DirectX graphics kernel subsystem call each other through interfaces.

-   The display miniport driver is no longer required to process most video I/O control codes (IOCTL). In XDDM, the kernel-mode display driver uses these codes to communicate with the video miniport driver. In WDDM, the user-mode display driver communicates with the Direct3D runtime; the WDDM graphics kernel subsystem, in turn, communicates with the display miniport driver.
    **Note**   The following IOCTLs are still used in WDDM, and the display miniport driver must process them:
    [**IOCTL\_VIDEO\_QUERY\_COLOR\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_color_capabilities)
    [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_handle_videoparameters)

     

<!-- -->

-   The user-mode display driver must implement and export an [**OpenAdapter**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_openadapter) function, which opens an instance of the graphics adapter. The user-mode display driver must also implement a [**CreateDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function, which creates representations of display devices that handle collections of rendering state.

-   The user-mode display driver's [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) function, along with the display miniport driver's [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) function, replace the [*DdCanCreateSurface*](/previous-versions/windows/hardware/drivers/ff549213(v=vs.85)), [*DdCreateSurface*](/previous-versions/windows/hardware/drivers/ff549263(v=vs.85)), and [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex) functions in XDDM.

-   Most of the remaining user-mode display driver functions implement the same functionality that the kernel-mode display driver for XDDM implemented in the following:
    -   The [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) function and [**DP2**](/windows-hardware/drivers/ddi/d3dhal/ne-d3dhal-_d3dhal_dp2operation) operation codes
    -   The [motion compensation callback functions](/windows-hardware/drivers/ddi/_display/#functions) and [DirectX Video Acceleration structures](/windows-hardware/drivers/ddi/_display/#structures)

 

