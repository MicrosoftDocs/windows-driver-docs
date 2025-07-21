---
title: Bluetooth Host Radio Support
description: Provides a list of questions and answers about Bluetooth host radio support in Windows
ms.date: 03/05/2025
ms.topic: faq
---

# Bluetooth Host Radio Support

This article provides answers to typical questions about Bluetooth Radio support.

## Bluetooth host controllers supported in Windows

With Windows, a Bluetooth radio can be packaged as an external dongle or embedded inside a computer but it must be connected to one of the computer's USB ports. For more information, see the [Bluetooth Devices Reference](/windows-hardware/drivers/ddi/_bltooth/).

## Forcing the Bluetooth stack to load if Windows can't match the device ID (Windows Vista)

A new Bluetooth radio might not match any of the device IDs in the Bluetooth INF (Bth.inf) that is included with Windows. A missing match prevents Windows from loading a Bluetooth stack for the device. Ensure that your radio works with the native Bluetooth stack in one of the following ways:

- Create an INF for the radio that references Bth.inf. For an example of a vendor-specific INF file for a Bluetooth radio, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.yml).
- Store an extended compatible ID OS descriptor in the device firmware that specifies an appropriate compatible and subcompatible ID. For information about extended compatible ID OS descriptors, see [Microsoft OS Descriptors](/previous-versions/gg463179(v=msdn.10)).
- Force the Bluetooth stack to load

The following procedure uses Device Manager to force the Bluetooth stack to load for a new radio:

1. Run the Control Panel Device Manager application and identify the Bluetooth radio on the list of devices.
1. To run the Update Driver Software Wizard, right-click the Bluetooth radio item and select **Update Driver Software**.
1. Use the wizard to force the Bluetooth stack to install.

For a detailed description of this procedure, see [Appendix A: How to Install an In-Box Bluetooth Driver on New Hardware in Windows Vista](bluetooth-faq--appendix-a.yml).

## Ensure in-box support for Bluetooth radios

IHVs should take the following steps to ensure that their Bluetooth radios have in box support on Windows:

- Ensure that the radio supports the extended compatible ID OS feature descriptor. For details, see [Microsoft OS Descriptors](../usbcon/microsoft-os-1-0-descriptors-specification.md).
- Obtain Windows Certification Program approval for the Bluetooth radio hardware and the associated INF file. For an example of a vendor-specific INF file for a Bluetooth radio, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.yml).
- Use the Partner Center to make the INF file available through Windows Update

It's no longer possible to add radios to the in-box Bth.inf file.

## INF files using the Microsoft-defined class GUID

Use the Microsoft-defined class globally unique identifier (GUID) ({e0cbf06c cd8b 4647 bb8a 263b43f0f974}) for Bluetooth devices only in those INF files that reference the in-box Bluetooth INF file (Bth.inf). The device uses the native Windows installer, services, and notification area icon. If you implement your own Bluetooth stack, you must create a vendor-specific class GUID and use the WLK test tools to ensure that the stack complies with the unclassified Windows Certification Program.

## Why the Control Panel Bluetooth application is missing

The Control Panel Bluetooth application was incorporated into Devices and Printers. Thus, adjusting the Bluetooth radio settings, managing Bluetooth devices, and adding new Bluetooth devices can only be performed from within Devices and Printers.

## Why the Bluetooth icon might not appear in the taskbar

If the Bluetooth icon doesn't appear in the taskbar, it could be due to one or more of the following reasons:

- The Bluetooth radio is turned off.
- The Bluetooth radio is in emulation mode.
- In the **Bluetooth Settings** dialog, the **Show the Bluetooth icon in the notification area** check box isn't selected.

## Windows support for Bluetooth radio firmware updates

Currently, the Bluetooth stack that is included with Windows doesn't directly support firmware updates. However, for Bluetooth radios connected through a USB port, Windows does support firmware updates in compliance with the USB Device Firmware Update (DFU) specification. IHVs can create a user-mode utility that communicates with their Bluetooth radio over the DFU interface to perform the firmware update and restart the radio.

