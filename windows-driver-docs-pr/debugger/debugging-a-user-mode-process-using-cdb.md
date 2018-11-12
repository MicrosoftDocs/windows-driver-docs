---
title: Debugging a User-Mode Process Using CDB
description: You can use CDB to attach to a running process or to spawn and attach to new process.
ms.assetid: 0C56F6B5-0FBC-45C9-8AB7-218C00F90521
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# <span id="debugger.debugging_a_user-mode_process_using_cdb"></span>Debugging a User-Mode Process Using CDB


You can use CDB to attach to a running process or to spawn and attach to new process.

## <span id="Attaching_to_a_Running_Process"></span><span id="attaching_to_a_running_process"></span><span id="ATTACHING_TO_A_RUNNING_PROCESS"></span>Attaching to a Running Process


### <span id="command_prompt1"></span><span id="COMMAND_PROMPT1"></span>Command Prompt

In a Command Prompt window, you can attach to a running process when you launch CDB. Use one of the following commands:

-   **cdb -p** *ProcessID*
-   **cdb -pn** *ProcessName*

where *ProcessID* is the Process ID of a running process or *ProcessName* is the name of a running process.

For more information about the command-line syntax, see [**CDB Command-Line Options**](cdb-command-line-options.md).

### <span id="cdb_command_window1"></span><span id="CDB_COMMAND_WINDOW1"></span>CDB Command Window

If the debugger is already debugging one or more processes, you can attach to a running process by using the [**.attach (Attach to Process)**](-attach--attach-to-process-.md) command.

The debugger always starts multiple target processes simultaneously, unless some of their threads are frozen or suspended.

If the [**.attach**](-attach--attach-to-process-.md) command is successful, the debugger attaches to the specified process the next time that the debugger issues an execution command. If you use this command several times in a row, execution has to be requested by the debugger as many times as you use this command.

## <span id="Attaching_to_a_Running_Process_Noninvasively"></span><span id="attaching_to_a_running_process_noninvasively"></span><span id="ATTACHING_TO_A_RUNNING_PROCESS_NONINVASIVELY"></span>Attaching to a Running Process Noninvasively


If you want to debug a running process and interfere only minimally in its execution, you should debug the process [noninvasively](noninvasive-debugging--user-mode-.md).

### <span id="command_prompt2"></span><span id="COMMAND_PROMPT2"></span>Command Prompt

To noninvasively debug a running process from the CDB command line, specify the **-pv** option, the **-p** option, and the process ID, in the following syntax.

**cdb -pv -p** *ProcessID*

Or, to noninvasively debug a running process by specifying the process name, use the following syntax instead.

**cdb -pv -pn** *ProcessName*

There are several other useful command-line options. For more information about the command-line syntax, see [**CDB Command-Line Options**](cdb-command-line-options.md).

### <span id="cdb_command_window2"></span><span id="CDB_COMMAND_WINDOW2"></span>CDB Command Window

If the debugger is already active, you can noninvasively debug a running process by entering the [**.attach -v (Attach to Process)**](-attach--attach-to-process-.md) command.

You can use the **.attach** command if the debugger is already debugging one or more processes invasively.

If the **.attach -v** command is successful, the debugger debugs the specified process the next time that the debugger issues an execution command. Because execution is not permitted during noninvasive debugging, the debugger cannot noninvasively debug more than one process at a time. This restriction also means that using the **.attach -v** command might make an existing invasive debugging session less useful.

## <span id="Spawning_a_New_Process"></span><span id="spawning_a_new_process"></span><span id="SPAWNING_A_NEW_PROCESS"></span>Spawning a New Process


CDB can start a user-mode application and then debug the application. The application is specified by name. The debugger can also automatically attach to child processes (additional processes that the original target process started).

Processes that the debugger creates (also known as spawned processes) behave slightly differently than processes that the debugger does not create.

Instead of using the standard heap API, processes that the debugger creates use a special debug heap. You can force a spawned process to use the standard heap instead of the debug heap by using the \_NO\_DEBUG\_HEAP [environment variable](general-environment-variables.md) or the **-hd** command-line option.

Also, because the target application is a child process of the debugger, it inherits the debugger's permissions. This permission might enable the target application to perform certain actions that it could not perform otherwise. For example, the target application might be able to affect protected processes.

In a Command Prompt window, you can spawn a new process when you launch CDB. Enter the following command.

**cdb \[-o\]** *ProgramName* **\[**<em>Arguments</em>**\]**

The **-o** option causes the debugger to attach to child processes. There are several other useful command-line options. For more information about the command-line syntax, see [**CDB Command-Line Options**](cdb-command-line-options.md).

If the debugger is already debugging one or more processes, you can create a new process by entering the [**.create (Create Process)**](-create--create-process-.md) command.

The debugger will always start multiple target processes simultaneously, unless some of their threads are frozen or suspended.

If the [**.create**](-create--create-process-.md) command is successful, the debugger creates the specified process the next time that the debugger issues an execution command. If you use this command several times in a row, execution has to be requested by the debugger as many times as you use this command.

You can control the application's starting directory by using the [**.createdir (Set Created Process Directory)**](-createdir--set-created-process-directory-.md) command before [**.create**](-create--create-process-.md). You can use the **.createdir -I** command or the **-noinh** command-line option to control whether the target application inherits the debugger's handles.

You can activate or deactivate the debugging of child processes by using the [**.childdbg (Debug Child Processes)**](-childdbg--debug-child-processes-.md) command.

## <span id="Reattaching_to_a_Process"></span><span id="reattaching_to_a_process"></span><span id="REATTACHING_TO_A_PROCESS"></span>Reattaching to a Process


If the debugger stops responding or freezes, you can attach a new debugger to the target process. For more information about how to attach a debugger in this situation, see [Reattaching to the Target Application](reattaching-to-the-target-application.md).

 

 





