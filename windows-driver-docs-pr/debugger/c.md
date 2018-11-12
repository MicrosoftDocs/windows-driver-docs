---
title: C (Windows Debugger Glossary)
description: Glossary page - C
Robots: noindex, nofollow
ms.assetid: 295b05a3-e27f-4761-a562-7e87e25bfd3b
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# C


<span id="c___expression"></span><span id="C___EXPRESSION"></span>**C++ expression**  
An expression that can be evaluated by the C++ expression evaluator.

<span id="c_call_stack"></span><span id="C_CALL_STACK"></span>**C call stack**  
See call stack.

<span id="call_stack"></span><span id="CALL_STACK"></span>**call stack**  
The set of stack frames for each thread containing representing the function calls made by the thread. Each time a function call is made a new stack frame is pushed onto the top of the stack. When that function returns, the stack frame is popped off the stack.

Sometimes referred to as the or simply the .

<span id="callback_object"></span><span id="CALLBACK_OBJECT"></span>**callback object**  
See event callbacks, input callbacks, and output callbacks.

<span id="checked_build"></span><span id="CHECKED_BUILD"></span>**checked build**  
Two different builds of each NT-based operating system exist:

-   The (or ) of Windows is the end-user version of the operating system. For details, see free build.
-   The (or ) of Windows serves as a testing and debugging aid in the developing of the operating system and kernel-mode drivers. The checked build contains extra error checking, argument verification, and debugging information that is not available in the free build. , making it easier to trace the cause of problems in system software. A checked system or driver can help isolate and track down driver problems that can cause unpredictable behavior, result in memory leaks, or result in improper device configuration.

Although the checked build provides extra protection, it consumes more memory and disk space than the free build. System and driver performance is slower, because additional code paths are executed due to parameter checking and output of diagnostic messages, and some alternate implementations of kernel functions are used.

The checked build of Windows should not be confused with a driver that has been built in one of the Checked Build Environments of the Windows Driver Kit (WDK).

<span id="child_symbol"></span><span id="CHILD_SYMBOL"></span>**child symbol**  
A symbol that is contained in another symbol. For example, the symbol for a member in a structure is a child of the symbol for that structure.

<span id="client"></span><span id="CLIENT"></span>**client**  
See client object.

<span id="client_object"></span><span id="CLIENT_OBJECT"></span>**client object**  
A client object is used for interaction with the debugger engine. It holds per-client state, and provides implementations for the top-level interfaces in the debugger engine API.

<span id="client_thread"></span><span id="CLIENT_THREAD"></span>**client thread**  
The thread in which the client object was created. In general, a client's methods may be called only from this thread. The debugger engine uses this thread to make all calls to the callback object registered with the client.

<span id="code_breakpoint"></span><span id="CODE_BREAKPOINT"></span>**code breakpoint**  
See software breakpoint.

<span id="crash_dump_file"></span><span id="CRASH_DUMP_FILE"></span>**crash dump file**  
A file that contains a snapshot of certain memory regions and other data related to an application or operating system. A crash dump file can be stored and then used to debug the application or operating system at a later time.

A user-mode crash dump file can be created by Windows when an application crashes, and a kernel-mode crash dump file can be created by special Windows routines when Windows itself crashes. There are several different types of crash dump files.

<span id="current_process"></span><span id="CURRENT_PROCESS"></span>**current process**  
The process that the debugger engine is currently controlling. When an event occurs, the current process is set to the event process.

<span id="current_target"></span><span id="CURRENT_TARGET"></span>**current target**  
The target that the debugger engine is currently controlling. When an event occurs, the current target is set to the event target.

<span id="current_thread"></span><span id="CURRENT_THREAD"></span>**current thread**  
The thread that the debugger engine is currently controlling. When an event occurs, the current thread is set to the event thread.

 

 





