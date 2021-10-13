---
title: Registering for Notifications
description: Registering for Notifications
keywords: ["filtering registry calls WDK kernel , registering for notifications", "registry filtering drivers WDK kernel , registering for notifications", "registering filter registry call notifications", "pre-notification option WDK filter registry call", "post-notification option WDK filter registry call", "notifications WDK filter registry call"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering for Notifications


To filter registry calls, your kernel-mode registry filtering driver must first call [**CmRegisterCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallback) or [**CmRegisterCallbackEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex) to register a [**RegistryCallback**](/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function) routine. (For Windows Vista and later operating system versions, drivers should use **CmRegisterCallbackEx** instead of **CmRegisterCallback**.)

After your driver has registered a *RegistryCallback* routine, the configuration manager calls the routine each time that a thread attempts to perform a registry operation. Threads that perform registry operations can be from user-mode applications that call the user-mode registry routines (**RegCreateKeyEx**, **RegOpenKeyEx**, and so on) and from drivers that call the kernel-mode registry routines ([**ZwCreateKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey), [**ZwOpenKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey), and so on).

For most operations, your driver can receive notification before the configuration manager processes the registry operation (a *pre-notification*) or immediately after the operation completes (but before the configuration manager returns to the caller—a *post-notification*). For a list of the types of notifications that your driver can receive, see [**REG\_NOTIFY\_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_reg_notify_class).

After a driver has called **CmRegisterCallback** or **CmRegisterCallbackEx**, the driver will receive notifications until it calls [**CmUnRegisterCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmunregistercallback) or is unloaded.

 

