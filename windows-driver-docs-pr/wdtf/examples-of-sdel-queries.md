---
title: Examples of SDEL Queries
description: Examples of device relation tokens used in SDEL queries
keywords:
- SDEL
- SDEL queries
ms.date: 09/03/2020
---

# Examples of SDEL Queries

For more information about device relation tokens used in SDEL queries, see [Device Relation Tokens in SDEL](device-relation-tokens-in-sdel.md).

## Examples of Simple Device Relation Tokens in SDEL Queries

The following SDEL query returns a collection of devices that are attached to the computer and are installed. This SDEL query returns all classes of connected devices, regardless of whether the device is enabled (started) or not.

```command
var Devices = WDTF.DeviceDepot.Query("IsAttached");
```

SDEL device relation tokens can also filter the query results. For example, the following SDEL query returns a collection of devices in the computer that are started and have a parent device that is a USB class device.

```command
var Devices = WDTF.DeviceDepot.Query("IsStarted AND ancestor/(Class='USB')");
```

The following SDEL query returns a collection of devices that are connected and installed in the computer, regardless of whether they are started, and have the class characteristic of either a storage volume, multimedia, or network adapter.

```command
var Devices = WDTF.DeviceDepot.Query("IsPhantom=False AND (Volume::DriveLetter OR class='Media' OR class='Net')");
```

## Examples of Combined Device Relation Tokens in SDEL Queries

If you use the SDEL device relationship tokens and append "-or-self" to the token, the resulting query returns an inclusive collection of devices.
For example, the following SDEL query returns a collection of devices in the computer that are topologically above or include either the floppy disk controllers, hard disk controllers, or 1394 host bus controllers.

```command
var Devices = WDTF.DeviceDepot.Query("above-or-self/(Class='HDC' OR Class='1394' OR  Class='FDC')");
```

As another example, this SDEL query returns a collection of devices that have the following properties:

- The device is attached and installed in the computer.
- The device is one of the following:
- The device is a display type device that can be disabled and has some kind of a child relation to a parent device.
- The device is the topmost HID class type that has a bus relation to a parent device (with the exception of the root hub).

```command
var Devices = WDTF.DeviceDepot.Query("IsAttached AND ((IsDisableable AND descendant-or-self/(Class='Display')) OR child/(Class='HIDClass') )" );
```
