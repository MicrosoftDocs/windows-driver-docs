---
title: Enlistment Objects
description: Enlistment Objects
ms.assetid: 80e61475-4bb7-4eaa-b9f1-ff95eac9bc77
keywords: ["enlistments WDK KTM", "enlistments WDK KTM , objects", "resource managers WDK KTM , creating enlistments", "Kernel Transaction Manager WDK , enlistments", "KTM WDK , enlistments", "enlistment objects WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Enlistment Objects


An *enlistment object* represents a resource manager's [*enlistment*](transaction-processing-terms.md#ktm-term-enlistment) to a transaction. Before a resource manager can receive notifications about a transaction's events, the resource manager must call [**ZwCreateEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566422) to create an enlistment to the transaction.

KTM provides a set of [enlistment object routines](https://msdn.microsoft.com/library/windows/hardware/ff544270) that kernel-mode resource managers can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates an enlistment object when a resource manager calls **ZwCreateEnlistment** to enlist in a transaction that the resource manager has received (typically from a transactional client).

[TPS components](understanding-tps-components.md) can call [**ZwOpenEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567008) to open additional handles to an enlistment object. But most TPS designs do not require additional open handles.

Resource managers close their handles to enlistment objects by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417). If the last handle is closed before the associated transaction object has been committed, KTM sends TRANSACTION\_NOTIFY\_ROLLBACK notifications to all the resource managers that have an enlistment for the transaction.

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

 




