---
title: Unloading a Provider Module
description: Unloading a Provider Module
ms.assetid: c6dd6552-2923-4091-9bf1-5833c049aa23
keywords:
- provider modules WDK Network Module Registrar , unloading
- unloading network modules
- NmrDeregisterProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unloading a Provider Module


To unload a provider module, the operating system calls the provider module's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function. See [Initializing and Registering a Provider Module](initializing-and-registering-a-provider-module.md) for more information about how to specify a provider module's **Unload** function during initialization.

A provider module's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function ensures that the provider module is deregistered from the Network Module Registrar (NMR) before the provider module is unloaded from system memory. A provider module initiates deregistration from the NMR by calling the [**NmrDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568778) function, which it typically calls from its **Unload** function. A provider module must not return from its **Unload** function until after it has been completely deregistered from the NMR. If the call to **NmrDeregisterProvider** returns STATUS\_PENDING, the provider module must call the [**NmrWaitForProviderDeregisterComplete**](https://msdn.microsoft.com/library/windows/hardware/ff568787) function to wait for the deregistration to complete before it returns from its **Unload** function.

For example:

```C++
// Variable containing the handle for the registration
HANDLE ProviderHandle;

// Unload function
VOID
  Unload(
    IN PDRIVER_OBJECT DriverObject
    )
{
  NTSTATUS Status;

  // Deregister the provider module from the NMR
  Status =
    NmrDeregisterProvider(
      ProviderHandle
      );

  // Check if pending
  if (Status == STATUS_PENDING)
  {
    // Wait for the deregistration to be completed
    NmrWaitForProviderDeregisterComplete(
      ProviderHandle
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

If a provider module is registered as a provider of multiple [Network Programming Interfaces (NPIs)](network-programming-interface.md), it must call [**NmrDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568778) for each NPI that it supports. If a network module is registered as both a provider module and a client module (that is, it is a provider of one NPI and a client of another NPI), it must call both **NmrDeregisterProvider** and [**NmrDeregisterClient**](https://msdn.microsoft.com/library/windows/hardware/ff568774).

A network module must wait until all of the deregistrations are complete before returning from its [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function.

A provider module is not required to call [**NmrDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568778) from within its [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function. For example, in the situation where a provider module is a subcomponent of a complex driver, the deregistration of the provider module might occur when the provider module subcomponent is deactivated. However, in such a situation the driver must still ensure that the provider module has been completely deregistered from the NMR before returning from its **Unload** function.

 

 





