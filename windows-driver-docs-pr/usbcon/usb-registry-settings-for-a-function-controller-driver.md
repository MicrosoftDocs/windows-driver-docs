---
Description: OEMs must set several registry values to make sure that their device enumerates with the correct metadata when connected to a computer.
title: USB registry settings for a function controller driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB registry settings for a function controller driver


**Summary**

-   Registry keys that must be set by OEMs to define USB descriptors.

**Applies to:**

-   Windows 10

**Last updated:**

-   November 2015

OEMs must set several registry values to make sure that their device enumerates with the correct metadata when connected to a computer. These values specify device and configuration descriptors for the [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md). OEMs that create and include their own interfaces must set additional registry values in order for their interfaces to be loaded and used.

Registry keys related to the device-side USB drivers are under:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**

This topic describes settings for the preceding key and subkeys that define the device, configuration, and interface descriptors for the device.

## USBFN registry key


Configuration information for the USB device are under:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**

This table describes the subkeys that OEMs can modify under this key. More information about the supported values for each subkey is provided in sections below.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Subkey</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Alternates</strong></td>
<td>This subkey contains additional subkeys that describe an interface that has one or more alternate settings:
<p><strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong>&lt;strong&gt;Alternates</strong></p></td>
</tr>
<tr class="even">
<td><strong>Associations</strong></td>
<td>This subkey defines Interface Association Descriptors (IADs). Each IAD allows multiple interfaces to be grouped into a single function. Each subkey represents a different IAD and OEMs can modify the values for those subkeys.
<p><strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong>&lt;strong&gt;Associations</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Default</strong></td>
<td>This subkey contains default values that are used to describe device-specific settings such as the VID and PID. This is a Microsoft-owned subkey whose values are overridden by those in the parent key:
<p><strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong></p></td>
</tr>
<tr class="even">
<td><strong>Configurations</strong></td>
<td>This subkey contains additional subkeys that contain configuration descriptor values that are used during USB enumeration. For example, the standard test configuration might exist under <strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong>&lt;strong&gt;Configurations</strong>&lt;strong&gt;TestConfigClassic</strong>.</td>
</tr>
<tr class="odd">
<td><strong>Configurations\Default</strong></td>
<td>This subkey contains values for the default configuration. The interfaces in the default configuration are added before the current configuration present when the <strong>IncludeDefaultCfg</strong> value is set under the <strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong> key.</td>
</tr>
<tr class="even">
<td><strong>Interfaces</strong></td>
<td>This subkey contains additional subkeys that describe specific interface descriptors. For example, the IP over USB configuration may reside under a subkey named <strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong>&lt;strong&gt;Interfaces</strong>&lt;strong&gt;IpOverUsb</strong>. The name of this subkey for an interface is what determines the hardware ID of the class driver. In the IP over USB example, the _HID of the loaded PDO is <strong>USBFN\IpOverUsb</strong>.</td>
</tr>
</tbody>
</table>

 

This table describes the values that OEMs can modify in the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN** key. Values that are not listed in this table assume the default values defined by Microsoft under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Default**.

All OEMs must set the **idVendor**, **idProduct**, **ManufacturerString**, and **ProductString** values. OEMs that create and add their own interfaces must also set **CurrentConfiguration** to the name of the subkey under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Configurations** that includes their interfaces in the **InterfaceList**.

| Value                    | Type       | Owner | Description                                                                                                                                                                                                                                                                                                                |
|--------------------------|------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **idVendor**             | REG\_DWORD | OEM   | The vendor identifier for the device descriptor that is sent to the host during enumeration.                                                                                                                                                                                                                               |
| **idProduct**            | REG\_DWORD | OEM   | The product identifier for the device descriptor that is sent to the host during enumeration.                                                                                                                                                                                                                              |
| **ManufacturerString**   | REG\_SZ    | OEM   | The manufacturer string that is sent to the host to identify the manufacturer of the device.                                                                                                                                                                                                                               |
| **ProductString**        | REG\_SZ    | OEM   | A string that describes the device as a product. The default value is Windows 10 Mobile Device. This value is used as the display name of the device in the connected computer's user interface. OEMs should make sure that this value matches the value of the PhoneModelName value under the DeviceTargetingInfo subkey. |
| **iSerialNumber**        | REG\_DWORD | OEM   | If this value is set to 0, then the device does not have a serial number. If this value is non-zero or does not exist, then the serial number is generated uniquely per device.                                                                                                                                            |
| **CurrentConfiguration** | REG\_SZ    | OEM   | This string must correspond to the name of a configuration subkey. This string determines which configuration to use to build a configuration descriptor for USB device enumeration.                                                                                                                                       |

 

