---
title: Changing Contexts
description: Changing Contexts
ms.assetid: 3690903c-4281-4c65-98b0-00ca22206168
keywords: ["context", "logon session, context", "context, session context", "session, context", "user sessions", "session"]
ms.author: domars
ms.date: 08/02/2018
ms.localizationpriority: medium
---

# Changing Contexts


## <span id="ddk-changing-contexts_dbg"></span><span id="DDK_CHANGING_CONTEXTS_DBG"></span>


In kernel-mode debugging, there are many processes, threads, and sometimes user sessions that are executing at the same time. Therfore, phrases such as "virtual address 0x80002000" or "the **eax** register" are ambiguous. You must specify the *context* in which such phrases can be understood.

The debugger has five different contexts that you can set while you are debugging:

1.  The session context indicates the default user session. 

2.  The process context determines how the debugger interprets virtual addresses.

3.  The *user-mode address context* is almost never set directly. This context is automatically set when you change the process context.

4.  The register context determines how the debugger interprets registers and also controls the results of a stack trace. This context is also known as the *thread context*, although that term is not completely accurate. An *explicit context* is also a type of register context. If you specify an explicit context, that context is used instead of the current register context.

5.  The local context determines how the debugger interprets local variables. This context is also known as the *scope*.

### <span id="session-context"></span><span id="SESSION_CONTEXT"></span>Session Context

Multiple logon sessions can run at the same time. Each logon session has its own processes.

The [**!session**](-session.md) extension displays all logon sessions or changes the current session context.

The session context is used by the [**!sprocess**](-sprocess.md) and [**!spoolused**](https://msdn.microsoft.com/library/windows/hardware/ff565361) extensions when the session number is entered as "-2".

When the session context is changed, the process context is automatically changed to the active process for that session.

### <span id="process-context"></span><span id="PROCESS_CONTEXT"></span>Process Context

Each process has its own page directory that records how virtual addresses are mapped to physical addresses. When any thread within a process is executing, the Windows operating system uses this page directory to interpret virtual addresses.

During user-mode debugging, the current process determines the process context. Virtual addresses that are used in debugger commands, extensions, and debugging information windows are interpreted by using the page directory of the current process.

During kernel-mode debugging, you can set the process context by using the [**.process (Set Process Context)**](-process--set-process-context-.md) command. Use this command to select which process's page directory is used to interpret virtual addresses. After you set the process context, you can use this context in any command that takes addresses. You can even set breakpoints at this address. By including a **/i** option in the **.process** command to specify invasive debugging, you can also use the kernel debugger to set breakpoints in user space.

You can also set user-mode breakpoints from the kernel debugger by using a process-specific breakpoint on a kernel-space function. Set strategic breakpoints and wait for the appropriate context to come up.

The *user-mode address context* is part of the process context. Typically, you do not have to set the user-mode address context directly. If you set the process context, the user-mode address context automatically changes to the directory base of the relevant page table for the process. 

When you set the process context during kernel-mode debugging, that process context is retained until another **.process** command changes the context. The user-mode address context is also retained until a **.process** or **.context** command changes it. These contexts are not changed when the target computer executes, and they are not affected by changes to the register context or the local context.

### <span id="register-context"></span><span id="REGISTER_CONTEXT"></span>Register Context

Each thread has its own register values. These values are stored in the CPU registers when the thread is executing and are stored in memory when another thread is executing.

During user-mode debugging, the current thread typically determines the register context. Any reference to registers in debugger commands, extensions, and debugging information windows is interpreted according to the current thread's registers.

You can change the register context to a value other than the current thread while you are performing user-mode debugging by using one of the following commands:

[**.cxr (Display Context Record)**](-cxr--display-context-record-.md)

[**.ecxr (Display Exception Context Record)**](-ecxr--display-exception-context-record-.md)

During kernel-mode debugging, you can control the register context by using a variety of debugger commands, including the following commands:

[**.thread (Set Register Context)**](-thread--set-register-context-.md)

[**.cxr (Display Context Record)**](-cxr--display-context-record-.md)

[**.trap (Display Trap Frame)**](-trap--display-trap-frame-.md)

These commands do not change the values of the CPU registers. Instead, the debugger retrieves the specified register context from its location in memory. Actually, the debugger can retrieve only the *saved* register values. (Other values are set dynamically and are not saved. The saved values are sufficient to re-create a stack trace.

After the register context is set, the new register context is used for any commands that use register values, such as [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) and [**r (Registers)**](r--registers-.md).

However, when you are debugging multiprocessor computers, some commands enable you to specify a processor. (For more information about such commands, see [Multiprocessor Syntax](multiprocessor-syntax.md).) If you specify a processor for a command, the command uses the register context of the active thread on the specified processor instead of the current register context, even if the specified processor is the currently-active processor.

Also, if the register context does not match the current processor mode setting, these commands produce incorrect or meaningless output. To avoid the output errors, commands that depend on the register state fail until you change the processor mode to match the register context. To change the processor mode, use the [**.effmach (Effective Machine)**](-effmach--effective-machine-.md) command,

Changing the register context can also change the local context. In this manner, the register context can affect the display of local variables.

If any application execution, stepping, or tracing occurs, the register context is immediately reset to match the program counter's position. In user mode, the register context is also reset if the current process or thread is changed.

The register context affects stack traces, because the stack trace begins at the location that the stack pointer register (**esp** on an x86-based processor) points to. If the register context is set to an invalid or inaccessible value, stack traces cannot be obtained.

You can apply a processor breakpoint (data breakpoint) to a specific register context by using the [**.apply\_dbp (Apply Data Breakpoint to Context)**](-apply-dbp--apply-data-breakpoint-to-context-.md) command.

### <span id="local-context"></span><span id="LOCAL_CONTEXT"></span>Local Context

When a program is executing, the meaning of local variables depends on the location of the program counter, because the scope of such variables extends only to the function that they are defined in.

When you are performing user-mode or kernel-mode debugging, the debugger uses the scope of the current function (the current frame on the stack) as the local context. To change this context, use the [**.frame (Set Local Context)**](-frame--set-local-context-.md) command, or double-click the desired frame in the [Calls window](calls-window.md).

In user-mode debugging, the local context is always a frame within the stack trace of the current thread. In kernel-mode debugging, the local context is always a frame within the stack trace of the current register context's thread.

You can use only one stack frame at a time for the local context. Local variables in other frames cannot be accessed.

The local context is reset if any of the following events occur:

-   Any program execution, stepping or tracing

-   Any use of the thread delimiter (~) in any command

-   Any change to the register context

The [**!for\_each\_frame**](-for-each-frame.md) extension enables you to execute a single command repeatedly, once for each frame in the stack. This command changes the local context for each frame, executes the specified command, and then returns the local context to its original value.

 

 





