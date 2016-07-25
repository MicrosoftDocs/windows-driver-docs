---
title: SetupAPI Logging Functions
description: SetupAPI Logging Functions
ms.assetid: d27bd44c-41c1-4546-b463-11ed3f5c7d84
---

# SetupAPI Logging Functions


Starting with Windows Vista, Plug and Play (PnP) device installation applications, class installers, and co-installers can use the following functions to write log entries to the [SetupAPI text logs](setupapi-text-logs.md).

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
<td align="left"><p>[<strong>SetupGetThreadLogToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552211)</p></td>
<td align="left"><p>Retrieves the [log token](log-tokens.md) for the thread that called [<strong>SetupGetThreadLogToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552211).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupSetThreadLogToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552216)</p></td>
<td align="left"><p>Sets the log token for the thread that called [<strong>SetupSetThreadLogToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552216).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupWriteTextLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552218)</p></td>
<td align="left"><p>Writes a log entry in a [SetupAPI text log](setupapi-text-logs.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupWriteTextLogError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552232)</p></td>
<td align="left"><p>Writes information about a SetupAPI-specific error or a Win32 error in SetupAPI text log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupWriteTextLogInfLine</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552236)</p></td>
<td align="left"><p>Writes a log entry in a SetupAPI text log that contains the text of a specified INF file line.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20SetupAPI%20Logging%20Functions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




