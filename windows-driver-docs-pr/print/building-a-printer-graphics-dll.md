---
title: Building a Printer Graphics DLL
description: Building a Printer Graphics DLL
ms.assetid: bec1e9cc-a846-43e5-bc9e-e43a151ef6c4
keywords:
- printer graphics DLL WDK , building
- graphics DLL WDK printer , building
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Building a Printer Graphics DLL





When building a printer graphics DLL, you must be aware of the following differences between DLLs intended for user-mode execution and those intended for kernel-mode execution.

**Note**   In Windows Vista, printer graphics DLLs can only execute in user mode. For more information, see [Choosing User Mode or Kernel Mode](choosing-user-mode-or-kernel-mode.md).

 

### Rules for Building a Printer Graphics DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>User-mode graphics DLL</th>
<th>Kernel-mode graphics DLL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Set TARGETTYPE=DYNLINK in source file.</p></td>
<td><p>Set TARGETTYPE=GDI_DRIVER in source file.</p></td>
</tr>
<tr class="even">
<td><p>Preprocessor macro USERMODE_DRIVER must be defined in source files before winddi.h is included.</p></td>
<td><p>Preprocessor macro USERMODE_DRIVER must not be defined.</p></td>
</tr>
<tr class="odd">
<td><p>Object modules must be linked with the umpdddi.lib and gdi32.lib import libraries.</p></td>
<td><p>Object modules must be linked with the win32k.lib import library.</p></td>
</tr>
<tr class="even">
<td><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff556261" data-raw-source="[&lt;strong&gt;DrvQueryDriverInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556261)"><strong>DrvQueryDriverInfo</strong></a> function must return <strong>TRUE</strong> for DRVQUERY_USERMODE.</p></td>
<td><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff556261" data-raw-source="[&lt;strong&gt;DrvQueryDriverInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556261)"><strong>DrvQueryDriverInfo</strong></a> function must return <strong>FALSE</strong> for DRVQUERY_USERMODE. (Alternatively, the function can be omitted.)</p></td>
</tr>
</tbody>
</table>

 

 

 




