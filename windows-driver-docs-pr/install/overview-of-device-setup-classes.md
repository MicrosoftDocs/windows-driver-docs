---
title: Overview of Device Setup Classes
description: Learn more about device setup classes
ms.date: 04/11/2022
---

# Overview of device setup classes

To facilitate device installation, devices that are set up and configured in the same manner are grouped into a device setup class. A device is grouped into a device setup class based on the class of the base [driver package](driver-packages.md) that is installed on the device. For example, SCSI media changer devices are grouped into the MediumChanger device setup class. The device setup class can define some common settings that apply to all devices that are in that device setup class such as filter drivers that should be inserted into the [device stack](../gettingstarted/driver-stacks.md) of that device.

Microsoft defines setup classes for most types of devices. IHVs and OEMs can define new device setup classes, but only if none of the existing classes apply. For example, a camera vendor does not have to define a new setup class because cameras fall under the Camera setup class. Similarly, uninterruptible power supply (UPS) devices fall under the Battery class.

There is a GUID associated with each device setup class. System-defined setup class GUIDs are defined in *Devguid.h* and typically have symbolic names of the form GUID_DEVCLASS_*Xxx*.
