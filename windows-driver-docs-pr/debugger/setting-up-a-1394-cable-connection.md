---
title: Setting Up Kernel-Mode Debugging over a 1394 Cable Manually
description: Debugging Tools for Windows supports kernel debugging over a 1394 (Firewire) cable. This topic describes how to set up 1394 debugging manually.
ms.assetid: bcfc61a1-0315-451c-a279-f6305995b05f
keywords: making a 1394 cable connection, 1394 connection, IEEE 1394 cable, FireWire cable
ms.author: domars
ms.date: 05/03/2018
ms.localizationpriority: medium
---

# Setting Up Kernel-Mode Debugging over a 1394 Cable Manually

> [!IMPORTANT]
> The 1394 transport is available for use in Windows 10, version 1607 and earlier. 
> It is not available in later versions of Windows. You should transition your projects to other transports, such as KDNET using Ethernet. 
> For more information about that transport, see [Setting Up Kernel-Mode Debugging over a Network Cable Manually](setting-up-a-network-debugging-connection.md).
>

Debugging Tools for Windows supports kernel debugging over a 1394 (Firewire) cable. This topic describes how to set up 1394 debugging manually.

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. The host and target computers must each have a 1394 adapter and must be running Windows XP or later. The host and target computers do not have to be running the same version of Windows.

## <span id="Setting_Up_the_Target_Computer"></span><span id="setting_up_the_target_computer"></span><span id="SETTING_UP_THE_TARGET_COMPUTER"></span>Setting Up the Target Computer


1.  Connect a 1394 cable to the 1394 controllers that you have chosen for debugging on the host and target computers.

> [!IMPORTANT]
> Before using BCDEdit to change boot information you may need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC.
> Re-enable these security features when testing is complete and appropriately manage the test PC, when the security features are disabled.

2. In an elevated Command Prompt window, enter the following commands, where *n* is a channel number of your choice, from 0 through 62:

   **bcdedit /debug on**

   **bcdedit /dbgsettings 1394 channel:**<em>n</em>

3. If there is more than one 1394 controller on the target computer, you must specify the bus, device, and function numbers of the 1394 controller that you intend to use for debugging. For more information, see [Troubleshooting Tips for 1394 Debugging](#troubleshooting-tips-for-debugging-over-a-1394-cable).

4. Do not reboot the target computer yet.

## <span id="Starting_a_Debugging_Session_for_the_First_Time"></span><span id="starting_a_debugging_session_for_the_first_time"></span><span id="STARTING_A_DEBUGGING_SESSION_FOR_THE_FIRST_TIME"></span>Starting a Debugging Session for the First Time


1.  Determine the bitness (32-bit or 64-bit) of Windows running on the host computer.
2.  On the host computer, open a version of WinDbg (as Administrator) that matches the bitness of Windows running on the host computer. For example, if the host computer is running a 64-bit version of Windows, open the 64-bit version of WinDbg as Administrator.
3.  On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **1394** tab. Enter your channel number, and click **OK**.

    At this point, the 1394 debug driver gets installed on the host computer. This is why it is important to match the bitness of WinDbg to the bitness of Windows. After the 1394 debug driver is installed, you can use either the 32-bit or 64-bit version of WinDbg for subsequent debugging sessions.

4.  Reboot the target computer.

## <span id="Starting_a_Debugging_Session"></span><span id="starting_a_debugging_session"></span><span id="STARTING_A_DEBUGGING_SESSION"></span>Starting a Debugging Session


### <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

- On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **1394** tab. Enter your channel number, and click **OK**.

  You can also start a session with WinDbg by entering the following command in a Command Prompt window, where *n* is your channel number:

  **windbg /k 1394:channel=**<em>n</em>

### <span id="Using_KD"></span><span id="using_kd"></span><span id="USING_KD"></span>Using KD

- On the host computer, open a Command Prompt window and enter the following command, where *n* is your channel number:

  **kd /k 1394:channel=**<em>n</em>

## <span id="Using_Environment_Variables"></span><span id="using_environment_variables"></span><span id="USING_ENVIRONMENT_VARIABLES"></span>Using Environment Variables


On the host computer, you can use environment variables to specify the 1394 channel. Then you do not have to specify the channel each time you start a debugging session. To use environment variables to specify the 1394 channel, open a Command Prompt window and enter the following commands, where *n* is your channel number:

- **set \_NT\_DEBUG\_BUS=1394**
- **set \_NT\_DEBUG\_1394\_CHANNEL=**<em>n</em>

To start a debugging session, open a Command Prompt window and enter one of the following commands:

-   **kd**
-   **windbg**

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For complete documentation of the **bcdedit** command and the boot.ini file, see Boot Options for Driver Testing and Debugging in the Windows Driver Kit (WDK) documentation.

## <span id="troubleshooting-tips-for-debugging-over-a-1394-cable"></span><span id="TROUBLESHOOTING-TIPS-FOR-DEBUGGING-OVER-A-1394-CABLE"></span>Troubleshooting Tips for Debugging over a 1394 Cable


Most 1394 debugging problems are caused by using multiple 1394 controllers in either the host or target computer. Using multiple 1394 controllers in the host computer is not supported. The 1394 debug driver, which runs on the host, can communicate only with the first 1394 controller enumerated in the registry. If you have a 1394 controller built into the motherboard and a separate 1394 card, either remove the card or disable the built-in controller in the BIOS settings of the computer.

The target computer can have multiple 1394 controllers, although this is not recommended. If your target computer has a 1394 controller on the motherboard, use that controller for debugging, if possible. If there is an additional 1394 card, you should remove the card and use the onboard controller. Another solution is to disable the onboard 1394 controller in the BIOS settings of the computer.

If you decide to have multiple 1394 controllers enabled on the target computer, you must specify bus parameters so that the debugger knows which controller to claim for debugging. To specify the bus parameters, Open Device Manager on the target computer, and locate the 1394 controller that you want to use for debugging. Open the property page for the controller, and make a note of the bus number, device number, and function number. In an elevated Command Prompt Window, enter the following command, where *b*, *d*, and *f* are the bus, device and function numbers in decimal format:

**bcdedit -set "{dbgsettings}" busparams** <em>b</em>**.**<em>d</em>**.**<em>f</em>.

Reboot the target computer.

## <span id="related_topics"></span>Related topics


[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

 

 






