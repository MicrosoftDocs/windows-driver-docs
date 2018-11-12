---
title: Setting Up User-Mode Debugging in Visual Studio
description: There are two user-mode debuggers available in the Microsoft Visual Studio environment.
ms.assetid: D36220DF-1ACB-4D8B-BC4C-1A6FCB54CA15
ms.author: domars
ms.date: 05/11/2018
ms.localizationpriority: medium
---

# <span id="debugger.setting_up_user-mode_debugging_in_visual_studio"></span>Setting Up User-Mode Debugging in Visual Studio


There are two user-mode debuggers available in the Microsoft Visual Studio environment. One is the Windows User-Mode Debugger, which is included in Debugging Tools for Windows. The other is the Visual Studio Debugger, which is part of the Visual Studio product. This topic describes how to get set up to use the Windows User-Mode Debugger from within the Visual Studio environment.

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>

## <span id="Debugging_a_User-Mode_Process_on_the_Local_Computer"></span><span id="debugging_a_user-mode_process_on_the_local_computer"></span><span id="DEBUGGING_A_USER-MODE_PROCESS_ON_THE_LOCAL_COMPUTER"></span>Debugging a User-Mode Process on the Local Computer


No special setup is required for debugging a user-mode process on the local computer. For information about attaching to a process or launching a process under the debugger, see [Debugging a User-Mode Process Using Visual Studio](debugging-a-user-mode-process-using-visual-studio.md).

## <span id="Debugging_a_User-Mode_Process_on_a_Target_Computer"></span><span id="debugging_a_user-mode_process_on_a_target_computer"></span><span id="DEBUGGING_A_USER-MODE_PROCESS_ON_A_TARGET_COMPUTER"></span>Debugging a User-Mode Process on a Target Computer


In some cases, two computers are used for debugging. The debugger runs on the *host computer*, and the code that is being debugged runs on the *target computer*. In Visual Studio (running on the host computer), you can use the Windows User-Mode Debugger to attach to a user-mode process on a target computer.

On the target computer, go to **Control Panel&gt;Network and Internet&gt;Network and Sharing Center&gt;Advanced sharing settings**. Under **Guest or Public**, select **Turn on network discovery** and **Turn on file and printer sharing**.

You can do the rest of the configuration from the host computer:

1.  On the host computer, in Visual Studio, on the **Tools** menu, choose **Attach to Process**.
2.  For **Transport**, choose **Windows User Mode Debugger**.
3.  To the right of the **Qualifier** box, click the **Browse** button.
4.  Click the **Add** button.
5.  Enter the name of the target computer.
6.  To the right of **Configure Target Computer**, click the **Configure** button. The **Configure Target Computer** dialog box opens and displays the configuration progress.
7.  When the configuration is complete, in the **Configure Computers** dialog box, click **OK**.

 

 





