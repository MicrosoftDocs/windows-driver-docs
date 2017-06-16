---
title: Transaction Objects
author: windows-driver-content
description: Transaction Objects
ms.assetid: 124105bd-70be-49b1-8ea4-af6ba1f3cf16
keywords: ["transactions WDK KTM , objects", "transactions WDK KTM", "transactional clients WDK KTM , creating transactions", "Kernel Transaction Manager WDK , transactions", "KTM WDK , transactions", "transaction objects WDK KTM"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Transaction Objects


*Transaction objects* represent transactions. A transactional client creates a transaction, performs some work, and the either commits or rolls back the transaction.

KTM provides a set of [transaction object routines](https://msdn.microsoft.com/library/windows/hardware/ff564831) that kernel-mode transactional clients can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates a transaction object when a client calls [**ZwCreateTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566429). The client can call either [**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420) or [**ZwRollbackTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567086) to commit or roll back the transaction.

[TPS components](understanding-tps-components.md) can call [**ZwOpenTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567033) to open additional handles to a transaction object.

Clients close their handles to transaction objects by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417). If the last handle is closed before the transaction object has been committed, KTM sends TRANSACTION\_NOTIFY\_ROLLBACK notifications to all resource managers that have an enlistment for the transaction.

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Transaction%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


