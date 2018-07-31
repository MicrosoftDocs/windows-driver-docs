---
title: Multiplane overlay support
description: Multiplane overlays can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.
ms.assetid: 8B2F5497-554D-4D4A-B44E-985A9F89143D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 





