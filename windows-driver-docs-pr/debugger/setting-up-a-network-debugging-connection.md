---
title: Set Up KDNET Network Kernel Debugging Manually
description: Learn how to set up KDNET network kernel debugging manually using Debugging Tools for Windows. Configure host and target computers for network debugging.
keywords: ["Network debugging", "Ethernet debugging", "Docking station", "Setting Up Kernel-Mode Debugging over a Network Cable Manually"]
ms.date: 11/05/2025
ms.topic: how-to
---

# Set up KDNET network kernel debugging manually

This article shows you how to set up KDNET network kernel debugging manually by using Debugging Tools for Windows. You configure both host and target computers to enable network debugging.

> [!IMPORTANT]
> Manual network debugging setup is complex and error-prone.
> **For most scenarios, use the automatic setup instead:** [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md). The KDNET utility is strongly recommended.

What you learn:

- How to configure host and target computers for network debugging
- How to establish and troubleshoot debugging connections
- When to use IPv6 vs IPv4 for debugging

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. The host computer must run Windows 7 or later, and the target computer must run Windows 8 or later.

Debugging over a network has the following advantages compared to debugging over other types of connectivity.

- The host and target computers can be anywhere on the local network.
- It's easy to debug many target computers from one host computer.
- Given any two computers, it's likely that they both have Ethernet adapters. It's less likely that they both have serial ports or 1394 ports.
- Network debugging is faster than serial port debugging.

## Supported network adapters

**Host computer:** Any network adapter works.

**Target computer:** Must use a supported network adapter. Check your Windows version:

