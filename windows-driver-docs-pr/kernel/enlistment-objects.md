---
title: Enlistment Objects
author: windows-driver-content
description: Enlistment Objects
ms.assetid: 80e61475-4bb7-4eaa-b9f1-ff95eac9bc77
keywords: ["enlistments WDK KTM", "enlistments WDK KTM , objects", "resource managers WDK KTM , creating enlistments", "Kernel Transaction Manager WDK , enlistments", "KTM WDK , enlistments", "enlistment objects WDK KTM"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enlistment Objects


An *enlistment object* represents a resource manager's [*enlistment*](transaction-processing-terms.md#ktm-term-enlistment) to a transaction. Before a resource manager can receive notifications about a transaction's events, the resource manager must call [**ZwCreateEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566422) to create an enlistment to the transaction.

KTM provides a set of [enlistment object routines](https://msdn.microsoft.com/library/windows/hardware/ff544270) that kernel-mode resource managers can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates an enlistment object when a resource manager calls **ZwCreateEnlistment** to enlist in a transaction that the resource manager has received (typically from a transactional client).

[TPS components](understanding-tps-components.md) can call [**ZwOpenEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567008) to open additional handles to an enlistment object. But most TPS designs do not require additional open handles.

Resource managers close their handles to enlistment objects by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417). If the last handle is closed before the associated transaction object has been committed, KTM sends TRANSACTION\_NOTIFY\_ROLLBACK notifications to all the resource managers that have an enlistment for the transaction.

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Enlistment%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


