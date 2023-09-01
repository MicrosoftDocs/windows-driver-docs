---
title: bs (Update Breakpoint Command)
description: The bs command changes the command executed when the specified breakpoint is encountered.
keywords: ["bs (Update Breakpoint Command) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- bs (Update Breakpoint Command)
api_type:
- NA
---

# bs (Update Breakpoint Command)


The **bs** command changes the command executed when the specified breakpoint is encountered.

```dbgcmd
bs ID ["CommandString"] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______ID______"></span><span id="_______id______"></span> *ID*   
Specifies the ID number of the breakpoint.

<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the new list of commands to be executed every time that the breakpoint is encountered. You must enclose the *CommandString* parameter in quotation marks. Use semicolons to separate multiple commands.

Debugger commands in *CommandString* can include parameters. You can use standard C-control characters (such as **\\n** and **\\"**). Semicolons that are contained in second-level quotation marks (**\\"**) are interpreted as part of the embedded quoted string.

The *CommandString* commands are executed only if the breakpoint is reached while the application is executing in response to a **g (Go)** command. The commands are not executed if you are stepping through the code or tracing past this point.

Any command that resumes program execution after a breakpoint (such as **g** or **t**) ends the execution of the command list.

### Environment

|  Item       | Description               |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

 

### Additional Information

For more information about and examples of how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, and how to set breakpoints in user space from a kernel debugger, see [Using Breakpoints](using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

## Remarks

If the *CommandString* is not specified, any commands already set on the breakpoint are removed.

 

 





