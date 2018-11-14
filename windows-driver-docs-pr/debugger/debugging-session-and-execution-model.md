---
title: Debugging Session and Execution Model
description: Debugging Session and Execution Model
ms.assetid: 1cc2c055-447c-44cd-94d4-ae3dfa8243fb
keywords: ["Debugger Engine, execution model", "execution model", "Debugger Engine, debugging session"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging Session and Execution Model


The debugger engine can debug multiple targets, simultaneously. A *debugging session* begins when the engine acquires a target and continues until all of the targets have been discarded. A debugging session is *inaccessible* while the targets are executing and *accessible* when the current target is suspended. The engine can only be used to examine and manipulate targets while the session is accessible.

The main loop of a debugger typically consists of setting the execution status, calling the method [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229) and handling the generated [events](events.md#events). When **WaitForEvent** is called, the session becomes inaccessible.

When an event occurs in a target, the engine suspends all targets and the session becomes accessible. The engine then notifies the event callbacks of the event and follows the event filter rules. The event callbacks and event filters determine how execution in the target should proceed. If they determine that the engine should break into the debugger, the **WaitForEvent** method returns and the session remains accessible; otherwise, the engine will resume execution of the target in the manner determined by the event callbacks and event filters, and the session becomes inaccessible again.

For the duration of the **WaitForEvent** call--in particular, while notifying the event callbacks and processing the filter rules--the engine is in a state referred to as "inside a wait". While in this state, **WaitForEvent** cannot be called (it is not reentrant).

There are two steps involved in initiating execution in a target: setting the execution status, and then calling **WaitForEvent**. The execution status can be set using the method [**SetExecutionStatus**](https://msdn.microsoft.com/library/windows/hardware/ff556693) or by executing a debugger command that sets the execution status--for example, **g(Go)** and **p (Step)**.

If a sequence of debugger commands are executed together--for example, "**g ; ? @$ip**"--an *implicit wait* will occur after any command that requires execution in the target if that command is not the last command in the sequence. An implicit wait cannot occur when the debugger engine is in the state "inside a wait"; in this case, the execution of the commands will stop and the current command--the one that attempted to cause the implicit wait--will be interpreted as an indication of how execution in the target should proceed. The rest of the commands will be discarded.

**Note**   When determining whether the session is accessible or inaccessible, limited execution of a target (for example, stepping) is considered execution by the engine. When the limited execution is complete, the session becomes accessible.

 

### <span id="host_engine"></span><span id="HOST_ENGINE"></span>Host Engine

When debugging remotely, you can use multiple instances of the debugger engine. Exactly one of these instances maintains the debugging session; this instance is called the *host engine*.

All debugger operations are relative to the host engine, for example, symbol loading and extension loading.

 

 





