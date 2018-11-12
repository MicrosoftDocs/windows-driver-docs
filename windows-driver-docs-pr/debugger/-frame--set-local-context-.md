---
title: .frame (Set Local Context)
description: The .frame command specifies which local context (scope) is used to interpret local variables or displays the current local context.
ms.assetid: eb843712-204f-4bbd-b711-a10756c9279a
keywords: ["Set Local Context (.frame) command", "memory, Set Local Context (.frame) command", "context, Set Local Context (.frame) command", ".frame (Set Local Context) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .frame (Set Local Context)
api_type:
- NA
ms.localizationpriority: medium
---

# .frame (Set Local Context)


The **.frame** command specifies which local context (scope) is used to interpret local variables or displays the current local context.

```dbgcmd
.frame [/c] [/r] [FrameNumber] 
.frame [/c] [/r] = BasePtr [FrameIncrement] 
.frame [/c] [/r] = BasePtr StackPtr InstructionPtr 
```

## <span id="ddk_meta_set_local_context_dbg"></span><span id="DDK_META_SET_LOCAL_CONTEXT_DBG"></span>Parameters


<span id="________c______"></span><span id="________C______"></span> **/c**   
Sets the specified frame as the current local override context. This action allows a user to access the nonvolatile registers for any function in the call stack.

<span id="________r______"></span><span id="________R______"></span> **/r**   
Displays registers and other information about the specified local context.

<span id="_______FrameNumber______"></span><span id="_______framenumber______"></span><span id="_______FRAMENUMBER______"></span> *FrameNumber*   
Specifies the number of the frame whose local context you want. If this parameter is zero, the command specifies the current frame. If you omit this parameter, this command displays the current local context.

<span id="_______BasePtr______"></span><span id="_______baseptr______"></span><span id="_______BASEPTR______"></span> *BasePtr*   
Specifies the base pointer for the stack trace that is used to determine the frame, if you add an equal sign (=) after the command name (**.frame**). On an x86-based processor, you add another argument after *BasePtr* (which is interpreted as *FrameIncrement*) or two more arguments after *BasePtr* (which are interpreted as *InstructionPtr* and *StackPtr*).

<span id="_______FrameIncrement______"></span><span id="_______frameincrement______"></span><span id="_______FRAMEINCREMENT______"></span> *FrameIncrement*   
(x86-based processor only)

Specifies an additional quantity of frames past the base pointer. For example, if the base pointer 0x0012FF00 is the address of frame 3, the command **.frame 12ff00** is equivalent to **.frame 3**, and **.frame 12ff00 2** is equivalent to **.frame 5**.

<span id="_______StackPtr______"></span><span id="_______stackptr______"></span><span id="_______STACKPTR______"></span> *StackPtr*   
(x86-based processor only) Specifies the stack pointer for the stack trace that is used to determine the frame. If you omit *StackPtr* and *InstructionPtr*, the debugger uses the stack pointer that the **esp** register specifies and the instruction pointer that the **eip** register specifies.

<span id="_______InstructionPtr______"></span><span id="_______instructionptr______"></span><span id="_______INSTRUCTIONPTR______"></span> *InstructionPtr*   
(x86-based processor only) Specifies the instruction pointer for the stack trace that is used to determine the frame. If you omit *StackPtr* and *InstructionPtr*, the debugger uses the stack pointer that the **esp** register specifies and the instruction pointer that the **eip** register specifies.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the local context and other context settings, see [Changing Contexts](changing-contexts.md). For more information about how to display local variables and other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

When an application is running, the meaning of local variables depends on the location of the program counter, because the scope of such variables extends only to the function that they are defined in. If you do not use the **.frame** command, the debugger uses the scope of the current function (the current frame on the stack) as the [local context](changing-contexts.md#local-context).

To change the local context, use the **.frame** command and specify the frame number that you want.

The *frame number* is the position of the stack frame within the stack trace. You can view this stack trace with the [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command or the [Calls window](calls-window.md). The first line (the current frame) is frame number 0. The subsequent lines represent frame numbers 1, 2, 3, and so on.

If you use the **n** parameter with the [**k**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command, the **k** command displays frame numbers together with the stack trace. These frame numbers are always displayed in hexadecimal form. On the other hand, the **.frame** command interprets its argument in the default radix, unless you override this setting with a prefix such as 0x. To change the default radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command.

You can set the local context to a different stack frame to enable you to view new local variable information. However, the actual variables that are available depend on the code that is being executed.

The local context is reset to the scope of the program counter if any application execution occurs. The local context is reset to the top stack frame if the register context is changed.

 

 





