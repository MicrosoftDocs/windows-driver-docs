---
Description: MuttUtil performs various tasks on MUTT devices.
title: MuttUtil
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MuttUtil


MuttUtil performs various tasks on [MUTT devices](microsoft-usb-test-tool--mutt--devices.md).

-   Updates the firmware of the test devices.
-   Installs drivers for MUTT devices.
-   Verifies that the devices are installed without errors.
-   Changes the operating bus speed of the device.
-   Configures the device to send a resume wake signal after a specified time period.
-   For the MUTT Pack, it sets the hub to operate at full or high speed; as a single-TT or multi-TT hub.

MuttUtil is embedded in the installation section of the included test scripts to ensure that the test device is properly upgraded to latest firmware. The tool is included in the [MUTT Software Package](http://go.microsoft.com/fwlink/p/?linkid=617710).

## How to run MuttUtil


**MuttUtil Help**

Run the following command to get a list of command-line options:

`MUTTUtil.exe`

**Finding all MUTT devices attached to the system**

`MUTTUtil.exe -list`

``` syntax
       :   : HARDWARE ID                    : PROBLEM CODE : DRIVER
DEVICE : 0 : USB\VID_045E&PID_0611&REV_0034 : 0            : WINUSB
DEVICE : 1 : USB\VID_045E&PID_078E&REV_8011 : 28           :

Return value: 1
```

The preceding command indicates that the system has a SuperMUTT (1) and a MUTT Pack (0) attached. The Microsoft-provided kernel mode driver, Winusb.sys, is the function driver for the SuperMUTT device. For information about Winusb.sys, see [WinUSB](winusb.md).

PROBLEM CODE 28 for the MUTT Pack device indicates that no driver is loaded for the device.

**Change the personality of a MUTT device**

MUTT devices are also used as test devices for the [USB UWP app sample](http://go.microsoft.com/fwlink/p/?linkid=309716). For that scenario, the firmware must be updated by running the `-SetWinRTUsb` option. In this exercise, SuperMUTT device is set to WinRT personality.

To change it back to MUTT personality, use this command:

`MuttUtil.exe -# 1 -MuttPersonality`

``` syntax
c:\Program Files (x86)\USBTest\x64>MuttUtil.exe -MuttPersonality
Looking for MUTT devices
Send command to change device personality
Return value: 0

c:\Program Files (x86)\USBTest\x64>MuttUtil.exe -list
       :    : HARDWARE ID                    :  PROBLEM CODE  : DRIVER
DEVICE :  0 : USB\VID_045E&PID_078F&REV_0034 :             0  : WINUSB
Return value: 1
```

Notice that the hardware ID is changed to USB\\VID\_045E&PID\_078F&REV\_0037. The revision version indicates the firmware version number.

**Installing a driver for a MUTT device**

Specify the INF file for the driver that contains installation information. For example,

`MUTTUtil.exe -UpdateDriver USBTCD.inf`

``` syntax
c:\Program Files (x86)\USBTest\x64>MuttUtil.exe -UpdateDriver USBTCD.inf
Return value: 0

c:\Program Files (x86)\USBTest\x64>MuttUtil.exe -list
       :    : HARDWARE ID                    :  PROBLEM CODE  : DRIVER
DEVICE :  0 : USB\VID_045E&PID_078F&REV_0034 :             0  : USBTCD
Return value: 1
```

The preceding command replaces the existing driver with the specified USBTCD.sys driver. The driver is included in the [MUTT Software Package](http://go.microsoft.com/fwlink/p/?linkid=617710).

If you have multiple MUTT devices attached, you can update the driver simultaneously.

`MUTTUtil.exe -# 0 -# 1 -MultiUpdateDriver USBTCD.inf usbfx2.inf`

The preceding command installs USBTCD.sys for device 0, Winusb.sys for device 1, and so on.

**Updating the firmware on a MUTT device**

`MuttUtil.exe -UpdateFirmware`

``` syntax
c:\Program Files (x86)\USBTest\x64>MuttUtil.exe -UpdateFirmware
Looking for MUTT devices
0: Updating device firmware from version 34 to version 37
  Erasing EEPROM -- this takes approx 30 seconds
Writing core firmware image
Writing Table at sector 0x09
Writing Table at sector 0x0A
Writing Table at sector 0x0B
Writing Table at sector 0x0C
Writing Table at sector 0x0D
Writing Table at sector 0x0E
Writing Table at sector 0x0F
Writing Table at sector 0x10
Writing Table at sector 0x08
0: Resetting device
Return value: 0
c:\Program Files (x86)\USBTest\x64>MuttUtil.exe -list
       :    : HARDWARE ID                    :  PROBLEM CODE  : DRIVER
DEVICE :  0 : USB\VID_045E&PID_078F&REV_0037 :             0  : USBTCD
Return value: 1
```

The command updates the EEPROM with firmware *only if* the version in the device is old. The firmware image is embedded in the tool. If the device has newer version than the firmware installed by the tool, it does not replace the firmware in the device. If you want to replace the firmware in the device regardless of the version, run MuttUtil with the `-ForceUpdateFirmware` option instead.

Another way of updating the firmware is by writing it to the EEPROM or RAM directly. For this, you must have the firmware file.

To erase EEPROM, use the `-EraseEEPROM` option

**Disconnecting, reconnecting, and re-enumerating the device**

`MuttUtil.exe -Reconnect`

`MuttUtil.exe -CyclePort`

The preceding command causes the device to disconnect and then reconnect on the same port.

The `-CyclePort` option causes the device to disconnect and connect back to the port, except the device is not disconnected electrically. The device is disconnected and reconnected in software. This operation leads to device reset and the PnP Manager rebuilds the device node.

To reset the hub of a MUTT Pack or a SuperMUTT Pack device, use this command:

`MuttUtil.exe -# 1 -ResetHub`

**Changing the speed of the device**

You can change the device speed of MUTT devices by using this command:

`MuttUtil.exe -# 0 -SetFullSpeed`

`MuttUtil.exe -# 1 -SetHighSpeed`

The command causes the device to disconnect and then reconnect on the same port at the specified speed.

If you want to change the speed of the hub, of a MUTT Pack or SuperMUTT Pack, to operate in full speed mode, use the `-HubFS` command:

`MuttUtil.exe -# 1 -HubFS`

**Sending a resume signal to wake up the system**

Typically, a resume signal are sent by the device (in low power) upon certain user action. You can simulate that behavior by using this command:

`MuttUtil.exe -WakeAfterSuspend 5000`

The command configures the device to send a resume signal, 5 seconds after the bus suspends.

You can also configure the device to disconnect and reconnect in a certain period of time after the bus suspends by using the `-DisconnectAfterSuspend` option.

**Setting and clearing overcurrent on the port downstream port - MUTT Pack and SuperMUTT Pack**

These commands set and clear the overcurrent pin for the exposed port of the Mutt-Pack.

`MuttUtil.exe -# 1 -SetOvercurrent`

`MuttUtil.exe -# 1 -ClearOvercurrent`

**Converting the hub to a TT high speed hub - MUTT Pack and SuperMUTT Pack**

You can set the hub to operate as a multi-TT high speed hub or a single-TT high speed hub by using these commands:

`MuttUtil.exe -# 1 -HubHSMultiTT`

`MuttUtil.exe -# 1 -HubHSSingleTT`

## Related topics
[USB test tools](usb-test-tools.md)  
[Tools in the MUTT software package](mutt-software-package.md)  
[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)  



