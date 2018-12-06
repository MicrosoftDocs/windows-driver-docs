---
title: Removing a Device
description: Removing a Device
ms.assetid: 8184987f-5c46-4dd6-aad2-3c32b14205fd
keywords: ["PnP WDK kernel , removing devices", "Plug and Play WDK kernel , removing devices", "removing devices", "notifications WDK PnP , removing devices", "IRPs WDK PnP", "I/O request packets WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Removing a Device





The PnP manager directs drivers to remove their device objects for a device when the device has been, or is being, physically removed from the machine. The PnP manager also sends a *remove* IRP when a user requests to update the drivers for a device and, on Windows 2000 and later, when the device is disabled or fails to start.

The following sections describe when the PnP manager issues *remove* IRPs and what drivers must do to respond to those IRPs. This section covers the following topics:

[Understanding When Remove IRPs Are Issued](understanding-when-remove-irps-are-issued.md)

[Handling an IRP\_MN\_QUERY\_REMOVE\_DEVICE Request](handling-an-irp-mn-query-remove-device-request.md)

[Handling an IRP\_MN\_REMOVE\_DEVICE Request](handling-an-irp-mn-remove-device-request.md)

[Handling an IRP\_MN\_CANCEL\_REMOVE\_DEVICE Request](handling-an-irp-mn-cancel-remove-device-request.md)

[Handling an IRP\_MN\_SURPRISE\_REMOVAL Request](handling-an-irp-mn-surprise-removal-request.md)

[Using Remove Locks](using-remove-locks.md)

 

 




