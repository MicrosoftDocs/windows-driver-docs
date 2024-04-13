---
title: CCD DDIs
description: CCD DDIs
keywords:
- miniport drivers WDK display , Connecting and Configuring Displays (CCD)
- Connecting and Configuring Displays (CCD) WDK display
- CCD (Connecting and Configuring Displays) WDK display
ms.date: 03/18/2022
---

# CCD DDIs

The Connecting and Configuring Displays (CCD) feature introduced in Windows 7 provides for improved display miniport driver control of display devices.

The following reference topics describe the CCD device driver interfaces (DDIs) that are available to developers of display miniport drivers.

* System-Implemented Functions:

  * [**DXGK_MONITOR_INTERFACE_V2::pfnGetAdditionalMonitorModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_getadditionalmonitormodeset)
  * [**DXGK_MONITOR_INTERFACE_V2::pfnReleaseAdditionalMonitorModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_releaseadditionalmonitormodeset)

* Driver-Implemented Function:

  * [**DxgkDdiQueryVidPnHWCapability**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryvidpnhwcapability). A display miniport driver that supports CCD must implement this function.

* Relevant structures:

  * [**D3DKMDT_VIDPN_HW_CAPABILITY**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_hw_capability)
  * [**D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path_scaling_support)
  * [**D3DKMT_POLLDISPLAYCHILDREN**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_polldisplaychildren)
  * [**D3DKMT_RENDERFLAGS**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_renderflags)
  * [**DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_aspect_ratio)
  * [**DXGKARG_QUERYVIDPNHWCAPABILITY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryvidpnhwcapability)
  * [**DXGK_MONITOR_INTERFACE_V2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitor_interface_v2)
  * [**DXGK_PRESENTATIONCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentationcaps)
  * [**DXGK_TARGETMODE_DETAIL_TIMING**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_targetmode_detail_timing)

* Relevant Enumerations:

  * [**D3DKMDT_VIDPN_PRESENT_PATH_SCALING**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_vidpn_present_path_scaling)
  * [**DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_aspect_ratio)
  * [**DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_scanning_mode)
  * [**DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_stereo_mode)
  * [**DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_sync_polarity)

For more details on how to implement CCD in your display miniport driver, see the following topics:

[Obtaining Additional Monitor Target Modes](obtaining-additional-monitor-target-modes.md)

[Using Aspect Ratio and Custom Scaling Modes](using-aspect-ratio-and-custom-scaling-modes.md)

[System Calls to Recommend VidPN Topology](system-calls-to-recommend-vidpn-topology.md)

[ACPI Keyboard Shortcut Logic](acpi-keyboard-shortcut-logic.md)

[Querying VidPN Hardware Capabilities](querying-vidpnhardware-capabilities.md)
