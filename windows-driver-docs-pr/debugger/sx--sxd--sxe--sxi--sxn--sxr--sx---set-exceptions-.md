---
title: sx, sxd, sxe, sxi, sxn, sxr, sx- (Set exceptions)
description: Learn about the sx* commands, which control the action that the debugger takes when an exception occurs in the application that is being debugged.
keywords: ["sx, sxd, sxe, sxi, sxn, sxr, sx- (Set Exceptions) Windows Debugging"]
ms.date: 12/13/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- sx, sxd, sxe, sxi, sxn, sxr, sx- (Set Exceptions)
api_type:
- NA
---

# sx, sxd, sxe, sxi, sxn, sxr, sx- (Set Exceptions)

The **sx** commands control the action that the debugger takes when an exception occurs in the application that is being debugged, or when certain events occur.

```dbgcmd
sx

sx{e|d|i|n} [-c "Cmd1"] [-c2 "Cmd2"] [-h] {Exception|Event|*}

sx- [-c "Cmd1"] [-c2 "Cmd2"] {Exception|Event|*}

sxr
```

## Parameters
  
**-c "**<em>Cmd1</em>**"**  
Specifies a command that's executed if the exception or event occurs. This command is executed when the first chance to handle this exception occurs, regardless of whether this exception breaks into the debugger. You must enclose the *Cmd1* string in quotation marks. This string can include multiple commands if you separate them with semicolons. The space between the -c and the quoted command string is optional.
  
**-c2"**<em>Cmd2</em>**"**  
Specifies a command that's executed if the exception or event occurs and isn't handled on the first chance. This command is executed when the second chance to handle this exception occurs, regardless of whether this exception breaks into the debugger. You must enclose the *Cmd2* string in quotation marks. This string can include multiple commands if you separate them with semicolons. The space between the -c2 and the quoted command string is optional.
 
**-h**  
Changes the specified event's handling status instead of its break status. If *Event* is **cc**, **hc**, **bpec**, or **ssec**, you don't have to use the **-h** option.
 
*Exception*  
Specifies the exception number that the command acts on in the current radix.
  
*Event*  
Specifies the event that the command acts on. These events are identified by short abbreviations. For a list of the events, see [Controlling exceptions and events](controlling-exceptions-and-events.md).
  
**\***  
Affects all exceptions that aren't otherwise explicitly named for **sx**. For a list of explicitly named exceptions, see [Controlling exceptions and events](controlling-exceptions-and-events.md).

### Environment

|&nbsp;         |&nbsp;                  |
|---------------|------------------------|
| **Modes**     | User mode, kernel mode |
| **Targets**   | Live debugging only    |
| **Platforms** | All                    |

### Additional Information

For more information about break status and handling status, descriptions of all event codes, a list of the default status for all events, and other methods of controlling this status, see [Controlling exceptions and events](controlling-exceptions-and-events.md).

## Remarks

The **sx** command displays the list of exceptions for the current process and the list of all non-exception events and displays the default behavior of the debugger for each exception and event.

The **sxe**, **sxd**, **sxn**, and **sxi** commands control the debugger settings for each exception and event.

The **sxr** command resets all of the exception and event filter states to the default settings. For example, commands are cleared and break, and continue options are reset to their default settings.

The **sx-** command doesn't change the handling status or the break status of the specified exception or event. This command can be used if you wish to change the first-chance command or second-chance command associated with a specific event, but don't wish to change anything else.

If you include the **-h** option (or if the **cc**, **hc**, **bpec**, or **ssec** events are specified), the **sxe**, **sxd**, **sxn**, and **sxi** commands control the [handling status](./debug-filter-xxx.md#handling-status) of the exception or event. In all other cases, these commands control the [break status](./debug-filter-xxx.md#break-status) of the exception or event.

When you're setting the break status, these commands have the following effects:

| Command | Status name | Description |
|---------|-------------|-------------|
| **sxe** | **Break <br> (Enabled)** | When this exception occurs, the target immediately breaks into the debugger before any other error handlers are activated. This kind of handling is called *first-chance* handling. |
| **sxd** | **Second chance break <br> (Disabled)** | The debugger doesn't break for a first-chance exception of this type (although a message is displayed). If other error handlers don't address this exception, the execution stops and the target breaks into the debugger. This kind of handling is called *second-chance* handling. |
| **sxn** | **Output <br> (Notify)** | When this exception occurs, the target application doesn't break into the debugger at all. However, a message is displayed that notifies the user of this exception. |
| **sxi** | **Ignore** | When this exception occurs, the target application doesn't break into the debugger at all, and no message is displayed. |

When you're setting the handling status, these commands have the following effects:

| Command | Status name | Description |
|---|---|---|
| **sxe** | **Handled** | The event is considered handled when execution resumes. |
| **sxd,sxn,sxi** | **Not Handled** | The event is considered not handled when execution resumes. |

You can use the **-h** option together with exceptions, not events. Use this option with **ch**, **bpe**, or **sse** to set the handling status for **hc**, **bpec**, or **ssec**, respectively. If you use the **-h** option with any other event, it has no effect.

Use the **-c** or **-c2** options with **hc**, **bpec**, or **ssec** to associate the specified commands with **ch**, **bpe**, or **sse**, respectively.

In the following example, the **sxe** command is used to set the break status of access violation events to break on the first chance, and to set the first-chance command that will be executed at that point to **r eax**. Then the **sx-** command is used to alter the first-chance command to **r ebx**, without changing the handling status. Finally, a portion of the **sx** output is shown, indicating the current settings for access violation events:

```dbgcmd
0:000> sxe -c "r eax" av

0:000> sx- -c "r ebx" av

0:000> sx
 av - Access violation - break - not handled
       Command: "r ebx"
  . . .  
```

## See also

- [Using breakpoints - debugging techniques](using-breakpoints.md)

- [Conditional breakpoints in WinDbg](setting-a-conditional-breakpoint.md)

- [Executing until a specified state is reached](executing-until-a-specified-state-is-reached.md)
