---
title: CCD DDIs
description: CCD DDIs
keywords:
- miniport drivers WDK display , Connecting and Configuring Displays (CCD)
- Connecting and Configuring Displays (CCD) WDK display
- CCD (Connecting and Configuring Displays) WDK display
ms.date: 10/11/2018
---

# CCD DDIs


The Connecting and Configuring Displays (CCD) feature introduced with Windows 7 provides for improved display miniport driver control of display devices. 

## CCD DDIs for Display Miniport Drivers

The following reference topics describe the CCD device driver interfaces (DDIs) that are available to developers of display miniport drivers:

<span id="System-Implemented_Functions"></span><span id="system-implemented_functions"></span><span id="SYSTEM-IMPLEMENTED_FUNCTIONS"></span>**System-Implemented Functions**  

**[**DXGK\_MONITOR\_INTERFACE\_V2::pfnGetAdditionalMonitorModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_getadditionalmonitormodeset)**: [**DXGK\_MONITOR\_INTERFACE\_V2::pfnReleaseAdditionalMonitorModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_releaseadditionalmonitormodeset)


<span id="Driver-Implemented_Function"></span><span id="driver-implemented_function"></span><span id="DRIVER-IMPLEMENTED_FUNCTION"></span>**Driver-Implemented Function**

The following function must be implemented by display miniport drivers that support CCD:

[**DxgkDdiQueryVidPnHWCapability**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryvidpnhwcapability)

<span id="Structures"></span><span id="structures"></span><span id="STRUCTURES"></span>**Structures**

**[**D3DKMDT\_VIDPN\_HW\_CAPABILITY**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_hw_capability)**: [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path_scaling_support)

**[**D3DKMT\_POLLDISPLAYCHILDREN**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_polldisplaychildren)**: [**D3DKMT\_RENDERFLAGS**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_renderflags)

**[**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_ASPECT\_RATIO**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_aspect_ratio)**: [**DXGKARG\_QUERYVIDPNHWCAPABILITY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryvidpnhwcapability)

**[**DXGK\_MONITOR\_INTERFACE\_V2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitor_interface_v2)**: [**DXGK\_PRESENTATIONCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentationcaps)

**[**DXGK\_TARGETMODE\_DETAIL\_TIMING**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_targetmode_detail_timing)**: 


<span id="Enumerations"></span><span id="enumerations"></span><span id="ENUMERATIONS"></span>**Enumerations**

**[**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_vidpn_present_path_scaling)**: [**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_ASPECT\_RATIO**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_aspect_ratio)

**[**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_SCANNING\_MODE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_scanning_mode)**: [**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_STEREO\_MODE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_stereo_mode)

**[**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_SYNC\_POLARITY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_displayid_detailed_timing_type_i_sync_polarity)**: 



For more details on how to implement CCD in your display miniport driver, see the following topics:

[Obtaining Additional Monitor Target Modes](obtaining-additional-monitor-target-modes.md)

[Using Aspect Ratio and Custom Scaling Modes](using-aspect-ratio-and-custom-scaling-modes.md)

[System Calls to Recommend VidPN Topology](system-calls-to-recommend-vidpn-topology.md)

[ACPI Keyboard Shortcut Logic](acpi-keyboard-shortcut-logic.md)

[Querying VidPN Hardware Capabilities](querying-vidpnhardware-capabilities.md)
