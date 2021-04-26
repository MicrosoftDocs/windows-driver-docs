---
title: Handling Rollback Operations
description: Handling Rollback Operations
keywords: ["transactions WDK KTM , rolling back transactions", "rolling back transactions WDK KTM", "resource managers WDK KTM , rolling backing transactions", "transactional clients WDK KTM , rolling back transactions"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Rollback Operations


A resource manager, a transactional client, or KTM can roll back a transaction if it determines that the transaction must not be committed (typically because an error has been detected).

To roll back a transaction, a resource manager can call [**ZwRollbackEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackenlistment). After the resource manager has called [**ZwCreateEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateenlistment) to enlist in a transaction, it can roll back the transaction at any time before it calls [**ZwPrepareComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreparecomplete).

Transactional clients can roll back their transactions by calling [**ZwRollbackTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbacktransaction). After a transactional client has called [**ZwCreateTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransaction) to create a transaction, it can roll back the transaction at any time before it calls [**ZwCommitTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommittransaction).

In addition, a transactional client can set a time-out value for a transaction by calling [**ZwSetInformationTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationtransaction). KTM rolls back the transaction if it has not been committed by the specified amount of time.

When a call to **ZwRollbackEnlistment** or **ZwRollbackTransaction** is made, or when a time-out value is exceeded, KTM sends a TRANSACTION\_NOTIFY\_ROLLBACK [notification](transaction-notifications.md) to all resource managers.

When each resource manager receives a TRANSACTION\_NOTIFY\_ROLLBACK notification, it must do the following:

1.  Restore the transaction's data to the state that it was in before the resource manager enlisted in the transaction.

    Typically, a resource manager restores the transaction's data by copying the transaction's saved initial data from the log stream to the database's public, permanent storage. For more information about how to use log streams, see [Using Log Streams with KTM](using-log-streams-with-ktm.md).

2.  Call [**ZwRollbackComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackcomplete).

After calling **ZwRollbackComplete**, the resource manager should call [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) to close the enlistment handle.

If a resource manager initiated the rollback operation, it must use its client interface to inform the client that the transaction failed.

 

