---
title: File Creation by a USB I/O Target
description: File Creation by a USB I/O Target
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 44bbc4c7-632d-4d75-94b9-f65e4d480e90
keywords: ["user mode drivers WDK UMDF USB I/O targets file creation", "UMDF WDK USB I/O targets file creation", "User Mode Driver Framework WDK USB I/O targets", "framework based drivers WDK UMDF USB I/O targets", "USB I/O targets WDK UMDF file creation", "I/O targets WDK UMDF USB file creation"]
---

# File Creation by a USB I/O Target


\[This topic applies to UMDF 1.*x*.\]

During its initialization, the USB I/O target creates an intra-stack file object, which represents a default session that the USB I/O target keeps open. For more information about an intra-stack file object, see [Creating a File Object to Handle I/O](creating-a-file-object-to-handle-i-o.md). The USB I/O target or its USB pipe target children use this file object to send any I/O that they originate (for example, I/O to obtain the USB configuration descriptor).

The driver can use this intra-stack file object in format functions (for example, the driver can pass a pointer to this file object to the *pFile* parameter in a call to the [**IWDFIoTarget::FormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559233) method) if the driver must send I/O on this file object's default session. To obtain the intra-stack file object, the driver can call the [**IWDFIoTarget::GetTargetFile**](https://msdn.microsoft.com/library/windows/hardware/ff559243) method.

This intra-stack file object is closed when the I/O target is disposed of either explicitly, when the driver calls the [**IWDFObject::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) method on the I/O target, or implicitly, when the I/O target's parent is disposed of.

If any I/O remains outstanding on this intra-stack file object at the time of device removal, this file object will fail to close, and UMDF will generate a driver stop. For more information, see [Creating and Using Driver-Created File Objects](creating-and-using-driver-created-file-objects.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20File%20Creation%20by%20a%20USB%20I/O%20Target%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




