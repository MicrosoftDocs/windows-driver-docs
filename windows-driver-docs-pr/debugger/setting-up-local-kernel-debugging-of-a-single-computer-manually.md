---
title: Setting Up Local Kernel Debugging of a Single Computer Manually
description: Setting Up Local Kernel Debugging of a Single Computer Manually
ms.assetid: FC717B1C-A68A-4002-A528-BFC3521C5E8A
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up Local Kernel Debugging of a Single Computer Manually


Debugging Tools for Windows supports *local kernel debugging*. This is kernel-mode debugging on a single computer. In other words, the debugger runs on the same computer that is being debugged. With local debugging you can examine state, but not break into kernel mode processes that would cause the OS to stop running.

The *local* bcdedit option is available in Windows 8.0 and Windows Server 2012 and later.

## <span id="starting_local_kernel_debugging"></span><span id="STARTING_LOCAL_KERNEL_DEBUGGING"></span>Setting Up Local Kernel-Mode Debugging


1.  Open a Command Prompt window as Administrator. Enter **bcdedit /debug on**
2.  If the computer is not already configured as the target of a debug transport, enter **bcdedit /dbgsettings local**
3.  Reboot the computer.

## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session


### <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

Open WinDbg as Administrator. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **Local** tab. Click **OK**.

You can also start a session with WinDbg by opening a Command Prompt window as Administrator and entering the following command:

**windbg -kl**

### <span id="Using_KD"></span><span id="using_kd"></span><span id="USING_KD"></span>Using KD

Open a Command Prompt window as Administrator, and enter the following command:

**kd -kl**

## <span id="related_topics"></span>Related topics


[Local Kernel-Mode Debugging](performing-local-kernel-debugging.md)

[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Local%20Kernel%20Debugging%20of%20a%20Single%20Computer%20Manually%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





