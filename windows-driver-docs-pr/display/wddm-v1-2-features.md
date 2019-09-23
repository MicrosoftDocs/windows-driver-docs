---
title: WDDM 1.2 features
description: This topic describes the Windows Display Driver Model (WDDM) Version 1.2 feature set, which includes several new enhancements that improve performance, reliability, and the overall end-user experience.
ms.assetid: 65072545-76F0-43A8-9E46-703CA99BFE90
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDDM 1.2 features


This topic describes the Windows Display Driver Model (WDDM) Version 1.2 feature set, which includes several new enhancements that improve performance, reliability, and the overall end-user experience.

Each of these features requires special support from third-party WDDM 1.2 and later drivers. This section elaborates on what constitutes the WDDM 1.2 feature set.

WDDM 1.2 has both mandatory and optional features. The driver must implement all the mandatory features to claim itself as a "WDDM 1.2 driver," while the driver can implement any combination (or none) of the optional features. A non-WDDM 1.2 driver must report none of the WDDM 1.2 features.

This table summarizes the WDDM 1.2 feature set. "M" indicates mandatory, "O" indicates optional, and "NA" indicates not applicable. To read details about each feature, follow the link in the left column.

**WDDM 1.2 feature set**

| Windows 8 features enabled by WDDM 1.2                                                                         | Feature benefit                                                                                                            | WDDM driver type: Full graphics | WDDM driver type: Render only | WDDM driver type: Display only |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------|-------------------------------|--------------------------------|
| [Video memory offer and reclaim](video-memory-offer-and-reclaim.md)                                           | Enables more efficient usage of video memory                                                                               | M                               | M                             | NA                             |
| [GPU preemption](gpu-preemption.md)                                                                           | Improves desktop responsiveness                                                                                            | M                               | M                             | NA                             |
| [TDR changes in Windows 8](tdr-changes-in-windows-8.md)                                                       | Improved resiliency to GPU hangs                                                                                           | M                               | M                             | NA                             |
| [Optimized screen rotation support](optimized-screen-rotation-support.md)                                     | Screen rotation experience without flicker                                                                                 | M                               | NA                            | M                              |
| [Stereoscopic 3D](stereoscopic-3d.md)                                                                         | Provides a consistent API and DDI platform to enable Stereoscopic 3D scenarios                                             | O                               | NA                            | NA                             |
| [Direct3D 11 video playback improvements](d3d11-video-playback-improvements.md)                               | Simplified programming experience for video playback applications                                                          | M\*                             | M\*                           | NA                             |
| [Direct flip of video memory](direct-flip-of-video-memory.md)                                                 | Improvements in the video playback and composition stack to reduce power consumption                                       | M                               | NA                            | NA                             |
| [Providing seamless state transitions](seamless-state-transitions-in-wddm-1-2-and-later.md)                   | High resolution is maintained in state transitions and during bug checks                                                   | M                               | NA                            | M                              |
| [Plug and Play (PnP) start and stop](plug-and-play--pnp--start-and-stop-cases.md)                             | Maintain high resolution as display ownership is transitioned between firmware, Windows, and driver                        | M                               | NA                            | M                              |
| [Standby hibernate optimizations](standby-hibernate-optimizations.md)                                         | Enables optimizations to the graphics stack to improve performance on sleep and resume                                     | O                               | O                             | NA                             |
| [GPU power management of idle states and active power](gpu-power-management-of-idle-and-active-power.md)      | Provides a standardized infrastructure for fine-grained device power management                                            | O                               | O                             | O                              |
| [XPS rasterization on the GPU](xps-rasterization-on-the-gpu.md)                                               | Enables a quality printing experience on Windows with third-party drivers                                                  | M\*\*                           | M\*\*                         | NA                             |
| [Container ID support for displays](container-id-support-for-displays-.md)                                    | Helps represent monitor device connectivity and associated state to the user in a user interface similar to the device hub | M                               | NA                            | M                              |
| [Disabling Frame Pointer Omission (FPO) optimization](disabling-frame-pointer-omission--fpo--optimization.md) | Improves debugging of performance problems related to FPO in the field                                                     | M                               | M                             | M                              |
| [User-mode driver logging](user-mode-driver-logging.md)                                                       | Improves ability to diagnose and investigate memory-related issues by providing better view into memory usage              | M                               | M                             | NA                             |

 

\*This feature is mandatory for all WDDM 1.2 drivers with Microsoft Direct3D 10-, 10.1-, 11-, or 11.1-capable hardware (or later).

\*\*No new device driver interface (DDI) or behavior changes. However, WDDM 1.2 and later drivers must be able to pass XML Paper Specification (XPS) rasterization conformance tests to ensure a quality printing experience for hardware-accelerated XPS printing scenarios.

**Note**  
A new set of APIs is available starting with Windows 8 for duplicating the desktop for collaboration scenarios. For more details, see [Desktop duplication](desktop-duplication-api.md).

 

## <span id="Additional_new_features_in_Windows_8"></span><span id="additional_new_features_in_windows_8"></span><span id="ADDITIONAL_NEW_FEATURES_IN_WINDOWS_8"></span>Additional new features in Windows 8


The following new or updated display driver DDIs are also provided in Windows 8:

[**Kernel Mode Display-Only Driver (KMDOD) Interface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)

Provides a limited set of display functions without rendering capability.

