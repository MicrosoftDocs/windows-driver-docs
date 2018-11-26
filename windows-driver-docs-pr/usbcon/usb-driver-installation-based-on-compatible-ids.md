---
Description: Microsoft-provided in-box driver (Usbser.sys) for your Communications and CDC Control device.
title: USB serial driver (Usbser.sys)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB serial driver (Usbser.sys)


**Last updated**

-   April, 2015

** OS version**

-   Windows 10
-   Windows 8.1

**Applies to**

-   Device manufacturers of CDC Control devices

Microsoft-provided in-box driver (Usbser.sys) for your Communications and CDC Control device.

In Windows 10, the driver has been rewritten by using the [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/) that improves the overall stability of the driver.

-   Improved PnP and power management by the driver (such as, handling surprise removal).
-   Added power management features such as [USB Selective Suspend](usb-selective-suspend.md).

In addition, UWP applications can now use the APIs provided by the new [**Windows.Devices.SerialCommunication**](https://msdn.microsoft.com/library/windows/apps/dn921817) namespace that allow apps to talk to these devices.

## Usbser.sys installation


Load the Microsoft-provided in-box driver (Usbser.sys) for your Communications and CDC Control device.

**Note**  If you trying to install a USB device class driver included in Windows, you do not need to download the driver. They are installed automatically. If they are not installed automatically, contact the device manufacturer. For the list of USB device class driver included in Windows, see [USB device class drivers included in Windows](supported-usb-classes.md).

 

**Windows 10**

In Windows 10, a new INF, Usbser.inf, has been added to %Systemroot%\\Inf that loads Usbser.sys as the function device object (FDO) in the device stack. If your device belongs to the Communications and CDC Control device class, Usbser.sys is loaded automatically.You do not need to write your own INF to reference the driver. The driver is loaded based on a compatible ID match similar to [other USB device class drivers included in Windows](supported-usb-classes.md).

`USB\Class_02`

`USB\Class_02&SubClass_02`

-   If you want to load Usbser.sys automatically, set the class code to 02 and subclass code to 02 in the [Device Descriptor](usb-device-descriptors.md). For more information, see USB communications device class (or USB CDC) Specification found on the [USB DWG website](http://go.microsoft.com/fwlink/p/?linkid=617741). With this approach, you are not required to distribute INF files for your device because the system uses Usbser.inf.
-   If your device specifies class code 02 but a subclass code value other than 02, Usbser.sys does not load automatically. Pnp Manager tries to find a driver. If a suitable driver is not found, the device might not have a driver loaded. In this case, you might have to load your own driver or write an INF that references another in-box driver.
-   If your device specifies class and subclass codes to 02, and you want to load another driver instead of Usbser.sys, you have to write an INF that specifies the hardware ID of the device and the driver to install. For examples, look through the INF files included with [sample drivers](http://go.microsoft.com/fwlink/p/?LinkId=534087) and find devices similar to your device. For information about INF sections, see [Overview of INF Files](https://msdn.microsoft.com/library/windows/hardware/ff549520).

**Note**  Microsoft encourages you to use in-box drivers whenever possible. On mobile editions of Windows, such as Windows 10 Mobile, only drivers that are part of the operating system are loaded. Unlike desktop editions, it is not possible to load a driver through an external driver package. With the new in-box INF, Usbser.sys is automatically loaded if a USB-to-serial device is detected on the mobile device.

 

**Windows 8.1 and earlier versions**

In Windows 8.1 and earlier versions of the operating system, Usbser.sys is not automatically loaded when a USB-to-serial device is attached to a computer. To load the driver, you need to write an INF that references the modem INF (mdmcpq.inf) by using the **Include** directive. The directive is required for instantiating the service, copying inbox binaries, and registering a device interface GUID that applications require to find the device and talk to it. That INF specifies "Usbser" as a lower filter driver in a device stack.

The INF also needs to specify the device setup class as **Modem** to use mdmcpq.inf. Under the [Version] section of the INF, specify the **Modem** and the device class GUID. for details, see [System-Supplied Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff553419).

``` syntax
[DDInstall.NT]
include=mdmcpq.inf
CopyFiles=FakeModemCopyFileSection 

[DDInstall.NT.Services]
include=mdmcpq.inf
AddService=usbser, 0x00000000, LowerFilter_Service_Inst 

[DDInstall.NT.HW]
include=mdmcpq.inf
AddReg=LowerFilterAddReg
```

For more information, see [this KB article](https://support.microsoft.com/kb/837637/).

## Configure selective suspend for Usbser.sys


Starting in Windows 10, Usbser.sys supports [USB Selective Suspend](usb-selective-suspend.md). It allows the attached USB-to-serial device to enter a low power state when not in use, while the system remains in the S0 state. When communication with the device resumes, the device can leave the Suspend state and resume Working state. The feature is disabled by default and can be enabled and configured by setting the **IdleUsbSelectiveSuspendPolicy** entry under this registry key:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\USB\\&lt;hardware id&gt;\\&lt;instance id&gt;\\Device Parameters**

To configure power management features of Usbser.sys, you can set **IdleUsbSelectiveSuspendPolicy** to:

-   "0x00000001"

    Enters selective suspend when idle, that is, when there are no active data transfers to or from the device.

-   "0x00000000"

    Enters selective suspend only when there are no open handles to the device.

That entry can be added in one of two ways:

-   Write an INF that references the install INF and add the registry entry in the **HW.AddReg** section.
-   Describe the registry entry in an extended properties OS feature descriptor. Add a custom property section that sets the **bPropertyName** field to a Unicode string, "IdleUsbSelectiveSuspendPolicy" and **wPropertyNameLength** to 62 bytes. Set the **bPropertyData** field to "0x00000001" or "0x00000000". The property values are stored as little-endian 32-bit integers.

    For more information, see [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?linkid=224878).

## Develop Windows applications for a USB CDC device


If you install Usbser.sys for the USB CDC device, here are the application programming model options:

-   Starting in Windows 10, a Windows app can send requests to Usbser.sys by using the [**Windows.Devices.SerialCommunication**](https://msdn.microsoft.com/library/windows/apps/dn921817) namespace. It defines Windows Runtime classes that can use to communicate with a USB CDC device through a serial port or some abstraction of a serial port. The classes provide functionality to discover such serial device, read and write data, and control serial-specific properties for flow control, such as setting baud rate, signal states.

-   In Windows 8.1 and earlier versions, you can write a Windows desktop application that opens a virtual COM port and communicates with the device. For more information, see:

    Win32 programming model:

    -   [Configuring a Communications Resource](https://msdn.microsoft.com/library/windows/desktop/aa363201)
    -   [Communications Reference](https://msdn.microsoft.com/library/windows/desktop/aa363195)

    .NET framework programming model:

    -   [System.IO.Ports Namespace](https://msdn.microsoft.com/library/System.IO.Ports.aspx)

## Related topics
[USB device class drivers included in Windows](supported-usb-classes.md)  
<!-- [How to use or to reference the Usbser.sys driver from universal serial bus (USB) modem .inf files](https://support.microsoft.com/help/837637/how-to-use-or-to-reference-the-usbser.sys-driver-from-universal-serial-bus-usb-modem-.inf-files) -->



