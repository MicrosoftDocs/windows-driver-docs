---
title: Remote Debugging Using KD
description: Remote debugging involves two debuggers running at two different locations.
ms.assetid: 274CAB1D-DD3B-4ACD-919C-8B8C253BCE50
ms.author: domars
ms.date: 05/03/2018
ms.localizationpriority: medium
---

# Remote Debugging Using KD


Remote debugging involves two debuggers running at two different locations. The debugger that performs the debugging is called the *debugging server*. The second debugger, called the *debugging client*, controls the debugging session from a remote location. To establish a remote session, you must set up the debugging server first and then activate the debugging client.

Remote debugging can be useful when you would like to involve someone else in looking at an issue, that you are debugging on a PC.

The code that is being debugged could be running on the same computer that is running the debugging server, or it could be running on a separate computer. If the debugging server is performing user-mode debugging, then the process that is being debugged can run on the same computer as the debugging server. If the debugging server is performing kernel-mode debugging, then the code being debugged would typically run on a separate target computer.

The following diagram illustrates a remote session where the debugging server, running on a host computer, is performing kernel-mode debugging of code that is running on a separate target computer.

![diagram that shows remote, host, and target computers](images/clientservertarget.png)

There are several transport protocols you can use for a remote debugging connection: TCP, NPIPE, SPIPE, SSL, and COM Port. Suppose you have chosen to use TCP as the protocol and you have chosen to use KD as both the debugging client and the debugging server. You can use the following procedure to establish a remote kernel-mode debugging session:

1. On the host computer, open KD and establish a kernel-mode debugging session with a target computer. (See [Performing Kernel-Mode Debugging Using KD](performing-kernel-mode-debugging-using-kd.md).)
2. Break in by pressing CRTL-Break.
3. Enter the following command.

   **.server tcp:port=5005**

   **Note**  The port number 5005 is arbitrary. The port number is your choice.

     

4. KD will respond with output similar to the following.

   ```dbgcmd
   Server started.  Client can connect with any of these command lines
   0: <debugger> -remote tcp:Port=5005,Server=YourHostComputer
   ```

5. On the remote computer, open a Command Prompt window, and enter the following command.

   **kd -remote tcp:Port=5005,Server=**<em>YourHostComputer</em>

   where *YourHostComputer* is the name of your host computer, which is running the debugging server.

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For complete information about launching KD (and establishing remote debugging) at the command line, see [**KD Command-Line Options**](kd-command-line-options.md).

 

 





