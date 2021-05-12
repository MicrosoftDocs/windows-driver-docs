---
title: KsInvalidStreamPointer rule (ks)
description: This rule verifies if a KS miniport driver provides a valid KS Stream Pointer as a function argument.
ms.date: 04/01/2020
keywords: ["KsInvalidStreamPointer rule (ks)"]
topic_type:
- apiref
api_name:
- KsInvalidStreamPointer
api_type:
- NA
ms.localizationpriority: medium
---

# KsInvalidStreamPointer rule (ks)

The **KsInvalidStreamPointer** rule verifies if a KS miniport driver provides a valid KS Stream Pointer as a function argument. Typical violations are caused by incorrect pointer handling or a pointer corruption caused by incorrect use of memory.

A valid stream pointer is a leading or trailing edge stream pointer or a stream pointer that has been cloned via [KsStreamPointerClone](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerclone). For more information see [Leading and Trailing Edge Stream Pointers](../stream/leading-and-trailing-edge-stream-pointers.md).

This rule also verifies that [KsStreamPointerDelete](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerdelete) has not been used to attempt to delete a non-cloned stream pointer.

**Driver model: KS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x0008100C)


## Example


The following code violates this rule.

```cpp
PKKSSTREAM_POINTER StreamPointer = KsPinGetLeadingEdgeStreamPointer (Pin, KSSTREAM_POINTER_STATE_UNLOCKED);

//
// ERROR: KsStreamPointerDelete can only be called on clone stream pointers.
//

KsStreamPointerDelete (StreamPointer);
```

This code also violates the rule. 

```cpp
KsStreamPointerDelete (NULL);
```

## How to test

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
<p></p>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

**verifier /domain ks** \[*options*\] **/driver** *&lt;yourdriver&gt;*

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](./ddi-compliance-checking.md)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

## Applies to

KsStreamPointerDelete

KsStreamPointerAdvance

KsStreamPointerAdvanceOffsetsAndUnlock

KsStreamPointerCancelTimeout

KsStreamPointerGetIrp

KsStreamPointerGetMdl

KsStreamPointerGetNextClone

KsStreamPointerLock

KsStreamPointerScheduleTimeout

KsStreamPointerSetStatusCode

KsStreamPointerUnlock