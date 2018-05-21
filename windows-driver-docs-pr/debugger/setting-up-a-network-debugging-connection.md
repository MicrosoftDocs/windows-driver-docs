---
title: Setting Up Kernel-Mode Debugging over a Network Cable Manually
description: Debugging Tools for Windows supports kernel debugging over an Ethernet network.
ms.assetid: B4A79B2E-D4B1-42CA-9121-DEC923C76927
keywords: ["Network debugging", "Ethernet debugging", "Docking station"]
ms.author: domars
ms.date: 05/18/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up Kernel-Mode Debugging over a Network Cable Manually


Debugging Tools for Windows supports kernel debugging over an Ethernet network. This topic describes how to set up Ethernet debugging manually.

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. The host computer must be running Windows XP or later, and the target computer must be running Windows 8 or later.

Debugging over a network has the following advantages compared to debugging over other types of cable.

-   The host and target computers can be anywhere on the local network.
-   It is easy to debug many target computers from one host computer.
-   Network cable is inexpensive and readily available.
-   Given any two computers, it is likely that they will both have Ethernet adapters. It is less likely that they will both have serial ports or both have 1394 ports.

## <span id="Supported_Network_Adapters"></span><span id="supported_network_adapters"></span><span id="SUPPORTED_NETWORK_ADAPTERS"></span>Supported Network Adapters


The host computer can use any network adapter, but the target computer must use a network adapter that is supported by Debugging Tools for Windows. For a list of supported network adapters, see [Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md) and [Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md).


## <span id="Determining_the_IP_Address_of_the_Host_Computer"></span><span id="determining_the_ip_address_of_the_host_computer"></span><span id="DETERMINING_THE_IP_ADDRESS_OF_THE_HOST_COMPUTER"></span>Determining the IP Address of the Host Computer


Use one of the following procedures to determine the IP address of the host computer.

-   On the host computer, open a Command Prompt window and enter the following command:

    **ipconfig**

    Make a note of the IPv4 address of the network adapter that you intend to use for debugging.

-   On the target computer, open a Command Prompt window and enter the following command, where *HostName* is the name of the host computer:

    **ping -4** *HostName*

## <span id="Choosing_a_Port_for_Network_Debugging"></span><span id="choosing_a_port_for_network_debugging"></span><span id="CHOOSING_A_PORT_FOR_NETWORK_DEBUGGING"></span>Choosing a Port for Network Debugging


Choose a port number that will be used for debugging on both the host and target computers. You can choose any number from 49152 through 65535. The port that you choose will be opened for exclusive access by the debugger running on the host computer. Take care to choose a port number that is not used by any other applications that run on the host computer.

**Note**  The range of port numbers that can be used for network debugging might be limited by your company's network policy. There is no way to tell from the host computer what the limitations are. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrators.

 
If you connect several target computers to a single host computer, each connection must have a unique port number. For example, if you connect 100 target computers to a single host computer, you can assign port 50000 to the first connection, port 50001 to the second connection, port 50002 to the third connection, and so on.

**Note**  A different host computer could use the same range of ports (50000 through 50099) to connect to another 100 target computers.

 

## <span id="Setting_Up_the_Target_Computer"></span><span id="setting_up_the_target_computer"></span><span id="SETTING_UP_THE_TARGET_COMPUTER"></span>Setting Up the Target Computer


1.  Verify that the target computer has a supported network adapter.

2.  Connect the supported adapter to a network hub or switch using an appropriate network cable. 

> [!IMPORTANT]
> Before using BCDEdit to change boot information you may need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC.
> Re-enable these security features when testing is complete and appropriately manage the test PC, when the security features are disabled.


3.  In an elevated Command Prompt window, enter the following commands, where *w.x.y.z* is the IP address of the host computer, and *n* is a port number of your choice:

    **bcdedit /debug on**

    **bcdedit /dbgsettings net hostip:***w.x.y.z* **port:***n*

4.  **bcdedit** will display an automatically generated key. Copy the key and store it on a removable storage device like a USB flash drive. You will need the key when you start a debugging session on the host computer.

    **Note**  We strongly recommend that you use an automatically generated key. However, you can create your own key as described later in the Creating Your Own Key section.

     

