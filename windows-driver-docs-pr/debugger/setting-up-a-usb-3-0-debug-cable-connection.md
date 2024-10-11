---
title: Setting up USB 3.0 xHCI kernel-mode debugging (KDUSB xHCI-DBC USB 3.0)
description: Learn how to manually set up xHCI kernel-mode debugging over a USB 3.0 cable. (KDUSB xHCI-DBC USB 3.0)
ms.date: 10/09/2024
---

# Setting up USB 3.0 xHCI kernel-mode debugging (KDUSB xHCI-DBC USB 3.0)

Debugging Tools for Windows supports kernel-mode debugging over a USB 3.0 cable. This article describes how to manually set up USB 3.0 debugging.

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*.

Debugging over a USB 3.0 cable requires the following hardware:

- On the host computer, an xHCI (USB 3.0) host controller
- On the target computer, an xHCI (USB 3.0) host controller that supports debugging
- The target computer USB host controller must support the Intel xHCI-Debug Capability Interface (DBC). For more information refer to xHCI specification available on the Intel Web site.

## Cable requirements

- An orange Microsoft USB debug cable, which is an A-A crossover cable that has two male type-A plugs and no Vbus connection. This cable is available from vendors such as DataPro - *USB 3.0 Super-Speed A/A Debugging Cable*.

To simplify the troubleshooting, connect the cable directly between the target and host computer, avoiding any hubs or docking stations.

## Binary transport files

The kdstub.dll is used to support the KDUSB xHCI-DBC USB 3.0 debugger transport.

## Set up the target computer

