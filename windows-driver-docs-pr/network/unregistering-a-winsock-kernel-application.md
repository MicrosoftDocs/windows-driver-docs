---
title: Unregistering a Winsock Kernel Application
description: Unregistering a Winsock Kernel Application
ms.assetid: f5d99c10-eeac-499e-8630-6aa188d38d75
keywords:
- Winsock Kernel WDK networking , registering
- unregistering Winsock Kernel applications
- WSK WDK networking , registering
- WskDeregister
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unregistering a Winsock Kernel Application


A Winsock Kernel (WSK) application that has successfully registered as a WSK client with the [**WskRegister**](https://msdn.microsoft.com/library/windows/hardware/ff571143) function must ensure that [**WskDeregister**](https://msdn.microsoft.com/library/windows/hardware/ff571128) has been called, and the call has returned, before the driver's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function returns. A WSK application that has called **WskRegister** successfully should never unload without calling **WskDeregister**, which will wait to unregister the WSK client object until all captured instances of the WSK provider NPI are released with [**WskReleaseProviderNPI**](https://msdn.microsoft.com/library/windows/hardware/ff571145) and all sockets are closed by the WSK application. If there are pending IRPs that were passed to the functions in [**WSK\_PROVIDER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571175), **WskDeregister** will also wait until those pending IRPs complete. A WSK application should never call the functions in WSK\_PROVIDER\_DISPATCH after **WskReleaseProviderNPI** is called.

For example:

```C++
// Unload function
VOID
  Unload(
    IN PDRIVER_OBJECT DriverObject
    )
{
  // Unregister the WSK application
  WskDeregister(
    &WskRegistration
    );

}
```

A WSK application is not necessarily required to always call **WskDeregister** from within its *Unload* function. For example, if a WSK application is a subcomponent of a complex driver, the WSK application's call to **WskDeregister** might occur when the WSK application subcomponent is deactivated. In such a scenario, before the driver returns from its *Unload* function, it must still ensure that the WSK application has been successfully unregistered with a call to **WskDeregister**.

 

 





