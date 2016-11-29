---
title: Debugging NDIS/WiFi time-out errors - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4)
description: When you have the NDIS/WIFI verification option selected, and Driver Verifier detects that the driver violates one of the NDIS/WiFi time-out rules, Driver Verifier generates Bug Check 0xC4 DRIVER\_VERIFIER\_DETECTED\_VIOLATION (with Parameter 1 equal to the identifier of the specific NDIS/WiFi time-out rule).
ms.assetid: 73D4B6DF-E667-4C71-B985-FCDC05837908
---

# <span id="devtest.debugging_ndis_wifi_timeouts_-_driver_verifier_detected_violation__c4___0x92003__etc_"></span>Debugging NDIS/WiFi time-out errors - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4)


When you have the [NDIS/WIFI verification](ndis-wifi-verification.md) option selected, and Driver Verifier detects that the driver violates one of the NDIS/WiFi time-out rules, [Driver Verifier](driver-verifier.md) generates [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (with Parameter 1 equal to the identifier of the specific NDIS/WiFi time-out rule).

When Driver Verifier is testing a NDIS/WIFI time-out rule, such as [**NdisTimedOidComplete**](https://msdn.microsoft.com/library/windows/hardware/dn305120), Driver Verifier’s polling mechanism expects a response from the miniport driver within a number of cycles. Each timed rule has defined its own maximum cycle allowed. When the maximum is exceeded, Driver Verifier generates a bug check. This section describes some example strategies for debugging these violations.

## <span id="Debugging_NDIS_WIFI_time-out_errors"></span><span id="debugging_ndis_wifi_time-out_errors"></span><span id="DEBUGGING_NDIS_WIFI_TIME-OUT_ERRORS"></span>Debugging NDIS/WIFI time-out errors


-   [Use !analyze to display information about the bug check](#use--analyze-to-display-information-about-the-bug-check)
-   [Use the !ruleinfo extension command](#use-the--ruleinfo-extension-command-)
-   [Click the LAST\_CALL\_STACK link to identify the location of the violation](#click-the-last-call-stack-link-to--identify-the-location-of-the-violation)
-   [Fixing the cause of the NDIS/WIFI time-out violation](#fixing-the-cause-of-the-ndis-wifi-time-out-violation)

### <span id="Use__analyze_to_display_information_about_the_bug_check"></span><span id="use__analyze_to_display_information_about_the_bug_check"></span><span id="USE__ANALYZE_TO_DISPLAY_INFORMATION_ABOUT_THE_BUG_CHECK"></span>Use !analyze to display information about the bug check

As with any bug check that occurs, once you have control of the debugger, the best first step is to run the [**!analyze -v**](https://msdn.microsoft.com/library/windows/hardware/ff562112) command.

``` syntax
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

``` syntax
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

``` syntax
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

### <span id="Use_the__ruleinfo_extension_command_"></span><span id="use_the__ruleinfo_extension_command_"></span><span id="USE_THE__RULEINFO_EXTENSION_COMMAND_"></span>Use the !ruleinfo extension command

The **DV\_RULE\_INFO:** field of the **!analyze** output shows a link to the command you can use to find more information about this rule violation. For this example, if you click the link, it runs the [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374) command with the RULE\_ID (0x92003) the Arg3 and Arg 4 bug check values.

``` syntax
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

### <span id="Click_the_LAST_CALL_STACK_link_to__identify_the_location_of_the_violation"></span><span id="click_the_last_call_stack_link_to__identify_the_location_of_the_violation"></span><span id="CLICK_THE_LAST_CALL_STACK_LINK_TO__IDENTIFY_THE_LOCATION_OF_THE_VIOLATION"></span>Click the LAST\_CALL\_STACK link to identify the location of the violation

In the example we are using here, the miniport driver, NdisTimedOidComplete.sys, has a sleep cycle injected into its *MPOidRequest* function. We can check by clicking on the LAST\_CALL\_STACK link in the [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374) output. This is the last call stack seen by Driver Verifier, where we see that NDIS called *ndisMInvokeOidRequest* before the time out occurred.

``` syntax
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

### <span id="Fixing_the_cause_of_the_NDIS_WIFI_time-out_violation"></span><span id="fixing_the_cause_of_the_ndis_wifi_time-out_violation"></span><span id="FIXING_THE_CAUSE_OF_THE_NDIS_WIFI_TIME-OUT_VIOLATION"></span>Fixing the cause of the NDIS/WIFI time-out violation

When the crash dump has been generated for a timed rule, there is a possibility that the root cause can be found at the time of the crash dump. To debug further, consider starting with the NdisKd debugger extension commands, see [NDIS Extensions (Ndiskd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff552270) and [Getting started with NDISKD](http://go.microsoft.com/fwlink/p/?linkid=327569). You may also need to look at [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md) logs, if your driver has implemented ETW. If this rule were not enabled, this error will manifest itself as user application hang at best, or a [**Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE**](https://msdn.microsoft.com/library/windows/hardware/ff559329) at the worst.

## <span id="related_topics"></span>Related topics


[NDIS Extensions (Ndiskd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff552270)

[Getting started with NDISKD (part 1)](http://go.microsoft.com/fwlink/p/?linkid=327569)

[NDISKD and !miniport (part 2)]( http://go.microsoft.com/fwlink/p/?linkid=327570)

[Debugging with NDISKD (part 3)](http://go.microsoft.com/fwlink/p/?linkid=327571)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Debugging%20NDIS/WiFi%20time-out%20errors%20-%20DRIVER_VERIFIER_DETECTED_VIOLATION%20%28C4%29%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





