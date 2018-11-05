---
title: Using the analyze Extension
description: Using the analyze Extension
ms.assetid: 0aa74153-e992-4d1c-b734-ccc60cff452c
keywords: ["analyze extension, examples"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using the !analyze Extension


## <span id="ddk_using_the_analyze_extension_dbg"></span><span id="DDK_USING_THE_ANALYZE_EXTENSION_DBG"></span>


The first step in debugging a crashed target computer or application is to use the [**!analyze**](-analyze.md) extension command.

This extension performs a tremendous amount of automated analysis. The results of this analysis are displayed in the Debugger Command window.

You should use the **-v** option for a fully verbose display of data. For details on other options, see the [**!analyze**](-analyze.md) reference page.

This topic contains:

- A User-Mode !analyze -v Example
- A Kernel-Mode !analyze -v Example
- The Followup Field and the triage.ini File
- Additional !analyze Techniques

### <span id="ddk_a_user_mode_analyze_v_example_dbg"></span><span id="DDK_A_USER_MODE_ANALYZE_V_EXAMPLE_DBG"></span>A User-Mode !analyze -v Example

In this example, the debugger is attached to a user-mode application that has encountered an exception.

```dbgcmd
0:000> !analyze -v
*******************************************************************************
*                                                                             *
*                        Exception Analysis                                   *
*                                                                             *
*******************************************************************************

Debugger SolutionDb Connection::Open failed 80004005
```

If you are connected to the internet, the debugger attempts to access a database of crash solutions maintained by Microsoft. In this case, an error message was displayed, indicating that either your machine was unable to access the internet or the web site was not working.

```dbgcmd
FAULTING_IP: 
ntdll!PropertyLengthAsVariant+73
77f97704 cc               int     3
```

The FAULTING\_IP field shows the instruction pointer at the time of the fault.

```dbgcmd
EXCEPTION_RECORD:  ffffffff -- (.exr ffffffffffffffff)
ExceptionAddress: 77f97704 (ntdll!PropertyLengthAsVariant+0x00000073)
   ExceptionCode: 80000003 (Break instruction exception)
  ExceptionFlags: 00000000
NumberParameters: 3
   Parameter[0]: 00000000
   Parameter[1]: 00010101
   Parameter[2]: ffffffff
```

The EXCEPTION\_RECORD field shows the exception record for this crash. This information can also be viewed by using the [**.exr (Display Exception Record)**](-exr--display-exception-record-.md) command.

```dbgcmd
BUGCHECK_STR:  80000003
```

The BUGCHECK\_STR field shows the exception code. The name is a misnomer—the term *bug check* actually signifies a kernel-mode crash. In user-mode debugging, the exception code will be displayed—in this case, 0x80000003.

```dbgcmd
DEFAULT_BUCKET_ID:  APPLICATION_FAULT
```

The DEFAULT\_BUCKET\_ID field shows the general category of failures that this failure belongs to.

```dbgcmd
PROCESS_NAME:  MyApp.exe
```

The PROCESS\_NAME field specifies the name of the process that raised the exception.

```dbgcmd
LAST_CONTROL_TRANSFER:  from 01050963 to 77f97704
```

The LAST\_CONTROL\_TRANSFER field shows the last call on the stack. In this case, the code at address 0x01050963 called a function at 0x77F97704. You can use these addresses with the [**ln (List Nearest Symbols)**](ln--list-nearest-symbols-.md) command to determine what modules and functions these addresses reside in.

```dbgcmd
STACK_TEXT:  
0006b9dc 01050963 00000000 0006ba04 000603fd ntdll!PropertyLengthAsVariant+0x73
0006b9f0 010509af 00000002 0006ba04 77e1a449 MyApp!FatalErrorBox+0x55 [D:\source_files\MyApp\util.c @ 541]
0006da04 01029f4e 01069850 0000034f 01069828 MyApp!ShowAssert+0x47 [D:\source_files\MyApp\util.c @ 579]
0006db6c 010590c3 000e01ea 0006fee4 0006feec MyApp!SelectColor+0x103 [D:\source_files\MyApp\colors.c @ 849]
0006fe04 77e11d0a 000e01ea 00000111 0000413c MyApp!MainWndProc+0x1322 [D:\source_files\MyApp\MyApp.c @ 1031]
0006fe24 77e11bc8 01057da1 000e01ea 00000111 USER32!UserCallWinProc+0x18
0006feb0 77e172b4 0006fee4 00000001 010518bf USER32!DispatchMessageWorker+0x2d0
0006febc 010518bf 0006fee4 00000000 01057c5d USER32!DispatchMessageA+0xb
0006fec8 01057c5d 0006fee4 77f82b95 77f83920 MyApp!ProcessQCQPMessage+0x3b [D:\source_files\MyApp\util.c @ 2212]
0006ff70 01062cbf 00000001 00683ed8 00682b88 MyApp!main+0x1e6 [D:\source_files\MyApp\MyApp.c @ 263]
0006ffc0 77e9ca90 77f82b95 77f83920 7ffdf000 MyApp!mainCRTStartup+0xff [D:\source_files\MyApp\crtexe.c @ 338]
0006fff0 00000000 01062bc0 00000000 000000c8 KERNEL32!BaseProcessStart+0x3d
```

The STACK\_TEXT field shows a stack trace of the faulting component.

```dbgcmd
FOLLOWUP_IP: 
MyApp!FatalErrorBox+55
01050963 5e               pop     esi

FOLLOWUP_NAME:  dbg

SYMBOL_NAME:  MyApp!FatalErrorBox+55

MODULE_NAME:  MyApp

IMAGE_NAME:  MyApp.exe

DEBUG_FLR_IMAGE_TIMESTAMP:  383490a9
```

When [**!analyze**](-analyze.md) determines the instruction that has probably caused the error, it displays it in the FOLLOWUP\_IP field. The SYMBOL\_NAME, MODULE\_NAME, IMAGE\_NAME, and DBG\_FLR\_IMAGE\_TIMESTAMP fields show the symbol, module, image name, and image timestamp corresponding to this instruction.

```dbgcmd
STACK_COMMAND:  .ecxr ; kb
```

The STACK\_COMMAND field shows the command that was used to obtain the STACK\_TEXT. You can use this command to repeat this stack trace display, or alter it to obtain related stack information.

```dbgcmd
BUCKET_ID:  80000003_MyApp!FatalErrorBox+55
```

The BUCKET\_ID field shows the specific category of failures that the current failure belongs to. This category helps the debugger determine what other information to display in the analysis output.

```dbgcmd
Followup: dbg
---------
```

For information about the FOLLOWUP\_NAME and the Followup fields, see The Followup Field and the triage.ini File.

There are a variety of other fields that may appear:

-   If control was transferred to an invalid address, then the FAULTING\_IP field will contain this invalid address. Instead of the FOLLOWUP\_IP field, the FAILED\_INSTRUCTION\_ADDRESS field will show the disassembled code from this address, although this disassembly will probably be meaningless. In this situation, the SYMBOL\_NAME, MODULE\_NAME, IMAGE\_NAME, and DBG\_FLR\_IMAGE\_TIMESTAMP fields will refer to the caller of this instruction.

-   If the processor misfires, you may see the SINGLE\_BIT\_ERROR, TWO\_BIT\_ERROR, or POSSIBLE\_INVALID\_CONTROL\_TRANSFER fields.

-   If memory corruption seems to have occurred, the CHKIMG\_EXTENSION field will specify the [**!chkimg**](-chkimg.md) extension command that should be used to investigate.

### <span id="ddk_a_kernel_mode_analyze_v_example_dbg"></span><span id="DDK_A_KERNEL_MODE_ANALYZE_V_EXAMPLE_DBG"></span>A Kernel-Mode !analyze -v Example

In this example, the debugger is attached to a computer that has just crashed.

```dbgcmd
kd> !analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

DRIVER_IRQL_NOT_LESS_OR_EQUAL (d1)
An attempt was made to access a pagable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.  This is usually
caused by drivers using improper addresses.
If kernel debugger is available get stack backtrace.
```

The first element of the display shows the bug check code and information about this type of bug check. Some of the text displayed may not apply to this specific instance. For more details on each bug check, see the [Bug Check Code Reference](bug-check-code-reference2.md) section.

```dbgcmd
Arguments:
Arg1: 00000004, memory referenced
Arg2: 00000002, IRQL
Arg3: 00000001, value 0 = read operation, 1 = write operation
Arg4: f832035c, address which referenced memory
```

The bug check parameters are displayed next. They are each followed by a description. For example, the third parameter is 1, and the comment following it explains that this indicates that a write operation failed.

```dbgcmd
## Debugging Details:


WRITE_ADDRESS:  00000004 Nonpaged pool

CURRENT_IRQL:  2
```

The next few fields vary depending on the nature of the crash. In this case, we see WRITE\_ADDRESS and CURRENT\_IRQL fields. These are simply restating the information shown in the bug check parameters. By comparing the statement "Nonpaged pool" to the bug check text that reads "an attempt was made to access a pagable (or completely invalid) address," we can see that the address was invalid. The invalid address in this case was 0x00000004.

```dbgcmd
FAULTING_IP: 
USBPORT!USBPORT_BadRequestFlush+7c
f832035c 894204           mov     [edx+0x4],eax
```

The FAULTING\_IP field shows the instruction pointer at the time of the fault.

```dbgcmd
DEFAULT_BUCKET_ID:  DRIVER_FAULT
```

The DEFAULT\_BUCKET\_ID field shows the general category of failures that this failure belongs to.

```dbgcmd
BUGCHECK_STR:  0xD1
```

The BUGCHECK\_STR field shows the bug check code, which we have already seen. In some cases additional triage information is appended.

```dbgcmd
TRAP_FRAME:  f8950dfc -- (.trap fffffffff8950dfc)
.trap fffffffff8950dfc
ErrCode = 00000002
eax=81cc86dc ebx=81cc80e0 ecx=81e55688 edx=00000000 esi=81cc8028 edi=8052cf3c
eip=f832035c esp=f8950e70 ebp=f8950e90 iopl=0         nv up ei pl nz ac po nc
cs=0008  ss=0010  ds=0023  es=0023  fs=0030  gs=0000             efl=00010216
USBPORT!USBPORT_BadRequestFlush+7c:
f832035c 894204           mov     [edx+0x4],eax     ds:0023:00000004=????????
.trap
Resetting default context
```

The TRAP\_FRAME field shows the trap frame for this crash. This information can also be viewed by using the [**.trap (Display Trap Frame)**](-trap--display-trap-frame-.md) command.

```dbgcmd
LAST_CONTROL_TRANSFER:  from f83206e0 to f832035c
```

The LAST\_CONTROL\_TRANSFER field shows the last call on the stack. In this case, the code at address 0xF83206E0 called a function at 0xF832035C. You can use the [**ln (List Nearest Symbols)**](ln--list-nearest-symbols-.md) command to determine what module and function these addresses reside in.

```dbgcmd
STACK_TEXT:  
f8950e90 f83206e0 024c7262 00000000 f8950edc USBPORT!USBPORT_BadRequestFlush+0x7c
f8950eb0 804f5561 81cc8644 81cc8028 6d9a2f30 USBPORT!USBPORT_DM_TimerDpc+0x10c
f8950fb4 804f5644 6e4be98e 00000000 ffdff000 nt!KiTimerListExpire+0xf3
f8950fe0 8052c47c 8053cf20 00000000 00002e42 nt!KiTimerExpiration+0xb0
f8950ff4 8052c16a efdefd44 00000000 00000000 nt!KiRetireDpcList+0x31
```

The STACK\_TEXT field shows a stack trace of the faulting component.

```dbgcmd
FOLLOWUP_IP: 
USBPORT!USBPORT_BadRequestFlush+7c
f832035c 894204           mov     [edx+0x4],eax
```

The FOLLOWUP\_IP field shows the disassembly of the instruction that has probably caused the error.

```dbgcmd
FOLLOWUP_NAME:  usbtri

SYMBOL_NAME:  USBPORT!USBPORT_BadRequestFlush+7c

MODULE_NAME:  USBPORT

IMAGE_NAME:  USBPORT.SYS

DEBUG_FLR_IMAGE_TIMESTAMP:  3b7d868b
```

The SYMBOL\_NAME, MODULE\_NAME, IMAGE\_NAME, and DBG\_FLR\_IMAGE\_TIMESTAMP fields show the symbol, module, image, and image timestamp corresponding to this instruction (if it is valid), or to the caller of this instruction (if it is not).

```dbgcmd
STACK_COMMAND:  .trap fffffffff8950dfc ; kb
```

The STACK\_COMMAND field shows the command that was used to obtain the STACK\_TEXT. You can use this command to repeat this stack trace display, or alter it to obtain related stack information.

```dbgcmd
BUCKET_ID:  0xD1_W_USBPORT!USBPORT_BadRequestFlush+7c
```

The BUCKET\_ID field shows the specific category of failures that the current failure belongs to. This category helps the debugger determine what other information to display in the analysis output.

```dbgcmd
INTERNAL_SOLUTION_TEXT:  https://oca.microsoft.com/resredir.asp?sid=62&State=1
```

If you are connected to the internet, the debugger attempts to access a database of crash solutions maintained by Microsoft. This database contains links to a tremendous number of Web pages that have information about known bugs. If a match is found for your problem, the INTERNAL\_SOLUTION\_TEXT field will show a URL that you can access for more information.

```dbgcmd
Followup: usbtri
---------

      This problem has a known fix.
      Please connect to the following URL for details:
      ------------------------------------------------
      https://oca.microsoft.com/resredir.asp?sid=62&State=1
```

For information about the FOLLOWUP\_NAME and the Followup fields, see The Followup Field and the triage.ini File:

There are a variety of other fields that may appear:

-   If control was transferred to an invalid address, then the FAULTING\_IP field will contain this invalid address. Instead of the FOLLOWUP\_IP field, the FAILED\_INSTRUCTION\_ADDRESS field will show the disassembled code from this address, although this disassembly will probably be meaningless. In this situation, the SYMBOL\_NAME, MODULE\_NAME, IMAGE\_NAME, and DBG\_FLR\_IMAGE\_TIMESTAMP fields will refer to the caller of this instruction.

-   If the processor misfires, you may see the SINGLE\_BIT\_ERROR, TWO\_BIT\_ERROR, or POSSIBLE\_INVALID\_CONTROL\_TRANSFER fields.

-   If memory corruption seems to have occurred, the CHKIMG\_EXTENSION field will specify the [**!chkimg**](-chkimg.md) extension command that should be used to investigate.

-   If a bug check occurred within the code of a device driver, its name may be displayed in the BUGCHECKING\_DRIVER field.

### <span id="ddk_the_followup_field_and_the_triage_ini_file_dbg"></span><span id="DDK_THE_FOLLOWUP_FIELD_AND_THE_TRIAGE_INI_FILE_DBG"></span>The Followup Field and the triage.ini File

In both user mode and kernel mode, the Followup field in the display will show information about the owner of the current stack frame, if this can be determined. This information is determined in the following manner:

1.  When the [**!analyze**](-analyze.md) extension is used, the debugger begins with the top frame in the stack and determines whether it is responsible for the error. If it isn't, the next frame is analyzed. This process continues until a frame that might be at fault is found.

2.  The debugger attempts to determine the owner of the module and function in this frame. If the owner can be determined, this frame is considered to be at fault.

3.  If the owner cannot be determined, the debugger passes to the next stack frame, and so on, until the owner is determined (or the stack is completely examined). The first frame whose owner is found in this search is considered to be at fault. If the stack is exhausted without any information being found, no Followup field is displayed.

4.  The owner of the frame at fault is displayed in the Followup field. If **!analyze -v** is used, the FOLLOWUP\_IP, SYMBOL\_NAME, MODULE\_NAME, IMAGE\_NAME, and DBG\_FLR\_IMAGE\_TIMESTAMP fields will refer to this frame.

For the Followup field to display useful information, you must first create a Triage.ini file containing the names of the module and function owners.

The Triage.ini file should identify the owners of all modules that could possibly have errors. You can use an informational string instead of an actual owner, but this string cannot contain spaces. If you are certain that a module will not fault, you can omit this module or indicate that it should be skipped. It is also possible to specify owners of individual functions, giving the triage process an even finer granularity.

For details on the syntax of the Triage.ini file, see [Specifying Module and Function Owners](specifying-module-and-function-owners.md).

### <span id="ddk_additional_analyze_techniques_dbg"></span><span id="DDK_ADDITIONAL_ANALYZE_TECHNIQUES_DBG"></span>Additional !analyze Techniques

If you do not believe that the BUCKET\_ID is correct, you can override the bucket choice by using [**!analyze**](-analyze.md) with the **-D** parameter.

If no crash or exception has occurred, [**!analyze**](-analyze.md) will display a very short text giving the current status of the target. In certain situations you may want to force the analysis to take place as if a crash had occurred. Use **!analyze -f** to accomplish this task.

In user mode, if an exception has occurred but you believe the underlying problem is a hung thread, set the current thread to the thread you are investigating, and then use **!analyze -hang**. This extension will perform a thread stack analysis to determine if any threads are blocking other threads.

In kernel mode, if a bug check has occurred but you believe the underlying problem is a hung thread, use **!analyze -hang**. This extension will investigate locks held by the system and scan the DPC queue chain, and will display any indications of hung threads. If you believe the problem is a kernel-mode resource deadlock, use the [**!deadlock**](-deadlock.md) extension along with the **Deadlock Detection** option of Driver Verifier.

You can also automatically ignore known issues. To do this, you must first create an XML file containing a formatted list of known issues. Use the **!analyze -c -load***KnownIssuesFile* extension to load this file. Then when an exception or break occurs, use the **!analyze -c** extension. If the exception matches one of the known issues, the target will resume execution. If the target does not resume executing, then you can use **!analyze -v** to determine the cause of the problem. A sample XML file can be found in the sdk\\samples\\analyze\_continue subdirectory of the debugger installation directory.

 

 





