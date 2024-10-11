---
title: Setting up KDNET USB kernel-mode debugging (KDNET-USB)
description: Learn how to use kdnet.exe to set up KDNET-USB kernel-mode debugging over a USB 3.0 cable.
ms.date: 10/09/2024
---

# Setting up KDNET USB kernel-mode debugging (KDNET-USB)

Debugging Tools for Windows supports kernel-mode debugging over a USB 3.0 cable using KDNET over USB. This article describes how to configure this transport option.

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*.


Debugging over a USB 3.0 cable requires the following hardware:

- On the host computer, an xHCI USB 3.0+ host controller and USB3 port.
- On the target computer, an xHCI USB 3.0+ host controller and a USB3 port that supports debugging (DBC)
- The target computer USB host controller must support the Intel xHCI Debug Capability Interface (DBC). For more information refer to xHCI specification available on the Intel Web site.

## Binary transport files

The kdstub.dll and kdnic.sys driver are used to support the KDNET-USB debugger transport.

## Cable requirements

- An orange Microsoft USB debug cable, which is an A-A crossover cable that has two male type-A plugs and no Vbus connection. This cable is available from vendors such as DataPro - *USB 3.0 Super-Speed A/A Debugging Cable*.

- A standard USB 3.0 Type C to Type A adapter is required to connect the host type A port to the target type C port.

To simplify the troubleshooting, connect the cable directly between the target and host computer, avoiding any hubs or docking stations.

## Set up the target computer

1. On the target computer, locate and launch the *UsbView* tool. The UsbView tool is included in Debugging Tools for Windows. For an x64 system, UsbView would be located in *C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\KitVersion\\x64\\usbview.exe*.
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

5. If you need to confirm the bus parameters, use Device Manager. In Device Manager, locate the USB Controller that you intend to use for debugging. Under **Location** on the **General** tab, the bus, device, and function numbers are displayed.   *b*, *d*, and *f* are the bus, device, and function numbers for the USB3 host controller. The bus, device, and function numbers must be in decimal format.

6. You can also use kdnet.exe to help gather information about the USB Controller.

    ```console
    C:\Program Files (x86)\Windows Kits\10\Debuggers\x64>kdnet
    
    Network debugging is supported on the following USB controllers:
    busparams=0.20.0, Intel(R) USB 3.0 eXtensible Host Controller - 1.0 (Microsoft)

    This Microsoft hypervisor supports using KDNET in guest VMs.
    ```

7. After you identify an xHCI controller that supports debugging, the next step is to locate the physical USB connector that's associated with a port on the xHCI controller. To find the physical connector, plug any USB 3.0 device into any USB connector on the target computer. Refresh UsbView to see where your device is located. If UsbView shows your device connected to your chosen xHCI host controller, then you have found a physical USB connector that you can use for USB 3.0 debugging.

> [!IMPORTANT]
> Before using `bcdedit` or kdnet.exe to change boot information, you might need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC. 
> Re-enable these security features when testing is complete and appropriately manage the test PC when the security features are disabled.

8. Pick a unique `<port address>` for each target/host pair that you work with, within the recommended range of 50000-50039. 50005 is shown in the examples below.

9. Locate the KDNet.exe utility in the WDK debugger directory matching your CPU type, for example x64. 

10. On the target computer, open a Command Prompt window as Administrator, and enter this command to enable kernel debugging with `-k` option. The -w, -b, and -h will enable kernel debugging for winload, bootmgr, and hypervisor system applications.For more information about the WinDbg options, see [WinDbg - Command line startup options](../debuggercmds/windbg-command-line-preview.md).

    ```console
    kdnet.exe 169.254.255.255 50005 -k
    ```
    - **169.254.255.255** the non routable link-local static IP address must be used for KDNET over USB3.
    - kdnet.exe will return a key `w.x.y.z` that will be used by WinDbg to connect to the target device.
 
    To use a specific USB port, use the *-busparams* parameter.  

    ```console
    kdnet.exe -busparams 0.13.0 169.254.255.255 50005 -k
    ```
 
    The use of the KDNET utility is recommended. This tool sets options that are more complicated to set using bcdedit, as well as checking and setting supporting registry values for PCI and power management.

    ```console
    bcdedit /dbgsettings NET hostip:169.254.255.255 port:50001 key:1.2.3.4 busparams:0.20.0 noDhcp
    ```

### Disable power management

