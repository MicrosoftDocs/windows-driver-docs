---
title: Required Graphics Driver Functions
description: Required Graphics Driver Functions
ms.assetid: 3a7a7516-b758-4499-bd9d-216fef7b3c8c
keywords: ["GDI WDK Windows 2000 display , functions, required", "graphics drivers WDK Windows 2000 display , functions, required", "functions WDK graphics , required", "drawing WDK GDI , functions, required", "GDI WDK Windows 2000 display , DDI, required functions", "graphics drivers WDK Windows 2000 display , DDI, required functions", "DDI WDK graphics , required functions"]
---

# Required Graphics Driver Functions


## <span id="ddk_required_graphics_driver_functions_gg"></span><span id="DDK_REQUIRED_GRAPHICS_DRIVER_FUNCTIONS_GG"></span>


All graphics drivers must support the entry points that GDI calls to enable and disable the driver, the [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) structure, and the surface associated with each PDEV. The following table lists the needed functions in the order in which they are typically called.

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
<td align="left"><p>[<strong>DrvEnableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556210)</p></td>
<td align="left"><p>As the initial driver entry point, this function provides GDI with the driver version number and entry points of optional functions supported. This is also the only driver function that GDI calls by name. All of the other driver functions are accessed through a table of function pointers. Unlike <strong>DrvEnableDriver</strong>, the names of the other driver functions are not fixed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvGetModes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556233)</p></td>
<td align="left"><p>Lists the modes supported by a specified video hardware device. (This function is required of display drivers only.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvEnablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556211)</p></td>
<td align="left"><p>Enables a PDEV.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvCompletePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556181)</p></td>
<td align="left"><p>Informs the driver upon completion of device installation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvEnableSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556214)</p></td>
<td align="left"><p>Creates a surface for a specified hardware device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvDisableSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556200)</p></td>
<td align="left"><p>Informs the driver that the surface created for the current device is no longer needed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvDisablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556198)</p></td>
<td align="left"><p>When the hardware is no longer needed, frees memory and resources used by the device and any surface created, but not yet deleted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvDisableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556196)</p></td>
<td align="left"><p>Frees all allocated resources for the driver and returns the device to its initial state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvAssertMode</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556178)</p></td>
<td align="left"><p>Resets the video mode for a specified hardware device. (This function is required of display drivers only.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvResetDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556275)</p></td>
<td align="left"><p>Resets the device when it has become inoperable or unresponsive.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Required%20Graphics%20Driver%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




