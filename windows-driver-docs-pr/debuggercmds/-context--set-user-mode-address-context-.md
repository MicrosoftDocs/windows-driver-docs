---
title: ".context (Set User-Mode Address Context)"
description: "The .context command specifies which page directory of a process will be used for the user-mode address context, or displays the current user-mode address context."
keywords: ["Set User-Mode Address Context (.context) command", "addresses, Set User-Mode Address Context (.context) command", "context, Set User-Mode Address Context (.context) command", ".context (Set User-Mode Address Context) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .context (Set User-Mode Address Context)
api_type:
- NA
---

# .context (Set User-Mode Address Context)


The **.context** command specifies which page directory of a process will be used for the user-mode address context, or displays the current user-mode address context.

```dbgsyntax
.context [PageDirectoryBase]
```

## <span id="ddk_meta_set_user_mode_address_context_dbg"></span><span id="DDK_META_SET_USER_MODE_ADDRESS_CONTEXT_DBG"></span>Parameters


<span id="_______PageDirectoryBase______"></span><span id="_______pagedirectorybase______"></span><span id="_______PAGEDIRECTORYBASE______"></span> *PageDirectoryBase*   
Specifies the base address for a page directory of a desired process. The user-mode address context will be set to this page directory. If *PageDirectoryBase* is zero, the user-mode address context will be set to the page directory for the current system state. If *PageDirectoryBase* is omitted, the current user-mode address context is displayed.

## Environment

|  Item       | Description       |
|-----------|------------------|
| Modes     | kernel mode only |
| Targets   | live, crash dump |
| Platforms | all              |

 

## Additional Information

For more information about the user-mode address context and other context settings, see [Changing Contexts](../debugger/changing-contexts.md).

## Remarks

Generally, when you are doing kernel debugging, the only visible user-mode address space is the one associated with the current process.

The **.context** command instructs the kernel debugger to use the specified page directory as the *user-mode address context*. After this command is executed, the debugger will have access to this virtual address space. The page tables for this address space will be used to interpret all user-mode memory addresses. This allows you to read and write to this memory.

The [**.process (Set Process Context)**](-process--set-process-context-.md) command has a similar effect. However, the **.context** command sets the user-mode address context to a specific page directory, while the **.process** command sets the *process context* to a specific process. On an x86 processor, these two commands have essentially the same effect. See [Process Context](../debugger/changing-contexts.md#process-context) for more details.

If you are doing live debugging, you should issue a [**.cache forcedecodeuser**](-cache--set-cache-size-.md) command in addition to the **.context** command. This forces the debugger to look up the physical addresses of the memory space needed. (This can be slow, because it often means a huge amount of data must be transferred across the debug cable.)

If you are doing crash dump debugging, the [**.cache**](-cache--set-cache-size-.md) command is not needed. However, you will not have access to any portions of the virtual address space of the user-mode process that were paged to disk when the crash occurred.

Here is an example. Use the [**!process**](-process.md) extension to find the directory base for the desired process:

```dbgcmd
kd> !process 0 0
**** NT ACTIVE PROCESS DUMP ****
PROCESS fe5039e0  SessionId: 0  Cid: 0008    Peb: 00000000  ParentCid: 0000
    DirBase: 00030000  ObjectTable: fe529b68  TableSize:  50.
    Image: System

...

PROCESS fe3c0d60  SessionId: 0  Cid: 0208    Peb: 7ffdf000  ParentCid: 00d4
 DirBase: 0011f000  ObjectTable: fe3d0f48  TableSize:  30.
    Image: regsvc.exe
```

Now use the **.context** command with this page directory base.

```dbgcmd
kd> .context 0011f000
```

This enables you to examine the address space in various ways. For example, here is the output of the [**!peb**](-peb.md) extension:

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
        WindowTitle: "'C:\WINNT\system32\regsvc.exe'"
        ImageFile:    'C:\WINNT\system32\regsvc.exe'
        CommandLine:  'C:\WINNT\system32\regsvc.exe'
        DllPath:     'C:\WINNT\system32;.;C:\WINNT\System32;C:\WINNT\system;C:\WINNT;C:\WINNT\system32;C:\WINNT;C:\WINNT\System32\Wbem;C:\PROGRA~1\COMMON~1\AUTODE~1'
        Environment:  0x10000
```

