---
title: Setting Up KDNET Network Kernel Debugging Manually
description: Debugging Tools for Windows supports kernel debugging over a network.
keywords: ["Network debugging", "Ethernet debugging", "Docking station", "Setting Up Kernel-Mode Debugging over a Network Cable Manually"]
ms.date: 12/07/2018
---

# Setting Up KDNET Network Kernel Debugging Manually

Debugging Tools for Windows supports kernel debugging over a network. This topic describes how to set up network debugging manually.

> [!IMPORTANT]
> Setting up a network debugging manually is a complex and error prone process.
> To set up network debugging automatically, see **[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)**. Using the KDNET utility is **strongly** recommended for all debugger users.

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. The host computer must be running Windows 7 or later, and the target computer must be running Windows 8 or later.

Debugging over a network has the following advantages compared to debugging over other types of connectivity.

- The host and target computers can be anywhere on the local network.
- It is easy to debug many target computers from one host computer.
- Given any two computers, it is likely that they will both have Ethernet adapters. It is less likely that they will both have serial ports or both have 1394 ports.
- Network debugging is significantly faster than serial port debugging.

## Supported Network Adapters

The host computer can use any network adapter, but the target computer must use a network adapter that is supported by Debugging Tools for Windows. For a list of supported network adapters, see [Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md) and [Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md).

## Install the Debugging Tools for Windows

Confirm that the Debugging Tools for Windows are installed on the host system. For information on downloading and installing the debugger tools, see [Download Debugging Tools for Windows](debugger-download-tools.md).

## Determining the IP Address of the Host Computer

Use one of the following procedures to determine the IP address of the host computer.

1. On the host computer, open a Command Prompt window and enter the following command:

   ```console
   ipconfig
   ```

    Make a note of the IPv4 address of the network adapter that you intend to use for debugging.

2. On the target computer, open a Command Prompt window and enter the following command, where *YourIPAddress* is the IP address of the host computer:

   ```console
   ping -4 <YourIPAddress>
   ```

## Choosing a Port for Network Debugging

Choose a port number that will be used for debugging on both the host and target computers. You can choose any number from 49152 through 65535, the recommended range is 50000 - 50039. The port that you choose will be opened for exclusive access by the debugger running on the host computer. Take care to choose a port number that is not used by any other applications that run on the host computer.

**Note**  The range of port numbers that can be used for network debugging might be limited by your company's network policy. There is no way to tell from the host computer what the limitations are. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrators.

If you connect several target computers to a single host computer, each connection must have a unique port number. For example, if you connect 100 target computers to a single host computer, you can assign port 50000 to the first connection, port 50001 to the second connection, port 50002 to the third connection, and so on.

**Note**  A different host computer could use the same range of ports (50000 through 50099) to connect to another 100 target computers.

## Setting Up the Target Computer

