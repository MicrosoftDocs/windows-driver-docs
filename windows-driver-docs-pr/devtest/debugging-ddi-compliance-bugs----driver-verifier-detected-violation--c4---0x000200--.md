---
title: Debugging DRIVER_VERIFIER_DETECTED_VIOLATION (C4) 0x20002 - 0x20022
description: When you have the DDI compliance checking option selected, and Driver Verifier detects that the driver violates one of the DDI compliance rules, Driver Verifier generates Bug Check 0xC4 DRIVER_VERIFIER_DETECTED_VIOLATION (with Parameter 1 equal to the identifier of the specific compliance rule).
ms.assetid: 9817AC4B-2BE8-44AC-8C9B-DED5EF0A7DD8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging DDI Compliance bugs - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4): 0x20002 - 0x20022


When you have the [DDI compliance checking](ddi-compliance-checking.md) option selected, and Driver Verifier detects that the driver violates one of the DDI compliance rules, [Driver Verifier](driver-verifier.md) generates [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (with Parameter 1 equal to the identifier of the specific compliance rule).

The DDI Compliance rules ensure that a driver correctly interacts with the Windows operating system kernel. For example, the rules verify that your driver makes function calls at the required IRQL for the function, or that the driver correctly acquires and releases spin locks. This section describes some example strategies for debugging these violations.

## Debugging DDI compliance checking violations


-   [Use !analyze to display information about the bug check](#use-analyze-to-display-information-about-the-bug-check)
-   [Use the !ruleinfo extension command](#use-the-ruleinfo-extension-command)
-   [Use the !analyze –v command to identify the location of the violation in source code](#use-the-analyze-v-command-to-identify-the-location-of-the-violation-in-source-code)
-   [Fixing the cause of the DDI compliance violation](#fixing-the-cause-of-the-ddi-compliance-violation)

### Use !analyze to display information about the bug check

As with any bug check that occurs, once you have control of the debugger, the best first step is to run the [**!analyze -v**](https://msdn.microsoft.com/library/windows/hardware/ff562112) command.

```
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
Arg1: 00020004, ID of the 'IrqlExAllocatePool' rule that was violated.
Arg2: 8481c118, A pointer to the string describing the violated rule condition.
Arg3: 00000000, Reserved (unused).
Arg4: 00000000, Reserved (unused).

## Debugging Details:


DV_VIOLATED_CONDITION:  ExAllocatePoolWithTagPriority should only be called at IRQL <= DISPATCH_LEVEL.

DV_MSDN_LINK: http://go.microsoft.com/fwlink/p/?linkid=216021

DV_RULE_INFO: 0x20004
```

Whenever [Driver Verifier](driver-verifier.md) catches a [DDI compliance checking](ddi-compliance-checking.md) violation, information about the violation will be provided in the [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112) output.

In this example, [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) has a parameter 1 (Arg1) value of 0x20004, which indicates that the driver has violated the [**IrqlExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff547747) compliance rule.

The [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112) output includes the following information:

**DV\_VIOLATED\_CONDITION:** This field provides a description of what caused the rule violation. In this example, the condition violated was that a driver attempted to allocate memory at a very high IRQL level, or attempted to allocated paged pool memory at DISPATCH\_LEVEL. For example, this may have been a driver that was attempting to call [**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523) in an Interrupt Service Routine (ISR), or a driver that attempted to allocate paged pool memory while holding a spin lock.

**DV\_MSDN\_LINK:** In WinDBG, this is a live link that causes the debugger to open the MSDN page showing more information about the [**IrqlExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff547747) rule.

**DV\_RULE\_INFO:** In WinDBG, this is a live link that will show information about this rule from the help available on the debugger.

### Use the !ruleinfo extension command

The **DV\_RULE\_INFO:** field of the **!analyze** output shows the command you can use to find more information about this rule violation. For this example, you can use the command: **!ruleinfo 0x20004**

```
kd> !ruleinfo 0x20004

RULE_ID: 0x20004

RULE_NAME: IrqlExAllocatePool

RULE_DESCRIPTION:
The IrqlExAllocatePool rule specifies that the driver calls:
ExAllocatePool,
ExAllocatePoolWithTag,
ExAllocatePoolWithQuota,
ExAllocatePoolWithQuotaTag and
ExAllocatePoolWithTagPriority
only when it is executing at IRQL <= DISPATCH_LEVEL. A caller
executing at DISPATCH_LEVEL must specify a NonPagedXxx value
for PoolType. A caller executing at IRQL <= APC_LEVEL can
specify any POOL_TYPE value.

MSDN_LINK: http://go.microsoft.com/fwlink/p/?linkid=216021
```

### Use the !analyze-v command to identify the location of the violation in source code

When this violation is caught, Driver Verifier will bug check the system immediately. The **!analyze** output will show the current IRQL, current stack, point where the call to allocate memory was made, and if source-code enabled The **!analyze –v** (for verbose) output will also show the source file and line number where the allocation request was made:

```
CURRENT_IRQL:  10

ANALYSIS_VERSION: 6.13.0016.1929 (debuggers(dbg).130725-1857) amd64fre

LAST_CONTROL_TRANSFER:  from 80ff159d to 80f751f4

STACK_TEXT:  
82f9eaa4 81dda59d 00000003 86fab4b0 00000065 nt!RtlpBreakWithStatusInstruction
82f9eaf8 81dda0b7 82fa0138 82f9eef8 82f9ef40 nt!KiBugCheckDebugBreak+0x1f
82f9eecc 81d5cdc6 000000c4 00020004 85435118 nt!KeBugCheck2+0x676
82f9eef0 81d5ccfd 000000c4 00020004 85435118 nt!KiBugCheck2+0xc6
82f9ef10 8542cb4e 000000c4 00020004 85435118 nt!KeBugCheckEx+0x19
82f9ef30 85425ded ffffffff 85425e0d 82f9ef60 VerifierExt!SLIC_abort+0x40
82f9ef38 85425e0d 82f9ef60 8210c19e 00000080 VerifierExt!SLIC_ExAllocatePoolWithTagPriority_internal_entry_IrqlExAllocatePool+0x6f
82f9ef40 8210c19e 00000080 00000000 00000000 VerifierExt!ExAllocatePoolWithTagPriority_internal_wrapper+0x19
82f9ef60 826c9e16 00000000 00000000 00000000 nt!VerifierExAllocatePoolWithTag+0x24
82f9efa8 81d0726c 833cba80 8a4b9480 00000000 MyDriver!HandleISR+0x146
82f9efbc 81d071c1 833cba80 8a4b9480 000000b8 nt!KiInterruptMessageDispatch+0x12
82f9efe4 81d71f29 00000001 525b61ea 00000224 nt!KiCallInterruptServiceRoutine+0x6d
82f9efe8 00000000 525b61ea 00000224 00000000 nt!KiInterruptDispatch+0x49

STACK_COMMAND:  kb

FOLLOWUP_IP: 
MyDriver!HandleISR+0x140
826c9e10 ff154440699b    call    dword ptr [IrqlExAllocatePool_ExAllocatePoolWithTag!_imp__ExAllocatePoolWithTag (9b694044)]

FAULTING_SOURCE_LINE:  d:\drvsrc\mydriver\isrhandler.c

FAULTING_SOURCE_FILE:  d:\drvsrc\mydriver\isrhandler.c

FAULTING_SOURCE_LINE_NUMBER:  206
```

### Fixing the cause of the DDI compliance violation

Fixing these bug checks that have Arg1 values in the range 0x00020000 to 0x00020022, generally consists of verifying the driver meets the API and DDI usage conditions described in the corresponding documentation.

In the example we've used here (0x20004), a memory allocation of any sort in the ISR is going to violate the IRQL rules set for the [**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523) routine.

In general, you should review the documentation about the routine for information about IRQL and proper usage. Review the specific [DDI Compliance Rules](https://msdn.microsoft.com/library/windows/hardware/ff552840) that test the function. In this case, the rule is [**IrqlExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff547747).

Use [Static Driver Verifier](static-driver-verifier.md) to analyze your driver source code, using the same rule(s). Static Driver Verifier is a tool that scans Windows driver source code and reports on possible issues by simulating the exercising of various code paths. Static Driver Verifier is an excellent development-time utility to help identify these kinds of issues.

## Related topics


[DDI compliance checking](ddi-compliance-checking.md)

[DDI Compliance Rules](https://msdn.microsoft.com/library/windows/hardware/ff552840)

[Static Driver Verifier](static-driver-verifier.md)

[**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187)

 

 






