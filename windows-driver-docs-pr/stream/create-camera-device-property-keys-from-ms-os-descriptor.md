---
title: Create device property keys from the MS OS descriptor in USB Video Class (UVC) camera firmware
description: Describes how to create device property keys from the MS OS descriptor in USB Video Class (UVC) camera firmware.
ms.date: 06/24/2021
ms.localizationpriority: medium
---

# Create device property keys from the MS OS descriptor in USB Video Class (UVC) camera firmware

In the past, manufacturers of USB Video Class (UVC) cameras had to author custom INF files to provide functionality such as device property keys. For simple registry keys, the USBVideo driver has a mechanism for creating registry keys from the MS OS descriptor if the key name in question is prefaced with `UVC-`. This expands that functionality in the USBVideo driver to also create device property keys from an MS OS descriptor if it follows a specific format. This allows the USBVideo camera firmware to reach feature parity with a MIPI camera driver without authoring a custom INF for those cameras.

> [!NOTE]
> If the same device property key is defined in a custom INF, it will override the value provided by the MS OS descriptor.

## Applies to

- WIN10_NEXT and later operating systems

## MS OS 2.0 registry property descriptor

The current MS OS 2.0 registry property descriptor is defined as follows:

| Offset | Field | Size | Description |
|--|--|--|--|
| 0 | wLength | 2 | Length, in bytes, of this descriptor. |
| 2 | wDescriptorType | 2 | MS_OS_20_FEATURE_REG_PROPERTY |
| 4 | wPropertyDataType| 2 | Type of registry property |
| 6 | wPropertyNameLength | 2 | Length of the property name. |
| 8 | PropertyName | Variable | Name of registry property. |
| 8+M | wPropertyDataLength | 2 | Length of property data |
| 10+M | PropertyData | Variable | Property data |

## wPropertyDataType values for the MS OS 2.0 registry property descriptor

The following table describes wPropertyDataType values for the MS OS 2.0 registry property descriptor:

| Value | Description |
|--|--|
| 0 | RESERVED |
| 1 | NULL-terminated Unicode String (REG_SZ) |
| 2 | NULL-terminated Unicode String that includes environment variables (REG_EXPAND_SZ) |
| 3 | Free-form binary (REG_BINARY) |
| 4 | Little-endian 32-bit integer (REG_DWORD_LITTLE_ENDIAN) |
| 5 | Big-endian 32-bit integer (REG_DWORD_BIG_ENDIAN) |
| 6 | NULL-terminated Unicode string that contains a symbolic link (REG_LINK) |
| 7 | Multiple NULL-terminated Unicode strings (REG_MULTI_SZ) |
| 8 and higher | RESERVED |

The USBVideo driver will currently copy all MS OS descriptors that have a prefix of `UVC-` as registry variable names to each device interface node. These are straight one-to-one copies of one registry key to another, removing the `UVC-` prefix. For device property keys, additional information is required. For defining a device property key, there needs to be a defined GUID and ID. Additionally, each key requires a corresponding data type and value for that data. For this feature, the USBVideo driver will map a registry value and type to a **DEVPROPTYPE**.

## Possible Registry Types

| Registry Value | Description | DEVPROPTYPE value | Description |
|--|--|--|--|
| 1 | REG_SZ | DEVPROP_TYPE_STRING | Null-terminated string |
| 2 | REG_EXPAND_SZ | NA | Not supported |
| 3 | REG_BINARY | DEVPROP_TYPE_BINARY | Custom binary data |
| 4 | REG_DWORD_LITTLE_ENDIAN | DEVPROP_TYPE_UINT32 | 32-bit unsigned int (ULONG32) |
| 5 | REG_DWORD_BIG_ENDIAN | NA | Not supported |
| 6 | REG_LINK | NA | Not supported |
| 7 | REG_MULTI_SZ | DEVPROP_TYPE_STRING_LIST | Multi-sz string list |

To determine that this device property key should be created, a new prefix will be defined. If a MS OS descriptor is found with the format of **DKEY-\<GUID\>,\<ID\>** then the USBVideo driver will attempt this creation. The registry value must be of one of the defined formats above (discarding and ignoring REG_LINK, REG_EXPAND_SZ, and REG_DWORD_BIG_ENDIAN). The format of GUID should be {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX} and the format of the ID should be a numerical value greater than 2.

## Example MS OS descriptor

The following example defines a MS OS descriptor:

```cpp
UCHAR Example2_MSOS20DescriptorSet_UVCDevicePropertyKeyForFutureWindows\[0x3C\] =
{

//
// MS OS 2.0 Descriptor Set Header
//
0x0A, 0x00, // wLength - 10 bytes
0x00, 0x00, // MSOS20_SET_HEADER_DESCRIPTOR
0x00, 0x00, 0x0?, 0x06, // dwWindowsVersion – 0x060?0000 for future Windows version
0x76, 0x00, // wTotalLength – 118 bytes

//
// MS OS 2.0 Registry Value Feature Descriptor
//
0x6c, 0x00, // wLength - 108 bytes
0x04, 0x00, // wDescriptorType – 4 for Registry Property
0x04, 0x00, // wPropertyDataType - 4 for REG_DWORD_LITTLE_ENDIAN
0x5E, 0x00, // wPropertyNameLength – 94 bytes
'D', 0x00, 'K', 0x00, // Property Name – **DKEY-{4023440c-a74e-46e0-82df-e486fa545f40},3**
'E', 0x00, 'Y', 0x00,
'-', 0x00, '{', 0x00,
'4', 0x00, '0', 0x00,
'2', 0x00, '3', 0x00,
'4', 0x00, '4', 0x00,
'0', 0x00, 'C', 0x00,
'-', 0x00, 'A', 0x00,
'7', 0x00, '4', 0x00,
'E', 0x00, '-', 0x00,
'4', 0x00, '6', 0x00,
'E', 0x00, '0', 0x00,
'-', 0x00, '8', 0x00,
'2', 0x00, 'D', 0x00,
'F', 0x00, '-', 0x00,
'E', 0x00, '4', 0x00,
'8', 0x00, '6', 0x00,
'F', 0x00, 'A', 0x00,
'5', 0x00, '4', 0x00,
'5', 0x00, 'F', 0x00,
'4', 0x00, '0', 0x00,
'}', 0x00, ',', 0x00,
'3', 0x00, 0x00, 0x00,
0x00, 0x00,
0x04, 0x00, // wPropertyDataLength – 4 bytes
0xAC, 0x03, 0x00, 0x00 // PropertyData – 0x000003AC (940)
};
```

This would convert to the following device property key using [IoSetDevicePropertyData](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdevicepropertydata) with the following parameters:

```output
DEVPROPKEY

    DEVPROPGUID = {4023440c-a74e-46e0-82df-e486fa545f40}

    DEVPROPID = 3

DEVPROPTYPE = DEVPROP_TYPE_UINT32

PropertyBuffer containing UINT32 value = 940
```
