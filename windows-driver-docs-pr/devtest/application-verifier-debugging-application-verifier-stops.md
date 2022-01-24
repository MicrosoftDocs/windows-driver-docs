---
title: Application Verifier - Debugging Application Verifier Stops
description: Application Verifier- Debugging Application Verifier Stops
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/11/2022
---

# Application Verifier - Debugging Application Verifier Stops
 
## Debugger install and setup 
 
Some Application Verifier actions can result in an exception being raised. The debugger must be set to catch these exceptions on the second chance, because Application Verifier itself will be handling the first chance exceptions.

The exceptions raised are of three types:

- An access violation exception (0xC0000005) is generated if the heap option detects a heap buffer overrun. In some cases, the Check system path usage option can cause an access violation as well. 

- An invalid handle exception (0xC0000008) is generated when the Detect invalid handle usage option detects an invalid handle operation. 

- A stack overflow exception (0xC00000FD) is generated when the Check for adequate stack option detects that the initial stack was too short. 

One way to prepare for these events is to start the debugger on a command line as follows:

`windbg -xd av -xd ch -xd sov ApplicationCommandLine`

or

`cdb -xd av -xd ch -xd sov ApplicationCommandLine`

If you have already started the debugger, you can use the sxd (Set Exceptions) command to catch all access violations, invalid handles, and stack overflows as second-chance exceptions:

```dbgcmd
0:000> sxd av 

0:000> sxd ch 

0:000> sxd sov 1
```

It is theoretically possible to control Application Verifier through a kernel debugger. However, this is not recommended — it requires frequent use of the .process and .pagein commands, yet it gives you no more power than using a user-mode debugger.

### Installing the debugging tools

To download the latest version of the tools, see [Download Debugging Tools for Windows](/windows-hardware/drivers/debugger/debugger-download-tools).

### Configuring Hardware for User-Mode Debugging

User-mode debugging is generally done on a single machine: the debugger is run on the same computer as the application that failed.

In this case, no specific hardware setup is required. Throughout this topic, the terms host computer and target computer are interchangeable in this case.

### Configuring Software for User-Mode Debugging

Basic User-Mode Configuration - Before you can begin user-mode debugging, you must download the necessary symbol files and set certain environment variables.

#### Symbol Files

You must download the symbol files for the user-mode process that is being debugged. If this is an application you have written, it should be built with full symbol files. If it is a commercial application, the symbol files may be available on a web server or for download, contact the manufacturer.

if you are performing remote debugging, the symbol file location depends on the method you are using:

- If you are performing remote debugging through the debugger, the symbol files should be on the computer with the debugging server. 

- If you are performing remote debugging through remote.exe, the symbol files should be on the computer with the debugger. 

- If you are performing remote debugging through a process server or a KD connection server, the symbol files should be on computer with the smart client. 

- If you are controlling the user-mode debugger from the kernel debugger, the symbol files need to be on both computers.

### Configuring Environment Variables

The debugger uses a variety of environment variables to indicate a number of important settings.

For more information on debuggers, see [Getting Started with Windows Debugging](/windows-hardware/drivers/debugger/getting-started-with-windows-debugging)

### Configuring Application Verifier with the Debugger using the Command line

To configure Application Verifier you can use the CDB or NTSD command line.

Use the following command line: 

`cdb OtherOptions -vf:Flags Target`

Where Target is the name of the target application, and Flags specifies the desired Application Verifier options that are to be applied to this target.

Flags should be a sum of the bits representing the desired options. The individual bit values are as follows:

| Flag value | Meaning                 |
|------------|-------------------------|
| 00000001   | HEAP CHECKS             |
| 00000004   | HANDLE CHECKS           |
| 00000008   | LOW RESOURCE SIM CHECKS |
| 00000020   | TLS CHECKS              |
| 00000040   | DIRTY STACKS            |
| 00000200   | DANGEROUS APIS          |
| 00001000   | EXCEPTION CHECKS        |
| 00002000   | MEMORY CHECKS           |
| 00020000   | MISCELLANEOUS CHECKS    |
| 00040000   | LOCK CHECKS             |

## Debugging with !avrf 
 
The !avrf extension controls the settings of Application Verifier and displays a variety of output produced by Application Verifier. For additional information about the !arvrf extension, see [!avrf](/windows-hardware/drivers/debugger/-avrf) in the debugger docs.

### Syntax

`!avrf`

The !avrf command without any parameters shows the Application Verifier settings and information about the current and previous Application Verifier breaks if any.

`!avrf –vs { Length | -aAddress }`

Displays the virtual space operation log. Length specifies the number of records to display starting from the most recent. Address specifies the virtual address. Records of the virtual operations containing this virtual address will be displayed.

`!avrf -hp { Length | -a Address }`

Displays the heap operation log. Address specifies the heap address. Records of the heap operations containing this heap address will be displayed.

`!avrf -cs { Length | -a Address }`

