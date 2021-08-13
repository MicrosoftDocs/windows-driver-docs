---
title: KSPROPERTY_RAW_AVC_CMD
description: The KSPROPERTY_RAW_AVC_CMD property issues a raw AV/C command. Raw AV/C commands are supported only for IEEE 1394 bus devices.
keywords: ["KSPROPERTY_RAW_AVC_CMD Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RAW_AVC_CMD
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 08/13/2021
ms.localizationpriority: medium
---

# KSPROPERTY_RAW_AVC_CMD

The KSPROPERTY_RAW_AVC_CMD property issues a raw AV/C command. Raw AV/C commands are supported only for IEEE 1394 bus devices.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | Embedded **RawAVC** structure |

The property value (operation data) is the embedded **RawAVC** member of the KSPROPERTY_EXTXPORT_S structure that describes the raw AV/C command to run.

## Remarks

This property can only be used with devices that can support AV/C commands and where [**KSPROPERTY_EXTDEVICE_PORT**](ksproperty-extdevice-port.md) returns DEV_PORT_1394 in the **DevPort** member of the [**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s) structure.

Driver developers for IEEE 1394 devices may optionally support this property in their drivers in order to extend the device transport controls that are not supported by standard interfaces (such as the user-mode **IAMExtTransport** COM interface methods **put_Mode** and **get_Mode**).

It is not necessary to implement support for this property on USB devices because the [USB Video Class Driver](./usb-video-class-driver.md) provides this functionality. Normally applications can use the **IKsControl** COM interface to control an IEEE 1394 device. However, the **IKsControl** COM interface does not provide a standard method to support tape seek that is portable across USB and IEEE 1394 buses. Therefore, to perform a tape seek a caller must use the **DeviceIoControl** function instead of the **IKsControl** COM interface. Callers perform a tape seek on 1394 AV/C devices by using a raw AV/C command with an absolute track number (ATN) or time code to seek to. This is a primary reason why this property does not apply to USB devices.

See the [Digital Video Application Compatibility (DOC download)](https://download.microsoft.com/download/5/b/5/5b5bec17-ea71-4653-9539-204a672f11cf/dv_appcompat.doc) white paper for more information about the differences between tape location searches on USB and 1394 devices.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)
