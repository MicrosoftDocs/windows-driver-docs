---
title: WIA_DIP_DEV_TYPE
description: The WIA_DIP_DEV_TYPE property contains a device type and device subtype.
keywords: ["WIA_DIP_DEV_TYPE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DIP_DEV_TYPE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DIP_DEV_TYPE

The WIA_DIP_DEV_TYPE property contains a device type and device subtype. The WIA service creates and maintains this property

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The device type and subtype are obtained from the driver's INF file of the device file. An application reads the WIA_DIP_DEV_TYPE property to determine whether it is using a scanner, camera, or video device.

The following table describes the possible values for the device type.

| Device type | Value | Definition |
|--|--|--|
| **StiDeviceTypeDefault** | 0x0000 | Default device |
| **StiDeviceTypeScanner** | 0x0001 | Scanner device |
| **StiDeviceTypeDigitalCamera** | 0x0002 | Camera device |
| **StiDeviceTypeStreamingVideo** | 0x0003 | Video device |

For more information about INF files, see [INF Files for WIA Devices](./inf-files-for-wia-devices.md). The **StiDeviceType***Xxx* constants are defined in *Sti.h*.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
