---
title: Setting Up Kernel-Mode Debugging over a USB 3.0 Cable Manually
description: Debugging Tools for Windows supports kernel debugging over a USB 3.0 cable. This topic describes how to set up USB 3.0 debugging manually.
ms.assetid: 9A9F5DA0-B98A-4C19-A723-67D06B2409B5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up Kernel-Mode Debugging over a USB 3.0 Cable Manually


Debugging Tools for Windows supports kernel debugging over a USB 3.0 cable. This topic describes how to set up USB 3.0 debugging manually.

As an alternative to setting up USB 3.0 debugging manually, you can do the setup using Microsoft Visual Studio. For more information, see [Setting Up Kernel-Mode Debugging over a USB 3.0 Cable in Visual Studio](setting-up-a-usb-3-0-cable-connection-in-visual-studio.md).

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*.

Debugging over a USB 3.0 cable requires the following hardware:

-   A USB 3.0 debug cable. This is an A-A crossover cable that has only the USB 3.0 lines and no Vbus.

-   On the host computer, an xHCI (USB 3.0) host controller

-   On the target computer, an xHCI (USB 3.0) host controller that supports debugging

## <span id="setting_up_the_computer_usb3_manual"></span><span id="SETTING_UP_THE_COMPUTER_USB3_MANUAL"></span>Setting Up the Target Computer


1.  On the target computer, launch the UsbView tool. The UsbView tool is included in Debugging Tools for Windows.
2.  In UsbView, locate all of the xHCI host controllers.
3.  In UsbView, expand the nodes of the xHCI host controllers. Look for an indication that a port on the host controller supports debugging.

    ```
    [Port1] 

    Is Port User Connectable:         yes
    Is Port Debug Capable:            yes
    Companion Port Number:            3
    Companion Hub Symbolic Link Name: USB#ROOT_HUB30#5&32bab638&0&0#{...}
    Protocols Supported:
     USB 1.1:                         no
     USB 2.0:                         no
     USB 3.0:                         yes
    ```

4.  Make a note of the bus, device, and function numbers for the xHCI controller that you intend to use for debugging. UsbView displays these number. In the following example, the bus number is 48, the device number is 0, and the function number is 0.

    ```
    USB xHCI Compliant Host Controller
    ...
    DriverKey: {36fc9e60-c465-11cf-8056-444553540000}\0020
    ...
    Bus.Device.Function (in decimal): 48.0.0
    ```

5.  After you have identified an xHCI controller that supports debugging, the next step is to locate the physical USB connector that is associated with a port on the xHCI controller. To find the physical connector, plug any USB 3.0 device into any USB connector on the target computer. Refresh UsbView to see where your device is located. If UsbView shows your device connected to your chosen xHCI host controller, then you have found a physical USB connector that you can use for USB 3.0 debugging.

6.  On the target computer, open a Command Prompt window as Administrator, and enter these commands:

    -   **bcdedit /debug on**
    -   **bcdedit /dbgsettings usb targetname:***TargetName*

    where *TargetName* is a name that you create for the target computer. Note that *TargetName* does not have to be the official name of the target computer; it can be any string that you create as long as it meets these restrictions:

    -   The maximum length of the string is 24 characters.
    -   The only characters in the string are the hyphen (-), the underscore(\_), the digits 0 through 9, and the letters A through Z (upper or lower case).

7.  If you have more than one USB host controller on the target computer, enter this command:

    **bcdedit /set "{dbgsettings}" busparams** *b.d.f*

    where *b*, *d*, and *f* are the bus, device, and function numbers for the USB host controller that you intend to use for debugging. The bus, device, and function numbers must be in decimal format.

    Example:

    **bcdedit /set "{dbgsettings}" busparams 48.0.0**

8.  Reboot the target computer.

## <span id="Starting_a_Debugging_Session_for_the_First_Time"></span><span id="starting_a_debugging_session_for_the_first_time"></span><span id="STARTING_A_DEBUGGING_SESSION_FOR_THE_FIRST_TIME"></span>Starting a Debugging Session for the First Time


1.  Connect a Universal Serial Bus (USB) 3.0 debug cable to the USB 3.0 ports that you have chosen for debugging on the host and target computers.
2.  Determine the bitness (32-bit or 64-bit) of Windows running on the host computer.
3.  On the host computer, open a version of WinDbg (as Administrator) that matches the bitness of Windows running on the host computer. For example, if the host computer is running a 64-bit version of Windows, open the 64-bit version of WinDbg as Administrator.
4.  On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **USB** tab. Enter the target name that you created when you set up the target computer. Click **OK**.

At this point, the USB debug driver gets installed on the host computer. This is why it is important to match the bitness of WinDbg to the bitness of Windows. After the USB debug driver is installed, you can use either the 32-bit or 64-bit version of WinDbg for subsequent debugging sessions.

## <span id="starting_the_debugging_session_usb3_manual"></span><span id="STARTING_THE_DEBUGGING_SESSION_USB3_MANUAL"></span>Starting a Debugging Session


### <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **USB** tab. Enter the target name that you created when you set up the target computer. Click **OK**.

You can also start a session with WinDbg by entering the following command in a Command Prompt window, where *TargetName* is the target name you created when you set up the target computer:

**windbg /k usb:targetname=***TargetName*

### <span id="Using_KD"></span><span id="using_kd"></span><span id="USING_KD"></span>Using KD

On the host computer, open a Command Prompt window and enter the following command, where *TargetName* is the target name you created when you set up the target computer:

**kd /k usb:targetname=***TargetName*

## <span id="troubleshooting_tips_for_debugging_over_usb_3.0"></span><span id="TROUBLESHOOTING_TIPS_FOR_DEBUGGING_OVER_USB_3.0"></span>Troubleshooting tips for debugging over USB 3.0


In some cases, power transitions can interfere with debugging over USB 3.0. If you have this problem, disable selective suspend for the xHCI host controller (and its root hub) that you are using for debugging.

1.  In Device Manager, navigate to the node for the xHCI host controller. Right click the node, and choose **Properties**. If there is a **Power Management** tab, open the tab, and clear the **Allow the computer to turn off this device to save power** check box.
2.  In Device Manager, navigate to the node for the root hub of the xHCI host controller. Right click the node, and choose **Properties**. If there is a **Power Management** tab, open the tab, and clear the **Allow the computer to turn off this device to save power** check box.

When you have finished using the xHCI host controller for debugging, enable selective suspend for the xHCI host controller.

## <span id="related_topics"></span>Related topics


[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Kernel-Mode%20Debugging%20over%20a%20USB%203.0%20Cable%20Manually%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





