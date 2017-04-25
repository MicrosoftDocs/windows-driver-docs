---
title: Unresolved Breakpoints (bu Breakpoints)
description: Unresolved Breakpoints (bu Breakpoints)
ms.assetid: 2c97314b-3098-47a0-8f15-3b7d61c95529
keywords: ["breakpoints, deferred", "deferred breakpoints", "breakpoints, BP versus BU", "breakpoints, unresolved"]
---

# Unresolved Breakpoints (bu Breakpoints)


If a [breakpoint](using-breakpoints.md) is set for a routine name that has not been loaded, the breakpoint is called a *deferred*, *virtual*, or *unresolved* breakpoint. (These terms are used interchangeably.) Unresolved breakpoints are not associated with any specific load of a module. Every time that a new application is loaded, it is checked for this routine name. If this routine appears, the debugger computes the actual coded address of the virtual breakpoint and enables the breakpoint.

If you set a breakpoint by using the **bu** command, the breakpoint is automatically considered unresolved. If this breakpoint is in a loaded module, the breakpoint is still enabled and functions normally. However, if the module is later unloaded and reloaded, this breakpoint does not vanish. On the other hand, a breakpoint that you set with **bp** is immediately resolved to an address.

There are three primary differences between **bp** breakpoints and **bu** breakpoints:

-   A **bp** breakpoint location is always converted to an address. If a module change moves the code at which a **bp** breakpoint was set, the breakpoint remains at the same address. On the other hand, a **bu** breakpoint remains associated with the symbolic value (typically a symbol plus an offset) that was used, and it tracks this symbolic location even if its address changes.

-   If a **bp** breakpoint address is found in a loaded module, and if that module is later unloaded, the breakpoint is removed from the breakpoint list. On the other hand, **bu** breakpoints persist after repeated unloads and loads.

-   Breakpoints that you set with **bp** are not saved in WinDbg [workspaces](using-workspaces.md). Breakpoints that are set with **bu** are saved in workspaces.

### <span id="controlling_address_breakpoints_and_unresolved_breakpoints"></span><span id="CONTROLLING_ADDRESS_BREAKPOINTS_AND_UNRESOLVED_BREAKPOINTS"></span>Controlling Address Breakpoints and Unresolved Breakpoints

Address breakpoints can be created with the [**bp (Set Breakpoint)**](https://msdn.microsoft.com/library/windows/hardware/ff538903) command, or the **bm (Set Symbol Breakpoint)** command when the **/d** switch is included. Unresolved breakpoints can be created with the **bu (Set Unresolved Breakpoint)** command, or the **bm** command when the **/d** switch is not included. Commands that disable, enable, and modify breakpoints apply to all kinds of breakpoints. Commands that display a list of breakpoints include all breakpoints, and indicate the type of each. For a listing of these commands, see [Methods of Controlling Breakpoints](methods-of-controlling-breakpoints.md).

The WinDbg **Breakpoints** dialog box displays all breakpoints, indicating unresolved breakpoints with the notation "u". This dialog box can be used to modify any breakpoint.The **Command** text box on this dialog box can be used to create any type of breakpoint; if the type is omitted, an unresolved breakpoint is created. For details, see [Edit | Breakpoints](https://msdn.microsoft.com/library/windows/hardware/ff542806). When you set a breakpoint by using the mouse in the WinDbg [Disassembly window](disassembly-window.md) or [Source window](source-window.md), the debugger creates an unresolved breakpoint.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Unresolved%20Breakpoints%20%28bu%20Breakpoints%29%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




