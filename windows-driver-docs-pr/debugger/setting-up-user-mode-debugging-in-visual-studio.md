---
title: Setting Up User-Mode Debugging in Visual Studio
description: There are two user-mode debuggers available in the Microsoft Visual Studio environment.
ms.assetid: D36220DF-1ACB-4D8B-BC4C-1A6FCB54CA15
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# <span id="debugger.setting_up_user-mode_debugging_in_visual_studio"></span>Setting Up User-Mode Debugging in Visual Studio


There are two user-mode debuggers available in the Microsoft Visual Studio environment. One is the Windows User-Mode Debugger, which is included in Debugging Tools for Windows. The other is the Visual Studio Debugger, which is part of the Visual Studio product. This topic describes how to get set up to use the Windows User-Mode Debugger from within the Visual Studio environment.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20User-Mode%20Debugging%20in%20Visual%20Studio%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




