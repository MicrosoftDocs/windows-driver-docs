---
title: USB Serial Driver (Usbser.sys)
description: Use the Microsoft-provided USB driver (Usbser.sys) for your communications and CDC control device.
ms.date: 01/17/2024
---

# USB serial driver (Usbser.sys)

> [!IMPORTANT]
> This topic is for programmers. If you are a customer experiencing USB problems, see [Troubleshoot common USB problems](https://support.microsoft.com/help/17614/windows-10-troubleshoot-common-usb-problems)

Use the Microsoft-provided USB driver (Usbser.sys) for your communications and CDC control device. Microsoft encourages you to use the drivers included with Windows whenever possible.

## Versions supported

- Windows 11
- Windows 10

## Applies to

- Device manufacturers of CDC control devices

In Windows 10, the driver was rewritten using the [Kernel-Mode Driver Framework](../wdf/index.md), improving the overall stability of the driver.

- Improved Plug and Play and power management by the driver.
- Added power management features such as [USB Selective Suspend](usb-selective-suspend.md).

In addition, UWP applications can now use the APIs provided by the **[Windows.Devices.SerialCommunication](/uwp/api/Windows.Devices.SerialCommunication)** namespace that allow apps to talk to these devices.

## Usbser.sys installation

Load the Microsoft-provided in-box driver (*Usbser.sys*) for your communications and CDC control device.

> [!NOTE]
> If you trying to install a USB device class driver included in Windows, you do not need to download the driver. They are installed automatically. If they are not installed automatically, contact the device manufacturer. For the list of USB device class driver included in Windows, see [USB device class drivers included in Windows](supported-usb-classes.md).

Starting in Windows 10, *Usbser.inf* was added to the %Systemroot%\\INF directory, which loads *Usbser.sys* as the functional device object (FDO) in the device stack. If your device belongs to the communications and CDC control device class, *Usbser.sys* is loaded automatically. You don't need to write your own INF to reference the driver. The driver is loaded based on a compatible ID match similar to [other USB device class drivers included in Windows](supported-usb-classes.md).

`USB\Class_02`

`USB\Class_02&SubClass_02`

- If you want to load *Usbser.sys* automatically, set the class code to 02 and subclass code to 02 in the [Device Descriptor](usb-device-descriptors.md). With this approach, you aren't required to distribute INF files for your device because the system uses Usbser.inf. For more information, see [Class definitions for Communication Devices 1.2](https://www.usb.org/document-library/class-definitions-communication-devices-12).

- If your device specifies class code 02 but a subclass code value other than 02, *Usbser.sys* doesn't load automatically. The Plug and Play manager tries to find a driver. If a suitable driver isn't found, the device might not have a driver loaded. You might have to load your own driver or write an INF that references another in-box driver.

- If your device specifies class and subclass codes to 02, and you want to load another driver instead of *Usbser.sys*, you have to write an INF that specifies the hardware ID of the device and the driver to install. For examples, look through the INF files included with [sample drivers](../samples/universal-serial-bus--usb--driver-samples.md) and find devices similar to your device. For information about INF sections, see [Overview of INF Files](../install/overview-of-inf-files.md).

## Configure selective suspend for Usbser.sys

Starting in Windows 10, *Usbser.sys* supports [USB Selective Suspend](usb-selective-suspend.md). It allows the attached USB-to-serial device to enter a low power state when not in use, while the system remains in the S0 state. When communication with the device resumes, the device can leave the suspend state and resume the working state. The feature is disabled by default and can be enabled and configured by setting the **IdleUsbSelectiveSuspendPolicy** entry under this registry key:

```syntax
HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\USB\\&lt;hardware id&gt;\\&lt;instance id&gt;\\Device Parameters
```

To configure power management features of *Usbser.sys*, you can set **IdleUsbSelectiveSuspendPolicy** to:

- "0x00000001": Enters selective suspend when idle, that is, when there are no active data transfers to or from the device.

- "0x00000000": Enters selective suspend only when there are no open handles to the device.

That entry can be added in one of two ways:

- Write an INF that references the install INF and add the registry entry in the **HW.AddReg** section.
- Describe the registry entry in an extended properties OS feature descriptor. Add a custom property section that sets the **bPropertyName** field to a Unicode string, "IdleUsbSelectiveSuspendPolicy" and **wPropertyNameLength** to 62 bytes. Set the **bPropertyData** field to "0x00000001" or "0x00000000". The property values are stored as little-endian 32-bit integers.

    For more information, see [Microsoft OS Descriptors](./microsoft-defined-usb-descriptors.md).

## Develop Windows applications for a USB CDC device

Starting in Windows 10, a Windows app can send requests to *Usbser.sys* by using the **[Windows.Devices.SerialCommunication](/uwp/api/Windows.Devices.SerialCommunication)** namespace. It defines Windows Runtime classes that can use to communicate with a USB CDC device through a serial port or some abstraction of a serial port. The classes provide functionality to discover such serial device, read and write data, and control serial-specific properties for flow control, such as setting baud rate, signal states.

## Related topics

- [USB device class drivers included in Windows](supported-usb-classes.md)