Displays the critical section delete log. Length specifies the number of records to display starting from the most recent. Address specifies the critical section address. Records for the particular critical section are displayed when Address is specified.

`!avrf -dlls [ Length ]`

Displays the DLL load/unload log. Length specifies the number of records to display starting from the most recent.

`!avrf -trm`

Displays a log of all terminated and suspended threads.

`!avrf -ex [ Length ]`

Displays the exception log. Application Verifier tracks all the exceptions happening in the application.

`!avrf -threads [ ThreadID ]`

Displays information about threads in the target process. For child threads, the stack size and the CreateThread flags specified by the parent are displayed as well. Providing a thread ID will display information only for that particular thread.

`!avrf -tp [ ThreadID ]`

Displays the thread pool log. This log may contain stack traces for various operations such as changing the thread affinity mask, changing thread priority, posting thread messages, initializing COM, and uninitializing COM from within the thread pool callback. Providing a thread ID will display information only for that particular thread.

`!avrf -srw [ Address | Address Length ] [ -stats ]`

Displays the Slim Reader/Writer (SRW) log. Specifying Address will display records pertaining to that SRW lock address. When Length is specified along with the Address , all SRW locks within that address range are displayed. The -stats option dumps the SRW lock statistics.

`!avrf -leak [ -m ModuleName ] [ -r ResourceType ] [ -a Address ] [ -t ]`

Displays the outstanding resources log. These resources may or may not be leaks at any given point. Specifying ModuleName (including the extension) displays all outstanding resources in the specified module. Specifying ResourceType displays outstanding resources of that particular resource type. Specifying Address dumps records of outstanding resources with that address. ResourceType can be one of the following:

- Heap: Displays heap allocations using Win32 Heap APIs
- Local: Displays Local/Global allocations
- CRT: Displays allocations using CRT APIs
- Virtual: Displays Virtual reservations
- BSTR: Displays BSTR allocations 
- Registry: Displays Registry key opens
- Power: Displays power notification objects
- Handle: Displays thread, file, and event handle allocations

`!avrf –trace TraceIndex`

Displays a stack trace for the specified trace index. Some structures use this 16-bit index number to identify a stack trace. This index points to a location within the stack trace database. If you are analyzing such a structure, you will find this syntax useful.

`!avrf -cnt`

Displays a list of global counters.

`!avrf -brk [ BreakEventType ]`

Specifies that this is a break-event command. When `!avrf -brk` is used with no additional parameters, the break event settings are displayed. BreakEventType specifies the type number of the break event. For a list of possible types, use `!avrf -brk`.

`!avrf -flt [ EventTypeProbability ]`

Specifies that this is a fault-injection command. When `!avrf -flt` is used with no additional parameters, the current fault injection settings are displayed. EventType specifies the type number of the event. Probability specifies the frequency with which the event will fail. This can be any integer between 0 and 1,000,000 (0xF4240).

`!avrf -flt break EventType`

Causes Application Verifier to break into the debugger each time this fault is injected.

`!avrf -flt stacks Length`

Displays Length number of stack traces for the most recent fault-injected operations.

`!avrf -trg [ StartEnd | dll Module | all ]`

Specifies that this is a target range command. When -trg is used with no additional parameters, the current target ranges are displayed. Start specifies the beginning address of the target range or exclusion range. End specifies the ending address of the target range or exclusion range. Module specifies the name of a module to be targeted or excluded. Module should include the full module name, including the .exe or .dll extension. Path information should not be included. Specifying all causes all target ranges or exclusion ranges to be reset.

`!avrf -skp [ StartEnd | dll Module | all | Time ]`

Specifies that this is an exclusion range command. Start specifies the beginning address of the target range or exclusion range. End specifies the ending address of the target range or exclusion range. Module specifies the name of a module to be targeted or excluded. Module should include the full module name, including the .exe or .dll extension. Path information should not be included. Specifying all causes all target ranges or exclusion ranges to be reset. Specifying Time causes all faults to be suppressed for Time milliseconds after execution resumes.

The following is the output provided by !avrf command in the debugger.

```dbgcmd
0:000> !avrf
Application verifier settings (816431A7):

   - full page heap
   - COM
   - RPC
   - Handles
   - Locks
   - Memory
   - TLS
   - Exceptions
   - Threadpool
   - Leak
   - SRWLock

No verifier stop active.

Note: Sometimes bugs found by verifier manifest themselves as raised
exceptions (access violations, stack overflows, invalid handles), 
and it is not always necessary to have a verifier stop.
```

### !avrf extension comments

When the !avrf extension is used with no parameters, it displays the current Application Verifier options. 

The !avrf extension uses the Exts.dll in the debugger.
 
If an Application Verifier Stop has occurred, the !avrf extension with no parameters will reveal the nature of the stop and what caused it.

If symbols for ntdll.dll and verifier.dll are missing, the !avrf extension will generate an error message. 

