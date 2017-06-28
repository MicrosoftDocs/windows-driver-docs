---
title: ks.eval
description: The ks.eval extension evaluates an expression using an extension-specific expression evaluator.
ms.assetid: 68c9cfb0-ff87-47ea-bd0d-5f45c1de0639
keywords: ["ks.eval Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ks.eval
api_type:
- NA
---

# !ks.eval


The **!ks.eval** extension evaluates an expression using an extension-specific expression evaluator.

```
!ks.eval Expression 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the expression to evaluate. *Expression* can include any MASM operators, symbols, or numerical syntax, as well as the extension-specific operators described below. For more information about MASM expressions, see [MASM Numbers and Operators](masm-numbers-and-operators.md).

### <span id="DLL"></span><span id="dll"></span>DLL

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

The extension module includes two extension-specific operators which can be used in address parameters to extension commands:

<span id="________fdo_________x_________"></span><span id="________FDO_________X_________"></span> **fdo(** *x* **)**  
Returns the functional device object associated with the object at address **x**.

<span id="________driver_________x_________"></span><span id="________DRIVER_________X_________"></span> **driver(** *x* **)**  
Returns the driver object associated with **fdo(***x***)**.

You can use the **!ks.eval** command to parse expressions that contain these extension-specific operators as well as [MASM Numbers and Operators](masm-numbers-and-operators.md).

Note that all operators supported by **!ks.eval** are also supported by all other extension commands in the Ks.dll extension module.

Here is an example of the **!ks.eval** extension being used with the address of a filter. Note the presence of the 0x8241C020 address in the [**!ks.allstreams**](-ks-allstreams.md) output:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ks.eval%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