5.  If there is more than one network adapter in the target computer, use Device Manager to determine the PCI bus, device, and function numbers for the adapter you want to use for debugging. Then in an elevated Command Prompt window, enter the following command, where *b*, *d*, and *f* are the bus number, device number, and function number of the adapter:

    **bcdedit /set "{dbgsettings}" busparams** *b.d.f*

6.  Reboot the target computer.

**Caution**  If your target computer is in a docking station, and you have network debugging enabled for a network adapter that is part of the docking station, do not remove the computer from the docking station. If you need to remove the target computer from the docking station, disable kernel debugging first. To disable kernel debugging on the target computer, open a Command Prompt window as Administrator and enter the command **bcdedit /debug off**. Reboot the target computer.

 

**Note**  If you intend to install the Hyper-V role on the target computer, see [Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md).

 

## <span id="Setting_Up_the_Host_Computer"></span><span id="setting_up_the_host_computer"></span><span id="SETTING_UP_THE_HOST_COMPUTER"></span>Setting Up the Host Computer


Connect the network adapter of the host computer to a network hub or switch using an appropriate network cable. 

## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session


### <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **Net** tab. Enter your port number and key. Click **OK**.

You can also start a session with WinDbg by opening a Command Prompt window and entering the following command, where *n* is your port number and *Key* is the key that was automatically generated by **bcdedit** when you set up the target computer:

**windbg -k net:port=***n***,key=***Key*

If you are prompted about allowing WinDbg to access the port through the firewall, allow WinDbg to access the port for all the different network types.

### <span id="Using_KD"></span><span id="using_kd"></span><span id="USING_KD"></span>Using KD

On the host computer, open a Command Prompt window. Enter the following command, where *n* is your port number and *Key* is the key that was automatically generated by **bcdedit** when you set up the target computer:

**kd -k net:port=***n***,key=***Key*

If you are prompted about allowing KD to access the port through the firewall, allow KD to access the port for all the different network types.


### <span id="Using_KDNET"></span><span id="using_kdnet"></span><span id="USING_KDNET"></span>Using KDNET.exe

Use the KDNET.exe utility to generate a unique key by following these steps.

1. Locate the WDK KDNET.exe and VerifiedNICList.xml files. By default it is located here.

```
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64
```

Copy them to a network share or thumb drive, so that they will be available on the target computer.


3. On the target computer, open a Command Prompt window as Administrator. Enter this command to validate that the NIC on the target PC is suported.

```
C:\KDNET>KDNet

Network debugging is supported on the following NICs:
busparams=0.25.0, Intel(R) 82579LM Gigabit Network Connection, KDNET is running on this NIC.kdnet.exe
```


4. Type this command to set the IP address of the host system. Use the IP address or the name of the host system. Pick a unique port address for each target/host pair that you work with, with in the range 50000-50039.

```
C:\>KDNet <HostComputerName> [DebugPort (50000-50039)] 

NtQuerySystemInformation cannot query SystemKernelDebuggingAllowed on this OS.
Enabling network debugging on Intel(R) 82577LM Gigabit Network Connection.
Key=2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
```
3. Note down the key returned, or copy it into notepad .txt file.

4. Restart the target PC. 

5. To connect to the target PC use the following, where <YourPort> is the port you selected above between 50000-50039, and <YourKey> is the key that was returned by KDNet above.

```
C:\Debuggers\windbg -k net:port=<YourPort>,key=<YourKey> 
```
6. If the debugger does not connect use the ping command to verify connectivity and then refer to the troubleshooting steps below. 

```
C:\>Ping <HostComputerIPAddress> 
```



### <span id="Allowing_the_debugger_through_the_firewall"></span><span id="allowing_the_debugger_through_the_firewall"></span><span id="ALLOWING_THE_DEBUGGER_THROUGH_THE_FIREWALL"></span>Allowing the debugger through the firewall

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. Client versions of Windows display the prompt, but Server versions of Windows do not display the prompt. You should respond to the prompt by checking the boxes for all three network types: domain, private, and public. If you do not get the prompt, or if you did not check the boxes when the prompt was available, you must use Control Panel to allow access through the firewall. Open **Control Panel &gt; System and Security**, and click **Allow an app through Windows Firewall**. In the list of applications, locate Windows GUI Symbolic Debugger and Windows Kernel Debugger. Use the check boxes to allow those two applications through the firewall. Restart your debugging application (WinDbg or KD).

