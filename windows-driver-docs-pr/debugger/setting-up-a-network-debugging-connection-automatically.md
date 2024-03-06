---
title: Set Up KDNET Network Kernel Debugging Automatically
description: Learn how to use KDNET to configure network kernel debugging automatically for the Windows debugging tools.
keywords: ["Network debugging", "Ethernet debugging", "WinDbg", "KDNET"]
ms.date: 03/08/2023
---

# Set up KDNET network kernel debugging automatically

[Debugging Tools for Windows](debugger-download-tools.md), supports kernel debugging over a network. This article describes how to set up network debugging automatically by using the *kdnet.exe* setup tool.

The computer that runs the debugger is called the host computer, and the computer being debugged is called the target computer. The host computer must be running **Windows 7** or later, and the target computer must be running **Windows 8** or later.

## Determine the IP address of the host computer

1. Confirm that the target and host PCs are connected to a network hub or switch using an appropriate network cable.

2. On the host computer, open a command prompt and enter `IPConfig` to display the IP configuration.

3. In the command output, locate the IPv4 address of the Ethernet adapter.

```console
...

Ethernet adapter Ethernet:
...

IPv4 Address. . . . . . . . . . . : <YourHostIPAddress>
...

```

4. Make a note of the IPv4 address of the network adapter that you intend to use for debugging.

## Set up the host and target computers

Use the kdnet.exe utility to automatically configure the debugger settings on the target PC by following these steps.

1. Confirm that the Windows Debugging Tools are installed on the host system. For information on downloading and installing the debugger tools, see [Debugging Tools for Windows](debugger-download-tools.md). 

2. Locate the *kdnet.exe* and *VerifiedNICList.xml* files. By default, the files are located in the following location:

   ```console
   C:\Program Files (x86)\Windows Kits\10\Debuggers\x64
   ```

   These directions assume that both PCs are running a 64-bit version of Windows on both the target and host.
   If that's not the case, the best approach is to run the same "bitness" of tools on the host that the target is running.
   For example, if the target is running 32-bit Windows, run a 32 version of the debugger on the host.
   For more information, see [Choosing the 32-bit or 64-bit Debugging Tools](choosing-a-32-bit-or-64-bit-debugger-package.md).
   
3. On the host computer, copy the two files to a network share or thumb drive so that they're available on the target computer.

4. On the target computer, create a **C:\KDNET** directory and copy the *kdnet.exe* and *VerifiedNICList.xml* files to that directory.

   > [!IMPORTANT]
   > Before using kdnet.exe to change boot information, you may need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC.
   > Re-enable these security features when testing is complete and appropriately manage the test PC when the security features are disabled.

5. On the target computer, open a command prompt as an administrator. Enter this command to verify that the target computer has a supported network adapter:

   ```console
   C:\KDNET>kdnet.exe
   Network debugging is supported on the following NICs:
   busparams=1.0.0, Broadcom NetXtreme Gigabit Ethernet, Plugged in.  
   This Microsoft hypervisor supports using KDNET in guest VMs.
   ```

6. When the output from kdnet.exe indicates that the network adapter on the target is supported, you can proceed.

7. Enter the following command to set the IP address of the host system and generate a unique connection key. Use the IP address or the name of the host system. Pick a unique port address for each target/host pair that you work with, within the recommended range of 50000-50039.

   ```console
   C:\KDNET>kdnet.exe <HostComputerIPAddress> <YourDebugPort> 
   
   Enabling network debugging on Intel(R) 82577LM Gigabit Network Connection.
   Key=2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
   ```

8. Copy the returned key into a *notepad .txt* file.

## Connect WinDbg to the target for kernel debugging

On the host computer, open WinDbg. On the **File** menu, select **Kernel Debug**. In the Kernel Debugging dialog, open the **Net** tab. Paste in your port number and key saved in the notepad .txt file earlier. Select **OK**.

You can also start a WinDbg session by opening a command prompt and entering the following command. \<YourPort> is the port you selected previously, and \<YourKey> is the key that was returned by kdnet.exe previously. Paste the key that you saved to the notepad .txt file earlier.

   ```console
  windbg.exe -k -d net:port=<YourDebugPort>,key=<YourKey> 
   ```

The optional `-d` parameter shown in the example, enables early break-in. For more information, see [WinDbg command-line options](windbg-command-line-options.md).

If you're prompted to allow WinDbg to access the port through the firewall, allow WinDbg to access the port for **all three** of the different network types.

:::image type="content" source="images/debuglab-image-firewall-dialog-box.png" alt-text="Screenshot of Windows Security Alert with selections to allow access to all three network types.":::



At this point, the debugger waits for the target to reconnect. Text displays in the debugger command window. That text will be similar to the following:

   ```console
   Microsoft (R) Windows Debugger Version 1.0.1908.30002 AMD64
   Copyright (c) Microsoft Corporation. All rights reserved.

   Using NET for debugging
   Opened WinSock 2.0
   Waiting to reconnect...
   ```

