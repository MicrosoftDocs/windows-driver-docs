---
title: dv (Display Local Variables)
description: The dv command displays the names and values of all local variables in the current scope.
ms.assetid: 1b5260f7-f47c-481a-b93f-015ab9fa4b58
keywords: ["dv (Display Local Variables) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dv (Display Local Variables)
api_type:
- NA
ms.localizationpriority: medium
---

# dv (Display Local Variables)


The **dv** command displays the names and values of all local variables in the current scope.

```dbgcmd
dv [Flags] [Pattern] 
```

## <span id="ddk_cmd_display_local_variables_dbg"></span><span id="DDK_CMD_DISPLAY_LOCAL_VARIABLES_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Causes additional information to be displayed. Any of the following case-sensitive *Flags* can be included:

<span id="_f__addr_"></span><span id="_F__ADDR_"></span>**/f** &lt;addr&gt;  
Lets you specify an arbitrary function address so that you can see what parameters and locals exist for any code anywhere. It turns off the value display and implies **/V**. The **/f** flag must be the last flag. A parameter filter pattern can still be specified after it if the string is quoted.

<span id="_i"></span><span id="_I"></span>**/i**  
Causes the display to specify the kind of variable: local, global, parameter, function, or unknown.

<span id="_t"></span><span id="_T"></span>**/t**  
Causes the display to include the data type for each local variable.

<span id="_v"></span><span id="_V"></span>**/v**  
Causes the display to include the virtual memory address or register location of each local variable.

<span id="_V"></span><span id="_v"></span>**/V**  
Same as **/v**, and also includes the address of the local variable relative to the relevant register.

<span id="_a"></span><span id="_A"></span>**/a**  
Sorts the output by address, in ascending order.

<span id="_A"></span><span id="_a"></span>**/A**  
Sorts the output by address, in descending order.

<span id="_n"></span><span id="_N"></span>**/n**  
Sorts the output by name, in ascending order.

<span id="_N"></span><span id="_n"></span>**/N**  
Sorts the output by name, in descending order.

<span id="_z"></span><span id="_Z"></span>**/z**  
Sorts the output by size, in ascending order.

<span id="_Z"></span><span id="_z"></span>**/Z**  
Sorts the output by size, in descending order.

<span id="_______Pattern______"></span><span id="_______pattern______"></span><span id="_______PATTERN______"></span> *Pattern*   
Causes the command to only display local variables that match the specified *Pattern*. The pattern may contain a variety of wildcards and specifiers; see [String Wildcard Syntax](string-wildcard-syntax.md) for details. If *Pattern* contains spaces, it must be enclosed in quotation marks. If *Pattern* is omitted, all local variables will be displayed.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details on displaying and changing local variables and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

In verbose mode, the addresses of the variables are displayed as well. (This can also be done with the [**x (Examine Symbols)**](x--examine-symbols-.md) command.)

Data structures and unfamiliar data types are not displayed in full; rather, their type name is displayed. To display the entire structure, or display a particular member of the structure, use the [**dt (Display Type)**](dt--display-type-.md) command.

The *local context* determines which set of local variables will be displayed. By default, this context matches the current position of the program counter. For information about how this can be changed, see [Local Context](changing-contexts.md#local-context).

 

 





