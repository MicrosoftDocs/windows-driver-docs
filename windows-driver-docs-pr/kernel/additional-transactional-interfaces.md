---
title: Additional Transactional Interfaces
author: windows-driver-content
description: Additional Transactional Interfaces
MS-HAID:
- 'ktm\_dg\_2adba2ca-2981-4b8c-92b8-fc96fcc3bda3.xml'
- 'kernel.additional\_transactional\_interfaces'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cbd88c96-6445-436b-8e02-09dd9cf40d77
keywords: ["transactions WDK KTM , non-KTM interfaces", "transactional interfaces WDK"]
---

# Additional Transactional Interfaces


In addition to the transactional interfaces that you can use by accessing KTM, Microsoft provides several additional transactional interfaces, including the following:

-   For file system minifilter drivers, the [filter manager](https://msdn.microsoft.com/library/windows/hardware/ff541591) provides routines that enable minifilter drivers to enlist in transactions, receive notification about transaction state changes, and attach contexts to transactions. For more information about these capabilities, see [**FltEnlistInTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff542053).

-   Beginning with Windows Vista, the NTFS file system and the registry are implemented as resource managers that support transactional operations. For more information about transactional NTFS and transactional registry capabilities, see the Microsoft Windows SDK.

-   The Distributed Transaction Coordinator (DTC) provides interoperability with KTM through the **IKernelTransaction** interface. For more information about the **IKernelTransaction** interface, see the Microsoft Windows SDK.

-   The .NET Framework supports the **System.Transactions** namespace. For more information about this namespace, see the [MSDN website](http://go.microsoft.com/fwlink/p/?linkid=8714).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Additional%20Transactional%20Interfaces%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