1. Verify that the target computer has a supported network adapter. See these topics for more information.

    - [Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

    - [Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)

2. Connect the supported adapter to a network hub or switch using an appropriate network cable.

> [!IMPORTANT]
> Before using BCDEdit to change boot information you may need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC.
> Re-enable these security features when testing is complete and appropriately manage the test PC, when the security features are disabled.

3. In an elevated Command Prompt window, enter the following commands, where *w.x.y.z* is the IP address of the host computer, and *n* is a port number of your choice:

    ```console
    bcdedit /debug on

    bcdedit /dbgsettings net hostip:w.x.y.z port:n
    ```

4. **bcdedit** will display an automatically generated key. Copy the key and store it on a removable storage device like a USB flash drive. You will need the key when you start a debugging session on the host computer.

    **Note**  We strongly recommend that you use an automatically generated key. However, you can create your own key as described later in the "Creating Your Own Key" section.

5. Use Device Manager to determine the PCI bus, device, and function numbers for the adapter you want to use for debugging. These values are displayed in Device Manager under *Location* on the *General* tab.  Then in an elevated Command Prompt window, enter the following command, where *b*, *d*, and *f* are the bus number, device number, and function number of the adapter:

    ```console
    bcdedit /set "{dbgsettings}" busparams b.d.f
    ```

6. The target PC will be rebooted after a kernel debugger is attached. This is described in the next section.

**Note**  If you intend to install the Hyper-V role on the target computer, see [Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md).

**Caution**  If your target computer is in a docking station, and you have network debugging enabled for a network adapter that is part of the docking station, do not remove the computer from the docking station. If you need to remove the target computer from the docking station, disable kernel debugging first. To disable kernel debugging on the target computer, open a Command Prompt window as Administrator and enter the command **bcdedit /debug off**. Reboot the target computer.

## Starting the Debugging Session

Confirm that the network adapter of the host computer to a network hub or switch using an appropriate network cable.

On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **Net** tab. Enter your port number and key. Select **OK**.

You can also start a session with WinDbg by opening a Command Prompt window and entering the following command, where *n* is your port number and *MyKey* is the key that was automatically generated by **bcdedit** when you set up the target computer:

```console
windbg -k net:port=<n>,key=<MyKey>
```

If you are prompted about allowing WinDbg to access the port through the firewall, allow WinDbg to access the port for **all three** of the different network types.

### Using KD

On the host computer, open a Command Prompt window. Enter the following command, where *n* is your port number and *MyKey* is the key that was automatically generated by **bcdedit** when you set up the target computer:

```console
kd -k net:port=<n>,key=<MyKey>
```

If you are prompted about allowing WinDbg to access the port through the firewall, allow WinDbg to access the port for **all three** of the different network types.

## Restarting the Target PC

Once the debugger is connected, and waiting to connect, reboot the target computer. One way to do restart the PC is to use this command, from an administrator's command prompt.

   ```console
   shutdown -r -t 0
   ```

When the target is restarted, the debugger in the host OS should connect.

After connecting to the target on the host, hit break on your debugger and you can start debugging.

### Allowing the debugger through the firewall

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. Client versions of Windows display the prompt, but Server versions of Windows do not display the prompt. You should respond to the prompt by checking the boxes for **all three** network types: domain, private, and public. If you do not get the prompt, or if you did not check the boxes when the prompt was available, you must use Control Panel to allow access through the firewall. Open **Control Panel &gt; System and Security** and select **Allow an app through Windows Firewall**. In the list of applications, locate Windows GUI Symbolic Debugger and Windows Kernel Debugger. Use the check boxes to allow those two applications through the firewall. Restart your debugging application (WinDbg or KD).

## Encryption key

To keep the target computer secure, packets that travel between the host and target computers must be encrypted. We strongly recommend that you use an automatically generated encryption key (provided by **bcdedit** when you configure the target computer). Network debugging uses a 256-bit key that is specified as four 64-bit values, in base 36, separated by periods. Each 64-bit value is specified by using up to 13 characters. Valid characters are the letters a through z and the digits 0 through 9. Special characters are not allowed.

To specify your own key, open an elevated Command Prompt window on the target computer. Enter the following command, where *w.x.y.z* is the IP address of the host computer, and *n* is your port number, and *Key* is your key:

```console
bcdedit /dbgsettings net hostip:w.x.y.z port:n key:Key
```

The target computer needs to be rebooted anytime the dbgsettings are changed.

## Troubleshooting Tips

### Debugging application must be allowed through firewall

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. Client versions of Windows display the prompt, but Server versions of Windows do not display the prompt. You should respond to the prompt by checking the boxes for **all three** network types: domain, private, and public. If you do not get the prompt, or if you did not check the boxes when the prompt was available, you must use Control Panel to allow access through the firewall. Open **Control Panel &gt; System and Security** and select **Allow an app through Windows Firewall**. In the list of applications, locate *Windows GUI Symbolic Debugger* and *Windows Kernel Debugger*. Use the check boxes to allow those two applications through the firewall. Scroll down and select **OK**, to save the firewall changes. Restart the debugger.

### Port number must be in range allowed by network policy

The range of port numbers that can be used for network debugging might be limited by your company's network policy. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrator. On the target computer, open a Command Prompt window as Administrator and enter the command **bcdedit /dbgsettings**. The output will be similar to this.

```console
C:\> bcdedit /dbgsettings
key                     XXXXXX.XXXXX.XXXXX.XXXXX
debugtype               NET
hostip                  169.168.1.1
port                    50085
dhcp                    Yes
The operation completed successfully.
```

In the preceding output, the value of port is 50085. If the value of port lies outside the range allowed by your network administrator, enter the following command, where *w.x.y.z* is the IP address of the host computer, and *YourDebugPort* is a port number in the allowed range.

```console
bcdedit /dbgsettings net hostip:w.x.y.z port:YourDebugPort
```

After changing the target machine debugger settings, rerun the debugger on the host machine with the new port setting, and then reboot the target computer.

### Use Ping to test connectivity

If the debugger does not connect use the ping command on the target PC to verify connectivity.

   ```console
   C:\>Ping <HostComputerIPAddress>
   ```

Note that this may not work if your host computer is not configured to be discoverable on the network, since the firewall may block ping requests, and because of this, you will not get any responses when you ping the host.


### How the Debugger Obtains an IP Address for the Target Computer

KDNET on the target computer attempts to use Dynamic Host Configuration Protocol (DHCP) to get a routable IP address for the network adapter that is being used for debugging. If KDNET obtains a DHCP-assigned address, then the target computer can be debugged by host computers located anywhere on the network. If KDNET fails to obtain a DHCP-assigned address, it uses Automatic Private IP Addressing (APIPA) to obtain a local link IP address. Local link IP addresses are not routable, so a host and target cannot use a local link IP address to communicate through a router. In that case, network debugging will work if you plug the host and target computers into the same network hub or switch.

### Always specify busparams when setting up KDNET on a physical machine with a PCI based NIC

If you are setting up KDNET on a physical machine with a PCI or PCIe based NIC, you should always specify the busparams for the NIC you want to use for KDNET. To specify the bus parameters, Open Device Manager, and locate the network adapter that you want to use for debugging. Open the property page for the network adapter and make a note of the bus number, device number, and function number that are displayed under *Location* on the *General* tab. In an elevated Command Prompt Window, enter the following command, where *b*, *d*, and *f* are the bus, device and function numbers in decimal format:

```console
bcdedit /set "{dbgsettings}" busparams b.d.f
```

When the debugger is running on the host machine, and waiting to connect, reboot the target computer, using this command.

```console
shutdown -r -t 0
```

## Manually delete BCDEdit entries

Manually deleting is not normally required but is provided here as a troubleshooting procedure for unusual situations.

Manually deleting entries is not necessary when using the kdnet utility. For more information, see [Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md).

When you use bcdedit –deletevalue, you must provide a valid bcd element name. For more information, see [BCDEdit /deletevalue](../devtest/bcdedit--deletevalue.md).

To manually delete BCDEdit entries, complete these steps.

1. On the target computer, open a Command Prompt window as Administrator.

2. As an example, enter this command to delete the BCDEdit debugging entry for the host IP address.

    ```console
    bcdedit -deletevalue {dbgsettings} hostip
    ```

When you delete the hostip, you need to specify *target=* on the debugger command line.

3. As another example, delete the port entry using this command.

    ```console
    bcdedit -deletevalue {dbgsettings} port
    ```

When you delete the port entry, KDNET will use the default ICANN registered debugger port of 5364.

## Hyper-V

### Setting up Hyper-V

If you intend to install the Hyper-V role on the target computer, see [Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md).

For information on debugging a hyper-v Virtual Machine (VM), see [Setting Up Network Debugging of a Virtual Machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md).

### Enabling KDNET on a hyper-v host that is running VMs with external network connectivity

There is a specific situation, which is not uncommon, which will cause networking in VMs to stop working:

- Hyper-V has been enabled on the PC, an external networking switch has been created and is pointed at a physical NIC in the machine, and VMs have been configured to use that external switch for their networking.

- KDNET is then enabled on the hyper-v host OS using the same physical NIC that is pointed to by the external networking switch, and the host is rebooted.

- All of the VMs that were using the previously configured external switch, lose their network connectivity after the reboot.

This is by design, and happens because KDNET takes exclusive control over the NIC it is configured to use, and the native NDIS miniport for that NIC is not loaded by the OS.  When this occurs, the external networking switch can no longer communicate with the native NDIS miniport driver, and will stop working.  To work around this situation, do the following:

1.	Open the Virtual Switch Manager from Hyper-V Manager, select your existing Virtual Switch, and change the external network NIC to the *Microsoft Kernel Debug Network Adapter* by selecting it from the drop down box and then selecting OK in the Virtual Switch Manager dialog box.

2.	After updating your Virtual Switch NIC, shutdown and restart your VMs.

When KDNET debugging is turned off, the same procedure will need to be followed to repoint the external switch back to the native NDIS miniport for the NIC.  Otherwise VM connectivity will be lost when the machine is rebooted after debugging is disabled.


## <span id="IPV6"></span><span id="ipv6"></span><span id="IPv6"></span>IPv6

IPv6 support was added in Windows version 1809.

To use IPv6 with the debugger complete these steps.

1. Ping your \<debughostname\> and note the IPv6 address that is reported on the Reply from output lines.Use this IPv6 address in place of x:y:z:p:d:q:r:n below.

2. Use BCDEdit to delete any existing ip address values in dbgsettings.

    ```console
    bcdedit -deletevalue {dbgsettings} hostip
    ```

3. Set the IPv6 address of the host. There must not be any spaces in the `hostipv6=s:t:u:v:w:x:y:z` string. \<YourPort\> is is the network port number to use for this target machine, \<YourKey\> is the four part security key, and \<b.d.f\> are the bus device function location numbers for the NIC you want to use for KDNET.

    ```console
    bcdedit /dbgsettings net hostipv6:s:t:u:v:w:x:y:z port:<YourPort> key:<YourKey> busparams:<b.d.f>
    ```

4. Type this command to confirm that the dbgsettings are set properly.

    ```console
    C:\> bcdedit /dbgsettings
    busparams               0.25.0
    key                     2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
    debugtype               NET
    hostipv6                  2001:db8:0:0:ff00:0:42:8329
    port                    50010
    dhcp                    Yes
    The operation completed successfully.
    ```

5. On the host machine use this command to start the debugger. 

    ```console
    Windbg -k net:port=<yournetworkportnumber>,key=<key_output_from_kdnet>,target=::<YourIPv6Address> 
    ```

6. When the debugger is running on the host machine, and waiting to connect, reboot the target computer. 

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

- The target will only do IPv4 or IPv6, not both at the same time. Which version of the IP protocol is used is controlled by the target machine dbgsettings.  If hostip is set, the target will use IPv4.  If hostipv6 is set, the target will use IPv6.

- The host debugger will normally auto select use of IPv4 or IPv6. By default the debugger listens on both an IPv4 socket and an IPv6 socket, and connects automatically on either one to the target machine.

- If you want to force use of IPv6 in the debugger on the host, but you want the debugger to listen for a connection from the target, then you can add, `target=::` to the debugger command line. :: is an IPv6 address of 0.

- If you want to force IPv4 debugging in the debugger on the host, but you want the debugger to listen for a connection from the target, then you can add, `target=0.0.0.0` to the debugger command line. 0.0.0.0 is an IPv4 address of 0.

- If you specify, target= on the debugger command line and use a machine name, the debugger will convert that machine name into an IPv4 address and an IPv6 address, and will attempt to connect on both.

- If you specify, target= on the debugger command line, and use an IP address, if the IP address contains any contains any : characters, the debugger will assume it is an IPv6 address, and will force use of IPv6 for that connection.  If the IP address contains any . characters, the debugger will assume it is an IPv4 address, and will force use of IPv4 for that connection.

- If you setup IPv6 on the target, and force use of IPv4 on the debugger command line, you will not get a connection.

- If you setup IPv4 on the target, and force use of IPv6 on the debugger command line, you will also not get a connection.




## Related topics

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)
