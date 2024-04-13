---
title: Checking Flags in the Device Object
description: Checking Flags in the Device Object
keywords: ["removable media WDK kernel , flag checking", "flags WDK removable media", "checking device object flags", "verifying device object flags"]
ms.date: 06/16/2017
---

# Checking Flags in the Device Object





For each IRP requesting an I/O operation to/from removable media, a removable-media device driver must determine whether DO\_VERIFY\_VOLUME is already set in its **DeviceObject-&gt;Flags**. If this value is set, the driver must do the following:

-   For [**IRP\_MJ\_READ**](./irp-mj-read.md), [**IRP\_MJ\_WRITE**](./irp-mj-write.md), and [**IRP\_MJ\_DEVICE\_CONTROL**](./irp-mj-device-control.md) requests, check whether SL\_OVERRIDE\_VERIFY\_VOLUME is set in the **Flags** member of the driver's [**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure. If it is, continue the requested operation.

    Device control requests that return information about the logical structure of the underlying media have SL\_OVERRIDE\_VERIFY\_VOLUME set in the I/O stack location's **Flags** member when an IFS mounts or remounts a removable-media volume.

-   Otherwise, the driver must refuse to carry out I/O requests for the corresponding drive, device, or partition while DO\_VERIFY\_VOLUME is set in its **DeviceObject-&gt;Flags**. A removable media driver must fail IRPs sent to the corresponding device until the FSD clears DO\_VERIFY\_VOLUME in the removable-media driver's **DeviceObject-&gt;Flags**.

If a removable-media device driver does not fail IRPs when DO\_VERIFY\_VOLUME is set and SL\_OVERRIDE\_VERIFY\_VOLUME is not set for the preceding transfer requests, the file system can neither maintain the integrity of cached file data nor cause the user to be prompted to remount the media that holds an open file.

 

