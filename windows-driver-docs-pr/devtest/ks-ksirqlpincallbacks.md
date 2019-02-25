---
title: KsIrqlPinCallbacks rule ()
description: The KsIrqlPinCallbacks rule specifies that a kernel-stream (KS) miniport driver returns from a KS Pin callback function with the same IRQL that it had when it was called.
ms.assetid: B2C1413A-9B94-499A-A15C-A943065F7CA1
ms.date: 05/21/2018
keywords: ["KsIrqlPinCallbacks rule ()"]
topic_type:
- apiref
api_name:
- KsIrqlPinCallbacks
api_type:
- NA
ms.localizationpriority: medium
---

# KsIrqlPinCallbacks rule ()


The KsIrqlPinCallbacks rule specifies that a kernel-stream (KS) miniport driver returns from a KS Pin callback function with the same IRQL that it had when it was called.

**Tips for debugging**

When Driver Verifier detects a violation of this rule, it triggers [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187), with an *arg1* value of 0x00081008. The *arg3* (RuleState) and *arg4* (SubState) of the bug check provide pointers to additional information about the rule violation.

Use the [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374) debugger extension to find out what the IRQL values were at function entry and exit.

Use the command:

**!ruleinfo 0x81008** *RuleState* *SubState*.

In the rule state data, the *OldIrql* is the IRQL when the callback is entered. The *NewIrql* is the IRQL when the callback function is exited.

Don't use [**!irql**](https://msdn.microsoft.com/library/windows/hardware/ff563825) to determine the current IRQL because Driver Verifier might have raised IRQL before the bug check. Instead, use **!verifier 0x008** to view the IRQL logs.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00081008) |

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

 

 

 





