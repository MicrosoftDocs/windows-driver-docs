---
title: Detaching a Provider Module from a Client Module
description: Detaching a Provider Module from a Client Module
keywords:
- provider modules WDK Network Module Registrar , detaching
- network modules WDK Network Module Registrar , detachment
- deregistering network modules
- Network Module Registrar WDK , detaching network modules
- NMR WDK , detaching network modules
- NmrDeregisterProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Detaching a Provider Module from a Client Module


When a provider module deregisters with the Network Module Registrar (NMR) by calling the [**NmrDeregisterProvider**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrderegisterprovider) function, the NMR calls the provider module's [*ProviderDetachClient*](/windows-hardware/drivers/ddi/netioddk/nc-netioddk-npi_provider_detach_client_fn) callback function, once for each client module to which it is attached, so that the provider module can detach itself from all of the client modules as part of the provider module's deregistration process.

Furthermore, whenever a client module to which the provider module is attached deregisters with the NMR by calling the [**NmrDeregisterClient**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrderegisterclient) function, the NMR also calls the provider module's [*ProviderDetachClient*](/windows-hardware/drivers/ddi/netioddk/nc-netioddk-npi_provider_detach_client_fn) callback function so that the provider module can detach itself from the client module as part of the client module's deregistration process.

After its [*ProviderDetachClient*](/windows-hardware/drivers/ddi/netioddk/nc-netioddk-npi_provider_detach_client_fn) callback function has been called, a provider module must not make any further calls to any of the client module's [Network Programming Interface (NPI)](network-programming-interface.md) callback functions. If there are no in-progress calls to any of the client module's NPI callback functions when the provider module's *ProviderDetachClient* callback function is called, then the *ProviderDetachClient* callback function should return STATUS\_SUCCESS.

If there are in-progress calls to one or more of the client module's NPI callback functions when the provider module's [*ProviderDetachClient*](/windows-hardware/drivers/ddi/netioddk/nc-netioddk-npi_provider_detach_client_fn) callback function is called, then the *ProviderDetachClient* callback function should return STATUS\_PENDING. In this case, the provider module must call the [**NmrProviderDetachClientComplete**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrproviderdetachclientcomplete) function after all in-progress calls to the client module's NPI callback functions have completed. The call to **NmrProviderDetachClientComplete** notifies the NMR that detachment of the provider module from the client module is complete.

For more information about how to track the number of in-progress calls to a client module's NPI callback functions, see [Programming Considerations](programming-considerations.md).

If a provider module implements a [*ProviderCleanupBindingContext*](/windows-hardware/drivers/ddi/netioddk/nc-netioddk-npi_provider_cleanup_binding_context_fn) callback function, the NMR calls the provider module's *ProviderCleanupBindingContext* callback function after both the provider module and the client module have completed detachment from each other. A provider module's *ProviderCleanupBindingContext* callback function should perform any necessary cleanup of the data contained within the provider module's binding context structure. It should then free the memory for the binding context structure if the provider module dynamically allocated the memory for the structure.

For example:

```C++
// ProviderDetachClient callback function
NTSTATUS
  ProviderDetachClient(
    IN PVOID ProviderBindingContext
    )
{
  PPROVIDER_BINDING_CONTEXT BindingContext;

  // Get a pointer to the binding context
  BindingContext = (PPROVIDER_BINDING_CONTEXT)ProviderBindingContext;

  // Set a flag indicating that the provider module is detaching
  // from the client module so that no more calls are made to
  // the client module's NPI callback functions.
  ...

  // Check if there are no in-progress NPI callback function calls
  // to the client module
  if (...)
  {
    // Return success status indicating detachment is complete
    return STATUS_SUCCESS;
  }

  // There are one or more in-progress NPI callback function
  // calls to the client module
  else
  {
    // Return pending status indicating detachment is pending
    // completion of the in-progress NPI callback function calls
    return STATUS_PENDING;

    // When the last in-progress call to the client module's
    // NPI callback functions completes, the provider module
    // must call NmrProviderDetachClientComplete() with the
    // binding handle for the attachment to the client module.
  }
}

// ProviderCleanupBindingContext callback function
VOID
  ProviderCleanupBindingContext(
    IN PVOID ProviderBindingContext
    )
{
  PPROVIDER_BINDING_CONTEXT BindingContext;

  // Get a pointer to the binding context
  BindingContext = (PPROVIDER_BINDING_CONTEXT)ProviderBindingContext;

  // Clean up the provider binding context structure
  ...

  // Free the memory for provider's binding context structure
  ExFreePoolWithTag(
    BindingContext,
    BINDING_CONTEXT_POOL_TAG
    );
}
```

 

