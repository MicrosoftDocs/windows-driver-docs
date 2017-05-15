---
title: Live Kernel-Mode Debugging Using WinDbg
description: There are two ways you can use WinDbg to initiate a live kernel-mode debugging session.
ms.assetid: CC911199-A16D-4B06-A5BE-FA476F916F21
---

# <span id="debugger.performing_kernel-mode_debugging_using_windbg"></span>Live Kernel-Mode Debugging Using WinDbg


There are two ways you can use WinDbg to initiate a live kernel-mode debugging session.

## <span id="WinDbg_Menu"></span><span id="windbg_menu"></span><span id="WINDBG_MENU"></span>WinDbg Menu


When WinDbg is in dormant mode, you can begin a kernel debugging session by choosing **Kernel Debug** from the **File** menu or by pressing CTRL+K. When the **Kernel Debugging** dialog box appears, click the appropriate tab: **NET**, **1394**, **USB**, **COM**, or **Local**. Each tab specifies a different connection method. For more information about the dialog box and its entries, see [File | Kernel Debug](file---kernel-debug.md).

## <span id="Command_Prompt"></span><span id="command_prompt"></span><span id="COMMAND_PROMPT"></span>Command Prompt


In a Command Prompt window, you can initiate a kernel-mode debugging session when you launch WinDbg. Enter one of the following commands:

**windbg \[-y** *SymbolPath***\] -k net:port=***PortNumber***,key=***Key*
**windbg \[-y** *SymbolPath***\] -k 1394:channel=***1394Channel***\[,symlink=***1394Protocol***\]**
**windbg \[-y** *SymbolPath***\] -k usb:targetname=***USBString*
**windbg \[-y** *SymbolPath***\] -k com:port=***ComPort***,baud=***BaudRate*
**windbg \[-y** *SymbolPath***\] -k com:pipe,port=\\\\***VMHost***\\pipe\\***PipeName***\[,resets=0\]\[,reconnect\]**
**windbg \[-y** *SymbolPath***\] -k com:***modem*
**windbg \[-y** *SymbolPath***\] -kl**
**windbg \[-y** *SymbolPath***\] -k**
For more information, see [**WinDbg Command-Line Options**](windbg-command-line-options.md).

## <span id="Environment_Variables"></span><span id="environment_variables"></span><span id="ENVIRONMENT_VARIABLES"></span>Environment Variables


For debugging over a serial (COM port) or 1394 connection, you can use environment variables to specify the connection settings.

Use the following variables to specify a serial connection.

**set \_NT\_DEBUG\_PORT =** *ComPort*
**set \_NT\_DEBUG\_BAUD\_RATE =** *BaudRate*
Use the following variables to specify a 1394 connection.

**set \_NT\_DEBUG\_BUS = 1394**
**set \_NT\_DEBUG\_1394\_CHANNEL =** *1394Channel* ****
**set \_NT\_DEBUG\_1394\_SYMLINK =** *1394Protocol* ****
For more information, see [Kernel-Mode Environment Variables](kernel-mode-environment-variables.md).

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______SymbolPath______"></span><span id="_______symbolpath______"></span><span id="_______SYMBOLPATH______"></span> *SymbolPath*   
A list of directories where symbol files are located. Directories in the list are separated by semicolons. For more information, see [Symbol Path](symbol-path.md).

<span id="_______PortNumber______"></span><span id="_______portnumber______"></span><span id="_______PORTNUMBER______"></span> *PortNumber*   
A port number to use for network debugging. You can choose any number from 49152 through 65535. For more information, see [Setting Up a Network Connection Manually](setting-up-a-network-debugging-connection.md).

<span id="_______Key______"></span><span id="_______key______"></span><span id="_______KEY______"></span> *Key*   
The encryption key to use for network debugging. We recommend that you use an automatically generated key, which is provided by bcdedit when you configure the target computer. For more information, see [Setting Up a Network Connection Manually](setting-up-a-network-debugging-connection.md).

<span id="_______1394Channel______"></span><span id="_______1394channel______"></span><span id="_______1394CHANNEL______"></span> *1394Channel*   
The 1394 channel number. Valid channel numbers are any integer between 0 and 62, inclusive. *1394Channel* must match the number used by the target computer, but does not depend on the physical 1394 port chosen on the adapter. For more information, see [Setting Up a 1394 Connection Manually](setting-up-a-1394-cable-connection.md).