## USBFN\\Configurations registry key


This table describes the values that OEMs can modify for subkeys under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Configurations**. Each subkey represents a different USB configuration. If the OEM wants to create their own interface, the OEM must define a new configuration which contains the interfaces to be used. To do this, create a subkey under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Configurations** that uses the name of the configuration and populate the subkey with the values in this table. Additionally, for the USB driver to use the new configuration, the **CurrentConfiguration** value (described in the preceding table) must be set to the name of the configuration subkey.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Type</th>
<th>Owner</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>InterfaceList</strong></td>
<td>REG_MULTI_SZ</td>
<td>OEM or Microsoft</td>
<td><p>Contains a list of interface names that correspond to interface subkeys under <strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong>&lt;strong&gt;Interfaces</strong>, the IAD associations defined under <strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong>&lt;strong&gt;Associations</strong>, and the alternate interfaces defined under <strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong>&lt;strong&gt;Alternates</strong>. Those keys determine the interfaces that are used to describe the composite configuration descriptor.</p>
<p>If the <strong>IncludeDefaultCfg</strong> value under the <strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong> key is set to 1, this list is appended to the Microsoft-owned default interface list to create the complete interface list that the device will use to enumerate.</p></td>
</tr>
<tr class="even">
<td><strong>MSOSCompatIdDescriptor</strong></td>
<td>REG_BINARY</td>
<td>OEM or Microsoft</td>
<td><p>Optional. Defines an Extended Compat ID OS Feature Descriptor for the configuration. If the <strong>IncludeDefaultCfg</strong> value under the <strong>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control</strong>&lt;strong&gt;USBFN</strong> key is set to 1, the functions in this descriptor are appended to the functions and interfaces in the default configuration.</p></td>
</tr>
</tbody>
</table>

 

## USBFN\\Interfaces registry key


This table describes the values that OEMs can modify for subkeys under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Interfaces**.

Each subkey represents a different USB interface. To define an interface, create a subkey under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Interfaces** using the name of the interface, and populate it with the values in the table below. Additionally, an interface will only be included if the interface is part of the **InterfaceList** of the **CurrentConfiguration**.

| Value                              | Type        | Owner            | Description                                                                                                                                                                                                                                                                                                  |
|------------------------------------|-------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **InterfaceDescriptor**            | REG\_BINARY | OEM or Microsoft | A binary representation of an interface descriptor to send to the host during USB enumeration. The **bInterfaceNumber** and **iInterface** values are automatically populated by the USB function stack after compiling a full configuration descriptor to avoid conflicts with other interface descriptors. |
| **InterfaceGUID**                  | REG\_SZ     | OEM or Microsoft | A GUID that uniquely identifies an interface on the bus.                                                                                                                                                                                                                                                     |
| **InterfaceNumber**                | REG\_DWORD  | OEM or Microsoft | Optional. This value is used to assign a fixed interface number to a function. Interface numbers 0-1F are reserved for legacy functions, 20-3F are reserved for Microsoft, and 40-5F are reserved for use by OEMs.                                                                                           |
| **MSOSExtendedPropertyDescriptor** | REG\_BINARY | OEM or Microsoft | Optional. Defines an Extended Property OS Feature Descriptor for the interface.                                                                                                                                                                                                                              |

 

## USBFN\\Alternates registry key


