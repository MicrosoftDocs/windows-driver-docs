---
title: WinUSB Device
description: Learn about how Windows recognizes a WinUSB device. You can load the Winusb.sys driver without having to provide a custom INF file.
ms.date: 10/27/2025
ms.topic: concept-article
#customer intent: As a software developer, I need to know how to use Winusb.sys as a driver without having to provide an INF file for devices that my team creates.
---

# WinUSB device

This article describes how Windows recognizes a WinUSB device. Manufacturers and independent hardware vendors (IHV) can use the information in this article to develop a device that uses Winusb.sys as the function driver. This article shows you how to load the driver automatically without having to provide a custom information (INF) file.

## What is a WinUSB device

A WinUSB device is a Universal Serial Bus (USB) device whose firmware defines certain Microsoft operating system (OS) feature descriptors that report `WINUSB` as the compatible ID.

The purpose of a WinUSB device is to enable Windows to load Winusb.sys as the device's function driver without a custom INF file. For a WinUSB device, you aren't required to distribute INF files for your device, which makes the driver installation process simple for end users. Conversely, if you need to provide a custom INF, you shouldn't define your device as a WinUSB device and specify the hardware ID of the device in the INF.

Microsoft provides a Winusb.inf file that contains information required to install Winusb.sys as the device driver for a USB device.

