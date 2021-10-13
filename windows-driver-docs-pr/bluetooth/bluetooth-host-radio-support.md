---
title: Bluetooth host radio support
description: Provides a list of questions and answers about Bluetooth host radio support in Windows
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth Host Radio Support

This topic provides answers to typical questions about Bluetooth Radio support.

## Bluetooth host controllers supported in Windows

With Windows, a Bluetooth radio can be packaged as an external dongle or embedded inside a computer but it must be connected to one of the computer’s USB ports. The Bluetooth stack that is included with Windows 7 and Windows Vista does not support Bluetooth radio connections over PCI, I2C, serial, Secure Digital I/O (SDIO), CompactFlash, or PC Card interfaces. In Windows 8 and Windows 8.1, radios connected over alternate transports can be added via a third-party bus driver. Refer to the Extensible Transport sections of the [Bluetooth Devices Reference](/windows-hardware/drivers/ddi/_bltooth/) for more information.

## Forcing the Bluetooth stack to load if Windows cannot match the device ID (Windows Vista)

A new Bluetooth radio might not match any of the device IDs in the Bluetooth INF (Bth.inf) that is included with Windows. This prevents Windows from loading a Bluetooth stack for the device. IHVs should ensure that their radio works with the native Bluetooth stack in one of the following ways:

* Create an INF for the radio that references Bth.inf. For an example of a vendor-specific INF file for a Bluetooth radio, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.yml).
* Store an extended compat ID OS descriptor in the device firmware that specifies an appropriate compatible and subcompatible ID. For information about extended compat ID OS descriptors, see [Microsoft OS Descriptors](/previous-versions/gg463179(v=msdn.10)).
* Force the Bluetooth stack to load

The following procedure uses Device Manager to force the Bluetooth stack to load for a new radio:

1. Run the Control Panel Device Manager application and identify the Bluetooth radio on the list of devices.
2. To run the Update Driver Software Wizard, right-click the Bluetooth radio item and select **Update Driver Software**.
3. Use the wizard to force the Bluetooth stack to install.

For a detailed description of this procedure, see [Appendix A: How to Install an In-Box Bluetooth Driver on New Hardware in Windows Vista](bluetooth-faq--appendix-a.yml).

## Ensure in-box support for Bluetooth radios

IHVs should take the following steps to ensure that their Bluetooth radios have in box support on Windows:

* Ensure that the radio supports the extended compat ID OS feature descriptor. For details, see [Microsoft OS Descriptors](../usbcon/microsoft-os-1-0-descriptors-specification.md).
* Obtain Windows Certification Program approval for the Bluetooth radio hardware and the associated INF file. For an example of a vendor-specific INF file for a Bluetooth radio, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.yml).
* Use the Partner Center to make the INF file available through Windows Update

It is no longer possible to add radios to the in-box Bth.inf file.

## Should third-party INF files use the Microsoft-defined class GUID

IHVs should use the Microsoft-defined class globally unique identifier (GUID) ({e0cbf06c cd8b 4647 bb8a 263b43f0f974}) for Bluetooth devices only in those INF files that reference the in-box Bluetooth INF file (Bth.inf). This means that the device uses the native Windows co installer, services, and notification area icon. IHVs that implement their own Bluetooth stack must create a vendor-specific class GUID and use the WLK test tools to ensure that the stack complies with the unclassified Windows Certification Program.

## Why the Control Panel Bluetooth application is missing

The Control Panel Bluetooth application was incorporated into Devices and Printers. Thus, adjusting the Bluetooth radio settings, managing Bluetooth devices, and adding new Bluetooth devices can only be performed from within Devices and Printers.

## Why the Bluetooth icon might not appear in the taskbar

If the Bluetooth icon does not appear in the taskbar, it could be due to one or more of the following reasons:

* The Bluetooth radio is turned off.
* The Bluetooth radio is in emulation mode.
* In the **Bluetooth Settings** dialog, the **Show the Bluetooth icon in the notification area** check box is not selected.

## Windows support for Bluetooth radio firmware updates

Currently, the Bluetooth stack that is included with Windows does not directly support firmware updates. However, for Bluetooth radios connected through a USB port, Windows does support firmware updates in compliance with the USB Device Firmware Update (DFU) specification. IHVs can create a user-mode utility that communicates with their Bluetooth radio over the DFU interface to perform the firmware update and restart the radio.

## Windows support for vendor-specific pass-through commands

Windows includes support for vendor-specific pass-through commands. These kernel-mode interfaces are documented in the WDK.

