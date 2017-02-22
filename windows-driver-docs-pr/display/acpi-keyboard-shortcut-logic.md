---
title: ACPI Keyboard Shortcut Logic
description: ACPI Keyboard Shortcut Logic
ms.assetid: cd62380b-1393-403e-b0e6-c52f60c06936
keywords: ["ACPI hotkeys WDK display"]
---

# ACPI Keyboard Shortcut Logic


Beginning with Windows 7, IHVs implement ACPI-based OEM-specific keyboard shortcuts. The operating system is unaware of these keyboard shortcuts. On Windows 7, OEMs must use the CCD database to store and apply keyboard shortcuts so that the operating system and any OEM applications are aware of each other.

The behavior of calls to the following functions has changed for drivers running on Windows 7:

<span id="DxgkDdiNotifyAcpiEvent_and_DxgkDdiRecommendFunctionalVidPn"></span><span id="dxgkddinotifyacpievent_and_dxgkddirecommendfunctionalvidpn"></span><span id="DXGKDDINOTIFYACPIEVENT_AND_DXGKDDIRECOMMENDFUNCTIONALVIDPN"></span>[*DxgkDdiNotifyAcpiEvent*](https://msdn.microsoft.com/library/windows/hardware/ff559695) and [*DxgkDdiRecommendFunctionalVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559775)  
-   If the display miniport driver receives a call to the [*DxgkDdiNotifyAcpiEvent*](https://msdn.microsoft.com/library/windows/hardware/ff559695) function with the DXGK\_ACPI\_CHANGE\_DISPLAY\_MODE flag set in the *AcpiFlags* parameter, DMM calls the [*DxgkDdiRecommendFunctionalVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559775) function to obtain the new VidPN and to compare against the current client VidPN. If the topology of the two VidPNs is the same, DMM does not modify the new VidPN. Otherwise, DMM removes mode information from the VidPN, leaving just the topology, and allows the CCD database to determine the modes for the given topology. DMM then sets the display configuration based on the new VidPN.

<span id="D3DKMTInvalidateActiveVidPn"></span><span id="d3dkmtinvalidateactivevidpn"></span><span id="D3DKMTINVALIDATEACTIVEVIDPN"></span>[**D3DKMTInvalidateActiveVidPn**](https://msdn.microsoft.com/library/windows/hardware/ff547023)  
-   This function is supported on Windows Vista and later for display miniport drivers with version &lt; DXGKDDI\_INTERFACE\_VERSION\_WIN7. Function behavior is identical to the behavior on Windows Vista.

-   This function is not supported on Windows 7 and later for display miniport drivers with version &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN7. If called, the status code STATUS\_NOT\_SUPPORTED is returned.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20ACPI%20Keyboard%20Shortcut%20Logic%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




