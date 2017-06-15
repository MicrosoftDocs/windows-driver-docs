---
title: Registering for Notifications
author: windows-driver-content
description: Registering for Notifications
MS-HAID:
- 'Other\_7dd52e70-ae41-4b4e-9cbd-199bec8fa571.xml'
- 'kernel.registering\_for\_notifications'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 06109726-77e8-49de-9486-4fa2a5aceb1c
keywords: ["filtering registry calls WDK kernel , registering for notifications", "registry filtering drivers WDK kernel , registering for notifications", "registering filter registry call notifications", "pre-notification option WDK filter registry call", "post-notification option WDK filter registry call", "notifications WDK filter registry call"]
---

# Registering for Notifications


To filter registry calls, your kernel-mode registry filtering driver must first call [**CmRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541918) or [**CmRegisterCallbackEx**](https://msdn.microsoft.com/library/windows/hardware/ff541921) to register a [**RegistryCallback**](https://msdn.microsoft.com/library/windows/hardware/ff560903) routine. (For Windows Vista and later operating system versions, drivers should use **CmRegisterCallbackEx** instead of **CmRegisterCallback**.)

After your driver has registered a *RegistryCallback* routine, the configuration manager calls the routine each time that a thread attempts to perform a registry operation. Threads that perform registry operations can be from user-mode applications that call the user-mode registry routines (**RegCreateKeyEx**, **RegOpenKeyEx**, and so on) and from drivers that call the kernel-mode registry routines ([**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425), [**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014), and so on).

For most operations, your driver can receive notification before the configuration manager processes the registry operation (a *pre-notification*) or immediately after the operation completes (but before the configuration manager returns to the caller—a *post-notification*). For a list of the types of notifications that your driver can receive, see [**REG\_NOTIFY\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560950).

After a driver has called **CmRegisterCallback** or **CmRegisterCallbackEx**, the driver will receive notifications until it calls [**CmUnRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541928) or is unloaded.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20for%20Notifications%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


