---
title: WIA Diagnostic Log Macros
author: windows-driver-content
description: WIA Diagnostic Log Macros
ms.assetid: 8b544045-e9d7-422b-825c-f1a5531e0e11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Diagnostic Log Macros





For error handling on Windows Vista and later operating systems, see [WIA Driver Error Recovery for Windows Vista](wia-driver-error-recovery-for-windows-vista.md).

The [Diagnostic Log Macros](https://msdn.microsoft.com/library/windows/hardware/ff540599) enable minidrivers to log trace, error, and warning messages to the *Wiaservc.log* diagnostic log file.

For more information about error handling on Windows Vista and later operating systems, see [WIA Driver Error Recovery for Windows Vista](wia-driver-error-recovery-for-windows-vista.md).

The first three macros can be used to write a logging statement with a specified type of error, trace, or warning, respectively. The fourth macro can be used to translate an HRESULT into a descriptive string.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Macro</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>WIAS_LERROR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549580)</p></td>
<td><p>Writes a log statement of type ERROR to the <em>Wiaservc.log</em> diagnostic log file..</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WIAS_LHRESULT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549589)</p></td>
<td><p>Translates an HRESULT value into a string and writes the string to the <em>Wiaservc.log</em> diagnostic log file.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WIAS_LTRACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549600)</p></td>
<td><p>Writes a log statement of type TRACE to the <em>Wiaservc.log</em> diagnostic log file..</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WIAS_LWARNING</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549610)</p></td>
<td><p>Writes a log statement of type WARNING to the <em>Wiaservc.log</em> diagnostic log file..</p></td>
</tr>
<tr class="odd">
<td><p><strong>WIAS_ERROR</strong></p></td>
<td><p>This macro is available in Windows Vista and later operating systems.</p>
<p>Writes a log statement of type ERROR to the <em>Wiatrace.log</em> diagnostic log file.</p></td>
</tr>
<tr class="even">
<td><p><strong>WIAS_TRACE</strong></p></td>
<td><p>This macro is available in Windows Vista and later operating systems.</p>
<p>Writes a log statement of type TRACE to the <em>Wiatrace.log</em> diagnostic log file.</p></td>
</tr>
</tbody>
</table>

 

For more information about these macros, see [IWiaLog Interface and Diagnostic Log Macros](https://msdn.microsoft.com/library/windows/hardware/ff543937).

 

 




