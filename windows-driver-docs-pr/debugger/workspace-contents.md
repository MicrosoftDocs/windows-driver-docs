---
title: Workspace Contents
description: Workspace Contents
ms.assetid: aa0a3bab-2907-4bcf-9a48-5669c423447a
keywords: ["workspaces, contents of workspaces", "workspaces, automatically starting a session"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Workspace Contents


## <span id="ddk_workspace_contents_dbg"></span><span id="DDK_WORKSPACE_CONTENTS_DBG"></span>


Each workspace preserves the following information about the current debugging session. This information is applied cumulatively, starting with the base workspace and ending with the most recently-loaded workspace.

-   All break and handling information for exceptions and events. For more information about the break and handling information, see Breakpoints in Workspaces.

-   All open source files. If a source file is not found, an error message appears. You can close these error messages individually or by using the [Window | Close All Error Windows](window---close-all-error-windows.md) command.

-   All user-defined aliases.

Each workspace preserves the following information about the debugger configuration settings. This information is applied cumulatively, starting with the base workspace and ending with the most recently-loaded workspace.

-   The symbol path.

-   The executable image path.

-   The source path. (In remote debugging, the main source path and the local source path are saved.)

-   The current source options that were set with [**l+, l- (Set Source Options)**](l---l---set-source-options-.md).

-   Log file settings.

-   The COM or 1394 kernel connection settings, if the connection was started by using the graphical interface.

-   The most recent paths in each **Open** dialog box (except for the workspace file and text file paths, which are not saved).

-   The current [**.enable\_unicode**](-enable-unicode--enable-unicode-display-.md), [**.force\_radix\_output**](-force-radix-output--use-radix-for-integers-.md), and [**.enable\_long\_status**](-enable-long-status--enable-long-integer-display-.md) settings.

All default workspaces and named workspaces preserve the following information about the WinDbg graphical interface. This information is loaded cumulatively, starting with the base workspace and ending with the most recently-loaded workspace.

-   The title of the WinDbg window

-   The [Automatically Open Disassembly](window---automatically-open-disassembly.md) setting

-   The default font

All default workspaces and named workspaces preserve the following information about the WinDbg graphical interface. This information is not applied cumulatively. It depends only on the most recently-loaded workspace.

-   The size and position of the WinDbg window on the desktop.

-   Which debugging information windows are open.

-   The size and position of each open window, including the window's size, its floating or docked status, whether it is tabbed with other windows, and all of the related settings in its shortcut menu.

-   The location of the pane boundary in the [Debugger Command window](debugger-command-window.md) and the word wrap setting in that window.

-   Whether the toolbar and status bar, and the individual toolbars on each debugging information window, are visible.

-   The customization of the [Registers window](registers-window.md).

-   The flags in the [Calls window](calls-window.md), Locals window, and Watch window.

-   The items that were viewed in the Watch window.

-   The cursor location in each [Source window](source-window.md).

### <span id="named_workspaces"></span><span id="NAMED_WORKSPACES"></span>Named Workspaces

Named workspaces contain additional information that is not stored in default workspaces.

This additional information includes information about the current session state. When a named workspace is saved, the current session is saved. If this workspace is later opened, this session is automatically restarted.

You can start only kernel debugging, dump file debugging, and debugging of spawned user-mode processes in this manner. Remote sessions and user-mode processes that the debugger attached to do not have this session information saved in their workspaces.

You cannot open this kind of named workspace if another session is already active.

### <span id="debugging_clients_and_workspaces"></span><span id="DEBUGGING_CLIENTS_AND_WORKSPACES"></span>Debugging Clients and Workspaces

When you use WinDbg as a debugging client, its workspace saves only values that you set through the graphical interface. Changes that you make through the Debugger Command window are not saved. (This restriction guarantees that only changes that the local client made are reflected, because the Debugger Command window accepts input from all clients and the debugging server.) For more information, see [Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md).

### <span id="breakpoints_in_workspaces"></span><span id="BREAKPOINTS_IN_WORKSPACES"></span>Breakpoints in Workspaces

In addition, breakpoint information is saved in workspaces, including the break address and status. Breakpoints that are active when a session ends are active when the next session is started. However, some of these breakpoints might be unresolved if the proper modules have not yet been loaded.

Breakpoints that you specify by a symbol expression, by a line number, by a numeric address, or by using the mouse in a Source window are all saved in workspaces. Breakpoints that you specify by using the mouse in a Disassembly or Calls window are not saved in workspaces.

If you are debugging multiple user-mode processes, only breakpoints that are associated with process zero are saved.

 

 





