---
title: Power management for HID over USB
description: HID over USB employs USB suspend to power manage a device.
ms.assetid: 7B5E10B0-2EEA-450A-9E21-B60215F60027
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power management


HID over USB employs USB suspend to power manage a device.

Power is managed primarily in the following two configurations:

1.  Case \#1: The system is in a power managed state (e.g. S3) but the device is armed to wake the system up. E.g. a HID USB keyboard that is armed to wake up a desktop from S3 on key press.
2.  Case \#2: The system is in a running state (e.g. S0) but the device has idled out (no user interaction). E.g. selective suspend a HID USB mouse when no one is using or touching it.

*Case \#1 Provisions*

HID devices don't automatically wake up a system from a low- power state. Only specific HID devices (e.g. Top level collections of keyboards and mice) do this.

If an end user wishes to disarm a device from waking up the system, the user can specify this via the properties/power management tab in device manager.

 

 




