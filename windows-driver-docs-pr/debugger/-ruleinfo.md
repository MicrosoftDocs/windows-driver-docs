---
title: ruleinfo
description: The ruleinfo command displays information about a Driver Verifier rule.
ms.assetid: 025FAAFA-7A5C-462C-9CC2-AA55530CD371
keywords: ["ruleinfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ruleinfo
api_type:
- NA
---

# !ruleinfo


The **!ruleinfo** command displays information about a Driver Verifier rule.

```
!ruleinfo RuleId [RuleState [SubState]]
```

## <span id="ddk__ptov_dbg"></span><span id="DDK__PTOV_DBG"></span>Parameters


<span id="_______RuleId______"></span><span id="_______ruleid______"></span><span id="_______RULEID______"></span> *RuleId*   
The ID of the verifier rule. This is the first argument of the [**DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](bug-check-0xc4--driver-verifier-detected-violation.md) bug check.

<span id="_______RuleState______"></span><span id="_______rulestate______"></span><span id="_______RULESTATE______"></span> *RuleState*   
Additional state information about the violation. This is the third argument of the **DRIVER\_VERIFIER\_DETECTED\_VIOLATION** bug check.

<span id="_______SubState______"></span><span id="_______substate______"></span><span id="_______SUBSTATE______"></span> *SubState*   
Sub-state information about the violation. This is the fourth argument of the **DRIVER\_VERIFIER\_DETECTED\_VIOLATION** bug check.

### <span id="DLL"></span><span id="dll"></span>DLL

ext.dll

Remarks
-------

This command applies only to rules in the Driver Verifier extension; that is, rules that have an ID greater than or equal to 0x10000.

The following example shows the four arguments of a [**DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](bug-check-0xc4--driver-verifier-detected-violation.md) bug check.

```
DRIVER_VERIFIER_DETECTED_VIOLATION (c4)
...
Arguments:
Arg1: 0000000000091001, ID of the 'NdisOidComplete' rule that was violated.
Arg2: fffff800002d49d0, A pointer to the string describing the violated rule condition.
Arg3: ffffe000027b8370, Address of internal rule state (second argument to !ruleinfo).
Arg4: ffffe000027b83f8, Address of supplemental states (third argument to !ruleinfo).

## Debugging Details:


DV_VIOLATED_CONDITION:  This OID should only be completed with NDIS_STATUS_NOT_ACCEPTED, 
                        NDIS_STATUS_SUCCESS, or NDIS_STATUS_PENDING.

DV_MSDN_LINK: http://go.microsoft.com/fwlink/p/?linkid=278802

DRIVER_OBJECT: ffffe0000277a2b0
...

STACK_TEXT:  
ffffd000`2118ff58 fffff803`4c83afa2 : 00000000`000000c4 00000000`00000001 ...
ffffd000`2118ff60 fffff803`4c83a8c0 : 00000000`00000003 00000000`00091001 ...
...

STACK_COMMAND:  kb

FOLLOWUP_NAME:  Xxxx

FAILURE_BUCKET_ID:  Xxxx
...
```

In the preceding output, the rule ID (0x91001) is shown as Arg1. Arg3 and Arg4 are the addresses of rule state and substate information. You can pass the rule ID, the rule state, and the substate to **!ruleinfo** to get a description of the rule and a link to detailed documentation of the rule.

```
3: kd> !ruleinfo 0x91001 0xffffe000027b8370 0xffffe000027b83f8

RULE_ID: 0x91001

RULE_NAME: NdisOidComplete

RULE_DESCRIPTION:
This rule verifies if an NDIS miniport driver completes an OID correctly.
Check RULE_STATE for Oid ( use !ndiskd.oid ), which can be one of the following:
1) NULL,
2) Pending OID, or
3) Previous OID if no OID is pending.

MSDN_LINK: http://go.microsoft.com/fwlink/p/?linkid=278802

CONTEXT: Miniport 0xFFFFE0000283F1A0

CURRENT_TIME (Timed Rules): 142 seconds

RULE_STATE: 0xFFFFE000027B83F8
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ruleinfo%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




