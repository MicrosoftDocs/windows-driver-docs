---
title: Debugging Multiple Targets
description: Debugging Multiple Targets
ms.assetid: 93eb6b49-e7a0-4f30-ade8-94019a1adf43
keywords: ["multiple targets", "system", "system, overview"]
---

# Debugging Multiple Targets


## <span id="ddk_debugging_multiple_targets_dbg"></span><span id="DDK_DEBUGGING_MULTIPLE_TARGETS_DBG"></span>


You can debug multiple dump files or live user-mode applications at the same time. Each target contains one or more processes, and each process contains one or more threads.

These targets are also grouped into *systems*. Systems are sets of targets that are grouped together for easy identification and manipulation. Systems are defined as follows:

-   Each kernel-mode or user-mode dump file is a separate system.

-   When you are debugging live user-mode applications on different computers (by using a [process server](process-servers--user-mode-.md), such as Dbgsrv), each application is a separate system.

-   When you are debugging live user-mode applications on the local computer, the applications are combined into a single system.

The *current* or *active* system is the system that you are currently debugging.

### <span id="acquiring_multiple_targets"></span><span id="ACQUIRING_MULTIPLE_TARGETS"></span>Acquiring Multiple Targets

The first target is acquired in the usual manner.

You can debug additional live user-mode applications by using the [**.attach (Attach to Process)**](-attach--attach-to-process-.md) or [**.create (Create Process)**](-create--create-process-.md) command, followed by the **g (Go)** command.

You can debug additional dump files by using the [**.opendump (Open Dump File)**](-opendump--open-dump-file-.md) command, followed by the **g (Go)** command. You can also open multiple dump files when the debugger is started. To open multiple dump files, include multiple **-z** switches in the command, each followed by a different file name.

You can use the preceding commands even if the processes are on different systems. You must start a process server on each system and then use the -premote parameter with **.attach** or **.create** to identify the proper process server. If you use the **.attach** or **.create** command again without specifying the -premote parameter, the debugger attaches to, or creates, a process on the current system.

### <span id="manipulating_systems_and_targets"></span><span id="MANIPULATING_SYSTEMS_AND_TARGETS"></span>Manipulating Systems and Targets

When debugging begins, the current system is the one that the debugger most recently attached to. If an exception occurs, the current system switches to the system that this exception occurred on.

To close one target and continue to debug the other targets, use the [**.kill (Kill Process)**](-kill--kill-process-.md) command. On Microsoft Windows XP and later versions of Windows, you can use the [**.detach (Detach from Process)**](-detach--detach-from-process-.md) command or WinDbg's [Debug | Detach Debuggee](debug---detach-debuggee.md) menu command instead. These commands detach the debugger from the target but leave the target running.

To control the debugging of multiple systems, you can use the following methods:

-   The [**|| (System Status)**](----system-status-.md) command displays information about one or more systems

-   The [**||s (Set Current System)**](--s--set-current-system-.md) command enables you to select the current system

-   (WinDbg only) The [Processes and Threads window](processes-and-threads-window.md) enables you display or select systems, processes, and threads

By using these commands to select the current system, and by using the standard commands to [select the current process and thread](controlling-processes-and-threads.md), you can determine the context of commands that display memory and registers.

However, you cannot separate execution of these processes. The [**g (Go)**](g--go-.md) command always causes all targets to execute together.

**Note**   We recommend that you do not debug live targets and dump targets together, because commands behave differently for each type of debugging. For example, if you use the **g (Go)** command when the current system is a dump file, the debugger begins executing, but you cannot break back into the debugger, because the break command is not recognized as valid for dump file debugging.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Multiple%20Targets%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




