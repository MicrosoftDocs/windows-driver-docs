---
title: Unregistering a Winsock Kernel Application
description: Unregistering a Winsock Kernel Application
keywords:
- Winsock Kernel WDK networking , registering
- unregistering Winsock Kernel applications
- WSK WDK networking , registering
- WskDeregister
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unregistering a Winsock Kernel Application


A Winsock Kernel (WSK) application that has successfully registered as a WSK client with the [**WskRegister**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskregister) function must ensure that [**WskDeregister**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskderegister) has been called, and the call has returned, before the driver's [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) function returns. A WSK application that has called **WskRegister** successfully should never unload without calling **WskDeregister**, which will wait to unregister the WSK client object until all captured instances of the WSK provider NPI are released with [**WskReleaseProviderNPI**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskreleaseprovidernpi) and all sockets are closed by the WSK application. If there are pending IRPs that were passed to the functions in [**WSK\_PROVIDER\_DISPATCH**](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_dispatch), **WskDeregister** will also wait until those pending IRPs complete. A WSK application should never call the functions in WSK\_PROVIDER\_DISPATCH after **WskReleaseProviderNPI** is called.

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

 

