---
title: Checking Flags in the Device Object
description: Checking Flags in the Device Object
ms.assetid: f7bff7b8-bd30-4489-ab3f-ca5ad4d5c1ba
keywords: ["removable media WDK kernel , flag checking", "flags WDK removable media", "checking device object flags", "verifying device object flags"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Checking Flags in the Device Object





For each IRP requesting an I/O operation to/from removable media, a removable-media device driver must determine whether DO\_VERIFY\_VOLUME is already set in its **DeviceObject-&gt;Flags**. If this value is set, the driver must do the following:

-   For [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794), [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819), and [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests, check whether SL\_OVERRIDE\_VERIFY\_VOLUME is set in the **Flags** member of the driver's [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure. If it is, continue the requested operation.

    Device control requests that return information about the logical structure of the underlying media have SL\_OVERRIDE\_VERIFY\_VOLUME set in the I/O stack location's **Flags** member when an IFS mounts or remounts a removable-media volume.

-   Otherwise, the driver must refuse to carry out I/O requests for the corresponding drive, device, or partition while DO\_VERIFY\_VOLUME is set in its **DeviceObject-&gt;Flags**. A removable media driver must fail IRPs sent to the corresponding device as described in the preceding subsection, repeating both Steps 3 and 4 for each IRP until the FSD clears DO\_VERIFY\_VOLUME in the removable-media driver's **DeviceObject-&gt;Flags**.

If a removable-media device driver does not fail IRPs when DO\_VERIFY\_VOLUME is set and SL\_OVERRIDE\_VERIFY\_VOLUME is not set for the preceding transfer requests, the file system can neither maintain the integrity of cached file data nor cause the user to be prompted to remount the media that holds an open file.

 

 




