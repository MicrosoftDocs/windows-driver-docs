---
title: WinUSB (Winusb.sys) Installation for Developers
description: Install WinUSB (Winusb.sys) in the device's kernel-mode stack as the USB device's function driver instead of implementing a driver.
ms.date: 03/26/2025

---

# WinUSB (Winusb.sys) installation for developers

For certain Universal Serial Bus (USB) devices, you can install [WinUSB](introduction-to-winusb-for-developers.md) (*Winusb.sys*) instead of implementing a driver.

> [!IMPORTANT]
> This article is for programmers. If you're a customer experiencing USB problems, see [Fix USB-C problems in Windows](https://support.microsoft.com/windows/fix-usb-c-problems-in-windows-f4e0e529-74f5-cdae-3194-43743f30eed2)

## Automatic installation of WinUSB without an INF file

As an OEM or independent hardware vendor (IHV), you can build your device so that the *Winusb.sys* gets installed automatically. Such a device is called a WinUSB device and doesn't require you to write a custom INF file that references in-box *Winusb.inf*.

When you connect a WinUSB device, Windows reads device information and loads *Winusb.sys* automatically.

For more information, see [WinUSB Device](automatic-installation-of-winusb.md).

## Installing WinUSB by specifying the system-provided device class

When you connect your device, you might notice that Windows loads *Winusb.sys* automatically. Otherwise, follow these instructions to load the driver:

1. Plug in your device to the host system.
1. Open **Device Manager** and locate the device.
1. Right-click the device and select **Update driver software...** from the context menu.
1. In the wizard, select **Browse my computer for driver software**.
1. Select **Let me pick from a list of device drivers on my computer**.
1. From the list of device classes, select **Universal Serial Bus devices**.
1. The wizard displays **WinUsb Device**. Select it to load the driver.

If **Universal Serial Bus devices** doesn't appear in the list of device classes, then you need to install the driver by using a custom INF.
The preceding procedure doesn't add a device interface GUID for an app (UWP app or Windows desktop app) to access the device. You must add the GUID manually by following this procedure.

1. Load the driver as described in the preceding procedure.
1. Generate a device interface GUID for your device by using a tool such as guidgen.exe.
1. Find the registry key for the device under this key:

    **HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\USB\\<VID_vvvv&PID_pppp>**

1. Under the **Device Parameters** key, add a *String* registry entry named **DeviceInterfaceGUID** or a *Multi-String* entry named **DeviceInterfaceGUIDs**. Set the value to the GUID you generated in step 2.
1. Disconnect the device from the system and reconnect it to the same physical port.

      > [!NOTE]
    > If you change the physical port, you must repeat steps 1 through 4.

## Writing a custom INF for WinUSB installation

As part of the driver package, you provide an .inf file that installs *Winusb.sys* as the function driver for the USB device.

