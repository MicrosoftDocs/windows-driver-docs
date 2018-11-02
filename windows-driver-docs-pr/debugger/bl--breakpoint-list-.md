---
title: bl (Breakpoint List)
description: The bl command lists information about existing breakpoints.
ms.assetid: 3e7c31d4-5c76-4609-91be-c6b0fc1cb292
keywords: ["bl (Breakpoint List) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bl (Breakpoint List)
api_type:
- NA
ms.localizationpriority: medium
---

# bl (Breakpoint List)


The **bl** command lists information about existing breakpoints.

```dbgcmd
bl [/L] [Breakpoints]
```

## <span id="ddk_cmd_breakpoint_list_dbg"></span><span id="DDK_CMD_BREAKPOINT_LIST_DBG"></span>Parameters


<span id="________L______"></span><span id="________l______"></span> **/L**   
Forces **bl** to always display breakpoint addresses instead of showing source file and line numbers.

<span id="_______Breakpoints______"></span><span id="_______breakpoints______"></span><span id="_______BREAKPOINTS______"></span> *Breakpoints*   
Specifies the ID numbers of the breakpoints to list. If you omit *Breakpoints*, the debugger lists all breakpoints. You can specify any number of breakpoints. You must separate multiple IDs by spaces or commas. You can specify a range of breakpoint IDs by using a hyphen (-). You can use an asterisk (**\\***) to indicate all breakpoints. If you want to use a [numeric expression](numerical-expression-syntax.md) for an ID, enclose it in brackets (*<em>\[\]</em><em>). If you want to use a [string with wildcard characters](string-wildcard-syntax.md) to match a breakpoint's symbolic name, enclose it in quotation marks ( **" "</em>* ).

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
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about and examples of how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, and how to set breakpoints in user space from a kernel debugger, see [Using Breakpoints](using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

Remarks
-------

For each breakpoint, the command displays the following information:

- The breakpoint ID. This ID is a decimal number that you can use to refer to the breakpoint in later commands.

- The breakpoint status. The status can be **e** (enabled) or **d** (disabled).

- (Unresolved breakpoints only) The letter "u" appears if the breakpoint is unresolved. That is, the breakpoint does not match a symbolic reference in any currently loaded module. For information about these breakpoints, see [Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md).

- The virtual address or symbolic expression that makes up the breakpoint location. If you enabled source line number loading, the **bl** command displays file and line number information instead of address offsets. If the breakpoint is unresolved, the address is omitted here and appears at the end of the listing instead.

- (Data breakpoints only) Type and size information are displayed for data breakpoints. The types can be **e** (execute), **r** (read/write), **w** (write), or **i** (input/output). These types are followed with the size of the block, in bytes. For information about these breakpoints, see [Processor Breakpoints (ba Breakpoints)](processor-breakpoints---ba-breakpoints-.md).

- The number of passes that remain until the breakpoint is activated, followed by the initial number of passes in parentheses. For more information about this kind of breakpoint, see the description of the *Passes* parameter in [**bp, bu, bm (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md).

- The associated process and thread. If thread is given as three asterisks ("**\*\*\\***"), this breakpoint is not a thread-specific breakpoint.

- The module and function, with offset, that correspond to the breakpoint address. If the breakpoint is unresolved, the breakpoint address appears here instead, in parentheses. If the breakpoint is set on a valid address but symbol information is missing, this field is blank.

- The command that is automatically executed when this breakpoint is hit. This command is displayed in quotation marks.

If you are not sure what command was used to set an existing breakpoint, use [**.bpcmds (Display Breakpoint Commands)**](-bpcmds--display-breakpoint-commands-.md) to list all breakpoints along with the commands that were used to create them.

The following example shows the output of a **bl** command.

Example

```dbgcmd
0:000> bl
 0 e 010049e0     0001 (0001)  0:**** stst!main
```

This output contains the following information:

- The breakpoint ID is **0**.

- The breakpoint status is **e** (enabled).

- The breakpoint is not unresolved (there is no **u** in the output).

- The virtual address of the breakpoint is **010049e0**.

- The breakpoint is active on the first pass through the code and the code has not yet been executed under the debugger. This information is indicated by a value of 1 (**0001**) in the "passes remaining" counter and a value of 1 (**(0001)**) in the initial passes counter.

- This breakpoint is not a thread-specific breakpoint (**\*\*\*\\***).

- The breakpoint is set on **main** in the **stst** module.

 

 