- [Supported adapters for Windows 11](supported-ethernet-nics-for-network-kernel-debugging-in-windows-11.md)
- [Supported adapters for Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)
- [Supported adapters for Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

## Install Debugging Tools for Windows

Confirm that the Debugging Tools for Windows are installed on the host system. For information on downloading and installing the debugger tools, see [Debugging Tools for Windows](debugger-download-tools.md).

## Determine the IP address of the host computer

Use one of the following procedures to determine the IP address of the host computer.

1. On the host computer, open a command prompt and enter the following command:

   ```console
   ipconfig
   ```

    Make a note of the IPv4 address of the network adapter that you intend to use for debugging.

1. On the target computer, open a command prompt and enter the following command, where *YourIPAddress* is the IP address of the host computer:

   ```console
   ping -4 <YourIPAddress>
   ```

## Choose a port for network debugging

**Recommended port range:** 50000-50039

You can use any port from 49152-65535, but the recommended range provides the best compatibility. The debugger uses this port exclusively, so make sure no other applications use it.

### Important considerations

- Corporate firewalls might restrict port ranges. Check with your network administrator.
- Each target computer needs a unique port (for example: 50000, 50001, 50002).
- Different host computers can reuse the same port range.

> [!NOTE]
> Your company's network policy might limit available ports. Check with your network administrators if you encounter connection issues.

If you connect several target computers to a single host computer, each connection must have a unique port number. For example, if you connect 100 target computers to a single host computer, you can assign port 50000 to the first connection, port 50001 to the second connection, and so on.

> [!NOTE]
> A different host computer can use the same range of ports (50000 through 50099) to connect to another 100 target computers.

## Set up the target computer

1. Verify that the target computer has a supported network adapter. For more information, see:

    - [Supported Ethernet NICs for network kernel debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

    - [Supported Ethernet NICs for network kernel debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)

1. Connect the supported adapter to a network hub or switch by using an appropriate network cable.

> [!IMPORTANT]
> Before using BCDEdit to change boot information, you might need to temporarily suspend Windows security features, such as BitLocker and Secure Boot, on the test PC.
> Re-enable these security features when testing is complete, and appropriately manage the test PC when the security features are disabled.

1. In an elevated command prompt, enter the following commands. Replace *w.x.y.z* with your host computer's IP address and *n* with your chosen port number:

    ```console
    bcdedit /debug on
    bcdedit /dbgsettings net hostip:w.x.y.z port:n
    ```

    For example:

    ```console
    bcdedit /debug on
    bcdedit /dbgsettings net hostip:192.168.1.100 port:50000
    ```

1. BCDEdit displays an automatically generated key. Copy the key and store it on a removable storage device, like a USB flash drive. You need the key when you start a debugging session on the host computer.

1. Use Device Manager to determine the PCI bus, device, and function numbers for the adapter you want to use for debugging. These values are displayed in Device Manager under *Location* on the *General* tab. Then in an elevated command prompt, enter the following command, where *b*, *d*, and *f* are the bus number, device number, and function number of the adapter:

    ```console
    bcdedit /set "{dbgsettings}" busparams b.d.f
    ```

1. The target PC is rebooted after a kernel debugger is attached.

> [!NOTE]
> If you intend to install the Hyper-V role on the target computer, see [Setting up network debugging of a virtual machine host](setting-up-network-debugging-of-a-virtual-machine-host.md).

> [!CAUTION] 
> If your target computer is in a docking station and you enable network debugging for a network adapter that's part of the docking station, don't remove the computer from the docking station. If you need to remove the target computer from the docking station, disable kernel debugging first. To disable kernel debugging on the target computer, open a command prompt as an administrator and enter the command `bcdedit /debug off`. Reboot the target computer.

## Start the debugging session

**Before you begin:** Ensure your host computer's network adapter is connected to a network hub or switch.

### Option 1: Use WinDbg (GUI)

1. Open WinDbg on the host computer.
1. Select **File** > **Kernel Debug**.
1. Open the **Net** tab.
1. Enter your port number and key.
1. Select **OK**.

### Option 2: Use WinDbg (Command line)

You can also start a session with WinDbg by opening a command prompt and entering the following command, where *n* is your port number and *MyKey* is the key that BCDEdit automatically generated when you set up the target computer:

```console
windbg -k net:port=<n>,key=<MyKey>
```

If you're prompted to allow WinDbg to access the port through the firewall, allow WinDbg to access the port for **all three** of the different network types.

### Use KD

On the host computer, open a command prompt. Enter the following command, where *n* is your port number and *MyKey* is the key that BCDEdit automatically generated when you set up the target computer:

```console
kd -k net:port=<n>,key=<MyKey>
```

If you're prompted about allowing WinDbg to access the port through the firewall, allow WinDbg to access the port for **all three** of the different network types.

## Restart the target PC

When the debugger connects and waits, reboot the target computer. One way to restart the PC is to use this command from an administrator's command prompt:

   ```console
   shutdown -r -t 0
   ```

When the target restarts, the debugger in the host OS connects.

After connecting to the target on the host, select break on your debugger and you can start debugging.

### Allow the debugger through the firewall

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. Client versions of Windows display the prompt, but server versions of Windows don't display the prompt. Respond to the prompt by checking the boxes for **all three** network types: domain, private, and public. 

If you don't get the prompt or if you didn't check the boxes when the prompt was available, use the Control Panel to allow access through the firewall on the host PC where the debugger is running. Open **Control Panel > System and Security** and select **Allow an app through Windows Firewall**.

- (WinDbg) In the list of applications, locate *WinDbg engine process (TCP) (all)*.

- (Classic WinDbg) In the list of applications, locate *Windows GUI Symbolic Debugger* and *Windows Kernel Debugger*.

Use the checkboxes to allow those applications through the firewall. Restart your debugging application (WinDbg or KD).

## Encryption key

To keep the target computer secure, packets that travel between the host and target computers must be encrypted. Use an automatically generated encryption key (provided by BCDEdit when you configure the target computer). An automatically generated encryption key is more secure and provides a unique value that you use to establish the connection to a specific target. 

Network debugging uses a 256-bit key that's specified as four 64-bit values, in base 36, separated by periods. Each 64-bit value is specified by using up to 13 characters. Valid characters are the letters *a* through *z* and the digits 0 through 9. Special characters aren't allowed.

To specify your own key, open an elevated command prompt on the target computer. Enter the following command, where `w.x.y.z` is the IP address of the host computer, *n* is your port number, and *Key* is your key:

```console
bcdedit /dbgsettings net hostip:w.x.y.z port:n key:Key
```

The target computer needs to be rebooted anytime you change the *dbgsettings*.

## Troubleshooting tips

### Allow the debugging application through firewalls

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. Client versions of Windows display the prompt, but server versions of Windows don't display the prompt. Respond to the prompt by checking the boxes for **all three** network types: domain, private, and public. 

If you don't get the prompt or if you didn't check the boxes when the prompt was available, you must use the Control Panel to allow access through the firewall. Open **Control Panel > System and Security** and select **Allow an app through Windows Firewall**. 

- (WinDbg) In the list of applications, locate *WinDbg engine process (TCP) (all)*.

- (WinDbg (Classic)) In the list of applications, locate *Windows GUI Symbolic Debugger* and *Windows Kernel Debugger*.

Use the checkboxes to allow those applications through the firewall. Scroll down and select **OK** to save the firewall changes. Restart the debugger.

### The port number must be in the range allowed by network policy

Your company's network policy might limit the range of port numbers you can use for network debugging. To find out if your company's policy limits the range of ports for network debugging, check with your network administrator. On the target computer, open a command prompt as an administrator and enter the command `bcdedit /dbgsettings`. The output is similar to the following example:

```console
C:\> bcdedit /dbgsettings
key                     XXXXXX.XXXXX.XXXXX.XXXXX
debugtype               NET
hostip                  169.168.1.1
port                    50085
dhcp                    Yes
The operation completed successfully.
```

In the preceding output, the value of the port is 50085. If the port value is outside the range allowed by your network administrator, enter the following command. The value *w.x.y.z* is the IP address of the host computer, and *YourDebugPort* is a port number in the allowed range.

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
> This method might not work if your host computer isn't configured to be discoverable on the network since the firewall might block ping requests. If the firewall blocks ping requests, you don't get any responses when you ping the host.

### How the debugger obtains an IP address for the target computer

KDNET on the target computer tries to use Dynamic Host Configuration Protocol (DHCP) to get a routable IP address for the network adapter that's used for debugging. If KDNET gets a DHCP-assigned address, then host computers anywhere on the network can debug the target computer. If KDNET can't get a DHCP-assigned address, it uses Automatic Private IP Addressing (APIPA) to get a local link IP address. Local link IP addresses aren't routable, so a host and target can't use a local link IP address to communicate through a router. In that case, network debugging works if you plug the host and target computers into the same network hub or switch.

### Always specify busparams when setting up KDNET on a physical machine with a PCI based NIC

If you're setting up KDNET on a physical machine with a PCI or PCIe-based NIC, always specify the busparams for the NIC you want to use for KDNET. To specify the bus parameters, open Device Manager, and locate the network adapter that you want to use for debugging. Open the property page for the network adapter and make a note of the bus number, device number, and function number that appears under *Location* on the *General* tab. In an elevated command prompt, enter the following command, where *b*, *d*, and *f* are the bus, device, and function numbers in decimal format:

```console
bcdedit /set "{dbgsettings}" busparams b.d.f
```

When the debugger is running on the host machine and waiting to connect, reboot the target computer by using the following command:

```console
shutdown -r -t 0
```

## Manually delete BCDEdit entries

You don't usually need to manually delete BCDEdit entries. However, you can use this procedure to troubleshoot unusual situations.

You don't need to manually delete entries when you use the kdnet utility. For more information, see [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md).

When you use `bcdedit –deletevalue`, you must provide a valid bcd element name. For more information, see [BCDEdit /deletevalue](../devtest/bcdedit--deletevalue.md).

To manually delete bcdedit entries, complete the following steps:

1. On the target computer, open a command prompt as an administrator.

1. As an example, enter the following command to delete the BCDEdit debugging entry for the host IP address:

    ```console
    bcdedit -deletevalue {dbgsettings} hostip
    ```

When you delete the hostip, you need to specify *target=* on the debugger command line.

1. As another example, delete the port entry by using the following command:

    ```console
    bcdedit -deletevalue {dbgsettings} port
    ```

When you delete the port entry, KDNET uses the default ICANN-registered debugger port of 5364.

## Set up Hyper-V

If you want to install the Hyper-V role on the target computer, see [Setting up network debugging of a virtual machine host](setting-up-network-debugging-of-a-virtual-machine-host.md).

For information on debugging a Hyper-V Virtual Machine (VM), see [Setting up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md).

## Enable KDNET on a Hyper-V host that's running VMs with external network connectivity

Sometimes a situation occurs that causes networking in VMs to stop working:

- You enable Hyper-V on the PC, create an external networking switch that points to a physical NIC in the machine, and configure VMs to use that external switch for their networking.

- You enable KDNET on the Hyper-V host OS by using the same physical NIC that the external networking switch points to. You reboot the host.

- All of the VMs that use the previously configured external switch lose their network connectivity after the reboot.

This stoppage is by design. KDNET takes exclusive control over the NIC it's configured to use. The OS doesn't load the native NDIS miniport for that NIC. The external networking switch can no longer communicate with the native NDIS miniport driver and stops working. To work around this situation, complete the following steps:

1. Open the Virtual Switch Manager from Hyper-V Manager, and select your existing Virtual Switch. Change the external network NIC to the *Microsoft Kernel Debug Network Adapter* by selecting it from the dropdown menu and then selecting **OK** in the Virtual Switch Manager dialog.

1. After you update your Virtual Switch NIC, shut down and restart your VMs.

When you turn off KDNET debugging, follow the same procedure to repoint the external switch back to the native NDIS miniport for the NIC. Otherwise, VM connectivity is lost when you reboot the machine after debugging is disabled.

## IPv6

Windows version 1809 adds support for IPv6.

To use IPv6 with the debugger, complete the following steps:

1. Ping your \<debughostname> and note the IPv6 address that's reported on the reply from output lines. Use this IPv6 address in place of `x:y:z:p:d:q:r:n`.

1. Use BCDEdit to delete any existing IP address values in dbgsettings.

    ```console
    bcdedit -deletevalue {dbgsettings} hostip
    ```

1. Set the IPv6 address of the host. The `hostipv6=s:t:u:v:w:x:y:z` string can't contain any spaces. \<YourPort> is the network port number to use for this target machine. \<YourKey> is the four-part security key. \<b.d.f> are the bus device function location numbers for the NIC you want to use for KDNET.

    ```console
    bcdedit /dbgsettings net hostipv6:s:t:u:v:w:x:y:z port:<YourPort> key:<YourKey> busparams:<b.d.f>
    ```

1. Type this command to confirm that the dbgsettings are set properly.

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

1. On the host machine, use the following command to start the debugger:

    ```console
    Windbg -k net:port=<yournetworkportnumber>,key=<key_output_from_kdnet>,target=::<YourIPv6Address> 
    ```

1. When the debugger is running on the host machine and waiting to connect, reboot the target computer.

1. The debugger connects to the host debugger early during boot. You can see that KDNET uses an IPv6 connection because the IP addresses reported in the connected message are IPv6 addresses instead of IPv4 addresses.

## Notes

- Every debugger bcd setting that allows you to specify the `hostip` has a corresponding `hostipv6` element. There are three pairs.

| IPv4 | IPv6 | Usage |
|-----------|-----------|-----------|
| hostip | hostipv6 | For boot and kernel debugging |
| targethostip | targethostipv6 | Specific to kernel debugging |
| hypervisorhostip | hypervisorhostipv6 | For Hyper-V debugging |

- If you set the `hostipv6` style address for any of those kinds of debugging, you get IPv6.

- If you set the `hostip` style address for any of those kinds of debugging, you get IPv4.

- The target only does IPv4 or IPv6, not both at the same time. The version of the IP protocol that's used is controlled by the target machine dbgsettings. If you set `hostip`, the target uses IPv4. If you set `hostipv6`, the target uses IPv6.

- The host debugger normally auto-selects the use of IPv4 or IPv6. By default, the debugger listens on both an IPv4 socket and an IPv6 socket and connects automatically on either one to the target machine.

- If you want to force the use of IPv6 in the debugger on the host, but you want the debugger to listen for a connection from the target, then you can add `target=::` to the debugger command line. `::` is an IPv6 address of 0.

- If you want to force IPv4 debugging in the debugger on the host, but you want the debugger to listen for a connection from the target, then you can add `target=0.0.0.0` to the debugger command line. `0.0.0.0` is an IPv4 address of 0.

- If you specify `target=` on the debugger command line and use a machine name, the debugger converts that machine name into an IPv4 address and an IPv6 address. The debugger then attempts to connect on both.

- When you specify `target=` on the debugger command line and use an IP address, if the IP address contains any **:** characters, the debugger assumes it's an IPv6 address, and forces the use of IPv6 for that connection. If the IP address contains any **.** characters, the debugger assumes it's an IPv4 address, and forces the use of IPv4 for that connection.

- If you set up IPv6 on the target and force use of IPv4 on the debugger command line, you don't get a connection.

- If you set up IPv4 on the target and force use of IPv6 on the debugger command line, you also don't get a connection.

## Related content

- [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md)

- [Setting up network debugging of a virtual machine host](setting-up-network-debugging-of-a-virtual-machine-host.md)

- [Setting up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md)

- [Supported Ethernet NICs for network kernel debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)

- [Supported Ethernet NICs for network kernel debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)