The alternates subkey is used to define a single interface that has one or more alternate interfaces. This table describes the values that OEMs can modify for subkeys under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Alternates**.

Each subkey represents a different interface. To define an interface with alternate settings, create a subkey under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Alternates** by using the name of the interface, and populate it with the values in the table below.

| Value                              | Type           | Owner            | Description                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------|----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **InterfaceList**                  | REG\_MULTI\_SZ | OEM or Microsoft | A list of two of more interface names that correspond to interfaces defined under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Interfaces**. That key collectively defines an interface with alternate settings. The first interface corresponds to alternate setting 0, the second interface corresponds to alternate setting 1, and so on. |
| **InterfaceNumber**                | REG\_DWORD     | OEM or Microsoft | Optional. This value is used to assign a fixed interface number to a function. Interface numbers 0-1F are reserved for legacy functions, 20-3F are reserved for Microsoft, and 40-5F are reserved for use by OEMs.                                                                                                                                                 |
| **MSOSExtendedPropertyDescriptor** | REG\_BINARY    | OEM or Microsoft | Optional. Defines an Extended Property OS Feature Descriptor for the interface.                                                                                                                                                                                                                                                                                    |

 

## USBFN\\Associations registry key


OEMs can specify associations by defining Interface Association Descriptors (IADs). Each IAD allows multiple interfaces to be grouped into a single function. This table describes the values that OEMs can modify for subkeys under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Associations**.

Each subkey represents a different IAD. To define an association, create a subkey under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control**\\**USBFN**\\**Associations** by using the name of the IAD, and populate it with the values in the table below.

| Value                              | Type           | Owner            | Description                                                                                                                                                                                                                 |
|------------------------------------|----------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **InterfaceList**                  | REG\_MULTI\_SZ | OEM or Microsoft | A list of interfaces or alternate interfaces that are associated with a USB function. If the size of the list is less than 2, then the function driver stack fails to load. Other functions or interfaces continue to load. |
| **bFunctionClass**                 | REG\_DWORD     | OEM or Microsoft | The class code of the function, set to 02.                                                                                                                                                                                  |
| **bFunctionSubClass**              | REG\_DWORD     | OEM or Microsoft | The subclass code of the function, set to 0d.                                                                                                                                                                               |
| **bFunctionProtocol**              | REG\_DWORD     |                  | The protocol code of the function, set to 01.                                                                                                                                                                               |
| **MSOSExtendedPropertyDescriptor** | REG\_BINARY    | OEM or Microsoft | Optional. Defines an Extended Property OS Feature Descriptor for the interface.                                                                                                                                             |

 

**Use case: Enabling MirrorLink**

MirrorLink is an interoperability standard that allows integration between mobile devices and car infotainment systems. The device must expose a USB CDC NCM interface to the MirrorLink client. As a Communications Device Class (CDC) device, it is required to describe the data interfaces by using either an Interface Association Descriptor (IAD) and/or a CDC Function Union Descriptor.

To enable MirrorLink connectivity on Windows 10 Mobile Device, OEM must make these changes to expose an IAD.

-   Create an association for the communication and data interfaces by using an Interface Association Descriptor (IAD) by setting registry values shown in the preceding table.
-   In addition to the registry settings, set this registry value to a non-zero value.

    | Value          | Type       | Owner            | Description                                                                                                                     |
    |----------------|------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|
    | **MirrorLink** | REG\_DWORD | OEM or Microsoft | A non-zero value indicates the interface supports MirrorLink. The USB function stack does not stall the MirrorLink USB command. |

     

-   Class-specific descriptors can be included in the interface descriptor set that is defined in the registry. The size field must be set in those descriptors so that USB function driver stack can parse them accurately.

Alternatively, a CDC Function Union Descriptor can also be defined as a Class-Specific Interface Descriptor; however, the interface numbers specified by the Union descriptor are static and are not be assigned by the USB function driver stack, and the presence of a Union descriptor does not cause the interfaces described by it to be associated with a single child PDO. An IAD is required for that association.

## Related topics
[USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)  
[Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md)  



