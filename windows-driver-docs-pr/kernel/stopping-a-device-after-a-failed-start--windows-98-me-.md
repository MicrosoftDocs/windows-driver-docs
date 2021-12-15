---
title: Stopping a Device after a Failed Start (Windows 98/Me)
description: Stopping a Device after a Failed Start (Windows 98/Me)
keywords: ["failed starts WDK PnP"]
ms.date: 06/16/2017
---

# Stopping a Device after a Failed Start (Windows 98/Me)





On Windows 98/Me, the PnP manager issues an [**IRP\_MN\_STOP\_DEVICE**](./irp-mn-stop-device.md) request without a preceding query when the drivers for a device fail an [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) request. (On Windows 2000 and later, the PnP manager sends remove IRPs in this situation. See [Understanding When Remove IRPs Are Issued](understanding-when-remove-irps-are-issued.md).)

In response to the stop IRP, drivers release the device's hardware resources (such as its I/O ports), disable and deregister any user-mode interfaces, and fail any incoming I/O requests that require access to the device.

 