## <span id="How_the_Debugger_Obtains_an_IP_Address_for_the_Target_Computer"></span><span id="how_the_debugger_obtains_an_ip_address_for_the_target_computer"></span><span id="HOW_THE_DEBUGGER_OBTAINS_AN_IP_ADDRESS_FOR_THE_TARGET_COMPUTER"></span>How the Debugger Obtains an IP Address for the Target Computer


The kernel debugging driver on the target computer attempts to use Dynamic Host Configuration Protocol (DHCP) to get a routable IP address for the network adapter that is being used for debugging. If the driver obtains a DHCP-assigned address, then the target computer can be debugged by host computers located anywhere on the network. If the driver fails to obtain a DHCP-assigned address, it uses Automatic Private IP Addressing (APIPA) to obtain a local link IP address. Local link IP addresses are not routable, so a host and target cannot use a local link IP address to communicate through a router. In that case, network debugging will work if you plug the host and target computers into the same network hub or switch.


## <span id="Encryption_Key"></span><span id="encryption_key"></span><span id="ENCRYPTION_KEY"></span>Encryption key

To keep the target computer secure, packets that travel between the host and target computers must be encrypted. We strongly recommend that you use an automatically generated encryption key (provided by **bcdedit** when you configure the target computer).Network debugging uses a 256-bit key that is specified as four 64-bit values, in base 36, separated by periods. Each 64-bit value is specified by using up to 13 characters. Valid characters are the letters a through z and the digits 0 through 9. Special characters are not allowed. 

To specify your own key, open an elevated Command Prompt window on the target computer. Enter the following command, where *w.x.y.z* is the IP address of the host computer, and *n* is your port number, and *Key* is your key:

**bcdedit /dbgsettings net hostip:***w.x.y.z* **port:***n* **key:***Key*

Reboot the target computer.


## <span id="troubleshooting_tips_for_debugging_over_a_network_cable"></span><span id="TROUBLESHOOTING_TIPS_FOR_DEBUGGING_OVER_A_NETWORK_CABLE"></span>Troubleshooting Tips for Debugging over a Network Cable


### <span id="Debugging_application_must_be_allowed_through_firewall"></span><span id="debugging_application_must_be_allowed_through_firewall"></span><span id="DEBUGGING_APPLICATION_MUST_BE_ALLOWED_THROUGH_FIREWALL"></span>Debugging application must be allowed through firewall

Your debugger (WinDbg or KD) must have access through the firewall. You can use Control Panel to allow access through the firewall. Open **Control Panel &gt; System and Security**, and click **Allow an app through Windows Firewall**. In the list of applications, locate Windows GUI Symbolic Debugger and Windows Kernel Debugger. Use the check boxes to allow those two applications through the firewall. Restart your debugging application (WinDbg or KD).

### <span id="Port_number_must_be_in_range_allowed_by_network_policy"></span><span id="port_number_must_be_in_range_allowed_by_network_policy"></span><span id="PORT_NUMBER_MUST_BE_IN_RANGE_ALLOWED_BY_NETWORK_POLICY"></span>Port number must be in range allowed by network policy

The range of port numbers that can be used for network debugging might be limited by your company's network policy. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrator. On the target computer, open a Command Prompt window as Administrator and enter the command **bcdedit /dbgsettings**. The output will be similar to this.

```
key                     XXXXXX.XXXXX.XXXXX.XXXXX
debugtype               NET
debugport               1
baudrate                115200
hostip                  10.125.4.86
port                    50085
```

Notice the value of **port**. For example, in the preceding output, the value of **port** is 50085. If the value of **port** lies outside the range allowed by your network administrator, enter the following command, where *w.x.y.z* is the IP address of the host computer, and *n* is a port number in the allowed range

**bcdedit /dbgsettings net hostip:***w.x.y.z* **port:***n*

Reboot the target computer.

**Note**  In the preceding output from **bcdedit**, the debugport and baudrate entries to not apply to debugging over a network cable. Those entries apply to debugging over a serial cable, but they sometimes appear even though the target is configured for debugging over a network cable.

 