Continuable and Non-Continuable Stops 
 

## Debugging a Continuable Stop

Here is an example of an invalid handle exception that has been raised by the Detect invalid handle usage option.

First, the following message appears:

```dbgcmd
Invalid handle - code c0000008 (first chance)

===================================================

VERIFIER STOP 00000300: pid 0x558: invalid handle exception for current stack trace

        C0000008 : Exception code.

        0012FBF8 : Exception record. Use .exr to display it.

        0012FC0C : Context record. Use .cxr to display it.

        00000000 :

===================================================

This verifier stop is continuable.

After debugging it use 'go' to continue.

===================================================

Break instruction exception - code 80000003 (first chance)

eax=00000000 ebx=6a27c280 ecx=6a226447 edx=0012fa4c esi=00942528 edi=6a27c260

eip=6a22629c esp=0012facc ebp=0012faf0 iopl=0         nv up ei pl zr na po nc

cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00000246

ntdll!DbgBreakPoint:

6a22629c cc               int     3
```

Notice that the message tells you that this Application Verifier Stop can be continued. After you understand what has transpired, you can continue running the target application.

First, you should use the !avrf extension. This gives information about the current failure:

```dbgcmd
0:000> !avrf

Global flags: 00000100

Application verifier global flag is set.

Application verifier settings (00000004):

   - no heap checking enabled!

   - handle checks

Page heap is not active for this process.

Current stop 00000300 : c0000008 0012fbf8 0012fc0c 00000000 .

    Using an invalid handle (either closed or simply bad).
```

The final line of this display summarizes the problem.

You may want to look at some logs at this point. After you are done, use the g (Go) command to start the application again:

```dbgcmd
0:000> g

## Debugging a Non-Continuable Stop

Here is an example of an access violation that has been raised by the page heap option.

First, the following message appears:

Access violation - code c0000005 (first chance)

===================================================

VERIFIER STOP 00000008: pid 0x504: exception raised while verifying block header

        00EC1000 : Heap handle

        00F10FF8 : Heap block

        00000000 : Block size

        00000000 :

===================================================

This verifier stop is not continuable. Process will be terminated when you use the 'go' debugger command.

===================================================

Break instruction exception - code 80000003 (first chance)

eax=00000000 ebx=00000000 ecx=6a226447 edx=0012fab7 esi=00f10ff8 edi=00000008

eip=6a22629c esp=0012fb5c ebp=0012fb80 iopl=0         nv up ei pl zr na po nc

cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00000246

ntdll!DbgBreakPoint:

6a22629c cc               int     3
```

In this case, the message tells you that this Application Verifier Stop cannot be continued. The error is too severe for the process to continue running, and there is no way for Application Verifier to salvage the process.

The !avrf extension can be used to give information about the current failure:

```dbgcmd
0:000> !avrf

Global flags: 02000100

Application verifier global flag is set.

Page heap global flag is set.

Application verifier settings (00000001):

   - full page heap

Page heaps active in the process (format: pageheap, lightheap, flags):

    00941000 , 00a40000 , 3 (pageheap traces )

    00b41000 , 00c40000 , 3 (pageheap traces )

    00cb1000 , 00db0000 , 3 (pageheap traces )

    00ec1000 , 00fc0000 , 3 (pageheap traces )

Current stop 00000008 : 00ec1000 00f10ff8 00000000 00000000 .

    Corrupted heap block.
```

The final line of this display summarizes the problem.

You may also want to look at some logs at this point. You may want to use the .restart (Restart Target Application) command at this point. Or perhaps you may prefer to end your Application Verifier session and begin fixing the bugs in your code.

## Debugging Critical Section Errors 
 
### !cs debugger extension

!cs can be used in both user-mode debugger and kernel debugger to display information about critical sections in the current process. For additional information about the !cs extension, see [!cs](/windows-hardware/drivers/debugger/-cs) in the debugger docs.

Matching symbols with type information is required, especially for ntdll.dll.

The syntax for this extension is:

!cs [-s]                    - dump all the active critical sections in the current process.

!cs [-s] address            - dump critical section at this address.

!cs [-s] -d address        - dump critical section corresponding to DebugInfo at this address.

-s will dump the critical section initialization stack trace if it's available.

Examples:

Dump information about a critical section using its address

```dbgcmd
0:001> ! cs 0x7803B0F8

Critical section   = 0x7803B0F8 (MSVCRT!__app_type+0x4)
DebugInfo          = 0x6A262080
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0
```

Dump information about a critical section using its address, including initialization stack trace

```dbgcmd
0:001> !cs -s 0x7803B0F8

Critical section   = 0x7803B0F8 (MSVCRT!__app_type+0x4)
DebugInfo          = 0x6A262080
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0

Stack trace for DebugInfo = 0x6A262080:
0x6A2137BD: ntdll!RtlInitializeCriticalSectionAndSpinCount+0x9B
0x6A207A4C: ntdll!LdrpCallInitRoutine+0x14
0x6A205569: ntdll!LdrpRunInitializeRoutines+0x1D9
0x6A20DCE1: ntdll!LdrpInitializeProcess+0xAE5
```