## Restart the target PC

Once the debugger is at the "Waiting to reconnect..." stage, reboot the target computer. One way to restart the PC is to use this command from an administrator's command prompt.

   ```console
   shutdown -r -t 0 
   ```

After the target PC restarts, the debugger should connect automatically.

## Troubleshooting tips

**Debugging applications must be allowed through a firewall**

On the host side, where the debugger is running, all types of networking must be enabled to allow the debugger to communicate with the target through the firewall.

Use the Control Panel to allow access through the firewall.

1. Open **Control Panel > System and Security** and select **Allow an app through Windows Firewall**.

   - (WinDbg) In the list of applications, locate *WinDbg engine process (TCP) (all)*.

   - (WinDbg (Classic)) In the list of applications, locate *Windows GUI Symbolic Debugger* and *Windows Kernel Debugger*.

3. Use the checkboxes to allow those two applications through **all three** of the different network types.

4. Scroll down and select **OK** to save the firewall changes. Restart the debugger.

    :::image type="content" source="images/firewall-control-pannel-windbg-gui-config.png" alt-text="Screenshot of Control Panel firewall configuration displaying Windows GUI Symbolic Debugger and Windows Kernel Debugger applications with all three network types enabled.":::

**Use ping to test connectivity**

If the debugger times out and doesn't connect, use the ping command on the target PC to verify connectivity.

```console
   C:\>Ping <HostComputerIPAddress>
```

**Choosing a port for network debugging**

If the debugger times out and doesn't connect, it might be because the default port number of 50000 is already in use or is blocked.

You can choose any port number from 49152 through 65535. The recommended range is between 50000 and 50039. The port that you choose is opened for exclusive access by the debugger running on the host computer.

The range of port numbers that can be used for network debugging might be limited by your company's network policy. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrators.

**Supported network adapters**

If "Network debugging is not supported on any of the NICs in this machine" is displayed when you run kdnet.exe, the network adapter isn't supported.

The host computer can use any network adapter, but the target computer must use a network adapter that's supported by Debugging Tools for Windows. For a list of supported network adapters, see [Supported Ethernet NICs for network kernel debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md) and [Supported Ethernet NICs for network kernel debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md).

## Enable other debugging types

Beginning with Windows 10 October 2020 Update (20H2), the following options are supported to enable four types of debugging:

- *b* - enables bootmgr debugging. See [BCDEdit /bootdebug](../devtest/bcdedit--bootdebug.md).

- *w* - enables winload debugging. See [BCDEdit /bootdebug](../devtest/bcdedit--bootdebug.md).

- *h* - enables hypervisor debugging. See [BCDEdit /hypervisorsettings](../devtest/bcdedit--hypervisorsettings.md).

- *k* - enables kernel debugging. See [Getting started with WinDbg (kernel-mode)](getting-started-with-windbg--kernel-mode-.md).

Any combination of debug types can be specified.

If no debug types are specified, then kernel debugging is enabled.

If both hypervisor and kernel debug are enabled, the hypervisor port is set to `<YourDebugPort>` + 1.

### Example usage

Use the - bkw option to enable bootmgr, kernel and winload debugging.

```console
C:\>kdnet.exe <HostComputerIPAddress> <YourDebugPort> -bkw

Enabling network debugging on Intel(R) 82577LM Gigabit Network Connection.
Key=2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
```

### Summary of debugging type options

| KNDET Option | Description                  | Equivalent set command           |
|--------------|------------------------------|----------------------------------|
| *b*          | enables bootmgr debugging    | bcdedit /bootdebug {bootmgr} on  |
| *h*          | enables hypervisor debugging | bcdedit /set hypervisordebug on  |
| *k*          | enables kernel debugging     | bcdedit /debug on                |
| *w*          | enables winload debugging    | bcdedit /bootdebug on            |

## Specify bus parameters

If kdnet isn't able to automatically determine the bus parameters for your transport, specify them on the command line with the `/busparams` option using this syntax.

`kdnet.exe /busparams [b.d.f] [host] [port] [-[b][h][k][w]]`

`b.d.f` specifies the bus parameters of the device to configure.

Use Device Manager on the target computer to determine the PCI bus, device, and function numbers for the adapter you want to use for debugging. For bus parameters, enter *b*.*d*.*f* where *b*, *d*, and *f* are the bus number, device number, and function number of the adapter. These values are displayed in Device Manager under *Location* on the *General* tab.

For example:

```console
C:\>kdnet.exe /busparams 0.29.7 <HostComputerIPAddress> <YourDebugPort> -bkw
```

## See also

- [Supported Ethernet NICs for network kernel debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)

- [Supported Ethernet NICs for network kernel debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

- [Setting up KDNET network kernel debugging manually](setting-up-a-network-debugging-connection.md)

- [Getting started with WinDbg (kernel-mode)](getting-started-with-windbg--kernel-mode-.md)

- [Debug universal drivers - step by step lab (echo kernel-mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)
