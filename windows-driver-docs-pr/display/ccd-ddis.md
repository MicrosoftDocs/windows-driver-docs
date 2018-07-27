---
title: CCD DDIs
description: CCD DDIs
ms.assetid: dde0e0b0-d6d0-4ca7-ae7e-427a650c080f
keywords:
- miniport drivers WDK display , Connecting and Configuring Displays (CCD)
- Connecting and Configuring Displays (CCD) WDK display
- CCD (Connecting and Configuring Displays) WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CCD DDIs


The Connecting and Configuring Displays (CCD) feature introduced with Windows 7 provides for improved display miniport driver control of display devices. The following reference topics describe the CCD device driver interfaces (DDIs) that are available to developers of display miniport drivers:

<span id="System-Implemented_Functions"></span><span id="system-implemented_functions"></span><span id="SYSTEM-IMPLEMENTED_FUNCTIONS"></span>**System-Implemented Functions**  
[**DXGK\_MONITOR\_INTERFACE\_V2::pfnGetAdditionalMonitorModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff561970)

[**DXGK\_MONITOR\_INTERFACE\_V2::pfnReleaseAdditionalMonitorModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff561977)

<span id="Driver-Implemented_Function"></span><span id="driver-implemented_function"></span><span id="DRIVER-IMPLEMENTED_FUNCTION"></span>**Driver-Implemented Function**
The following function must be implemented by display miniport drivers that support CCD:

[**DxgkDdiQueryVidPnHWCapability**](https://msdn.microsoft.com/library/windows/hardware/ff559771)

<span id="Structures"></span><span id="structures"></span><span id="STRUCTURES"></span>**Structures**
[**D3DKMDT\_VIDPN\_HW\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/ff546639)

[**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546712)

[**D3DKMT\_POLLDISPLAYCHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff548161)

[**D3DKMT\_RENDERFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff548244)

[**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_ASPECT\_RATIO**](https://msdn.microsoft.com/library/windows/hardware/ff554017)

[**DXGKARG\_QUERYVIDPNHWCAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/ff557628)

[**DXGK\_MONITOR\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff561968)

[**DXGK\_PRESENTATIONCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562004)

[**DXGK\_TARGETMODE\_DETAIL\_TIMING**](https://msdn.microsoft.com/library/windows/hardware/ff562060)

<span id="Enumerations"></span><span id="enumerations"></span><span id="ENUMERATIONS"></span>**Enumerations**
[**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING**](https://msdn.microsoft.com/library/windows/hardware/ff546706)

[**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_ASPECT\_RATIO**](https://msdn.microsoft.com/library/windows/hardware/ff554017)

[**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_SCANNING\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff554019)

[**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_STEREO\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff554023)

[**DISPLAYID\_DETAILED\_TIMING\_TYPE\_I\_SYNC\_POLARITY**](https://msdn.microsoft.com/library/windows/hardware/ff554026)

For more details on how to implement CCD in your display miniport driver, see the following topics:

[Obtaining Additional Monitor Target Modes](obtaining-additional-monitor-target-modes.md)

[Using Aspect Ratio and Custom Scaling Modes](using-aspect-ratio-and-custom-scaling-modes.md)

[System Calls to Recommend VidPN Topology](system-calls-to-recommend-vidpn-topology.md)

[ACPI Keyboard Shortcut Logic](acpi-keyboard-shortcut-logic.md)

[Querying VidPN Hardware Capabilities](querying-vidpnhardware-capabilities.md)

 

 