Dump information about a critical section using its debug info address

```dbgcmd
0:001> !cs -d 0x6A262080

DebugInfo          = 0x6A262080
Critical section   = 0x7803B0F8 (MSVCRT!__app_type+0x4)
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0
```

Dump information about a critical section using its debug info address, including initialization stack trace

```dbgcmd
0:001> !cs -s -d 0x6A262080

DebugInfo          = 0x6A262080
Critical section   = 0x7803B0F8 (MSVCRT!__app_type+0x4)
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0
Stack trace for DebugInfo = 0x6A262080:
0x6A2137BD: ntdll!RtlInitializeCriticalSectionAndSpinCount+0x9B
0x6A207A4C: ntdll!LdrpCallInitRoutine+0x14
0x6A205569: ntdll!LdrpRunInitializeRoutines+0x1D9
0x6A20DCE1: ntdll!LdrpInitializeProcess+0xAE
```

Dump information about all the active critical sections in the current process

```dbgcmd
0:001> !cs

-----------------------------------------

DebugInfo          = 0x6A261D60
Critical section   = 0x6A262820 (ntdll!RtlCriticalSectionLock+0x0)
LOCKED
LockCount          = 0x0
OwningThread       = 0x460
RecursionCount     = 0x1
LockSemaphore      = 0x0
SpinCount          = 0x0
-----------------------------------------

DebugInfo          = 0x6A261D80
Critical section   = 0x6A262580 (ntdll!DeferedCriticalSection+0x0)
NOT LOCKED
LockSemaphore      = 0x7FC
SpinCount          = 0x0
-----------------------------------------

DebugInfo          = 0x6A262600
Critical section   = 0x6A26074C (ntdll!LoaderLock+0x0)
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0
.....
```

Dump information about all the active critical sections in the current process, including initialization stack trace

```dbgcmd

0:001> !cs -s

...

-----------------------------------------

DebugInfo          = 0x6A261EA0
Critical section   = 0xA8001C (+0xA8001C)
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0
No stack trace saved

-----------------------------------------

DebugInfo          = 0x6A261EC0
Critical section   = 0x6A263560 (ntdll!RtlpDphTargetDllsLock+0x0)
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0
No stack trace saved

-----------------------------------------

DebugInfo          = 0x6A261EE0
Critical section   = 0xA90608 (+0xA90608)
NOT LOCKED
LockSemaphore      = 0x7EC
SpinCount          = 0x0
Stack trace for DebugInfo = 0x6A261EE0:

0x6A2137BD: ntdll!RtlInitializeCriticalSectionAndSpinCount+0x9B
0x6A20B0DC: ntdll!CsrpConnectToServer+0x1BE
0x6A20B2AA: ntdll!CsrClientConnectToServer+0x148
0x77DBE83F: KERNEL32!BaseDllInitialize+0x11F
0x6A207A4C: ntdll!LdrpCallInitRoutine+0x14
0x6A205569: ntdll!LdrpRunInitializeRoutines+0x1D9
0x6A20DCE1: ntdll!LdrpInitializeProcess+0xAE5

-----------------------------------------

DebugInfo          = 0x6A261F00
Critical section   = 0x77E1AEB8 (KERNEL32!BaseDllRegistryCache+0x18)
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0
Stack trace for DebugInfo = 0x6A261F00:
0x6A2137BD: ntdll!RtlInitializeCriticalSectionAndSpinCount+0x9B
0x6A207A4C: ntdll!LdrpCallInitRoutine+0x14
0x6A205569: ntdll!LdrpRunInitializeRoutines+0x1D9
0x6A20DCE1: ntdll!LdrpInitializeProcess+0xAE5
```
 
## Debugging Exception Errors 

The exception log records all exceptions that have occurred in the target process.

You can use the !avrf -ex Length extension command to display the last several exceptions; Length specifies the number of exceptions. If Length is omitted, all exceptions are displayed.

Here is an example:

```dbgcmd
0:000> !avrf -ex 4

=================================

Thread ID: 0000052c
Exception code: c0000008
Exception address: 6a226663
Exception record: 0012fb50
Context record: 0012fb64

Displayed 1 exception log entries.
```


## Debugging Handles Errors 
 
!htrace can be used in both user-mode debugger and kernel debugger to display stack trace information for one or all the handles in a process. This information is available if handle tracing is enabled for the process – automatically enabled if handle checking is enabled in the application verifier. Stack traces are saved every time the process is opening or closing a handle or when it is referencing an invalid handle.  For additional information about the !htrace extension, see [!htrace](/windows-hardware/drivers/debugger/-htrace) in the debugger docs.

The kernel debugger syntax for this extension is:

