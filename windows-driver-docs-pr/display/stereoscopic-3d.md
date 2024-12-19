---
title: Stereoscopic 3D
description: Windows 8 provides a consistent API and device driver interface (DDI) platform for stereoscopic 3-D scenarios such as gaming and video playback.
ms.date: 12/18/2024
---

# Supporting Stereoscopic 3D in Windows

Starting in Windows 8 (WDDM 1.2), a consistent API and DDI platform is available to support stereoscopic 3-D scenarios such as gaming and video playback.

* Driver implementation—Full graphics: Optional
* [WHCK](/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests: **Device.Graphics** ¦ **ProcessingStereoscopicVideoContent**; **Device.Display.Monitor.Stereoscopic3DModes**

Stereoscopic 3-D rendering is only enabled on systems that have all the components that are stereoscopic 3-D-capable. These components include 3-D-capable display hardware, graphics hardware, peripherals, and software applications.

The stereo design in the graphics stack is such that the particular visualization or display technology used is agnostic to the operating system. The kernel-mode display driver (KMD) communicates directly to the graphics display and has knowledge about the display capabilities through the standardized Extended Display Identification Data (EDID) structure. The KMD enumerates stereo capabilities only when it recognizes that such a display is connected to the system.

On Windows 8, the stereoscopic display setting is part of the **Screen Resolution** control panel, as shown here:

:::image type="content" source="images/stereo3ddisplaysetting.jpg" alt-text="Screenshot of the stereoscopic display setting in the Screen Resolution control panel on Windows 8.":::

The **Enable Stereo** setting is a checkbox with the following states:

* **Not available** (either grayed out or invisible): On systems incapable of rendering on stereo displays.
* Set to **Enabled** (checked): This is the default setting on systems capable of rendering on stereo displays and implies Stereo-On-Demand. By default, the Desktop Window Manager (DWM) is mono mode. DWM switches to stereo mode only when the user launches a stereo app (on-demand). The DWM can be in either mono or stereo mode when this checkbox is checked.
* Set to **Disabled** (unchecked): DWM is in mono mode if the user has unchecked this setting. Stereo applications present in mono mode in this case.

To implement stereo capabilities in your KMD and user-mode drivers, see the following lists of added or updated DDIs.

## Stereoscopic 3-D kernel-mode support

The following DDIs are updated for Windows 8 to support stereoscopic 3-D rendering on a VidPN.

* [**D3D11DDIARG_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddiarg_createresource)
* [**D3DDDI_ALLOCATIONINFO**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_allocationinfo)
* [**D3DKMDT_VIDPN_SOURCE_MODE_TYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_vidpn_source_mode_type)
* [**D3DKMT_PRESENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_presentflags)
* [**DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_arg_rotate_resource_identities)
* [**DXGK_PRESENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentflags)
* [**DXGK_SETVIDPNSOURCEADDRESS_FLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_setvidpnsourceaddress_flags)
* [**DXGKARG_OPENALLOCATION**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_openallocation)

## Stereoscopic 3-D swapchain DDIs

The following DDIs were added or updated for Windows 8 to support stereoscopic 3-D swapchains.

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

Stereo 3-D functionality can be enabled only on DirectX 10-capable hardware and higher. However, since Direct3D 11 APIs work on DirectX 9.x and 10.x hardware, all WDDM 1.2 drivers must support Direct3D 11 and be tested thoroughly to ensure that Direct3D 11 APIs work on all Windows 8 hardware.

Although stereoscopic 3-D is an optional WDDM 1.2 feature, Direct3D 11 API support is required on all Windows 8 hardware. Therefore, WDDM 1.2 drivers (Full Graphics and Render devices) must support Direct3D 11 APIs by adding support for cross-process sharing of texture arrays. This requirement ensures that stereo apps don't have failures in mono modes.

For more info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ Processing Stereoscopic Video Content** and **Device.Display.Monitor.Stereoscopic 3D Modes**.