<span id="_______1394Protocol______"></span><span id="_______1394protocol______"></span><span id="_______1394PROTOCOL______"></span> *1394Protocol*   
The connection protocol to be used for the 1394 kernel connection. This can almost always be omitted, because the debugger will automatically choose the correct protocol. If you wish to set this manually, and the target computer is running Windows XP, *1394Protocol* should be set equal to "channel". If the target computer is running Windows Server 2003 or later, *1394Protocol* should be set equal to "instance". If it is omitted, the debugger will default to the protocol appropriate for the current target computer. This can only be specified through the command line or the environment variables, not through the WinDbg graphical interface.

<span id="_______USBString______"></span><span id="_______usbstring______"></span><span id="_______USBSTRING______"></span> *USBString*   
A USB connection string. This must match the string specified with the /targetname boot option. For more information, see [Setting Up a USB 3.0 Connection Manually](setting-up-a-usb-3-0-debug-cable-connection.md) and [Setting Up a USB 2.0 Connection Manually](setting-up-a-usb-2-0-debug-cable-connection.md).

<span id="_______ComPort______"></span><span id="_______comport______"></span><span id="_______COMPORT______"></span> *ComPort*   
The name of the COM port. This can be in the format "com2" or in the format "\\\\.\\com2", but should not simply be a number. For more information, see [Setting Up a Serial Connection Manually](setting-up-a-null-modem-cable-connection.md).

<span id="_______BaudRate______"></span><span id="_______baudrate______"></span><span id="_______BAUDRATE______"></span> *BaudRate*   
The baud rate. This can be 9600, 19200, 38400, 57600, or 115200.

<span id="_______VMHost______"></span><span id="_______vmhost______"></span><span id="_______VMHOST______"></span> *VMHost*   
When debugging a virtual machine, *VMHost* specifies the name of the physical computer on which the virtual machine is running. If the virtual machine is running on the same computer as the kernel debugger itself, use a single period (.) for *VMHost*. For more information, see [Setting Up a Connection to a Virtual Machine](attaching-to-a-virtual-machine--kernel-mode-.md).

<span id="_______PipeName______"></span><span id="_______pipename______"></span><span id="_______PIPENAME______"></span> *PipeName*   
The name of the pipe created by the virtual machine for the debugging connection.

<span id="_______resets_0"></span><span id="_______RESETS_0"></span> **resets=0**  
Specifies that an unlimited number of reset packets can be sent to the target when the host and target are synchronizing. This parameter is only needed when debugging certain kinds of virtual machines.

<span id="_______reconnect"></span><span id="_______RECONNECT"></span> **reconnect**  
Causes the debugger to automatically disconnect and reconnect the pipe if a read/write failure occurs. Additionally, if the named pipe is not found when the debugger is started, the reconnect parameter will cause it to wait for a pipe of this name to appear. This parameter is only needed when debugging certain kinds of virtual machines.

<span id="_______-kl"></span><span id="_______-KL"></span> **-kl**  
Causes the debugger to perform local kernel-mode debugging. For more information, see [Local Kernel-Mode Debugging](performing-local-kernel-debugging.md).

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


The following batch file could be used to set up and start a debugging session over a COM port connection.

``` syntax
set _NT_SYMBOL_PATH=d:\mysymbols
set _NT_DEBUG_PORT=com1
set _NT_DEBUG_BAUD_RATE=115200
set _NT_DEBUG_LOG_FILE_OPEN=d:\debuggers\logfile1.log
windbg -k
```

The following batch file could be used to set up and start a debugging session over a 1394 connection.

``` syntax
set _NT_SYMBOL_PATH=d:\mysymbols
set _NT_DEBUG_BUS=1394
set _NT_DEBUG_1394_CHANNEL=44
set _NT_DEBUG_LOG_FILE_OPEN=d:\debuggers\logfile1.log
windbg -k
```

The following command lines could be used to start WinDbg without any environment variables.

**windbg -y d:\\mysymbols -k com:port=com2,baud=57600**
**windbg -y d:\\mysymbols -k com:port=\\\\.\\com2,baud=115200**
**windbg -y d:\\mysymbols -k 1394:channel=20,symlink=instance**
**windbg -y d:\\mysymbols -k net:port=50000,key=***AutoGeneratedKey*

## <span id="related_topics"></span>Related topics


[**WinDbg Command-Line Options**](windbg-command-line-options.md)

[Kernel-Mode Environment Variables](kernel-mode-environment-variables.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Live%20Kernel-Mode%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