`!htrace [ handle [process] ]`    

If handle is not specified or is 0, information about all the handles in the process will be displayed. If process is not specified, the current process will be used.

The user-mode debugger syntax is:

`!htrace [handle]` 

The user-mode debugger extension always displays information about the current debugee process.

Examples:


Dump information about handle 7CC in process 815328b0

```dbgcmd
kd> !htrace 7CC 815328b0

Loaded \\...\kdexts extension DLL
Process 0x815328B0
ObjectTable 0xE15ECBB8

--------------------------------------

Handle 0x7CC - CLOSE:
0x8018FCB9: ntoskrnl!ExDestroyHandle+0x103
0x801E1D12: ntoskrnl!ObpCloseHandleTableEntry+0xE4
0x801E1DD9: ntoskrnl!ObpCloseHandle+0x85
0x801E1EDD: ntoskrnl!NtClose+0x19
0x77DBFCD6: KERNEL32!GetLocaleFileInfo+0x3D
0x77DBF942: KERNEL32!NlsProcessInitialize+0x11D
0x77E0C6DF: KERNEL32!NlsDllInitialize+0x35
0x6A20785C: ntdll!LdrpCallInitRoutine+0x14
0x6A205393: ntdll!LdrpRunInitializeRoutines+0x1D9
0x6A20DD80: ntdll!LdrpInitializeProcess+0xAF6

--------------------------------------

Handle 0x7CC - OPEN:

0x8018F44A: ntoskrnl!ExCreateHandle+0x94
0x801E3180: ntoskrnl!ObpCreateHandle+0x304
0x801E1563: ntoskrnl!ObOpenObjectByName+0x1E9
0x77DBFCD6: KERNEL32!GetLocaleFileInfo+0x3D
0x77DBF942: KERNEL32!NlsProcessInitialize+0x11D
0x77E0C6DF: KERNEL32!NlsDllInitialize+0x35
0x6A20785C: ntdll!LdrpCallInitRoutine+0x14
0x6A205393: ntdll!LdrpRunInitializeRoutines+0x1D9
0x6A20DD80: ntdll!LdrpInitializeProcess+0xAF6

--------------------------------------

Parsed 0x1CA stack traces.
Dumped 0x2 stack traces.
```

Dump information about all handles in process 815328b0

```dbgcmd
kd> !htrace 0 81400300

Process 0x81400300
ObjectTable 0xE10CCF60

--------------------------------------

Handle 0x7CC - CLOSE:
0x8018FCB9: ntoskrnl!ExDestroyHandle+0x103
0x801E1D12: ntoskrnl!ObpCloseHandleTableEntry+0xE4
0x801E1DD9: ntoskrnl!ObpCloseHandle+0x85
0x801E1EDD: ntoskrnl!NtClose+0x19
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

--------------------------------------

Handle 0x7CC - OPEN:

0x8018F44A: ntoskrnl!ExCreateHandle+0x94
0x801E3390: ntoskrnl!ObpCreateUnnamedHandle+0x10C
0x801E7317: ntoskrnl!ObInsertObject+0xC3
0x77DE23B2: KERNEL32!CreateSemaphoreA+0x66
0x010011C5: badhandle!main+0x45
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

--------------------------------------

Handle 0x7DC - BAD REFERENCE:

0x8018F709: ntoskrnl!ExMapHandleToPointerEx+0xEA
0x801E10F2: ntoskrnl!ObReferenceObjectByHandle+0x12C
0x801902BE: ntoskrnl!NtSetEvent+0x6C
0x80154965: ntoskrnl!_KiSystemService+0xC4
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

--------------------------------------

Handle 0x7DC - CLOSE:

0x8018FCB9: ntoskrnl!ExDestroyHandle+0x103
0x801E1D12: ntoskrnl!ObpCloseHandleTableEntry+0xE4
0x801E1DD9: ntoskrnl!ObpCloseHandle+0x85
0x801E1EDD: ntoskrnl!NtClose+0x19
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

--------------------------------------

Handle 0x7DC - OPEN:

0x8018F44A: ntoskrnl!ExCreateHandle+0x94
0x801E3390: ntoskrnl!ObpCreateUnnamedHandle+0x10C
0x801E7317: ntoskrnl!ObInsertObject+0xC3
0x77DE265C: KERNEL32!CreateEventA+0x66
0x010011A0: badhandle!main+0x20
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

--------------------------------------

Parsed 0x6 stack traces.

Dumped 0x5 stack traces.
```

Dump information about handle 7DC in the current process

