---
description: OEMs must set several registry values to make sure that their device enumerates with the correct metadata when connected to a computer.
title: USB registry settings for a function controller driver
ms.date: 06/30/2022
---

# USB registry settings for a function controller driver

OEMs must set several registry values to make sure that their device enumerates with the correct metadata when connected to a computer. These values specify device and configuration descriptors for the [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md). OEMs that create and include their own interfaces must set additional registry values in order for their interfaces to be loaded and used.

Registry keys related to the device-side USB drivers are under:

**HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN**

This topic describes settings for the preceding key and sub-keys that define the device, configuration, and interface descriptors for the device.

## USBFN registry key

Configuration information for the USB device are in the registry under: **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN**

This table describes its sub-keys. Some of them can be modified by OEMs. More information about the supported values for each sub-key is provided in sections below.

| Sub-key | Description |
|--|--|
| **Alternates** | This sub-key contains additional sub-keys that describe an interface that has one or more alternate settings. |
| **Associations** | This sub-key defines Interface Association Descriptors (IADs). Each IAD allows multiple interfaces to be grouped into a single function. Each sub-key represents a different IAD and OEMs can modify the values for those sub-keys. |
| **Default** | This sub-key contains default values that are used to describe device-specific settings such as the VID and PID. This is a Microsoft-owned sub-key whose values are overridden by those in the parent key. |
| **Configurations** | This sub-key contains additional sub-keys that contain configuration descriptor values that are used during USB enumeration. For example, the standard test configuration might exist under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Configurations\TestConfig**. |
| **Configurations\Default** | This is a Microsoft-owned sub-key. It contains values for the default configuration. The interfaces in the default configuration are added before the current configuration present when the **IncludeDefaultCfg** value is set to 1 under the **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN** key. |
| **Interfaces** | This sub-key contains additional sub-keys that describe specific interface descriptors. For example, the IP over USB interface may reside under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Interfaces\IpOverUsb**. The name of the interface sub-key is also used as the hardware ID of the USBFN child device for loading the USBFn class driver. In the IP over USB example, the hardware ID of the USBFN child device will be **USBFN\IpOverUsb**. |

This table describes the values that OEMs can define in the **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN** key. Values that are not defined in this key assume the default values defined by Microsoft under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Default**.

All OEMs must set the **idVendor**, **idProduct**, **ManufacturerString**, and **ProductString** values. OEMs that create and add their own interfaces must also set **CurrentConfiguration** to the name of the sub-key under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Configurations** that includes their interfaces in the **InterfaceList**.

