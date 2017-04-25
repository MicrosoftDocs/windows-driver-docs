---
title: Setting Up Kernel-Mode Debugging of a Virtual Machine Manually
description: Debugging Tools for Windows supports kernel debugging of a virtual machine.
ms.assetid: e863e664-8338-4bbe-953b-e000a6843db9
keywords: ["virtual machine debugging", "Virtual PC debugging", "VMware debugging"]
---

# Setting Up Kernel-Mode Debugging of a Virtual Machine Manually


Debugging Tools for Windows supports kernel debugging of a virtual machine. The virtual machine can be located on the same physical computer as the debugger or on a different computer that is connected to the same network. This topic describes how to set up debugging of a virtual machine manually.

As an alternative to setting up debugging of a virtual machine manually, you can do the setup using Microsoft Visual Studio. For more information, see [Setting Up Kernel-Mode Debugging of a Virtual Machine in Visual Studio](setting-up-a-connection-to-a-virtual-machine-in-visual-studio.md).

The computer that runs the debugger is called the *host computer*, and the virtual machine being debugged is called the *target virtual machine*.

## <span id="Setting_Up_the_Target_Virtual_Machine"></span><span id="setting_up_the_target_virtual_machine"></span><span id="SETTING_UP_THE_TARGET_VIRTUAL_MACHINE"></span>Setting Up the Target Virtual Machine


1.  In the virtual machine, in an elevated Command Prompt window, enter the following commands.

    **bcdedit /debug on**

    **bcdedit /dbgsettings serial debugport:***n* **baudrate:115200**

    where *n* is the number of a COM port on the virtual machine.

2.  Reboot the virtual machine.
3.  In the virtual machine, configure the COM port to map to a named pipe. The debugger will connect through this pipe. For more information about how to create this pipe, see your virtual machine's documentation.

## <span id="starting_the_debugger"></span><span id="STARTING_THE_DEBUGGER"></span>Starting the Debugging Session Using WinDbg


On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **COM** tab. Check the **Pipe** box, and check the **Reconnect** box. For **Baud Rate**, enter 115200. For **Resets**, enter 0.

If the debugger is running on the same computer as the virtual machine, enter the following for **Port**.

**\\\\.\\pipe\\***PipeName*.

If the debugger is running on a different computer from the virtual machine, enter the following for **Port**.

**\\\\***VMHost***\\pipe\\***PipeName*

Click **OK**.

You can also start WinDbg at the command line. If the debugger is running on the same physical computer as the virtual machine, enter the following command in a Command Prompt window.

**windbg -k com:pipe,port=\\\\.\\pipe\\***PipeName***,resets=0,reconnect**

If the debugger is running on a different physical computer from the virtual machine, enter the following command in a Command Prompt window.

**windbg -k com:pipe,port=\\\\***VMHost***\\pipe\\***PipeName***,resets=0,reconnect**

## <span id="Starting_the_Debugging_Session_Using_KD"></span><span id="starting_the_debugging_session_using_kd"></span><span id="STARTING_THE_DEBUGGING_SESSION_USING_KD"></span>Starting the Debugging Session Using KD


To debug a virtual machine that is running on the same physical computer as the debugger, enter the following command in a Command Prompt window.

**kd -k com:pipe,port=\\\\.\\pipe\\***PipeName***,resets=0,reconnect**

To debug a virtual machine that is running on a different physical computer from the debugger, enter the following command in a Command Prompt window.

**kd -k com:pipe,port=\\\\***VMHost***\\pipe\\***PipeName***,resets=0,reconnect**

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________VMHost"></span><span id="________vmhost"></span><span id="________VMHOST"></span> *VMHost*  
Specifies the name of the computer that the virtual machine is running on.

<span id="PipeName_______"></span><span id="pipename_______"></span><span id="PIPENAME_______"></span>*PipeName*   
Specifies the name of the pipe that you created on the virtual machine.

<span id="resets_0"></span><span id="RESETS_0"></span>**resets=0**  
Specifies that an unlimited number of reset packets can be sent to the target when the host and target are synchronizing. Use the **resets=0** parameter for Microsoft Virtual PC and other virtual machines whose pipes drop excess bytes. Do not use this parameter for VMware or other virtual machines whose pipes do not drop all excess bytes.

<span id="________reconnect"></span><span id="________RECONNECT"></span> *reconnect*  
Causes the debugger to automatically disconnect and reconnect the pipe if a read/write failure occurs. Additionally, if the debugger does not find the named pipe when the debugger is started, the *reconnect* parameter causes the debugger to wait for a pipe that is named *PipeName* to appear. Use *reconnect* for Virtual PC and other virtual machines that destroy and re-create their pipes during a computer restart. Do not use this parameter for VMware or other virtual machines that preserve their pipes during a computer restart.

For more information about additional command-line options, see [**KD Command-Line Options**](https://msdn.microsoft.com/library/windows/hardware/ff551851) or [**WinDbg Command-Line Options**](https://msdn.microsoft.com/library/windows/hardware/ff561306).

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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


If the target computer has stopped responding, the target computer is still stopped because of an earlier kernel debugging action, or you used the **-b** [command-line option](https://msdn.microsoft.com/library/windows/hardware/ff539174), the debugger breaks into the target computer immediately.

Otherwise, the target computer continues running until the debugger orders it to break.

**Note**  If you restart the virtual machine by using the VMWare facilities (for example, the reset button), exit WinDbg, and then restart WinDbg to continue debugging.
During virtual machine debugging, VMWare often consumes 100% of the CPU.

 

## <span id="related_topics"></span>Related topics


[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Kernel-Mode%20Debugging%20of%20a%20Virtual%20Machine%20Manually%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





