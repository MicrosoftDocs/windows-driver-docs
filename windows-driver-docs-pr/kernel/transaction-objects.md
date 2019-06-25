---
title: Transaction Objects
description: Transaction Objects
ms.assetid: 124105bd-70be-49b1-8ea4-af6ba1f3cf16
keywords: ["transactions WDK KTM , objects", "transactions WDK KTM", "transactional clients WDK KTM , creating transactions", "Kernel Transaction Manager WDK , transactions", "KTM WDK , transactions", "transaction objects WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Transaction Objects


*Transaction objects* represent transactions. A transactional client creates a transaction, performs some work, and the either commits or rolls back the transaction.

KTM provides a set of [transaction object routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index) that kernel-mode transactional clients can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates a transaction object when a client calls [**ZwCreateTransaction**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ntcreatetransaction). The client can call either [**ZwCommitTransaction**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ntcommittransaction) or [**ZwRollbackTransaction**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ntrollbacktransaction) to commit or roll back the transaction.

[TPS components](understanding-tps-components.md) can call [**ZwOpenTransaction**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ntopentransaction) to open additional handles to a transaction object.

Clients close their handles to transaction objects by calling [**ZwClose**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-ntclose). If the last handle is closed before the transaction object has been committed, KTM sends TRANSACTION\_NOTIFY\_ROLLBACK notifications to all resource managers that have an enlistment for the transaction.

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

 




