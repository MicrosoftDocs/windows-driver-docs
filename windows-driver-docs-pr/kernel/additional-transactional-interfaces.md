---
title: Additional Transactional Interfaces
description: Additional Transactional Interfaces
ms.assetid: cbd88c96-6445-436b-8e02-09dd9cf40d77
keywords: ["transactions WDK KTM , non-KTM interfaces", "transactional interfaces WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Additional Transactional Interfaces


In addition to the transactional interfaces that you can use by accessing KTM, Microsoft provides several additional transactional interfaces, including the following:

-   For file system minifilter drivers, the [filter manager](https://msdn.microsoft.com/library/windows/hardware/ff541591) provides routines that enable minifilter drivers to enlist in transactions, receive notification about transaction state changes, and attach contexts to transactions. For more information about these capabilities, see [**FltEnlistInTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff542053).

-   Beginning with Windows Vista, the NTFS file system and the registry are implemented as resource managers that support transactional operations. For more information about transactional NTFS and transactional registry capabilities, see the Microsoft Windows SDK.

-   The Distributed Transaction Coordinator (DTC) provides interoperability with KTM through the **IKernelTransaction** interface. For more information about the **IKernelTransaction** interface, see the Microsoft Windows SDK.

-   The .NET Framework supports the **System.Transactions** namespace. For more information about this namespace, see the [Microsoft developer website](http://go.microsoft.com/fwlink/p/?linkid=8714).

 

 




