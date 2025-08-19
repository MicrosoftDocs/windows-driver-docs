---
title: Stereoscopic 3D
description: Stereoscopic 3D support is available starting on Windows 8 (WDDM 1.2).
ms.keywords:
- Windows, 3D stereo, driver support, WDK
- 3D stereoscopic support, WDK , Windows, Direct3D
- 3D stereoscopic support, gaming and video playback
ms.date: 03/17/2025
ms.topic: concept-article
---

# Supporting stereoscopic 3D in Windows drivers

Starting in Windows 8 (WDDM 1.2), graphics drivers can support stereoscopic 3D rendering to support scenarios such as gaming and video playback.

Stereoscopic 3D rendering is only enabled on systems that have the necessary stereoscopic 3D-capable components. These components include 3D-capable display hardware, graphics hardware, peripherals, and software applications. The user interface settings are available in the **Display Settings** control panel only if the system has all the necessary components.

* Driver implementation—Full graphics: Optional
* [WHLK](/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests: **Device.Graphics** ¦ **ProcessingStereoscopicVideoContent**; **Device.Display.Monitor.Stereoscopic3DModes** (DX11 3DStereoVideo)

The stereo design in the graphics stack is such that the particular visualization or display technology used is agnostic to the operating system. The kernel-mode display driver (KMD) communicates directly with the graphics display and has knowledge about the display capabilities through the standardized Extended Display Identification Data (EDID) structure. The KMD enumerates stereo capabilities only when it recognizes that such a display is connected to the system.

To implement stereo capabilities in your KMD and user-mode drivers, see the following lists of added or updated DDIs.

## Stereoscopic 3D kernel-mode support

The following DDIs were updated to support stereoscopic 3D rendering on a VidPN.

* [**D3D11DDIARG_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddiarg_createresource)
* [**D3DDDI_ALLOCATIONINFO**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_allocationinfo)
* [**D3DKMDT_VIDPN_SOURCE_MODE_TYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_vidpn_source_mode_type)
* [**D3DKMT_PRESENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_presentflags)
* [**DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_arg_rotate_resource_identities)
* [**DXGK_PRESENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentflags)
* [**DXGK_SETVIDPNSOURCEADDRESS_FLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_setvidpnsourceaddress_flags)
* [**DXGKARG_OPENALLOCATION**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_openallocation)

## Stereoscopic 3D swapchain DDIs

The following DDIs were added or updated to support stereoscopic 3D swapchains.

* [*BltDXGI*](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_functions)
* [*Blt1DXGI*](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions)
* [*CreateResource(D3D10)*](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createresource)
* [*CreateResource(D3D11)*](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createresource)
* [*RotateResourceIdentitiesDXGI*](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_functions)
* [**D3DDDI_ALLOCATIONINFO**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_allocationinfo)
* [**D3D10DDIARG_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createresource)
* [**D3D11DDIARG_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddiarg_createresource)
* [**DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_arg_rotate_resource_identities)
* [**DXGI_DDI_PRESENT_FLAGS**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_present_flags)
* [**DXGI_DDI_PRIMARY_DESC**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_primary_desc)

## Hardware certification requirements

System builders are encouraged to test their stereo driver packages by using the settings described in this article to ensure correct functionality.

Stereo 3D functionality can be enabled on DirectX 10-capable hardware and higher. However, since Direct3D 11 APIs work on DirectX 9.x and 10.x hardware, all WDDM 1.2 drivers must support Direct3D 11. To that end, they must be tested thoroughly to ensure that Direct3D 11 APIs work on all Windows 8 and later hardware.

Although stereoscopic 3D is an optional WDDM 1.2 feature, Direct3D 11 API support is required starting on all Windows 8+ hardware. Therefore, WDDM 1.2 drivers (Full Graphics and Render devices) must support Direct3D 11 APIs by adding support for cross-process sharing of texture arrays. This requirement ensures that stereo apps don't have failures in mono modes.

For more info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ Processing Stereoscopic Video Content** and **Device.Display.Monitor.Stereoscopic 3D Modes**.
