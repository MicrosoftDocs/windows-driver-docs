---
title: Setting Up KDNET Network Kernel Debugging Automatically
description: Use KDNET to configure network kernel debugging automatically for the Windows debuggging tools.
ms.assetid: B4A79B2E-D4B1-42CA-9121-DEC923C76927
keywords: ["Network debugging", "Ethernet debugging", "WinDbg", "KDNET"]
ms.author: domars
ms.date: 06/14/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up KDNET Network Kernel Debugging Automatically

Debugging Tools for Windows supports kernel debugging over an Ethernet network. This topic describes how to set up Ethernet debugging automatically using KDNET.

For information on setting up a conection manually, see [Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md).

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. The host computer must be running Windows 7 or later, and the target computer must be running Windows 8 or later.

Debugging over a network has the following advantages compared to debugging over other types of connectivity.

-   The host and target computers can be anywhere on the local network.
-   It is easy to debug many target computers from one host computer.
-   Given any two computers, it is likely that they will both have Ethernet adapters. It is less likely that they will both have serial ports or both have 1394 ports.

## <span id="Supported_Network_Adapters"></span><span id="supported_network_adapters"></span><span id="SUPPORTED_NETWORK_ADAPTERS"></span>Supported Network Adapters

The host computer can use any network adapter, but the target computer must use a network adapter that is supported by Debugging Tools for Windows. For a list of supported network adapters, see [Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md) and [Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md).

## <span id="Determining_the_IP_Address_of_the_Host_Computer"></span><span id="determining_the_ip_address_of_the_host_computer"></span><span id="DETERMINING_THE_IP_ADDRESS_OF_THE_HOST_COMPUTER"></span>Determining the IP Address of the Host Computer


Use one of the following procedures to determine the IP address of the host computer.

-   On the host computer, open a Command Prompt window and enter the following command:

    ```
    ipconfig
    ```
    Make a note of the IPv4 address of the network adapter that you intend to use for debugging.

-   On the target computer, open a Command Prompt window and enter the following command, where *HostName* is the name of the host computer:

    ```
    ping -4 HostName
    ```


## <span id="Choosing_a_Port_for_Network_Debugging"></span><span id="choosing_a_port_for_network_debugging"></span><span id="CHOOSING_A_PORT_FOR_NETWORK_DEBUGGING"></span>Choosing a Port for Network Debugging

Choose a port number that will be used for debugging on both the host and target computers. You can choose any number from 49152 through 65535. The port that you choose will be opened for exclusive access by the debugger running on the host computer. Take care to choose a port number that is not used by any other applications that run on the host computer.

**Note**  The range of port numbers that can be used for network debugging might be limited by your company's network policy. There is no way to tell from the host computer what the limitations are. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrators.
 
If you connect several target computers to a single host computer, each connection must have a unique port number. For example, if you connect 100 target computers to a single host computer, you can assign port 50000 to the first connection, port 50001 to the second connection, port 50002 to the third connection, and so on.

**Note**  A different host computer could use the same range of ports (50000 through 50099) to connect to another 100 target computers.
 

## <span id="Setting_Up_the_Target_Computer"></span><span id="setting_up_the_target_computer"></span><span id="SETTING_UP_THE_TARGET_COMPUTER"></span>Setting Up the Target Computer

Use the KDNET.exe utility to automatically configure the  debugger settings on the target PC,  by following these steps.


1.  Confirm that the target PC is connected to a network hub or switch using an appropriate network cable. 


2. Locate the WDK *KDNET.exe* and *VerifiedNICList.xml* files. By default they are located here.

```
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64
```

> [!NOTE]
> These directions assumes that both PCs are running a 64 bit version of Windows on both the target and host. 
> If that is not the case, the best approach is to run the same "bitness" of tools on the host that the target is running. 
For example if the target is running 32 bit Windows, run a 32 version of the debugger on the host. 
> For more information, see [Choosing the 32-Bit or 64-Bit Debugging Tools](choosing-a-32-bit-or-64-bit-debugger-package.md).
> 

3. Copy the two files to a network share or thumb drive, so that they will be available on the target computer.


4. On the target computer, open a Command Prompt window as Administrator. Enter this command to verify that the target computer has a supported network adapter.

```
C:\KDNET>KDNet

Network debugging is supported on the following NICs:
busparams=0.25.0, Intel(R) 82579LM Gigabit Network Connection, KDNET is running on this NIC.kdnet.exe
```

5. Type this command to set the IP address of the host system and generated a unique connection key. Use the IP address or the name of the host system. Pick a unique port address for each target/host pair that you work with, with in the range 50000-50039.

```
C:\>KDNet <HostComputerIPAddress> <YourDebugPort> 

NtQuerySystemInformation cannot query SystemKernelDebuggingAllowed on this OS.
Enabling network debugging on Intel(R) 82577LM Gigabit Network Connection.
Key=2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
```

6. Record the key returned, or copy it into a notepad .txt file.


