---
title: Setting up IRPs in Intermediate Drivers
description: Setting up IRPs in Intermediate Drivers
keywords: ["removable media WDK kernel , intermediate driver IRPs", "intermediate driver IRPs WDK removable media"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Setting up IRPs in Intermediate Drivers





Any intermediate driver layered between a file system driver and a removable-media device driver must set up the next-lower-level driver's I/O stack location in IRPs. From incoming [**IRP\_MJ\_READ**](./irp-mj-read.md), [**IRP\_MJ\_WRITE**](./irp-mj-write.md), and [**IRP\_MJ\_DEVICE\_CONTROL**](./irp-mj-device-control.md) requests, the intermediate driver must copy its own I/O stack location **Flags** into the next-lower-level driver's I/O stack location when it sets up the I/O stack location for the lower driver.

If the intermediate driver allocates new IRPs for lower-level removable-media drivers, it must set up those IRPs as follows:

-   For transfer requests, it must set up the thread context in each driver-allocated IRP from the value at **Tail.Overlay.Thread** in the original IRP.

-   For **IRP\_MJ\_READ**, **IRP\_MJ\_WRITE**, and **IRP\_MJ\_DEVICE\_CONTROL** requests, it must copy the I/O stack location **Flags** from the original IRP to each driver-allocated IRP.

Otherwise, the file system can neither maintain the integrity of cached file data nor cause the user to be prompted to remount the media that holds an open file.

 

