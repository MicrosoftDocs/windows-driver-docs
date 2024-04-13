---
title: Invalid Key Object Pointers in Registry Notifications
description: Invalid Key Object Pointers in Registry Notifications
ms.date: 10/17/2018
---

# Invalid Key Object Pointers in Registry Notifications


To avoid fatal errors and possible memory corruption, a registry filtering driver must not try to access a key object by using an invalid object pointer. This topic lists the circumstances in which the **Object** member of a registry callback notification structure might contain an undefined, non-**NULL** value.

In a registry filtering driver, the second parameter of the [*RegistryCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function) routine is a [**REG\_NOTIFY\_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_reg_notify_class) enumeration value. This value indicates which type of registry callback notification structure the third parameter of the *RegistryCallback* routine points to. The notification structure contains information about the registry operation. The type of this structure varies according to the registry operation that is being performed.

Many of the notification structure types contain an **Object** member that points to a key object. In some cases, the **Object** member can contain a value that is non-**NULL**, but is not a pointer to a valid key object.

### Key Object Value is Undefined

If the second parameter in a call to the *RegistryCallback* routine of a registry filtering driver is a **REG\_NOTIFY\_CLASS** enumeration value of **RegNtPostCreateKeyEx** or **RegNtPostOpenKeyEx**, the third parameter is a pointer to a [**REG\_POST\_OPERATION\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_post_operation_information) structure. The **Object** member of this structure is valid only if the **Status** member of the structure is set to STATUS\_SUCCESS. Any other **Status** value, including a nonzero status code for which the **NT\_SUCCESS** macro evaluates to **TRUE**, indicates that the value of the **Object** member is undefined.

### Key Object Value is Not in a Valid State

If the second parameter in a registry callback is one of the following **REG\_NOTIFY\_CLASS** enumeration values, the **Object** member of the registry callback notification structure points to a key object that is being destroyed and whose reference count is zero:

-   **RegNtPreKeyHandleClose** ([**REG\_KEY\_HANDLE\_CLOSE\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_key_handle_close_information) structure)

-   **RegNtPostKeyHandleClose** ([**REG\_POST\_OPERATION\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_post_operation_information) structure)

-   **RegNtCallbackObjectContextCleanup** ([**REG\_CALLBACK\_CONTEXT\_CLEANUP\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_callback_context_cleanup_information) structure)

Because the **Object** member points to a key object that is not in a valid state, the registry filtering driver must not pass the **Object** pointer value as a parameter to a [Windows driver support routine](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbypointer) (for example, **ObReferenceObjectByPointer**).

However, during a [*RegistryCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function) call to handle a **RegNtPreKeyHandleClose** or **RegNtPostKeyHandleClose** notification, a registry filter driver can call a configuration manager routine (for example, [**CmGetBoundTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmgetboundtransaction)) that takes a registry object as a parameter.

 

