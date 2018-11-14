---
title: Using Breakpoints with the Debugger Engine API
description: Using Breakpoints Debugger Engine API - Setting and Controlling 
ms.assetid: d1880895-dc01-429b-af48-762cb24539f1
keywords: ["Debugger Engine, breakpoints", "breakpoints"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Breakpoints with the Debugger Engine API


## <span id="ddk_breakpoints_dbx"></span><span id="DDK_BREAKPOINTS_DBX"></span>


Breakpoints are event triggers which, when the breakpoint's conditions are satisfied, will halt execution of the target and break into the debugger. Breakpoints allow the user to analyze and perhaps modify the target when execution reaches a certain point or when a certain memory location is accessed.

The debugger engine inserts a *software breakpoint* into a target by modifying the processor instruction at the breakpoint's location; this modification is invisible to the engine's clients. A software breakpoint is triggered when the target executes the instruction at the breakpoint location. A *processor breakpoint* is inserted into the target's processor by the debugger engine; its capabilities are processor-specific. It is triggered by the processor when the memory at the breakpoint location is accessed; what type of access will trigger this breakpoint is specified when the breakpoint is created.

This topic includes:

[Setting Breakpoints](setting-breakpoints.md)

[Controlling Breakpoint Flags and Parameters](controlling-breakpoint-flags-and-parameters.md)

 

 





