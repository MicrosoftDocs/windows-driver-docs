---
title: Breakpoints
description: Breakpoints
ms.assetid: f805667c-7ee1-4f66-bfc5-7e3b90b35b86
keywords: ["Debugger Engine, breakpoints"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Breakpoints


The [debugger engine](introduction.md#debugger-engine) can create and monitor breakpoints in the target.

There are two types of breakpoints that the engine can insert into a target: software breakpoints and processor breakpoints.

-   *Software breakpoints* are inserted into the target's code by modifying the processor instruction at the breakpoint's location. The debugger engine keeps track of such breakpoints; they are invisible to the clients reading and writing memory at that location. A software breakpoint is triggered when the target executes the modified instruction.

-   *Processor breakpoints* are inserted into the target's processor by the debugger engine. A processor breakpoint can be triggered by different actions, for example, executing an instruction at the location (like software breakpoints), or reading or writing memory at the breakpoint's location. Support for processor breakpoints is dependent on the processor in the target's computer.

A breakpoint's address can be specified by an explicit address, by an expression that evaluates to an address, or by an expression that might evaluate to an address at a future time. In the last case, each time a module is loaded or unloaded in the target, the engine will attempt to reevaluate the expression and insert the breakpoint if it can determine the address; this makes it possible to set breakpoints in modules before they are loaded.

A number of parameters can be associated with a breakpoint to control its behavior:

-   A breakpoint can be associated with a particular thread in the target and will only be triggered by that thread.

-   A breakpoint can have debugger commands associated with it; these commands will automatically be executed when the breakpoint is triggered.

-   A breakpoint can be flagged as inactive until the target has passed it a specified number of times.

-   A breakpoint can be automatically removed the first time it is triggered.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about using breakpoints, see [Using Breakpoints](setting-breakpoints.md).

 

 





