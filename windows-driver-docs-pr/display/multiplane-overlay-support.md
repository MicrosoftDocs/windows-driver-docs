---
title: MPO Support
description: Windows Display Driver Model (WDDM) 1.3 and later drivers can support multiplane overlays. This capability is available starting with Windows 8.1.
keywords:
- multiplane overlay support , WDDM , DirectX, Direct3D , DXGI, D3D
ms.date: 04/24/2025
ms.topic: concept-article
---

# Multiplane overlay support

This article describes the multiplane overlay (MPO) feature introduced in Windows 8.1 (WDDM 1.3). It lists the system-supplied and driver-implemented functions used to support this feature in a user-mode display driver (UMD) and a kernel-mode display miniport driver (KMD) in WDDM 1.3 and later. It also lists the structures and enumerations that are used with MPOs.

MPO support allows graphics hardware to compose multiple layers of content into a single image that it can then display on a screen. It's essentially a hardware-accelerated method of compositing different *planes* of content without having to involve the CPU or use up other system resources to do the blending in software. A plane can be a video, the desktop, an application window, and so on. The hardware can then take these planes and combine them into a single image that is sent to the display.

## MPO functions called by user-mode display drivers

The following table lists user-mode MPO functions that the operating system implements and that user-mode display drivers (UMDs) can call.

| Function | Description |
| -------- | ----------- |
| [D3D: pfnPresentMultiPlaneOverlayCb](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_presentmultiplaneoverlaycb) | Copies content from a source MPO allocation to a destination allocation. |
| [DXGI: pfnPresentMultiPlaneOverlayCb](/windows-hardware/drivers/ddi/dxgiddi/nc-dxgiddi-pfnddxgiddi_present_multiplane_overlaycb) | Copies content from a source MPO allocation to a destination allocation. |

## MPO functions implemented by the UMD

This section contains functions that a WDDM 1.3 and later UMD must implement in order to support MPOs.

* Direct3D: The UMD supplies pointers to D3D MPO functions through members of the [D3DDDI_DEVICEFUNCS](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) structure in a call to the UMD's [CreateDevice](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function.

