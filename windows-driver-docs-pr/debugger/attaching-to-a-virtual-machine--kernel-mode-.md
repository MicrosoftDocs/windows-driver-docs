---
title: Setting Up Kernel-Mode Debugging of a Virtual Machine Manually using a Virtual COM Port
description: Debugging Tools for Windows supports kernel debugging of a virtual machine using a Virtual COM Port.
ms.assetid: e863e664-8338-4bbe-953b-e000a6843db9
keywords: ["virtual machine debugging", "Virtual PC debugging", "VMware debugging"]
ms.author: domars
ms.date: 05/30/2018
ms.localizationpriority: medium
---

# Setting Up Kernel-Mode Debugging of a Virtual Machine Manually using a Virtual COM Port

Debugging Tools for Windows supports kernel debugging of a virtual machine. The virtual machine can be located on the same physical computer as the debugger or on a different computer that is connected to the same network. This topic describes how to set up debugging of a virtual machine manually using a virtual COM Port via KDCOM.

Using KDNET virtual networking is a faster option and is recommended. For more information, see [Setting Up Network Debugging of a Virtual Machine with KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md).


## <span id="Setting_Up_the_Target_Virtual_Machine"></span><span id="setting_up_the_target_virtual_machine"></span><span id="SETTING_UP_THE_TARGET_VIRTUAL_MACHINE"></span>Setting Up the Target Virtual Machine

The computer that runs the debugger is called the *host computer*, and the virtual machine being debugged is called the *target virtual machine*.

> [!IMPORTANT]
> Before using BCDEdit to change boot information you may need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC.
> Re-enable these security features when testing is complete and appropriately manage the test PC, when the security features are disabled.

1. In the virtual machine, in an elevated Command Prompt window, enter the following commands.

   **bcdedit /debug on**

   **bcdedit /dbgsettings serial debugport:**<em>n</em> **baudrate:115200**

   where *n* is the number of a COM port on the virtual machine.

2. In the virtual machine, configure the COM port to map to a named pipe. The debugger will connect through this pipe. For more information about how to create this pipe, see your virtual machine's documentation.

3. Once the debugger is attached and running, reboot the target machine.


## <span id="starting_the_debugger"></span><span id="STARTING_THE_DEBUGGER"></span>Starting the Debugging Session Using WinDbg

On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **COM** tab. Check the **Pipe** box, and check the **Reconnect** box. For **Baud Rate**, enter 115200. For **Resets**, enter 0.

If the debugger is running on the same computer as the virtual machine, enter the following for **Port**.

**\\\\.\\pipe\\**<em>PipeName</em>.

If the debugger is running on a different computer from the virtual machine, enter the following for **Port**.

**\\\\**<em>VMHost</em>**\\pipe\\**<em>PipeName</em>

Click **OK**.

You can also start WinDbg at the command line. If the debugger is running on the same physical computer as the virtual machine, enter the following command in a Command Prompt window.

**windbg -k com:pipe,port=\\\\.\\pipe\\**<em>PipeName</em>**,resets=0,reconnect**

If the debugger is running on a different physical computer from the virtual machine, enter the following command in a Command Prompt window.

**windbg -k com:pipe,port=\\\\**<em>VMHost</em>**\\pipe\\**<em>PipeName</em>**,resets=0,reconnect**

## <span id="Starting_the_Debugging_Session_Using_KD"></span><span id="starting_the_debugging_session_using_kd"></span><span id="STARTING_THE_DEBUGGING_SESSION_USING_KD"></span>Starting the Debugging Session Using KD


To debug a virtual machine that is running on the same physical computer as the debugger, enter the following command in a Command Prompt window.

**kd -k com:pipe,port=\\\\.\\pipe\\**<em>PipeName</em>**,resets=0,reconnect**

To debug a virtual machine that is running on a different physical computer from the debugger, enter the following command in a Command Prompt window.

**kd -k com:pipe,port=\\\\**<em>VMHost</em>**\\pipe\\**<em>PipeName</em>**,resets=0,reconnect**

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________VMHost"></span><span id="________vmhost"></span><span id="________VMHOST"></span> *VMHost*  
Specifies the name of the computer that the virtual machine is running on.

<span id="PipeName_______"></span><span id="pipename_______"></span><span id="PIPENAME_______"></span>*PipeName*   
Specifies the name of the pipe that you created on the virtual machine.

<span id="resets_0"></span><span id="RESETS_0"></span>**resets=0**  
Specifies that an unlimited number of reset packets can be sent to the target when the host and target are synchronizing. Use the **resets=0** parameter for Microsoft Virtual PC and other virtual machines whose pipes drop excess bytes. Do not use this parameter for VMware or other virtual machines whose pipes do not drop all excess bytes.

<span id="________reconnect"></span><span id="________RECONNECT"></span> *reconnect*  
Causes the debugger to automatically disconnect and reconnect the pipe if a read/write failure occurs. Additionally, if the debugger does not find the named pipe when the debugger is started, the *reconnect* parameter causes the debugger to wait for a pipe that is named *PipeName* to appear. Use *reconnect* for Virtual PC and other virtual machines that destroy and re-create their pipes during a computer restart. Do not use this parameter for VMware or other virtual machines that preserve their pipes during a computer restart.

For more information about additional command-line options, see [**KD Command-Line Options**](kd-command-line-options.md) or [**WinDbg Command-Line Options**](windbg-command-line-options.md).

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


3. Once the debugger is attached and running, stop and cold start the VM to activate the COM ports in the VM.　The emulated UARTS aren’t available for debugging unless at least one is actually configured with a pipe name and they cannot be hot-added.

4. Re-enable secure boot, once you are done updating the configuration changes.

For more information about Generation 2 VMs, see [Generation 2 Virtual Machine Overview](https://go.microsoft.com/fwlink/p/?Linkid=331326).


## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


If the target computer has stopped responding, the target computer is still stopped because of an earlier kernel debugging action, or you used the **-b** [command-line option](command-line-options.md), the debugger breaks into the target computer immediately.

Otherwise, the target computer continues running until the debugger orders it to break.


## <span id="Firewalls"></span>Troubleshooting Firewalls and Network Access Issues

Your debugger (WinDbg or KD) must have access through the firewall. This can even be the case for virtual serial ports that are supported by network adapters.

If you are prompted by Windows to turn off the firewall when the debugger is loaded, select all three boxes.

Depending on the specifics of the VM in use, you may need to change the network settings for your virtual machines to bridge them to the Microsoft Kernel Network Debug Adapter. Otherwise, the virtual machines will not have access to the network.

**Windows Firewall**

You can use Control Panel to allow access through the Windows firewall. Open Control Panel > System and Security, and select Allow an app through Windows Firewall. In the list of applications, locate *Windows GUI Symbolic Debugger* and *Windows Kernel Debugger*. Use the check boxes to allow those two applications through the firewall. Restart your debugging application (WinDbg or KD).


## <span id="Third_Party_VMs"></span>Third Party VMs

**VMWare**  
If you restart the virtual machine by using the VMWare facilities (for example, the reset button), exit WinDbg, and then restart WinDbg to continue debugging. During virtual machine debugging, VMWare often consumes 100% of the CPU.

 

## <span id="related_topics"></span>Related topics

[Setting Up Network Debugging of a Virtual Machine with KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md)

[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

[Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md)
 






