---
title: Transaction Objects
description: Transaction Objects
keywords: ["transactions WDK KTM , objects", "transactions WDK KTM", "transactional clients WDK KTM , creating transactions", "Kernel Transaction Manager WDK , transactions", "KTM WDK , transactions", "transaction objects WDK KTM"]
ms.date: 06/16/2017
---

# Transaction Objects


*Transaction objects* represent transactions. A transactional client creates a transaction, performs some work, and the either commits or rolls back the transaction.

KTM provides a set of transaction object routines that kernel-mode transactional clients can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates a transaction object when a client calls [**ZwCreateTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransaction). The client can call either [**ZwCommitTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommittransaction) or [**ZwRollbackTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbacktransaction) to commit or roll back the transaction.

[TPS components](understanding-tps-components.md) can call [**ZwOpenTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransaction) to open additional handles to a transaction object.

Clients close their handles to transaction objects by calling [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose). If the last handle is closed before the transaction object has been committed, KTM sends TRANSACTION\_NOTIFY\_ROLLBACK notifications to all resource managers that have an enlistment for the transaction.

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