Here's an example of a universal INF file that is valid for both x64 and ARM64 platforms running Windows 10 or later. This example doesn't include coinstallers, making it eligible for signing by the [Hardware Developer Center Dashboard](https://partner.microsoft.com/dashboard/home) portal.

```inf
;
; Universal INF file for WinUsb installation
;

[Version]
Signature   = "$Windows NT$"
Class       = USBDevice
ClassGUID   = {88BAE032-5A81-49f0-BC3D-A4FF138216D6}
Provider    = %ManufacturerName%
CatalogFile = WinUSBInstallation.cat
DriverVer   = 09/04/2012,13.54.20.543
PnpLockdown = 1

; ========== Manufacturer and Models sections ===========

[Manufacturer]
%ManufacturerName% = Standard,NTamd64,NTarm64

[Standard.NTamd64]
%DeviceName% =USB_Install, USB\VID_0547&PID_1002

[Standard.NTarm64]
%DeviceName% =USB_Install, USB\VID_0547&PID_1002

; =================== Installation ===================

[USB_Install]
Include = winusb.inf
Needs   = WINUSB.NT

[USB_Install.Services]
Include =winusb.inf
Needs   = WINUSB.NT.Services

[USB_Install.HW]
AddReg=Dev_AddReg

[Dev_AddReg]
HKR,,DeviceInterfaceGUIDs,0x10000,"{9f543223-cede-4fa3-b376-a25ce9a30e74}"

; =================== Strings ===================

[Strings]
ManufacturerName="Contoso"
ClassName="Universal Serial Bus devices"
DeviceName="Fx2 Learning Kit Device"
REG_MULTI_SZ = 0x00010000
```

This universal INF file can be used across multiple Windows platforms (x64 and ARM64) and is eligible to be signed by the [Hardware Developer Center Dashboard](https://partner.microsoft.com/dashboard/home) portal.

To install only a new custom device setup class, include a ClassInstall32 section in a device INF file. INF files for devices in an installed class, whether a system-supplied device setup class or a custom class, must not include a ClassInstall32 section.

Except for device-specific values and several issues that are noted in the following list, you can use these sections and directives to install WinUSB for any USB device. These list items describe the **Includes** and **Directives** in the preceding .inf file.

- **USB_Install**: The **Include** and **Needs** directives in the **USB_Install** section are required for installing WinUSB. You shouldn't modify these directives.
- **USB_Install.Services**: The **Include** directive in the **USB_Install.Services** section includes the system-supplied .inf for WinUSB (*Winusb.inf*). Windows installs this .inf file if it isn't already on the target system. The **Needs** directive specifies the section within *Winusb.inf* that contains information required to install *Winusb.sys* as the device's function driver. You shouldn't modify these directives.
- **USB_Install.HW**: This section is the key in the .inf file. It specifies the device interface globally unique identifier (GUID) for your device. The **AddReg** directive sets the specified interface GUID in a standard registry value. When *Winusb.sys* is loaded as the device's function driver, it reads the registry value DeviceInterfaceGUIDs key and uses the specified GUID to represent the device interface. You should replace the GUID in this example with one that you create specifically for your device. If the protocols for the device change, create a new device interface GUID.

  > [!NOTE]
  > User-mode software must call **[SetupDiGetClassDevs](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw)** to enumerate the registered device interfaces that are associated with one of the device interface classes specified under the DeviceInterfaceGUIDs key. **SetupDiGetClassDevs** returns the device handle for the device that the user-mode software must then pass to the [**WinUsb_Initialize**](/windows/win32/api/winusb/nf-winusb-winusb_initialize) routine to obtain a WinUSB handle for the device interface. For more info about these routines, see [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md).

Each time *Winusb.sys* loads, it registers a device interface that has the device interface classes that are specified in the registry under the **DeviceInterfaceGUIDs** key.

`HKR,,DeviceInterfaceGUIDs, 0x10000,"{D696BFEB-1734-417d-8A04-86D01071C512}"`

## How to create a driver package that installs Winusb.sys

To use WinUSB as the device's function driver, you create a driver package. Here are the steps to create a driver package the installs *Winusb.sys*:

1. [Download the Windows Driver Kit (WDK)](../download-the-wdk.md) and install it on your machine.
1. Create a driver package folder on your system where the USB device is connected, C:\\UsbDevice, for example.
1. Write an .inf file that installs *Winusb.sys* as the function driver for the USB device and save it in the driver package folder. An example of how to write this file can be found in the [Writing a custom INF for WinUSB installation](#writing-a-custom-inf-for-winusb-installation) section of this document.
1. Create a signed catalog file for the package. This file is required to install WinUSB on Windows. You can find more info about how to create and test signed catalog files in [Kernel-Mode Code Signing Walkthrough](/windows-hardware/test/hlk/) on the Windows Dev Center - Hardware site.

    :::image type="content" source="images/winusb-package.jpg" alt-text="Diagram showing the contents of a WinUSB driver installation package":::

1. Connect the USB device to your computer.
1. Open **Device Manager** on your computer. Follow the instructions on the **Update Driver Software** wizard and choose manual installation. When prompted, provide the location of the driver package folder to complete the installation.

## Related topics

- [WinUSB Architecture and Modules](winusb-architecture.md)
- [Choosing a driver model for developing a USB client driver](winusb-considerations.md)
- [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)
- [WinUSB Power Management](winusb-power-management.md)
- [WinUSB Functions for Pipe Policy Modification](winusb-functions-for-pipe-policy-modification.md)
- [WinUSB functions](using-winusb-api-to-communicate-with-a-usb-device.md)
- [Introduction to WinUSB for Developers](introduction-to-winusb-for-developers.md)
