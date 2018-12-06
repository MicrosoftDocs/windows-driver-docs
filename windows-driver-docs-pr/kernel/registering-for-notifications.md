---
title: Registering for Notifications
description: Registering for Notifications
ms.assetid: 06109726-77e8-49de-9486-4fa2a5aceb1c
keywords: ["filtering registry calls WDK kernel , registering for notifications", "registry filtering drivers WDK kernel , registering for notifications", "registering filter registry call notifications", "pre-notification option WDK filter registry call", "post-notification option WDK filter registry call", "notifications WDK filter registry call"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering for Notifications


To filter registry calls, your kernel-mode registry filtering driver must first call [**CmRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541918) or [**CmRegisterCallbackEx**](https://msdn.microsoft.com/library/windows/hardware/ff541921) to register a [**RegistryCallback**](https://msdn.microsoft.com/library/windows/hardware/ff560903) routine. (For Windows Vista and later operating system versions, drivers should use **CmRegisterCallbackEx** instead of **CmRegisterCallback**.)

After your driver has registered a *RegistryCallback* routine, the configuration manager calls the routine each time that a thread attempts to perform a registry operation. Threads that perform registry operations can be from user-mode applications that call the user-mode registry routines (**RegCreateKeyEx**, **RegOpenKeyEx**, and so on) and from drivers that call the kernel-mode registry routines ([**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425), [**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014), and so on).

For most operations, your driver can receive notification before the configuration manager processes the registry operation (a *pre-notification*) or immediately after the operation completes (but before the configuration manager returns to the caller—a *post-notification*). For a list of the types of notifications that your driver can receive, see [**REG\_NOTIFY\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560950).

After a driver has called **CmRegisterCallback** or **CmRegisterCallbackEx**, the driver will receive notifications until it calls [**CmUnRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541928) or is unloaded.

 

 




