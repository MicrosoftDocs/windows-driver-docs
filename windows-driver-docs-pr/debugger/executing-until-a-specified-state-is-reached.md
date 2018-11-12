---
title: Executing Until a Specified State is Reached
description: Executing Until a Specified State is Reached
ms.assetid: 0657a7bf-4d72-4248-9e45-d79d51b91139
keywords: ["executing until a specified state is reached", "breakpoints, used to control execution", "breakpoints, and pseudo-registers", "script file, used to control execution"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Executing Until a Specified State is Reached


## <span id="ddk_determining_the_acl_of_an_object_dbg"></span><span id="DDK_DETERMINING_THE_ACL_OF_AN_OBJECT_DBG"></span>


There are several ways to cause the target to execute until a specified state is reached.

### <span id="using_a_breakpoint_to_control_execution"></span><span id="USING_A_BREAKPOINT_TO_CONTROL_EXECUTION"></span>Using a Breakpoint to Control Execution

One method is to use a breakpoint. The simplest breakpoint halts execution when the program counter reaches a specified address. A more complex breakpoint can:

-   be triggered only when this address is executed by a specific thread,

-   allow a specified number of passes through this address before being triggered,

-   automatically issue a specified command when it is triggered, or

-   watch a specified address in non-executable memory, being triggered when that memory is read or written to.

For details on how to set and control breakpoints, see [Using Breakpoints](using-breakpoints.md).

A more complicated way to execute until a specified state is reached is to use a *conditional breakpoint*. This kind of breakpoint is set at a certain address, but is only triggered if a specified condition holds. For details, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

### <span id="breakpoints_and_pseudo_registers"></span><span id="BREAKPOINTS_AND_PSEUDO_REGISTERS"></span>Breakpoints and Pseudo-Registers

In specifying the desired state, it is often helpful to use *automatic pseudo-registers*. These are variables controlled by the debugger which allow you to reference a variety of values related to the target state.

For example, the following breakpoint uses the **$thread** pseudo-register, which is always equal to the value of the current thread. It resolves to the value of the current thread when it is used in a command. By using **$thread** as the argument of the **/t** parameter of the [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command, you can create a breakpoint that will be triggered every time that **NtOpenFile** is called by the thread which was active at the time you issued the **bp** command:

```dbgcmd
kd> bp /t @$thread nt!ntopenfile
```

This breakpoint will not be triggered when any other thread calls **NtOpenFile**.

For a list of automatic pseudo-registers, see [Pseudo-Register Syntax](pseudo-register-syntax.md).

### <span id="using_a_script_file_to_control_execution"></span><span id="USING_A_SCRIPT_FILE_TO_CONTROL_EXECUTION"></span>Using a Script File to Control Execution

Another way to execute until a specified state is reached is to create a script file that calls itself recursively, testing the desired state in each iteration.

Typically, this script file will contain the [**.if**](-if.md) and [**.else**](-else.md) tokens. You can use a command such as [**t (Trace)**](t--trace-.md) to execute a single step, and then test the condition in question.

For example, if you wish to execute until the **eax** register contains the value 0x1234, you can create a script file called *eaxstep* that contains the following line:

```dbgcmd
.if (@eax == 1234) { .echo 1234 } .else { t "$<eaxstep" }
```

Then issue the following command from the Debugger Command window:

```dbgcmd
t "$<eaxstep"
```

This **t** command will execute a single step, and then execute the quoted command. This command happens to be [**$&lt; (Run Script File)**](-----------------------a---run-script-file-.md), which runs the *eaxstep* file. The script file tests the value of **eax**, runs the **t** command, and then calls itself recursively. This continues until the **eax** register equals 0x1234, at which point the [**.echo (Echo Comment)**](-echo--echo-comment-.md) command prints a message to the Debugger Command window, and execution stops.

For details on script files, see [Using Script Files](using-script-files.md) and [Using Debugger Command Programs](using-debugger-command-programs.md).

 

 





