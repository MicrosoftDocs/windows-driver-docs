---
title: What's new for Windows 8.1 display drivers (WDDM 1.3)
description: This topic lists display driver features that are new or updated for Windows 8.1. Windows 8.1 introduces version 1.3 of the Windows Display Driver Model (WDDM).
ms.assetid: 0B699676-A43B-4E53-9598-CE2930E126AB
---

# What's new for Windows 8.1 display drivers (WDDM 1.3)


This topic lists display driver features that are new or updated for Windows 8.1. Windows 8.1 introduces version 1.3 of the Windows Display Driver Model (WDDM).

<span id="Enumerating_GPU_engine_capabilities"></span><span id="enumerating_gpu_engine_capabilities"></span><span id="ENUMERATING_GPU_ENGINE_CAPABILITIES"></span>[Enumerating GPU engine capabilities](enumerating-gpu-nodes.md)  
An interface that's used to query a GPU node's engine capabilities.

<span id="Using_cross-adapter_resources_in_a_hybrid_system"></span><span id="using_cross-adapter_resources_in_a_hybrid_system"></span><span id="USING_CROSS-ADAPTER_RESOURCES_IN_A_HYBRID_SYSTEM"></span>[Using cross-adapter resources in a hybrid system](using-cross-adapter-resources-in-a-hybrid-system.md)  
Describes how to handle resources that are shared between integrated and discrete GPUs.

<span id="YUV_format_ranges_in_"></span><span id="yuv_format_ranges_in_"></span><span id="YUV_FORMAT_RANGES_IN_"></span>[YUV format ranges in Windows 8.1](yuv-format-ranges.md)  
An interface that's used to signal user-mode display drivers that video inputs are either in the studio luminance range or in the extended range.

<span id="Wireless_displays__Miracast_"></span><span id="wireless_displays__miracast_"></span><span id="WIRELESS_DISPLAYS__MIRACAST_"></span>[Wireless displays (Miracast)](wireless-displays--miracast-.md)  
Describes how to enable wireless (Miracast) displays.

<span id="Multiplane_overlay_support"></span><span id="multiplane_overlay_support"></span><span id="MULTIPLANE_OVERLAY_SUPPORT"></span>[Multiplane overlay support](multiplane-overlay-support.md)  
Describes how to implement multiplane overlays.

<span id="Tiled_resource_support"></span><span id="tiled_resource_support"></span><span id="TILED_RESOURCE_SUPPORT"></span>[Tiled resource support](tiled-resource-support.md)  
Describes how to support tiled resources.

<span id="Adaptive_refresh_for_playing_24_fps_video_content"></span><span id="adaptive_refresh_for_playing_24_fps_video_content"></span><span id="ADAPTIVE_REFRESH_FOR_PLAYING_24_FPS_VIDEO_CONTENT"></span>[Adaptive refresh for playing 24 fps video content](adaptive-refresh-for-playing-24-fps-content.md)  
Describes how drivers implement 48-Hz adaptive refresh to conserve power on monitors that are normally run at 60 Hz.

<span id="Direct3D_rendering_performance_improvements"></span><span id="direct3d_rendering_performance_improvements"></span><span id="DIRECT3D_RENDERING_PERFORMANCE_IMPROVEMENTS"></span>[Direct3D rendering performance improvements](direct3d-rendering-performance-improvements.md)  
Describes how drivers can improve rendering performance on Microsoft Direct3D 9 hardware.

<span id="Graphics_kernel_performance_improvements"></span><span id="graphics_kernel_performance_improvements"></span><span id="GRAPHICS_KERNEL_PERFORMANCE_IMPROVEMENTS"></span>[Graphics kernel performance improvements](graphics-kernel-performance-improvements.md)  
Describes how drivers can manage history buffers to provide accurate timing data about the execution of API calls in a direct memory access (DMA) buffer.

<span id="Present_overhead_improvements"></span><span id="present_overhead_improvements"></span><span id="PRESENT_OVERHEAD_IMPROVEMENTS"></span>[Present overhead improvements](present-overhead-improvements.md)  
Describes how drivers must support additional texture formats and a new present device driver interface (DDI).

<span id="Specifying_device_state_and_frame_latency"></span><span id="specifying_device_state_and_frame_latency"></span><span id="SPECIFYING_DEVICE_STATE_AND_FRAME_LATENCY"></span>[Specifying device state and frame latency](specifying-device-state-and-frame-latency-starting-in-wddm-1-3.md)  
Describes how a user-mode display driver can pass device status and frame latency info to the display miniport driver.

<span id="Supporting_Path-Independent_Rotation"></span><span id="supporting_path-independent_rotation"></span><span id="SUPPORTING_PATH-INDEPENDENT_ROTATION"></span>[Supporting Path-Independent Rotation](supporting-path-independent-rotation.md)  
Supported starting with Windows 8.1 Update. Describes how a display miniport driver can support cloning portrait-first displays on landscape-first displays with the greatest possible resolution.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20What's%20new%20for%20Windows%C2%A08.1%20display%20drivers%20%28WDDM%201.3%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




