---
title: Setting Up Kernel-Mode Debugging of a Virtual Machine in Visual Studio
description: You can use Microsoft Visual Studio to set up and perform kernel-mode debugging of a virtual machine.
ms.assetid: E7A289CA-29CE-4C6F-AD08-529E58379715
ms.author: domars
ms.date: 10/08/2018
ms.localizationpriority: medium
---

# Setting Up Kernel-Mode Debugging of a Virtual Machine in Visual Studio

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>

You can use Microsoft Visual Studio to set up and perform kernel-mode debugging of a virtual machine. The virtual machine can be located on the same physical computer as the debugger or on a different computer that is connected to the same network. To use Visual Studio for kernel-mode debugging, you must have the Windows Driver Kit (WDK) integrated with Visual Studio. For information about how to install the integrated environment, see [Windows Driver Development](https://go.microsoft.com/fwlink/p?linkid=301383).

The computer that runs the debugger is called the *host computer*, and the virtual machine that is being debugged is called the *target virtual machine*.

## <span id="Configuring_the_Target_Virtual_Machine"></span><span id="configuring_the_target_virtual_machine"></span><span id="CONFIGURING_THE_TARGET_VIRTUAL_MACHINE"></span>Configuring the Target Virtual Machine


1. In the virtual machine, in an elevated Command Prompt window, enter the following commands.

   **bcdedit /debug on**

   **bcdedit /dbgsettings serial debugport:**<em>n</em> **baudrate:115200**

   where *n* is the number of a COM port on the virtual machine.

2. Reboot the virtual machine.
3. In the virtual machine, configure the COM port to map to a named pipe. The debugger will connect through this pipe. For more information about how to create this pipe, see your virtual machine's documentation.

## <span id="Configuring_the_Host_Computer"></span><span id="configuring_the_host_computer"></span><span id="CONFIGURING_THE_HOST_COMPUTER"></span>Configuring the Host Computer


The host computer can be the same physical computer that is running the virtual machine, or it can be a separate computer.

1. On the host computer, in Visual Studio, on the **Driver** menu, choose **Test &gt; Configure Computer**.
2. Click **Add New Computer**.
3. For **Computer name**, enter the name of the physical computer that is running the target virtual machine.
4. Select **Manually configure debuggers and do not provision**, and click **Next**.
5. For **Connection Type**, select **Serial**.
6. Check **Pipe**, and check **Reconnect**.
7. If the debugger is running on the same computer as the virtual machine, enter the following for **Pipe name**:

   **\\\\.\\pipe\\**<em>PipeName</em>.

   If the debugger is running on a different computer from the virtual machine, enter the following for **Pipe name**:

   **\\\\**<em>VMHost</em>**\\pipe\\**<em>PipeName</em>

   where, *VMHost* is the name of the physical computer that is running the target virtual machine, and *PipeName* is the name of the pipe that you associated with the COM port on the target virtual machine.

8. Click **Next**. Click **Finish**.

## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session


1.  On the host computer, in Visual Studio, on the **Debug** menu, choose **Attach to Process**.
2.  For **Transport**, choose **Windows Kernel Mode Debugger**.
3.  For **Qualifier**, select the name of the physical computer that is running the target virtual machine.
4.  Click **Attach**.

>[!TIP] 
> If you receive the message "Could not start debug session, error 8007005: Access denied",  run Visual Studio as ADMINISTRATOR on the host computer. 

## <span id="generation_2_virtual_machines"></span><span id="GENERATION_2_VIRTUAL_MACHINES"></span>Generation 2 Virtual Machines


By default, COM ports are not presented in generation 2 virtual machines. You can add COM ports through PowerShell or WMI. For the COM ports to be displayed in the Hyper-V Manager console, they must be created with a path.

To enable kernel debugging using a COM port on a generation 2 virtual machine, follow these steps:

1. Disable Secure Boot by entering this PowerShell command:

   **Set-VMFirmware –Vmname** *VmName* **–EnableSecureBoot Off**

   where *VmName* is the name of your virtual machine.

2. Add a COM port to the virtual machine by entering this PowerShell command:

   **Set-VMComPort –VMName** *VmName* **1 \\\\.\\pipe\\**<em>PipeName</em>

   For example, the following command configures the first COM port on virtual machine TestVM to connect to named pipe TestPipe on the local computer.

   **Set-VMComPort –VMName TestVM 1 \\\\.\\pipe\\TestPipe**

3. Restart the VM so that the new settings are in effect.

For more information, see [Generation 2 Virtual Machine Overview](https://go.microsoft.com/fwlink/p/?Linkid=331326).


## <span id="Firewalls"></span>Troubleshooting Firewalls and Network Access Issues

Your debugger (WinDbg or KD) must have access through the firewall. This can even be the case for virtual serial ports that are supported by network adapters.

If you are prompted by Windows to turn off the firewall when the debugger is loaded, select **all three** boxes.

Depending on the specifics of the VM in use, you may need to change the network settings for your virtual machines to bridge them to the Microsoft Kernel Network Debug Adapter. Otherwise, the virtual machines will not have access to the network.

**Windows Firewall**

You can use Control Panel to allow access through the Windows firewall. 

1. Open Control Panel > System and Security, and select Allow an app through Windows Firewall. 
2. In the list of applications, locate *Windows GUI Symbolic Debugger* and *Windows Kernel Debugger*. 
3. Use the check boxes to allow those two applications through the firewall. Click OK to save your settings.
4. Restart your debugging application (WinDbg or KD).


## <span id="related_topics"></span>Related topics


[Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md)
 

 






