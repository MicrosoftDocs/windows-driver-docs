---
title: .jdinfo (Use JIT_DEBUG_INFO)
description: The .jdinfo command uses a JIT_DEBUG_INFO structure as the source of the exception and context for just in time (JIT) debugging.
ms.assetid: C35A2A04-CF0E-475e-8471-2A8562BB3650
keywords: ["Use JIT_DEBUG_INFO (.jdinfo) command ----- Appendix", "JIT_DEBUG_INFO ----- Appendix", ".jdinfo (Use JIT_DEBUG_INFO) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .jdinfo (Use JIT_DEBUG_INFO)
api_type:
- NA
ms.localizationpriority: medium
---

# .jdinfo (Use JIT\_DEBUG\_INFO)


The **.jdinfo** command uses a JIT\_DEBUG\_INFO structure as the source of the exception and context for just in time (JIT) debugging. The address to the structure is passed to the **.jdinfo** command using the %p parameter that is specified in the AeDebug registry entry.

For more information about the registry keys used, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md). For more information about register contexts, see [Changing Contexts](changing-contexts.md).

```dbgcmd
.jdinfo Address 
```

## <span id="ddk_apc_meta_use_jit_debug_info_dbg"></span><span id="DDK_APC_META_USE_JIT_DEBUG_INFO_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the JIT\_DEBUG\_INFO structure. The address to the structure is passed to the **.jdinfo** command using the %p parameter that is specified in the AeDebug registry entry.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode</p></td>
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

 

### <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example

This example show how the AeDebug registry entry can be configured to use the WinDbg can be used as the JIT debugger.

```dbgcmd
Debugger = "Path\WinDbg.EXE -p %ld -e %ld -c ".jdinfo 0x%p"
```

Then, when a crash occurs, the configured JIT debugger is invoked and the %p parameter is used to pass the address of the JIT\_DEBUG\_INFO structure to the **.jdinfo** command that is executed after the debugger is started.

```dbgcmd
nMicrosoft (R) Windows Debugger Version 10.0.10240.9 AMD64
Copyright (c) Microsoft Corporation. All rights reserved.

*** wait with pending attach
Executable search path is: 
...
ModLoad: 00000000`68a20000 00000000`68ac3000   C:\WINDOWS\WinSxS\amd64_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.30729.9247_none_08e394a1a83e212f\MSVCR90.dll
(153c.5d0): Break instruction exception - code 80000003 (first chance)
Processing initial command '.jdinfo 0x00000000003E0000'
ntdll!DbgBreakPoint:
00007ffc`81a986a0 cc              int     3
0:003> .jdinfo 0x00000000003E0000
----- Exception occurred on thread 0:15c8
ntdll!ZwWaitForMultipleObjects+0x14:
00007ffc`81a959a4 c3              ret

----- Exception record at 00000000`003e0028:
ExceptionAddress: 00007ff791d81014 (CrashAV_x64!wmain+0x0000000000000014)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 0000000000000001
   Parameter[1]: 0000000000000000
Attempt to write to address 0000000000000000

----- Context record at 00000000`003e00c0:
rax=0000000000000000 rbx=0000000000000000 rcx=00007ffc81a954d4
rdx=0000000000000000 rsi=0000000000000000 rdi=0000000000000001
rip=00007ff791d81014 rsp=00000000006ff8b0 rbp=0000000000000000
 r8=00000000006ff808  r9=0000000000000000 r10=0000000000000000
r11=0000000000000000 r12=0000000000000000 r13=0000000000000000
r14=0000000000000000 r15=0000000000000000
iopl=0         nv up ei pl zr na po nc
cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010246
CrashAV_x64!wmain+0x14:
00007ff7`91d81014 45891b          mov     dword ptr [r11],r11d ds:00000000`00000000=????????
```

Remarks
-------

The **.jdinfo** command uses the **AeDebug** registry information introduced in Windows Vista. For more information about the registry keys used, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md). The **.jdinfo** command takes the address of a JIT\_DEBUG\_INFO that the system set up for **AeDebug** and sets the context to the exception that caused the crash.

You can use the **.jdinfo** command instead of **-g** in **AeDebug** to have your debugger set to the **AeDebug** state without requiring execution.

This state can be advantageous, because under usual conditions, when a user-mode exception occurs, the following sequence occurs:

1.  The Microsoft Windows operating system halts execution of the application.

