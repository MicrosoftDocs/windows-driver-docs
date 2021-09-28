---
title: GUID_DEVINTERFACE_IMAGE Device Interface Class
description: The image device interface class is defined for still image devices, including digital cameras and scanners.
ms.date: 09/27/2021
ms.localizationpriority: medium
---

# GUID_DEVINTERFACE_IMAGE Device Interface Class

The image [device interface class](../install/overview-of-device-interface-classes.md) is defined for [still image devices](./index.md), including digital cameras and scanners.

| Attribute | Setting |
|--|--|
| Manifest constant | GUID_DEVINTERFACE_IMAGE |
| Class GUID | {0x6bdd1fc6L, 0x810f, 0x11d0, 0xbe, 0xc7, 0x08, 0x00, 0x2b, 0xe2, 0x09, 0x2f} |

## Headers

Defined in *Wiaintfc.h*. Include *Wiaintfc.h.*

## Remarks

The system-supplied kernel-mode drivers for still image devices register an instance of this device interface class for still image devices. You can access an instance of this device interface class by using the I/O interface that still image drivers support. For more information about still image devices and drivers, see [Windows Image Acquisition Drivers](./windows-image-acquisition-drivers.md).

This interface is applicable to both still image drivers and WIA drivers.
