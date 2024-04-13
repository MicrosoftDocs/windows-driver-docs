---
title: Powering Up a Device
description: Powering Up a Device
keywords: ["I/O WDK power management", "device power ups WDK kernel", "powering up devices WDK kernel", "IRP_MN_SET_POWER", "working state returns WDK power management", "turning on devices WDK power management", "automatic power ups WDK kernel", "on power WDK kernel", "IRPs WDK power management", "startup power management WDK kernel"]
ms.date: 06/16/2017
---

# Powering Up a Device





When a bus driver handles a PnP [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) request for one of its child devices, it should power on the device and call [**PoSetPowerState**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-posetpowerstate) to report the device power state to the power manager. Powering on the device is an implicit part of device start-up. The device power policy owner does not send an [**IRP\_MN\_SET\_POWER**](./irp-mn-set-power.md) request for **PowerDeviceD0**, so drivers should not expect to receive these IRPs at start-up.

When a device has been powered down to conserve power, its drivers should power it up when an I/O request arrives. In this case, the device power policy owner must send an **IRP\_MN\_SET\_POWER** to return the device to the working state. When the IRP completes, the drivers for the device stop queuing I/O and begin to process requests off the queue.

 