```dbgcmd

kd> !htrace  7DC

Process 0x81400300

ObjectTable 0xE10CCF60

--------------------------------------

Handle 0x7DC - BAD REFERENCE:

0x8018F709: ntoskrnl!ExMapHandleToPointerEx+0xEA
0x801E10F2: ntoskrnl!ObReferenceObjectByHandle+0x12C
0x801902BE: ntoskrnl!NtSetEvent+0x6C
0x80154965: ntoskrnl!_KiSystemService+0xC4
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

--------------------------------------

Handle 0x7DC - CLOSE:

0x8018FCB9: ntoskrnl!ExDestroyHandle+0x103
0x801E1D12: ntoskrnl!ObpCloseHandleTableEntry+0xE4
0x801E1DD9: ntoskrnl!ObpCloseHandle+0x85
0x801E1EDD: ntoskrnl!NtClose+0x19
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

--------------------------------------

Handle 0x7DC - OPEN:

0x8018F44A: ntoskrnl!ExCreateHandle+0x94
0x801E3390: ntoskrnl!ObpCreateUnnamedHandle+0x10C
0x801E7317: ntoskrnl!ObInsertObject+0xC3
0x77DE265C: KERNEL32!CreateEventA+0x66
0x010011A0: badhandle!main+0x20
0x010012C1: badhandle!mainCRTStartup+0xE3
0x77DE0B2F: KERNEL32!BaseProcessStart+0x3D

--------------------------------------

Parsed 0x6 stack traces.

Dumped 0x3 stack traces.
```


## Debugging Heap Errors 
 
### Heap verifier debugger extension

The heap verifier debugger extension is part of the !heap extension (NT heap debugger extension). Simple help can be obtained with !heap -? or more extensive with !heap -p -? . The current extension does not detect on its own if page heap is enabled for a process and act accordingly. For now the user of the extension needs to know that page heap is enabled and use commands prefixed by !heap -p . For additional information about the !htrace extension, see [!heap](/windows-hardware/drivers/debugger/-heap) in the debugger docs.

`!heap -p`

Dumps addresses of all full page heaps created in the process.

`!heap -p -h ADDRESS-OF-HEAP`

Full dump of full page heap at ADDRESS-OF-HEAP.

`!heap -p -a ADDRESS`

Tries to figure out if there is a heap block at ADDRESS. This value does not need to be the address of the start of the block. The command is useful if there is no clue whatsoever about the nature of a memory area.

### Heap operation log

The heap operation log tracks all heap routines. These include HeapAlloc, HeapReAlloc, and HeapFree.

You can use the `!avrf -hp Length` extension command to display the last several records; Length specifies the number of records.

You can use `!avrf -hp -a Address` to display all heap space operations that affected the specified Address. For an allocation operation, it is sufficient that Address be contained in the allocated heap block. For a free operation, the exact address of the beginning of the block must be given.

For each entry in the log, the following information is displayed:

- The heap function called. 
- The thread ID of the thread that called the routine. 
- The address involved in the call — this is the address that was returned by an allocation routine or that was passed to a free routine. 
- The size of the region involved in the call. 
- The stack trace of the call. 

The most recent entries are displayed first.

In this example, the two most recent entries are displayed:

```dbgcmd
0:001> !avrf -hp 2

alloc (tid: 0xFF4): 
address: 00ea2fd0 
size: 00001030
00403062: Prymes!_heap_alloc_dbg+0x1A2
00402e69: Prymes!_nh_malloc_dbg+0x19
00402e1e: Prymes!_malloc_dbg+0x1E
00404ff3: Prymes!_stbuf+0xC3
00401c23: Prymes!printf+0x43
00401109: Prymes!main+0xC9
00402039: Prymes!mainCRTStartup+0xE9
77e7a278: kernel32!BaseProcessStart+0x23

alloc (tid: 0xFF4): 
address: 00ea07d0 
size: 00000830
00403062: Prymes!_heap_alloc_dbg+0x1A2
00402e69: Prymes!_nh_malloc_dbg+0x19
00402e1e: Prymes!_malloc_dbg+0x1E
00403225: Prymes!_calloc_dbg+0x25
00401ad5: Prymes!__initstdio+0x45
00401f38: Prymes!_initterm+0x18
00401da1: Prymes!_cinit+0x21
00402014: Prymes!mainCRTStartup+0xC4

77e7a278: kernel32!BaseProcessStart+0x23
```

### Typical debug scenarios

There are several failure scenarios that might be encountered. Some of them require quite a bit of detective work to get the whole picture.

#### Access violation in non-accessible page

This happens when full page heap is enabled if the tested application accesses beyond the end of buffer. It can also happen if it touches a freed block. In order to understand what is the nature of the address on which the exception occurred, you need to use:

`!heap –p –a ADDRESS-OF-AV`

#### Corrupted block message

At several moments during the lifetime of an allocation (allocation, user free, real free) the page heap manager checks if the block has all fill patterns intact and the block header has consistent data. If this is not the case you will get a verifier stop. 

If the block is a full page heap block (for example, if you know for sure full page heap is enabled for all allocations) then you can use “!heap –p –a ADDRESS” to find out what are the characteristics of the block. 

