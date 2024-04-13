---
title: Using TmXxx Routines
description: Using TmXxx Routines
keywords: ["Kernel Transaction Manager WDK , TmXxx routines", "KTM WDK , TmXxx routines", "TmXxx routines WDK KTM"]
ms.date: 06/16/2017
---

# Using TmXxx Routines


Most KTM routines use a naming format of **Zw*Xxx***. These routines are handle-based. That is, at least one of their input or output parameters is a handle to a KTM object.

KTM also provides a smaller number of routines that use a naming format of **Tm*Xxx***. These routines are pointer-based. At least one of their input or output parameters is a pointer to a KTM object.

Some **Tm*Xxx*** routines duplicate **Zw*Xxx*** routines. Other **Tm*Xxx*** routines do not have **Zw*Xxx*** equivalents.

In most cases, you should use the **Zw*Xxx*** routines. But you should use **Tm*Xxx*** routines in the following situations:

- Your resource manager uses the [**ResourceManagerNotification**](/windows-hardware/drivers/ddi/wdm/nc-wdm-ptm_rm_notification) callback routine, which provides a pointer to an enlistment object instead of a handle.

  You can pass the enlistment object pointer to the enlistment object's **Tm*Xxx*** routines.

- Your transaction processing system (TPS) component performs many rapid calls to KTM, which potentially causes system performance to be too slow.

  In this case, your component can call [**ObReferenceObjectByHandle**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle) to convert each KTM object handle to a pointer, save the pointer, and then pass the pointer to **Tm*Xxx*** routines. This conversion eliminates the need for KTM to convert each handle to a pointer internally every time that a **Zw*Xxx*** routine is called.

  Each call to **ObReferenceObectByHandle** should include an access mask that contains appropriate KTM-defined flags. These flags are described on the reference pages for KTM's create and open routines.

  When your component has finished using the KTM object, it must dereference the object by calling either [**ObDereferenceObjectDeferDelete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobjectdeferdelete) or [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject).

  -   You must use **ObDereferenceObjectDeferDelete** if your component, or any other component in your driver stack, is holding any system-provided locks, such as spin locks, mutex objects, or fast mutexes.

  -   You can use **ObDereferenceObject** if you are sure that no component on your driver stack holds system-provided locks.

  Deadlocks can occur if your component calls **ObDereferenceObject** while holding locks, because KTM might also be holding locks for the object namespace. Also, your component can call [**TmGetTransactionId**](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmgettransactionid) to quickly obtain a transaction's identifier more efficiently than calling [**ZwQueryInformationTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransaction).

- You must have a capability that a **Zw*Xxx*** routine does not provide.

  Specifically, a resource manager can call the following routines:

  -   [**TmEnableCallbacks**](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmenablecallbacks) to enable asynchronous delivery of notifications by a callback routine.
  -   [**TmReferenceEnlistmentKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmreferenceenlistmentkey) and [**TmDereferenceEnlistmentKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmdereferenceenlistmentkey) to increment or decrement an enlistment object's key reference count.
  -   [**TmRequestOutcomeEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmrequestoutcomeenlistment) to request an immediate commit or rollback notification for an enlistment.
  -   [**TmIsTransactionActive**](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmistransactionactive) to determine whether a transaction is in its active state.

 

