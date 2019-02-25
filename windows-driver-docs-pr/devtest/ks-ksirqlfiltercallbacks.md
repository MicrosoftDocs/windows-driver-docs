---
title: KsIrqlFilterCallbacks rule ()
description: The KsIrqlFilterCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a KS filter callback function with the same IRQL it had when the callback function was called.
ms.assetid: AC27FF93-DC7C-4287-B3D6-2579FAA65A77
ms.date: 05/21/2018
keywords: ["KsIrqlFilterCallbacks rule ()"]
topic_type:
- apiref
api_name:
- KsIrqlFilterCallbacks
api_type:
- NA
ms.localizationpriority: medium
---

# KsIrqlFilterCallbacks rule ()


The KsIrqlFilterCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a KS filter callback function with the same IRQL it had when the callback function was called.

**Tips for debugging**

When Driver Verifier detects a violation of this rule, it triggers [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187), with an *arg1* value of 0x00081007. The *arg3* (RuleState) and *arg4* (SubState) of the bug check provide pointers to additional information about the rule violation.

Use the [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374) debugger extension to find out what the IRQL values were at function entry and exit.

Use the command:

**!ruleinfo 0x81007** *RuleState* *SubState*.

In the rule state data, the *OldIrql* is the IRQL when the callback is entered. The *NewIrql* is the IRQL when the callback function is exited.

Don't use [**!irql**](https://msdn.microsoft.com/library/windows/hardware/ff563825) to determine the current IRQL because Driver Verifier might have raised IRQL before the bug check. Instead, use **!verifier 0x008** to view the IRQL logs.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00081007) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain ks</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain ks</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





