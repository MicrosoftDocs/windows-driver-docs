---
title: Required Graphics Driver Functions
description: Required Graphics Driver Functions
keywords:
- GDI WDK Windows 2000 display , functions, required
- graphics drivers WDK Windows 2000 display , functions, required
- functions WDK graphics , required
- drawing WDK GDI , functions, required
- GDI WDK Windows 2000 display , DDI, required functions
- graphics drivers WDK Windows 2000 display , DDI, required functions
- DDI WDK graphics , required functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required Graphics Driver Functions


## <span id="ddk_required_graphics_driver_functions_gg"></span><span id="DDK_REQUIRED_GRAPHICS_DRIVER_FUNCTIONS_GG"></span>


All graphics drivers must support the entry points that GDI calls to enable and disable the driver, the *PDEV* structure, and the surface associated with each PDEV. The following table lists the needed functions in the order in which they are typically called.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry Point</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvenabledriver" data-raw-source="[&lt;strong&gt;DrvEnableDriver&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvenabledriver)"><strong>DrvEnableDriver</strong></a></p></td>
<td align="left"><p>As the initial driver entry point, this function provides GDI with the driver version number and entry points of optional functions supported. This is also the only driver function that GDI calls by name. All of the other driver functions are accessed through a table of function pointers. Unlike <strong>DrvEnableDriver</strong>, the names of the other driver functions are not fixed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvgetmodes" data-raw-source="[&lt;strong&gt;DrvGetModes&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvgetmodes)"><strong>DrvGetModes</strong></a></p></td>
<td align="left"><p>Lists the modes supported by a specified video hardware device. (This function is required of display drivers only.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvenablepdev" data-raw-source="[&lt;strong&gt;DrvEnablePDEV&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvenablepdev)"><strong>DrvEnablePDEV</strong></a></p></td>
<td align="left"><p>Enables a PDEV.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvcompletepdev" data-raw-source="[&lt;strong&gt;DrvCompletePDEV&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvcompletepdev)"><strong>DrvCompletePDEV</strong></a></p></td>
<td align="left"><p>Informs the driver upon completion of device installation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvenablesurface" data-raw-source="[&lt;strong&gt;DrvEnableSurface&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvenablesurface)"><strong>DrvEnableSurface</strong></a></p></td>
<td align="left"><p>Creates a surface for a specified hardware device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdisablesurface" data-raw-source="[&lt;strong&gt;DrvDisableSurface&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdisablesurface)"><strong>DrvDisableSurface</strong></a></p></td>
<td align="left"><p>Informs the driver that the surface created for the current device is no longer needed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdisablepdev" data-raw-source="[&lt;strong&gt;DrvDisablePDEV&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdisablepdev)"><strong>DrvDisablePDEV</strong></a></p></td>
<td align="left"><p>When the hardware is no longer needed, frees memory and resources used by the device and any surface created, but not yet deleted.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdisabledriver" data-raw-source="[&lt;strong&gt;DrvDisableDriver&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdisabledriver)"><strong>DrvDisableDriver</strong></a></p></td>
<td align="left"><p>Frees all allocated resources for the driver and returns the device to its initial state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvassertmode" data-raw-source="[&lt;strong&gt;DrvAssertMode&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvassertmode)"><strong>DrvAssertMode</strong></a></p></td>
<td align="left"><p>Resets the video mode for a specified hardware device. (This function is required of display drivers only.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvresetdevice" data-raw-source="[&lt;strong&gt;DrvResetDevice&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvresetdevice)"><strong>DrvResetDevice</strong></a></p></td>
<td align="left"><p>Resets the device when it has become inoperable or unresponsive.</p></td>
</tr>
</tbody>
</table>

 

