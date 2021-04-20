---
title: Unloading a Client Module
description: Unloading a Client Module
keywords:
- client modules WDK Network Module Registrar , unloading
- unloading network modules
- NmrDeregisterClient
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unloading a Client Module


To unload a client module, the operating system calls the client module's [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) function. See [Initializing and Registering a Client Module](initializing-and-registering-a-client-module.md) for more information about how to specify a client module's **Unload** function during initialization.

A client module's [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) function ensures that the client module is deregistered from the Network Module Registrar (NMR) before the client module is unloaded from system memory. A client module initiates deregistration from the NMR by calling the [**NmrDeregisterClient**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrderegisterclient) function, which it typically calls from its **Unload** function. A client module must not return from its **Unload** function until after it has been completely deregistered from the NMR. If the call to **NmrDeregisterClient** returns STATUS\_PENDING, the client module must call the [**NmrWaitForClientDeregisterComplete**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrwaitforclientderegistercomplete) function to wait for the deregistration to complete before it returns from its **Unload** function.

For example:

```C++
// Variable containing the handle for the registration
HANDLE ClientHandle;

// Unload function
VOID
  Unload(
    IN PDRIVER_OBJECT DriverObject
    )
{
  NTSTATUS Status;

  // Deregister the client module from the NMR
  Status =
    NmrDeregisterClient(
      ClientHandle
      );

  // Check if pending
  if (Status == STATUS_PENDING)
  {
    // Wait for the deregistration to be completed
    NmrWaitForClientDeregisterComplete(
      ClientHandle
      );
  }

  // An error occurred
  else
  {
    // Handle error
    ...
  }
}
```

If a client module is registered as a client of multiple [Network Programming Interfaces (NPIs)](network-programming-interface.md), it must call [**NmrDeregisterClient**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrderegisterclient) for each NPI that it supports. If a network module is registered as both a client module and a provider module (that is, it is a client of one NPI and a provider of another NPI), it must call both **NmrDeregisterClient** and [**NmrDeregisterProvider**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrderegisterprovider).

A network module must wait until all of the deregistrations are complete before returning from its [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) function.

A client module is not required to call [**NmrDeregisterClient**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrderegisterclient) from within its [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) function. For example, in the situation where a client module is a subcomponent of a complex driver, the deregistration of the client module might occur when the client module subcomponent is deactivated. However, in such a situation the driver must still ensure that the client module has been completely deregistered from the NMR before returning from its **Unload** function.

 

