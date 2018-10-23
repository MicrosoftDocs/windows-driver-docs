---
title: IWiaLog COM Interface
author: windows-driver-content
description: IWiaLog COM Interface
ms.assetid: e5d42b5d-796f-42f3-9c01-4234b8765ca6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IWiaLog COM Interface





The [**IWiaLog interface**](https://msdn.microsoft.com/library/windows/hardware/ff543935) is obsolete in Microsoft Windows XP and later and is no longer supported. Use the WIA Diagnostic Log Macros instead.

It is provided for backward compatibility only. The methods in this interface allow a minidriver to write error, trace, and warning messages to a log. The **IWiaLog** interface provides the following methods.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaLog::InitializeLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543932)</p></td>
<td><p>Initializes the logging utility.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaLog::Log</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543939)</p></td>
<td><p>Logs a message to a file or other target.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaLog::hResult</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543928)</p></td>
<td><p>Translates an HRESULT into a string.</p></td>
</tr>
</tbody>
</table>

 

For more information about this interface, see [IWiaLog Interface and Diagnostic Log Macros](https://msdn.microsoft.com/library/windows/hardware/ff543937).

 

 