If the block is a light page heap block then you need to find out the start address for the block header. You can find the start address by dumping 30-40 bytes below the reported address and look for the magic start/end patterns for a block header (ABCDAAAA, ABCDBBBB, ABCDAAA9, ABCDBBBA). 

The header will give all the information you need to understand the failure. Particularly, the magic patterns will tell if the block is allocated or free if it is a light page heap or a full page heap block. The information here has to be matched carefully with the offending call. 

For example if a call to HeapFree is made with the address of a block plus four bytes, then you will get the corrupted message. The block header will look fine but you will have to notice that the first byte after the end of the header (first byte after 0xDCBAXXXX magic value) has a different address then the one in the call.

#### Special fill pointers

The page heap manager fills the user allocation with values that will look as kernel pointers. This happens when the block gets freed (fill value is F0) and when the block gets allocated but no request is made for the block to be zeroed (fill value is E0 for light page heap and C0 for full page heap). The non-zeroed allocations are typical for malloc/new users. If there is a failure (access violation) where a read/write is attempted at addresses like F0F0F0F0, E0E0E0E0, C0C0C0C0 then most probably you hit one of these cases. 

A read/write at F0F0F0F0 means a block has been used after it got freed. Unfortunately you will need some detective work to find out which block caused this. You need to get the stack trace of the failure and then inspect the code for the functions on the stack. One of them might make a wrong assumption about an allocation being alive.

A read/write at E0E0E0E0/C0C0C0C0 means the application did not initialize properly the allocation. This also requires code inspection of the functions in the current stack trace. Here it is an example for this kind of failure. In a test process an access violation while doing a HeapFree on address E0E0E0E0 was noticed. It turned out that the test allocated a structure, did not initialize it correctly and then called the destructor of the object. Since a certain field was not null (it had E0E0E0E0 in it) it called delete on it.

#### Page Heap Technical Details

To detect heap corruptions (overflows or underflows), AppVerifier will modify the way memory is allocated by padding the requested memory with either full non-writable pages or with special tags before and after the allocated memory. AppVerifier does this by loading Verifier.dll into the process being verified and redirecting some of the Win32 Heap APIs called by the application to corresponding Verifier.dll APIs.

When padding the requested memory with full non-writable pages (the FULL setting is enabled in the page heap properties section and is the default setting), AppVerifier will consume a large amount of virtual memory but has the advantage that heap corruption events are cached in real time when the overflow or underflow occurs. Remember that the memory in this mode will look either like this [AppVerifier Read-Only Heap Page (4k)] [Amount of memory requested by Application under test] or like this [Amount of memory requested by Application under test] [AppVerifier Read-Only Heap Page (4k)].

The heap check will place a guard page at the beginning or end of allocation depending on the Backward property. If Backward is set to False, which is the default, it will place a guard page at the end of the allocation to catch buffer overruns. If it is set to True, the guard page is placed at the beginning of the allocation to catch buffer underruns.

When padding the requested memory with special tags (enabled by clearing the "Full" check box item in the heap properties), AppVerifier will check and alert you when this memory is released. The main problem in using this technique is that there are some cases when the memory corruption will only be detected when the memory is released (the minimum amount of memory block is 8 bytes), so when on a 3-byte variable or a 5-byte overflow occurs it will not be immediately detected.

On an underflow event, an attempt will be made to write to a Read-Only page. This will trigger an exception. Note that this exception can only be caught if the target application is being executed under a debugger. Note that the full page heap mode will also detect these errors because it uses padding+guard pages. The reason you would use light page heap is if your computer cannot tolerate the high memory constraints of full page heap.

For memory intensive applications, or when it is required to use AppVerifier during long periods of time (for example, stress testing), it is better to run normal (light) heap tests instead of full mode due to the performance degradation. However, when you run into an issue, turn on full page heap to investigate further.