* DXGI: The UMD supplies pointers to DXGI MPO functions through members of the [DXGI1_3_DDI_BASE_FUNCTIONS](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions) structure when its adapter-specific [CreateDevice(D3D10)](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function is called. For more info, see [Supporting the DXGI DDI](supporting-the-dxgi-ddi.md).

The following table lists the functions that a UMD must implement in order to support MPOs.

| Function | Description |
| -------- | ----------- |
| [pfnCheckMultiPlaneOverlaySupport (D3D)](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_checkmultiplaneoverlaysupport) | Called by the D3D runtime to check the details on hardware support for MPOs.|
| [pfnCheckMultiPlaneOverlaySupport (DXGI)](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions) | Called by the DirectX Graphics Infrastructure (DXGI) runtime to check the details on hardware support for MPOs.|
| [pfnPresentMultiplaneOverlay (D3D)](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_presentmultiplaneoverlay) | Called by the D3D runtime to notify the UMD that an application finished rendering and request that the UMD display the source surface. The driver should display this surface by copying, flipping, or performing a color-fill operation. |
| [pfnPresentMultiplaneOverlay (DXGI)](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions) | Called by the DXGI runtime to notify the UMD that an application finished rendering and requests that the UMD display the source surface. The UMD should display the surface by copying, flipping, or performing a color-fill operation. |

The following table lists the DXGI DDI functions that a UMD can optionally implement.

| Function | Description |
| -------- | ----------- |
| [pfnGetMultiPlaneOverlayCaps](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions) | Called by the DXGI runtime to request that the UMD get basic overlay plane capabilities. |
| [pfnGetMultiplaneOverlayGroupCaps](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions) | Called by the DXGI runtime to request that the UMD get a group of overlay plane capabilities. |

## MPO user-mode structures and enumerations

This section lists the user-mode structures and enumerations that are used with MPO DDIs.

| Struct/Enum | Description |
| ----------- | ----------- |
| [D3DDDI_MULTIPLANE_ALLOCATION_INFO](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddi_multiplane_overlay_allocation_info) |Specifies info about an MPO allocation.|
| [D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_multiplane_overlay_attributes) | Used by the UMD to specify overlay plane attributes.|
| [D3DDDI_MULTIPLANE_OVERLAY_BLEND](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddi_multiplane_overlay_blend) | Identifies a blend operation to be performed on an overlay plane.|
| [D3DDDI_MULTIPLANE_OVERLAY_CAPS](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddi_multiplane_overlay_caps) | Used by the UMD to specify overlay plane capabilities.|
| [D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddi_multiplane_overlay_feature_caps) | Identifies overlay capabilities.|
| [D3DDDI_MULTIPLANE_OVERLAY_FLAGS](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddi_multiplane_overlay_flags) | Identifies a flip operation to be performed on an overlay plane.|
| [D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddi_multiplane_overlay_group_caps) | Used by the UMD to specify a group of overlay plane capabilities.|
| [D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS_INPUT](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddi_multiplane_overlay_group_caps_input) | Specifies info on an MPO capability group.|
| [D3DDDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-d3dddi_multiplane_overlay_stretch_quality) | Identifies filtering processes that the hardware should perform when it stretches or shrinks MPO data. |
| [D3DDDI_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-d3dddi_multiplane_overlay_video_frame_format) |Identifies the overlay plane's video frame format. Only the D3DDDI_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE value is supported.|
| [D3DDDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-d3dddi_multiplane_overlay_ycbcr_flags) | Identifies YUV range and conversion info that describes an MPO.|
| [D3DDDI_PRESENT_MULTIPLANE_OVERLAY](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_present_multiplane_overlay) | Specifies an overlay plane to display.|
| [D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_checkmultiplaneoverlaysupport) | Used in a call to the pfnCheckMultiPlaneOverlaySupport (D3D) function to check details on hardware support for MPOs.|
| [D3DDDIARG_PRESENTMULTIPLANEOVERLAY](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddiarg_presentmultiplaneoverlay) | Specifies an MPO resource to display.|
| [D3DDDICB_PRESENTMULTIPLANEOVERLAY](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddicb_presentmultiplaneoverlay) | Describes MPO allocations that content is copied to and from.|

## MPO kernel-mode driver-implemented functions

The following table lists the MPO functions that the kernel-mode display miniport driver (KMD) implements.

|Function|Description|
|:--|:--|
| [DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport) | Called by the DirectX graphics kernel subsystem to check the details of hardware support for MPOs.|
| [DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3) | The following function is called to determine whether a specific multi-plane overlay configuration is supported.|
| [DXGKDDI_GETMULTIPLANEOVERLAYCAPS](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getmultiplaneoverlaycaps) | Called to retrieve MPO capabilities. Support for this DDI is required for any WDDM 2.2 KMD that wants to support multiple planes.|
| [DXGKDDI_POSTMULTIPLANEOVERLAYPRESENT](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_postmultiplaneoverlaypresent) | Called after a new multi-plane overlay configuration takes effect, allowing the KMD to optimize hardware state. Optional for WDDM 1.3 or later KMDs that support multi-plane overlays.|
| [DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay3) | Called to change the overlay configuration being displayed.|
| [DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT2](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport2) | DxgkDdiCheckMultiPlaneOverlaySupport2 is called to determine whether a specific multi-plane overlay configuration is supported. |
| [DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay) |Sets the addresses of multiple surfaces that are associated with a particular video present source. These surfaces include the Desktop Window Manager (DWM)'s swapchain. This function is used to present multiple surfaces (including the DWM’s swapchain) to the screen.|
| [DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay2) | DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 is called to change the overlay configuration being displayed.|

## MPO kernel-mode structures

The following table lists the structures that KMD uses.

|Structure|Description|
|:--|:--|
| [DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_check_multiplane_overlay_support_plane) | Specifies the support attributes that the hardware provides for MPOs.|
| [DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_check_multiplane_overlay_support_return_info) | Specifies limitations on hardware support of MPOs.|
| [DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_attributes) | Used by the KMD to specify overlay plane attributes.|
| [DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_attributes2) |DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 is used by the KMD to specify overlay plane attributes. |
| [DXGK_MULTIPLANE_OVERLAY_BLEND](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_blend) | Identifies a blend operation to be performed on an overlay plane.|
| [DXGK_MULTIPLANE_OVERLAY_FLAGS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_flags) | Identifies a flip operation to be performed on an overlay plane.|
| [DXGK_MULTIPLANE_OVERLAY_PLANE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_plane) | Specifies an overlay plane to display in a call to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay function.|
| [DXGK_MULTIPLANE_OVERLAY_PLANE2](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_plane2) |DXGK_MULTIPLANE_OVERLAY_PLANE2 is used with the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to specify an overlay plane to display.|
| [DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_plane_with_source) |DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE describes the multi-plane overlay plane attributes, allocation, and video present network source identification number.|
| [DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_vsync_info) |Specifies an overlay plane to display during a VSync interval.|
| [DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_ycbcr_flags) |Identifies YUV range and conversion info that describes an MPO.|
| [DXGK_PRESENTMULTIPLANEOVERLAYINFO](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentmultiplaneoverlayinfo) |Specifies info on a VidPN input and an overlay plane to display.|
| [DXGK_PRESENTMULTIPLANEOVERLAYLIST](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentmultiplaneoverlaylist) |Specifies an overlay plane to display in a call to the DxgkDdiPresent function.|
| [DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_checkmultiplaneoverlaysupport) |Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport function to check details on hardware support for MPOs.|
| [DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_checkmultiplaneoverlaysupport2) |DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 is passed to the DxgkDdiCheckMultiPlaneOverlaySupport2 function to determine whether a specific multi-plane overlay configuration is supported.|
| [DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay) |Contains arguments for the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay function.|
| [DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay2) |DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 is passed to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to change the overlay configuration being displayed.|

## MPO kernel-mode enumerations

The following table lists the enumerations used by KMD.

| Enumeration | Description |
| ----------- | ----------- |
| [DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_multiplane_overlay_stereo_flip_mode) |Identifies the overlay plane's stereo flip mode. Only the DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE value is supported. |
| [DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_multiplane_overlay_stereo_format) |Identifies the overlay plane's stereo presentation format. Only the DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO value is supported.|
| [DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_multiplane_overlay_stretch_quality) |Identifies filtering processes that the hardware should perform when it stretches or shrinks MPO data.|
| [DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_multiplane_overlay_video_frame_format) |Identifies the overlay plane's video frame format. Only the DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE value is supported.|

The **D3DDDICAPS_GET_MULTIPLANE_OVERLAY_GROUP_CAPS** value in [**D3DDDICAPS_TYPE**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddicaps_type) indicates UMD support for MPOs.
