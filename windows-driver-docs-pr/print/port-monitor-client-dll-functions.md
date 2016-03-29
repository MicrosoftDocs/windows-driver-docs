---
title: Port Monitor Client DLL Functions
description: Port Monitor Client DLL Functions
ms.assetid: 41efab1a-0638-4925-90a2-cf68d2306ca6
keywords: ["port monitors WDK print , functions", "client DLL port monitor functions WDK"]
---

# Port Monitor Client DLL Functions


## <a href="" id="ddk-port-monitor-client-dll-functions-gg"></a>


The following table lists the functions that a port monitor UI DLL must define.

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
<td align="left"><p>[<strong>AddPortUI</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545026)</p></td>
<td align="left"><p>Creates a port and obtains configuration information by displaying a dialog box.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ConfigurePortUI</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546290)</p></td>
<td align="left"><p>Configures a previously added port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DeletePortUI</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547432)</p></td>
<td align="left"><p>Deletes a port.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>InitializePrintMonitorUI</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551608)</p></td>
<td align="left"><p>Initializes the port monitor UI DLL.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Port%20Monitor%20Client%20DLL%20Functions%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




