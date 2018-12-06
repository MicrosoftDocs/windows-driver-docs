---
title: Debugging DRIVER_VERIFIER_DETECTED_VIOLATION (C4)
description: Driver Verifier detects that the driver violates one of the NDIS/WiFi time-out rule.
ms.assetid: 73D4B6DF-E667-4C71-B985-FCDC05837908
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging NDIS/WiFi time-out errors - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4)


When you have the [NDIS/WIFI verification](ndis-wifi-verification.md) option selected, and Driver Verifier detects that the driver violates one of the NDIS/WiFi time-out rules, [Driver Verifier](driver-verifier.md) generates [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (with Parameter 1 equal to the identifier of the specific NDIS/WiFi time-out rule).

When Driver Verifier is testing a NDIS/WIFI time-out rule, such as [**NdisTimedOidComplete**](https://msdn.microsoft.com/library/windows/hardware/dn305120), Driver Verifier’s polling mechanism expects a response from the miniport driver within a number of cycles. Each timed rule has defined its own maximum cycle allowed. When the maximum is exceeded, Driver Verifier generates a bug check. This section describes some example strategies for debugging these violations.

## Debugging NDIS/WIFI timeout errors


-   [Use !analyze to display information about the bug check](#use-analyze-to-display-information-about-the-bug-check)
-   [Use the !ruleinfo extension command](#use-the-ruleinfo-extension-command)
-   [Click the LAST\_CALL\_STACK link to identify the location of the violation](#identify-the-location-of-the-violation)
-   [Fixing the cause of the NDIS/WIFI timeout violation](#fixing-the-cause-of-the-ndis-wifi-timeout-violation)

### Use !analyze to display information about the bug check

As with any bug check that occurs, once you have control of the debugger, the best first step is to run the [**!analyze -v**](https://msdn.microsoft.com/library/windows/hardware/ff562112) command.

```
DRIVER_VERIFIER_DETECTED_VIOLATION (c4)
A device driver attempting to corrupt the system has been caught.  This is
because the driver was specified in the registry as being suspect (by the
administrator) and the kernel has enabled substantial checking of this driver.
If the driver attempts to corrupt the system, bugchecks 0xC4, 0xC1 and 0xA will
be among the most commonly seen crashes.
Arguments:
Arg1: 00092003, ID of the 'NdisTimedOidComplete' rule that was violated.
Arg2: 8521dd34, A pointer to the string describing the violated rule condition.
Arg3: 9c17b860, Address of internal rule state (second argument to !ruleinfo).
Arg4: 9c1f3480, Address of supplemental states (third argument to !ruleinfo).
```

In the following section of the **!analyze -v** output, the reason why the rule was violated under is shown under the DV\_VIOLATED\_CONDITION field. The DV\_MSDN\_LINK section is also useful to pull up a link to documentation on this rule.

```
## Debugging Details:


*** ERROR: Module load completed but symbols could not be loaded for NdisTimedOidComplete.sys

DV_VIOLATED_CONDITION:  Timeout on completing an NDIS OID request.

DV_MSDN_LINK: http://go.microsoft.com/fwlink/p/?linkid=278804

DRIVER_OBJECT: 98a87980

IMAGE_NAME:  NdisTimedOidComplete.sys

DEBUG_FLR_IMAGE_TIMESTAMP:  5229c857

MODULE_NAME: NdisTimedOidComplete

FAULTING_MODULE: 9fee1000 NdisTimedOidComplete
```

Further down this analysis output, you can click on the link under the DV\_RULE\_INFO section for additional rule descriptions. For time-out type of rules, the current stack might not contain relevant information.

```
DV_RULE_INFO: 0x92003

BUGCHECK_STR:  0xc4_NdisTimedOidComplete_XDV

DEFAULT_BUCKET_ID:  WIN8_DRIVER_FAULT

PROCESS_NAME:  System

CURRENT_IRQL:  2

ANALYSIS_VERSION: 6.13.0016.1929 (debuggers(dbg).130725-1857) amd64fre

LAST_CONTROL_TRANSFER:  from 80f87fd3 to 80f0ed14

STACK_TEXT:  
8912380c 80f87fd3 00000003 e6c3476e 00000065 nt!RtlpBreakWithStatusInstruction
89123860 80f87aed 825a6138 89123c5c 89123cac nt!KiBugCheckDebugBreak+0x1f
89123c30 80f0d8d6 000000c4 00092003 8521dd34 nt!KeBugCheck2+0x676
89123c54 80f0d80d 000000c4 00092003 8521dd34 nt!KiBugCheck2+0xc6
89123c74 85211584 000000c4 00092003 8521dd34 nt!KeBugCheckEx+0x19
89123cac 85216d54 9c17b860 9c1f3480 9c17b8dc VerifierExt!SLIC_StatefulAbort+0x1a4
89123cd0 85216ffe 85220000 85215f5b 00000000 VerifierExt!Ndis_OnTimerExpire+0x234
89123cd8 85215f5b 00000000 80ecd56a 843d0c38 VerifierExt!CheckOnTimerExpire+0x26
89123ce0 80ecd56a 843d0c38 00000000 80ecd502 VerifierExt!XdvPassiveTimerRoutine+0x1d
89123d24 80eec133 882befd0 00000000 887debc0 nt!IopProcessWorkItem+0x68
89123d70 80ec1162 00000000 e6c342be 00000000 nt!ExpWorkerThread+0x14f
89123db0 80f23201 80eebfe4 00000000 00000000 nt!PspSystemThreadStartup+0x58
89123dbc 00000000 00000000 00000000 00000000 nt!KiThreadStartup+0x15
```

### Use the !ruleinfo extension command

The **DV\_RULE\_INFO:** field of the **!analyze** output shows a link to the command you can use to find more information about this rule violation. For this example, if you click the link, it runs the [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374) command with the RULE\_ID (0x92003) the Arg3 and Arg 4 bug check values.

```
kd> !ruleinfo 0x92003 0xffffffff9c17b860 0xffffffff9c1f3480

RULE_ID: 0x92003

RULE_NAME: NdisTimedOidComplete

RULE_DESCRIPTION:
This rule verifies if an NDIS miniport driver completes an OID in time.
The OID is tracked (a.k.a., TRACKED_OBJECT). Use !ndiskd.oid .

MSDN_LINK: http://go.microsoft.com/fwlink/p/?linkid=278804

CONTEXT: Miniport 0x86BD10E8

CURRENT_TIME (Timed Rules): 168 seconds

TRACKED_OBJECT: 0x86633804

LAST_CALL_STACK: 0x9C1F3480 + 0x10

RULE_STATE: 0x9C1F3480
```

### Identify the location of the violation

In the example we are using here, the miniport driver, NdisTimedOidComplete.sys, has a sleep cycle injected into its *MPOidRequest* function. We can check by clicking on the LAST\_CALL\_STACK link in the [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374) output. This is the last call stack seen by Driver Verifier, where we see that NDIS called *ndisMInvokeOidRequest* before the time out occurred.

```
kd> dps 0x9C1F3480 + 0x10
9c1f3490  850e1e37 ndis!ndisMInvokeOidRequest+0x16641
9c1f3494  850765c8 ndis!ndisMDoOidRequest+0x24a
9c1f3498  8507552a ndis!ndisQueueOidRequest+0x2fa
9c1f349c  8507372b ndis!ndisQuerySetMiniportEx+0xd9
9c1f34a0  85073646 ndis!ndisQuerySetMiniport+0x18
9c1f34a4  850dd9c8 ndis!ndisMDoMiniportOp+0x8c
9c1f34a8  850dd916 ndis!ndisMNotifyMachineName+0xe4
9c1f34ac  85104005 ndis!ndisMInitializeAdapter+0xad7
```

### Fixing the cause of the NDIS WIFI timeout violation

When the crash dump has been generated for a timed rule, there is a possibility that the root cause can be found at the time of the crash dump. To debug further, consider starting with the NdisKd debugger extension commands, see [NDIS Extensions (Ndiskd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff552270) and [Getting started with NDISKD](http://go.microsoft.com/fwlink/p/?linkid=327569). You may also need to look at [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md) logs, if your driver has implemented ETW. If this rule were not enabled, this error will manifest itself as user application hang at best, or a [**Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE**](https://msdn.microsoft.com/library/windows/hardware/ff559329) at the worst.

## <span id="related_topics"></span>Related topics


[NDIS Extensions (Ndiskd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff552270)

[Getting started with NDISKD (part 1)](http://go.microsoft.com/fwlink/p/?linkid=327569)

[NDISKD and !miniport (part 2)]( http://go.microsoft.com/fwlink/p/?linkid=327570)

[Debugging with NDISKD (part 3)](http://go.microsoft.com/fwlink/p/?linkid=327571)










