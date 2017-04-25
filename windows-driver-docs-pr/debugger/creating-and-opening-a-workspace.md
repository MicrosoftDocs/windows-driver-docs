---
title: Creating and Opening a Workspace
description: Creating and Opening a Workspace
ms.assetid: 0163f380-f982-4635-a450-ed83f0b52e03
keywords: ["workspaces, creating", "workspaces, opening", "workspaces, named workspaces", "workspaces, default workspaces", "workspaces, types of workspaces"]
---

# Creating and Opening a Workspace


## <span id="ddk_creating_and_opening_a_workspace_dbg"></span><span id="DDK_CREATING_AND_OPENING_A_WORKSPACE_DBG"></span>


WinDbg has two kinds of workspaces: *default workspaces* and *named workspaces*.

### <span id="default_workspaces"></span><span id="DEFAULT_WORKSPACES"></span>Default Workspaces

WinDbg has several different kinds of default workspaces:

-   The *base workspace* is used when WinDbg is in a dormant state.

-   The *default user-mode workspace* is used when you are attaching to a user-mode process (by using the **-p**[**command-line option**](https://msdn.microsoft.com/library/windows/hardware/ff561306) or by using the [File | Attach to a Process](https://msdn.microsoft.com/library/windows/hardware/ff545325) command).

-   The *remote default workspace* is used when you are connecting to a debugging server.

-   The *default kernel-mode workspace* is used when WinDbg begins a kernel-mode debugging session.

-   The *processor-specific workspace* is used during kernel-mode debugging after WinDbg attaches to the target computer. There are separate processor-specific workspaces for x86-based and x64-based processors.

When WinDbg creates a user-mode process for debugging, a workspace is created for that executable file. Each created executable file has its own workspace.

When WinDbg analyzes a dump file, a workspace is created for that dump file analysis session. Each dump file has its own workspace.

When you begin a debugging session, the appropriate workspace is loaded. When you end a debugging session or exit WinDbg, a dialog box is displayed and asks you if you want to save the changes that you have made to the current workspace. If you start WinDbg with the **-QY**[**command-line option**](https://msdn.microsoft.com/library/windows/hardware/ff561306), this dialog box does not appear, and workspaces are automatically saved. Also, if you start WinDbg by the **-Q** command-line option, this dialog box does not appear, and no changes are saved.

Workspaces load in a cumulative manner. The base workspace is always loaded first. When you begin a particular debugging action, the appropriate workspace is loaded. So most debugging is completed after two workspaces have been loaded. Kernel-mode debugging is completed after three workspaces have been loaded (the base workspace, the default kernel-mode workspace, and the processor-specific workspace).

For greatest efficiency, you should save settings in lower-level workspaces if you want them to apply to all of your WinDbg work.

**Note**   The layout of the debugging information windows is one exception to the cumulative behavior of workspaces. The position, docking status, and size of each window are determined by only the most recent workspace that you opened. This behavior includes the contents of the Watch window and the locations that you viewed in each [Memory window](memory-window.md). The command history in the [Debugger Command window](debugger-command-window.md) is not cleared when a new workspace is opened, but all other window states are reset.

 

To access the base workspace, start WinDbg with no target, or click [Stop Debugging](https://msdn.microsoft.com/library/windows/hardware/ff541838) on the **Debug** menu after your session is complete. You can then make any edits that are allowed in the base workspace.

### <span id="named_workspaces"></span><span id="NAMED_WORKSPACES"></span>Named Workspaces

You can also give workspaces names and then save or load them individually. After you load a named workspace, all automatic loading and saving of default workspaces is disabled.

Named workspaces contain some additional information that default workspaces do not. For more information about this additional information, see [Workspace Contents](workspace-contents.md).

### <span id="opening__saving__and_clearing_workspaces"></span><span id="OPENING__SAVING__AND_CLEARING_WORKSPACES"></span>Opening, Saving, and Clearing Workspaces

To control workspaces, you can do the following:

-   Open and load a named workspace by using the **-W** [**command-line option**](https://msdn.microsoft.com/library/windows/hardware/ff561306).

-   Open and load a workspace from a file by using the **-WF** [**command-line option**](https://msdn.microsoft.com/library/windows/hardware/ff561306).

-   Disable all automatic workspace loading by using the **-WX** [**command-line option**](https://msdn.microsoft.com/library/windows/hardware/ff561306). Only explicit workspace commands cause workspaces to be saved or loaded.

-   Open and load a named workspace by clicking [Open Workspace](https://msdn.microsoft.com/library/windows/hardware/ff545361) on the **File** menu or pressing CTRL+W.

-   Save the current default workspace or the current named workspace by clicking [Save Workspace](https://msdn.microsoft.com/library/windows/hardware/ff545375) on the **File** menu.

-   Assign a name to the current workspace and save it by clicking [Save Workspace As](https://msdn.microsoft.com/library/windows/hardware/ff545380) on the **File** menu.

-   Delete specific items and settings from the current workspace by clicking [Clear Workspace](https://msdn.microsoft.com/library/windows/hardware/ff545328) on the **File** menu.

-   Delete workspaces by clicking [Delete Workspaces](https://msdn.microsoft.com/library/windows/hardware/ff545338) on the **File** menu.

-   Open and load a workspace from a file by clicking [Open Workspace in File](https://msdn.microsoft.com/library/windows/hardware/ff545364) on the **File** menu.

-   Save a workspace to a file by clicking [Save Workspace to File](https://msdn.microsoft.com/library/windows/hardware/ff545383) on the **File** menu.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Creating%20and%20Opening%20a%20Workspace%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




