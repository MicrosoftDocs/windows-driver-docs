---
title: Handling Rollback Operations
description: Handling Rollback Operations
ms.assetid: d36bfac8-47dc-4fcd-a6e2-feb27d244630
keywords: ["transactions WDK KTM , rolling back transactions", "rolling back transactions WDK KTM", "resource managers WDK KTM , rolling backing transactions", "transactional clients WDK KTM , rolling back transactions"]
ms.date: 06/16/2017
ms.localizationpriority: medium
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

 

 




