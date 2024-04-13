---
title: "n (Set Number Base)"
description: "The n command sets the default number base (radix) to the specified value or displays the current number base.Do not confuse this command with the ~n (Suspend Thread) command."
keywords: ["n (Set Number Base) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- n (Set Number Base)
api_type:
- NA
---

# n (Set Number Base)


The **n** command sets the default number base (radix) to the specified value or displays the current number base.

Do not confuse this command with the [**~n (Suspend Thread)**](-n--suspend-thread-.md) command.

```dbgcmd
n [Radix]
```

## <span id="ddk_cmd_set_number_base_dbg"></span><span id="DDK_CMD_SET_NUMBER_BASE_DBG"></span>Parameters


<span id="_______Radix______"></span><span id="_______radix______"></span><span id="_______RADIX______"></span> *Radix*   
Specifies the default number base that is used for numeric display and entry. You can use one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>8</p></td>
<td align="left"><p>Octal</p></td>
</tr>
<tr class="even">
<td align="left"><p>10</p></td>
<td align="left"><p>Decimal</p></td>
</tr>
<tr class="odd">
<td align="left"><p>16</p></td>
<td align="left"><p>Hexadecimal</p></td>
</tr>
</tbody>
</table>

 

If you omit *Radix*, the current default number base is displayed.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The current radix affects the input and output of MASM expressions. It does not affect the input or output of C++ expressions. For more information about these expressions, see [Evaluating Expressions](evaluating-expressions.md).

The default radix is set to 16 when the debugger is started.

In all MASM expressions, numeric values are interpreted as numbers in the current radix (16, 10, or 8). You can override the default radix by specifying the **0x** prefix (hexadecimal), the **0n** prefix (decimal), the **0t** prefix (octal), or the **0y** prefix (binary).

