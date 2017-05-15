---
title: Using Breakpoints
description: Using Breakpoints
ms.assetid: d1880895-dc01-429b-af48-762cb24539f1
keywords: ["Debugger Engine, breakpoints", "breakpoints"]
---

# Using Breakpoints


## <span id="ddk_breakpoints_dbx"></span><span id="DDK_BREAKPOINTS_DBX"></span>


Breakpoints are event triggers which, when the breakpoint's conditions are satisfied, will halt execution of the target and break into the debugger. Breakpoints allow the user to analyze and perhaps modify the target when execution reaches a certain point or when a certain memory location is accessed.

The debugger engine inserts a *software breakpoint* into a target by modifying the processor instruction at the breakpoint's location; this modification is invisible to the engine's clients. A software breakpoint is triggered when the target executes the instruction at the breakpoint location. A *processor breakpoint* is inserted into the target's processor by the debugger engine; its capabilities are processor-specific. It is triggered by the processor when the memory at the breakpoint location is accessed; what type of access will trigger this breakpoint is specified when the breakpoint is created.

This topic includes:

[Setting Breakpoints](setting-breakpoints.md)

[Controlling Breakpoint Flags and Parameters](controlling-breakpoint-flags-and-parameters.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Breakpoints%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