Applications that are using custom heaps (a heap that bypasses the operating system's implementation of the heap) might not get the full benefit of using page heap or might even malfunction when it is enabled.

## Debugging Memory Errors 
 
### The memory verifier debugger extension

The virtual space operation log tracks all routines that modify the virtual space of a process in any way. These include VirtualAlloc, VirtualFree, MapViewOfFile, and UnmapViewOfFile.

You can use the `!avrf -vs Length` extension command to display the last several records; Length specifies the number of records.

You can use !avrf -vs -a Address to display all virtual space operations that affected the specified Address. For an allocation, it is sufficient that Address be contained in the allocated block. For a free, the exact address of the beginning of the region must be given.

For each entry in the log, the following information is displayed:

- The function called 
- The thread ID of the thread that called the routine 
- The address involved in the call — this is the address that was returned by an allocation routine or that was passed to a free routine 
- The size of the region involved in the call 
- The type of memory operation (the AllocationType parameter) 
- The type of protection requested 
- The stack trace of the call 

#### Examples

The most recent entries are displayed first.

In the following example, the two most recent entries are displayed:

```dbgcmd
0:001> !avrf -vs 2

VirtualFree (tid: 0xB4): addr:04bb0000 sz:00400000 op:8000 prot:0
        00aa1ac2: verifier!VsLogCall+0x42
        00aa19c1: verifier!AVrfpNtFreeVirtualMemory+0x30
        68925d17: kernel32!VirtualFreeEx+0x35
        6892611c: kernel32!VirtualFree+0x13
        75ef6525: mshtml+0x116525
        75ef68af: mshtml+0x1168AF
        6a20787c: ntdll!LdrpCallInitRoutine+0x14
        6a211c6f: ntdll!LdrUnloadDll+0x39A
        689275c1: kernel32!FreeLibrary+0x3B
        77b22d69: ole32!CoQueryReleaseObject+0x1E6
        77b02bd2: ole32!SetErrorInfo+0x1ED

VirtualFree (tid: 0xB4): addr:04bb0000 sz:00001000 op:4000 prot:0

        00aa1ac2: verifier!VsLogCall+0x42
        00aa19c1: verifier!AVrfpNtFreeVirtualMemory+0x30
        68925d17: kernel32!VirtualFreeEx+0x35
        6892611c: kernel32!VirtualFree+0x13
        75ef65ae: mshtml+0x1165AE
        75ef68af: mshtml+0x1168AF
        6a20787c: ntdll!LdrpCallInitRoutine+0x14
        6a211c6f: ntdll!LdrUnloadDll+0x39A
        689275c1: kernel32!FreeLibrary+0x3B
        77b22d69: ole32!CoQueryReleaseObject+0x1E6
        77b02bd2: ole32!SetErrorInfo+0x1ED
```

It can be seen from the output that thread 0xB4 first decommitted a page and then released the entire virtual region.

Here is a display of all operations affecting the address 0x4BB1000:

```dbgcmd
0:001> !avrf -vs -a 4bb1000

Searching in vspace log for address 04bb1000 ...

VirtualFree (tid: 0xB4): addr:04bb0000 sz:00400000 op:8000 prot:0
        00aa1ac2: verifier!VsLogCall+0x42
        00aa19c1: verifier!AVrfpNtFreeVirtualMemory+0x30
        68925d17: kernel32!VirtualFreeEx+0x35
        6892611c: kernel32!VirtualFree+0x13
        75ef6525: mshtml+0x116525
        75ef68af: mshtml+0x1168AF
        6a20787c: ntdll!LdrpCallInitRoutine+0x14
        6a211c6f: ntdll!LdrUnloadDll+0x39A
        689275c1: kernel32!FreeLibrary+0x3B
        77b22d69: ole32!CoQueryReleaseObject+0x1E6
        77b02bd2: ole32!SetErrorInfo+0x1ED

VirtualFree (tid: 0xB4): addr:04bb1000 sz:00001000 op:4000 prot:0

        00aa1ac2: verifier!VsLogCall+0x42
        00aa19c1: verifier!AVrfpNtFreeVirtualMemory+0x30
        68925d17: kernel32!VirtualFreeEx+0x35
        6892611c: kernel32!VirtualFree+0x13
        75ef65ae: mshtml+0x1165AE
        75ef68af: mshtml+0x1168AF
        6a20787c: ntdll!LdrpCallInitRoutine+0x14
        6a211c6f: ntdll!LdrUnloadDll+0x39A
        689275c1: kernel32!FreeLibrary+0x3B
        77b22d69: ole32!CoQueryReleaseObject+0x1E6
        77b02bd2: ole32!SetErrorInfo+0x1ED

VirtualAlloc (tid: 0xB4): addr:04bb0000 sz:00010000 op:1000 prot:4

        00aa1ac2: verifier!VsLogCall+0x42
        00aa1988: verifier!AVrfpNtAllocateVirtualMemory+0x37
        68925ca3: kernel32!VirtualAllocEx+0x61
        68926105: kernel32!VirtualAlloc+0x16
        75ef63f3: mshtml+0x1163F3

VirtualAlloc (tid: 0xB4): addr:04bb0000 sz:00400000 op:2000 prot:4

        00aa1ac2: verifier!VsLogCall+0x42
        00aa1988: verifier!AVrfpNtAllocateVirtualMemory+0x37
        68925ca3: kernel32!VirtualAllocEx+0x61
        68926105: kernel32!VirtualAlloc+0x16
        75ef63d9: mshtml+0x1163D9
```

To read this output, remember that the entries are dumped starting with the most recent one. Thus, this log shows that thread 0xB4 allocated a large region in which it committed a page. Later it decommitted the page, and then released the entire virtual region.


## See Also

[Application Verifier - Overview](application-verifier.md)

[Application Verifier - Testing Applications](application-verifier-testing-applications.md)
 
[Application Verifier - Tests within Application Verifier](application-verifier-tests-within-application-verifier.md)

[Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md)

[Application Verifier - Frequently Asked Questions](application-verifier-faqs.md)

 

 





