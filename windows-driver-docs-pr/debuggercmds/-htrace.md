---
title: htrace (WinDbg)
description: The htrace extension displays stack trace information for one or more handles.
keywords: ["handle, htrace extension", "htrace Windows Debugging"]
ms.date: 08/29/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- htrace
api_type:
- NA
---

# !htrace

The **!htrace** extension displays stack trace information for one or more handles.

User-Mode Syntax

```dbgcmd
!htrace [Handle [Max_Traces]] 
!htrace -enable [Max_Traces]
!htrace -snapshot
!htrace -diff
!htrace -disable
!htrace -? 
```

Kernel-Mode Syntax

```dbgcmd
!htrace [Handle [Process [Max_Traces]]] 
!htrace -? 
```

## Parameters

*Handle* Specifies the handle whose stack trace will be displayed. If *Handle* is 0 or omitted, stack traces for all handles in the process will be displayed.

*Process* (Kernel mode only) Specifies the process whose handles will be displayed. If *Process* is 0 or omitted, then the current process is used. In user mode, the current process is always used.

*Max\_Traces* Specifies the maximum number of stack traces to display. In user mode, if this parameter is omitted, then all the stack traces for the target process will be displayed.

**-enable** (User mode only) Enables handle tracing and takes the first snapshot of the handle information to use as the initial state by the **-diff** option.

**-snapshot** (User mode only) Takes a snapshot of the current handle information to use as the initial state by the **-diff** option.

**-diff** (User mode only) Compares current handle information with the last snapshot of handle information that was taken. Displays all handles that are still open.

**-disable**
(User mode only) Disables handle tracing.

**-?**

Displays brief help text for this extension in the Debugger Command window.

### DLL

Windows XP and later

Kdexts.dll
Ntsdexts.dll

### Additional Information

To display further information about a specific handle, use the [**!handle**](-handle.md) extension.

For information about handles, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

Before **!htrace** can be used, handle tracing must be enabled. One way to enable handle tracing is to enter the **!htrace -enable** command. When handle tracing is enabled, stack trace information is saved each time the process opens a handle, closes a handle, or references an invalid handle. It is this stack trace information that **!htrace** displays.

**Note**   You can also enable handle tracing by activating Application Verifier for the target process and selecting the **Handles** option.

Some of the traces reported by **!htrace** may be from a different process context. In this case, the return addresses may not resolve properly in the current process context, or may resolve to the wrong symbols.

The following example displays information about all handles in process 0x81400300.

```dbgcmd
kd> !htrace 0 81400300
Process 0x81400300
ObjectTable 0xE10CCF60
## 

Handle 0x7CC - CLOSE:
0x8018FCB9: ntoskrnl!ExDestroyHandle+0x103
0x801E1D12: ntoskrnl!ObpCloseHandleTableEntry+0xE4
0x801E1DD9: ntoskrnl!ObpCloseHandle+0x85
0x801E1EDD: ntoskrnl!NtClose+0x19
0x010012C1: badhandle!mainCRTStartup+0xE3
## 0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

Handle 0x7CC - OPEN:
0x8018F44A: ntoskrnl!ExCreateHandle+0x94
0x801E3390: ntoskrnl!ObpCreateUnnamedHandle+0x10C
0x801E7317: ntoskrnl!ObInsertObject+0xC3
0x77DE23B2: KERNEL32!CreateSemaphoreA+0x66
0x010011C5: badhandle!main+0x45
0x010012C1: badhandle!mainCRTStartup+0xE3
## 0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

Handle 0x7DC - BAD REFERENCE:
0x8018F709: ntoskrnl!ExMapHandleToPointerEx+0xEA
0x801E10F2: ntoskrnl!ObReferenceObjectByHandle+0x12C
0x801902BE: ntoskrnl!NtSetEvent+0x6C
0x80154965: ntoskrnl!_KiSystemService+0xC4
0x010012C1: badhandle!mainCRTStartup+0xE3
## 0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

Handle 0x7DC - CLOSE:
0x8018FCB9: ntoskrnl!ExDestroyHandle+0x103
0x801E1D12: ntoskrnl!ObpCloseHandleTableEntry+0xE4
0x801E1DD9: ntoskrnl!ObpCloseHandle+0x85
0x801E1EDD: ntoskrnl!NtClose+0x19
0x010012C1: badhandle!mainCRTStartup+0xE3
## 0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

Handle 0x7DC - OPEN:
0x8018F44A: ntoskrnl!ExCreateHandle+0x94
0x801E3390: ntoskrnl!ObpCreateUnnamedHandle+0x10C
0x801E7317: ntoskrnl!ObInsertObject+0xC3
0x77DE265C: KERNEL32!CreateEventA+0x66
0x010011A0: badhandle!main+0x20
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D
## 

Parsed 0x6 stack traces.
Dumped 0x5 stack traces.
```
