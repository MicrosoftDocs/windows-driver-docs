---
title: What's new for Windows 7 display drivers (WDDM 1.1)
description: What's new for Windows 7 display drivers (WDDM 1.1)
ms.assetid: 516A9C56-7ABC-49F4-8E92-3B6C3DB78CF6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What's new for Windows 7 display drivers (WDDM 1.1)


The Windows Driver Kit (WDK) that is released with Windows 7 includes new features for user-mode display drivers and kernel-mode display miniport drivers. It also includes updates to the requirements for installing display drivers that are optimized for Windows 7 and information about new Microsoft Win32 APIs that are available in Windows 7 that control desktop display setup.

### <span id="new_windows_7_features_for_user_mode_display_drivers"></span><span id="NEW_WINDOWS_7_FEATURES_FOR_USER_MODE_DISPLAY_DRIVERS"></span>New Windows 7 Features for User-Mode Display Drivers

The new Windows 7 features for user-mode display drivers include:

[Processing High-Definition Video](processing-high-definition-video.md)

[Protecting Video Content](protecting-video-content.md)

[Verifying Overlay Support](verifying-overlay-support.md)

[Supporting Direct3D Version 11](supporting-direct3d-version-11.md)

[Supporting OpenGL Enhancements](supporting-opengl-enhancements.md)

[Managing Resources for Multiple GPU Scenarios](managing-resources-for-multiple-gpu-scenarios.md)

Windows 7 also provides extended format awareness to Microsoft Direct3D version 10.1. For more information about extended format awareness, see [Supporting Extended Format Awareness](supporting-extended-format-awareness.md).

### <span id="connecting_and_configuring_displays"></span><span id="CONNECTING_AND_CONFIGURING_DISPLAYS"></span>Connecting and Configuring Displays

For information about the new Win32 APIs that control desktop display setup, see [Connecting and Configuring Displays](connecting-and-configuring-displays.md).

### <span id="new_windows_7_features_for_kernel_mode_display_miniport_drivers"></span><span id="NEW_WINDOWS_7_FEATURES_FOR_KERNEL_MODE_DISPLAY_MINIPORT_DRIVERS"></span>New Windows 7 Features for Kernel-Mode Display Miniport Drivers

You can develop your kernel-mode display miniport driver to run on Windows 7 with the following capabilities:

[Connecting and Configuring Displays - DDIs](ccd-ddis.md)

[GDI Hardware Acceleration](gdi-hardware-acceleration.md)

### <span id="new_inf_requirements"></span><span id="NEW_INF_REQUIREMENTS"></span>New INF Requirements

The INF files for display drivers that are written to the Windows Vista display driver model and that are optimized for the model's Windows 7 features, require several updates. For information about these updates, see [Installing Display Drivers Optimized for Windows 7 and Later](installing-display-drivers-optimized-for-windows-7-and-later.md).

### <span id="gpuview"></span><span id="GPUVIEW"></span>GPUView

The release of the Windows 7 operating system also introduces GPUView (GPUView.exe), which is a new development tool that monitors the performance of the graphics processing unit (GPU). For more information about GPUView, see [Using GPUView](using-gpuview.md).

 

 





