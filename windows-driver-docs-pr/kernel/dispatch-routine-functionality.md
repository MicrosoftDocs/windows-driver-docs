---
title: Dispatch Routine Functionality
description: Dispatch Routine Functionality
ms.assetid: cfc191af-2b65-465b-972e-9617a8f7d8b7
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Dispatch Routine Functionality





The required functionality of a particular dispatch routine varies, depending on the I/O function code it handles, on the individual driver's position in a chain of drivers, and on the type of underlying physical device.

Most dispatch routines process incoming I/O request packets (IRPs) as follows:

1. Check the driver's I/O stack location in the IRP to determine what to do and check the parameters, if any, for validity.

   Whether a driver must check its I/O stack location to determine what to do and to check parameters depends on the given **IRP\_MJ\_**<em>XXX</em>, as well as on whether that driver set up a separate Dispatch routine for each **IRP\_MJ\_**<em>XXX</em> that the driver handles.

2. Satisfy the request and complete the IRP if possible; otherwise, pass it on for further processing by lower-level drivers or by other device driver routines.

   Whether a driver must pass on an IRP for further processing depends on the validity of the parameters, if any, as well as on the **IRP\_MJ\_**<em>XXX</em> and on the driver's level, if any, in a chain of layered drivers.

For more information about IRPs, see [Handling IRPs](handling-irps.md).

 

 