2.  The postmortem debugger is started.

3.  The debugger attaches to the application.

4.  The debugger issues a "Go" command. (This command is caused by the **-g** in the **AeDebug** key.)

5.  The target attempts to execute and may or may not encounter the same exception.

6.  This exception breaks into the debugger.

There are several problems that can occur because of these events:

-   Exceptions do not always repeat, possibly because of a transient condition that no longer exists when the exception is restarted.

-   Another event, such as a different exception, might occur. There is no way of knowing whether it is identical to the original event.

-   Attaching a debugger involves injecting a new thread, which can be blocked if a thread is holding the loader lock. Injecting a new thread can be a significant disturbance of the process.

If you use **-c .jdinfo** instead of **-g** in your **AeDebug** key, no execution occurs. Instead, the exception information is retrieved from the JIT\_DEBUG\_INFO structure using the %p variable.

For example, consider the following **AeDebug** key.

```dbgcmd
ntsd -p %ld -e %ld -c ".jdinfo 0x%p"
```

The following example is even less invasive. The **-pv** switch causes the debugger to attach noninvasively, which does not inject any new threads into the target.

```dbgcmd
ntsd -pv -p %ld -e %ld -c ".jdinfo 0x%p"
```

If you use this noninvasive option, exiting the debugger does not end the process. You can use the [**.kill (Kill Process)**](-kill--kill-process-.md) command to end the process.

If you want to use this for dump file debugging, you should use [**.dump /j**](-dump--create-dump-file-.md) to add the JIT\_DEBUG\_INFO structure to your dump file, when the dump file is created.

The JIT\_DEBUG\_INFO structure is defined as follows.

```dbgcmd
typedef struct _JIT_DEBUG_INFO {
    DWORD dwSize;
    DWORD dwProcessorArchitecture;
    DWORD dwThreadID;
    DWORD dwReserved0;
    ULONG64 lpExceptionAddress;
    ULONG64 lpExceptionRecord;
    ULONG64 lpContextRecord;
} JIT_DEBUG_INFO, *LPJIT_DEBUG_INFO;
```

You can use the dt command to display the JIT\_DEBUG\_INFO structure.

```dbgcmd
0: kd> dt JIT_DEBUG_INFO
nt!JIT_DEBUG_INFO
   +0x000 dwSize           : Uint4B
   +0x004 dwProcessorArchitecture : Uint4B
   +0x008 dwThreadID       : Uint4B
  +0x00c dwReserved0      : Uint4B
   +0x010 lpExceptionAddress : Uint8B
   +0x018 lpExceptionRecord : Uint8B
   +0x020 lpContextRecord  : Uint8B
```

**Viewing the Exception Record, Call Stack and LastEvent Using WinDbg**

After the .jdinfo command has been used to set the context to the moment of failure, you can view the exception record returned by .jdinfo, the call stack and the lastevent, as shown below, to investigate cause.

```dbgcmd
0:000> .jdinfo  0x00000000003E0000
----- Exception occurred on thread 0:15c8
ntdll!NtWaitForMultipleObjects+0x14:
00007ffc`81a959a4 c3              ret

----- Exception record at 00000000`003e0028:
ExceptionAddress: 00007ff791d81014 (CrashAV_x64!wmain+0x0000000000000014)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 0000000000000001
   Parameter[1]: 0000000000000000
Attempt to write to address 0000000000000000
...

0:000> k
  *** Stack trace for last set context - .thread/.cxr resets it
# Child-SP          RetAddr           Call Site
00 00000000`006ff8b0 00007ff7`91d811d2 CrashAV_x64!wmain+0x14 [c:\my\my_projects\crash\crashav\crashav.cpp @ 14]
01 00000000`006ff8e0 00007ffc`7fa38364 CrashAV_x64!__tmainCRTStartup+0x11a [f:\dd\vctools\crt_bld\self_64_amd64\crt\src\crtexe.c @ 579]
02 00000000`006ff910 00007ffc`81a55e91 KERNEL32!BaseThreadInitThunk+0x14
03 00000000`006ff940 00000000`00000000 ntdll!RtlUserThreadStart+0x21

0:000> .lastevent
Last event: 153c.5d0: Break instruction exception - code 80000003 (first chance)
  debugger time: Thu Sep  8 12:55:08.968 2016 (UTC - 7:00)
```

 

 





