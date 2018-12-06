---
title: Multiplane overlay support
description: Multiplane overlays can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.
ms.assetid: 8B2F5497-554D-4D4A-B44E-985A9F89143D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiplane overlay support


Multiplane overlays can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.

These sections describe how to implement this capability in your driver.

## Multiplane overlay functions called by user-mode display drivers

All user-mode multiplane overlay functions that the operating system implements.

| Function | Description |
|:--|:--|
|[pfnPresentMultiPlaneOverlayCb (D3D)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_presentmultiplaneoverlaycb)|Copies content from a source multiplane overlay allocation to a destination allocation. Can be called by Windows Display Driver Model (WDDM) 1.3 or later user-mode display drivers.|
|[pfnPresentMultiPlaneOverlayCb (DXGI)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/nc-dxgiddi-pfnddxgiddi_present_multiplane_overlaycb)|Copies content from a source multiplane overlay allocation to a destination allocation. Can be called by WDDM 1.3 or later user-mode display drivers.|

## Multiplane overlay functions implemented by the user-mode driver

This section contains functions that a Windows Display Driver Model (WDDM) 1.3 and later user-mode display driver must implement in order to support multiplane overlays.

The driver supplies pointers to DXGI multiplane overlay functions through members of the [DXGI1_3_DDI_BASE_FUNCTIONS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function. For more info, see [Supporting the DXGI DDI](supporting-the-dxgi-ddi.md).

The driver supplies pointers to Microsoft Direct3D multiplane overlay functions through members of the [D3DDDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) structure in a call to the driver's [CreateDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function.

All functions that a user-mode driver must implement in order to support multiplane overlays.

| Function | Description |
|:--|:--|
|[pfnCheckMultiPlaneOverlaySupport (D3D)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_checkmultiplaneoverlaysupport)| Called by the Direct3D runtime to check the details on hardware support for multiplane overlays.|
|[pfnCheckMultiPlaneOverlaySupport (DXGI)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions)| Called by the Microsoft DirectX Graphics Infrastructure (DXGI) runtime to check the details on hardware support for multiplane overlays.|
|[pfnGetMultiPlaneOverlayCaps](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions)| Called by the DXGI runtime to request that the user-mode display driver get basic overlay plane capabilities. Optionally implemented by WDDM 1.3 and later user-mode display drivers.|
|[pfnGetMultiplaneOverlayGroupCaps](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions)| Called by the DXGI runtime to request that the user-mode display driver get a group of overlay plane capabilities. Optionally implemented by WDDM 1.3 and later user-mode display drivers.|
|[pfnPresentMultiplaneOverlay (D3D)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_presentmultiplaneoverlay)| Called by the Direct3D runtime to notify the user-mode display driver that an application finished rendering and requests that the driver display the source surface by either copying or flipping or that the driver perform a color-fill operation. Must be implemented by WDDM 1.3 or later drivers that support multiplane overlays.|
|[pfnPresentMultiplaneOverlay (DXGI)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions)| Called by the DXGI runtime to notify the user-mode display driver that an application finished rendering and requests that the driver display the source surface by either copying or flipping or that the driver perform a color-fill operation. Must be implemented by WDDM 1.3 or later drivers that support multiplane overlays.|
 
## Multiplane overlay user-mode structures and enumerations

All user-mode structures and enumerations that are used with multiplane overlay device driver interfaces (DDIs).

| DDI | Description |
|:--|:--|
|[D3DDDI_MULTIPLANE_ALLOCATION_INFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-d3dddi_multiplane_overlay_allocation_info)|Specifies info about a multiplane overlay allocation.|
|[D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_multiplane_overlay_attributes)| Used by the user-mode display driver to specify overlay plane attributes.|
|[D3DDDI_MULTIPLANE_OVERLAY_BLEND](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ne-d3dumddi-_d3dddi_multiplane_overlay_blend)| Identifies a blend operation to be performed on an overlay plane.|
|[D3DDDI_MULTIPLANE_OVERLAY_CAPS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-d3dddi_multiplane_overlay_caps)| Used by the user-mode display driver to specify overlay plane capabilities.|
|[D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ne-d3dumddi-_d3dddi_multiplane_overlay_feature_caps)| Identifies overlay capabilities.|
|[D3DDDI_MULTIPLANE_OVERLAY_FLAGS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ne-d3dumddi-_d3dddi_multiplane_overlay_flags)| Identifies a flip operation to be performed on an overlay plane.|
|[D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-d3dddi_multiplane_overlay_group_caps)| Used by the user-mode display driver to specify a group of overlay plane capabilities.|
|[D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-d3dddi_multiplane_overlay_group_caps_input)| Specifies info on a multiplane overlay capability group.|
|[D3DDDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ne-d3dumddi-d3dddi_multiplane_overlay_stretch_quality)| Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data.
|[D3DDDI_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ne-d3dumddi-d3dddi_multiplane_overlay_video_frame_format)|Identifies the overlay plane's video frame format. Only the D3DDDI_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE value is supported.|
|[D3DDDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ne-d3dumddi-d3dddi_multiplane_overlay_ycbcr_flags)| Identifies YUV range and conversion info that describes a multiplane overlay.|
|[D3DDDI_PRESENT_MULTIPLANE_OVERLAY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_present_multiplane_overlay)| Specifies an overlay plane to display.|
|[D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddiarg_checkmultiplaneoverlaysupport)| Used in a call to the pfnCheckMultiPlaneOverlaySupport (D3D) function to check details on hardware support for multiplane overlays.|
|[D3DDDIARG_PRESENTMULTIPLANEOVERLAY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-d3dddiarg_presentmultiplaneoverlay)| Specifies a multiplane overlay resource to display.|
|[D3DDDICB_PRESENTMULTIPLANEOVERLAY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-d3dddicb_presentmultiplaneoverlay)| Describes multiplane overlay allocations that content is copied to and from.|
 
## Multiplane overlay kernel-mode driver-implemented functions

All multiplane overlay functions that the display miniport driver implements.

|Function|Description|
|:--|:--|
|[DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport)| Called by the Microsoft DirectX graphics kernel subsystem to check the details of hardware support for multiplane overlays.|
|[DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3)| The following new function is called to determine whether a specific multi-plane overlay configuration is supported.|
|[DXGKDDI_GETMULTIPLANEOVERLAYCAPS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_getmultiplaneoverlaycaps)| Called to retrieve multiplane overlay capabilities. Support for this DDI is required for any WDDM 2.2 driver that wants to support multiple planes.|
|[DXGKDDI_POSTMULTIPLANEOVERLAYPRESENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_postmultiplaneoverlaypresent)| Called after a new multi-plane overlay configuration has taken effect, allowing the driver to optimize hardware state. Optional for Windows Display Driver Model (WDDM) 2.0 or later drivers that support multi-plane overlays.|
|[DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay3)|Called to change the overlay configuration being displayed.|
|[DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport2)|DxgkDdiCheckMultiPlaneOverlaySupport2 is called to determine whether a specific multi-plane overlay configuration is supported. |
|[DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay)|Sets the addresses of multiple surfaces, including the Desktop Window Manager (DWM)'s swapchain, that are associated with a particular video present source. This function is used to present multiple surfaces (including the DWM’s swapchain) to the screen.|
|[DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay2)| DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 is called to change the overlay configuration being displayed.|

## Multiplane overlay kernel-mode structures

All structures that are used by the display miniport driver.

|Structure|Description|
|:--|:--|
|[DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_check_multiplane_overlay_support_plane)| Specifies the support attributes that the hardware provides for multiplane overlays.|
|[DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-dxgk_check_multiplane_overlay_support_return_info)| Specifies limitations on hardware support of multiplane overlays.|
|[DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_attributes)| Used by the display miniport driver to specify overlay plane attributes.|
|[DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_attributes2)|DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 is used by the display miniport driver to specify overlay plane attributes. |
|[DXGK_MULTIPLANE_OVERLAY_BLEND](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_blend)| Identifies a blend operation to be performed on an overlay plane.|
|[DXGK_MULTIPLANE_OVERLAY_FLAGS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_flags)| Identifies a flip operation to be performed on an overlay plane.|
|[DXGK_MULTIPLANE_OVERLAY_PLANE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_plane)| Specifies an overlay plane to display in a call to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay function.|
|[DXGK_MULTIPLANE_OVERLAY_PLANE2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_plane2)|DXGK_MULTIPLANE_OVERLAY_PLANE2 is used with the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to specify an overlay plane to display.|
|[DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_plane_with_source)|DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE describes the multi-plane overlay plane attributes, allocation, and video present network source identification number.|
|[DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_vsync_info)|Specifies an overlay plane to display during a VSync interval.|
|[DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_ycbcr_flags)|Identifies YUV range and conversion info that describes a multiplane overlay.|
|[DXGK_PRESENTMULTIPLANEOVERLAYINFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_presentmultiplaneoverlayinfo)|Specifies info on a VidPN input and an overlay plane to display.|
|[DXGK_PRESENTMULTIPLANEOVERLAYLIST](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_presentmultiplaneoverlaylist)|Specifies an overlay plane to display in a call to the DxgkDdiPresent function.|
|[DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgkarg_checkmultiplaneoverlaysupport)|Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport function to check details on hardware support for multiplane overlays.|
|[DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgkarg_checkmultiplaneoverlaysupport2)|DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 is passed to the DxgkDdiCheckMultiPlaneOverlaySupport2 function to determine whether a specific multi-plane overlay configuration is supported.|
|[DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay)|Contains arguments for the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay function.|
|[DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay2)|DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 is passed to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to change the overlay configuration being displayed.|
 

## Multiplane overlay kernel-mode enumerations

All enumerations that are used by the display miniport driver.

| Enumeration | Description |
|:--|:--|
|[DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ne-d3dkmddi-_dxgk_multiplane_overlay_stereo_flip_mode)|Identifies the overlay plane's stereo flip mode. Only the DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE value is supported. |
|[DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ne-d3dkmddi-_dxgk_multiplane_overlay_stereo_format)|Identifies the overlay plane's stereo presentation format. Only the DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO value is supported.|
|[DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ne-d3dkmddi-_dxgk_multiplane_overlay_stretch_quality)|Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data.|
|[DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ne-d3dkmddi-_dxgk_multiplane_overlay_video_frame_format)|Identifies the overlay plane's video frame format. Only the DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE value is supported.|
 

This user-mode enumeration constant value supports multiplane overlays and is new for Windows 8.1:

-   [**D3DDDICAPS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff544132) (**D3DDDICAPS\_GET\_MULTIPLANE\_OVERLAY\_GROUP\_CAPS** constant value)

 

 





