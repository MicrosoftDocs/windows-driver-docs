---
title: Detaching a Client Module from a Provider Module
description: Detaching a Client Module from a Provider Module
ms.assetid: 148c1a90-0fef-4b22-bf7e-f35285f1bc55
keywords:
- client modules WDK Network Module Registrar , detaching
- NmrDeregisterClient
- network modules WDK Network Module Registrar , detachment
- deregistering network modules
- Network Module Registrar WDK , detaching network modules
- NMR WDK , detaching network modules
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Detaching a Client Module from a Provider Module


When a client module deregisters with the Network Module Registrar (NMR) by calling the [**NmrDeregisterClient**](https://msdn.microsoft.com/library/windows/hardware/ff568774) function, the NMR calls the client module's [*ClientDetachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544908) callback function, once for each provider module to which it is attached, so that the client module can detach itself from all of the provider modules as part of the client module's deregistration process.

Furthermore, whenever a provider module to which the client module is attached deregisters with the NMR by calling the [**NmrDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568778) function, the NMR also calls the client module's [*ClientDetachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544908) callback function so that the client module can detach itself from the provider module as part of the provider module's deregistration process.

After its [*ClientDetachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544908) callback function has been called, a client module must not make any further calls to any of the provider module's [Network Programming Interface (NPI)](network-programming-interface.md) functions. If there are no in-progress calls to any of the provider module's NPI functions when the client module's *ClientDetachProvider* callback function is called, then the *ClientDetachProvider* callback function should return STATUS\_SUCCESS.

If there are in-progress calls to one or more of the provider module's NPI functions when the client module's [*ClientDetachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544908) callback function is called, then the *ClientDetachProvider* callback function should return STATUS\_PENDING. In this case, the client module must call the [**NmrClientDetachProviderComplete**](https://msdn.microsoft.com/library/windows/hardware/ff568772) function after all in-progress calls to the provider module's NPI functions have completed. The call to **NmrClientDetachProviderComplete** notifies the NMR that detachment of the client module from the provider module is complete.

For more information about how to track the number of in-progress calls to a provider module's NPI functions, see [Programming Considerations](programming-considerations.md).

If a client module implements a [*ClientCleanupBindingContext*](https://msdn.microsoft.com/library/windows/hardware/ff544904) callback function, the NMR calls the client module's *ClientCleanupBindingContext* callback function after both the client module and the provider module have completed detachment from each other. A client module's *ClientCleanupBindingContext* callback function should perform any necessary cleanup of the data contained within the client module's binding context structure. It should then free the memory for the binding context structure if the client module dynamically allocated the memory for the structure.

For example:

```C++
// ClientDetachProvider callback function
NTSTATUS
  ClientDetachProvider(
    IN PVOID ClientBindingContext
    )
{
  PCLIENT_BINDING_CONTEXT BindingContext;

  // Get a pointer to the binding context
  BindingContext = (PCLIENT_BINDING_CONTEXT)ClientBindingContext;

  // Set a flag indicating that the client module is detaching
  // from the provider module so that no more calls are made to
  // the provider module&#39;s NPI functions.
  ...

  // Check if there are no in-progress NPI function calls to the
  // provider module
  if (...)
  {
    // Return success status indicating detachment is complete
    return STATUS_SUCCESS;
  }

  // There are one or more in-progress NPI function calls
  // to the provider module
  else
  {
    // Return pending status indicating detachment is pending
    // completion of the in-progress NPI function calls
    return STATUS_PENDING;

    // When the last in-progress call to the provider module&#39;s
    // NPI functions completes, the client module must call
    // NmrClientDetachProviderComplete() with the binding handle
    // for the attachment to the provider module.
  }
}

// ClientCleanupBindingContext callback function
VOID
  ClientCleanupBindingContext(
    IN PVOID ClientBindingContext
    )
{
  PCLIENT_BINDING_CONTEXT BindingContext;

  // Get a pointer to the binding context
  BindingContext = (PCLIENT_BINDING_CONTEXT)ClientBindingContext;

  // Clean up the client binding context structure
  ...

  // Free the memory for client&#39;s binding context structure
  ExFreePoolWithTag(
    BindingContext,
    BINDING_CONTEXT_POOL_TAG
    );
}
```

 

 





