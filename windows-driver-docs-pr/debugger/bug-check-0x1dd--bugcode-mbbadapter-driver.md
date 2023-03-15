---
title: Bug Check 0x1DD BUGCODE_MBBADAPTER_DRIVER
description: The BUGCODE_MBBADAPTER_DRIVER bug check has a value of 0x000001DD. This indicates that the operating system encountered an error caused by a networking driver managed by MbbAdapterCx.
keywords: ["Bug Check 0x1DD BUGCODE_MBBADAPTER_DRIVER", "BUGCODE_MBBADAPTER_DRIVER"]
ms.date: 10/05/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- BUGCODE_MBBADAPTER_DRIVER
api_type:
- NA
---

# Bug Check 0x1DD: BUGCODE\_MBBADAPTER\_DRIVER

The BUGCODE\_MBBADAPTER\_DRIVER bug check has a value of 0x000001DD. This indicates that the operating system encountered an error caused by a networking driver managed by MBBCx. MBBCx provides mobile broadband (MBB) media-specific functionality in the form of a KMDF-based MBB client driver for MBB devices. For more information, see [Introduction to the Mobile Broadband (MBB) WDF class extension (MBBCx)](../netcx/mobile-broadband-mbb-wdf-class-extension-mbbcx.md).

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## BUGCODE\_MBBADAPTER\_DRIVER Parameters

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>One of the following failure codes</p>
<p>0 - FailureCode_CorruptedPrivateGlobals</p>
<p>1 - FailureCode_IrqlIsNotPassive</p>
<p>2 - FailureCode_IrqlNotLessOrEqualDispatch</p>
<p>3 - FailureCode_InvalidStructTypeSize</p>
<p>4 - FailureCode_InvalidPowerCapabilities</p>
<p>5 - FailureCode_InvalidWakeReason</p>
<p>6 - FailureCode_DisarmNotInProgress</p>
<p>7 - FailureCode_WdfObjectCreateFailed</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>


## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bugcheck and can be helpful in determining the root cause.

Parameter 1 describes the type of violation. Look at the call stack to determine the misbehaving driver.

 ## See also

[Introduction to the Mobile Broadband (MBB) WDF class extension (MBBCx)](../netcx/mobile-broadband-mbb-wdf-class-extension-mbbcx.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
