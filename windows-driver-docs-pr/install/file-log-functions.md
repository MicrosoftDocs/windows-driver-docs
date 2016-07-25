---
title: File Log Functions
description: File Log Functions
ms.assetid: 7d9fe4c9-834f-4dcc-a216-dc6a98ee2fd3
keywords: ["SetupAPI functions WDK , log files", "log files WDK SetupAPI"]
---

# File Log Functions


## <a href="" id="ddk-file-log-functions-dg"></a>


You can use a log file to record information about the files copied to a system during an installation. The log file can be either the system log or your own installation log file.

The following table lists the functions that can be used to manipulate log files. For more information about function descriptions, see the Microsoft Windows SDK documentation on [MSDN](http://go.microsoft.com/fwlink/p/?linkid=131248).

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
<td align="left"><p>[<strong>SetupInitializeFileLog</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377397)</p></td>
<td align="left"><p>Initializes a log file for use.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupLogError</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377405)</p></td>
<td align="left"><p>Writes an error message to a log file. (It should be used only during the installation of the operating system.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupLogFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377406)</p></td>
<td align="left"><p>Adds an entry to the log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQueryFileLog</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377415)</p></td>
<td align="left"><p>Retrieves information from a log file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupRemoveFileLogEntry</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377429)</p></td>
<td align="left"><p>Removes an entry from a log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupTerminateFileLog</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377443)</p></td>
<td align="left"><p>Releases resources allocated to a log file.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20File%20Log%20Functions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