## Windows support for vendor-supplied profiles

Windows supports vendor-supplied Bluetooth profiles. The GUIDs for those profiles that have been standardized by the Bluetooth SIG are included in the in box INF file (Bth.inf).

When users pair a Bluetooth device with a computer, the device’s profiles are compared to the profiles that are listed in Bth.inf. If the device profile does not match one of those profiles, users receive a dialog box that asks them to provide appropriate vendor software.

Vendors that want a vendor-specific profile must use their own GUID and reference it in a vendor-specific INF file. This INF file can use Include and Needs directives to reference the appropriate Bth.inf sections and directives. For an example of a vendor-specific INF file, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.yml).

## Bluetooth profiles and protocols that are enabled by default

The Bluetooth stack included with Windows provides in-box support for only some Bluetooth profiles. Vendors must implement the required services to support any other Bluetooth profiles, much as they do for USB and PCI. Windows can use the Bluetooth profiles that are enabled by default—referred to as supported profiles—to generate physical device objects (PDOs). This enables default loading of the drivers that are required to enable the profile. You can identify the supported profiles in the registry by looking at the SupportedServices and UnsupportedServices values under the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\Bthport \\Parameters** key.

> [!NOTE]
> The Bthport key is added to the registry only after you install a Bluetooth device.

The following table lists the profiles in Bth.inf that Windows supports.

|Service ID|Description|
|----|----|
|{00001101-0000-1000-8000-00805f9b34fb}|SPP|
|{00001103-0000-1000-8000-00805f9b34fb}|DUN
|{00001124-0000-1000-8000-00805f9b34fb}|HID|
|{00001126-0000-1000-8000-00805f9b34fb}|HCRP|

### Windows Bluetooth Profiles

For a Bluetooth-enabled device or accessory to work with your PC that’s running Windows 10, the device needs to use one of the supported Bluetooth profiles. See the most current list at [Supported Bluetooth profiles](https://support.microsoft.com/help/10568/windows-10-supported-bluetooth-profiles).

If IHVs do not want Windows to automatically generate a PDO for their device, they can add the service GUID to the list of unsupported services. For examples, see Bth.inf.

## How Group Policy can block Bluetooth radio installation

For details on how to use Group Policy to block the installation of Bluetooth radios, see the “Prevent installation of prohibited devices” section of [Step-by-Step Guide to Controlling Device Installation and Usage with Group Policy](/previous-versions/dotnet/articles/bb530324(v=msdn.10)).

Use the following compatible IDs for the Bluetooth radio:

USB\\Class\_E0 (for USB based radios)
MS\_BTHX\_BTHMINI (for non-USB radios)

> [!NOTE]
> This won’t remove Bluetooth driver support if it has already been installed. Also, this policy needs to be applied to the preinstall image.

## How to change the Device ID Profile record published by Windows

The Device ID Profile defines an SDP record that can be used to provide identity information to remote devices. Previous and current Windows versions have used the Device ID record published on paired devices to provide device-specific Hardware IDs for generic Bluetooth services.

Windows also publishes a local Device ID record to identify the Windows device to remote Bluetooth devices. The default values can be adjusted by OEMs to better identify their specific Windows device. These values are defined as in the following table under the HKLM\\System\\CCS\\services\\BTHPORT\\Parameters registry key:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="odd">
<th align="left"><p>ValueName</p></th>
<th align="left"><p>Type</p></th>
<th align="left"><p>Description</p></th>
<th align="left"><p>Default Value</p></th>
</tr>
</thead>
<tbody>
<tr class="even">
<td align="left"><p>DIDVendorIDSource</p></td>
<td align="left"><p>DWORD</p></td>
<td align="left"><p>0x01 = Bluetooth SIG namespace</p>
<p>0x02 = USB Forum namespace</p></td>
<td align="left"><p>0x01</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DIDVendorID</p></td>
<td align="left"><p>DWORD</p></td>
<td align="left"><p>OEM specified VendorID</p></td>
<td align="left"><p>0x06 – Microsoft Vendor ID</p></td>
</tr>
<tr class="even">
<td align="left"><p>DIDProductID</p></td>
<td align="left"><p>DWORD</p></td>
<td align="left"><p>OEM specified ProductID</p></td>
<td align="left"><p>0x01 – Microsoft Windows</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DIDVersion</p></td>
<td align="left"><p>DWORD</p></td>
<td align="left"><p>OEM specified product version</p></td>
<td align="left"><p>0x0800 – Windows 8</p></td>
</tr>
</tbody>
</table>
