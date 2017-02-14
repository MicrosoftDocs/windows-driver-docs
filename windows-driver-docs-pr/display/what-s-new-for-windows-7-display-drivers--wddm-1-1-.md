---
title: What's new for Windows 7 display drivers (WDDM 1.1)
description: What's new for Windows 7 display drivers (WDDM 1.1)
ms.assetid: 516A9C56-7ABC-49F4-8E92-3B6C3DB78CF6
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20What's%20new%20for%20Windows%207%20display%20drivers%20%28WDDM%201.1%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




