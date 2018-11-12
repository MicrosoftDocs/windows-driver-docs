---
title: j (Execute If - Else)
description: The j command conditionally executes one of the specified commands, depending on the evaluation of a given expression.
ms.assetid: c6bb2415-e888-458b-8fb9-9d50b90cc531
keywords: ["j (Execute If - Else) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- j (Execute If - Else)
api_type:
- NA
ms.localizationpriority: medium
---

# j (Execute If - Else)


The **j** command conditionally executes one of the specified commands, depending on the evaluation of a given expression.

```dbgcmd
j Expression Command1 ; Command2 
j Expression 'Command1' ; 'Command2' 
```

## <span id="ddk_cmd_execute_if_else_dbg"></span><span id="DDK_CMD_EXECUTE_IF_ELSE_DBG"></span>Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
The expression to evaluate. If this expression evaluates to a nonzero value, *Command1* is executed. If this expression evaluates to zero, *Command2* is executed. For more information about the syntax of this expression, see [Numerical Expression Syntax](numerical-expression-syntax.md).

<span id="_______Command1______"></span><span id="_______command1______"></span><span id="_______COMMAND1______"></span> *Command1*   
The command string to be executed if the expression in *Expression* evaluates to a nonzero value (TRUE). You can combine multiple commands by surrounding the command string with single straight quotation marks ( **'** ) and separating commands by using semicolons. If the command string is a single command, the single quotation marks are optional.

<span id="_______Command2______"></span><span id="_______command2______"></span><span id="_______COMMAND2______"></span> *Command2*   
The command string to be executed if the expression in *Expression* evaluates to zero (FALSE). You can combine multiple commands by surrounding the command string with single straight quotation marks ( **'** ) and separating commands by using semicolons. If the command string is a single command, the single quotation marks are optional.

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

You cannot add a semicolon or additional commands after the **j** command. If a semicolon appears after *Command2*, everything after the semicolon is ignored.

The following command displays the value of **eax** if **MySymbol** is equal to zero and displays the values of **ebx** and **ecx** otherwise.

```dbgcmd
0:000> j (MySymbol=0) 'r eax'; 'r ebx; r ecx' 
```

You could omit the single quotation marks around **r eax**, but they make the command easier to read. If you want to omit one of the commands, you can include empty quotation marks or omit the parameter for that command, as in the following commands.

```dbgcmd
0:000> j (MySymbol=0) ''; 'r ebx; r ecx' 
0:000> j (MySymbol=0)  ; 'r ebx; r ecx' 
```

You can also use the **j** command inside other commands. For example, you can use a **j** command to create conditional breakpoints.

```dbgcmd
0:000> bp `mysource.cpp:143` "j (poi(MyVar)>0n20) ''; 'gc' "
```

For more information about the syntax for conditional breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

## <span id="see_also"></span>See also


[**z (Execute While)**](z--execute-while-.md)

 

 






