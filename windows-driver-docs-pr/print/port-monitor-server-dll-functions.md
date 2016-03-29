---
title: Port Monitor Server DLL Functions
description: Port Monitor Server DLL Functions
ms.assetid: ffbcaaaa-7f9d-4b29-b939-189e10174074
keywords: ["port monitors WDK print , functions", "server DLL port monitor functions WDK"]
---

# Port Monitor Server DLL Functions


## <a href="" id="ddk-port-monitor-server-dll-functions-gg"></a>


The following table lists the functions that a port monitor server DLL must define.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>DllEntryPoint</strong></p></td>
<td align="left"><p>DLL entry point, typically called <strong>DllMain</strong>, which is described in the Microsoft Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ClosePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545975)</p></td>
<td align="left"><p>Closes a port if there are no printers connected to it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EndDocPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548742)</p></td>
<td align="left"><p>Performs end-of-print-job tasks on a port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EnumPorts</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548754)</p></td>
<td align="left"><p>Enumerates the ports available for printing on a server.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>InitializePrintMonitor2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551605)</p></td>
<td align="left"><p>Initializes the print monitor and returns an instance handle.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>OpenPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559593)</p></td>
<td align="left"><p>Opens a printer port.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>OpenPortEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559596)</p></td>
<td align="left"><p>Opens a printer port. (Language monitor only)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ReadPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561909)</p></td>
<td align="left"><p>Reads data from a printer port.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StartDocPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562710)</p></td>
<td align="left"><p>Performs the tasks required to start a print job on a port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WritePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563792)</p></td>
<td align="left"><p>Writes data to a printer port.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>XcvClosePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564254)</p></td>
<td align="left"><p>Closes a port after port management is complete. Available in Windows 2000 and later NT-based operating system versions.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>XcvDataPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564258)</p></td>
<td align="left"><p>Handles port management tasks. Available in Windows 2000 and later NT-based operating system versions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>XcvOpenPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564259)</p></td>
<td align="left"><p>Opens a port for management purposes. Available in Windows 2000 and later NT-based operating system versions.</p></td>
</tr>
</tbody>
</table>

 

The following port monitor server DLL functions are optional.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>GetPrinterDataFromPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550506)</p></td>
<td align="left"><p>Sends an I/O control code to a port driver and returns the result.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SendRecvBidiDataFromPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562071)</p></td>
<td align="left"><p>Supports bidirectional communication between an application and a printer or print server. Available in Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetPortTimeOuts</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562630)</p></td>
<td align="left"><p>Sets a time-out value on an open port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Shutdown</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562646)</p></td>
<td align="left"><p>Deletes a monitor instance. This function is required for cluster support.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Port%20Monitor%20Server%20DLL%20Functions%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




