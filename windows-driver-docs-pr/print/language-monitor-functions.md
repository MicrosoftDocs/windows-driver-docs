---
title: Language Monitor Functions
author: windows-driver-content
description: Language Monitor Functions
ms.assetid: ffe1a52f-69cc-4346-945f-3f1bc0a1a91e
keywords: ["language monitors WDK print , functions"]
---

# Language Monitor Functions


## <a href="" id="ddk-language-monitor-functions-gg"></a>


The following table lists the functions that a language monitor must define.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DllEntryPoint</strong></p></td>
<td><p>A DLL entry point, typically called <strong>DllMain</strong>, which is described in the Microsoft Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ClosePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545975)</p></td>
<td><p>Closes a port when there are no printers connected to it.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>EndDocPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548742)</p></td>
<td><p>Performs end-of-print-job tasks on a port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GetPrinterDataFromPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550506)</p></td>
<td><p>Optional. Polls a port for values that are stored in the registry.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>InitializePrintMonitor2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551605)</p></td>
<td><p>Initializes the print monitor and returns an instance handle.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>OpenPortEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559596)</p></td>
<td><p>Opens a port for a newly connected printer.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ReadPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561909)</p></td>
<td><p>Reads data from a printer port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>SendRecvBidiDataFromPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562071)</p></td>
<td><p>Optional. Supports bidirectional communication between an application and a printer or print server.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>Shutdown</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562646)</p></td>
<td><p>Optional. Deletes a monitor instance. This function is required for cluster support.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>StartDocPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562710)</p></td>
<td><p>Performs the tasks required to start a print job on a port.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WritePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563792)</p></td>
<td><p>Writes data to a printer port.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Language%20Monitor%20Functions%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


