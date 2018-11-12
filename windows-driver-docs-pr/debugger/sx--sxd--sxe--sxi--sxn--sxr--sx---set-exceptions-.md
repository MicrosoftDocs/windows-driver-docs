---
title: sx, sxd, sxe, sxi, sxn, sxr, sx- (Set Exceptions)
description: The sx* commands control the action that the debugger takes when an exception occurs in the application that is being debugged, or when certain events occur.
ms.assetid: fdb5059f-e7d9-4e14-aa3d-030e72c30732
keywords: ["sx, sxd, sxe, sxi, sxn, sxr, sx- (Set Exceptions) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- sx, sxd, sxe, sxi, sxn, sxr, sx- (Set Exceptions)
api_type:
- NA
ms.localizationpriority: medium
---

# sx, sxd, sxe, sxi, sxn, sxr, sx- (Set Exceptions)


The **sx***\** commands control the action that the debugger takes when an exception occurs in the application that is being debugged, or when certain events occur.

```dbgcmd
sx 

sx{e|d|i|n} [-c "Cmd1"] [-c2 "Cmd2"] [-h] {Exception|Event|*} 

sx- [-c "Cmd1"] [-c2 "Cmd2"] {Exception|Event|*} 

sxr
```

## <span id="ddk_cmd_set_exceptions_dbg"></span><span id="DDK_CMD_SET_EXCEPTIONS_DBG"></span>Parameters


<span id="-c__Cmd1_"></span><span id="-c__cmd1_"></span><span id="-C__CMD1_"></span>**-c "**<em>Cmd1</em>**"**  
Specifies a command that is executed if the exception or event occurs. This command is executed when the first chance to handle this exception occurs, regardless of whether this exception breaks into the debugger. You must enclose the *Cmd1* string in quotation marks. This string can include multiple commands, separated by semicolons. The space between the -c and the quoted command string is optional.

<span id="-c2_Cmd2_"></span><span id="-c2_cmd2_"></span><span id="-C2_CMD2_"></span>**-c2"**<em>Cmd2</em>**"**  
Specifies a command that is executed if the exception or event occurs and is not handled on the first chance. This command is executed when the second chance to handle this exception occurs, regardless of whether this exception breaks into the debugger. You must enclose the *Cmd2* string in quotation marks. This string can include multiple commands, separated by semicolons. The space between the -c2 and the quoted command string is optional.

<span id="_______-h______"></span><span id="_______-H______"></span> **-h**   
Changes the specified event's handling status instead of its break status. If *Event* is **cc**, **hc**, **bpec**, or **ssec**, you do not have to use the **-h** option.

<span id="_______Exception______"></span><span id="_______exception______"></span><span id="_______EXCEPTION______"></span> *Exception*   
Specifies the exception number that the command acts on, in the current radix.

<span id="_______Event______"></span><span id="_______event______"></span><span id="_______EVENT______"></span> *Event*   
Specifies the event that the command acts on. These events are identified by short abbreviations. For a list of the events, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

<span id="______________"></span> **\\***   
Affects all exceptions that are not otherwise explicitly named for **sx**. For a list of explicitly named exceptions, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

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

For more information about break status and handling status, descriptions of all event codes, a list of the default status for all events, and other methods of controlling this status, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

Remarks
-------

The **sx** command displays the list of exceptions for the current process and the list of all nonexception events and displays the default behavior of the debugger for each exception and event.

The **sxe**, **sxd**, **sxn**, and **sxi** commands control the debugger settings for each exception and event.

The **sxr** command resets all of the exception and event filter states to the default settings. Commands are cleared, break and continue options are reset to their default settings, and so on.

The **sx-** command does not change the handling status or the break status of the specified exception or event. This command can be used if you wish to change the first-chance command or second-chance command associated with a specific event, but do not wish to change anything else.

If you include the **-h** option (or if the **cc**, **hc**, **bpec**, or **ssec** events are specified), the **sxe**, **sxd**, **sxn**, and **sxi** commands control the [handling status](https://msdn.microsoft.com/library/windows/hardware/ff541490#handling-status) of the exception or event. In all other cases, these commands control the [break status](https://msdn.microsoft.com/library/windows/hardware/ff541490#break-status) of the exception or event.

When you are setting the break status, these commands have the following effects.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Status name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>sxe</strong></p></td>
<td align="left"><p><strong>Break</strong></p>
<p><strong>(Enabled)</strong></p></td>
<td align="left"><p>When this exception occurs, the target immediately breaks into the debugger before any other error handlers are activated. This kind of handling is called <em>first chance</em> handling.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>sxd</strong></p></td>
<td align="left"><p><strong>Second chance break</strong></p>
<p><strong>(Disabled)</strong></p></td>
<td align="left"><p>The debugger does not break for a first-chance exception of this type (although a message is displayed). If other error handlers do not address this exception, execution stops and the target breaks into the debugger. This kind of handling is called <em>second chance</em> handling.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>sxn</strong></p></td>
<td align="left"><p><strong>Output</strong></p>
<p><strong>(Notify)</strong></p></td>
<td align="left"><p>When this exception occurs, the target application does not break into the debugger at all. However, a message is displayed that notifies the user of this exception.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>sxi</strong></p></td>
<td align="left"><p><strong>Ignore</strong></p></td>
<td align="left"><p>When this exception occurs, the target application does not break into the debugger at all, and no message is displayed.</p></td>
</tr>
</tbody>
</table>

 

When you are setting the handling status, these commands have the following effects:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Status name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>sxe</strong></p></td>
<td align="left"><p><strong>Handled</strong></p></td>
<td align="left"><p>The event is considered handled when execution resumes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>sxd,sxn,sxi</strong></p></td>
<td align="left"><p><strong>Not Handled</strong></p></td>
<td align="left"><p>The event is considered not handled when execution resumes.</p></td>
</tr>
</tbody>
</table>

 

You can use the **-h** option together with exceptions, not events. Using this option with **ch**, **bpe**, or **sse** sets the handling status for **hc**, **bpec**, or **ssec**, respectively. If you use the -h option with any other event, it has no effect.

Using the **-c** or **-c2** options with **hc**, **bpec**, or **ssec** associates the specified commands with **ch**, **bpe**, or **sse**, respectively.

In the following example, the **sxe** command is used to set the break status of access violation events to break on the first chance, and to set the first-chance command that will be executed at that point to **r eax**. Then the **sx-** command is used to alter the first-chance command to **r ebx**, without changing the handling status. Finally, a portion of the **sx** output is shown, indicating the current settings for access violation events:

```dbgcmd
0:000> sxe -c "r eax" av 

0:000> sx- -c "r ebx" av 

0:000> sx 
 av - Access violation - break - not handled
       Command: "r ebx"
  . . .  
```

 

 





