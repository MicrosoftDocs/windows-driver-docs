---
title: .process (Set Process Context)
description: The .process command specifies which process is used for the process context.
ms.assetid: f454faef-bc28-43f1-b511-bcee0c12fc24
keywords: ["Set Process Context (.process) command", "addresses, Set Process Context (.process) command", "context, Set Process Context (.process) command", "Process, Set Process Context (.process) command", ".process (Set Process Context) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .process (Set Process Context)
api_type:
- NA
ms.localizationpriority: medium
---

# .process (Set Process Context)


The **.process** command specifies which process is used for the process context.

```dbgcmd
.process [/i] [/p [/r]] [/P] [Process]
```

## <span id="ddk_meta_set_process_context_dbg"></span><span id="DDK_META_SET_PROCESS_CONTEXT_DBG"></span>Parameters


<span id="________i______"></span><span id="________I______"></span> **/i**   
(Windows XP and later; live debugging only; not during local kernel debugging) Specifies that *Process* is to be debugged *invasively*. This kind of debugging means that the operating system of the target computer actually makes the specified process active. (Without this option, the **.process** command alters the debugger's output but does not affect the target computer itself.) If you use **/i**, you must use the [**g (Go)**](g--go-.md) command to execute the target. After several seconds, the target breaks back in to the debugger, and the specified *Process* is active and used for the process context.

<span id="________p______"></span><span id="________P______"></span> **/p**   
Translates all transition page table entries (PTEs) for this process to physical addresses before access, if you use **/p** and *Process* is nonzero. This translation might cause slowdowns, because the debugger must find the physical addresses for all of the memory that this process uses. Also, the debugger might have to transfer a significant amount of data across the debug cable. (This behavior is the same as [**.cache forcedecodeuser**](-cache--set-cache-size-.md).)

If you include the **/p** option and *Process* is zero or you omit it, the translation is disabled. (This behavior is the same as [**.cache noforcedecodeptes**](-cache--set-cache-size-.md).)

<span id="________r______"></span><span id="________R______"></span> **/r**   
Reloads user-mode symbols after the process context has been set, if you use the **/r** and **/p** options. (This behavior is the same as [**.reload /user**](-reload--reload-module-.md).)

<span id="________P______"></span><span id="________p______"></span> **/P**   
(Live debugging and complete memory dumps only) Translates all transition page table entries (PTEs) to physical addresses before access, if you use **/P** and *Process* is nonzero. Unlike the **/p** option, the **/P** option translates the PTEs for all user-mode and kernel-mode processes, not only the specified process. This translation might cause slowdowns, because the debugger must find the physical addresses for all memory in use. Also, the debugger might have to transfer lots of data across the debug cable. (This behavior is the same as [**.cache forcedecodeptes**](-cache--set-cache-size-.md).)

<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
Specifies the address of the process that you want. (More precisely, this parameter specifies the address of the EPROCESS block for this process). The process context is set to this process. If you omit *Process* or specify zero, the process context is reset to the default process for the current system state. (If you used the **/i** option to set process context, you must use the **/i** option to reset the process context.)

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the process context and other context settings, see [Changing Contexts](changing-contexts.md).

Remarks
-------

Typically, when you are doing kernel debugging, the only visible user-mode address space is the one that is associated with the current process.

The **.process** command instructs the kernel debugger to use a specific user-mode process as the *process context*. This usage has several effects, but the most important is that the debugger has access to the virtual address space of this process. The debugger uses the page tables for this process to interpret all user-mode memory addresses, so you can read and write to this memory.

The [**.context (Set User-Mode Address Context)**](-context--set-user-mode-address-context-.md) command has a similar effect. However, the **.context** command sets the *user-mode address context* to a specific page directory, while the **.process** command sets the process context to a specific process. On an x86-based processor, **.context** and **.process** have almost the same effect. However, on an Itanium-based processor, a single process might have more than one page directory. In this situation, the **.process** command is more powerful, because it enables access to all of the page directories that are associated with a process. For more information about the process context, see [Process Context](changing-contexts.md#process-context).

**Note**   If you are performing live debugging, you should use the **/i** or the **/p** parameter. Without one of these parameters, you cannot correctly display user-mode or session memory.

 

The **/i** parameter activates the target process. When you use this option, you must execute the target once for this command to take effect. If you execute again, the process context is lost.

The **/p** parameter enables the **forcedecodeuser** setting. (You do not have to use **/p** if the **forcedecodeuser** option is already active.) The process context and the **forcedecodeuser** state remain only until the target executes again.

If you are performing crash dump debugging, the **/i** and **/p** options are not available. However, you cannot access any part of the user-mode process' virtual address space that were paged to disk when the crash occurred.

If you want to use the kernel debugger to set breakpoints in user space, use the **/i** option to switch the target to the correct process context.

The following example shows how to use the [**!process**](-process.md) extension to find the address of the EPROCESS block for the desired process.

```dbgcmd
kd> !process 0 0
**** NT ACTIVE PROCESS DUMP ****
PROCESS fe5039e0  SessionId: 0  Cid: 0008    Peb: 00000000  ParentCid: 0000
    DirBase: 00030000  ObjectTable: fe529b68  TableSize:  50.
    Image: System

.....

PROCESS fe3c0d60  SessionId: 0  Cid: 0208    Peb: 7ffdf000  ParentCid: 00d4
    DirBase: 0011f000  ObjectTable: fe3d0f48  TableSize:  30.
    Image: regsvc.exe
```

Now the example uses the **.process** command with this process address.

```dbgcmd
kd> .process fe3c0d60
Implicit process is now fe3c0d60
```

Notice that this command makes the [**.context**](-context--set-user-mode-address-context-.md) command unnecessary. The user-mode address context already has the desired value.

```dbgcmd
kd> .context 
User-mode page directory base is 11f000
```

This value enables you to examine the address space in various ways. For example, the following example shows the output of the [**!peb**](-peb.md) extension.

```dbgcmd
kd> !peb
PEB at 7FFDF000
    InheritedAddressSpace:    No
    ReadImageFileExecOptions: No
    BeingDebugged:            No
    ImageBaseAddress:         01000000
    Ldr.Initialized: Yes
    Ldr.InInitializationOrderModuleList: 71f40 . 77f68
    Ldr.InLoadOrderModuleList: 71ec0 . 77f58
    Ldr.InMemoryOrderModuleList: 71ec8 . 77f60
        01000000 C:\WINNT\system32\regsvc.exe
        77F80000 C:\WINNT\System32\ntdll.dll
        77DB0000 C:\WINNT\system32\ADVAPI32.dll
        77E80000 C:\WINNT\system32\KERNEL32.DLL
        77D40000 C:\WINNT\system32\RPCRT4.DLL
        77BE0000 C:\WINNT\system32\secur32.dll
    SubSystemData:     0
    ProcessHeap:       70000
    ProcessParameters: 20000
        WindowTitle:  'C:\WINNT\system32\regsvc.exe'
        ImageFile:    'C:\WINNT\system32\regsvc.exe'
        CommandLine:  'C:\WINNT\system32\regsvc.exe'
        DllPath:     'C:\WINNT\system32;.;C:\WINNT\System32;C:\WINNT\system;C:\WINNT;C:\WINNT\system32;C:\WINNT;C:\WINNT\System32\Wbem;C:\PROGRA~1\COMMON~1\AUTODE~1'
        Environment:  0x10000
```

 

 





