---
title: Required Display Driver Functions
description: Required Display Driver Functions
keywords:
- graphics DDI functions WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required Display Driver Functions


## <span id="ddk_required_display_driver_functions_gg"></span><span id="DDK_REQUIRED_DISPLAY_DRIVER_FUNCTIONS_GG"></span>


At a minimum, every display driver must:

1.  Enable and disable the graphics hardware.

2.  Supply GDI with information about hardware capabilities.

3.  Enable the drawing surface.

The following table lists the functions that all display drivers must implement. Following **DrvEnableDriver**, the remaining functions are listed alphabetically. Note that except for **DrvEnableDriver**, which GDI calls by name, all other display driver functions do not have fixed names, and are listed with pseudonames.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvenabledriver" data-raw-source="[&lt;strong&gt;DrvEnableDriver&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvenabledriver)"><strong>DrvEnableDriver</strong></a></p></td>
<td align="left"><p>As the initial driver entry point, provides GDI with the driver version number and entry points of optional functions supported.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvassertmode" data-raw-source="[&lt;strong&gt;DrvAssertMode&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvassertmode)"><strong>DrvAssertMode</strong></a></p></td>
<td align="left"><p>Resets the video mode for a specified video hardware device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvcompletepdev" data-raw-source="[&lt;strong&gt;DrvCompletePDEV&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvcompletepdev)"><strong>DrvCompletePDEV</strong></a></p></td>
<td align="left"><p>Informs the driver about the completion of device installation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdisabledriver" data-raw-source="[&lt;strong&gt;DrvDisableDriver&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdisabledriver)"><strong>DrvDisableDriver</strong></a></p></td>
<td align="left"><p>Frees all allocated resources for the driver and returns the device to its initially loaded state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdisablepdev" data-raw-source="[&lt;strong&gt;DrvDisablePDEV&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdisablepdev)"><strong>DrvDisablePDEV</strong></a></p></td>
<td align="left"><p>When the hardware is no longer needed, frees memory and resources used by the device and any surface created, but not yet deleted.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdisablesurface" data-raw-source="[&lt;strong&gt;DrvDisableSurface&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdisablesurface)"><strong>DrvDisableSurface</strong></a></p></td>
<td align="left"><p>Informs the driver that the surface created for the current device is no longer needed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvenablepdev" data-raw-source="[&lt;strong&gt;DrvEnablePDEV&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvenablepdev)"><strong>DrvEnablePDEV</strong></a></p></td>
<td align="left"><p>Enables a <a href="/windows-hardware/drivers/#wdkgloss-pdev" data-raw-source="&lt;em&gt;PDEV&lt;/em&gt;"><em>PDEV</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvenablesurface" data-raw-source="[&lt;strong&gt;DrvEnableSurface&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvenablesurface)"><strong>DrvEnableSurface</strong></a></p></td>
<td align="left"><p>Creates a surface for a specified hardware device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvgetmodes" data-raw-source="[&lt;strong&gt;DrvGetModes&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvgetmodes)"><strong>DrvGetModes</strong></a></p></td>
<td align="left"><p>Lists the modes supported by a specified video hardware device.</p></td>
</tr>
</tbody>
</table>

 

A list of required functions for all graphics drivers appears in [Required Graphics Driver Functions](required-graphics-driver-functions.md).

