---
title: Required Display Driver Functions
description: Required Display Driver Functions
ms.assetid: 483aa13b-a14d-49f3-8265-013f7bb64d40
keywords:
- graphics DDI functions WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>DrvEnableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556210)</p></td>
<td align="left"><p>As the initial driver entry point, provides GDI with the driver version number and entry points of optional functions supported.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvAssertMode</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556178)</p></td>
<td align="left"><p>Resets the video mode for a specified video hardware device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvCompletePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556181)</p></td>
<td align="left"><p>Informs the driver about the completion of device installation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvDisableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556196)</p></td>
<td align="left"><p>Frees all allocated resources for the driver and returns the device to its initially loaded state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvDisablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556198)</p></td>
<td align="left"><p>When the hardware is no longer needed, frees memory and resources used by the device and any surface created, but not yet deleted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvDisableSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556200)</p></td>
<td align="left"><p>Informs the driver that the surface created for the current device is no longer needed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvEnablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556211)</p></td>
<td align="left"><p>Enables a [<em>PDEV</em>](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvEnableSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556214)</p></td>
<td align="left"><p>Creates a surface for a specified hardware device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvGetModes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556233)</p></td>
<td align="left"><p>Lists the modes supported by a specified video hardware device.</p></td>
</tr>
</tbody>
</table>

 

A list of required functions for all graphics drivers appears in [Required Graphics Driver Functions](required-graphics-driver-functions.md).

 

 