| Value | Type | Owner | Description|
|--|--|--|--|
| **IncludeDefaultCfg** | REG_DWORD | OEM | Set to 1 when OEMs want to include the interfaces of the Default configuration such as IpOverUsb or MTP. |
| **idVendor** | REG_DWORD | OEM | The vendor identifier for the device descriptor that is sent to the host during enumeration. |
| **idProduct** | REG_DWORD | OEM | The product identifier for the device descriptor that is sent to the host during enumeration. |
| **ManufacturerString** | REG_SZ| OEM | The manufacturer string that is sent to the host to identify the manufacturer of the device. |
| **ProductString** | REG_SZ| OEM | A string that describes the device as a product. The default value is Windows 10 Mobile Device. This value is used as the display name of the device in the connected computer's user interface. OEMs should make sure that this value matches the value of the PhoneModelName value under the DeviceTargetingInfo sub-key. |
| **iSerialNumber**| REG_DWORD | OEM | If this value is set to 0, then the device does not have a serial number. If this value is non-zero or does not exist, then the serial number is generated uniquely per device. |
| **CurrentConfiguration** | REG_SZ | OEM | This string must correspond to the name of a configuration sub-key. This string determines which configuration to use to build a configuration descriptor for USB device enumeration. |
| **ClassEndpointRequestEnabled** | REG_DWORD | OEM | Set to 1 when you want to indicate that class endpoint requests are accepted. Class endpoint requests are not accepted by default. Set to 0 (or do not set this registry value) when you want to indicate that class endpoint requests are not accepted or are only accepted for specific interfaces. See the **ClassEndpointRequestEnabled** value in the [USBFN\Interfaces registry key](#usbfninterfaces-registry-key) section to learn how to accept class endpoint requests for specific interfaces. |

## USBFN\Configurations registry key

This table describes the values that OEMs can define for sub-keys under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Configurations**. Each sub-key represents a different USB configuration. If the OEM wants to create their own interface, the OEM must define a new configuration which contains the interfaces to be used. To do this, create a sub-key under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Configurations** that uses the name of the configuration and populate the sub-key with the values in this table. Additionally, for the USB driver to use the new configuration, the **CurrentConfiguration** value (described in the preceding table) must be set to the name of the configuration sub-key.

| Value | Type | Owner | Description |
|--|--|--|--|
| **InterfaceList** | REG_MULTI_SZ | OEM or Microsoft | Contains a list of interface names that correspond to interface sub-keys under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Interfaces**, the IAD associations defined under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Associations**, and the alternate interfaces defined under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Alternates**. Those keys determine the interfaces that are used to describe the composite configuration descriptor.</br></br> If the **IncludeDefaultCfg** value under the **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN** key is set to 1, this list is appended to the Microsoft-owned default interface list to create the complete interface list that the device will use to enumerate. |
| **MSOSCompatIdDescriptor** | REG_BINARY | OEM or Microsoft | Optional. Defines an Extended Compat ID OS Feature Descriptor for the configuration. If the **IncludeDefaultCfg** value under the **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN** key is set to 1, the functions in this descriptor are appended to the functions and interfaces in the default configuration. |

## USBFN\Interfaces registry key

This table describes the values that OEMs can modify for sub-keys under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Interfaces**.

Each sub-key represents a different USB interface. To define an interface, create a sub-key under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Interfaces** using the name of the interface, and populate it with the values in the table below. Additionally, an interface will only be included if the interface is part of the **InterfaceList** of the **CurrentConfiguration**.

| Value | Type | Owner | Description |
|--|--|--|--|
| **InterfaceDescriptor** | REG_BINARY | OEM or Microsoft | A binary representation of an interface descriptor to send to the host during USB enumeration. The **bInterfaceNumber** and **iInterface** values are automatically populated by the USB function stack after compiling a full configuration descriptor to avoid conflicts with other interface descriptors. |
| **InterfaceGUID** | REG_SZ | OEM or Microsoft | A GUID that uniquely identifies an interface on the bus. |
| **InterfaceNumber** | REG_DWORD | OEM or Microsoft | Optional. This value is used to assign a fixed interface number to a function. Interface numbers 0-1F are reserved for legacy functions, 20-3F are reserved for Microsoft, and 40-5F are reserved for use by OEMs. |
| **MSOSExtendedPropertyDescriptor** | REG_BINARY | OEM or Microsoft | Optional. Defines an Extended Property OS Feature Descriptor for the interface. |
| **ClassEndpointRequestEnabled** | REG_DWORD | OEM | This registry value is only valid when **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\ClassEndpointRequestEnabled** is not present or is set to 0. Set this registry value to 1 when you want to indicate that class endpoint requests for this interface are accepted. Set to 0 (or do not set this registry value) when you want to indicate that class endpoint requests for this interface are not accepted. |

## USBFN\Alternates registry key

The alternates sub-key is used to define a single interface that has one or more alternate interfaces. This table describes the values that OEMs can modify for sub-keys under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Alternates**.

Each sub-key represents a different interface. To define an interface with alternate settings, create a sub-key under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Alternates** by using the name of the interface, and populate it with the values in the table below.

| Value | Type | Owner | Description |
|--|--|--|--|
| **InterfaceList** | REG_MULTI_SZ | OEM or Microsoft | A list of two of more interface names that correspond to interfaces defined under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Interfaces**. That key collectively defines an interface with alternate settings. The first interface corresponds to alternate setting 0, the second interface corresponds to alternate setting 1, and so on. |
| **InterfaceNumber** | REG_DWORD | OEM or Microsoft | Optional. This value is used to assign a fixed interface number to a function. Interface numbers 0-1F are reserved for legacy functions, 20-3F are reserved for Microsoft, and 40-5F are reserved for use by OEMs. |
| **MSOSExtendedPropertyDescriptor** | REG_BINARY | OEM or Microsoft | Optional. Defines an Extended Property OS Feature Descriptor for the interface. |

## USBFN\Associations registry key

OEMs can specify associations by defining Interface Association Descriptors (IADs). Each IAD allows multiple interfaces to be grouped into a single function. This table describes the values that OEMs can modify for sub-keys under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Associations**.

Each sub-key represents a different IAD. To define an association, create a sub-key under **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\USBFN\Associations** by using the name of the IAD, and populate it with the values in the table below.

| Value | Type | Owner | Description |
|--|--|--|--|
| **InterfaceList** | REG_MULTI_SZ | OEM or Microsoft | A list of interfaces or alternate interfaces that are associated with a USB function. If the size of the list is less than 2, then the function driver stack fails to load. Other functions or interfaces continue to load. |
| **bFunctionClass** | REG_DWORD | OEM or Microsoft | The class code of the function, set to 02. |
| **bFunctionSubClass** | REG_DWORD | OEM or Microsoft | The subclass code of the function, set to 0d. |
| **bFunctionProtocol** | REG_DWORD |  | The protocol code of the function, set to 01. |
| **MSOSExtendedPropertyDescriptor** | REG_BINARY | OEM or Microsoft | Optional. Defines an Extended Property OS Feature Descriptor for the interface. |

### Use case: Enabling MirrorLink

MirrorLink is an interoperability standard that allows integration between mobile devices and car infotainment systems. The device must expose a USB CDC NCM interface to the MirrorLink client. As a Communications Device Class (CDC) device, it is required to describe the data interfaces by using either an Interface Association Descriptor (IAD) and/or a CDC Function Union Descriptor.

To enable MirrorLink connectivity on Windows 10 Mobile Device, OEM must make these changes to expose an IAD.

- Create an association for the communication and data interfaces by using an Interface Association Descriptor (IAD) by setting registry values shown in the preceding table.
- In addition to the registry settings, set this registry value to a non-zero value.

   | Value | Type | Owner | Description |
   |--|--|--|--|
   | **MirrorLink** | REG_DWORD | OEM or Microsoft | A non-zero value indicates the interface supports MirrorLink. The USB function stack does not stall the MirrorLink USB command. |

- Class-specific descriptors can be included in the interface descriptor set that is defined in the registry. The size field must be set in those descriptors so that USB function driver stack can parse them accurately.

Alternatively, a CDC Function Union Descriptor can also be defined as a Class-Specific Interface Descriptor; however, the interface numbers specified by the Union descriptor are static and are not be assigned by the USB function driver stack, and the presence of a Union descriptor does not cause the interfaces described by it to be associated with a single child PDO. An IAD is required for that association.

## Related topics

- [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)
- [Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md)
