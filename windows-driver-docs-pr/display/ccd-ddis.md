---
title: CCD DDIs
description: CCD DDIs
ms.assetid: dde0e0b0-d6d0-4ca7-ae7e-427a650c080f
keywords:
- miniport drivers WDK display , Connecting and Configuring Displays (CCD)
- Connecting and Configuring Displays (CCD) WDK display
- CCD (Connecting and Configuring Displays) WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20CCD%20DDIs%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




