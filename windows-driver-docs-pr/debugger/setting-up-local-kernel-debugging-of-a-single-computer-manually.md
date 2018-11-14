---
title: Setting Up Local Kernel Debugging of a Single Computer Manually
description: Setting Up Local Kernel Debugging of a Single Computer Manually
ms.assetid: FC717B1C-A68A-4002-A528-BFC3521C5E8A
ms.author: domars
ms.date: 07/11/2018
ms.localizationpriority: medium
---

# Setting Up Local Kernel Debugging of a Single Computer Manually


Debugging Tools for Windows supports *local kernel debugging*. This is kernel-mode debugging on a single computer. In other words, the debugger runs on the same computer that is being debugged. With local debugging you can examine state, but not break into kernel mode processes that would cause the OS to stop running.

The *local* bcdedit option is available in Windows 8.0 and Windows Server 2012 and later.

## <span id="starting_local_kernel_debugging"></span><span id="STARTING_LOCAL_KERNEL_DEBUGGING"></span>Setting Up Local Kernel-Mode Debugging

> [!IMPORTANT]
> Before using bcdedit to change boot information you may need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC. 
> You can re-enable Secure Boot once you’re done debugging and you’ve disabled kernel debugging on the local computer.  


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

 

 






