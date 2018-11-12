---
title: Setting Up Network Debugging of a Virtual Machine with KDNET
description: This topic describes how to configure a kernel debugging connection to a Hyper-V virtual machine.
ms.assetid: E4C4D2A1-2FB0-4028-8A52-30B8F4F738D0
ms.author: domars
ms.date: 07/02/2018
ms.localizationpriority: medium
---

# Setting Up Network Debugging of a Virtual Machine - KDNET

This topic describes how to configure a kernel debugging connection to a Hyper-V virtual machine (VM).


## Hyper-V Virtual Machine Setup

To debug a Gen 2 Hyper-V Virtual Machine (VM) complete the following steps.

**1. Create a VM with Windows installed**

For information on how to create a VM, see [Create a Virtual Machine with Hyper-V](https://docs.microsoft.com/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine).

**2. Define an external virtual switch is defined** 

To communicate with the VM a virtual external network switch can be used. For information on how to create external network switch, see [Create a virtual network](https://docs.microsoft.com/virtualization/hyper-v-on-windows/quick-start/connect-to-network).

When the external network switch is configured the following options must be set.

|Option| Value|
|----------|----------|
| Connection Type | External Network|
| Allow management operating system to share this network adapter | Enabled |
| VLAN ID | Disabled |


**3. Disable Secure Boot**

To allow the kdnet utility to update BCDEdit boot settings, temporarily disable secure boot on the virtual machine by following these steps.

1. Load the Hyper-V manager and select the properties for your VM.

2. Click on the **Security** settings.

3. Un-check the **Enable Secure Boot** checkbox.

4. Click **OK** to save the settings.

You can re-enable Secure Boot once you’re done debugging and you’ve disabled kernel debugging on the target VM.  


**4. Install the Debugging Tools for Windows**

The debugging tools are used for the debugger and the kdnet utility and must be installed. For information on how to download and install the debugging tools, see [Download Debugging Tools for Windows](debugger-download-tools.md). 


## Setting Up Network Debugging of a Virtual Machine - KDNET

### Record the Host IP Address 

To run the host debugger on the same PC as the target virtual machine, follow these steps. 

1. In the host computer OS, open a Command Prompt window and enter *IPConfig* to display the IP configuration. 

2. In the command output, locate the Ethernet adapter that you configured as the External Virtual Switch.

    ```console
    ...

    Ethernet adapter vEthernet (External Virtual Switch):

    ...

    IPv4 Address. . . . . . . . . . . : <YourHostIPAddress>

    ...

    ```

3. Record the IPv4 address of the External Virtual Switch that will be used as the host address for debugging.

4. To confirm connectivity between the target and the host computer, open an elevated command prompt window on the target computer, and enter the following command, where *YourHostIPAddress* is the IP address of the host computer. 

    ```console
    ping -4 <YourHostIPAddress>
    ```


## <span id="Setting_Up_the_Target_Computer"></span><span id="setting_up_the_target_computer"></span><span id="SETTING_UP_THE_TARGET_COMPUTER"></span>Setting Up the VM Target Computer

Use the kdnet.exe utility to automatically configure the  debugger settings on the target PC,  by following these steps.

1. Locate the WDK *kdnet.exe* and *VerifiedNICList.xml* files. By default they are located here.

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64
```

> [!NOTE]
> These directions assumes that both PCs are running a 64 bit version of Windows on both the target and host. 
> If that is not the case, the best approach is to run the same "bitness" of tools on the host that the target is running. 
For example, if the target is running 32 bit Windows, run a 32 version of the debugger on the host. 
> For more information, see [Choosing the 32-Bit or 64-Bit Debugging Tools](choosing-a-32-bit-or-64-bit-debugger-package.md).
> 

4. To allow the long key that is used to be cut and pasted, enable enhanced session support. In the VM window, from the **View** pull down menu, enable *Enhanced session*. 

5. On the target VM computer, create a C:\KDNET directory and copy the *kdnet.exe* and *VerifiedNICList.xml* files to that directory.

6. On the target computer, open a Command Prompt window as Administrator. Enter this command to verify that the target computer has a supported network adapter.

    ```console
    C:\KDNET>kdnet

    Network debugging is supported on the following NICs:
    busparams=0.25.0, Intel(R) 82579LM Gigabit Network Connection, KDNET is running on this NIC.kdnet.exe
    ```

7. Type this command to set the IP address of the host system and generated a unique connection key. Use the IP address of the host system you recorded earlier.  Pick a unique port address for each target/host pair that you work with, with in the range 50000-50039. For this example, we will select 50005.

    ```console
    C:\>kdnet <YourIPAddress> <YourDebugPort> 

    Enabling network debugging on Microsoft Hypervisor Virtual Machine.
    Key=3u8smyv477z20.2owh9gl90gbxx.3sfsihzgq7di4.nh8ugnmzb4l7

    To debug this vm, run the following command on your debugger host machine.
    windbg -k net:port=50005,key=3u8smyv477z20.2owh9gl90gbxx.3sfsihzgq7di4.nh8ugnmzb4l7

    Then restart this VM by running shutdown -r -t 0 from this command prompt.
    ```

8. Use CRTL+C to copy the provided windbg output into the command buffer. Doing this avoids attempting to write down the long key value that is returned.

9. Re-enable BitLocker and secure boot when you're done configuring the debugger settings.

10. Because a VM with enhanced session support can timeout when it is left in a breakpoint, disable *Enhanced session* support using the **View** pull down menu in the VM. 

11. The VM will be restarted after the debugger is loaded and running. This process is described next. 


## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session


2. To connect to the target PC, use CTRL+V to paste in the main OS command window the windbg string that was returned by kdnet that you copied earlier.

    ```console
    C:\Debuggers\windbg -k net:port=<YourDebugPort>,key=<YourKey> 
    ```

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. You should respond to the prompt by checking the boxes for **all three** network types: domain, private, and public. 



## <span id="Restarting_Target"></span><span id="restarting_target"></span><span id="RESTARTING_TARGET"></span> Restarting the Target PC

Once the debugger is connected, reboot the target computer. To force the VM to completely restart, use this command, from an administrator's command prompt.

   ```console
   shutdown -r -t 0 
   ```

When the target virtual machine is restarted, the debugger in the host OS should connect. 

After connecting to the VM, hit break on your debugger and you can start debugging. 


## Troubleshooting KDNET Virtual Machine Network Debugging 

If the debugger does not connect, use the ping command from the target VM to verify connectivity. 

```console
C:\>Ping <HostComputerIPAddress> 
```

*Something didn't work right and I'm not sure what...* 

- Ensure you've let WinDbg through your firewall. 
- Confirm that you are using a unique Key that was generated by BCDEdit or kdnet.


*My VMs don't have network connectivity*  

- Open Virtual Switch Manager from Hyper-V Manager, select your existing Virtual Switch, and change the external network NIC to the Microsoft Kernel Debug Network Adapter by selecting it from the drop down box and then clicking OK in the Virtual Switch Manager dialog box.  After updating your Virtual Switch NIC, make sure to then shutdown and restart your VMs. 



## Sequence to add Hyper-V role to a Windows PC

If your target computer is a virtual machine host, you can set up network debugging and still have network access for the virtual machines.

Suppose you want to set up network debugging in the following situation.

-   The target computer has a single network interface card.
-   You intend to install the Hyper-V role on the target computer.
-   You intend to create one or more virtual machines on the target computer.

The best approach is to set up network debugging on the target computer before you install the Hyper-V role. Then the virtual machines will have access to the network.

If you decide to set up network debugging after the Hyper-V role has been installed on the target computer, you must change the network settings for your virtual machines to bridge them to the Microsoft Kernel Network Debug Adapter. Otherwise, the virtual machines will not have access to the network.


## <span id="related_topics"></span>Related topics

[Setting Up Kernel-Mode Debugging of a Virtual Machine Manually using a Virtual COM Port](attaching-to-a-virtual-machine--kernel-mode-.md)

[Setting Up a Network Connection Manually](setting-up-a-network-debugging-connection.md)

 

 






