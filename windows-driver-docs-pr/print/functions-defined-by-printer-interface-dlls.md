---
title: Functions Defined by Printer Interface DLLs
author: windows-driver-content
description: Functions Defined by Printer Interface DLLs
ms.assetid: 8b0ae796-67cf-4619-a0a7-6cb6aab8c2e4
keywords:
- printer interface DLL WDK , functions
- functions WDK printer interface DLL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Functions Defined by Printer Interface DLLs


## <a href="" id="ddk-functions-defined-by-printer-interface-dlls-gg"></a>


Printer interface DLLs export the functions listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DllEntryPoint</strong></p></td>
<td><p>Initial DLL entry point, typically called DLLMain (described in the Microsoft Windows SDK documentation).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DrvConvertDevMode</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548532)</p></td>
<td><p>Converts the specified [<strong>DEVMODEW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure from one version to another.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DrvDeviceCapabilities</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548539)</p></td>
<td><p>Returns requested information about a printer's capabilities.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DrvDevicePropertySheets</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548542)</p></td>
<td><p>Calls [CPSUI](common-property-sheet-user-interface.md) to create property sheet pages that describe a printer's properties.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DrvDocumentEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548544)</p></td>
<td><p>(Optional) Allows the printer interface DLL to specify which events associated with printing a document it will handle.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DrvDriverEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548551)</p></td>
<td><p>(Optional) Allows the printer interface DLL to respond to notifications from the spooler that certain driver-specific events have occurred.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DrvDocumentPropertySheets</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548548)</p></td>
<td><p>Calls CPSUI to create property sheet pages that describe a print document's properties.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DrvPrinterEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548564)</p></td>
<td><p>Allows the printer interface DLL to respond to notifications from the spooler that certain printer-specific events have occurred.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DrvQueryColorProfile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548573)</p></td>
<td><p>(Optional) Allows the printer interface DLL to specify an ICC profile to use for color management.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DrvQueryJobAttributes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548581)</p></td>
<td><p>(Optional) Allows the printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page (&quot;N-up&quot; printing), printing multiple copies of each page, and collating pages.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DevQueryPrintEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547576)</p></td>
<td><p>Determines if a print job can be printed using the printer's current configuration.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DrvSplDeviceCaps</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548600)</p></td>
<td><p>Returns requested information about a printer's capabilities.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DrvUpgradePrinter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548648)</p></td>
<td><p>(Optional) Updates a printer's registry settings when a new version of the driver is added to a system.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Functions%20Defined%20by%20Printer%20Interface%20DLLs%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


