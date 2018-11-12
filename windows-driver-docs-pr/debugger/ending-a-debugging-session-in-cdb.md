---
title: Ending a Debugging Session in CDB
description: You can exit CDB by entering the q (Quit) command. This command also closes the application that you are debugging.
ms.assetid: B32AD09D-7F88-420E-94BD-59FAE6EC1720
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Ending a Debugging Session in CDB


You can exit CDB by entering the [**q (Quit)**](q--qq--quit-.md) command. This command also closes the application that you are debugging.

The [**qd (Quit and Detach)**](qd--quit-and-detach-.md) command detaches CDB from the target application, exits the debugger, and leaves the target application running. If you used the **-pd** command-line option when you started the debugger, detaching occurs if the session is ended for any reason. (This technique makes **-pd** especially useful when you are debugging a sensitive process, such as the Client Server Run-Time Subsystem (CSRSS), that you do not want to end.)

If the debugger is not responding, you can exit by pressing [**CTRL+B**](ctrl-b--quit-local-debugger-.md) and then ENTER. This method is a secondary exit mechanism. It abruptly ends the debugger and is similar to ending a process through Task Manager or by closing the window.

To end a user-mode debugging session, return the debugger to dormant mode, and close the target application, you can use the following method:

-   Enter the [**.kill (Kill Process)**](-kill--kill-process-.md) command.

To end a user-mode debugging session, return the debugger to dormant mode, and set the target application running again, you can use the following methods:

-   Enter the [**.detach (Detach from Process)**](-detach--detach-from-process-.md) command. If you are debugging multiple targets, this command detaches from the current target and continues the debugging session with the remaining targets.

-   Enter the [**qd (Quit and Detach)**](qd--quit-and-detach-.md) command.

-   Enter the [**q (Quit)**](q--qq--quit-.md) command, if you started the debugger with the **-pd** option.

To end a user-mode debugging session, return the debugger to dormant mode, but leave the target application in the debugging state, you can use the following method:

-   Enter the [**.abandon (Abandon Process)**](-abandon--abandon-process-.md) command.

For more information about reattaching to the target, see [Reattaching to the Target Application](reattaching-to-the-target-application.md).

 

 





