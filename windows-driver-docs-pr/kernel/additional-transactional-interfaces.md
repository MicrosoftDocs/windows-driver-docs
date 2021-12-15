---
title: Additional Transactional Interfaces
description: Additional Transactional Interfaces
keywords: ["transactions WDK KTM , non-KTM interfaces", "transactional interfaces WDK"]
ms.date: 06/16/2017
---

# Additional Transactional Interfaces


In addition to the transactional interfaces that you can use by accessing KTM, Microsoft provides several additional transactional interfaces, including the following:

-   For file system minifilter drivers, the [filter manager](../ifs/filter-manager-concepts.md) provides routines that enable minifilter drivers to enlist in transactions, receive notification about transaction state changes, and attach contexts to transactions. For more information about these capabilities, see [**FltEnlistInTransaction**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltenlistintransaction).

-   Beginning with Windows Vista, the NTFS file system and the registry are implemented as resource managers that support transactional operations. For more information about transactional NTFS and transactional registry capabilities, see the Microsoft Windows SDK.

-   The Distributed Transaction Coordinator (DTC) provides interoperability with KTM through the **IKernelTransaction** interface. For more information about the **IKernelTransaction** interface, see the Microsoft Windows SDK.

-   The .NET Framework supports the **System.Transactions** namespace. For more information about this namespace, see the [Microsoft developer website](https://go.microsoft.com/fwlink/p/?linkid=8714).

