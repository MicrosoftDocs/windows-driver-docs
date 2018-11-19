---
title: Attaching a Client Module to a Provider Module
description: Attaching a Client Module to a Provider Module
ms.assetid: 351c07f6-186a-4f47-95f8-c94084ff68fb
keywords:
- attaching network modules
- registering network modules
- Network Module Registrar WDK , attaching network modules
- NMR WDK , attaching network modules
- client modules WDK Network Module Registrar , attaching
- network modules WDK Network Module Registrar , attachment
- NmrClientAttachProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching a Client Module to a Provider Module


After a client module has registered with the Network Module Registrar (NMR), the NMR calls the client module's [*ClientAttachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544903) callback function, once for each provider module that is registered as a provider of the same [Network Programming Interface (NPI)](network-programming-interface.md) for which the client module has registered as a client.

The NMR also calls a client module's [*ClientAttachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544903) callback function whenever a new provider module registers as a provider of the same NPI for which the client module has registered as a client.

When the NMR calls the client module's [*ClientAttachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544903) callback function for a particular provider module, it passes, in the *ProviderRegistrationInstance* parameter, a pointer to the [**NPI\_REGISTRATION\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff568815) structure that is associated with the provider module. The client module's *ClientAttachProvider* callback function can use the data in the provider module's **NPI\_REGISTRATION\_INSTANCE** structure, as well as the data in the [**NPI\_MODULEID**](https://msdn.microsoft.com/library/windows/hardware/ff568813) structure and the NPI-specific provider characteristics structure pointed to by the **ModuleId** and **NpiSpecificCharacteristics** members of the provider module's **NPI\_REGISTRATION\_INSTANCE** structure, to determine if it will attach to the provider module.

If the client module determines that it will attach to the provider module, the client module's [*ClientAttachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544903) callback function allocates and initializes a binding context structure for the attachment to the provider module and then calls the [**NmrClientAttachProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568770) function to continue the attachment process. In this situation, the client module's *ClientAttachProvider* callback function must return the status code that is returned by the **NmrClientAttachProvider** function.

If [**NmrClientAttachProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568770) returns STATUS\_SUCCESS, the client module and the provider module have successfully attached to each other. In this situation, the client module's [*ClientAttachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544903) callback function must save the binding handle that the NMR passed in the *NmrBindingHandle* parameter when the NMR called the client module's *ClientAttachProvider* callback function. The client module's *ClientAttachProvider* callback function must also save the pointers to the provider binding context and the provider dispatch table that are returned in the variables that the client module passed to the **NmrClientAttachProvider** function in the *ProviderBindingContext* and *ProviderDispatch* parameters. A client module typically saves this data in its binding context for the attachment to the provider module.

If [**NmrClientAttachProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568770) does not return STATUS\_SUCCESS, the client module's [*ClientAttachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544903) callback function should clean up and free any resources that it allocated before it called **NmrClientAttachProvider**.

If the client module determines that it will not attach to the provider module, then the client module's [*ClientAttachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544903) callback function must return STATUS\_NOINTERFACE.

For example, suppose the "EXNPI" Network Programming Interface (NPI) defines the following in header file Exnpi.h:

```C++
// EXNPI provider characteristics structure
typedef struct EXNPI_PROVIDER_CHARACTERISTICS_
{
  .
  . // NPI-specific members
  .
} EXNPI_PROVIDER_CHARACTERISTICS, *PEXNPI_PROVIDER_CHARACTERISTICS;

// EXNPI client dispatch table
typedef struct EXNPI_CLIENT_DISPATCH_ {
  .
  . // NPI-specific dispatch table of function pointers that
  . // point to a client module&#39;s NPI callback functions.
  .
} EXNPI_CLIENT_DISPATCH, *PEXNPI_CLIENT_DISPATCH;

// EXNPI provider dispatch table
typedef struct EXNPI_PROVIDER_DISPATCH_ {
  .
  . // NPI-specific dispatch table of function pointers that
  . // point to a provider module&#39;s NPI functions.
  .
} EXNPI_PROVIDER_DISPATCH, *PEXNPI_PROVIDER_DISPATCH;
```

