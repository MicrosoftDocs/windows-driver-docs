---
ms.assetid: D92A4E42-82F0-4034-B208-66E04F6EAB26
title: Troubleshooting Driver Deployment, Testing and Debugging
description: Provides troubleshooting tips for provisioning Visual Studio for driver deployment.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting Configuration of Driver Deployment, Testing and Debugging

Provisioning a target computer is described in [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909). Here we give some troubleshooting tips for the provisioning process.

## <span id="General_tips"></span><span id="general_tips"></span><span id="GENERAL_TIPS"></span>General tips


-   [Configure Computers menu command is inactive](#configure_computers_menu_command_is_inactive)
-   [Provisioning fails](#provisioning_fails_general_tips)

## <span id="Provisioning_fails"></span><span id="provisioning_fails"></span><span id="PROVISIONING_FAILS"></span>Provisioning fails


-   [The network path was not found](#domain_the_network_path_was_not_found)
-   [The network name cannot be found](#domain_the_network_name_cannot_be_found)
-   [Could not access remote machine](#domain_could_not_access_remote_machine)

## <span id="Debugger_won_t_connect_or_break_in"></span><span id="debugger_won_t_connect_or_break_in"></span><span id="DEBUGGER_WON_T_CONNECT_OR_BREAK_IN"></span>Debugger won't connect or break in


-   [Debugger network connection](#debugger_wont_connect_network)
-   [Debugger 1394 connection](#debugger_wont_connect_1394)
-   [Debugger serial connection](#debugger_wont_connect_serial)

## <span id="configure_computers_menu_command_is_inactive"></span><span id="CONFIGURE_COMPUTERS_MENU_COMMAND_IS_INACTIVE"></span>Configure Computers menu command is inactive


When you first start Microsoft Visual Studio, the **Test &gt; Configure Computers** command on the **Driver** menu might be inactive (greyed out). If you wait about 20 seconds, and then click the **Driver** menu again, the **Test &gt; Configure Computers** command will be available.

## <span id="provisioning_fails_general_tips"></span><span id="PROVISIONING_FAILS_GENERAL_TIPS"></span>Provisioning fails: General tips


If provisioning fails, read the sequence of messages in the Computer Configuration window. Typically, this window also displays the location of the configuration log. View the log and make a note of its location so you can refer to it later.

The path to the log might contain a hidden folder. For example, in the following path, AppData is a hidden folder.

C:\\Users\\*currentUser*\\AppData\\Roaming\\Microsoft\\DriverTest\\Install

The log file will have a name similar to this:

Driver Test Computer Configuration 20121115130459167.log

## <span id="domain_the_network_path_was_not_found"></span><span id="DOMAIN_THE_NETWORK_PATH_WAS_NOT_FOUND"></span>Provisioning fails: The network path was not found


When you start to provision a target computer, you might see a message that says **The network path was not found**.

On the target computer, make sure that you have turned on **Network Discovery** and that you have turned on **File and Printer Sharing** for the appropriate network profile. For example, if the host and target computers are joined to a network domain, you must turn on network discovery and file and printer sharing for the **Domain** network profile. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909).

Make sure you can ping the target computer from the host computer. On the host computer, open a Command Prompt window, and enter **ping** *targetComputerName*, where *targetComputerName* is the name of the target computer.

**Note**  
You might see several messages before you see the message **The network path was not found**. Some of those messages might make you think that the network path was found and the first steps of provisioning were succeeding. In fact, the network path was not found and no portion of provisioning succeeded. For example, you might see this:

 

```cpp
Connecting to computer "MyComputer"
Installing driver test automation service
Getting computer system information
Copying driver test automation files
The network path was not found.
```

## <span id="domain_the_network_name_cannot_be_found"></span><span id="DOMAIN_THE_NETWORK_NAME_CANNOT_BE_FOUND"></span>Provisioning fails: The network name cannot be found


When you start to provision a target computer, you might see a message that says **The network name cannot be found**. Double check the name of the target computer. If the computer name you entered originally was incorrect, start the provisioning wizard again (**Driver &gt; Test &gt; Configure Computers)**. Select the incorrect computer name, and click **Next**. For **Computer name**, enter the correct name of the target computer, and complete the wizard.

**Note**  
You might see several messages before you see the message **The network name cannot be found**. Some of those messages might make you think that the computer name was found and the first steps of provisioning were succeeding. In fact, the computer name was not found, and no portion of provisioning succeeded. For example, you might see this:

 

```cpp
Connecting to computer "NonExistentComputer"
Installing driver test automation service
Getting computer system information
Copying driver test automation files
The network name cannot be found.
```

**Note**  
The messages that are displayed when you enter an incorrect target computer name can vary. For example, you might see a message about enabling network discovery.

 

```cpp
Connecting to computer "NonExistentComputer"
Installing driver test automation service
Could not access remote machine "NonExistentComputer" over the network. 
Error:53. Automatic configuration of machines over the network requires
that network discovery and file and print sharing be enabled on the 
target machine.
```

Or you might be prompted to enter credentials.

```cpp
Enter your password to connect to: NonExistentComputer
```

## <span id="domain_could_not_access_remote_machine"></span><span id="DOMAIN_COULD_NOT_ACCESS_REMOTE_MACHINE"></span>Provisioning fails: Could not access remote machine


When you start to provision a target computer, you might see a message that says **Could not access the remote machine** "*computerName*" **over the network**. This message can be displayed for several reasons. Verify that your host and target computers are both joined to the same domain or the same workgroup. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909). Verify that you entered the correct name for the target computer. Verify that you have enabled network discovery and file and print sharing on the target computer.

## Debugger breakpoints are not triggered for kernel-mode driver


1. Deploy the driver with breakpoints disabled. 
2. Manually break into the kernel-mode debugger. 
3. Set an exception on load of the module:
   ```cpp
   sxe ld <DriverName>
   ``` 
4. Enable the breakpoint and resume execution. 
5. On the target computer, disable the device node and then re-enable it. 

## <span id="debugger_wont_connect_network"></span><span id="DEBUGGER_WONT_CONNECT_NETWORK"></span>Debugger won't connect or break in: Network connection


Verify that your debugging application is allowed through the firewall for all network types.

Check with network administrator about ports that allow network debugging.

If the target computer has more than one network adapter, you must specify the bus parameters of the network adapter that you intend to use for debugging.

For more information, see [Troubleshooting Tips for Debugging over a Network Cable](https://msdn.microsoft.com/library/windows/hardware/hh439346)

## <span id="debugger_wont_connect_1394"></span><span id="DEBUGGER_WONT_CONNECT_1394"></span>Debugger won't connect or break in: 1394 connection


If the target computer has more than one 1394 controller, you must specify the bus parameters of the 1394 controller that you intend to use for debugging. For more information, see [Troubleshooting Tips for Debugging over a 1394 Cable](https://msdn.microsoft.com/library/windows/hardware/ff556866).

## <span id="debugger_wont_connect_serial"></span><span id="DEBUGGER_WONT_CONNECT_SERIAL"></span>Debugger won't connect or break in : Serial connection


Check the COM port numbers on the host and target computer. Verify that you have configured the same baud rate for debugging on both the host and target computers. For more information, see [Troubleshooting Tips for Debugging over a Serial Cable](https://msdn.microsoft.com/windows/hardware/hh439359)

 

 





