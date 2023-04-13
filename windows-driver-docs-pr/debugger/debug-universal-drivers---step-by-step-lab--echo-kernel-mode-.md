---
title: Debug Windows drivers step-by-step lab (echo kernel mode)
description: This lab introduces the WinDbg kernel debugger. Use WinDbg to debug the echo kernel mode sample driver code.
keywords: ["debug lab", "step-by-step", "ECHO"]
ms.date: 03/07/2023
---

# Debug Windows drivers step-by-step lab (echo kernel mode)

This lab introduces the WinDbg kernel debugger. You use WinDbg to debug the echo kernel-mode sample driver code.

## Lab objectives

This lab includes exercises that introduce the debugging tools, teach common debugging commands, illustrate the use of breakpoints, and show how to use the debugging extensions.

In this lab, you use a live kernel debug connection to explore the following actions:

- Use the Windows debugger commands
- Use standard commands (call stacks, variables, threads, IRQL)
- Use advanced driver debugging commands (!commands)
- Use symbols
- Set breakpoints in live debugging
- View call stacks
- Display the Plug and Play device tree
- Work with thread and process context

### User and kernel mode debugging

When working with the Windows debugger, you can do two types of debugging:

*User mode* - Applications and subsystems run on the computer in user mode. Processes that run in user mode do so within their own virtual address spaces. They're restricted from gaining direct access to many parts of the system, including system hardware, memory that isn't allocated for their use, and other portions of the system that might compromise system integrity. Because processes that run in user mode are effectively isolated from the system and other user mode processes, they can't interfere with these resources.

*Kernel mode* - The operating system and privileged programs run in kernel mode. Kernel-mode code has permission to access any part of the system. It isn't restricted like user mode code. It can gain access to any part of any other process running in either user mode or kernel mode. Much of the core OS functionality and many hardware device drivers run in kernel mode.

This exercise covers debug commands that are frequently used during both user mode and kernel-mode debugging. The exercise also covers debug extensions, sometimes called *!commands*, that are used for kernel-mode debugging.

## Lab setup

You need the following hardware to complete the lab:

- A laptop or desktop computer (host) running Windows 10
- A second laptop or desktop computer (target) running Windows 10
- A network hub or router and network cables to connect the two computers
- Access to the internet to download symbol files

You need the following software to complete the lab:

- Visual Studio
- Windows Software Development Kit (SDK) for Windows 10
- Windows Driver Kit (WDK) for Windows 10
- The sample echo driver for Windows 10

The lab has the following sections:

