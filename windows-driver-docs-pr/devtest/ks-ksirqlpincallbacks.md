---
title: KsIrqlPinCallbacks rule ()
description: The KsIrqlPinCallbacks rule specifies that a kernel-stream (KS) miniport driver returns from a KS Pin callback function with the same IRQL that it had when it was called.
ms.assetid: B2C1413A-9B94-499A-A15C-A943065F7CA1
keywords: ["KsIrqlPinCallbacks rule ()"]
topic_type:
- apiref
api_name:
- KsIrqlPinCallbacks
api_type:
- NA
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
<p>For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20KsIrqlPinCallbacks%20rule%20%28%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