## Windows support for vendor-specific pass-through commands

Windows includes support for vendor-specific pass-through commands. These kernel-mode interfaces are documented in the WDK.

## Windows support for vendor-supplied profiles

Windows supports vendor-supplied Bluetooth profiles. The GUIDs for those profiles standardized by the Bluetooth SIG are included in the in box INF file (Bth.inf).

When users pair a Bluetooth device with a computer, the device's profiles are compared to the profiles that are listed in Bth.inf. If the device profile doesn't match one of those profiles, users receive a dialog box that asks them to provide appropriate vendor software.

Vendors that want a vendor-specific profile must use their own GUID and reference it in a vendor-specific INF file. This INF file can use Include and Needs directives to reference the appropriate Bth.inf sections and directives. For an example of a vendor-specific INF file, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.yml).

## Bluetooth profiles and protocols that are enabled by default

The Bluetooth stack included with Windows provides in-box support for only some Bluetooth profiles. Vendors must implement the required services to support any other Bluetooth profiles, much as they do for USB and PCI. Windows can use the Bluetooth profiles that are enabled by default—referred to as supported profiles—to generate physical device objects (PDOs). This enables default loading of the drivers that are required to enable the profile. You can identify the supported profiles in the registry by looking at the SupportedServices and UnsupportedServices values under the **HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\Bthport \\Parameters** key.

> [!NOTE]
> The Bthport key is added to the registry only after you install a Bluetooth device.

The following table lists the profiles in Bth.inf that Windows supports.

| Service ID | Description |
|--|--|
| {00001101-0000-1000-8000-00805f9b34fb} | SPP |
| {00001103-0000-1000-8000-00805f9b34fb} | DUN |
| {00001124-0000-1000-8000-00805f9b34fb} | HID |
| {00001126-0000-1000-8000-00805f9b34fb} | HCRP |

### Windows Bluetooth Profiles

For a Bluetooth-enabled device or accessory to work with your PC running Windows 10, the device needs to use one of the supported Bluetooth profiles. See the list at [Bluetooth Version and Profile Support in Previous Windows Versions](bluetooth-support-in-previous-windows-versions.md).

If IHVs don't want Windows to automatically generate a PDO for their device, they can add the service GUID to the list of unsupported services. For examples, see Bth.inf.

## How Group Policy can block Bluetooth radio installation

For details on how to use Group Policy to block the installation of Bluetooth radios, see the "Prevent installation of prohibited devices" section of [Step-by-Step Guide to Controlling Device Installation and Usage with Group Policy](/previous-versions/dotnet/articles/bb530324(v=msdn.10)).

Use the following compatible IDs for the Bluetooth radio:

USB\\Class_E0 (for USB based radios)
MS_BTHX_BTHMINI (for non-USB radios)

> [!NOTE]
> Blocking Bluetooth radio installation doesn't remove Bluetooth driver support if it's already installed. Also, this policy must be applied to the preinstalled image.

## How to change the Device ID Profile record published by Windows

The Device ID Profile defines an SDP record that can be used to provide identity information to remote devices. Windows uses the Device ID record published on paired devices to provide device-specific Hardware IDs for generic Bluetooth services.

Windows also publishes a local Device ID record to identify the Windows device to remote Bluetooth devices. You can adjust the default values to better identify your specific Windows device. These values are defined as in the following table under the HKLM\\System\\CCS\\services\\BTHPORT\\Parameters registry key:

| ValueName | Type | Description | Default Value |
|--|--|--|--|
| DIDVendorIDSource | DWORD | 0x01 = Bluetooth SIG namespace</br>0x02 = USB Forum namespace | 0x01 |
| DIDVendorID | DWORD | OEM specified VendorID | 0x06 – Microsoft Vendor ID |
| DIDProductID | DWORD | OEM specified ProductID | 0x01 – Microsoft Windows |
| DIDVersion | DWORD | OEM specified product version | 0x0800 – Windows 8 |
