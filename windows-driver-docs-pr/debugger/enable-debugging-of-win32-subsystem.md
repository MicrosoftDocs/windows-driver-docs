---
title: Enable Debugging of Win32 Subsystem
description: Enable debugging of Win32 subsystem
keywords: ["Enable debugging of Win32 subsystem (global flag)"]
ms.date: 12/22/2021
---

# Enable debugging of Win32 subsystem


## <span id="ddk_enable_debugging_of_win32_subsystem_dtools"></span><span id="DDK_ENABLE_DEBUGGING_OF_WIN32_SUBSYSTEM_DTOOLS"></span>

> [!NOTE]
> Starting in Windows 10, CSRSS is a protected process and can only be debugged in kernel mode.
>


The **Enable debugging of Win32 subsystem** flag debugs the Client Server Run-time Subsystem (csrss.exe) in the NTSD debugger.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>d32</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x20000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_ENABLE_CSRDEBUG</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

NTSD debugs the process by using the command **ntsd -d -p -1**.

This flag is effective only when the [Debug initial command](debug-initial-command.md) flag (dic) or the [Debug WinLogon](debug-winlogon.md) flag (dwl) is also set.

For details on NTSD, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

 

 