---
title: Enabling Device Wake-Up
description: Enabling Device Wake-Up
keywords: ["IRPs WDK power management", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management", "IRP_MN_WAIT_WAKE", "IRP_MJ_POWER", "DEVICE_CAPABILITIES structure", "restoring power WDK kernel"]
ms.date: 06/16/2017
---

# Enabling Device Wake-Up





If a device supports wake-up, its power policy owner must be able to enable and disable wake-up for the device. A driver enables wake up by sending an [**IRP\_MJ\_POWER**](./irp-mj-power.md) request with minor function code [**IRP\_MN\_WAIT\_WAKE**](./irp-mn-wait-wake.md) and disables wake-up by canceling a previously sent **IRP\_MN\_WAIT\_WAKE**. A device can have only one **IRP\_MN\_WAIT\_WAKE** request pending at a time.

To determine whether its device supports wake-up, the device power states from which it can signal wake-up, and the system power states from which the device can wake the system, a driver checks the **SystemWake**, **DeviceWake**, and **WakeFromD***x* members in the [**DEVICE\_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) structure.

For more information about enabling, disabling, and responding to wake-up signals in a driver, see [Supporting Devices that Have Wake-Up Capabilities](supporting-devices-that-have-wake-up-capabilities.md).

 

