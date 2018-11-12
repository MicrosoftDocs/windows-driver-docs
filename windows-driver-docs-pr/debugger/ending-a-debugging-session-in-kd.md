---
title: Ending a Debugging Session in KD
description: Ending a Debugging Session in KD
ms.assetid: 6CD39971-424D-4F29-9A36-CCD14187DEB0
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Ending a Debugging Session in KD


There are two different ways to exit KD.

-   Issue a [**q (Quit)**](q--qq--quit-.md) command in KD to save the log file, end the debugging session, and exit the debugger. The target computer remains locked.

-   Press [**CTRL+B**](ctrl-b--quit-local-debugger-.md) and then press ENTER to end the debugger abruptly. If you want the target computer to continue to run after the debugger is ended, you must use this method. Because CTRL+B does not remove breakpoints, you should use the following commands first.

    ```dbgcmd
    kd>  bc *
    kd>  g
    ```

Exiting the debugger by using CTRL+B does not clear kernel-mode breakpoints, but attaching a new kernel debugger does clear these breakpoints.

When you are performing remote debugging, [**q**](q--qq--quit-.md) ends the debugging session. CTRL+B exits the debugger but leaves the session active. This situation enables another debugger to connect to the session.

If the [**q (Quit)**](q--qq--quit-.md) command does not work, press [**CTRL+R**](ctrl-r--re-synchronize-.md) and then press ENTER on the host computer's keyboard, and then retry the **q** command. If this procedure does not work, you must use CTRL+B to exit the debugger.

 

 