- [Connect to a kernel-mode WinDbg session](#connect-to-a-kernel-mode-windbg-session)
- [Kernel-mode debugging commands and techniques](#kernel-mode-debugging-commands-and-techniques)
- [Download and build the KMDF echo driver](#download-and-build-the-kmdf-echo-driver)
- [Install the echo driver sample on the target system](#install-the-kmdf-echo-driver-sample-on-the-target-system)
- [Use WinDbg to display information about the driver](#use-windbg-to-display-information-about-the-driver)
- [Display Plug and Play device tree information](#display-plug-and-play-device-tree-information)
- [Work with breakpoints and source code](#work-with-breakpoints-and-source-code)
- [View variables and call stacks](#view-variables-and-call-stacks)
- [Display processes and threads](#display-processes-and-threads)
- [IRQL, registers, and ending the WinDbg session](#irql-registers-and-ending-the-windbg-session)
- [Windows debugging resources](#windows-debugging-resources)

## Connect to a kernel-mode WinDbg session

In this section, configure network debugging on the host and target system.

The computers in this lab need to be configured to use an Ethernet network connection for kernel debugging.

This lab uses two computers. Windows debugger runs on the *host* system and the Kernel Mode Driver Framework (KMDF) echo driver runs on the *target* system.

Use a network hub or router and network cables to connect the two computers.

![Diagram shows two computers connected with a double arrow.](images/debuglab-image-targethostdrawing1.png)

To work with kernel-mode applications and use WinDbg, we recommend that you use the KDNET over Ethernet transport. For information about how to use the Ethernet transport protocol, see [Get started with WinDbg (kernel mode)](getting-started-with-windbg--kernel-mode-.md). For more information about setting up the target computer, see [Preparing a computer for manual driver deployment](../develop/preparing-a-computer-for-manual-driver-deployment.md) and [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md).

### Configure kernel–mode debugging by using the Ethernet

To enable kernel-mode debugging on the target system:

1. On the host system, open a Command Prompt window and enter *ipconfig* to determine its IP address.

   ```output
   Windows IP Configuration
   Ethernet adapter Ethernet:
      Connection-specific DNS Suffix  . :
      Link-local IPv6 Address . . . . . : fe80::c8b6:db13:d1e8:b13b%3
      Autoconfiguration IPv4 Address. . : 169.182.1.1
      Subnet Mask . . . . . . . . . . . : 255.255.0.0
      Default Gateway . . . . . . . . . :
   ```

2. Record the IP address of the host system: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3. On the target system, open a Command Prompt window and use the `ping` command to confirm network connectivity between the two systems. 

   ```console
   ping 169.182.1.1
   ```

   Use the actual IP address of the host system you recorded instead of 169.182.1.1 that's shown in the sample output.

   ```output
   Pinging 169.182.1.1 with 32 bytes of data:
   Reply from 169.182.1.1: bytes=32 time=1ms TTL=255
   Reply from 169.182.1.1: bytes=32 time<1ms TTL=255
   Reply from 169.182.1.1: bytes=32 time<1ms TTL=255
   Reply from 169.182.1.1: bytes=32 time<1ms TTL=255

   Ping statistics for 169.182.1.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 0ms, Maximum = 1ms, Average = 0ms
   ```

Enable kernel-mode debugging on the target system by completing the following steps.

> [!IMPORTANT]
> Before you use BCDEdit to change boot information, you might need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test computer.
> Re-enable these security features when testing is complete. Appropriately manage the test computer when the security features are disabled.

1. On the target computer, open a Command Prompt window as Administrator. Enter this command to enable debugging:

    ```console
    bcdedit /set {default} DEBUG YES
    ```

1. Enter this command to enable test signing:

    ```console
    bcdedit /set TESTSIGNING ON 
    ```

1. Enter this command to set the IP address of the host system. Use the IP address of the host system that you recorded earlier, not the one shown.

    ```console
    bcdedit /dbgsettings net hostip:192.168.1.1 port:50000 key:2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
    ```

   > [!WARNING]
   > To increase the security of the connection and decrease the risk of the random client debugger connection requests, use an autogenerated random key. For more information, see [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md).

1. Enter this command to confirm that the values for `dbgsettings` are set properly:

   ```console
   bcdedit /dbgsettings
   ```

   ```output
   key                     2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
   debugtype               NET
   hostip                  169.168.1.1
   port                    50000
   dhcp                    Yes
   The operation completed successfully.
   ```

   > [!NOTE]
   > If you receive a message from the firewall, and you want to use the debugger, select all three of the boxes.
   >
   > ![Screenshot shows the Windows Security Alert dialog box saying that Windows Firewall has blocked some features of this app.](images/debuglab-image-firewall-dialog-box.png)

1. On the host computer, open a Command Prompt window as Administrator. This lab uses the x64 version of *WinDbg.exe* from the Windows Driver Kit (WDK) that was installed as part of the Windows kit installation. Change to the default WinDbg directory, the default location is shown below.

    ```console
    cd C:\Program Files(x86)\Windows Kits\10\Debuggers\x64 
    ```

   This labs assumes that both computers run a 64-bit version of Windows on both the target and host.
   If that isn't the case, the best approach is to run the same *bitness* of tools on the host that the target runs.
   For example, if the target runs 32-bit Windows, run a 32-bit version of the debugger on the host. For more information, see [Choosing the 32-Bit or 64-Bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md).

1. Open WinDbg with remote user debug by using the following command. The values for the key and port match the values you set earlier using BCDEdit on the target computer.

    ```console
    WinDbg –k net:port=50000,key=2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
    ```

1. Restart the target system.

1. In a minute or two, debug output should be displayed on the host system.

   ```output
   Microsoft (R) Windows Debugger Version 10.0.17074.1002 AMD64
   Copyright (c) Microsoft Corporation. All rights reserved.

   Using NET for debugging
   Opened WinSock 2.0
   Waiting to reconnect...
   Connected to target 169.182.1.1 on port 50005 on local IP 169.182.1.2
   You can get the target MAC address by running .kdtargetmac command.
   Connected to Windows 10 16299 x64 target at (Wed Feb 28 17:16:23.051 2018 (UTC - 8:00)), ptr64 TRUE
   Kernel Debugger connection established.  (Initial Breakpoint requested)
   Symbol search path is: srv*
   Executable search path is: 
   Windows 10 Kernel Version 16299 MP (4 procs) Free x64
   Product: WinNt, suite: TerminalServer SingleUserTS
   Built by: 16299.15.amd64fre.rs3_release.170928-1534
   Machine Name:
   Kernel base = 0xfffff800`9540d000 PsLoadedModuleList = 0xfffff800`95774110
   Debug session time: Wed Feb 28 17:16:23.816 2018 (UTC - 8:00)
   System Uptime: 0 days 0:00:20.534
   ```

The Debugger Command window is the primary debugging information window in WinDbg. You can enter debugger commands and view the command output in this window.

The Debugger Command window is split into two panes. Enter commands in the smaller pane, which is the command entry pane at the bottom of the window, and view the command output in the larger pane at the top of the window.

In the command entry pane, use the Up arrow and Down arrow keys to scroll through the command history. When a command appears, you can edit it or press Enter to run the command.

## Kernel-mode debugging commands and techniques

In this section, use debug commands to display information about the target system.

Some debug commands display text using Debugger Markup Language (DML) that you can select to quickly gather more information.

1. On the host system, use Ctrl+Scroll Lock in WinDBg to break into the code running on the target system. It may take some time for the target system to respond.

   ![Main screen in debugger showing Command Window output from a live kernel connection.](images/windbgx-main-menu.png)

2. Enter the following command to enable DML in the Debugger Command window:

   ```dbgcmd
   0: kd> .prefer_dml 1
   DML versions of commands on by default
   ```

3. You can access reference command help using the `.hh` command. Enter the following command to view the command reference help for `.prefer_dml`:

   ```dbgcmd
   0: kd> .hh .prefer_dml
   ```

   The Debugger help file displays help for the `.prefer_dml` command.

   ![Screenshot shows the debugger help application showing help for the .prefer\-dml command.](images/debuglab-image-prefer-dml-help.png)

4. To display detailed version information on the target system, enter the [vertarget (Show Target Computer Version)](vertarget--show-target-computer-version-.md) command in the WinDbg window:

   ```dbgcmd
   0: kd> vertarget
   Windows 10 Kernel Version 9926 MP (4 procs) Free x64
   Product: WinNt, suite: TerminalServer SingleUserTS
   Built by: 9926.0.amd64fre.fbl_awesome1501.150119-1648
   Machine Name: ""
   Kernel base = 0xfffff801`8d283000 PsLoadedModuleList = 0xfffff801`8d58aef0
   Debug session time: Fri Feb 20 10:15:17.807 2015 (UTC - 8:00)
   System Uptime: 0 days 01:31:58.931
   ```

5. To verify that you're working with the correct kernel-mode process, enter the [lm (List Loaded Modules)](lm--list-loaded-modules-.md) command in the WinDbg window to display the loaded modules:

   ```dbgcmd
   0: Kd> lm
   start             end                 module name
   fffff801`09200000 fffff801`0925f000   volmgrx    (no symbols)
   fffff801`09261000 fffff801`092de000   mcupdate_GenuineIntel   (no symbols)
   fffff801`092de000 fffff801`092ec000   werkernel   (export symbols)       werkernel.sys
   fffff801`092ec000 fffff801`0934d000   CLFS       (export symbols)       CLFS.SYS
   fffff801`0934d000 fffff801`0936f000   tm         (export symbols)       tm.sys
   fffff801`0936f000 fffff801`09384000   PSHED      (export symbols)       PSHED.dll
   fffff801`09384000 fffff801`0938e000   BOOTVID    (export symbols)       BOOTVID.dll
   fffff801`0938e000 fffff801`093f7000   spaceport   (no symbols)
   fffff801`09400000 fffff801`094cf000   Wdf01000   (no symbols)
   fffff801`094d9000 fffff801`09561000   CI         (export symbols)       CI.dll
   ...
   ```

   Output that's been omitted is indicated with "…" in this lab.

6. To request detailed information about a specific module, use the `v` (verbose) option:

   ```dbgcmd
   0: Kd> lm v m tcpip
   Browse full module list
   start             end                 module name
   fffff801`09eeb000 fffff801`0a157000   tcpip      (no symbols)           
       Loaded symbol image file: tcpip.sys
       Image path: \SystemRoot\System32\drivers\tcpip.sys
       Image name: tcpip.sys
       Browse all global symbols  functions  data
       Timestamp:        Sun Nov 09 18:59:03 2014 (546029F7)
       CheckSum:         00263DB1
       ImageSize:        0026C000
       Translations:     0000.04b0 0000.04e4 0409.04b0 0409.04e4

   Unable to enumerate user-mode unloaded modules, Win32 error 0n30
   ```

   There's no set symbol path and loaded symbols, so limited information is available in the debugger.

## Download and build the KMDF echo driver

In this section, download and build the KMDF echo driver.

Typically, you would be working with your own driver code when you use WinDbg. To become familiar with WinDbg operation, this lab uses the KMDF Template "Echo" sample driver. The source code is available to help understand the information that's displayed in WinDbg. This sample is also used to illustrate how you can single-step through native kernel-mode code. This technique can be valuable for debugging complex kernel-mode code issues.

To download and build the Echo sample audio driver:

1. Download and extract the KMDF Echo sample from GitHub.

   - View the [echo sample in GitHub](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/echo/kmdf/).

   - [Read](https://github.com/microsoft/Windows-driver-samples/blob/main/general/echo/kmdf/README.md) about the sample.

   - Browse [all Windows driver samples](https://github.com/Microsoft/Windows-driver-samples).

    The KMDF Echo sample is located in the *general* folder.

    ![Screenshot of github windows-driver-samples highlighting the general folder and the download zip button.](images/debuglab-image-github.png)

    1. Download the driver samples in one zip file: [Driver samples](https://github.com/Microsoft/Windows-driver-samples/archive/master.zip)

    1. Download the zip file to your local hard drive.

    1. Select and hold or right-click the zip file and select **Extract All**. Specify a new folder, or browse to an existing one to store the extracted files. For example, you could specify *C:\\DriverSamples\\* as the new folder into which to extract the files.

    1. After the files are extracted, go to the following subfolder: *C:\\DriverSamples\\general\\echo\\kmdf*

2. In Microsoft Visual Studio, select **File** > **Open** > **Project/Solution...** and go to the folder that contains the extracted files, for example, *C:\\DriverSamples\\general\\echo\\kmdf*. Double-click the *kmdfecho* solution file to open it.

   In Visual Studio, locate the Solution Explorer. If this window isn't already open, select **Solution Explorer** from the **View** menu. In Solution Explorer, you can see one solution that has three projects.

   ![Screenshot shows Visual Studio with the device.c file loaded from the kmdfecho project.](images/debuglab-image-echo-visual-studio.png)

3. Set the sample's configuration and platform. In Solution Explorer, select and hold or right-click **Solution 'kmdfecho' (3 projects)**, and select **Configuration Manager**. Make sure that the configuration and platform settings are the same for the three projects. By default, the configuration is set to **Win10 Debug**, and the platform is set to **Win64** for all the projects. If you make any configuration or platform changes for one project, make the same changes for the remaining three projects.

4. Driver samples need to be modified to use values that don't overlap with existing drivers. Refer to [From Sample Code to Production Driver - What to Change in the Samples](../gettingstarted/from-sample-code-to-production-driver.md) on how to create a unique driver sample that will coexist with existing real drivers installed in Windows.

5. Set the runtime library. Open the echo driver property page and locate **C/C++** > **Code Generation**.  Change Runtime Library to Multi-threaded Debug (/MTd). For more information about the build options, see [/MD, /MT, /LD (Use Run-Time Library)](/cpp/build/reference/md-mt-ld-use-run-time-library).

   ![Screenshot shows the echo property page highlighting the runtime library setting.](images/debuglab-image-echoapp-properties.png)

6. In the driver properties, make sure **Driver Signing** > **Sign Mode** is set to **Test Sign**.  

   ![Screenshot shows echo property page highlighting the sign mode setting.](images/debuglab-image-echoapp-driver-signing.png)

7. In Visual Studio, select **Build** > **Build Solution**.

   The build windows should display a message indicating that the build for all three projects succeeded.

> [!TIP]
> If you encounter a build error message, use the build error number to determine a fix. For example, *[MSBuild error MSB8040](/visualstudio/msbuild/errors/msb8040)* describes how to work with spectre mitigated libraries.
>

8. In File Explorer, go to the folder that contains the extracted files for the sample. For example, go to *C:\\DriverSamples\\general\\echo\\kmdf*, if that's the folder you specified earlier. Within that folder, the location of the compiled driver files varies depending on the configuration and platform settings that you selected in the Configuration Manager. If you left the default settings unchanged, then the compiled driver files are saved to a folder named *\\x64\\Debug* for a 64 bit debug build.

   Go to the folder that contains the built files for the Autosync driver: *C:\\DriverSamples\\general\\echo\\kmdf\\driver\\AutoSync\\x64\\Debug*.

   The folder should contain these files:

   | File     | Description                                                                       |
   |----------|-----------------------------------------------------------------------------------|
   | Echo.sys | The driver file.                                                                  |
   | Echo.inf | An information (INF) file that contains information needed to install the driver. |

   Also, the *echoapp.exe* file was built and it should be located here: *C:\\DriverSamples\\general\\echo\\kmdf\\exe\\x64\\Debug*.

   | File        | Description                                                                       |
   |-------------|-----------------------------------------------------------------------------------|
   | EchoApp.exe | A Command Prompt executable test file that communicates with the echo.sys driver. |

9. Locate a USB thumb drive or set up a network share to copy the built driver files and the test **EchoApp** from the host to the target system.

In the next section, copy the code to the target system, and install and test the driver.

## Install the KMDF echo driver sample on the target system

In this section, use the DevCon tool to install the echo sample driver.

The computer where you install the driver is called the *target computer* or the *test computer*. Typically, this computer is separate from the computer on which you develop and build the driver package. The computer where you develop and build the driver is called the *host computer*.

The process of moving the driver package to the target computer and installing the driver is called *deploying* the driver.

Before you deploy a test signed driver, prepare the target computer by enabling test signing. You also need to locate the DevCon tool in your WDK installation and copy that to the target system.

To install the driver on the target system, do the following steps.

On the target system, enable test signed drivers:

1. Open **Windows Settings**.

1. In **Update and Security**, select **Recovery**.

1. Under **Advanced startup**, select **Restart Now**.

1. When the computer restarts, select **Startup options**. In Windows 10, select **Troubleshoot** > **Advanced options** > **Startup Settings** , then select **Restart**.

1. Select *Disable driver signature enforcement* by pressing the F7 key.

1. Restart the target computer.

On the host system, go to the *Tools* folder in your WDK installation and locate the DevCon tool. For example, look in the following folder: *C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\x64\\devcon.exe*.

Create a folder on the target for the built driver package, for example, *C:\\EchoDriver*. Copy *devcon.exe* to the target system. Locate the *.cer* certificate on the host system. It is in the same folder on the host computer in the folder that contains the built driver files. Copy all the files from the built driver described earlier on the host computer and save them to the same folder that you created on the target computer.

On the target computer, select and hold or right-click the certificate file, and select **Install**, then follow the prompts to install the test certificate.

If you need more detailed instructions for setting up the target computer, see [Preparing a computer for manual driver deployment](../develop/preparing-a-computer-for-manual-driver-deployment.md).

The following instructions show you how to install and test the sample driver. Here's the general syntax for the devcon tool that you use to install the driver:

```console
devcon install <INF file> <hardware ID>
```

The INF file required for installing this driver is *echo.inf*. The inf file contains the hardware ID for installing the *echo.sys*. For the echo sample, the hardware ID is *root\\ECHO*.

On the target computer, open a Command Prompt window as Administrator. Go to your driver package folder, and enter the following command:

```console
devcon install echo.inf root\ECHO
```

If you get an error message about *devcon* not being recognized, try adding the path to the *devcon* tool. For example, if you copied it to a folder called *C:\\Tools*, then try using the following command:

```console
c:\tools\devcon install echo.inf root\ECHO
```

A dialog box appears that indicates that the test driver is an unsigned driver. Select **Install this driver anyway** to proceed.

![Screenshot shows a Windows Security warning that Windows can't verify the publisher of this driver software.](images/debuglab-image-install-security-warning.png)

> [!TIP]
> If you have any issues with the installation, check the following file for more information.
*%windir%\inf\setupapi.dev.log*

After successfully installing the sample driver, you're ready to test it.

On the target computer, in a Command Prompt window, enter *devmgmt* to open Device Manager. In Device Manager, on the **View** menu, choose **Devices by type.** In the device tree, locate **Sample WDF Echo Driver** in the **Sample Device** node.

![Screenshot shows the Device Manager tree with the sample wdf echo driver highlighted.](images/debuglab-image-device-manager-echo.png)

Enter *echoapp* to start the test echo app to confirm that the driver is functional.

```dbgcmd
C:\Samples\KMDF_Echo_Sample> echoapp
DevicePath: \\?\root#sample#0005#{cdc35b6e-0be4-4936-bf5f-5537380a7c1a}
Opened device successfully
512 Pattern Bytes Written successfully
512 Pattern Bytes Read successfully
Pattern Verified successfully
30720 Pattern Bytes Written successfully
30720 Pattern Bytes Read successfully
Pattern Verified successfully
```

## Use WinDbg to display information about the driver

In this section, set the symbol path and use kernel debugger commands to display information about the KMDF echo sample driver.

To view information about the driver:

1. On the host system, if you closed the debugger, open it again by using the following command in the administrator Command Prompt window.

   ```dbgcmd
   WinDbg -k net:port=50000,key=2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
   ```

1. Use Ctrl+Break (Scroll Lock) to break into the code running on the target system.

1. To set the symbols path to the Microsoft symbol server in the WinDbg environment, use the `.symfix` command.

   ```dbgcmd
   0: kd> .symfix
   ```

1. To add your local symbol location to use your local symbols, add the path using `.sympath+` and then `.reload /f`.

   ```dbgcmd
   0: kd> .sympath+ C:\DriverSamples\general\echo\kmdf
   0: kd> .reload /f
   ```

   The `.reload` command with the `/f` force option deletes all symbol information for the specified module and reloads the symbols. In some cases, this command also reloads or unloads the module itself.

You must load the proper symbols to use advanced functionality that WinDbg provides. If you don't have symbols properly configured, when you attempt to use functionality that's dependent on symbols, you receive messages indicating that symbols aren't available.

```dbgcmd
0:000> dv
Unable to enumerate locals, HRESULT 0x80004005
Private symbols (symbols.pri) are required for locals.
Type “.hh dbgerr005” for details.
```

There are many approaches that can be used to work with symbols. In many situations, you can configure the computer to access symbols from a symbol server that Microsoft provides when they're needed. This lab uses that approach. If the symbols in your environment are in a different location, modify the steps to use that location. For more information, see [Symbol path for Windows debugger](symbol-path.md).

To perform source debugging, you must build a checked (debug) version of your binaries. The compiler creates symbol files (*.pdb* files). These symbol files show the debugger how the binary instructions correspond to the source lines. The actual source files themselves must also be accessible to the debugger.

The symbol files don't contain the text of the source code. For debugging, it's best if the linker doesn't optimize your code. Source debugging and access to local variables are more difficult, and sometimes nearly impossible, if the code has been optimized. If you're having problems viewing local variables or source lines, set the following build options:

```console
set COMPILE_DEBUG=1
set ENABLE_OPTIMIZER=0
```

1. Enter the following command in the command area of the debugger to display information about the echo driver:

   ```dbgcmd
   0: kd> lm m echo* v
   Browse full module list
   start             end                 module name
   fffff801`4ae80000 fffff801`4ae89000   ECHO       (private pdb symbols)  C:\Samples\KMDF_ECHO_SAMPLE\echo.pdb
       Loaded symbol image file: ECHO.sys
       Image path: \SystemRoot\system32\DRIVERS\ECHO.sys
       Image name: ECHO.sys
   ...  
   ```

   For more information, see [lm](lm--list-loaded-modules-.md).

2. Because this lab set `prefer_dml` earlier, some elements of the output are hot links that you can select. Select the **Browse all global symbols** link in the debug output to display information about items symbols that start with the letter "a".

   ```dbgcmd
   0: kd> x /D Echo!a*
   ```

3. The echo sample doesn’t contain any symbols that start with the letter "a", so type `x ECHO!Echo*` to display information about all of the symbols associated with echo driver that start with "Echo".

   ```dbgcmd
   0: kd> x ECHO!Echo*
   fffff801`0bf95690 ECHO!EchoEvtIoQueueContextDestroy (void *)
   fffff801`0bf95000 ECHO!EchoEvtDeviceSelfManagedIoStart (struct WDFDEVICE__ *)
   fffff801`0bf95ac0 ECHO!EchoEvtTimerFunc (struct WDFTIMER__ *)
   fffff801`0bf9b120 ECHO!EchoEvtDeviceSelfManagedIoSuspend (struct WDFDEVICE__ *)
   ...
   ```

   For more information, see [x (Examine Symbols)](x--examine-symbols-.md).

4. The `!lmi` extension displays detailed information about a module. Enter `!lmi echo`. Your output should be similar to the text shown in this example:

   ```dbgcmd
   0: kd> !lmi echo
   Loaded Module Info: [echo] 
            Module: ECHO
      Base Address: fffff8010bf94000
        Image Name: ECHO.sys
   … 
   ```

5. Use the `!dh` extension to display header information as shown in this example:

   ```dbgcmd
   0: kd> !dh echo

   File Type: EXECUTABLE IMAGE
   FILE HEADER VALUES
        14C machine (i386)
          6 number of sections
   54AD8A42 time date stamp Wed Jan 07 11:34:26 2015
   ...
   ```

6. Enter the following to change the default debug bit mask so that all debug messages from the target system are displayed in the debugger:

   ```dbgcmd
   0: kd> ed nt!Kd_DEFAULT_MASK 0xFFFFFFFF
   ```

   Some drivers display additional information when the mask of 0xFFFFFFFF is used. Set the mask to 0x00000000 if you would like to reduce the amount of information that's displayed.

   ```dbgcmd
   0: kd> ed nt!Kd_DEFAULT_MASK 0x00000000
   ```

   Use the `dd` command to confirm the mask is set to display all of the debugger messages.

   ```dbgcmd
   0: kd> dd nt!kd_DEFAULT_MASK 
   fffff802`bb4057c0  ffffffff 00000000 00000000 00000000
   fffff802`bb4057d0  00000000 00000000 00000000 00000000
   fffff802`bb4057e0  00000001 00000000 00000000 00000000
   fffff802`bb4057f0  00000000 00000000 00000000 00000000
   fffff802`bb405800  00000000 00000000 00000000 00000000
   fffff802`bb405810  00000000 00000000 00000000 00000000
   fffff802`bb405820  00000000 00000000 00000000 00000000
   fffff802`bb405830  00000000 00000000 00000000 00000000
   ```

## Display Plug and Play device tree information

In this section, display information about the echo sample device driver and where it lives in the Plug and Play device tree.

Information about the device driver in the Plug and Play device tree can be useful for troubleshooting. For example, if a device driver isn't resident in the device tree, there might an issue with the installation of the device driver.

For more information about the device node debug extension, see [!devnode](-devnode.md).

1. On the host system, to see all the device nodes in the Plug and Play device tree, enter the `!devnode 0 1` command.

   ```dbgcmd
   0: kd> !devnode 0 1
   Dumping IopRootDeviceNode (= 0xffffe0005a3a8d30)
   DevNode 0xffffe0005a3a8d30 for PDO 0xffffe0005a3a9e50
     InstancePath is "HTREE\ROOT\0"
     State = DeviceNodeStarted (0x308)
     Previous State = DeviceNodeEnumerateCompletion (0x30d)
     DevNode 0xffffe0005a3a3d30 for PDO 0xffffe0005a3a4e50
       InstancePath is "ROOT\volmgr\0000"
       ServiceName is "volmgr"
       State = DeviceNodeStarted (0x308)
       Previous State = DeviceNodeEnumerateCompletion (0x30d)
       DevNode 0xffffe0005a324560 for PDO 0xffffe0005bd95ca0…
   …
   ```

2. Use Ctrl+F to search in the output that's generated to look for the name of the device driver, *echo*.

   ![Screenshot shows the Find dialog box showing the term echo being searched for.](images/debuglab-image-find-dialog.png)

3. The echo device driver should be loaded. Use the `!devnode 0 1 echo` command to display Plug and Play information associated with your echo device driver as shown in this example:

   ```dbgcmd
   0: Kd> !devnode 0 1 echo
   Dumping IopRootDeviceNode (= 0xffffe0007b725d30)
   DevNode 0xffffe0007b71a630 for PDO 0xffffe0007b71a960
     InstancePath is "ROOT\SAMPLE\0000"
     ServiceName is "ECHO"
     State = DeviceNodeStarted (0x308)
     Previous State = DeviceNodeEnumerateCompletion (0x30d)
   …
   ```

4. The output displayed in the previous command includes the PDO associated with the running instance of your driver, in this example, *0xffffe0007b71a960*. Enter the `!devobj <PDO address>` command to display Plug and Play information associated with the echo device driver. Use the PDO address that `!devnode` displays on your computer, not the one shown here.

   ```dbgcmd
   0: kd> !devobj 0xffffe0007b71a960
   Device object (ffffe0007b71a960) is for:
    0000000e \Driver\PnpManager DriverObject ffffe0007b727e60
   Current Irp 00000000 RefCount 0 Type 00000004 Flags 00001040
   Dacl ffffc102c9b36031 DevExt 00000000 DevObjExt ffffe0007b71aab0 DevNode ffffe0007b71a630 
   ExtensionFlags (0x00000800)  DOE_DEFAULT_SD_PRESENT
   Characteristics (0x00000180)  FILE_AUTOGENERATED_DEVICE_NAME, FILE_DEVICE_SECURE_OPEN
   AttachedDevice (Upper) ffffe000801fee20 \Driver\ECHO
   Device queue is not busy.
   ```

5. The output displayed in the `!devnode 0 1` command includes the PDO address associated with the running instance of your driver, in this example it's *0xffffe0007b71a960*. Enter the `!devstack <PDO address>` command to display Plug and Play information associated with the device driver. Use the PDO address that `!devnode` displays on your computer, not the one shown in this example.

   ```dbgcmd
   0: kd> !devstack 0xffffe0007b71a960
     !DevObj           !DrvObj            !DevExt           ObjectName
     ffffe000801fee20  \Driver\ECHO       ffffe0007f72eff0  
   > ffffe0007b71a960  \Driver\PnpManager 00000000  0000000e
   !DevNode ffffe0007b71a630 :
     DeviceInst is "ROOT\SAMPLE\0000"
     ServiceName is "ECHO"
   ```

The output shows that you have a fairly simple device driver stack. The echo driver is a child of the *PnPManager* node. *PnPManager* is a root node.

```console
\Driver\ECHO
\Driver\PnpManager
```

This diagram shows a more complex device node tree.

![Diagram shows a device node tree with about 20 nodes.](images/debuglab-image-device-node-tree.png)

For more information about more complex driver stacks, see [Driver stacks](../gettingstarted/driver-stacks.md) and [Device nodes and device stacks](../gettingstarted/device-nodes-and-device-stacks.md).

## Work with breakpoints and source code

In this section, set breakpoints and single-step through kernel-mode source code.

To be able to step through code and check the values of variables in real time, enable breakpoints and set a path to the source code.

Breakpoints stop code execution at a particular line of code. Step forward in the code from that point to debug that specific section of code.

To set a breakpoint using a debug command, use one of the following `b` commands.

| Command | Description |
|:-------- |:----------- |
| `bp` | Sets a breakpoint that's active until the module that it is in is unloaded. |
| `bu` | Sets a breakpoint that's unresolved when the module is unloaded and re-enables when the module reloads. |
| `bm` | Sets a breakpoint for a symbol. This command uses `bu` or `bp` appropriately and allows wildcards (`*`) to be used to set breakpoints on every symbol that matches, like all methods in a class.

For more information, see [Source code debugging in WinDbg](source-window.md).

1. On the host system, use the WinDbg UI to confirm that **Debug** > **Source Mode** is enabled in the current WinDbg session.

1. Enter the following command to add your local code location to the source path:

   ```dbgcmd
   .srcpath+ C:\DriverSamples\KMDF_Echo_Sample\driver\AutoSync
   ```

1. Enter the following command to add your local symbol location to the symbol path:

   ```dbgcmd
   .sympath+ C:\DriverSamples\KMDF_Echo_Sample\driver\AutoSync
   ```

1. Use the `x` command to examine the symbols associated with the echo driver to determine the function name to use for the breakpoint. You can use a wildcard or Ctrl+F to locate the `DeviceAdd` function name.

   ```dbgcmd
   0: kd> x ECHO!EchoEvt*
   8b4c7490          ECHO!EchoEvtIoQueueContextDestroy (void *)
   8b4c7000          ECHO!EchoEvtDeviceSelfManagedIoStart (struct WDFDEVICE__ *)
   8b4c7820          ECHO!EchoEvtTimerFunc (struct WDFTIMER__ *)
   8b4cb0e0          ECHO!EchoEvtDeviceSelfManagedIoSuspend (struct WDFDEVICE__ *)
   8b4c75d0          ECHO!EchoEvtIoWrite (struct WDFQUEUE__ *, struct WDFREQUEST__ *, unsigned int)
   8b4cb170          ECHO!EchoEvtDeviceAdd (struct WDFDRIVER__ *, struct 
   …
   ```

   The output shows that `DeviceAdd` method for your echo driver is `ECHO!EchoEvtDeviceAdd`.

   Alternatively, review the source code to find the function name for your breakpoint.

1. Set the breakpoint with the `bm` command using the name of the driver, followed by the function name, for example, `AddDevice`, where you want to set the breakpoint, separated by an exclamation mark. This lab uses `AddDevice` to watch the driver being loaded.

   ```dbgcmd
   0: kd> bm ECHO!EchoEvtDeviceAdd
     1: fffff801`0bf9b1c0 @!"ECHO!EchoEvtDeviceAdd"
   ```

   You can use different syntax in conjunction with setting variables like `<module>!<symbol>`, `<class>::<method>`,`'<file.cpp>:<line number>'`, or skip a number of times `<condition> <#>`. For more information, see [Conditional breakpoints in WinDbg and other Windows debuggers](setting-a-conditional-breakpoint.md).

1. List the current breakpoints to confirm that the breakpoint was set by entering the `bl` command:

    ```dbgcmd
    0: kd> bl
    1 e fffff801`0bf9b1c0     0001 (0001) ECHO!EchoEvtDeviceAdd
    ```

    The "e" in the output shown here indicates that the breakpoint number 1 is enabled to fire.

1. Restart code execution on the target system by entering the `g` (go) command.

1. On the target system, in Windows, open **Device Manager** by using the icon or entering **mmc devmgmt.msc**. In Device Manager, expand the *Samples* node.

1. Select and hold or right-click the KMDF echo driver entry and select **Disable** from the menu.

1. Select and hold or right-click the KMDF echo driver entry again and select **Enable** from the menu.

1. On the host system, when the driver is enabled, the [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) debug breakpoint should fire. The execution of the driver code on the target system should halt. When the breakpoint is hit, the execution should be stopped at the start of the *AddDevice* routine. The debug command output displays `Breakpoint 1 hit`.

   ![Screenshot shows windbg showing sample code locals and command windows.](images/debuglab-image-breakpoint-echo-deviceadd.png)

1. Step through the code line by line by entering the `p` command or pressing F10 until you reach the following end of the [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine. The Brace character (`}`) is highlighted as shown.

   ![Screenshot shows the code window showing brace character highlighted at start of adddevice routine.](images/debuglab-image-breakpoint-end-deviceadd.png)

In the next section, examine the state of the variables after the DeviceAdd code has executed.

You can modify existing breakpoints by using the following commands:

| Command | Description |
|:------- |:----------- |
| `bl` | Lists breakpoints. |
| `bc` | Clears a breakpoint from the list. Use `bc *` to clear all breakpoints. |
| `bd` | Disables a breakpoint. Use `bd *` to disable all breakpoints. |
| `be` | Enables a breakpoint. Use `be *` to enable all breakpoints. |

Alternatively, you can also modify breakpoints in the WinDbg UI.

You can also set breakpoints that fire when a memory location is accessed. Use the `ba` (break on access) command, with the following syntax:

```dbgcmd
ba <access> <size> <address> {options}
```

| Option | Description |
|:------ |:----------- |
| `e` | execute: when CPU fetches an instruction from the address |
| `r` | read/write: when CPU reads or writes to the address |
| `w` | write: when the CPU writes to the address |

You can only set four data breakpoints at any given time. It's up to you to make sure that you're aligning your data correctly to trigger the breakpoint. Words must end in addresses divisible by 2, dwords must be divisible by 4, and quad words by 0 or 8.

For example, to set a read/write breakpoint on a specific memory address, you could use a command like this example.

```dbgcmd
ba r 4 0x0003f7bf0
```

You can use the following commands to step through your code with the associated keyboard short cuts shown in parentheses.

- Break in (Ctrl+Break). This command interrupts a system as long as the system is running and is in communication with WinDbg. The sequence in the Kernel Debugger is Ctrl+C.
- Run to cursor (F7 or Ctrl+F10). Place the cursor in a source or disassembly window where you want the execution to break, then press F7. Code execution runs to that point. If the flow of code execution doesn't reach the point indicated by the cursor, WinDbg wouldn't break. This situation can happen if an IF statement isn't executed.
- Run (F5). Run until a breakpoint is encountered or an event like a bug check occurs.
- Step over (F10). This command causes code execution to proceed one statement or one instruction at a time. If a call is encountered, code execution passes over the call without entering the called routine. If the programming language is C or C++ and WinDbg is in source mode, source mode can be turned on or off using **Debug** > **Source Mode**.
- Step in (F11). This command is like step-over, except that the execution of a call does go into the called routine.
- Step out (Shift+F11). This command causes execution to run to and exit from the current routine or current place in the call stack. This command is useful if you've seen enough of the routine.

For more information, see [Source code debugging in WinDbg](source-window.md).

## View variables and call stacks

In this section, display information about variables and call stacks.

This lab assumes that you're stopped at the [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine using the process described earlier. To view the output shown here, repeat the steps described previously, if necessary.

On the host system, to display variables, use the **view** > **local** menu item to display local variables.

![Screenshot shows WinDbg local variables window.](images/debuglab-image-display-variables.png)

To find the location of a global variable address, enter `? <variable name>`.

- Step out (Shift+F11) – This command causes execution to run to and exit from the current routine (current place in the call stack). This is useful if you've seen enough of the routine.

For more information, see [Source Code Debugging in WinDbg (Classic)](source-window.md) in the debugging reference documentation.

## Section 8: Viewing variables and call stacks

*In Section 8, you will display information about variables and call stacks.*

This lab assumes that you are stopped at the [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine using the process described earlier. To view the output show here, repeat the steps described previously, if necessary.

**&lt;- On the host system**

**Display variables**

Use the **view**&gt; **local** menu item to display local variables.

![windbg local variables window.](images/debuglab-image-display-variables.png)

**Global variables**

You can find the location of a global variable address by typing *? &lt;variable name&gt;*.

**Local variables**

You can display the names and values of all local variables for a given frame by typing the **dv** command.
To display the names and values of all local variables for a specific frame, enter the `dv` command:

```dbgcmd
0: kd> dv
         Driver = 0x00001fff`7ff9c838
     DeviceInit = 0xffffd001`51978190
         status = 0n0
```

The call stack is the chain of function calls that have led to the current location of the program counter. The top function on the call stack is the current function, and the next function is the function that called the current function, and so on.

To display the call stack, use the `k*` commands.

| Command | Description |
|:------- |:----------- |
| `kb` | Displays the stack and first three parameters. |
| `kp` | Displays the stacks and the full list of parameters. |
| `kn` | Allows you to see the stack with the frame information next to it. |

1. On the host system, if you want to keep the call stack available, select **view** > **call stack** to view it. Select the columns at the top of the window to toggle the display of additional information.

   ![Screenshot shows the WinDbg display call stacks window.](images/debuglab-image-display-callstacks.png)

2. Use the `kn` command to show the call stack while debugging the sample adapter code in a break state.

   ```dbgcmd
   3: kd> kn
   # Child-SP          RetAddr           Call Site
   00 ffffd001`51978110 fffff801`0942f55b ECHO!EchoEvtDeviceAdd+0x66 [c:\Samples\kmdf echo sample\c++\driver\autosync\driver.c @ 138]
   01 (Inline Function) --------`-------- Wdf01000!FxDriverDeviceAdd::Invoke+0x30 [d:\wbrtm\minkernel\wdf\framework\shared\inc\private\common\fxdrivercallbacks.hpp @ 61]
   02 ffffd001`51978150 fffff801`eed8097d Wdf01000!FxDriver::AddDevice+0xab [d:\wbrtm\minkernel\wdf\framework\shared\core\km\fxdriverkm.cpp @ 72]
   03 ffffd001`51978570 fffff801`ef129423 nt!PpvUtilCallAddDevice+0x35 [d:\9142\minkernel\ntos\io\pnpmgr\verifier.c @ 104]
   04 ffffd001`519785b0 fffff801`ef0c4112 nt!PnpCallAddDevice+0x63 [d:\9142\minkernel\ntos\io\pnpmgr\enum.c @ 7397]
   05 ffffd001`51978630 fffff801`ef0c344f nt!PipCallDriverAddDevice+0x6e2 [d:\9142\minkernel\ntos\io\pnpmgr\enum.c @ 3390]
   ...
   ```

The call stack shows that the kernel (nt) called into Plug and Play code (PnP) that called driver framework code (WDF) that later called the echo driver `DeviceAdd` function.

## Display processes and threads

In this section, display information about the processes and threads running in kernel mode.

### Processes

You can display or set process information by using the [!process](-process.md) debugger extension. Set a breakpoint to examine the process that's used when a sound is played.

1. On the host system, enter the `dv` command to examine the locale variables associated with the `EchoEvtIo` routine:

   ```dbgcmd
   0: kd> dv ECHO!EchoEvtIo*
   ECHO!EchoEvtIoQueueContextDestroy
   ECHO!EchoEvtIoWrite
   ECHO!EchoEvtIoRead         
   ```

2. Clear the previous breakpoints by using `bc *`:

   ```dbgcmd
   0: kd> bc *  
   ```

3. Set a symbol breakpoint on the `EchoEvtIo` routines by using the following command:

   ```dbgcmd
   0: kd> bm ECHO!EchoEvtIo*
     2: aade5490          @!”ECHO!EchoEvtIoQueueContextDestroy”
     3: aade55d0          @!”ECHO!EchoEvtIoWrite”
     4: aade54c0          @!”ECHO!EchoEvtIoRead”
   ```

4. List the breakpoints to confirm that the breakpoint is set properly:

   ```dbgcmd
   0: kd> bl
   1 e aabf0490 [c:\Samples\kmdf echo sample\c++\driver\autosync\queue.c @ 197]    0001 (0001) ECHO!EchoEvtIoQueueContextDestroy
   ...
   ```

5. Enter `g` to restart code execution:

   ```dbgcmd
   0: kd> g
   ```

6. On the target system, run the `EchoApp.exe` driver test program on the target system.

7. On the host system, when the test app runs, the I/O routine in the driver is called. This call causes the breakpoint to fire, and execution of the driver code on the target system halts.

   ```dbgcmd
   Breakpoint 2 hit
   ECHO!EchoEvtIoWrite:
   fffff801`0bf95810 4c89442418      mov     qword ptr [rsp+18h],r8
   ```

8. Use the `!process` command to display the current process that's involved in running *echoapp.exe*:

   ```dbgcmd
   0: kd> !process
   PROCESS ffffe0007e6a7780
       SessionId: 1  Cid: 03c4    Peb: 7ff7cfec4000  ParentCid: 0f34
       DirBase: 1efd1b000  ObjectTable: ffffc001d77978c0  HandleCount:  34.
       Image: echoapp.exe
       VadRoot ffffe000802c79f0 Vads 30 Clone 0 Private 135. Modified 5. Locked 0.
       DeviceMap ffffc001d83c6e80
       Token                             ffffc001cf270050
       ElapsedTime                       00:00:00.052
       UserTime                          00:00:00.000
       KernelTime                        00:00:00.000
       QuotaPoolUsage[PagedPool]         33824
       QuotaPoolUsage[NonPagedPool]      4464
       Working Set Sizes (now,min,max)  (682, 50, 345) (2728KB, 200KB, 1380KB)
       PeakWorkingSetSize                652
       VirtualSize                       16 Mb
       PeakVirtualSize                   16 Mb
       PageFaultCount                    688
       MemoryPriority                    BACKGROUND
       BasePriority                      8
       CommitCharge                      138

           THREAD ffffe00080e32080  Cid 03c4.0ec0  Teb: 00007ff7cfece000 Win32Thread: 0000000000000000 RUNNING on processor 1
   ```

   The output shows that the process is associated with the *echoapp.exe* thread, which was running when your breakpoint on the driver write event was hit. For more information, see [!process](-process.md).

9. Use the `!process 0 0` to display summary information for all processes. In the output, use Ctrl+F to locate the same process address for the process associated with the *echoapp.exe* image. In the example, the process address is `ffffe0007e6a7780`.

   ```dbgcmd
   ...

   PROCESS ffffe0007e6a7780
       SessionId: 1  Cid: 0f68    Peb: 7ff7cfe7a000  ParentCid: 0f34
       DirBase: 1f7fb9000  ObjectTable: ffffc001cec82780  HandleCount:  34.
       Image: echoapp.exe

   ...
   ```

10. Record the process ID associated with *echoapp.exe* to use later in this lab. You can also use Ctrl+C to copy the address to the copy buffer for later use.

    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_(echoapp.exe process address)

11. Enter `g` as required into the debugger to run the code forward until *echoapp.exe* finishes running. It hits the breakpoint in the read and write event many times. When *echoapp.exe* finishes, break in to the debugger, by pressing Ctrl+ScrLk (Ctrl+Break).

12. Use the `!process` command to confirm that you're running a different process. In the output shown here, the process with the Image value of *System* is different from the *Echo* Image value.

    ```dbgcmd
    1: kd> !process
    PROCESS ffffe0007b65d900
        SessionId: none  Cid: 0004    Peb: 00000000  ParentCid: 0000
        DirBase: 001ab000  ObjectTable: ffffc001c9a03000  HandleCount: 786.
        Image: System
        VadRoot ffffe0007ce45930 Vads 14 Clone 0 Private 22. Modified 131605. Locked 64.
        DeviceMap ffffc001c9a0c220
        Token                             ffffc001c9a05530
        ElapsedTime                       21:31:02.516
    ...
    ```

    The output shows that a system process ffffe0007b65d900 was running when you stopped the OS.

13. Use the `!process` command to try to look at the process ID that had been associated with *echoapp.exe* that you recorded earlier. Provide your *echoapp.exe* process address that you recorded earlier, instead of the example process address shown in this example.

    ```dbgcmd
    0: kd> !process ffffe0007e6a7780
    TYPE mismatch for process object at 82a9acc0
    ```

    The process object is no longer available, because the *echoapp.exe* process is no longer running.

### Threads

The commands to view and set threads are similar to the commands for processes. Use the [!thread](-thread.md) command to view threads. Use [.thread](-thread--set-register-context-.md) to set the current threads.

1. On the host system, enter `g` into the debugger to restart code execution on the target system.

2. On the target system, run the EchoApp.exe driver test program.

3. On the host system, the breakpoint is hit and code execution halts.

    ```dbgcmd
    Breakpoint 4 hit
    ECHO!EchoEvtIoRead:
    aade54c0 55              push    ebp
    ```

4. To view the threads that are running, enter [!thread](-thread.md). Information similar to the following example should be displayed:

    ```dbgcmd
    0: kd>  !thread
    THREAD ffffe000809a0880  Cid 0b28.1158  Teb: 00007ff7d00dd000 Win32Thread: 0000000000000000 RUNNING on processor 0
    IRP List:
        ffffe0007bc5be10: (0006,01f0) Flags: 00060a30  Mdl: 00000000
    Not impersonating
    DeviceMap                 ffffc001d83c6e80
    Owning Process            ffffe0008096c900       Image:         echoapp.exe
    ...
    ```

    Note the image name of *echoapp.exe*. That indicates that you're looking at the thread associated with the test app.

5. Use the `!process` command to determine if this thread is the only thread running in the process associated with *echoapp.exe*. The thread number of the running thread in the process is the same thread running that the `!thread` command displayed.

   ```dbgcmd
   0: kd> !process
   PROCESS ffffe0008096c900
       SessionId: 1  Cid: 0b28    Peb: 7ff7d00df000  ParentCid: 0f34
       DirBase: 1fb746000  ObjectTable: ffffc001db6b52c0  HandleCount:  34.
       Image: echoapp.exe
       VadRoot ffffe000800cf920 Vads 30 Clone 0 Private 135. Modified 8. Locked 0.
       DeviceMap ffffc001d83c6e80
       Token                             ffffc001cf5dc050
       ElapsedTime                       00:00:00.048
       UserTime                          00:00:00.000
       KernelTime                        00:00:00.000
       QuotaPoolUsage[PagedPool]         33824
       QuotaPoolUsage[NonPagedPool]      4464
       Working Set Sizes (now,min,max)  (681, 50, 345) (2724KB, 200KB, 1380KB)
       PeakWorkingSetSize                651
       VirtualSize                       16 Mb
       PeakVirtualSize                   16 Mb
       PageFaultCount                    686
       MemoryPriority                    BACKGROUND
       BasePriority                      8
       CommitCharge                      138

           THREAD ffffe000809a0880  Cid 0b28.1158  Teb: 00007ff7d00dd000 Win32Thread: 0000000000000000 RUNNING on processor 0
   ```

6. Use the `!process 0 0` command to locate the process address of two related processes and record those process address here.

   Cmd.exe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   EchoApp.exe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   ```dbgcmd
   0: kd> !process 0 0 

   …

   PROCESS ffffe0007bbde900
       SessionId: 1  Cid: 0f34    Peb: 7ff72dfa7000  ParentCid: 0c64
       DirBase: 19c5fa000  ObjectTable: ffffc001d8c2f300  HandleCount:  31.
       Image: cmd.exe
   …
   PROCESS ffffe0008096c900
       SessionId: 1  Cid: 0b28    Peb: 7ff7d00df000  ParentCid: 0f34
       DirBase: 1fb746000  ObjectTable: ffffc001db6b52c0  HandleCount:  34.
       Image: echoapp.exe
   …
   ```

   You can alternatively use `!process 0 17` to display detailed information about every process. The output from this command can be lengthy. The output can be searched using Ctrl+F.

7. Use the `!process` command to list process information for both processes running your computer. Provide the process address from your `!process 0 0` output, not the address shown in this example.

   This example output is for the *cmd.exe* process ID that was recorded earlier. The image name for this process ID is *cmd.exe*.

   ```dbgcmd
   0: kd>  !process ffffe0007bbde900
   PROCESS ffffe0007bbde900
       SessionId: 1  Cid: 0f34    Peb: 7ff72dfa7000  ParentCid: 0c64
       DirBase: 19c5fa000  ObjectTable: ffffc001d8c2f300  HandleCount:  31.
       Image: cmd.exe
       VadRoot ffffe0007bb8e7b0 Vads 25 Clone 0 Private 117. Modified 20. Locked 0.
       DeviceMap ffffc001d83c6e80
       Token                             ffffc001d8c48050
       ElapsedTime                       21:33:05.840
       UserTime                          00:00:00.000
       KernelTime                        00:00:00.000
       QuotaPoolUsage[PagedPool]         24656
       QuotaPoolUsage[NonPagedPool]      3184
       Working Set Sizes (now,min,max)  (261, 50, 345) (1044KB, 200KB, 1380KB)
       PeakWorkingSetSize                616
       VirtualSize                       2097164 Mb
       PeakVirtualSize                   2097165 Mb
       PageFaultCount                    823
       MemoryPriority                    FOREGROUND
       BasePriority                      8
       CommitCharge                      381

           THREAD ffffe0007cf34880  Cid 0f34.0f1c  Teb: 00007ff72dfae000 Win32Thread: 0000000000000000 WAIT: (UserRequest) UserMode Non-Alertable
               ffffe0008096c900  ProcessObject
           Not impersonating
   ...
   ```

    This example output is for the *echoapp.exe* process ID that was recorded earlier.

   ```dbgcmd
   0: kd>  !process ffffe0008096c900
   PROCESS ffffe0008096c900
       SessionId: 1  Cid: 0b28    Peb: 7ff7d00df000  ParentCid: 0f34
       DirBase: 1fb746000  ObjectTable: ffffc001db6b52c0  HandleCount:  34.
       Image: echoapp.exe
       VadRoot ffffe000800cf920 Vads 30 Clone 0 Private 135. Modified 8. Locked 0.
       DeviceMap ffffc001d83c6e80
       Token                             ffffc001cf5dc050
       ElapsedTime                       00:00:00.048
       UserTime                          00:00:00.000
       KernelTime                        00:00:00.000
       QuotaPoolUsage[PagedPool]         33824
       QuotaPoolUsage[NonPagedPool]      4464
       Working Set Sizes (now,min,max)  (681, 50, 345) (2724KB, 200KB, 1380KB)
       PeakWorkingSetSize                651
       VirtualSize                       16 Mb
       PeakVirtualSize                   16 Mb
       PageFaultCount                    686
       MemoryPriority                    BACKGROUND
       BasePriority                      8
       CommitCharge                      138

           THREAD ffffe000809a0880  Cid 0b28.1158  Teb: 00007ff7d00dd000 Win32Thread: 0000000000000000 RUNNING on processor 0
           IRP List:
               ffffe0007bc5be10: (0006,01f0) Flags: 00060a30  Mdl: 00000000
           Not impersonating
   ...
   ```

8. Record the first thread address associated with the two processes here.

   Cmd.exe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   EchoApp.exe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9. Use the `!Thread` command to display information about the current thread.

   ```dbgcmd
   0: kd>  !Thread
   THREAD ffffe000809a0880  Cid 0b28.1158  Teb: 00007ff7d00dd000 Win32Thread: 0000000000000000 RUNNING on processor 0
   IRP List:
       ffffe0007bc5be10: (0006,01f0) Flags: 00060a30  Mdl: 00000000
   Not impersonating
   DeviceMap                 ffffc001d83c6e80
   Owning Process            ffffe0008096c900       Image:         echoapp.exe
   Attached Process          N/A            Image:         N/A
   ...
   ```

   As expected, the current thread is the thread associated with *echoapp.exe* and it is in a running state.

10. Use the `!Thread` command to display information about the thread associated with *cmd.exe* process. Provide the thread address you recorded earlier.

    ```dbgcmd
    0: kd> !Thread ffffe0007cf34880
    THREAD ffffe0007cf34880  Cid 0f34.0f1c  Teb: 00007ff72dfae000 Win32Thread: 0000000000000000 WAIT: (UserRequest) UserMode Non-Alertable
        ffffe0008096c900  ProcessObject
    Not impersonating
    DeviceMap                 ffffc001d83c6e80
    Owning Process            ffffe0007bbde900       Image:         cmd.exe
    Attached Process          N/A            Image:         N/A
    Wait Start TickCount      4134621        Ticks: 0
    Context Switch Count      4056           IdealProcessor: 0             
    UserTime                  00:00:00.000
    KernelTime                00:00:01.421
    Win32 Start Address 0x00007ff72e9d6e20
    Stack Init ffffd0015551dc90 Current ffffd0015551d760
    Base ffffd0015551e000 Limit ffffd00155518000 Call 0
    Priority 14 BasePriority 8 UnusualBoost 3 ForegroundBoost 2 IoPriority 2 PagePriority 5
    Child-SP          RetAddr           : Args to Child                                                           : Call Site
    ffffd001`5551d7a0 fffff801`eed184fe : fffff801`eef81180 ffffe000`7cf34880 00000000`fffffffe 00000000`fffffffe : nt!KiSwapContext+0x76 [d:\9142\minkernel\ntos\ke\amd64\ctxswap.asm @ 109]
    ffffd001`5551d8e0 fffff801`eed17f79 : ffff03a5`ca56a3c8 000000de`b6a6e990 000000de`b6a6e990 00007ff7`d00df000 : nt!KiSwapThread+0x14e [d:\9142\minkernel\ntos\ke\thredsup.c @ 6347]
    ffffd001`5551d980 fffff801`eecea340 : ffffd001`5551da18 00000000`00000000 00000000`00000000 00000000`00000388 : nt!KiCommitThreadWait+0x129 [d:\9142\minkernel\ntos\ke\waitsup.c @ 619]
    ...
    ```

    This thread is associated with *cmd.exe* and is in a wait state.

11. Provide the thread address of the waiting *CMD.exe* thread to change the context to that waiting thread.

    ```dbgcmd
    0: kd> .Thread ffffe0007cf34880
    Implicit thread is now ffffe000`7cf34880
    ```

12. Use the `k` command to view the call stack associated with the waiting thread.

    ```dbgcmd
    0: kd> k
      *** Stack trace for last set context - .thread/.cxr resets it
    # Child-SP          RetAddr           Call Site
    00 ffffd001`5551d7a0 fffff801`eed184fe nt!KiSwapContext+0x76 [d:\9142\minkernel\ntos\ke\amd64\ctxswap.asm @ 109]
    01 ffffd001`5551d8e0 fffff801`eed17f79 nt!KiSwapThread+0x14e [d:\9142\minkernel\ntos\ke\thredsup.c @ 6347]
    02 ffffd001`5551d980 fffff801`eecea340 nt!KiCommitThreadWait+0x129 [d:\9142\minkernel\ntos\ke\waitsup.c @ 619]
    03 ffffd001`5551da00 fffff801`ef02e642 nt!KeWaitForSingleObject+0x2c0 [d:\9142\minkernel\ntos\ke\wait.c @ 683]
    ...
    ```

    Call stack elements such as `KiCommitThreadWait` indicate that this thread isn't running as is expected.

For more information about threads and processes, see the following references:

- [Threads and processes](threads-and-processes.md)
- [Changing contexts](changing-contexts.md)

## IRQL, registers, and ending the WinDbg session

In this section, display the interrupt request level (IRQL) and the contents of the registers.

### View the saved IRQL

The IRQL is used to manage the priority of interrupt servicing. Each processor has an IRQL setting that threads can raise or lower. Interrupts that occur at or below the processor's IRQL setting are masked and don't interfere with the current operation. Interrupts that occur above the processor's IRQL setting take precedence over the current operation.

On the host system, the [!irql](-irql.md) extension displays the IRQL on the current processor of the target computer before the debugger break occurred. When the target computer breaks into the debugger, the IRQL changes, but the IRQL that was effective just before the debugger break is saved and is displayed by `!irql`.

```dbgcmd
0: kd> !irql
Debugger saved IRQL for processor 0x0 -- 2 (DISPATCH_LEVEL)
```

### View the registers

On the host system, display the contents of the registers for the current thread on the current processor by using the [r (Registers)](r--registers-.md) command.

```dbgcmd
0: kd> r
rax=000000000000c301 rbx=ffffe00173eed880 rcx=0000000000000001
rdx=000000d800000000 rsi=ffffe00173eed8e0 rdi=ffffe00173eed8f0
rip=fffff803bb757020 rsp=ffffd001f01f8988 rbp=ffffe00173f0b620
 r8=000000000000003e  r9=ffffe00167a4a000 r10=000000000000001e
r11=ffffd001f01f88f8 r12=0000000000000000 r13=ffffd001f01efdc0
r14=0000000000000001 r15=0000000000000000
iopl=0         nv up ei pl nz na pe nc
cs=0010  ss=0018  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
nt!DbgBreakPointWithStatus:
fffff803`bb757020 cc              int     3
```

Alternatively, you can display the contents of the registers by selecting **View** > **Registers**. For more information, see [r (Registers)](r--registers-.md).

Viewing the contents of the registers can be helpful when stepping through assembly language code execution and in other scenarios. For more information about assembly language disassembly, see [Annotated x86 Disassembly](annotated-x86-disassembly.md) and [Annotated x64 disassembly](annotated-x64-disassembly.md).

For information about contents of the register, see [x86 architecture](x86-architecture.md) and [x64 architecture](x64-architecture.md).

### End the WinDbg session

If you want to leave the debugger attached, but want to work on the target, clear any breakpoints using `bc *`, so that the target computer won't try to connect to the host computer debugger. Then use the `g` command to let the target computer run again.

To end the debugging session, on the host system, break into the debugger and enter the `qd` (Quit and Detach) command or select **Stop Debugging** from the menu.

```dbgcmd
0: kd> qd
```

For more information, see [End a debugging session in WinDbg](ending-a-debugging-session-in-windbg.md).

## Windows debugging resources

More information is available on Windows debugging. Some of these books use earlier versions of Windows like Windows Vista in their examples, but the concepts discussed are applicable to most versions of Windows.

- Books

  - Advanced Windows Debugging by Mario Hewardt and Daniel Pravat
  - Inside Windows Debugging: A Practical Guide to Debugging and Tracing Strategies in Windows® by Tarik Soulami
  - [Windows Internals by Pavel Yosifovich, Alex Ionescu, Mark Russinovich and David Solomon](/sysinternals/resources/windows-internals)

- Video

  - [Defrag Tools Show WinDbg Episodes 13-29](/shows/defrag-tools/)

- Training vendors

  - [OSR](https://www.osr.com/)

## See also

- [Standard debugging techniques](standard-debugging-techniques.md)
- [Specialized debugging techniques](specialized-debugging-techniques.md)
- [Get started with Windows Debugging](getting-started-with-windows-debugging.md)