### <span id="Specify_busparams_if_target_computer_has_multiple_network_adapters"></span><span id="specify_busparams_if_target_computer_has_multiple_network_adapters"></span><span id="SPECIFY_BUSPARAMS_IF_TARGET_COMPUTER_HAS_MULTIPLE_NETWORK_ADAPTERS"></span>Specify busparams if target computer has multiple network adapters

If your target computer has more than one network adapter, you must specify the bus, device, and function numbers of the network adapter that you intend to use for debugging. To specify the bus parameters, Open Device Manager, and locate the network adapter that you want to use for debugging. Open the property page for the network adapter, and make a note of the bus number, device number, and function number. In an elevated Command Prompt Window, enter the following command, where *b*, *d*, and *f* are the bus, device and function numbers in decimal format:

**bcdedit /set "{dbgsettings}" busparams** *b***.***d***.***f*

Reboot the target computer.

## <span id="IPV6"></span><span id="ipv6"></span><span id="IPv6"></span>IPv6

IPv6 support was added in June of 2018.

To use IpV6 with the debugger complete these steps.

1. Ping your \<debughostname\> and note the IPv6 address that is reported on the Reply from output lines.Use this IPv6 address in place of x:y:z:p:d:q:r:n below

TBD - Should we show the usage of KDNET to generate a proper key?

2. Use BCDEdit to delete any existing ip address values in dbgsettings.

```
bcdedit -deletevalue {dbgsettings} hostip
```

3. Set the IPv6 address of the host. There must not be any spaces in the hostipv6=x:y:z:p:d:q:r:n string. <YourPort> is the port you selected above between 50000-50039, and <YourKey> is the key that was returned by KDNet above.


```
bcdedit /dbgsettings net hostipv6:x:y:z:p:d:q:r:n port:<YourPort> key:<YourKey>
```

??? TBD - does upper/lower case matter?


4. Type this command to confirm that the dbgsettings are set properly.

```
C:\> bcdedit /dbgsettings
busparams               0.25.0
key                     2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
debugtype               NET
hostipv6                  2001:db8:0:0:ff00:0:42:8329
port                    50010
dhcp                    Yes
The operation completed successfully.
```

5. Reboot your target machine. 

6. On the host machine use this command to start the debugger. 

```
Windbg -k net:port=<yournetworkportnumber>,key=<key_output_from_kdnet>,target=::<YourIPv6Address> 
```

7. The debugger should connect to the host debugger early during boot. You will know that KDNET is using an IPv6 connection because the IP addresses reported in the connected message will be IPv6 addresses instead of IPv4 addresses. 


**NOTES**

- Every debugger bcd setting that allows the hostip to be specified has a corresponding hostipv6 element.  There are three.  

    IPv4 | IPv6 | Usage
    |-----------|-----------|-----------|
    hostip | hostipv6 | For boot and kernel debugging
    targethostip | targethostipv6  | Specific to kernel debugging  
    hypervisorhostip | hypervisorhostipv6  | For hyper-v debugging


- If you set the hostipv6 style address for any of those kinds of debugging, it means you want and will get IPv6.

- If you set the hostip style address for any of those kinds of debugging, it means you want and will get IPv4.

- The target will only do IPv4 or IPv6, not both at the same time.

- The host do will either one, and what is used, is under control of the target machine.

- If the target= option on the debugger command line contains any : characters, the debugger will assume it is an IPv6 address, and will force use of IPv6 for that connection.

- The debugger auto selects IPv4 or IPv6. The debugger determines if IPv4 or IPv6 is being used by the target machine, and connects automatically.

- If you want to force IPv6 debugging in the debugger on the host, but you want the debugger to listen for a connection from the target, then you specify ,target=:: \<ipv6 address of 0\>.

- If you want to force IPv4 debugging in the debugger on the host, but you want the debugger to listen for a connection from the target, then you specify ,target=0.0.0.0 (ipv4 address of 0)

- If you specify ,target= and use a machine name, the debugger will convert that machine name into an IPv4 address and an IPv6 address, and will attempt to connect on both.


## <span id="related_topics"></span>Related topics

[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)
 

 