The following code example shows how a client module that is registered as a client of the EXNPI NPI can attach itself to a provider module that is registered as a provider of the EXNPI NPI:

```C++
// Context structure for the client
// module&#39;s binding to a provider module
typedef struct CLIENT_BINDING_CONTEXT_ {
  HANDLE NmrBindingHandle;
  PVOID ProviderBindingContext;
  PEXNPI_PROVIDER_DISPATCH ProviderDispatch;
  .
  . // Other client-specific members
  .
} CLIENT_BINDING_CONTEXT, *PCLIENT_BINDING_CONTEXT;

// Pool tag used for allocating the binding context
#define BINDING_CONTEXT_POOL_TAG &#39;tpcb&#39;

// Structure for the client&#39;s dispatch table
const EXNPI_CLIENT_DISPATCH Dispatch = {
  .
  . // Function pointers to the client module&#39;s
  . // NPI callback functions
  .
};

// ClientAttachProvider callback function
NTSTATUS
  ClientAttachProvider(
    IN HANDLE NmrBindingHandle,
    IN PVOID ClientContext,
    IN PNPI_REGISTRATION_INSTANCE ProviderRegistrationInstance
    )
{
  PNPI_MODULEID ProviderModuleId;
  PEXNPI_PROVIDER_CHARACTERISTICS ProviderNpiSpecificCharacteristics;
  PCLIENT_BINDING_CONTEXT BindingContext;
  PVOID ProviderBindingContext;
  PEXNPI_PROVIDER_DISPATCH ProviderDispatch;
  NTSTATUS Status;

  // Get pointers to the provider module&#39;s identification structure
  // and the provider module&#39;s NPI-specific characteristics structure
  ProviderModuleId = ProviderRegistrationInstance->ModuleId;
  ProviderNpiSpecificCharacteristics =
    (PEXNPI_PROVIDER_CHARACTERISTICS)
      ProviderRegistrationInstance->NpiSpecificCharacteristics;

  //
  // Use the data in the structures pointed to by
  // ProviderRegistrationInstance, ProviderModuleId,
  // and ProviderNpiSpecificCharacteristics to determine
  // whether to attach to the provider module.
  //

  // If the client module determines that it will not attach
  // to the provider module
  if (...)
  {
    // Return status code indicating the modules did not
    // attach to each other
    return STATUS_NOINTERFACE;
  }

  // Allocate memory for the client module&#39;s
  // binding context structure
  BindingContext =
    (PCLIENT_BINDING_CONTEXT)
      ExAllocatePoolWithTag(
        NonPagedPool,
        sizeof(CLIENT_BINDING_CONTEXT),
        BINDING_CONTEXT_POOL_TAG
        );

  // Check result of allocation
  if (BindingContext == NULL)
  {
    // Return error status code
    return STATUS_INSUFFICIENT_RESOURCES;
  }

  // Initialize the client binding context structure
  ...
 
  // Continue with the attachment to the provider module
  Status = NmrClientAttachProvider(
    NmrBindingHandle,
    BindingContext,
    &Dispatch,
    &ProviderBindingContext,
    &ProviderDispatch
    );

  // Check result of attachment
  if (Status == STATUS_SUCCESS)
  {
    // Save NmrBindingHandle, ProviderBindingContext,
    // and ProviderDispatch for future reference
    BindingContext->NmrBindingHandle =
      NmrBindingHandle;
    BindingContext->ProviderBindingContext =
      ProviderBindingContext;
    BindingContext->ProviderDispatch =
      ProviderDispatch;
  }

  // Attachment did not succeed
  else
  {
    // Free memory for client&#39;s binding context structure
    ExFreePoolWithTag(
      BindingContext,
      BINDING_CONTEXT_POOL_TAG
      );
  }

  // Return result of attachment
  return Status;
}
```

 

 





