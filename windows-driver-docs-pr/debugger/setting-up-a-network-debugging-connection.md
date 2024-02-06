---
title: Set Up KDNET Network Kernel Debugging Manually
description: Learn how Debugging Tools for Windows supports kernel debugging over a network. This article describes how to set up network debugging manually.
keywords: ["Network debugging", "Ethernet debugging", "Docking station", "Setting Up Kernel-Mode Debugging over a Network Cable Manually"]
ms.date: 01/20/2022
---

# Set up KDNET network kernel debugging manually

Debugging Tools for Windows supports kernel debugging over a network. This article describes how to set up network debugging manually.

> [!IMPORTANT]
> Setting up a network debugging manually is a complex and error prone process.
> To set up network debugging automatically, see [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md). Using the KDNET utility is strongly recommended for all debugger users.

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. The host computer must be running Windows 7 or later, and the target computer must be running Windows 8 or later.

Debugging over a network has the following advantages compared to debugging over other types of connectivity.

- The host and target computers can be anywhere on the local network.
- It's easy to debug many target computers from one host computer.
- Given any two computers, it's likely that they both have Ethernet adapters. It's less likely that they both have serial ports or 1394 ports.
- Network debugging is faster than serial port debugging.

## Supported network adapters

The host computer can use any network adapter, but the target computer must use a network adapter that's supported by Debugging Tools for Windows. For a list of supported network adapters, see [Supported Ethernet NICs for network kernel debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md) and [Supported Ethernet NICs for network kernel debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md).

## Install Debugging Tools for Windows

Confirm that the Debugging Tools for Windows are installed on the host system. For information on downloading and installing the debugger tools, see [Debugging Tools for Windows](debugger-download-tools.md).

## Determine the IP address of the host computer

Use one of the following procedures to determine the IP address of the host computer.

1. On the host computer, open a command prompt and enter the following command:

   ```console
   ipconfig
   ```

    Make a note of the IPv4 address of the network adapter that you intend to use for debugging.

2. On the target computer, open a command prompt and enter the following command, where *YourIPAddress* is the IP address of the host computer:

   ```console
   ping -4 <YourIPAddress>
   ```

## Choose a port for network debugging

Choose a port number for debugging on both the host and target computers. You can choose any number from 49152 through 65535. The recommended range is 50000 - 50039. The port that you choose is opened for exclusive access by the debugger running on the host computer. Take care to choose a port number that isn't used by any other applications that run on the host computer.

> [!NOTE]
> The range of port numbers that can be used for network debugging might be limited by your company's network policy. There's no way to tell from the host computer what the limitations are. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrators.

If you connect several target computers to a single host computer, each connection must have a unique port number. For example, if you connect 100 target computers to a single host computer, you can assign port 50000 to the first connection, port 50001 to the second connection, and so on.

> [!NOTE]
> A different host computer could use the same range of ports (50000 through 50099) to connect to another 100 target computers.

## Set up the target computer

