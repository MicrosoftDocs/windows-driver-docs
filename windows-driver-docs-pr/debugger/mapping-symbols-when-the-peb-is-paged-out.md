---
title: Mapping Symbols When the PEB is Paged Out
description: Mapping Symbols When the PEB is Paged Out
ms.assetid: dba9e686-81fc-4efa-a5c7-293b9e47e0b1
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Mapping Symbols When the PEB is Paged Out


## <span id="ddk_invalid_or_missing_symbols_dbg"></span><span id="DDK_INVALID_OR_MISSING_SYMBOLS_DBG"></span>


To load symbols, the debugger looks at the list of modules loaded by the operating system. The pointer to the user-mode module list is one of the items stored in the process environment block (PEB).

To reclaim memory, the Memory Manager may page out user-mode data to make space for other process or kernel mode components. The user-mode data that is paged out may include the PEB data structure. Without this data structure, the debugger cannot determine for which images to load symbols.

**Note**   This affects symbol files only for the user-mode modules. Kernel-mode modules and symbols are not affected, as they are tracked in a different list.

 

Suppose a user-mode module is mapped into the current process and you want to fix the symbols for it. Find any address in the range of virtual addresses of the module. For example, suppose a module is mapped into a virtual address range that contains the address 7f78e9e000F. Enter the following command.

```dbgcmd
3: kd> !vad 7f78e9e000F 1
```

The command output displays information about the virtual address descriptor (VAD) for the module. The command output also includes a Reload command string that you can use to load the symbols for the module. The Reload command string includes the starting address (000007f7\`8e9e0000) and size (32000) of the notepad module.

```dbgcmd
VAD @ fffffa80056fb960
...
Reload command: .reload notepad.exe=000007f7`8e9e0000,32000
```

To load the symbols, enter the command that was given in the Reload command string.

```dbgcmd
.reload notepad.exe=000007f7`8e9e0000,32000
```

Here is another example that uses a slightly different technique. The example demonstrates how to use the [**!vad**](-vad.md) extension to map symbols when the PEB is paged out. The basic idea is to find the starting address and size of the relevant DLL so that you can then use the [**.reload**](-reload--reload-module-.md) command to load the necessary symbols. Suppose that the address of the current process is 0xE0000126\`01BA0AF0 and you want to fix the symbols for it. First, use the [**!process**](-process.md) command to obtain the virtual address descriptor (VAD) root address:

```dbgcmd
kd> !process e000012601ba0af0 1
PROCESS e000012601ba0af0
    SessionId: 2  Cid: 0b50    Peb: 6fbfffde000  ParentCid: 0efc
    DirBase: 079e8461  ObjectTable: e000000600fbceb0  HandleCount: 360.
    Image: explorer.exe
    VadRoot e000012601a35e70 Vads 201 Clone 0 Private 917. Modified 2198. Locked 0.
...
```

Then use the [**!vad**](-vad.md) extension to list the VAD tree associated with the process. Those VADs labeled "EXECUTE\_WRITECOPY" belong to code modules.

```dbgcmd
kd> !vad e000012601a35e70
VAD     level      start      end    commit
...
e0000126019f9790 ( 6)      3fff0    3fff7        -1 Private      READONLY
e000012601be1080 ( 7)   37d9bd30 37d9bd3e         2 Mapped  Exe  EXECUTE_WRITECOPY  <-- these are DLLs
e000012600acd970 ( 5)   37d9bec0 37d9bece         2 Mapped  Exe  EXECUTE_WRITECOPY
e000012601a5cba0 ( 7)   37d9c910 37d9c924         2 Mapped  Exe  EXECUTE_WRITECOPY
...
```

Then use the [**!vad**](-vad.md) extension again to find the starting address and size of the paged out memory which holds the DLL of interest. This confirms that you have found the correct DLL:

```dbgcmd
kd> !vad e000012601be1080 1

VAD @ e000012601be1080
  Start VPN:      37d9bd30  End VPN: 37d9bd3e  Control Area:  e00001260197b8d0
  First ProtoPte: e0000006013e00a0  Last PTE fffffffffffffffc  Commit Charge         2 (2.)
  Secured.Flink          0  Blink           0  Banked/Extend:        0
  File Offset   0
   ImageMap ViewShare EXECUTE_WRITECOPY

...
        File: \Windows\System32\ExplorerFrame.dll
```

The "Start VPN" field - in this case, 0x37D9BD30 - indicates the starting virtual page number. This must be converted to an actual address, by multiplying it by the page size. You can use the [**? (Evaluate Expression)**](---evaluate-expression-.md) command to multiply this value by 0x2000, which is the page size for the Itanium-based machine the example comes from.

```dbgcmd
kd> ? 37d9bd3e*2000 
Evaluate expression: 7676040298496 = 000006fb`37a7c000
```

Then the size of the range can be converted to bytes:

```dbgcmd
kd> ? 37d9bd3e-37d9bd30+1 <--   computes the number of pages
Evaluate expression: 15 = 00000000`0000000f
kd> ? f*2000
Evaluate expression: 122880 = 00000000`0001e000        
```

So ExplorerFrame.dll starts at address 0x000006Fb\`37A7C000 and is 0x1E000 bytes large. You can load its symbols with:

```dbgcmd
kd> .reload /f ExplorerFrame.dll=6fb`37a7c000,1e000
```

 

 





