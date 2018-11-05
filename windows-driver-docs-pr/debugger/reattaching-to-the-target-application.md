---
title: Reattaching to the Target Application
description: Reattaching to the Target Application
ms.assetid: cc137185-58a7-44bf-b262-2698c46730f6
keywords: ["re-attaching to the target application", "process, re-attaching debugger to"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Reattaching to the Target Application


## <span id="ddk_re_attaching_to_the_target_application_dbg"></span><span id="DDK_RE_ATTACHING_TO_THE_TARGET_APPLICATION_DBG"></span>


If the debugger freezes or otherwise stops responding (that is, *crashes*) while you perform user-mode debugging, you can attach a new debugger to the existing process.

**Note**  This method is supported only on Microsoft Windows XP and later versions of Windows. This method does not depend on whether the debugger originally created the process or attached to an existing process. This method does not depend on whether you used the **-pd** option.

 

To reattach a debugger to an existing target application, do the following:

1.  [Determine the process ID](finding-the-process-id.md) of the target application.

2.  Start a new instance of CDB or WinDbg. Use the **-pe** command-line option.

    ```console
    Debugger -pe -p PID 
    ```

    You can also use other [command-line options](command-line-options.md).

    You can also connect from a dormant debugger by using the [**.attach (Attach to Process)**](-attach--attach-to-process-.md) command together with the **-e** option.

3.  After the attach is complete, end the original debugger process.

4.  If the process does not respond properly, it might have a suspend count that is too high. You can use the [**~m (Resume Thread)**](-m--resume-thread-.md) command to reduce the suspend count. For more information about suspend counts, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

If the original debugger is still operating properly, this method might not work. The two debuggers are competing for debugging events, and the Windows operating system does not necessarily assign all of the debugging events to the new debugger.

If the original debugger is ended before you attach the new debugger, the target application is also closed. (However, if the debugger attached with the **-pd** option and then exits normally, the target application continues running. In this situation, a second debugger can attach to the target application without using the **-pe** option.)

If you are already debugging a process and want to detach from the process but leave it frozen in a debugging state, you can use the [**.abandon (Abandon Process)**](-abandon--abandon-process-.md) command. After this command, any Windows debugger can reattach to the process by using the procedure that is described in this topic.

 

 





