---
title: Transaction Manager Objects
description: Transaction Manager Objects
ms.assetid: af53cda4-e2ab-47df-9311-a4da2a2ee08d
keywords: ["log streams WDK KTM , creating", "virtual clock values WDK KTM , in transaction manager objects", "Kernel Transaction Manager WDK , transaction managers", "transaction manager objects WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Transaction Manager Objects


The main purpose of the *transaction manager object* is to create and maintain a [Common Log File System](using-common-log-file-system.md) (CLFS) log stream that KTM uses to record status information about transactions.

The transaction manager object also contains a [virtual clock value](using-virtual-clock-values.md) that KTM maintains and uses to sequence information in the object's log stream.

KTM provides a set of [transaction manager object routines](https://msdn.microsoft.com/library/windows/hardware/ff564807) that kernel-mode [TPS components](understanding-tps-components.md) can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates a transaction manager object when a resource manager calls [**ZwCreateTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff566430). Typically, each resource manager in a TPS creates a transaction manager object. But you can also design a TPS in which several resource managers share a single transaction manager object.

TPS components can open additional handles to an existing transaction manager object by calling [**ZwOpenTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567035). For example, if your TPS has several resource managers that share a single transaction manager object, one resource manager calls **ZwCreateTransactionManager** and then passes the object GUID to the other resource managers so that they can call **ZwOpenTransactionManager**.

Resource managers close their handles to transaction manager objects by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417).

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

 




