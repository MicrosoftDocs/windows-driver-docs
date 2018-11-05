---
title: bpid
description: The bpid extension requests that a process on the target computer break into the debugger or requests that a user-mode debugger be attached to a process on the target computer.
ms.assetid: 47091651-3b39-4e3d-86cf-a8e95779a025
keywords: ["bpid Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bpid
api_type:
- NA
ms.localizationpriority: medium
---

# !bpid


The **!bpid** extension requests that a process on the target computer break into the debugger or requests that a user-mode debugger be attached to a process on the target computer.

```dbgcmd
    !bpid [Options] PID 
```

## <span id="ddk__bpid_dbg"></span><span id="DDK__BPID_DBG"></span>Parameters


<span id="_______Option______"></span><span id="_______option______"></span><span id="_______OPTION______"></span> *Option*   
Controls the additional activities of this command.

The valid values for *Option* appear in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-a</strong></p></td>
<td align="left"><p>Attaches a new user-mode debugger to the process specified by <em>PID</em>. The user-mode debugger runs on the target machine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-s</strong></p></td>
<td align="left"><p>Adds a breakpoint that occurs in the WinLogon process immediately before the break in the user-mode process specified by <em>PID</em>. This allows the user to verify the request before attempting the action.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-w</strong></p></td>
<td align="left"><p>Stores the request in the memory in the target computer. The target system can then repeat the request, but this is not usually necessary.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______PID______"></span><span id="_______pid______"></span> *PID*   
Specifies the process ID of the desired process on the target computer. If you are using this to control a user-mode debugger on the target computer, *PID* should be the process ID of the target application, not of the user-mode debugger. (Because process IDs are usually listed in decimal format, you might need to prefix this with **0n** or convert it to hexadecimal format.)

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

This extension command is supported on x86-based, x64-based, and Itanium-based target computers.

Remarks
-------

This command is especially useful when redirecting input and output from a user-mode debugger to the kernel debugger. It causes the user-mode target application to break into the user-mode debugger, which in turn requests input from the kernel debugger. See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details.

If this command is used in another situation, the user-mode process calls **DbgBreakPoint**. This will usually break directly into the kernel debugger.

The **-s** option causes a break in WinLogon just before the break in the specified process occurs. This is useful if you want to perform debugging actions within WinLogon's process context. The [**g (Go)**](g--go-.md) command can then be used to move on to the second break.

Note that there are ways in which this extension can fail to execute:

-   Lack of resources. The **!bpid** extension injects a thread into the target process, so the system must have enough resources to create a thread. Using the **-a** option requires even more system resources since **!bpid -a** must run a full instance of a debugger on the target computer.

-   The loader lock is already held. Both **!bpid** and **!bpid -a** require a thread to run in the target process in order to make it break into the debugger. If another thread is holding the loader lock, then the **!bpid** thread will not be able to run and a break into the debugger may not occur. Thus, if **!bpid** fails when there is enough user-mode memory available for the target process, it is possible that the loader lock is held.

-   Lack of permission. The operation of the !bpid extension requires permission sufficient for WinLogon to create a remote thread and attach a debugger to a given process.

-   No access to ntsd.exe. If ntsd.exe is not found in a commonly known path, !bpid will fail to set an appropriate PID. Note that ntsd.exe is not included by default with Windows Vista.

 

 





