---
title: Setting Up Kernel-Mode Debugging over a 1394 Cable Manually
description: Debugging Tools for Windows supports kernel debugging over a 1394 (Firewire) cable. This topic describes how to set up 1394 debugging manually.
ms.assetid: bcfc61a1-0315-451c-a279-f6305995b05f
keywords: making a 1394 cable connection, 1394 connection, IEEE 1394 cable, FireWire cable
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up Kernel-Mode Debugging over a 1394 Cable Manually


Debugging Tools for Windows supports kernel debugging over a 1394 (Firewire) cable. This topic describes how to set up 1394 debugging manually.

As an alternative to setting up 1394 debugging manually, you can do the setup using Microsoft Visual Studio. For more information, see [Setting Up Kernel-Mode Debugging over a 1394 Cable in Visual Studio](setting-up-a-1394-cable-connection-in-visual-studio.md).

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. The host and target computers must each have a 1394 adapter and must be running Windows XP or later. The host and target computers do not have to be running the same version of Windows.

## <span id="Setting_Up_the_Target_Computer"></span><span id="setting_up_the_target_computer"></span><span id="SETTING_UP_THE_TARGET_COMPUTER"></span>Setting Up the Target Computer


1.  Connect a 1394 cable to the 1394 controllers that you have chosen for debugging on the host and target computers.
2.  In an elevated Command Prompt window, enter the following commands, where *n* is a channel number of your choice, from 0 through 62:

    **bcdedit /debug on**

    **bcdedit /dbgsettings 1394 channel:***n*

3.  If there is more than one 1394 controller on the target computer, you must specify the bus, device, and function numbers of the 1394 controller that you intend to use for debugging. For more information, see [Troubleshooting Tips for 1394 Debugging](#troubleshooting-tips-for-debugging-over-a-1394-cable).

4.  Do not reboot the target computer yet.

## <span id="Starting_a_Debugging_Session_for_the_First_Time"></span><span id="starting_a_debugging_session_for_the_first_time"></span><span id="STARTING_A_DEBUGGING_SESSION_FOR_THE_FIRST_TIME"></span>Starting a Debugging Session for the First Time


1.  Determine the bitness (32-bit or 64-bit) of Windows running on the host computer.
2.  On the host computer, open a version of WinDbg (as Administrator) that matches the bitness of Windows running on the host computer. For example, if the host computer is running a 64-bit version of Windows, open the 64-bit version of WinDbg as Administrator.
3.  On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **1394** tab. Enter your channel number, and click **OK**.

    At this point, the 1394 debug driver gets installed on the host computer. This is why it is important to match the bitness of WinDbg to the bitness of Windows. After the 1394 debug driver is installed, you can use either the 32-bit or 64-bit version of WinDbg for subsequent debugging sessions.

4.  Reboot the target computer.

## <span id="Starting_a_Debugging_Session"></span><span id="starting_a_debugging_session"></span><span id="STARTING_A_DEBUGGING_SESSION"></span>Starting a Debugging Session


### <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

-   On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **1394** tab. Enter your channel number, and click **OK**.

    You can also start a session with WinDbg by entering the following command in a Command Prompt window, where *n* is your channel number:

    **windbg /k 1394:channel=***n*

### <span id="Using_KD"></span><span id="using_kd"></span><span id="USING_KD"></span>Using KD

-   On the host computer, open a Command Prompt window and enter the following command, where *n* is your channel number:

    **kd /k 1394:channel=***n*

## <span id="Using_Environment_Variables"></span><span id="using_environment_variables"></span><span id="USING_ENVIRONMENT_VARIABLES"></span>Using Environment Variables


On the host computer, you can use environment variables to specify the 1394 channel. Then you do not have to specify the channel each time you start a debugging session. To use environment variables to specify the 1394 channel, open a Command Prompt window and enter the following commands, where *n* is your channel number:

-   **set \_NT\_DEBUG\_BUS=1394**
-   **set \_NT\_DEBUG\_1394\_CHANNEL=***n*

To start a debugging session, open a Command Prompt window and enter one of the following commands:

-   **kd**
-   **windbg**

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For complete documentation of the **bcdedit** command and the boot.ini file, see Boot Options for Driver Testing and Debugging in the Windows Driver Kit (WDK) documentation.

## <span id="troubleshooting-tips-for-debugging-over-a-1394-cable"></span><span id="TROUBLESHOOTING-TIPS-FOR-DEBUGGING-OVER-A-1394-CABLE"></span>Troubleshooting Tips for Debugging over a 1394 Cable


Most 1394 debugging problems are caused by using multiple 1394 controllers in either the host or target computer. Using multiple 1394 controllers in the host computer is not supported. The 1394 debug driver, which runs on the host, can communicate only with the first 1394 controller enumerated in the registry. If you have a 1394 controller built into the motherboard and a separate 1394 card, either remove the card or disable the built-in controller in the BIOS settings of the computer.

The target computer can have multiple 1394 controllers, although this is not recommended. If your target computer has a 1394 controller on the motherboard, use that controller for debugging, if possible. If there is an additional 1394 card, you should remove the card and use the onboard controller. Another solution is to disable the onboard 1394 controller in the BIOS settings of the computer.

If you decide to have multiple 1394 controllers enabled on the target computer, you must specify bus parameters so that the debugger knows which controller to claim for debugging. To specify the bus parameters, Open Device Manager on the target computer, and locate the 1394 controller that you want to use for debugging. Open the property page for the controller, and make a note of the bus number, device number, and function number. In an elevated Command Prompt Window, enter the following command, where *b*, *d*, and *f* are the bus, device and function numbers in decimal format:

**bcdedit -set "{dbgsettings}" busparams** *b***.***d***.***f*.

Reboot the target computer.

## <span id="related_topics"></span>Related topics


[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Kernel-Mode%20Debugging%20over%20a%201394%20Cable%20Manually%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





