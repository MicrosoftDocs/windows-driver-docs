---
title: Debugging a User-Mode Process Using Visual Studio
description: In Microsoft Visual Studio, you can use the Windows User Mode Debugger to attach to a running process or to spawn and attach to a new process. 
ms.assetid: C19D1B6F-B97B-4C1B-AD84-AC974C5F5C8C
ms.author: domars
ms.date: 05/11/2018
ms.localizationpriority: medium
---

# <span id="debugger.debugging_a_user-mode_process_using_visual_studio"></span>Debugging a User-Mode Process Using Visual Studio

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>

In Microsoft Visual Studio, you can use the Windows User Mode Debugger to attach to a running process or to spawn and attach to a new process. The process can run on the same computer that is running the debugger, or it can run on a separate computer.

The procedures shown in this topic require that you have the Windows Driver Kit integrated into Visual Studio. To get the integrated environment, first install Visual Studio, and then install the Windows Driver Kit (WDK). For more information, see [Windows Driver Kit (WDK)](https://go.microsoft.com/fwlink/p?linkid=391063).

## <span id="Attaching_to_a_running_process_on_the_same_computer"></span><span id="attaching_to_a_running_process_on_the_same_computer"></span><span id="ATTACHING_TO_A_RUNNING_PROCESS_ON_THE_SAME_COMPUTER"></span>Attaching to a running process on the same computer


1.  In Visual Studio, from the **Tools** menu, choose **Attach to Process**.
2.  In the **Attach to Process** dialog box, set **Transport** to **Windows User Mode Debugger**, and set **Qualifier** to **Localhost**.
3.  In the **Available Processes** list, select the process that you want to attach to.
4.  Click **Attach**.

### <span id="Noninvasive_debugging"></span><span id="noninvasive_debugging"></span><span id="NONINVASIVE_DEBUGGING"></span>Noninvasive debugging

If you want to debug a running process and interfere only minimally in its execution, you should debug the process [noninvasively](noninvasive-debugging--user-mode-.md).

## <span id="Spawning_a_new_process_on_the_same_computer"></span><span id="spawning_a_new_process_on_the_same_computer"></span><span id="SPAWNING_A_NEW_PROCESS_ON_THE_SAME_COMPUTER"></span>Spawning a new process on the same computer


1.  In Visual Studio, from the **Tools** menu, choose **Launch Under Debugger**.
2.  In the **Launch Under Debugger** dialog box, enter the path to the executable file. You can also enter arguments and a working directory.
3.  Click **Launch.**

Processes that the debugger creates (also known as spawned processes) behave a little differently than processes that the debugger does not create.

Instead of using the standard heap API, processes that the debugger creates use a special debug heap. You can force a spawned process to use the standard heap instead of the debug heap by using the \_NO\_DEBUG\_HEAP environment variable.

Also, because the target application is a child process of the debugger, it inherits the debugger's permissions. This permission might enable the target application to perform certain actions that it could not perform otherwise. For example, the target application might be able to affect protected processes.

## <span id="Attaching_to_a_running_process_on_a_separate_computer"></span><span id="attaching_to_a_running_process_on_a_separate_computer"></span><span id="ATTACHING_TO_A_RUNNING_PROCESS_ON_A_SEPARATE_COMPUTER"></span>Attaching to a running process on a separate computer


Sometimes the debugger and the code being debugged run on separate computers. The computer that runs the debugger is called the *host computer*, and the computer that runs the code being debugged is called the *target computer*. You can configure a target computer from Visual Studio on the host computer. Configuring the target computer is also called *provisioning* the target computer. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909).

After you have provisioned a target computer, you can use Visual Studio on the host computer to attach to a process running on the target computer.

1.  On the host computer, in Visual Studio, from the **Tools** menu, choose **Attach to Process**.
2.  In the **Attach to Process** dialog box, set **Transport** to **Windows User Mode Debugger**, and set **Qualifier** to the name of the target computer.
3.  In the **Available Processes** list, select the process that you want to attach to.
4.  Click **Attach**.

**Note**  
If you are using separate host and target computers, do not install Visual Studio and the WDK on the target computer. Debugging is not supported if Visual Studio and the WDK are installed on the target computer.

 

 

 





