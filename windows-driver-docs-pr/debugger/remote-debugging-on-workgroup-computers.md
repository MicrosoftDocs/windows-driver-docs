---
title: Remote Debugging on Workgroup Computers
description: You can perform remote debugging with computers that are joined to a workgroup.
ms.assetid: 0E740E1A-8DEA-4086-AE9D-6B135BF278B0
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Remote Debugging on Workgroup Computers


You can perform remote debugging with computers that are joined to a workgroup. First configure the computer that will run the debugging server. Then activate the debugging server. After the debugging server is activated, you can connect to the server from a debugging client.

## <span id="Configuring_the_debugging_server_computer"></span><span id="configuring_the_debugging_server_computer"></span><span id="CONFIGURING_THE_DEBUGGING_SERVER_COMPUTER"></span>Configuring the debugging server computer


-   Create a local administrator account, and log on using that account.
-   Enable file and printer sharing for your active network. For example if your active network is Private, enable file and printer sharing for Private networks.

    You can use Control Panel to enable file and printer sharing. For example, here are the steps in Windows 8.

    1.  Open Control Panel.
    2.  Click **Network and Internet** and then **Network and Sharing Center**. Under **View your active networks**, note the type of network (for example, Private) that is active.
    3.  Click **Change advanced sharing settings**. For your active network type, select **Turn on network discovery** and **Turn on file and printer sharing**.
-   Start the remote registry service by following these steps.

    1.  In a Command Prompt window or in the Run box, enter **services.msc**.
    2.  Right click **Remote Registry**, and choose **Start**.
-   Turn off the ForceGuest feature by following these steps.

    1.  In a Command Prompt window or in the Run box, enter **regedit**.
    2.  In Registry Editor, set this value to 0.

        **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa ForceGuest**

## <span id="Activating_the_debugging_server"></span><span id="activating_the_debugging_server"></span><span id="ACTIVATING_THE_DEBUGGING_SERVER"></span>Activating the debugging server


You can activate the debugging server through the debugger or by using a process server or a KD connection server. For more information, see the following topics.

-   [**Activating a Debugging Server**](activating-a-debugging-server.md)
-   [**Activating a Process Server**](activating-a-process-server.md)
-   [**Activating a KD Connection Server**](activating-a-kd-connection-server.md)

## <span id="Activating_the_debugging_client"></span><span id="activating_the_debugging_client"></span><span id="ACTIVATING_THE_DEBUGGING_CLIENT"></span>Activating the debugging client


There are several ways to activate a debugging client. For more information, see the following topics.

-   [**Activating a Debugging Client**](activating-a-debugging-client.md)
-   [**Activating a Smart Client**](activating-a-smart-client.md)
-   [**Activating a Smart Client (Kernel Mode)**](activating-a-smart-client--kernel-mode-.md)
-   [**Searching for Process Servers**](searching-for-process-servers.md)
-   [**Searching for KD Connection Servers**](searching-for-kd-connection-servers.md)

**Note**  
If you are using a named pipe to connect a debugging client to a debugging server, you must provide the user name and password of an account that has access to the computer running the debugging server. Use one, but not both, of the following options.

- Log on to the debugging client computer with an account that shares the user name and password of an account on the debugging server computer.
- On the debugging client computer, in a Command Prompt window, enter the following command.

  **net use \\\\**<em>Server</em>**\\ipc$ /user:**<em>UserName</em>

  where *Server* is the name of the server computer, and *UserName* is the name of an account that has access to the server computer.

  When you are prompted, enter the password for *UserName*.

 

 

 