Before Windows 8, to load Winusb.sys as the function driver, you needed to provide a custom INF. The custom INF specifies the device-specific hardware ID and also includes sections from the in-box Winusb.inf. Those sections are required for instantiating the service, copying inbox binaries, and registering a device interface GUID that applications required to find the device and talk to it. For more information, see [Writing a custom INF for WinUSB installation](winusb-installation.md#writing-a-custom-inf-for-winusb-installation).

In Windows 8, the in-box Winusb.inf file is updated to enable Windows to automatically match the INF with a WinUSB device.

## WinUSB device installation by using the in-box Winusb.inf

In Windows 8, the in-box Winusb.inf file is updated. The INF includes an install section that references a compatible ID called **USB\\MS_COMP_WINUSB**.

```inf
[Generic.Section.NTamd64]
%USB\MS_COMP_WINUSB.DeviceDesc%=WINUSB,USB\MS_COMP_WINUSB
```

The updated INF also includes a new setup class called *USBDevice*.

The USBDevice setup class is available for those devices for which Microsoft doesn't provide an in-box driver. Typically, such devices don't belong to well-defined USB classes, such as Audio or Bluetooth, and require a custom driver. If your device is a WinUSB device, most likely, the device doesn't belong to a USB class. Your device must be installed under the USBDevice setup class. The updated Winusb.inf facilitates that requirement.

### About using the USBDevice class

Don't use the USB setup class for unclassified devices. That class is reserved for installing controllers, hubs, and composite devices. Misusing the USB class can lead to significant reliability and performance issues. Use USBDevice for unclassified devices.

In Windows 8, add this definition to your INF file to use the USBDevice device class:

```inf
  [Version]
  ...
  Class=USBDevice
  ClassGuid={88BAE032-5A81-49f0-BC3D-A4FF138216D6}
  ...
```

In Device Manager, see a new node called **USB Universal Serial Bus devices**. Your device appears under that node.

In Windows 7, in addition to the preceding lines, you need to create these registry settings in the INF:

```inf
  ;---------- Add Registry Section ----------
  [USBDeviceClassReg]
  HKR,,,,"Universal Serial Bus devices"
  HKR,,NoInstallClass,,1
  HKR,,SilentInstall,,1
  HKR,,IconPath,%REG_MULTI_SZ%,"%systemroot%\system32\setupapi.dll,-20"
```

In Device Manager, your device appears under **USB Universal Serial Bus devices**. The device class description is derived from the registry setting specified in your INF.

The USBDevice class isn't limited to WinUSB. If you have a custom driver for your device, you can use the USBDevice setup class in the custom INF.

During device enumeration, the USB driver stack reads the compatible ID from the device. If `WINUSB` is the compatible ID, Windows uses it as the device identifier and finds a match in the updated in-box Winusb.inf, and then loads Winusb.sys as the device's function driver.

This image is for a single interface Microsoft USB Test Tool (MUTT) device that is defined as a WinUSB device and as a result Winusb.sys gets loaded as the function driver for the device.

:::image type="content" source="images/winusb-device.png" alt-text="Screenshot of Windows Device Manager showing a WinUSB device.":::

For versions of Windows earlier than Windows 8, the updated Winusb.inf is available through Windows Update. If your computer is configured to get driver update automatically, WinUSB driver gets installed without any user intervention by using the new INF package.

## How to change the device description for a WinUSB device

For a WinUSB device, Device Manager shows `WinUsb Device` as the device description. That string is derived from Winusb.inf. If there are multiple WinUSB devices, all devices get the same device description.

To uniquely identify and differentiate the device in Device Manager, Windows 8 provides a new property on a device class. The property instructs the system to give precedence to the device description reported by the device in its **iProduct** string descriptor over the description in the INF. The USBDevice class defined in Windows 8 sets this property.

When a device is installed under the USBDevice class, Windows queries the device for a device description and sets the Device Manager string to whatever is retrieved in the query. In that case, the device description provided in the INF is ignored. Notice the device description strings: **MUTT** in the preceding image. The USB device provides the string in its product string descriptor.

The new class property isn't supported on earlier versions of Windows. To have a customized device description on an earlier version of Windows, you have to write your own custom INF.

## How to configure a WinUSB device

To identify a USB device as a WinUSB device, the device firmware must have Microsoft OS descriptors. For more information, see [Microsoft OS descriptors for USB devices](microsoft-defined-usb-descriptors.md).

### Supporting extended feature descriptors

For the USB driver stack to know that the device supports extended feature descriptors, the device must define an OS string descriptor stored at string index `0xEE`. During enumeration, the driver stack queries for the string descriptor. If the descriptor is present, the driver stack assumes that the device contains one or more OS feature descriptors and the data that is required to retrieve those feature descriptors.

The retrieved string descriptor has a **bMS_VendorCode** field value. The value indicates the vendor code that the USB driver stack must use to retrieve the extended feature descriptor.

To define an OS string descriptor, see [Microsoft OS descriptors for USB devices](microsoft-defined-usb-descriptors.md#why-does-windows-issue-a-string-descriptor-request-to-index-0xee).

### Setting the compatible ID

An extended compatible ID OS feature descriptor is required to match the in-box Winusb.inf and load the WinUSB driver module.

The extended compatible ID OS feature descriptor includes a header section followed by one or more function sections, depending on whether the device is composite or noncomposite. The header section specifies the length of the entire descriptor, number of function sections, and version number.

For a noncomposite device, the header is followed by one function section associated with the device's only interface. The **compatibleID** field of that section must specify `WINUSB` as the field value. For a composite device, there are multiple function sections. The **compatibleID** field of each function section must specify `WINUSB`.

### Registering a device interface GUID

An extended properties OS feature descriptor is required to register its device interface GUID. The GUID is required to find the device from an application or service, configure the device, and perform I/O operations.

In previous versions of Windows, device interface GUID registration is done through the custom INF. Starting in Windows 8, your device should report the interface GUID by using extended properties OS feature descriptor.

The extended properties OS feature descriptor includes a header section that is followed by one or more custom property sections. The header section describes the entire extended properties descriptor, including its total length, the version number, and the number of custom property sections. To register the device interface GUID, add a custom property section that sets the **bPropertyName** field to `DeviceInterfaceGUID` and **wPropertyNameLength** to 40 bytes.

Generate a unique device interface GUID by using a GUID generator and set the **bPropertyData** field to that GUID, such as `{8FE6D4D7-49DD-41E7-9486-49AFC6BFE475}`. The GUID is specified as a Unicode string and the length of the string is 78 bytes, including the null terminator.

| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|
| **bPropertyData** | 78 bytes | 7B 00 38 00 46 00 45 00 36 00 44 00 34 00 44 00 37 00 2D 00 34 00 39 00 00 44 00 2D 00 34 00 31 00 45 00 37 00 2D 00 39 00 34 00 38 00 36 00 2D 00 34 00 39 00 41 00 46 00 43 00 36 00 42 00 46 00 45 00 34 00 37 00 35 00 7D 00 00 00 | Property value is {8FE6D4D7-49DD-41E7-9486-49AFC6BFE475}. |

During device enumeration, The USB driver stack then retrieves the **DeviceInterfaceGUID** value from the extended properties OS feature descriptor and registers the device in the device's hardware key. An application can retrieve the value by using **SetupDiXxx** APIs. See [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey). For more information, see [Access a USB device by using WinUSB functions](using-winusb-api-to-communicate-with-a-usb-device.md).

### Enabling or disabling WinUSB power management features

Before Windows 8, to configure power management features of WinUSB, you had to write registry entry values in the **HW.AddReg** section of your custom INF.

In Windows 8 and later, you can specify power settings in device. You can report values through the extended properties OS feature descriptor that enable or disable features in WinUSB for that device. There are two features that you can configure: *selective suspend* and *system wake*. Selective suspend allows the device to enter low-power state when it's idle. System wake refers to the ability of a device to wake up a system when the system is in low-power state.

For more information, see [WinUSB Power Management](winusb-power-management.md).

| Property name | Description |
|---|---|
| DeviceIdleEnabled | This value is set to 1 to indicate that the device can power down when idle (selective suspend). |
| DefaultIdleState | This value is set to 1 to indicate that the device can be suspended when idle by default. |
| DefaultIdleTimeout | This value is set to 5000 in milliseconds to indicate the amount of time in milliseconds to wait before determining that a device is idle. |
| UserSetDeviceIdleEnabled | This value is set to 1 to allow the user to control the ability of the device to enable or disable USB selective suspend. There's a checkbox **Allow the computer to turn off this device to save power** in the device **Power Management** property page. Users can enable or disable USB selective suspend. |
| SystemWakeEnabled | This value is set to 1 to allow the user to control the ability of the device to wake the system from a low-power state. When enabled, the **Allow this device to wake the computer** checkbox appears in the device **Power Management** property page. The user can enable or disable USB system wake. |

For example, to enable selective suspend on the device, add a custom property section that sets the **bPropertyName** field to a Unicode string `DeviceIdleEnabled` and **wPropertyNameLength** to 36 bytes. Set the **bPropertyData** field to `0x00000001`. The property values are stored as little-endian 32-bit integers.

During enumeration, the USB driver stack reads the extended properties feature descriptors and creates registry entries under this key:

**HKEY_LOCAL_MACHINE**\\**System**\\**CurrentControlSet**\\**Enum**\\**USB**\\***&lt;Device Identifier&gt;***\\***&lt;Instance Identifier&gt;***\\**Device Parameters**

This image shows sample settings for a WinUSB device.

:::image type="content" source="images/winusb-device-reg.png" alt-text="Screenshot of Windows Registry Editor showing settings for a WinUSB device.":::

For more examples, see [Microsoft OS descriptors](microsoft-defined-usb-descriptors.md).

## Related content

- [Microsoft OS descriptors for USB devices](microsoft-defined-usb-descriptors.md)
