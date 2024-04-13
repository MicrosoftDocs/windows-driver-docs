---
title: "!ks.eval (WinDbg)"
description: "The !ks.eval extension evaluates an expression using an extension-specific expression evaluator."
keywords: ["!ks.eval Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ks.eval
api_type:
- NA
---

# !ks.eval


The **!ks.eval** extension evaluates an expression using an extension-specific expression evaluator.

```dbgcmd
!ks.eval Expression 
```

## Parameters

*Expression*   
Specifies the expression to evaluate. *Expression* can include any MASM operators, symbols, or numerical syntax, as well as the extension-specific operators described below. For more information about MASM expressions, see [MASM Numbers and Operators](masm-numbers-and-operators.md).

### DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For more information, see [Kernel Streaming Debugging](../debugger/kernel-streaming-debugging.md).

## Remarks

The extension module includes two extension-specific operators which can be used in address parameters to extension commands:

<span id="________fdo_________x_________"></span><span id="________FDO_________X_________"></span> **fdo(** *x* **)**  
Returns the functional device object associated with the object at address **x**.

<span id="________driver_________x_________"></span><span id="________DRIVER_________X_________"></span> **driver(** *x* **)**  
Returns the driver object associated with **fdo(**<em>x</em>**)**.

You can use the **!ks.eval** command to parse expressions that contain these extension-specific operators as well as [MASM Numbers and Operators](masm-numbers-and-operators.md).

Note that all operators supported by **!ks.eval** are also supported by all other extension commands in the Ks.dll extension module.

Here is an example of the **!ks.eval** extension being used with the address of a filter. Note the presence of the 0x8241C020 address in the [**!ks.allstreams**](-ks-allstreams.md) output:

```dbgcmd
kd> !eval fdo(829493c4)
Resulting Evaluation: 8241c020

kd> !allstreams
6 Kernel Streaming FDOs found:
    Functional Device 82a17690 [\Driver\smwdm]
    Functional Device 8296eb08 [\Driver\wdmaud]
    Functional Device 82490388 [\Driver\sysaudio]
    Functional Device 82970cb8 [\Driver\MSPQM]
    Functional Device 824661b8 [\Driver\MSPCLOCK]
    Functional Device 8241c020 [\Driver\avssamp]
```

