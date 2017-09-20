---
title: Setting Up Kernel-Mode Debugging of a Virtual Machine in Visual Studio
description: You can use Microsoft Visual Studio to set up and perform kernel-mode debugging of a virtual machine.
ms.assetid: E7A289CA-29CE-4C6F-AD08-529E58379715
---

# Setting Up Kernel-Mode Debugging of a Virtual Machine in Visual Studio


You can use Microsoft Visual Studio to set up and perform kernel-mode debugging of a virtual machine. The virtual machine can be located on the same physical computer as the debugger or on a different computer that is connected to the same network. To use Visual Studio for kernel-mode debugging, you must have the Windows Driver Kit (WDK) integrated with Visual Studio. For information about how to install the integrated environment, see [Windows Driver Development](http://go.microsoft.com/fwlink/p?linkid=301383).

As an alternative to using Visual Studio to set up debugging of a virtual machine, you can do the setup manually. For more information, see [Setting Up Kernel-Mode Debugging of a Virtual Machine Manually](attaching-to-a-virtual-machine--kernel-mode-.md).

The computer that runs the debugger is called the *host computer*, and the virtual machine that is being debugged is called the *target virtual machine*.

## <span id="Configuring_the_Target_Virtual_Machine"></span><span id="configuring_the_target_virtual_machine"></span><span id="CONFIGURING_THE_TARGET_VIRTUAL_MACHINE"></span>Configuring the Target Virtual Machine


1.  In the virtual machine, in an elevated Command Prompt window, enter the following commands.

    **bcdedit /debug on**

    **bcdedit /dbgsettings serial debugport:***n* **baudrate:115200**

    where *n* is the number of a COM port on the virtual machine.

2.  Reboot the virtual machine.
3.  In the virtual machine, configure the COM port to map to a named pipe. The debugger will connect through this pipe. For more information about how to create this pipe, see your virtual machine's documentation.

## <span id="Configuring_the_Host_Computer"></span><span id="configuring_the_host_computer"></span><span id="CONFIGURING_THE_HOST_COMPUTER"></span>Configuring the Host Computer


The host computer can be the same physical computer that is running the virtual machine, or it can be a separate computer.

1.  On the host computer, in Visual Studio, on the **Driver** menu, choose **Test &gt; Configure Computer**.
2.  Click **Add New Computer**.
3.  For **Computer name**, enter the name of the physical computer that is running the target virtual machine.
4.  Select **Manually configure debuggers and do not provision**, and click **Next**.
5.  For **Connection Type**, select **Serial**.
6.  Check **Pipe**, and check **Reconnect**.
7.  If the debugger is running on the same computer as the virtual machine, enter the following for **Pipe name**:

    **\\\\.\\pipe\\***PipeName*.

    If the debugger is running on a different computer from the virtual machine, enter the following for **Pipe name**:

    **\\\\***VMHost***\\pipe\\***PipeName*

    where, *VMHost* is the name of the physical computer that is running the target virtual machine, and *PipeName* is the name of the pipe that you associated with the COM port on the target virtual machine.

8.  Click **Next**. Click **Finish**.

## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session


1.  On the host computer, in Visual Studio, on the **Debug** menu, choose **Attach to Process**.
2.  For **Transport**, choose **Windows Kernel Mode Debugger**.
3.  For **Qualifier**, select the name of the physical computer that is running the target virtual machine.
4.  Click **Attach**.

## <span id="generation_2_virtual_machines"></span><span id="GENERATION_2_VIRTUAL_MACHINES"></span>Generation 2 Virtual Machines


By default, COM ports are not presented in generation 2 virtual machines. You can add COM ports through PowerShell or WMI. For the COM ports to be displayed in the Hyper-V Manager console, they must be created with a path.

To enable kernel debugging using a COM port on a generation 2 virtual machine, follow these steps:

1.  Disable Secure Boot by entering this PowerShell command:

    **Set-VMFirmware –Vmname** *VmName* **–EnableSecureBoot Off**

    where *VmName* is the name of your virtual machine.

2.  Add a COM port to the virtual machine by entering this PowerShell command:

    **Set-VMComPort –VMName** *VmName* **1 \\\\.\\pipe\\***PipeName*

    For example, the following command configures the first COM port on virtual machine TestVM to connect to named pipe TestPipe on the local computer.

    **Set-VMComPort –VMName TestVM 1 \\\\.\\pipe\\TestPipe**

For more information, see [Generation 2 Virtual Machine Overview](http://go.microsoft.com/fwlink/p/?Linkid=331326).

## <span id="related_topics"></span>Related topics


[Setting Up Kernel-Mode Debugging in Visual Studio](setting-up-kernel-mode-debugging-in-visual-studio.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Kernel-Mode%20Debugging%20of%20a%20Virtual%20Machine%20in%20Visual%20Studio%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





