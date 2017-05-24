---
title: .expr (Choose Expression Evaluator)
description: The .expr command specifies the default expression evaluator.
ms.assetid: 96d246c2-10fe-4688-a04f-1325ac51e4b3
keywords: [".expr (Choose Expression Evaluator) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .expr (Choose Expression Evaluator)
api_type:
- NA
---

# .expr (Choose Expression Evaluator)


The **.expr** command specifies the default expression evaluator.

``` syntax
    .expr /s masm 
.expr /s c++ 
.expr /q 
.expr 
```

## <span id="ddk_meta_choose_expression_evaluator_dbg"></span><span id="DDK_META_CHOOSE_EXPRESSION_EVALUATOR_DBG"></span>Parameters


<span id="________s_masm______"></span><span id="________S_MASM______"></span> **/s masm**   
Changes the default expression type to Microsoft Assembler expression evaluator (MASM). This type is the default value when you start the debugger.

<span id="________s_c________"></span><span id="________S_C________"></span> **/s c++**   
Changes the default expression type to the C++ expression evaluator.

<span id="________q______"></span><span id="________Q______"></span> **/q**   
Displays the list of possible expression types.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When you use the **.expr** command without an argument, the debugger displays the current default expression type.

The [**?? (Evaluate C++ Expression)**](----evaluate-c---expression-.md) command, the

Watch window, and the [Locals window](locals-window.md) always use C++ expression syntax. All other commands and debugging information windows use the default expression evaluator.

For more information about how to control which syntax is used, see [Evaluating Expressions](evaluating-expressions.md). For more information about the syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.expr%20%28Choose%20Expression%20Evaluator%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




