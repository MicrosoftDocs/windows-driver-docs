---
title: Printer Dirids
author: windows-driver-content
description: Printer Dirids
MS-HAID:
- 'prtinst\_e0288931-16eb-4ca0-8582-dd81639d5c99.xml'
- 'print.printer\_dirids'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 104af180-c739-4733-b21b-448cfe15ab71
keywords: ["INF files WDK print , dirids", "dirids WDK", "directory identifiers WDK printer", "printer dirids WDK", "identifiers WDK printer"]
---

# Printer Dirids


## <a href="" id="ddk-printer-dirids-gg"></a>


When specifying target directories within INF files, directory identifiers (`dirids`) should be used. For more information, see [Using Dirids](https://msdn.microsoft.com/library/windows/hardware/ff553598).

The following table lists printer-specific `dirids` and the purpose of each.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Dirid</th>
<th>Purpose</th>
<th>Directory Contents</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>66000</p></td>
<td><p>Represents the directory path returned by the [GetPrinterDriverDirectory](http://go.microsoft.com/fwlink/p/?linkid=124454) function.</p></td>
<td><p>Driver files and [dependent files](printer-inf-file-entries.md#ddk-dependent-files-gg).</p></td>
</tr>
<tr class="even">
<td><p>66001</p></td>
<td><p>Represents the directory path returned by the [GetPrintProcessorDirectory](http://go.microsoft.com/fwlink/p/?linkid=124455) function.</p></td>
<td><p>[<em>Print processor</em>](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-processor) files.</p></td>
</tr>
<tr class="odd">
<td><p>66002</p></td>
<td><p>Represents the directory path to additional files to be copied to \System32 of the local system. See the paragraph following this table.</p></td>
<td><p>[<em>Print monitor</em>](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-monitor) files.</p></td>
</tr>
<tr class="even">
<td><p>66003</p></td>
<td><p>Represents the directory path returned by the [GetColorDirectory](http://go.microsoft.com/fwlink/p/?linkid=124456) function.</p></td>
<td><p>ICM color profile files.</p></td>
</tr>
<tr class="odd">
<td><p>66004</p></td>
<td><p>Represents the directory path to which printer type-specific ASP files are copied.</p></td>
<td><p>ASP files and associated files.</p></td>
</tr>
</tbody>
</table>

 

Files in the directory assigned to `dirid` 66002 are copied to the System32 subdirectory when printer drivers for the native architecture are being installed on the local system, such as when x86 drivers are installed locally on a x86 system. Files in this directory are ignored if a driver is being installed to a remote system.

A printer driver is installed when the printer class installer calls the spooler's [AddPrinterDriverEx](http://go.microsoft.com/fwlink/p/?linkid=124457) function. This function requires all driver files to be located in the directory that is returned by the **GetPrinterDriverDirectory** function.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Dirids%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


