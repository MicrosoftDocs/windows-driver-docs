---
title: Transaction Manager Objects
author: windows-driver-content
description: Transaction Manager Objects
MS-HAID:
- 'ktm\_dg\_04dc8582-4f46-4bad-9ee1-c58d89ea4cf3.xml'
- 'kernel.transaction\_manager\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: af53cda4-e2ab-47df-9311-a4da2a2ee08d
keywords: ["log streams WDK KTM , creating", "virtual clock values WDK KTM , in transaction manager objects", "Kernel Transaction Manager WDK , transaction managers", "transaction manager objects WDK KTM"]
---

# Transaction Manager Objects


The main purpose of the *transaction manager object* is to create and maintain a [Common Log File System](using-common-log-file-system.md) (CLFS) log stream that KTM uses to record status information about transactions.

The transaction manager object also contains a [virtual clock value](using-virtual-clock-values.md) that KTM maintains and uses to sequence information in the object's log stream.

KTM provides a set of [transaction manager object routines](https://msdn.microsoft.com/library/windows/hardware/ff564807) that kernel-mode [TPS components](understanding-tps-components.md) can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates a transaction manager object when a resource manager calls [**ZwCreateTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff566430). Typically, each resource manager in a TPS creates a transaction manager object. But you can also design a TPS in which several resource managers share a single transaction manager object.

TPS components can open additional handles to an existing transaction manager object by calling [**ZwOpenTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567035). For example, if your TPS has several resource managers that share a single transaction manager object, one resource manager calls **ZwCreateTransactionManager** and then passes the object GUID to the other resource managers so that they can call **ZwOpenTransactionManager**.

Resource managers close their handles to transaction manager objects by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417).

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Transaction%20Manager%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


