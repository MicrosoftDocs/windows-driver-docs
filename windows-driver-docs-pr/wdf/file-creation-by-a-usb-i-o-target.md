---
title: File Creation by a USB I/O Target
description: File Creation by a USB I/O Target
ms.assetid: 44bbc4c7-632d-4d75-94b9-f65e4d480e90
keywords:
- user-mode drivers WDK UMDF , USB I/O targets, file creation
- UMDF WDK , USB I/O targets, file creation
- User-Mode Driver Framework WDK , USB I/O targets
- framework-based drivers WDK UMDF , USB I/O targets
- USB I/O targets WDK UMDF , file creation
- I/O targets WDK UMDF , USB, file creation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File Creation by a USB I/O Target


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

During its initialization, the USB I/O target creates an intra-stack file object, which represents a default session that the USB I/O target keeps open. For more information about an intra-stack file object, see [Creating a File Object to Handle I/O](creating-a-file-object-to-handle-i-o.md). The USB I/O target or its USB pipe target children use this file object to send any I/O that they originate (for example, I/O to obtain the USB configuration descriptor).

The driver can use this intra-stack file object in format functions (for example, the driver can pass a pointer to this file object to the *pFile* parameter in a call to the [**IWDFIoTarget::FormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559233) method) if the driver must send I/O on this file object's default session. To obtain the intra-stack file object, the driver can call the [**IWDFIoTarget::GetTargetFile**](https://msdn.microsoft.com/library/windows/hardware/ff559243) method.

This intra-stack file object is closed when the I/O target is disposed of either explicitly, when the driver calls the [**IWDFObject::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) method on the I/O target, or implicitly, when the I/O target's parent is disposed of.

If any I/O remains outstanding on this intra-stack file object at the time of device removal, this file object will fail to close, and UMDF will generate a driver stop. For more information, see [Creating and Using Driver-Created File Objects](creating-and-using-driver-created-file-objects.md).

 

 





