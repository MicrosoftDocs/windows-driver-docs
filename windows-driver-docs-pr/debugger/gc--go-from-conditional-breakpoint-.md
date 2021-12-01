---
title: gc (Go from Conditional Breakpoint)
description: The gc command resumes execution from a conditional breakpoint in the same fashion that was used to hit the breakpoint (stepping, tracing, or freely executing).
keywords: ["gc (Go from Conditional Breakpoint) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gc (Go from Conditional Breakpoint)
api_type:
- NA
ms.localizationpriority: medium
---

# gc (Go from Conditional Breakpoint)


The **gc** command resumes execution from a conditional breakpoint in the same fashion that was used to hit the breakpoint (stepping, tracing, or freely executing). This only applies to the older style of conditional breakpoints using a "j (Condition) ..." style expression, rather than the simpler "/w" style conditional breakpoint. For more information, see [setting a conditional breakpoint](setting-a-conditional-breakpoint.md).

```dbgcmd
gc
```

While this command is no longer as useful for conditional breakpoints, it can still be used for breakpoints that do logging or some other activity without breaking into the debugger. For instance, a breakpoint could be written that looks like this:

```dbgcmd
bp module!myFunction ".echo myFunction executed; gc"
```

If a normal "g" command were used instead, the program would continue execution when stepping over "myFunction", instead of simply printing the message and continuing the step operation.


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
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of related commands, see [Controlling the Target](controlling-the-target.md).

## Remarks

When a [conditional breakpoint](setting-a-conditional-breakpoint.md) using a "j (Condition) ..." expression includes an execution command at the end, this should be the **gc** command.

For example, the following is an example conditional breakpoint:

```dbgcmd
0:000> bp Address "j (Condition) 'OptionalCommands'; 'gc' " 
```

When this breakpoint is encountered and the expression is false, execution will resume using the same execution type that was previously used. For example, if you used a **g (Go)** command to reach this breakpoint, execution would resume freely. But if you reached this breakpoint while stepping or tracing, execution would resume with a step or a trace.

On the other hand, the following is an improper breakpoint formulation, since execution will always resume freely even if you had been stepping before reaching the breakpoint:

```dbgcmd
0:000> bp Address "j (Condition) 'OptionalCommands'; 'g' " 
```

 

 