**Note**  Refer also to the [Kernel mode display-only miniport driver](https://go.microsoft.com/fwlink/p/?linkid=258742) sample.

 

[**Support for system on a chip (SoC) architecture through the SPB interface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)

Lets a display miniport driver access bus resources on an SoC system.

### <span id="Surprise_removal_of_secondary_adapter"></span><span id="surprise_removal_of_secondary_adapter"></span><span id="SURPRISE_REMOVAL_OF_SECONDARY_ADAPTER"></span>Surprise removal of secondary adapter

-   [*DxgkDdiNotifySurpriseRemoval*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_notify_surprise_removal)
-   [**DXGK\_SURPRISE\_REMOVAL\_TYPE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dispmprt/ne-dispmprt-_dxgk_surprise_removal_type)
-   [**DXGK\_DRIVERCAPS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps)
-   [**D3DKMT\_WDDM\_1\_2\_CAPS**](https://docs.microsoft.com/windows-hardware/drivers/display/d3dkmt-wddm-1-2-caps)

[**System Firmware Table Interface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dispmprt/ns-dispmprt-_dxgk_firmware_table_interface)

Lets the display miniport driver enumerate and read the system firmware table.

[**Brightness Control Interface V. 2 (Adaptive and Smooth Brightness Control)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)

Lets a display miniport driver reduce power to the display backlight and still smoothly adapt to changes in ambient light and user requests to change brightness.

Also see [Windows 8 brightness control for integrated displays](https://docs.microsoft.com/previous-versions/windows/hardware/design/dn614018(v=vs.85)).

### <span id="Microsoft_DirectX_Graphics_Infrastructure_DDI__DXGI_"></span><span id="microsoft_directx_graphics_infrastructure_ddi__dxgi_"></span><span id="MICROSOFT_DIRECTX_GRAPHICS_INFRASTRUCTURE_DDI__DXGI_"></span>Microsoft DirectX Graphics Infrastructure DDI (DXGI)

-   [*Blt1DXGI*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions)
-   [**DXGI\_DDI\_ARG\_BLT1**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi_ddi_arg_blt1)
-   [**DXGI\_DDI\_BASE\_ARGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi_ddi_base_args)
-   [**DXGI1\_2\_DDI\_BASE\_FUNCTIONS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions)

### <span id="Allocation_sharing___enqueing_GPU_events"></span><span id="allocation_sharing___enqueing_gpu_events"></span><span id="ALLOCATION_SHARING___ENQUEING_GPU_EVENTS"></span>Allocation sharing & enqueing GPU events

-   [*pfnCreateSynchronizationObject2Cb*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_createsynchronizationobject2cb)
-   [*pfnSignalSynchronizationObject2Cb*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_signalsynchronizationobject2cb)
-   [*pfnWaitForSynchronizationObject2Cb*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_waitforsynchronizationobject2cb)
-   [**D3DDDI\_DEVICECALLBACKS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_devicecallbacks)
-   [**D3DDDI\_SYNCHRONIZATIONOBJECT\_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dukmdt/ns-d3dukmdt-_d3dddi_synchronizationobject_flags)
-   [**D3DDDICB\_CREATESYNCHRONIZATIONOBJECT2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddicb_createsynchronizationobject2)
-   [**D3DDDICB\_SIGNALFLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dukmdt/ns-d3dukmdt-_d3dddicb_signalflags)
-   [**D3DDDICB\_SIGNALSYNCHRONIZATIONOBJECT2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddicb_signalsynchronizationobject2)
-   [**D3DDDICB\_WAITFORSYNCHRONIZATIONOBJECT2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddicb_waitforsynchronizationobject2)
-   [**D3DKMT\_CREATEALLOCATIONFLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_createallocationflags)
-   [**D3DKMT\_CREATEKEYEDMUTEX2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_createkeyedmutex2)
-   [**D3DKMT\_CREATEKEYEDMUTEX2\_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_createkeyedmutex2_flags)
-   [**D3DKMT\_RELEASEKEYEDMUTEX2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_releasekeyedmutex2)
-   [**D3DKMTShareObjects**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/nf-d3dkmthk-d3dkmtshareobjects)

### <span id="Cancel_command_interface"></span><span id="cancel_command_interface"></span><span id="CANCEL_COMMAND_INTERFACE"></span>Cancel command interface

-   [*DxgkDdiCancelCommand*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_cancelcommand)
-   [**DXGKARG\_CANCELCOMMAND**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgkarg_cancelcommand)
-   [**DXGK\_VIDSCHCAPS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps)

### <span id="Output_duplication"></span><span id="output_duplication"></span><span id="OUTPUT_DUPLICATION"></span>Output duplication

-   [**D3DKMTOutputDuplPresent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/nf-d3dkmthk-d3dkmtoutputduplpresent)
-   [**D3DKMTOutputDuplReleaseFrame**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/nf-d3dkmthk-d3dkmtoutputduplreleaseframe)
-   [**D3DKMT\_OUTPUTDUPL\_RELEASE\_FRAME**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_outputdupl_release_frame)
-   [**D3DKMT\_OUTPUTDUPL\_SNAPSHOT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_outputdupl_snapshot)
-   [**D3DKMT\_OUTPUTDUPLCONTEXTSCOUNT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_outputduplcontextscount)
-   [**D3DKMT\_OUTPUTDUPLPRESENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_outputduplpresent)
-   [**D3DKMT\_OUTPUTDUPLPRESENTFLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_outputduplpresentflags)
-   [**D3DKMT\_PRESENT\_RGNS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ns-d3dkmthk-_d3dkmt_present_rgns)

[**Windows 8 OpenGL Enhancements**](supporting-opengl-enhancements.md)

OpenGL installable client drivers (ICDs) can call new functions to control access to resources and to map between objects and identifiers.

 

 





