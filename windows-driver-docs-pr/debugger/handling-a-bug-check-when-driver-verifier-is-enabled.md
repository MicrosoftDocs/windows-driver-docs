---
title: Handling a Bug Check When Driver Verifier is Enabled
description: Driver Verifier detects driver errors at run time. You can use Driver Verifier along with the analyze debugger command to detect and display information about errors in your driver.
ms.assetid: 4226B62B-0AA5-4D04-A32D-7DD22FD694E3
keywords: ["Driver Verifier", "Verifier"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Handling a Bug Check When Driver Verifier is Enabled


[Driver Verifier](https://go.microsoft.com/fwlink/p?LinkID=268663) detects driver errors at run time. You can use Driver Verifier along with the [**!analyze**](-analyze.md) debugger command to detect and display information about errors in your driver.

In Windows 8, [Driver Verifier](https://go.microsoft.com/fwlink/p?LinkID=268663) has been enhanced with new features, including [DDI Compliance Checking](https://go.microsoft.com/fwlink/p?LinkID=268676). Here we give an example that demonstrates DDI Compliance Checking.

Use the following procedure to get set up.

1.  Establish a kernel-mode debugging session between a host and target computer.
2.  Install your driver on the target computer.
3.  On the target computer, open a Command Prompt window and enter the command **verifier**. Use [Driver Verifier Manager](https://go.microsoft.com/fwlink/p?LinkID=268659) to enable Driver Verifier for your driver.
4.  Reboot the target computer.

When Driver Verifier detects an error, it generates a bug check. Then Windows breaks into the debugger and displays a brief description of the error. Here is an example where Driver Verifier generates Bug Check [**DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4)**](bug-check-0xc4--driver-verifier-detected-violation.md).

```dbgcmd
Driver Verifier: Extension abort with Error Code 0x20005
Error String ExAcquireFastMutex should only be called at IRQL <= APC_LEVEL.

*** Fatal System Error: 0x000000c4
                       (0x0000000000020005,0xFFFFF88000E16F50,0x0000000000000000,0x0000000000000000)

Break instruction exception - code 80000003 (first chance)

A fatal system error has occurred.
Debugger entered on first try; Bugcheck callbacks have not been invoked.

A fatal system error has occurred.

nt!DbgBreakPointWithStatus:
fffff802`a40ef930 cc              int     3
```

In the debugger, enter [**!analyze -v**](-analyze.md) to get a detailed description of the error.

```dbgcmd
0: kd> !analyze -v
Connected to Windows 8 9200 x64 target at (Thu Oct 11 13:48:31.270 2012 (UTC - 7:00)), ptr64 TRUE
Loading Kernel Symbols
...............................................................
................................................................
...................
Loading User Symbols
..................................................
Loading unloaded module list
............
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

DRIVER_VERIFIER_DETECTED_VIOLATION (c4)
A device driver attempting to corrupt the system has been caught.  This is
because the driver was specified in the registry as being suspect (by the
administrator) and the kernel has enabled substantial checking of this driver.
If the driver attempts to corrupt the system, bugchecks 0xC4, 0xC1 and 0xA will
be among the most commonly seen crashes.
Arguments:
Arg1: 0000000000020005, ID of the 'IrqlExApcLte1' rule that was violated.
Arg2: fffff88000e16f50, A pointer to the string describing the violated rule condition.
Arg3: 0000000000000000, An optional pointer to the rule state variable(s).
Arg4: 0000000000000000, Reserved (unused)

## Debugging Details:

...

DV_VIOLATED_CONDITION:  ExAcquireFastMutex should only be called at IRQL <= APC_LEVEL.

DV_MSDN_LINK: !url https://go.microsoft.com/fwlink/p/?linkid=216022

DV_RULE_INFO: !ruleinfo 0x20005

BUGCHECK_STR:  0xc4_IrqlExApcLte1_XDV

DEFAULT_BUCKET_ID:  WIN8_DRIVER_FAULT

PROCESS_NAME:  TiWorker.exe

CURRENT_IRQL:  9
```

In the preceding output, you can see the name and description of the rule, **IrqlExApcLte1**, that was violated, and you can click a link to the reference page that describes the rule: <https://go.microsoft.com/fwlink/p/?linkid=216022>. You can also click a debugger command link, **!ruleinfo 0x20005**, to get information about the rule. In this case, the rule states that you cannot call [ExAcquireFastMutex](https://go.microsoft.com/fwlink/p?LinkID=268628) if the interrupt request level (IRQL) is greater than APC\_LEVEL. The output shows that the current IRQL is 9, and in wdm.h you can see that APC\_LEVEL has a value of 1. For more information about IRQLs, see [Managing Hardware Priorities](https://go.microsoft.com/fwlink/p?LinkID=268625).

The output of [**!analyze -v**](-analyze.md) continues with a stack trace and information about the code that caused the error. In the following output, you can see that the **OnInterrupt** routine in MyDriver.sys called [ExAcquireFastMutex](https://go.microsoft.com/fwlink/p?LinkID=268628). **OnInterrupt** is an interrupt service routine that runs at an IRQL greater than APC\_LEVEL, so it is a violation for this routine to call [ExAcquireFastMutex](https://go.microsoft.com/fwlink/p?LinkID=268628).

```dbgcmd
LAST_CONTROL_TRANSFER:  from fffff802a41f00ea to fffff802a40ef930

STACK_TEXT:  
... : nt!DbgBreakPointWithStatus ...
... : nt!KiBugCheckDebugBreak+0x12 ...
... : nt!KeBugCheck2+0x79f ...
... : nt!KeBugCheckEx+0x104 ...
... : VerifierExt!SLIC_abort+0x47 ...
... : VerifierExt!SLIC_ExAcquireFastMutex_entry_irqlexapclte1+0x25 ...
... : VerifierExt!ExAcquireFastMutex_wrapper+0x1a ...
... : nt!ViExAcquireFastMutexCommon+0x1d ...
... : nt!VerifierExAcquireFastMutex+0x1a ...
... : MyDriver!OnInterrupt+0x69 ...
... : nt!KiScanInterruptObjectList+0x6f ...
... : nt!KiChainedDispatch+0x19a ...
...

STACK_COMMAND:  kb

FOLLOWUP_IP: 
MyDriver!OnInterrupt+69 ...
fffff880`16306649 4c8d0510040000  lea     r8,[MyDriver! ?? ::FNODOBFM::`string' (fffff880`16306a60)]

FAULTING_SOURCE_LINE:  c:\MyDriverwdm03\cpp\MyDriver\pnp.c

FAULTING_SOURCE_FILE:  c:\MyDriverwdm03\cpp\MyDriver\pnp.c

FAULTING_SOURCE_LINE_NUMBER:  26

FAULTING_SOURCE_CODE:  
    22:    if(1 == interruptStatus)
    23:    {
    24:       ...
    25:       ExAcquireFastMutex( &(fdoExt->fastMutex) );
>   26:       ...
    27:       ExReleaseFastMutex( &(fdoExt->fastMutex) );
    28:       ...
    29:       return TRUE;
    30:    }
    31:    else


SYMBOL_STACK_INDEX:  9

SYMBOL_NAME:  MyDriver!OnInterrupt+69

FOLLOWUP_NAME:  ...

MODULE_NAME: MyDriver

IMAGE_NAME:  MyDriver.sys

DEBUG_FLR_IMAGE_TIMESTAMP:  50772f37

BUCKET_ID_FUNC_OFFSET:  69

FAILURE_BUCKET_ID:  0xc4_IrqlExApcLte1_XDV_VRF_MyDriver!OnInterrupt

BUCKET_ID:  0xc4_IrqlExApcLte1_XDV_VRF_MyDriver!OnInterrupt
```

## <span id="related_topics"></span>Related topics


[Static Driver Verifier](https://go.microsoft.com/fwlink/p?LinkID=268668)

 

 






