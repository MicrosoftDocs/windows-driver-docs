---
title: ACPI Keyboard Shortcut Logic
description: ACPI Keyboard Shortcut Logic
keywords:
- ACPI hotkeys WDK display
ms.date: 04/20/2017
---

# ACPI Keyboard Shortcut Logic


Beginning with Windows 7, IHVs implement ACPI-based OEM-specific keyboard shortcuts. The operating system is unaware of these keyboard shortcuts. On Windows 7, OEMs must use the CCD database to store and apply keyboard shortcuts so that the operating system and any OEM applications are aware of each other.

The behavior of calls to the following functions has changed for drivers running on Windows 7:

<span id="DxgkDdiNotifyAcpiEvent_and_DxgkDdiRecommendFunctionalVidPn"></span><span id="dxgkddinotifyacpievent_and_dxgkddirecommendfunctionalvidpn"></span><span id="DXGKDDINOTIFYACPIEVENT_AND_DXGKDDIRECOMMENDFUNCTIONALVIDPN"></span>[*DxgkDdiNotifyAcpiEvent*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_acpi_event) and [*DxgkDdiRecommendFunctionalVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendfunctionalvidpn)  
-   If the display miniport driver receives a call to the [*DxgkDdiNotifyAcpiEvent*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_acpi_event) function with the DXGK\_ACPI\_CHANGE\_DISPLAY\_MODE flag set in the *AcpiFlags* parameter, DMM calls the [*DxgkDdiRecommendFunctionalVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendfunctionalvidpn) function to obtain the new VidPN and to compare against the current client VidPN. If the topology of the two VidPNs is the same, DMM does not modify the new VidPN. Otherwise, DMM removes mode information from the VidPN, leaving just the topology, and allows the CCD database to determine the modes for the given topology. DMM then sets the display configuration based on the new VidPN.

<span id="D3DKMTInvalidateActiveVidPn"></span><span id="d3dkmtinvalidateactivevidpn"></span><span id="D3DKMTINVALIDATEACTIVEVIDPN"></span>[**D3DKMTInvalidateActiveVidPn**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtinvalidateactivevidpn)  
-   This function is supported on Windows Vista and later for display miniport drivers with version &lt; DXGKDDI\_INTERFACE\_VERSION\_WIN7. Function behavior is identical to the behavior on Windows Vista.

-   This function is not supported on Windows 7 and later for display miniport drivers with version &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN7. If called, the status code STATUS\_NOT\_SUPPORTED is returned.

 

