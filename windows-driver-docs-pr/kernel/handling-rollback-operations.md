---
title: Handling Rollback Operations
author: windows-driver-content
description: Handling Rollback Operations
MS-HAID:
- 'ktm\_dg\_2f52bca1-eca6-4181-b73f-dbeb74ada53a.xml'
- 'kernel.handling\_rollback\_operations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d36bfac8-47dc-4fcd-a6e2-feb27d244630
keywords: ["transactions WDK KTM , rolling back transactions", "rolling back transactions WDK KTM", "resource managers WDK KTM , rolling backing transactions", "transactional clients WDK KTM , rolling back transactions"]
---

# Handling Rollback Operations


A resource manager, a transactional client, or KTM can roll back a transaction if it determines that the transaction must not be committed (typically because an error has been detected).

To roll back a transaction, a resource manager can call [**ZwRollbackEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567083). After the resource manager has called [**ZwCreateEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566422) to enlist in a transaction, it can roll back the transaction at any time before it calls [**ZwPrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567037).

Transactional clients can roll back their transactions by calling [**ZwRollbackTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567086). After a transactional client has called [**ZwCreateTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566429) to create a transaction, it can roll back the transaction at any time before it calls [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420).

In addition, a transactional client can set a time-out value for a transaction by calling [**ZwSetInformationTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567104). KTM rolls back the transaction if it has not been committed by the specified amount of time.

When a call to **ZwRollbackEnlistment** or **ZwRollbackTransaction** is made, or when a time-out value is exceeded, KTM sends a TRANSACTION\_NOTIFY\_ROLLBACK [notification](transaction-notifications.md) to all resource managers.

When each resource manager receives a TRANSACTION\_NOTIFY\_ROLLBACK notification, it must do the following:

1.  Restore the transaction's data to the state that it was in before the resource manager enlisted in the transaction.

    Typically, a resource manager restores the transaction's data by copying the transaction's saved initial data from the log stream to the database's public, permanent storage. For more information about how to use log streams, see [Using Log Streams with KTM](using-log-streams-with-ktm.md).

2.  Call [**ZwRollbackComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567081).

After calling **ZwRollbackComplete**, the resource manager should call [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) to close the enlistment handle.

If a resource manager initiated the rollback operation, it must use its client interface to inform the client that the transaction failed.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Rollback%20Operations%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