1. Verify that the target computer has a supported network adapter. For more information, see:

    - [Supported Ethernet NICs for network kernel debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

    - [Supported Ethernet NICs for network kernel debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)

2. Connect the supported adapter to a network hub or switch using an appropriate network cable.

> [!IMPORTANT]
> Before using BCDEdit to change boot information you might need to temporarily suspend Windows security features, such as BitLocker and Secure Boot, on the test PC.
> Re-enable these security features when testing is complete, and appropriately manage the test PC when the security features are disabled.

3. In an elevated command prompt, enter the following commands, where *w.x.y.z* is the IP address of the host computer, and *n* is a port number of your choice:

    ```console
    bcdedit /debug on

    bcdedit /dbgsettings net hostip:w.x.y.z port:n
    ```

4. BCDEdit displays an automatically generated key. Copy the key and store it on a removable storage device, like a USB flash drive. You need the key when you start a debugging session on the host computer.

5. Use Device Manager to determine the PCI bus, device, and function numbers for the adapter you want to use for debugging. These values are displayed in Device Manager under *Location* on the *General* tab. Then in an elevated command prompt, enter the following command, where *b*, *d*, and *f* are the bus number, device number, and function number of the adapter:

    ```console
    bcdedit /set "{dbgsettings}" busparams b.d.f
    ```

6. The target PC will be rebooted after a kernel debugger is attached.

> [!NOTE]
> If you intend to install the Hyper-V role on the target computer, see [Setting up network debugging of a virtual machine host](setting-up-network-debugging-of-a-virtual-machine-host.md).

**Caution**  If your target computer is in a docking station and you have network debugging enabled for a network adapter that's part of the docking station, don't remove the computer from the docking station. If you need to remove the target computer from the docking station, disable kernel debugging first. To disable kernel debugging on the target computer, open a command prompt as an administrator and enter the command `bcdedit /debug off`. Reboot the target computer.

## Start the debugging session

Confirm that the network adapter of the host computer is connected to a network hub or switch using an appropriate network cable.

On the host computer, open WinDbg. On the **File** menu, select **Kernel Debug**. In the Kernel Debugging dialog, open the **Net** tab. Enter your port number and key. Select **OK**.

You can also start a session with WinDbg by opening a command prompt and entering the following command, where *n* is your port number and *MyKey* is the key that was automatically generated by BCDEdit when you set up the target computer:

```console
windbg -k net:port=<n>,key=<MyKey>
```

If you're prompted to allow WinDbg to access the port through the firewall, allow WinDbg to access the port for **all three** of the different network types.

### Use KD

On the host computer, open a command prompt. Enter the following command, where *n* is your port number and *MyKey* is the key that was automatically generated by BCDEdit when you set up the target computer:

```console
kd -k net:port=<n>,key=<MyKey>
```

If you're prompted about allowing WinDbg to access the port through the firewall, allow WinDbg to access the port for **all three** of the different network types.

## Restart the Target PC

Once the debugger is connected and waiting to connect, reboot the target computer. One way to restart the PC is to use this command from an administrator's command prompt:

   ```console
   shutdown -r -t 0
   ```

When the target is restarted, the debugger in the host OS should connect.

After connecting to the target on the host, hit break on your debugger and you can start debugging.

### Allow the debugger through the firewall

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. Client versions of Windows display the prompt, but server versions of Windows don't display the prompt. You should respond to the prompt by checking the boxes for **all three** network types: domain, private, and public. 

If you don't get the prompt or if you didn't check the boxes when the prompt was available, you must use the Control Panel to allow access through the firewall on the host PC where the debugger is running. Open **Control Panel > System and Security** and select **Allow an app through Windows Firewall**. 

   - (WinDbg) In the list of applications, locate *WinDbg engine process (TCP) (all)*.

   - (Classic WinDbg) In the list of applications, locate *Windows GUI Symbolic Debugger* and *Windows Kernel Debugger*.

Use the checkboxes to allow those applications through the firewall. Restart your debugging application (WinDbg or KD).

## Encryption key

To keep the target computer secure, packets that travel between the host and target computers must be encrypted. You should use an automatically generated encryption key (provided by BCDEdit when you configure the target computer). Using an automatically generated encryption key is recomended as it is a more secure, and provides a unique value that is used in establishing the connection to a specific target. 

Network debugging uses a 256-bit key that's specified as four 64-bit values, in base 36, separated by periods. Each 64-bit value is specified by using up to 13 characters. Valid characters are the letters *a* through *z* and the digits 0 through 9. Special characters aren't allowed.

To specify your own key, open an elevated command prompt on the target computer. Enter the following command, where `w.x.y.z` is the IP address of the host computer, and *n* is your port number, and *Key* is your key:

```console
bcdedit /dbgsettings net hostip:w.x.y.z port:n key:Key
```

The target computer needs to be rebooted anytime the *dbgsettings* are changed.

## Troubleshooting tips

### The debugging application must be allowed through firewalls

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. Client versions of Windows display the prompt, but server versions of Windows don't display the prompt. You should respond to the prompt by checking the boxes for **all three** network types: domain, private, and public. 

If you don't get the prompt or if you didn't check the boxes when the prompt was available, you must use Control Panel to allow access through the firewall. Open **Control Panel > System and Security** and select **Allow an app through Windows Firewall**. 

   - (WinDbg) In the list of applications, locate *WinDbg engine process (TCP) (all)*.

   - (WinDbg (Clasic)) In the list of applications, locate *Windows GUI Symbolic Debugger* and *Windows Kernel Debugger*.

Use the checkboxes to allow those applications through the firewall. Scroll down and select **OK** to save the firewall changes. Restart the debugger.

### The port number must be in the range allowed by network policy

The range of port numbers that can be used for network debugging might be limited by your company's network policy. To determine whether your company's policy limits the range of ports that can be used for network debugging, check with your network administrator. On the target computer, open a command prompt as an administrator and enter the command `bcdedit /dbgsettings`. The output will be similar to the following:

```console
C:\> bcdedit /dbgsettings
key                     XXXXXX.XXXXX.XXXXX.XXXXX
debugtype               NET
hostip                  169.168.1.1
port                    50085
dhcp                    Yes
The operation completed successfully.
```

In the preceding output, the value of port is 50085. If the value of port lies outside the range allowed by your network administrator, enter the following command. The value *w.x.y.z* is the IP address of the host computer, and *YourDebugPort* is a port number in the allowed range.

```console
bcdedit /dbgsettings net hostip:w.x.y.z port:YourDebugPort
```

After changing the target machine debugger settings, rerun the debugger on the host machine with the new port setting, and then reboot the target computer.

### Use ping to test connectivity

If the debugger doesn't connect, use the ping command on the target PC to verify connectivity.

   ```console
   C:\>Ping <HostComputerIPAddress>
   ```

> [!NOTE]
> This may not work if your host computer isn't configured to be discoverable on the network since the firewall may block ping requests. If the firewall blocks ping requests, you will not get any responses when you ping the host.

### How the debugger obtains an IP address for the target computer

KDNET on the target computer attempts to use Dynamic Host Configuration Protocol (DHCP) to get a routable IP address for the network adapter that's being used for debugging. If KDNET obtains a DHCP-assigned address, then the target computer can be debugged by host computers located anywhere on the network. If KDNET fails to obtain a DHCP-assigned address, it uses Automatic Private IP Addressing (APIPA) to obtain a local link IP address. Local link IP addresses aren't routable, so a host and target can't use a local link IP address to communicate through a router. In that case, network debugging will work if you plug the host and target computers into the same network hub or switch.

### Always specify busparams when setting up KDNET on a physical machine with a PCI based NIC

If you're setting up KDNET on a physical machine with a PCI or PCIe based NIC, you should always specify the busparams for the NIC you want to use for KDNET. To specify the bus parameters, open Device Manager, and locate the network adapter that you want to use for debugging. Open the property page for the network adapter and make a note of the bus number, device number, and function number that are displayed under *Location* on the *General* tab. In an elevated command prompt, enter the following command, where *b*, *d*, and *f* are the bus, device and function numbers in decimal format:

```console
bcdedit /set "{dbgsettings}" busparams b.d.f
```

When the debugger is running on the host machine and waiting to connect, reboot the target computer using the following command:

```console
shutdown -r -t 0
```

## Manually delete BCDEdit entries

Manually deleting isn't normally required but is provided here as a troubleshooting procedure for unusual situations.

Manually deleting entries isn't necessary when using the kdnet utility. For more information, see [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md).

When you use `bcdedit –deletevalue`, you must provide a valid bcd element name. For more information, see [BCDEdit /deletevalue](../devtest/bcdedit--deletevalue.md).

To manually delete bcedit entries, complete the following steps:

1. On the target computer, open a command prompt as an administrator.

2. As an example, enter the following command to delete the BCDEdit debugging entry for the host IP address:

    ```console
    bcdedit -deletevalue {dbgsettings} hostip
    ```

When you delete the hostip, you need to specify *target=* on the debugger command line.

3. As another example, delete the port entry by using the following command:

    ```console
    bcdedit -deletevalue {dbgsettings} port
    ```

When you delete the port entry, KDNET uses the default ICANN registered debugger port of 5364.

## Set up Hyper-V

If you intend to install the Hyper-V role on the target computer, see [Setting up network debugging of a virtual machine host](setting-up-network-debugging-of-a-virtual-machine-host.md).

For information on debugging a Hyper-V Virtual Machine (VM), see [Setting up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md).

## Enable KDNET on a Hyper-V host that's running VMs with external network connectivity

Sometimes a situation occurs that causes networking in VMs to stop working:

- Hyper-V has been enabled on the PC, an external networking switch has been created and is pointed at a physical NIC in the machine, and VMs have been configured to use that external switch for their networking.

- KDNET is then enabled on the Hyper-V host OS using the same physical NIC that's pointed to by the external networking switch. The host is rebooted.

- All of the VMs that used the previously configured external switch, lose their network connectivity after the reboot.

This stoppage is by design and happens because KDNET takes exclusive control over the NIC it's configured to use. The native NDIS miniport for that NIC isn't loaded by the OS. The external networking switch can then no longer communicate with the native NDIS miniport driver and stops working. To work around this situation, do the following:

1. Open the Virtual Switch Manager from Hyper-V Manager, and select your existing Virtual Switch. Change the external network NIC to the *Microsoft Kernel Debug Network Adapter* by selecting it from the dropdown menu and then selecting **OK** in the Virtual Switch Manager dialog.

2. After you update your Virtual Switch NIC, shutdown and restart your VMs.

When KDNET debugging is turned off, the same procedure needs to be followed to repoint the external switch back to the native NDIS miniport for the NIC. Otherwise, VM connectivity is lost when the machine is rebooted after debugging is disabled.

## IPv6

IPv6 support was added in Windows version 1809.

To use IPv6 with the debugger, complete the following steps:

1. Ping your \<debughostname> and note the IPv6 address that's reported on the reply from output lines. Use this IPv6 address in place of `x:y:z:p:d:q:r:n`.

2. Use BCDEdit to delete any existing IP address values in dbgsettings.

    ```console
    bcdedit -deletevalue {dbgsettings} hostip
    ```

3. Set the IPv6 address of the host. There must not be any spaces in the `hostipv6=s:t:u:v:w:x:y:z` string. \<YourPort> is the network port number to use for this target machine. \<YourKey> is the four part security key. \<b.d.f> are the bus device function location numbers for the NIC you want to use for KDNET.

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

5. On the host machine, use the following command to start the debugger:

    ```console
    Windbg -k net:port=<yournetworkportnumber>,key=<key_output_from_kdnet>,target=::<YourIPv6Address> 
    ```

6. When the debugger is running on the host machine and waiting to connect, reboot the target computer.

7. The debugger should connect to the host debugger early during boot. You can see that KDNET is using an IPv6 connection because the IP addresses reported in the connected message are IPv6 addresses instead of IPv4 addresses.

## Notes

- Every debugger bcd setting that allows the `hostip` to be specified has a corresponding `hostipv6` element. There are three.  

    IPv4 | IPv6 | Usage
    |-----------|-----------|-----------|
    hostip | hostipv6 | For boot and kernel debugging
    targethostip | targethostipv6  | Specific to kernel debugging  
    hypervisorhostip | hypervisorhostipv6  | For hyper-v debugging

- If you set the `hostipv6` style address for any of those kinds of debugging, it means you want and will get IPv6.

- If you set the `hostip` style address for any of those kinds of debugging, it means you want and will get IPv4.

- The target only will do IPv4 or IPv6, not both at the same time. The version of the IP protocol that's used is controlled by the target machine dbgsettings. If `hostip` is set, the target uses IPv4. If `hostipv6` is set, the target uses IPv6.

- The host debugger normally auto selects use of IPv4 or IPv6. By default, the debugger listens on both an IPv4 socket and an IPv6 socket, and connects automatically on either one to the target machine.

- If you want to force use of IPv6 in the debugger on the host, but you want the debugger to listen for a connection from the target, then you can add `target=::` to the debugger command line. `::` is an IPv6 address of 0.

- If you want to force IPv4 debugging in the debugger on the host, but you want the debugger to listen for a connection from the target, then you can add `target=0.0.0.0` to the debugger command line. `0.0.0.0` is an IPv4 address of 0.

- If you specify `target=` on the debugger command line and use a machine name, the debugger converts that machine name into an IPv4 address and an IPv6 address. The debugger then attempts to connect on both.

- When you specify `target=` on the debugger command line, and use an IP address, if the IP address contains any **:** characters, the debugger assumes it's an IPv6 address, and forces use of IPv6 for that connection. If the IP address contains any **.** characters, the debugger assumes it's an IPv4 address, and forces use of IPv4 for that connection.

- If you set up IPv6 on the target and force use of IPv4 on the debugger command line, you don't get a connection.

- If you set up IPv4 on the target and force use of IPv6 on the debugger command line, you also don't get a connection.

## See also

- [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md)

- [Supported Ethernet NICs for network kernel debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)

- [Supported Ethernet NICs for network kernel debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)
