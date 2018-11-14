---
title: Unresolved Breakpoints (bu Breakpoints)
description: Unresolved Breakpoints (bu Breakpoints)
ms.assetid: 2c97314b-3098-47a0-8f15-3b7d61c95529
keywords: ["breakpoints, deferred", "deferred breakpoints", "breakpoints, BP versus BU", "breakpoints, unresolved"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Unresolved Breakpoints (bu Breakpoints)


If a [breakpoint](using-breakpoints.md) is set for a routine name that has not been loaded, the breakpoint is called a *deferred*, *virtual*, or *unresolved* breakpoint. (These terms are used interchangeably.) Unresolved breakpoints are not associated with any specific load of a module. Every time that a new application is loaded, it is checked for this routine name. If this routine appears, the debugger computes the actual coded address of the virtual breakpoint and enables the breakpoint.

If you set a breakpoint by using the **bu** command, the breakpoint is automatically considered unresolved. If this breakpoint is in a loaded module, the breakpoint is still enabled and functions normally. However, if the module is later unloaded and reloaded, this breakpoint does not vanish. On the other hand, a breakpoint that you set with **bp** is immediately resolved to an address.

There are three primary differences between **bp** breakpoints and **bu** breakpoints:

-   A **bp** breakpoint location is always converted to an address. If a module change moves the code at which a **bp** breakpoint was set, the breakpoint remains at the same address. On the other hand, a **bu** breakpoint remains associated with the symbolic value (typically a symbol plus an offset) that was used, and it tracks this symbolic location even if its address changes.

-   If a **bp** breakpoint address is found in a loaded module, and if that module is later unloaded, the breakpoint is removed from the breakpoint list. On the other hand, **bu** breakpoints persist after repeated unloads and loads.

-   Breakpoints that you set with **bp** are not saved in WinDbg [workspaces](using-workspaces.md). Breakpoints that are set with **bu** are saved in workspaces.

### <span id="controlling_address_breakpoints_and_unresolved_breakpoints"></span><span id="CONTROLLING_ADDRESS_BREAKPOINTS_AND_UNRESOLVED_BREAKPOINTS"></span>Controlling Address Breakpoints and Unresolved Breakpoints

Address breakpoints can be created with the [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command, or the **bm (Set Symbol Breakpoint)** command when the **/d** switch is included. Unresolved breakpoints can be created with the **bu (Set Unresolved Breakpoint)** command, or the **bm** command when the **/d** switch is not included. Commands that disable, enable, and modify breakpoints apply to all kinds of breakpoints. Commands that display a list of breakpoints include all breakpoints, and indicate the type of each. For a listing of these commands, see [Methods of Controlling Breakpoints](methods-of-controlling-breakpoints.md).

The WinDbg **Breakpoints** dialog box displays all breakpoints, indicating unresolved breakpoints with the notation "u". This dialog box can be used to modify any breakpoint.The **Command** text box on this dialog box can be used to create any type of breakpoint; if the type is omitted, an unresolved breakpoint is created. For details, see [Edit | Breakpoints](edit---breakpoints.md). When you set a breakpoint by using the mouse in the WinDbg [Disassembly window](disassembly-window.md) or [Source window](source-window.md), the debugger creates an unresolved breakpoint.

 

 





