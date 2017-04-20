---
title: Multiplane overlay support
description: Multiplane overlays can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.
ms.assetid: 8B2F5497-554D-4D4A-B44E-985A9F89143D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multiplane overlay support


Multiplane overlays can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.

These sections describe how to implement this capability in your driver:

<span id="Multiplane_overlay_functions_called_by_user-mode_display_drivers"></span><span id="multiplane_overlay_functions_called_by_user-mode_display_drivers"></span><span id="MULTIPLANE_OVERLAY_FUNCTIONS_CALLED_BY_USER-MODE_DISPLAY_DRIVERS"></span>[Multiplane overlay functions called by user-mode display drivers](https://msdn.microsoft.com/library/windows/hardware/dn265491)  
All user-mode multiplane overlay functions that the operating system implements.

<span id="Multiplane_overlay_functions_implemented_by_the_user-mode_driver"></span><span id="multiplane_overlay_functions_implemented_by_the_user-mode_driver"></span><span id="MULTIPLANE_OVERLAY_FUNCTIONS_IMPLEMENTED_BY_THE_USER-MODE_DRIVER"></span>[Multiplane overlay functions implemented by the user-mode driver](https://msdn.microsoft.com/library/windows/hardware/dn265484)  
All functions that a user-mode driver must implement in order to support multiplane overlays.

<span id="Multiplane_overlay_user-mode_structures_and_enumerations"></span><span id="multiplane_overlay_user-mode_structures_and_enumerations"></span><span id="MULTIPLANE_OVERLAY_USER-MODE_STRUCTURES_AND_ENUMERATIONS"></span>[Multiplane overlay user-mode structures and enumerations](https://msdn.microsoft.com/library/windows/hardware/dn265489)  
All user-mode structures and enumerations that are used with multiplane overlay device driver interfaces (DDIs).

<span id="Multiplane_overlay_kernel-mode_driver-implemented_functions"></span><span id="multiplane_overlay_kernel-mode_driver-implemented_functions"></span><span id="MULTIPLANE_OVERLAY_KERNEL-MODE_DRIVER-IMPLEMENTED_FUNCTIONS"></span>[Multiplane overlay kernel-mode driver-implemented functions](https://msdn.microsoft.com/library/windows/hardware/dn265485)  
All multiplane overlay functions that the display miniport driver implements.

<span id="Multiplane_overlay_kernel-mode_structures"></span><span id="multiplane_overlay_kernel-mode_structures"></span><span id="MULTIPLANE_OVERLAY_KERNEL-MODE_STRUCTURES"></span>[Multiplane overlay kernel-mode structures](https://msdn.microsoft.com/library/windows/hardware/dn265486)  
All structures that are used by the display miniport driver.

<span id="Multiplane_overlay_kernel-mode_enumerations"></span><span id="multiplane_overlay_kernel-mode_enumerations"></span><span id="MULTIPLANE_OVERLAY_KERNEL-MODE_ENUMERATIONS"></span>[Multiplane overlay kernel-mode enumerations](https://msdn.microsoft.com/library/windows/hardware/dn265483)  
All enumerations that are used by the display miniport driver.

This user-mode enumeration constant value supports multiplane overlays and is new for Windows 8.1:

-   [**D3DDDICAPS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff544132) (new **D3DDDICAPS\_GET\_MULTIPLANE\_OVERLAY\_GROUP\_CAPS** constant value)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multiplane%20overlay%20support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




