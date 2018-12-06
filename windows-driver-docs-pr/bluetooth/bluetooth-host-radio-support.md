---
title: Bluetooth host radio support
ms.assetid: 7AA53797-F8DC-4FA6-9A19-E20289AF50CA
description: Provides a list of questions and answers about Bluetooth host radio support in Windows
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth Host Radio Support


The following list provides a Bluetooth Radio Support Q&A:

- [Which Bluetooth host controllers does Windows support?](#targ1)
- [In Windows Vista, can the Bluetooth stack be forced to load if Windows cannot match the device ID?](#targ2)
- [How do I ensure in-box support for Bluetooth radios in Windows Vista?](#targ3)
- [Should third-party INF files use the Microsoft-defined class GUID?](#targ4)
- [Why is the Control Panel Bluetooth application missing in Windows 7?](#targ5)
- [Why does the Bluetooth icon not appear in the taskbar?](#targ6)
- [Does Windows support Bluetooth radio firmware updates?](#targ7)
- [Does Windows support vendor-specific pass-through commands?](#targ8)
- [Does Windows support vendor-supplied profiles?](#targ9)
- [Why are only some Bluetooth profiles and protocols enabled by default?](#targ10)
- [Can Group Policy block Bluetooth radio installation?](#targ11)
- [How do I change the Device ID Profile record published by Windows 8 and Windows 8.1?](#targ12)

## <span id="targ1"></span><span id="TARG1"></span>Which Bluetooth host controllers does Windows support?

With Windows, a Bluetooth radio can be packaged as an external dongle or embedded inside a computer but it must be connected to one of the computer’s USB ports. The Bluetooth stack that is included with Windows 7 and Windows Vista does not support Bluetooth radio connections over PCI, I2C, serial, Secure Digital I/O (SDIO), CompactFlash, or PC Card interfaces. In Windows 8 and Windows 8.1, radios connected over alternate transports can be added via a third-party bus driver. Refer to the Extensible Transport sections of the [Bluetooth Devices Reference](https://msdn.microsoft.com/library/windows/hardware/ff536585) for more information.

## <span id="targ2"></span><span id="TARG2"></span>In Windows Vista, can the Bluetooth stack be forced to load if Windows cannot match the device ID?


A new Bluetooth radio might not match any of the device IDs in the Bluetooth INF (Bth.inf) that is included with Windows. This prevents Windows from loading a Bluetooth stack for the device. IHVs should ensure that their radio works with the native Bluetooth stack in one of the following ways:

-   Create an INF for the radio that references Bth.inf. For an example of a vendor-specific INF file for a Bluetooth radio, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.md).
-   Store an extended compat ID OS descriptor in the device firmware that specifies an appropriate compatible and subcompatible ID. For information about extended compat ID OS descriptors, see [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?linkid=308932).
-   Force the Bluetooth stack to load

The following procedure summarizes how to use Device Manager to force the Bluetooth stack to load for a new radio:

1.  Run the Control Panel Device Manager application and identify the Bluetooth radio on the list of devices.
2.  To run the Update Driver Software Wizard, right-click the Bluetooth radio item and select **Update Driver Software**.
3.  Use the wizard to force the Bluetooth stack to install.

For a detailed description of this procedure, see [Appendix A: How to Install an In-Box Bluetooth Driver on New Hardware in Windows Vista](bluetooth-faq--appendix-a.md).

## <span id="targ3"></span><span id="TARG3"></span>How do I ensure in-box support for Bluetooth radios in Windows Vista?


IHVs should take the following steps to ensure that their Bluetooth radios have in box support on Windows:

-   Ensure that the radio supports the extended compat ID OS feature descriptor. For details, see [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?linkid=617154).
-   Obtain Windows Certification Program approval for the Bluetooth radio hardware and the associated INF file. For an example of a vendor-specific INF file for a Bluetooth radio, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.md).
-   Use the **Windows Dev Center - Hardware Dashboard** to make the INF file available through Windows Update

It is no longer possible to add radios to the in-box Bth.inf file for Windows Vista.

## <span id="targ4"></span><span id="TARG4"></span>Should third-party INF files use the Microsoft-defined class GUID?


IHVs should use the Microsoft-defined class globally unique identifier (GUID) ({e0cbf06c cd8b 4647 bb8a 263b43f0f974}) for Bluetooth devices only in those INF files that reference the in-box Bluetooth INF file (Bth.inf). This means that the device uses the native Windows co installer, services, and notification area icon. IHVs that implement their own Bluetooth stack must create a vendor-specific class GUID and use the WLK test tools to ensure that the stack complies with the unclassified Windows Certification Program.

## <span id="targ5"></span><span id="TARG5"></span>Why is the Control Panel Bluetooth application missing in Windows 7?


In Windows 7, the Control Panel Bluetooth application was incorporated into Devices and Printers. Thus, adjusting the Bluetooth radio settings, managing Bluetooth devices, and adding new Bluetooth devices can only be performed from within Devices and Printers.

## <span id="targ6"></span><span id="TARG6"></span>Why does the Bluetooth icon not appear in the taskbar?


If the Bluetooth icon does not appear in the taskbar, it could be due to one or more of the following reasons:

-   The Bluetooth radio is turned off.
-   The Bluetooth radio is in emulation mode
-   In the **Bluetooth Settings** dialog, the **Show the Bluetooth icon in the notification area** check box is not selected

## <span id="targ7"></span><span id="TARG7"></span>Does Windows support Bluetooth radio firmware updates?


Currently, the Bluetooth stack that is included with Windows does not directly support firmware updates. However, for Bluetooth radios connected through a USB port, Windows does support firmware updates in compliance with the USB Device Firmware Update (DFU) specification. IHVs can create a user-mode utility that communicates with their Bluetooth radio over the DFU interface to perform the firmware update and restart the radio.

## <span id="targ8"></span><span id="TARG8"></span>Does Windows support vendor-specific pass-through commands?


Windows 8.1, Windows 8, Windows 7, and Windows Vista with SP2 include support for vendor-specific pass-through commands. These kernel-mode interfaces are documented in the WDK.

## <span id="targ9"></span><span id="TARG9"></span>Does Windows support vendor-supplied profiles?


Windows 8.1, Windows 8, Windows 7, and Windows Vista support vendor-supplied Bluetooth profiles. However, Windows XP does not. The GUIDs for those profiles that have been standardized by the Bluetooth SIG are included in the in box INF file (Bth.inf).

When users pair a Bluetooth device with a computer, the device’s profiles are compared to the profiles that are listed in Bth.inf. If the device profile does not match one of those profiles, users receive a dialog box that asks them to provide appropriate vendor software.

Vendors that want a vendor-specific profile must use their own GUID and reference it in a vendor-specific INF file. This INF file can use Include and Needs directives to reference the appropriate Bth.inf sections and directives. For an example of a vendor-specific INF file, see [Appendix B: An Example of a Vendor-Provided INF File for Use in Windows Vista](bluetooth-faq--appendix-b.md).

## <span id="targ10"></span><span id="TARG10"></span>Why are only some Bluetooth profiles and protocols enabled by default?


The Bluetooth stack that is included with Windows provides in-box support for only some Bluetooth profiles. Vendors must implement the required services to support any other Bluetooth profiles, much as they do for USB and PCI. Windows can use the Bluetooth profiles that are enabled by default—referred to as supported profiles—to generate physical device objects (PDOs). This allows default loading of the drivers that are required to enable the profile. You can identify the supported profiles in the registry by looking at the SupportedServices and UnsupportedServices values under the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\Bthport \\Parameters** key.

**Note**  The Bthport key is added to the registry only after you install a Bluetooth device.

 

The following table lists the profiles in Bth.inf that Windows supports.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Service ID</p></td>
<td align="left"><p>Description</p></td>
</tr>
<tr class="even">
<td align="left"><p>{00001101-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>SPP</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001103-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>DUN</p></td>
</tr>
<tr class="even">
<td align="left"><p>{00001124-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>HID</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001126-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>HCRP</p></td>
</tr>
</tbody>
</table>

 

**Windows XP Bluetooth Profiles**
The following table lists the unsupported Bluetooth profiles and protocols. Note that, in this context, “unsupported” means that Windows does not automatically generate a PDO or devnode or display the Add New Hardware Wizard. Therefore, some in-box profiles and protocols are handled as if they are unsupported. For example, SDP is an in-box protocol that has a Bluetooth service ID but does not require a PDO. The SDP protocol is therefore marked as unsupported in Bth.inf to prevent the creation of a PDO

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Service ID</p></td>
<td align="left"><p>In-box</p></td>
<td align="left"><p>Description</p></td>
</tr>
<tr class="even">
<td align="left"><p>{0000110a-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Audio Source</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{0000110c-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>AV Remote Target</p></td>
</tr>
<tr class="even">
<td align="left"><p>{00001001-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Browse Group Service</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001111-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Fax Service</p></td>
</tr>
<tr class="even">
<td align="left"><p>{0000111f-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Handsfree Audio Gateway</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001112-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Headset Audio Gateway</p></td>
</tr>
<tr class="even">
<td align="left"><p>{00001104-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Infrared Mobile Communication (IRMC) Sync Service</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001107-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>IRMC Sync Commands</p></td>
</tr>
<tr class="even">
<td align="left"><p>{00001106-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Obex File Transfer</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001105-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Object Push</p></td>
</tr>
<tr class="even">
<td align="left"><p>{00001117-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>PAN group ad hoc network (GN)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001116-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>PAN network access point (NAP)</p></td>
</tr>
<tr class="even">
<td align="left"><p>{00001115-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>PAN U</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{0000112e-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Phone book client equipment (PCE) service</p></td>
</tr>
<tr class="even">
<td align="left"><p>{0000112f-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Phone book server equipment (PSE) service</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001200-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>PnP service</p></td>
</tr>
<tr class="even">
<td align="left"><p>{00001002-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Public Browse Group Service</p></td>
</tr>
<tr class="odd">
<td align="left"><p>{00001000-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>SDP</p></td>
</tr>
<tr class="even">
<td align="left"><p>{0000112d-0000-1000-8000-00805f9b34fb}</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Sim Access</p></td>
</tr>
</tbody>
</table>

 

If IHVs do not want Windows to automatically generate a PDO for their device, they can add the service GUID to the list of unsupported services. For examples, see Bth.inf.

## <span id="targ11"></span><span id="TARG11"></span>Can Group Policy block Bluetooth radio installation?


For details on how to use Group Policy to block the installation of Bluetooth radios, see the “Prevent installation of prohibited devices” section of [Step-by-Step Guide to Controlling Device Installation and Usage with Group Policy](http://go.microsoft.com/fwlink/p/?linkid=324335).

Use the following compatible IDs for the Bluetooth radio:

USB\\Class\_E0 (for USB based radios)
MS\_BTHX\_BTHMINI (for non-USB radios)
**Note**  This won’t remove Bluetooth driver support if it has already been installed. Also, this policy needs to be applied to the preinstall image.

 

## <span id="targ12"></span><span id="TARG12"></span>How do I change the Device ID Profile record published by Windows 8 and Windows 8.1?


The Device ID Profile defines an SDP record that can be used to provide identity information to remote devices. Previous and current Windows versions have used the Device ID record published on paired devices to provide device-specific Hardware IDs for generic Bluetooth services.

Beginning with Windows 8, Windows will also publish a local Device ID record to identify the Windows 8 device to remote Bluetooth devices. The default values can be adjusted by OEMs to better identify their specific Windows 8 device. These values are defined as in the following table under the HKLM\\System\\CCS\\services\\BTHPORT\\Parameters registry key:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>ValueName</p></td>
<td align="left"><p>Type</p></td>
<td align="left"><p>Description</p></td>
<td align="left"><p>Default Value</p></td>
</tr>
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

 

 

 





