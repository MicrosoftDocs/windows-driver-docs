---
title: Determining When to Send a Wait/Wake IRP
description: Determining When to Send a Wait/Wake IRP
keywords: ["timing wait/wake IRPs WDK power management", "sending wait/wake IRPs", "wait/wake IRPs WDK power management , sending"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Determining When to Send a Wait/Wake IRP





The driver that owns device power policy sends wait/wake IRPs on behalf of its device. Such a driver must send a wait/wake IRP when one of the following occurs:

-   The driver is putting the device to sleep but the device must be able to wake up in response to an external wake-up signal.

-   The system is going to sleep and the device must be able to awaken it.

The power policy owner should send the wait/wake IRP before any such conditions are imminent. It can send the IRP any time its device is in D0, but it must not send such an IRP while it is handling another set-power or query-power IRP. As a general rule, the driver should send the IRP during its handling of the Plug and Play manager's [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) request, after it has initialized and started the device.

 