7. To connect to the target PC use the following, where <YourPort> is the port you selected above between 50000-50039, and <YourKey> is the key that was returned by KDNet above.

```
C:\Debuggers\windbg -k net:port=<YourDebugPort>,key=<YourKey> 
```

8. Restart the target PC. 

9. If the debugger does not connect use the ping command to verify connectivity and then refer to the troubleshooting steps below. 

```
C:\>Ping <HostComputerIPAddress> 
```


**Note**  If you intend to install the Hyper-V role on the target computer, see [Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md).
 

## <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

Confirm that the network adapter of the host computer is connected to a network hub or switch using an appropriate network cable. 

On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **Net** tab. Enter your port number and key. Click **OK**.

You can also start a session with WinDbg by opening a Command Prompt window and entering the following command, where *YourDebugPort* is your port number and *MyKey* is the key that was automatically generated when you set up the target computer:

```
windbg -k net:port=YourDebugPort,key=MyKey
```

If you are prompted about allowing WinDbg to access the port through the firewall, allow WinDbg to access the port for **all three** of the different network types.

Once the debugger is connected, reboot the target computer.


## <span id="Allowing_the_debugger_through_the_firewall"></span><span id="allowing_the_debugger_through_the_firewall"></span><span id="ALLOWING_THE_DEBUGGER_THROUGH_THE_FIREWALL"></span>Allowing the debugger through the firewall

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. Client versions of Windows display the prompt, but Server versions of Windows do not display the prompt. You should respond to the prompt by checking the boxes for all three network types: domain, private, and public. If you do not get the prompt, or if you did not check the boxes when the prompt was available, you must use Control Panel to allow access through the firewall. Open **Control Panel &gt; System and Security**, and click **Allow an app through Windows Firewall**. In the list of applications, locate Windows GUI Symbolic Debugger and Windows Kernel Debugger. Use the check boxes to allow those two applications through the firewall. Restart your debugging application (WinDbg or KD).

## <span id="How_the_Debugger_Obtains_an_IP_Address_for_the_Target_Computer"></span><span id="how_the_debugger_obtains_an_ip_address_for_the_target_computer"></span><span id="HOW_THE_DEBUGGER_OBTAINS_AN_IP_ADDRESS_FOR_THE_TARGET_COMPUTER"></span>How the Debugger Obtains an IP Address for the Target Computer


The kernel debugging driver on the target computer attempts to use Dynamic Host Configuration Protocol (DHCP) to get a routable IP address for the network adapter that is being used for debugging. If the driver obtains a DHCP-assigned address, then the target computer can be debugged by host computers located anywhere on the network. If the driver fails to obtain a DHCP-assigned address, it uses Automatic Private IP Addressing (APIPA) to obtain a local link IP address. Local link IP addresses are not routable, so a host and target cannot use a local link IP address to communicate through a router. In that case, network debugging will work if you plug the host and target computers into the same network hub or switch.


## <span id="troubleshooting_tips_for_debugging_over_a_network_cable"></span><span id="TROUBLESHOOTING_TIPS_FOR_DEBUGGING_OVER_A_NETWORK_CABLE"></span>Troubleshooting Tips for Debugging over a Network Cable


### <span id="Debugging_application_must_be_allowed_through_firewall"></span><span id="debugging_application_must_be_allowed_through_firewall"></span><span id="DEBUGGING_APPLICATION_MUST_BE_ALLOWED_THROUGH_FIREWALL"></span>Debugging application must be allowed through firewall

Your debugger (WinDbg or KD) must have access through the firewall. You can use Control Panel to allow access through the firewall. Open **Control Panel &gt; System and Security**, and click **Allow an app through Windows Firewall**. In the list of applications, locate Windows GUI Symbolic Debugger and Windows Kernel Debugger. Use the check boxes to allow those two applications through the firewall. Restart your debugging application (WinDbg or KD).

### <span id="Port_number_must_be_in_range_allowed_by_network_policy"></span><span id="port_number_must_be_in_range_allowed_by_network_policy"></span><span id="PORT_NUMBER_MUST_BE_IN_RANGE_ALLOWED_BY_NETWORK_POLICY"></span>Port number must be in range allowed by network policy

The range of port numbers that can be used for network debugging might be limited by your company's network policy. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrator. On the target computer, open a Command Prompt window as Administrator and enter the command **bcdedit /dbgsettings**. The output will be similar to this.

```
C:\> bcdedit /dbgsettings
key                     XXXXXX.XXXXX.XXXXX.XXXXX
debugtype               NET
hostip                  169.168.1.1
port                    50085
dhcp                    Yes
The operation completed successfully.
```

In the preceding output, the value of port is 50085. If the value of port lies outside the range allowed by your network administrator, enter the following command, where *w.x.y.z* is the IP address of the host computer, and *YourDebugPort* is a port number in the allowed range.

```
bcdedit /dbgsettings net hostip:w.x.y.z port:YourDebugPort
```

When the host debugger is connected, reboot the target computer.



## <span id="related_topics"></span>Related topics

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)
 
[Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

 






