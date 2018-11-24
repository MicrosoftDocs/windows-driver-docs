---
title: Attaching a Provider Module to a Client Module
description: Attaching a Provider Module to a Client Module
ms.assetid: 5c68273e-d343-4d83-8703-957960934136
keywords:
- attaching network modules
- registering network modules
- Network Module Registrar WDK , attaching network modules
- NMR WDK , attaching network modules
- provider modules WDK Network Module Registrar , attaching
- network modules WDK Network Module Registrar , attachment
- NmrClientAttachProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching a Provider Module to a Client Module


A client module calls the [**NmrClientAttachProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568770) function to attach itself to a provider module. For more information about how a client module attaches to a provider module, see [Attaching a Client Module to a Provider Module](attaching-a-client-module-to-a-provider-module.md).

When a client module calls [**NmrClientAttachProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568770), the NMR calls the provider module's [*ProviderAttachClient*](https://msdn.microsoft.com/library/windows/hardware/ff570395) callback function. When the NMR calls a provider module's *ProviderAttachClient* callback function, it passes, in the *ClientRegistrationInstance* parameter, a pointer to the [**NPI\_REGISTRATION\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff568815) structure that is associated with the client module that called **NmrClientAttachProvider**. The provider module's *ProviderAttachClient* callback function can use the data in the client module's **NPI\_REGISTRATION\_INSTANCE** structure, the data in the [**NPI\_MODULEID**](https://msdn.microsoft.com/library/windows/hardware/ff568813) structure and the [Network Programming Interface (NPI)](network-programming-interface.md)-specific client characteristics structure pointed to by the **ModuleId** and **NpiSpecificCharacteristics** members of the client module's **NPI\_REGISTRATION\_INSTANCE** structure, to determine if it will attach to the client module.

If the provider module determines that it will attach to the client module, then the provider module's [*ProviderAttachClient*](https://msdn.microsoft.com/library/windows/hardware/ff570395) callback function must do the following:

-   Allocate and initialize a binding context structure for the attachment to the client module.

-   Save the binding handle passed in the *NmrBindingHandle* parameter.

-   Save the pointers passed in the *ClientBindingContext* and *ClientDispatch* parameters so that the provider module can make calls to the client module's NPI callback functions.

-   Set the variable pointed to by the *ProviderBindingContext* parameter to point to the provider module's binding context structure.

-   Set the variable pointed to by the *ProviderDispatch* parameter to point to a structure that contains the provider module's dispatch table of NPI functions.

-   Return STATUS\_SUCCESS.

A provider module typically saves the binding handle, the pointer to the client binding context, and the pointer to the client dispatch structure in its binding context for the attachment to the client module.

If a provider module's [*ProviderAttachClient*](https://msdn.microsoft.com/library/windows/hardware/ff570395) callback function returns STATUS\_SUCCESS, the client module and the provider module have successfully attached to each other.

If the provider module determines that it will not attach to the client module, then the provider module's [*ProviderAttachClient*](https://msdn.microsoft.com/library/windows/hardware/ff570395) callback function must return STATUS\_NOINTERFACE.

For example, suppose the "EXNPI" Network Programming Interface (NPI) defines the following in header file Exnpi.h:

```C++
// EXNPI client characteristics structure
typedef struct EXNPI_CLIENT_CHARACTERISTICS_
{
  .
  . // NPI-specific members
  .
} EXNPI_CLIENT_CHARACTERISTICS, *PEXNPI_CLIENT_CHARACTERISTICS;

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

The following code example shows how a provider module that is registered as a provider of the EXNPI NPI can attach itself to a client module that is registered as a client of the EXNPI NPI:

```C++
// Context structure for the provider
// module&#39;s binding to a client module
typedef struct PROVIDER_BINDING_CONTEXT_ {
  HANDLE NmrBindingHandle;
  PVOID ClientBindingContext;
  PEXNPI_CLIENT_DISPATCH ClientDispatch;
  .
  . // Other provider-specific members
  .
} PROVIDER_BINDING_CONTEXT, *PPROVIDER_BINDING_CONTEXT;

// Pool tag used for allocating the binding context
#define BINDING_CONTEXT_POOL_TAG &#39;tpcb&#39;

// Structure for the provider&#39;s dispatch table
const EXNPI_PROVIDER_DISPATCH Dispatch = {
  .
  . // Function pointers to the provider
  . // module&#39;s NPI functions
  .
};

// ProviderAttachClient callback function
NTSTATUS
  ProviderAttachClient(
    IN HANDLE NmrBindingHandle,
    IN PVOID ProviderContext,
    IN PNPI_REGISTRATION_INSTANCE ClientRegistrationInstance,
    IN PVOID ClientBindingContext,
    IN CONST VOID *ClientDispatch,
    OUT PVOID *ProviderBindingContext,
    OUT PVOID *ProviderDispatch
    )
{
  PNPI_MODULEID ClientModuleId;
  PEXNPI_CLIENT_CHARACTERISTICS ClientNpiSpecificCharacteristics;
  PPROVIDER_BINDING_CONTEXT BindingContext;
  PVOID ClientBindingContext;
  PEXNPI_CLIENT_DISPATCH ClientDispatch;

  // Check parameters
  if ((ProviderBindingContext == NULL) ||
      (ProviderDispatch == NULL))
  {
    // Return error status code
    return STATUS_INVALID_PARAMETER;
  }

  // Get pointers to the client module&#39;s identification structure
  // and the client module&#39;s NPI-specific characteristics structure
  ClientModuleId = ClientRegistrationInstance->ModuleId;
  ClientNpiSpecificCharacteristics =
    (PEXNPI_CLIENT_CHARACTERISTICS)
      ProviderRegistrationInstance->NpiSpecificCharacteristics;

  //
  // Use the data in the structures pointed to by
  // ClientRegistrationInstance, ClientModuleId,
  // and ClientNpiSpecificCharacteristics to determine
  // whether to attach to the client module.
  //

  // If the provider module determines that it will not attach
  // to the client module
  if (...)
  {
    // Return status code indicating the modules did not
    // attach to each other
    return STATUS_NOINTERFACE;
  }

  // Allocate memory for the provider module&#39;s
  // binding context structure
  BindingContext =
    (PPROVIDER_BINDING_CONTEXT)
      ExAllocatePoolWithTag(
        NonPagedPool,
        sizeof(PROVIDER_BINDING_CONTEXT),
        BINDING_CONTEXT_POOL_TAG
        );

  // Check result of allocation
  if (BindingContext == NULL)
  {
    // Return error status code
    return STATUS_INSUFFICIENT_RESOURCES;
  }

  // Initialize the provider binding context structure
  ...

  // Save NmrBindingHandle, ClientBindingContext,
  // and ClientDispatch for future reference
  BindingContext->NmrBindingHandle =
    NmrBindingHandle;
  BindingContext->ClientBindingContext =
    ClientBindingContext;
  BindingContext->ClientDispatch =
    ClientDispatch;

  // Return a pointer to the provider binding context structure
  // in the ProviderBindingContext parameter
  *ProviderBindingContext = BindingContext;

  // Return a pointer to the provider dispatch structure
  // in the ProviderDispatch parameter
  *ProviderDispatch = &Dispatch;

  // Return success status
  return STATUS_SUCCESS;
}
```

 

 