1. On the target computer, launch the *UsbView* tool. The UsbView tool is included in Debugging Tools for Windows. For an x64 system, UsbView would be located in *C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\kitversion\\x64\\usbview.exe*.
2. In UsbView, locate all of the xHCI host controllers.
3. In UsbView, expand the nodes of the xHCI host controllers. Look for an indication that a port on the host controller supports debugging.

    ```console
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

4. Make a note of the bus, device, and function numbers for the xHCI controller that you intend to use for debugging. UsbView displays these numbers. In the following example, the bus number is 48, the device number is 0, and the function number is 0.

    ```console
    USB xHCI Compliant Host Controller
    ...
    DriverKey: {36fc9e60-c465-11cf-8056-444553540000}\0020
    ...
    Bus.Device.Function (in decimal): 48.0.0
    ```

5. After you identify an xHCI controller that supports debugging, the next step is to locate the physical USB connector that's associated with a port on the xHCI controller. To find the physical connector, plug any USB 3.0 device into any USB connector on the target computer. Refresh UsbView to see where your device is located. If UsbView shows your device connected to your chosen xHCI host controller, then you have found a physical USB connector that you can use for USB 3.0 debugging.

> [!IMPORTANT]
> Before using `bcdedit` to change boot information, you might need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC. 
> Re-enable these security features when testing is complete and appropriately manage the test PC when the security features are disabled.

6. On the target computer, open a Command Prompt window as Administrator, and enter these commands:

   ```console
   bcdedit /debug on
   bcdedit /dbgsettings usb targetname:<TargetName>
   ```

   *TargetName* is a name that you create for the target computer. Note that *TargetName* doesn't have to be the official name of the target computer; it can be any string that you create as long as it meets these restrictions:

   - The string must not contain “debug” anywhere in the *TargetName* in any combination of upper or lower case. For example if you use “DeBuG” or "DEBUG" anywhere in your targetname, debugging doesn't work correctly.  
   - The only characters in the string are the hyphen (-), the underscore(\_), the digits 0 through 9, and the letters A through Z (upper or lower case).
   - The maximum length of the string is 24 characters.

7. In Device Manager, locate the USB Controller that you intend to use for debugging. Under **Location** on the **General** tab, the bus, device, and function numbers are displayed. Enter this command:

   ```console
   bcdedit /set "{dbgsettings}" busparams <b.d.f>
   ```

   *B*, *d*, and *f* are the bus, device, and function numbers for the USB host controller. The bus, device, and function numbers must be in decimal format.

   Example:

   ```console
   bcdedit /set "{dbgsettings}" busparams 48.0.0
   ```

8. Reboot the target computer.

### Disable power management

In some cases, power transitions can interfere with debugging over USB 3.0. To avoid these problems, disable selective suspend for the xHCI host controller, and its root hub, that you're using for debugging.

1. In Device Manager, navigate to the node for the xHCI host controller. Right-click the node, and choose **Properties**. If there's a **Power Management** tab, open the tab, and clear the **Allow the computer to turn off this device to save power** checkbox.

2. In Device Manager, navigate to the node for the root hub of the xHCI host controller. Right click the node, and choose **Properties**. If there's a **Power Management** tab, open the tab, and clear the **Allow the computer to turn off this device to save power** check box.

When you finish using the xHCI host controller for debugging, re-enable selective suspend for the xHCI host controller.

## Start a debugging session for the first time

1. Connect a USB 3.0 debug cable to the USB 3.0 ports that you've chosen for debugging on the host and target computers.
2. Determine the bitness (32-bit or 64-bit) of Windows running on the host computer.
3. On the host computer, open a version of WinDbg (as Administrator) that matches the bitness of Windows running on the host computer. For example, if the host computer is running a 64-bit version of Windows, open the 64-bit version of WinDbg as Administrator.
4. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **USB** tab. Enter the target name that you created when you set up the target computer. Click **OK**.

At this point, the USB debug driver gets installed on the host computer, which is why it's important to match the bitness of WinDbg to the bitness of Windows. After the USB debug driver is installed, you can use either the 32-bit or 64-bit version of WinDbg for subsequent debugging sessions.

## Start a debugging session

### Using WinDbg

On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **USB** tab. Enter the target name that you created when you set up the target computer. Select **OK**.

You can also start a session with WinDbg by entering the following command in a Command Prompt window, where *TargetName* is the target name you created when you set up the target computer:

```console
windbg /k usb:targetname=<TargetName>
```

### Using KD

On the host computer, open a Command Prompt window and enter the following command, where *TargetName* is the target name you created when you set up the target computer:

```console
kd /k usb:targetname=<TargetName>
```

### Reboot the target computer

Once the debugger is connected, reboot the target computer. One way to do reboot the PC, is to use the `shutdown -r -t 0` command from an administrator's command prompt.

After the target PC restarts, the debugger should connect automatically.

## Troubleshooting

### USB device not recognized

If a windows notification appears on the host with the text *USB device not recognized* when you insert the debug cable, it's possible that a known USB 3.1 to 3.1 compatibility issue is being hit. This issue affects debug configurations when the debug cable is connected to a USB 3.1 controller on the host and an Intel (Ice Lake or Tiger Lake) 3.1 USB controller on the target.

For more information and processor model listings, see [Ice Lake (microprocessor)](https://en.wikipedia.org/wiki/Ice_Lake_(microprocessor)) and or [Tiger Lake (microprocessor)](https://en.wikipedia.org/wiki/Tiger_Lake_(microprocessor)). To find the processor model of the target machine, open the Settings app and go to **System** then **About**. **Processor** is listed under **Device specifications**.

To verify this problem, open Device Manager and look for **USB Debug Connection Device** under **Universal Serial Bus controllers**. If this device can't be found, check for an **Unknown device** under **Other devices**. Right-click on the device to open its properties page. The device status text box will have the text **Windows has stopped this device because it has reported problems (Code 43)** and **The USB device returned an invalid USB BOS descriptor**.

To work around this problem, run these commands from an administrator command prompt to make changes to the registry:

```console
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\usbflags\349500E00000 /v SkipBOSDescriptorQuery /t REG_DWORD /d 1 /f
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\usbflags\045E06560000 /v SkipBOSDescriptorQuery /t REG_DWORD /d 1 /f
```

Then, remove and reinsert the debug cable.

### Connection retries messages on the debugger console windows and cannot break-in into the target - SkipPciProbeDebugDevice

If you encounter the following message in KDNET debugger console, cannot initiate a break-in into the target, or experience issues with certain commands (e.g., kdfiles), it may be due to KDNET receiving an out-of-sequence ping packet."

```console
... Retry sending the same data packet for 128 times.

The transport connection between host kernel debugger and target Windows seems lost.
please try resync with target, recycle the host debugger, or reboot the target Windows.
```

This issue can happen because the pci.sys driver is incorrectly probing the debug device. To eliminate the errors, create the following registry entry on the TARGET device at an administrator command prompt.

```console
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\SERVICES\kdnet /v SkipPciProbeDebugDevice /t REG_DWORD /d 1 /f
```

Then restart the target machine.

```console
shutdown /r /t 0
```

Once the device reboots then the errors should disappear, and commands should work as expected.

## See also

[Set up kernel-mode debugging manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)

[Setting Up USB KDNET EEM Kernel-Mode Debugging (KDNET-EEM-USB)](setting-up-kernel-mode-debugging-over-usb-eem-arm-kdnet.md) 

[Setting up USB KDNET kernel-mode debugging (KDNET-USB)](setting-up-a-kdnet-usb-connection.md)