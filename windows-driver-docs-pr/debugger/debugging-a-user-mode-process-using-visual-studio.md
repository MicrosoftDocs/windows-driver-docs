---
title: Debugging a User-Mode Process Using Visual Studio
description: In Microsoft Visual Studio, you can use the Windows User Mode Debugger to attach to a running process or to spawn and attach to a new process. The process can run on the same computer that is running the debugger, or it can run on a separate computer.
ms.assetid: C19D1B6F-B97B-4C1B-AD84-AC974C5F5C8C
---

# <span id="debugger.debugging_a_user-mode_process_using_visual_studio"></span>Debugging a User-Mode Process Using Visual Studio


In Microsoft Visual Studio, you can use the Windows User Mode Debugger to attach to a running process or to spawn and attach to a new process. The process can run on the same computer that is running the debugger, or it can run on a separate computer.

The procedures shown in this topic require that you have the Windows Driver Kit integrated into Visual Studio. To get the integrated environment, first install Visual Studio, and then install the Windows Driver Kit (WDK). For more information, see [Windows Driver Kit (WDK)](http://go.microsoft.com/fwlink/p?linkid=391063).

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20a%20User-Mode%20Process%20Using%20Visual%20Studio%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




