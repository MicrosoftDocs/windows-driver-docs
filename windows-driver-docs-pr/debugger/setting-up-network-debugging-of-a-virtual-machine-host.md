---
title: Setting Up Network Debugging of a Virtual Machine with KDNET
description: This topic describes how to configure a kernel debugging connection to a Hyper-V virtual machine.
ms.assetid: E4C4D2A1-2FB0-4028-8A52-30B8F4F738D0
ms.author: domars
ms.date: 06/14/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up Network Debugging of a Virtual Machine - KDNET

This topic describes how to configure a kernel debugging connection to a Hyper-V virtual machine (VM).


## Hyper-V Virtual Machine Assumptions

This topic makes the following assumptions about how your Hyper-V virtual machine is configured.

**A Windows VM has been created and Windows is installed on the VM**

For information on how to create a VM, see [Create a Virtual Machine with Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine).


**An external virtual switch is defined** 

To communicate with the VM a virtual external network switch can be used. For information on how to create external network switch, see [Create a virtual network](https://docs.microsoft.com/virtualization/hyper-v-on-windows/quick-start/connect-to-network).


**Secure Boot is Disabled**

To allow the KDNET utility to update BCDEdit boot settings, temporarily disable secure boot on the virtual machine by following these steps.

1. Load the Hyper-V manager and select the properties for your VM.

2. Click on the **Security** settings.

3. Un-check the **Enable Secure Boot** checkbox.

4. Click **OK** to save the settings.

Re-enable secure boot after the BCDEdit setting have been configured by the KDNet utiltity.



## Setting Up Network Debugging of a Virtual Machine - KDNET


### Record the Host IP Address - Host Running on the same PC as the VM

To run the host debugger on the same PC as the target virtual machine, follow these steps. 

1. On the host computer, open a Command Prompt window and enter *IPConfig* to display the IP configuration. 

2. In the command output, locate the Ethernet adapter that you configured as the External Virtual Switch.

    ```
    ...

    Ethernet adapter vEthernet (External Virtual Switch):

    ...

    IPv4 Address. . . . . . . . . . . : <YourHostIPAddress>

    ...

    ```
3. Record the IPv4 address of the External Virtual Switch that will be used as the host address for debugging.

4. to confirm connectivty between the target and the host computer, open an elevated command prompt window on the target computer, and enter the following command, where *YourHostIPAddress* is the IP address of the host computer. 

    ```
    ping -4 <YourHostIPAddress>
    ```


### Record the Host IP Address - Host Running on a different PC as the VM

To run the host debugger on a different PC from the PC that is running the  target virtual machine, follow these steps.

1. On the host computer, open a Command Prompt window and enter *IPConfig* to display the IP configuration. 

2. In the command output, locate the Ethernet adapter.

    ```
    ...

    Ethernet adapter Ethernet:
    ...

   IPv4 Address. . . . . . . . . . . : <YourHostIPAddress>
    ...

    ```
3. Record the IPv4 address of the Ethernet adapter that will be used as the host address for debugging.

4. to confirm connectivty between the target and the host computer, open an elevated command prompt window on the target computer, and enter the following command, where *YourHostIPAddress* is the IP address of the host computer. 

    ```
    ping -4 <YourHostIPAddress>
    ```



## <span id="Setting_Up_the_Target_Computer"></span><span id="setting_up_the_target_computer"></span><span id="SETTING_UP_THE_TARGET_COMPUTER"></span>Setting Up the VM Target Computer

Use the KDNET.exe utility to automatically configure the  debugger settings on the target PC,  by following these steps.

1.  Confirm that the target PC is connected to a network hub or switch with an appropriate network cable. 

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

5. Type this command to set the IP address of the host system and generated a unique connection key. Use the IP address or the name of the host system, or the wildcard address of 255.255.255.255.  Pick a unique port address for each target/host pair that you work with, with in the range 50000-50039. Because we will be using a unique key and port address for each host and target pair, we can use the wildcard hostip address of 255.255.255.255.

    ```
    C:\>KDNet 255.255.255.255 <YourDebugPort> 

    Enabling network debugging on Microsoft Hypervisor Virtual Machine.
    Key=3u8smyv477z20.2owh9gl90gbxx.3sfsihzgq7di4.nh8ugnmzb4l7

    To debug this vm, run the following command on your debugger host machine.
    windbg -k net:port=<YourDebugPort>,key=3u8smyv477z20.2owh9gl90gbxx.3sfsihzgq7di4.nh8ugnmzb4l7

    Then restart this VM by running shutdown -r -t 0 from this command prompt.
    ```

6. Re-enable BitLocker and secure boot when you're done configuring the debugger settings.


7. The VM will be restarted after the debugger is loaded and running. 


## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session

1. Record the returned windbg command line, or copy it into a notepad .txt file or the command buffer.

2. To connect to the target PC use the following in the non-virtual machine command window, where \<YourDebugPort\> is the port you selected above between 50000-50039, and \<YourKey\> is the unique key that was returned by KDNet above.

    ```
    C:\Debuggers\windbg -k net:port=<YourDebugPort>,key=<YourKey> 
    ```

When you first attempt to establish a network debugging connection, you might be prompted to allow the debugging application (WinDbg or KD) access through the firewall. You should respond to the prompt by checking the boxes for **all three** network types: domain, private, and public. 

3. Once the debugger is connected, reboot the target virtual machine and the debugger in the host OS should connect during the reboot. 

4. After connecting to your VM, hit break on your debugger and you can start debugging. 

5. If the debugger does not connect, use the ping command to verify connectivity, and then refer to the troubleshooting steps below. 

    ```
    C:\>Ping <HostComputerIPAddress> 
    ```



## Troubleshooting KDNET Virtual Machine Network Debugging 

*Something didn't work right and I'm not sure what...* 

- Ensure you've let WinDbg through your firewall. 
- Confirm that you are using a unique Key that was generated by BCDEdit or KDNet.
- Consider trying a different hub/router. 

*Everything was working fine and now it's not working* 

- Sometimes the routers/switch/hubs can get stuck. Unplug the power to router/switch/hub for ~60 seconds and then plug back in and reboot target machine. This fixes a number of issues and may need to to happen from time to time. 

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

 

 






