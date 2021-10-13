---
title: Specifying Context Information
description: Specifying Context Information
keywords: ["filtering registry calls WDK kernel , context information", "registry filtering drivers WDK kernel , context information", "context information", "context information WDK filter registry call"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Specifying Context Information


The configuration manager provides several ways for registry filtering drivers to assign context information to registry operations. A registry filtering driver can:

-   Assign context information to the [*RegistryCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function) routine.

    When your driver calls [**CmRegisterCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallback) or [**CmRegisterCallbackEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex) to register for notification of a registry operation, the driver can specify a driver-defined context value. The configuration manager passes this context value to the driver's *RegistryCallback* routine each time that the configuration manager calls the routine.

    This context information is supported starting with Windows XP.

-   Assign context information to a registry operation.

    Drivers can store operation-specific context information in the **CallContext** member of each **REG\_*XXX*\_KEY\_INFORMATION** structure that the driver's *RegistryCallback* routine receives. If your driver receives both a pre-notification and a post-notification for a registry operation, the [**REG\_POST\_OPERATION\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_post_operation_information) structure contains a pointer to the appropriate pre-notification structure. When a *RegistryCallback* routine receives a **REG\_POST\_OPERATION\_INFORMATION** structure, the **CallContext** member of that structure matches the **CallContext** member of the pre-notification structure.

    The **CallContext** member of these structures is available starting with Windows Vista.

-   Assign context information to a registry key object.

    A [*RegistryCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function) routine can assign context information to a particular registry key object. If the *RegistryCallback* routine calls [**CmSetCallbackObjectContext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmsetcallbackobjectcontext) to assign context information to a key object, subsequent pre-notifications and post-notifications for all operations on the object will include the context value in the **ObjectContext** member of each **REG\_*XXX*\_KEY\_INFORMATION** structure. If a driver provides multiple *RegistryCallback* routines, the driver can assign different context information for each routine, for a single registry key object.

    If a driver has called **CmSetCallbackObjectContext**, the driver's *RegistryCallback* routine will receive a **RegNtCallbackObjectContextCleanup** notification after the key object's handle has been closed. In response to this notification, the routine should release any resources that it allocated for the object's context. When the *Argument1* parameter to the *RegistryCallback* routine is **RegNtCallbackObjectContextCleanup**, the *Argument2* parameter is a pointer to a [**REG\_CALLBACK\_CONTEXT\_CLEANUP\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_callback_context_cleanup_information) structure that contains a pointer to the context.

    The **CmSetCallbackObjectContext** routine and **RegNtCallbackObjectContextCleanup** notification are available starting with Windows Vista.

 

