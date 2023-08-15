---
title: USB device registry entries
description: This article describes USB device-specific registry entries.
ms.date: 08/15/2023
ms.custom: contperf-fy22q4
---

# USB device registry entries

This article describes USB device-specific registry entries.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer experiencing USB problems, see [Troubleshoot common USB problems](https://support.microsoft.com/help/17614/windows-10-troubleshoot-common-usb-problems)

## Registry settings for configuring USB driver stack behavior

The registry entries described in this article are found under this key:

```output
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Control
            usbflags
               <vvvvpppprrrr>
                  <Device-specific registry entry>
```

In the ***vvvvpppprrrr*** key,

- ***vvvv*** is a 4-digit hexadecimal number that identifies the vendor
- ***pppp*** is a 4-digit hexadecimal number that identifies the product
- ***rrrr*** is a 4-digit hexadecimal number that contains the revision number of the device.

The vendor ID, product ID, and revision number values are obtained from the [USB device descriptor](usb-device-descriptors.md). The [USB_DEVICE_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_device_descriptor) structure describes a device descriptor.

The following table describes the possible registry entries for the ***vvvvpppprrrr*** key. The USB driver stack considers these entries to be read-only values.

| Registry entry | Description | Possible values |
|---|---|---|
| **osvc**<br><br>REG_BINARY | Indicates whether the operating system queried the device for [Microsoft-defined USB descriptors](microsoft-defined-usb-descriptors.md). If the previously attempted OS descriptor query was successful, the value contains the vendor code from the OS string descriptor. | <ul><li>0x0000: The device didn't provide a valid response to the Microsoft OS string descriptor request.</li><li>0x01xx: The device provided a valid response to the Microsoft OS string descriptor request, where xx is the **bVendorCode** contained in the response.</li></ul> |
| **IgnoreHWSerNum**<br><br>REG_BINARY | Indicates whether the USB driver stack must ignore the serial number of the device. | <ul><li>0x00: The setting is disabled.</li><li>0x01: Forces the USB driver stack to ignore the serial number of the device. Therefore, the device instance is tied to the port to which the device is attached.</li></ul> |
| **ResetOnResume**<br><br>REG_BINARY | Indicates whether the USB driver stack must reset the device when the port resumes from a sleep cycle. | <ul><li>0x0000: The setting is disabled.</li><li>0x0001: Forces the USB driver stack to reset a device on port resume.</li></ul> |

## Find device information after it enumerates on Windows

View the device interface GUID, Hardware ID, and [device class](supported-usb-classes.md#usb-device-classes) information about your device

1. Find the device that exposes the device interface you are interested in and make note of the instance ID:

    ```cmd
    >pnputil /enum-interfaces /class {A5DCBF10-6530-11D2-901F-00C04FB951ED} /instanceid
    
    Microsoft PnP Utility
    
    Interface Path:         \\?\USB#VID_1395&PID_005A#0000000000#{a5dcbf10-6530-11d2-901f-00c04fb951ed}
    Interface Description:  Unknown
    Interface Class GUID:   {a5dcbf10-6530-11d2-901f-00c04fb951ed}
    Device Instance ID:     USB\VID_1395&PID_005A\0000000000
    Interface Status:       Enabled
     
    Interface Path:         \\?\USB#VID_045E&PID_0840#0C33CG9212501N0#{a5dcbf10-6530-11d2-901f-00c04fb951ed}
    Interface Description:  Unknown
    Interface Class GUID:   {a5dcbf10-6530-11d2-901f-00c04fb951ed}
    Device Instance ID:     USB\VID_045E&PID_0840\0C33CG9212501N0
    Interface Status:       Enabled
     
    Interface Path:         \\?\USB#VID_045E&PID_07A5#5&109d12e&0&1#{a5dcbf10-6530-11d2-901f-00c04fb951ed}
    Interface Description:  Unknown
    Interface Class GUID:   {a5dcbf10-6530-11d2-901f-00c04fb951ed}
    Device Instance ID:     USB\VID_045E&PID_07A5\5&109d12e&0&1
    Interface Status:       Enabled
    ```

1. Retrieve a list of the compatible IDs for the device and note the device class, subclass, and protocol codes:

    ```cmd
    >pnputil /enum-devices /instanceid "USB\VID_045E&PID_0840\0C33CG9212501N0" /ids
    
    Microsoft PnP Utility
    
    Instance ID:                USB\VID_045E&PID_0840\0C33CG9212501N0

    Device Description:         USB Composite Device

    Class Name:                 USB

    Class GUID:                 {36fc9e60-c465-11cf-8056-444553540000}

    Manufacturer Name:          (Standard USB Host Controller)

    Status:                     Started

    Driver Name:                usb.inf

    Hardware IDs:               USB\VID_045E&PID_0840&REV_0215
                                USB\VID_045E&PID_0840

    Compatible IDs:             USB\COMPAT_VID_045E&DevClass_00&SubClass_00&Prot00
                                USB\COMPAT_VID_045E&DevClass_00&SubClass_00
                                USB\COMPAT_VID_045E&DevClass_00
                                USB\DevClass_00&SubClass_00&Prot_00
                                USB\DevClass_00&SubClass_00
                                USB\DevClass_00
                                USB\COMPOSITE
    ```

## Related topics

- [Microsoft-provided USB drivers](system-supplied-usb-drivers.md)
- [USB device descriptor](usb-device-descriptors.md)
- [USB device class drivers included in Windows](supported-usb-classes.md)
- [Microsoft-defined USB descriptors](microsoft-defined-usb-descriptors.md)
