---
title: Checking Flags in the Device Object
author: windows-driver-content
description: Checking Flags in the Device Object
MS-HAID:
- 'Other\_d865abba-7708-4f15-9204-d4b4eea4f9c4.xml'
- 'kernel.checking\_flags\_in\_the\_device\_object'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f7bff7b8-bd30-4489-ab3f-ca5ad4d5c1ba
keywords: ["removable media WDK kernel , flag checking", "flags WDK removable media", "checking device object flags", "verifying device object flags"]
---

# Checking Flags in the Device Object


## <a href="" id="ddk-checking-flags-in-the-device-object-kg"></a>


For each IRP requesting an I/O operation to/from removable media, a removable-media device driver must determine whether DO\_VERIFY\_VOLUME is already set in its **DeviceObject-&gt;Flags**. If this value is set, the driver must do the following:

-   For [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794), [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819), and [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests, check whether SL\_OVERRIDE\_VERIFY\_VOLUME is set in the **Flags** member of the driver's [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure. If it is, continue the requested operation.

    Device control requests that return information about the logical structure of the underlying media have SL\_OVERRIDE\_VERIFY\_VOLUME set in the I/O stack location's **Flags** member when an IFS mounts or remounts a removable-media volume.

-   Otherwise, the driver must refuse to carry out I/O requests for the corresponding drive, device, or partition while DO\_VERIFY\_VOLUME is set in its **DeviceObject-&gt;Flags**. A removable media driver must fail IRPs sent to the corresponding device as described in the preceding subsection, repeating both Steps 3 and 4 for each IRP until the FSD clears DO\_VERIFY\_VOLUME in the removable-media driver's **DeviceObject-&gt;Flags**.

If a removable-media device driver does not fail IRPs when DO\_VERIFY\_VOLUME is set and SL\_OVERRIDE\_VERIFY\_VOLUME is not set for the preceding transfer requests, the file system can neither maintain the integrity of cached file data nor cause the user to be prompted to remount the media that holds an open file.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Checking%20Flags%20in%20the%20Device%20Object%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


