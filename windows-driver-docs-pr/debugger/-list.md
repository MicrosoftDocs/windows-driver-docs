---
title: list
description: The list extension executes the specified debugger commands repeatedly, once for every element in a linked list.
ms.assetid: 763742f3-1cb8-4263-861b-b9d01483245e
keywords: ["list Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- list
api_type:
- NA
ms.localizationpriority: medium
---

# !list


The **!list** extension executes the specified debugger commands repeatedly, once for every element in a linked list.

```dbgcmd
!list -t [Module!]Type.Field -x "Commands" [-a "Arguments"] [Options] StartAddress 
!list " -t [Module!]Type.Field -x \"Commands\" [-a \"Arguments\"] [Options] StartAddress " 
!list -h 
```

## <span id="ddk__list_dbg"></span><span id="DDK__LIST_DBG"></span>Parameters


<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
An optional parameter specifying the module that defines this structure. If there is a chance that *Type* may match a valid symbol in a different module, you should include *Module* to eliminate the ambiguity.

<span id="_______Type______"></span><span id="_______type______"></span><span id="_______TYPE______"></span> *Type*   
Specifies the name of a data structure.

<span id="_______Field______"></span><span id="_______field______"></span><span id="_______FIELD______"></span> *Field*   
Specifies the field containing the list link. This can actually be a sequence of fields separated by periods (in other words, **Type.Field.Subfield.Subsubfield**, and so on).

<span id="_______-x__Commands_"></span><span id="_______-x__commands_"></span><span id="_______-X__COMMANDS_"></span> **-x "**<em>Commands</em>**"**  
Specifies the commands to execute. This can be any combination of debugger commands. It must be enclosed in quotation marks. If multiple commands are specified, separate them with semicolons, enclose the entire collection of **!list** arguments in quotation marks, and use an escape character ( \\ ) before each quotation mark inside these outer quotation marks. If *Commands* is omitted, the default is [**dp (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md).

<span id="_______-a__Arguments_"></span><span id="_______-a__arguments_"></span><span id="_______-A__ARGUMENTS_"></span> **-a "**<em>Arguments</em>**"**  
Specifies the arguments to pass to the *Commands* parameter. This must be enclosed in quotation marks. *Arguments* can be any valid argument string that would normally be allowed to follow this command, except that *Arguments* cannot contain quotation marks. If the pseudo-register **$extret** is included in *Commands*, the **-a "**<em>Arguments</em>**"** parameter can be omitted.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Can be any number of the following options:

<span id="-e"></span><span id="-E"></span>**-e**  
Echoes the command being executed for each element.

<span id="-m_Max"></span><span id="-m_max"></span><span id="-M_MAX"></span>**-m** *Max*  
Specifies the maximum number of elements to execute the command for.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address of the first data structure. This is the address at the top of the structure, not necessarily the address of the link field.

<span id="_______-h______"></span><span id="_______-H______"></span> **-h**   
Displays some brief Help text for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **!list** extension will go through the linked list and issue the specified command once for each list element.

The pseudo-register **$extret** is set to the value of the list-entry address for each list element. For each element, the command string *Commands* is executed. This command string can reference this pseudo-register using the **$extret** syntax. If this does not appear in the command string, the value of the list-entry address is appended to the end of the command string before execution. If you need to specify where this value should appear in your command, you must specify this pseudo-register explicitly.

This command sequence will run until the list terminates in a null pointer, or terminates by looping back onto the first element. If the list loops back onto a later element, this command will not stop. However, you can stop this command at any time by using [**CTRL+C**](ctrl-c--break-.md) in KD and CDB, or [Debug | Break](debug---break.md) or CTRL+BREAK in WinDbg.

Each time a command is executed, the address of the current structure will be used as the *default address* if the command being used has optional address parameters.

Following are two examples of how to use this command in user mode. Note that kernel mode usage is also possible but follows a different syntax.

As a simple example, assume that you have a structure whose type name is **MYTYPE**, and which has links within its **.links.Flink** and **.links.Blink** fields. You have a linked list that begins with the structure at 0x6BC000. The following extension command will go through the list and for each element will execute a [**dd**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) L2 command. Because no address is being specified to the **dd** command, it will take the address of the list head as the desired address. This causes the first two DWORDs in each structure to be displayed.

```dbgcmd
0:000> !list -t MYTYPE.links.Flink -x "dd" -a "L2" 0x6bc00 
```

As a more complex example, consider the case of using **$extret**. It follows the list of type \_LIST\_ENTRY at **RtlCriticalSectionList**. For each element, it displays the first four DWORDS, and then displays the \_RTL\_CRITICAL\_SECTION\_DEBUG structure located at an offset of eight bytes prior to the **Flink** element of the list entry.

```dbgcmd
0:000> !list "-t ntdll!_LIST_ENTRY.Flink -e -x \"dd @$extret l4; dt ntdll!_RTL_CRITICAL_SECTION_DEBUG @$extret-0x8\" ntdll!RtlCriticalSectionList"
dd @$extret l4; dt ntdll!_RTL_CRITICAL_SECTION_DEBUG @$extret-0x8
7c97c0c8  7c97c428 7c97c868 01010000 00000080
   +0x000 Type             : 1
   +0x002 CreatorBackTraceIndex : 0
   +0x004 CriticalSection  : (null)
   +0x008 ProcessLocksList : _LIST_ENTRY [ 0x7c97c428 - 0x7c97c868 ]
   +0x010 EntryCount       : 0x1010000
   +0x014 ContentionCount  : 0x80
   +0x018 Spare            : [2] 0x7c97c100

dd @$extret l4; dt ntdll!_RTL_CRITICAL_SECTION_DEBUG @$extret-0x8
7c97c428  7c97c448 7c97c0c8 00000000 00000000
   +0x000 Type             : 0
   +0x002 CreatorBackTraceIndex : 0
   +0x004 CriticalSection  : 0x7c97c0a0
   +0x008 ProcessLocksList : _LIST_ENTRY [ 0x7c97c448 - 0x7c97c0c8 ]
   +0x010 EntryCount       : 0
   +0x014 ContentionCount  : 0
   +0x018 Spare            : [2] 0
```

 

 





