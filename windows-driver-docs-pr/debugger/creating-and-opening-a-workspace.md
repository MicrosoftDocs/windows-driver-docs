---
title: Creating and Opening a Workspace
description: Creating and Opening a Workspace
ms.assetid: 0163f380-f982-4635-a450-ed83f0b52e03
keywords: ["workspaces, creating", "workspaces, opening", "workspaces, named workspaces", "workspaces, default workspaces", "workspaces, types of workspaces"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Creating and Opening a Workspace


## <span id="ddk_creating_and_opening_a_workspace_dbg"></span><span id="DDK_CREATING_AND_OPENING_A_WORKSPACE_DBG"></span>


WinDbg has two kinds of workspaces: *default workspaces* and *named workspaces*.

### <span id="default_workspaces"></span><span id="DEFAULT_WORKSPACES"></span>Default Workspaces

WinDbg has several different kinds of default workspaces:

-   The *base workspace* is used when WinDbg is in a dormant state.

-   The *default user-mode workspace* is used when you are attaching to a user-mode process (by using the **-p**[**command-line option**](windbg-command-line-options.md) or by using the [File | Attach to a Process](file---attach-to-a-process.md) command).

-   The *remote default workspace* is used when you are connecting to a debugging server.

-   The *default kernel-mode workspace* is used when WinDbg begins a kernel-mode debugging session.

-   The *processor-specific workspace* is used during kernel-mode debugging after WinDbg attaches to the target computer. There are separate processor-specific workspaces for x86-based and x64-based processors.

When WinDbg creates a user-mode process for debugging, a workspace is created for that executable file. Each created executable file has its own workspace.

When WinDbg analyzes a dump file, a workspace is created for that dump file analysis session. Each dump file has its own workspace.

When you begin a debugging session, the appropriate workspace is loaded. When you end a debugging session or exit WinDbg, a dialog box is displayed and asks you if you want to save the changes that you have made to the current workspace. If you start WinDbg with the **-QY**[**command-line option**](windbg-command-line-options.md), this dialog box does not appear, and workspaces are automatically saved. Also, if you start WinDbg by the **-Q** command-line option, this dialog box does not appear, and no changes are saved.

Workspaces load in a cumulative manner. The base workspace is always loaded first. When you begin a particular debugging action, the appropriate workspace is loaded. So most debugging is completed after two workspaces have been loaded. Kernel-mode debugging is completed after three workspaces have been loaded (the base workspace, the default kernel-mode workspace, and the processor-specific workspace).

For greatest efficiency, you should save settings in lower-level workspaces if you want them to apply to all of your WinDbg work.

**Note**   The layout of the debugging information windows is one exception to the cumulative behavior of workspaces. The position, docking status, and size of each window are determined by only the most recent workspace that you opened. This behavior includes the contents of the Watch window and the locations that you viewed in each [Memory window](memory-window.md). The command history in the [Debugger Command window](debugger-command-window.md) is not cleared when a new workspace is opened, but all other window states are reset.

 

To access the base workspace, start WinDbg with no target, or click [Stop Debugging](debug---stop-debugging.md) on the **Debug** menu after your session is complete. You can then make any edits that are allowed in the base workspace.

### <span id="named_workspaces"></span><span id="NAMED_WORKSPACES"></span>Named Workspaces

You can also give workspaces names and then save or load them individually. After you load a named workspace, all automatic loading and saving of default workspaces is disabled.

Named workspaces contain some additional information that default workspaces do not. For more information about this additional information, see [Workspace Contents](workspace-contents.md).

### <span id="opening__saving__and_clearing_workspaces"></span><span id="OPENING__SAVING__AND_CLEARING_WORKSPACES"></span>Opening, Saving, and Clearing Workspaces

To control workspaces, you can do the following:

-   Open and load a named workspace by using the **-W** [**command-line option**](windbg-command-line-options.md).

-   Open and load a workspace from a file by using the **-WF** [**command-line option**](windbg-command-line-options.md).

-   Disable all automatic workspace loading by using the **-WX** [**command-line option**](windbg-command-line-options.md). Only explicit workspace commands cause workspaces to be saved or loaded.

-   Open and load a named workspace by clicking [Open Workspace](file---open-workspace.md) on the **File** menu or pressing CTRL+W.

-   Save the current default workspace or the current named workspace by clicking [Save Workspace](file---save-workspace.md) on the **File** menu.

-   Assign a name to the current workspace and save it by clicking [Save Workspace As](file---save-workspace-as.md) on the **File** menu.

-   Delete specific items and settings from the current workspace by clicking [Clear Workspace](file---clear-workspace.md) on the **File** menu.

-   Delete workspaces by clicking [Delete Workspaces](file---delete-workspaces.md) on the **File** menu.

-   Open and load a workspace from a file by clicking [Open Workspace in File](file---open-workspace-in-file.md) on the **File** menu.

-   Save a workspace to a file by clicking [Save Workspace to File](file---save-workspace-to-file.md) on the **File** menu.

 

 





