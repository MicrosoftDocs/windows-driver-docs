---
title: Ending a Debugging Session in CDB
description: You can exit CDB by entering the q (Quit) command. This command also closes the application that you are debugging.
ms.assetid: B32AD09D-7F88-420E-94BD-59FAE6EC1720
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Ending%20a%20Debugging%20Session%20in%20CDB%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




