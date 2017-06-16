---
title: Using TmXxx Routines
author: windows-driver-content
description: Using TmXxx Routines
ms.assetid: 8bc763e9-e67c-4810-9901-e5dc1a1cfd0c
keywords: ["Kernel Transaction Manager WDK , TmXxx routines", "KTM WDK , TmXxx routines", "TmXxx routines WDK KTM"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using TmXxx Routines


Most [KTM routines](https://msdn.microsoft.com/library/windows/hardware/ff553232) use a naming format of **Zw*Xxx***. These routines are handle-based. That is, at least one of their input or output parameters is a handle to a KTM object.

KTM also provides a smaller number of routines that use a naming format of **Tm*Xxx***. These routines are pointer-based. At least one of their input or output parameters is a pointer to a KTM object.

Some **Tm*Xxx*** routines duplicate **Zw*Xxx*** routines. Other **Tm*Xxx*** routines do not have **Zw*Xxx*** equivalents.

In most cases, you should use the **Zw*Xxx*** routines. But you should use **Tm*Xxx*** routines in the following situations:

-   Your resource manager uses the [**ResourceManagerNotification**](https://msdn.microsoft.com/library/windows/hardware/ff561077) callback routine, which provides a pointer to an enlistment object instead of a handle.

    You can pass the enlistment object pointer to the enlistment object's **Tm*Xxx*** routines.

-   Your transaction processing system (TPS) component performs many rapid calls to KTM, which potentially causes system performance to be too slow.

    In this case, your component can call [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679) to convert each KTM object handle to a pointer, save the pointer, and then pass the pointer to **Tm*Xxx*** routines. This conversion eliminates the need for KTM to convert each handle to a pointer internally every time that a **Zw*Xxx*** routine is called.

    Each call to **ObReferenceObectByHandle** should include an access mask that contains appropriate KTM-defined flags. These flags are described on the reference pages for KTM's create and open routines.

    When your component has finished using the KTM object, it must dereference the object by calling either [**ObDereferenceObjectDeferDelete**](https://msdn.microsoft.com/library/windows/hardware/ff557728) or [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724).

    -   You must use **ObDereferenceObjectDeferDelete** if your component, or any other component in your driver stack, is holding any system-provided locks, such as spin locks, mutex objects, or fast mutexes.

    -   You can use **ObDereferenceObject** if you are sure that no component on your driver stack holds system-provided locks.

    Deadlocks can occur if your component calls **ObDereferenceObject** while holding locks, because KTM might also be holding locks for the object namespace. Also, your component can call [**TmGetTransactionId**](https://msdn.microsoft.com/library/windows/hardware/ff564679) to quickly obtain a transaction's identifier more efficiently than calling [**ZwQueryInformationTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567057).

-   You must have a capability that a **Zw*Xxx*** routine does not provide.

    Specifically, a resource manager can call the following routines:

    -   [**TmEnableCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff564676) to enable asynchronous delivery of notifications by a callback routine.
    -   [**TmReferenceEnlistmentKey**](https://msdn.microsoft.com/library/windows/hardware/ff564726) and [**TmDereferenceEnlistmentKey**](https://msdn.microsoft.com/library/windows/hardware/ff564671) to increment or decrement an enlistment object's key reference count.
    -   [**TmRequestOutcomeEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff564727) to request an immediate commit or rollback notification for an enlistment.
    -   [**TmIsTransactionActive**](https://msdn.microsoft.com/library/windows/hardware/ff564681) to determine whether a transaction is in its active state.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20TmXxx%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


