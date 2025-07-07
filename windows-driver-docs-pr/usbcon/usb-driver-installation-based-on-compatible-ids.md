---
title: USB Serial Driver (Usbser.sys)
description: Use the Microsoft-provided USB driver (Usbser.sys) for your communications and CDC control device.
ms.date: 06/11/2025
---

# USB serial driver (Usbser.sys)

Use the Microsoft-provided USB driver (Usbser.sys) for your communications and communications device class (CDC) control devices. Use the drivers included with Windows whenever possible.

> [!IMPORTANT]
> This article is for manufacturers of CDC control devices. If you're a customer experiencing USB problems, see [Fix USB-C problems in Windows](https://support.microsoft.com/windows/fix-usb-c-problems-in-windows-f4e0e529-74f5-cdae-3194-43743f30eed2)

Usbser.sys is implemented using the [Kernel-Mode Driver Framework](../wdf/index.md). The driver supports Plug and Play, and power management features like [USB Selective Suspend](usb-selective-suspend.md).


Universal Windows Platform (UWP) applications can use the APIs provided by the **[Windows.Devices.SerialCommunication](/uwp/api/Windows.Devices.SerialCommunication)** namespace, allowing apps to talk to CDC devices.

## Usbser.sys installation

Load the Microsoft-provided in-box driver (*Usbser.sys*) for your communications and CDC control device.

> [!NOTE]
> If you're trying to install a USB device class driver included in Windows, you don't need to download the driver. Windows installs these drivers automatically. If Windows doesn't install the driver, contact the device manufacturer. For a list of USB device class drivers included in Windows, see [USB device class drivers included in Windows](supported-usb-classes.md).

*Usbser.inf* is located in the `%Systemroot%\INF` directory. This setup information (INF) file loads *Usbser.sys* as the functional device object (FDO) in the device stack. If your device belongs to the communications and CDC control device class, *Usbser.sys* loads automatically. You don't need to write your own INF file to reference the driver. Windows loads the driver based on a compatible ID match, similar to [other USB device class drivers included in Windows](supported-usb-classes.md).

`USB\Class_02`

`USB\Class_02&SubClass_02`

To load *Usbser.sys* automatically, set the class code to 02 and subclass code to 02 in the [Device Descriptor](usb-device-descriptors.md). With this approach, you don't need to distribute INF files for your device because the system uses *Usbser.inf*. For more information, see [Class definitions for Communication Devices 1.2](https://www.usb.org/document-library/class-definitions-communication-devices-12).

If your device specifies class code 02 but a subclass code other than 02, *Usbser.sys* doesn't load automatically. The Plug and Play manager tries to find a driver. If Windows doesn't find a suitable driver, the device might not have a driver loaded. You might need to load your own driver or write an INF file that references another in-box driver.

If your device specifies class and subclass codes of 02, and you want to load another driver instead of *Usbser.sys*, write an INF file. In the INF file, specify the hardware ID of the device and the driver to install.

## Configure selective suspend for Usbser.sys

*Usbser.sys* supports [USB Selective Suspend](usb-selective-suspend.md). This driver lets the attached USB-to-serial device enter a low power state when not in use, while the system stays in the S0 state. When communication with the device resumes, the device leaves the suspend state and resumes the working state. The feature is disabled by default, but can be enabled and configured by setting the **IdleUsbSelectiveSuspendPolicy** entry under this registry key:

`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USB\<hardware id>\<instance id>\Device Parameters`

To configure power management features of *Usbser.sys*, set the **IdleUsbSelectiveSuspendPolicy** parameter to:

| Value | Behavior |
|--|--|
| `0x00000001` | Enter selective suspend when idle, that is, when there are no active data transfers to or from the device. |
| `0x00000000` | Enter selective suspend only when there are no open handles to the device. |

Add that entry in one of two ways:

1. Write an INF that references the install INF and add the registry entry in the **HW.AddReg** section.

1. Describe the registry entry in an extended properties OS feature descriptor. Add a custom property section that sets the **bPropertyName** field to a Unicode string: `IdleUsbSelectiveSuspendPolicy`. Set the **wPropertyNameLength** to 62 bytes. Set the **bPropertyData** field to `0x00000001` or `0x00000000`. The property values store as little-endian 32-bit integers.

    For more information, see [Microsoft OS Descriptors](./microsoft-defined-usb-descriptors.md).

## Develop Windows applications for a USB CDC device

A Windows app sends requests to *Usbser.sys* by using the **[Windows.Devices.SerialCommunication](/uwp/api/Windows.Devices.SerialCommunication)** namespace. The namespace defines Windows Runtime classes that communicate with a USB CDC device through a serial port or an abstraction of a serial port. The classes let you discover serial devices, read and write data, and control serial-specific properties for flow control, such as setting the baud rate and signal states.

## Related articles

- [USB device class drivers included in Windows](supported-usb-classes.md)