In some cases, power transitions can interfere with debugging over USB 3.0. To avoid these problems, disable selective suspend for the xHCI host controller, and its root hub, that you're using for debugging.

1. In Device Manager, navigate to the node for the xHCI host controller. Right-click the node, and choose **Properties**. If there's a **Power Management** tab, open the tab, and clear the **Allow the computer to turn off this device to save power** checkbox.

2. In Device Manager, navigate to the node for the root hub of the xHCI host controller. Right click the node, and choose **Properties**. If there's a **Power Management** tab, open the tab, and clear the **Allow the computer to turn off this device to save power** check box.

When you finish using the xHCI host controller for debugging, re-enable selective suspend for the xHCI host controller.

## Start a debugging session using WinDbg

1. Connect a USB 3.0 debug cable to the identified USB 3.0 ports that you've chosen for debugging on the host and target computers.

2. On the host computer, open a version of WinDbg (as Administrator) that matches the bitness of Windows running on the host computer. For example, if the host computer is running a 64-bit version of Windows, open the 64-bit version of WinDbg as Administrator.

3. On the **File** menu, choose **Attach to Kernel**. In the Kernel Debugging dialog box, open the **Net** tab. Enter the following information and click **OK**.

    - The `<port address>` that is unique for each target/host pair, and is within the recommended range of 50000-50039, was provided as input when kdnet.exe was run.

    - The `<session key>` w.x.y.z that was generated when kdnet.exe was run and its value was displayed in the command output.

### Command line session with WinDbg

You can also start a session with WinDbg by entering this command in a Command Prompt window.

```console
Windbg /k NET:port=<port address>,key=<session key>
```

## Reboot the target computer

Once the debugger is loaded and ready to go, reboot the target computer. One way to do reboot the PC, is to use the `shutdown -r -t 0` command from an administrator's command prompt.

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

Use caution when editing the registry directly, as incorrect changes can lead to system instability.

### Connection retries messages on the debugger console windows and cannot break-in into the target - SkipPciProbeDebugDevice

If you encounter the following message in KDNET debugger console, cannot initiate a break-in into the target, or experience issues with certain commands (e.g., kdfiles), it may be due to KDNET receiving an out-of-sequence ping packet.

```console
... Retry sending the same data packet for 128 times.

The transport connection between host kernel debugger and target Windows seems lost.
please try resync with target, recycle the host debugger, or reboot the target Windows.
```

This issue can happen because the pci.sys driver is probing the debug device. To eliminate these error messages, create the following registry entry on the TARGET device at an administrator command prompt.

This setting can also allow the debugger to connect if the initial KD transport failed to connect at boot, for some other reason, for example if the the debug device could not be configured at boot.

```console
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\SERVICES\kdnet /v SkipPciProbeDebugDevice /t REG_DWORD /d 1 /f
```

Then restart the target machine.

```console
shutdown /r /t 0
```

Once the device reboots then the errors should disappear, and commands should work as expected.

### NO_KDNIC setting for enhanced performance and reliablity

If an ethernet NIC is installed on the target PC, additional reliability and performance improvements can be achieved by setting the `NO_KDNIC` option.

   ```console
   bcdedit /set {current} loadoptions NO_KDNIC
   ```

Adding `NO_KDNIC` is optional and can be used only if the target has an extra NIC, Wi-Fi, or USB port to connect a USB-Ethernet adapter to provide network access to Windows. 

Adding `NO_KDNIC` will prevent the kdnic.sys driver (a miniport timer-based driver) from running on top of KDNET, meaning that Windows TCP/IP traffic won’t be routed via KDNET transport. Then the KDNET transport can be used only to route debugging-related packets between the target KDNET and the host debugger.

This can help with network performance that can be affected when kdnic.sys driver is running on top of kdnet. In this situation the target will never go to sleep, preventing power drip tests, or delays will occur when accessing the target via RDP. This is because the KDNET interface needs to route both debugger packets and Windows TCP/IP network packets when kdnic.sys is running.

## See also

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)

[Set up kernel-mode debugging manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

[Setting up USB 3.0 xHCI-DBC kernel-mode debugging (KDUSB)](setting-up-a-usb-3-0-debug-cable-connection.md)

[Setting Up USB KDNET EEM Kernel-Mode Debugging (KDNET-EEM-USB)](setting-up-kernel-mode-debugging-over-usb-eem-arm-kdnet.md) 
