---
title: Debugging CSRSS
description: Debugging CSRSS
keywords: ["CSRSS debugging", "NTSD, debugging CSRSS", "controlling the user-mode debugger from the kernel debugger, debugging CSRSS"]
ms.date: 12/22/2021
---

# Debugging CSRSS

## <span id="ddk_debugging_csrss_with_ntsd_dbg"></span><span id="DDK_DEBUGGING_CSRSS_WITH_NTSD_DBG"></span>

The Client Server Run-Time Subsystem (CSRSS) is the user-mode process that controls the underlying layer for the Windows environment. 

> [!NOTE]
> Starting in Windows 10, CSRSS is a protected process and can only be debugged in kernel mode.
>

For general information on protected processes, as well as additional specifics on Windows protected, critical code such as wininit and csrss, see *Windows Internals* by Pavel Yosifovich, Mark E. Russinovich, David A. Solomon, and Alex Ionescu.


### <span id="starting_ntsd"></span><span id="STARTING_NTSD"></span>Display CSRSS Process Information

To examine CSRSS, some information is available using kernel debugging.

Use the [**!process**](-process.md) extension to display information about processes associated with csrss.exe.

```dbgcmd
0: kd> !process 0 0 csrss.exe
PROCESS ffffe381a583b080
    SessionId: 0  Cid: 027c    Peb: e0c93ef000  ParentCid: 0270
    DirBase: 115478000  ObjectTable: ffffaa87786b67c0  HandleCount: 722.
    Image: csrss.exe

PROCESS ffffe381a68ab140
    SessionId: 1  Cid: 02f4    Peb: 186a447000  ParentCid: 02dc
    DirBase: 143c0e000  ObjectTable: ffffaa87786b5200  HandleCount: 445.
    Image: csrss.exe
```

Take either of the associated processes, and set the context to that location using the [**.process (Set Process Context)**](-process--set-process-context-.md) command.

```dbgcmd
0: kd> .process /r /p ffffe381a583b080
Implicit process is now ffffe381`a583b080
Loading User Symbols
```

Now use the [**dt (Display Type)**](dt--display-type-.md) command to show the process structure directly:

```dbgcmd
0: kd> dt csrss!_csr_process
   +0x000 ClientId         : _CLIENT_ID
   +0x010 ListLink         : _LIST_ENTRY
   +0x020 ThreadList       : _LIST_ENTRY
   +0x030 NtSession        : Ptr64 _CSR_NT_SESSION
   +0x038 ClientPort       : Ptr64 Void
   +0x040 ClientViewBase   : Ptr64 Char
   +0x048 ClientViewBounds : Ptr64 Char
   +0x050 ProcessHandle    : Ptr64 Void
   +0x058 SequenceNumber   : Uint4B
   +0x05c Flags            : Uint4B
   +0x060 DebugFlags       : Uint4B
   +0x064 ReferenceCount   : Int4B
   +0x068 ProcessGroupId   : Uint4B
   +0x06c ProcessGroupSequence : Uint4B
   +0x070 LastMessageSequence : Uint4B
   +0x074 NumOutstandingMessages : Uint4B
   +0x078 ShutdownLevel    : Uint4B
   +0x07c ShutdownFlags    : Uint4B
   +0x080 Luid             : _LUID
   +0x088 ServerDllPerProcessData : [1] Ptr64 Void
```

The [!peb](-peb.md) extension can be used to display additional information about the process environment block (PEB).


