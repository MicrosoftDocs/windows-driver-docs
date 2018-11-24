---
title: Attaching the WSK Client to the WSK Subsystem
description: Attaching the WSK Client to the WSK Subsystem
ms.assetid: 752d204f-3022-48b0-9237-707b753a7ad3
keywords:
- Network Module Registrar WDK Winsock Kernel
- NMR WDK Winsock Kernel
- unloading WSK clients
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching the WSK Client to the WSK Subsystem


After a Winsock Kernel (WSK) application has registered with the [Network Module Registrar (NMR)](network-module-registrar2.md) as a client of the WSK NPI, the NMR immediately calls the application's [*ClientAttachProvider*](https://msdn.microsoft.com/library/windows/hardware/ff544903) callback function if the WSK subsystem is loaded and has registered itself with the NMR. If the WSK subsystem is not registered with the NMR, the NMR does not call the application's *ClientAttachProvider* callback function until the WSK subsystem registers with the NMR.

The WSK application should make the following sequence of calls to complete the attachment procedure.

1.  When the NMR calls the WSK application's *ClientAttachProvider* callback function, it passes a pointer to the [**NPI\_REGISTRATION\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff568815) structure associated with the WSK subsystem. The WSK application's *ClientAttachProvider* callback function can use the data passed to it by the NMR to determine if it can attach to the WSK subsystem. Typically, a WSK application only needs the version information contained within a [**WSK\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff571172) structure that is pointed to by the **NpiSpecificCharacteristics** member of the WSK subsystem's NPI\_REGISTRATION\_INSTANCE structure.

2.  If the WSK application determines that it can attach to the WSK subsystem, the WSK application's *ClientAttachProvider* callback function allocates and initializes a binding context structure for the attachment to the WSK subsystem. The application then calls the [**NmrClientAttachProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568770) function to continue the attachment process.

    If **NmrClientAttachProvider** returns STATUS\_SUCCESS, the WSK application has successfully attached to the WSK subsystem. In this situation, the WSK application's *ClientAttachProvider* callback function must save the binding handle that the NMR passed in the *NmrBindingHandle* parameter when the NMR called the application's *ClientAttachProvider* callback function. The WSK application's *ClientAttachProvider* callback function must also save the pointers to the client object ( [**WSK\_CLIENT**](https://msdn.microsoft.com/library/windows/hardware/ff571155)) and the provider dispatch table ( [**WSK\_PROVIDER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571175)) that are returned in the variables that the application passed to the **NmrClientAttachProvider** function in the *ProviderBindingContext* and *ProviderDispatch* parameters. A WSK application typically saves this data in its binding context for the attachment to the WSK subsystem. After the WSK application has successfully attached to the WSK subsystem, the WSK application's *ClientAttachProvider* callback function must return STATUS\_SUCCESS.

3.  If **NmrClientAttachProvider** returns STATUS\_NOINTERFACE, the WSK application can make another attempt to attach to the WSK subsystem by calling the **NmrClientAttachProvider** function again, passing a *ClientDispatch* pointer to a different [**WSK\_CLIENT\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff571159) structure that specifies an alternate version of the WSK NPI that is supported by the application.

4.  If a call to the **NmrClientAttachProvider** function does not return STATUS\_SUCCESS, and the WSK application does not make any further attempts to attach to the WSK subsystem, the WSK application's *ClientAttachProvider* callback function should clean up and deallocate any resources that it allocated before it called **NmrClientAttachProvider**. In this situation, the WSK application's *ClientAttachProvider* callback function must return the status code that was returned by the last call to the **NmrClientAttachProvider** function.

5.  If the WSK application determines that it cannot attach to the provider module, the application's *ClientAttachProvider* callback function must return STATUS\_NOINTERFACE.

The following code example shows how a WSK application can attach itself to the WSK subsystem.

```C++
// Context structure type for the WSK application's
// binding to the WSK subsystem
typedef struct WSK_APP_BINDING_CONTEXT_ {
  HANDLE NmrBindingHandle;
  PWSK_CLIENT WskClient;
  PWSK_PROVIDER_DISPATCH WskProviderDispatch;
  .
  . // Other application-specific members
  .
} WSK_APP_BINDING_CONTEXT, *PWSK_APP_BINDING_CONTEXT;

// Pool tag used for allocating the binding context
#define BINDING_CONTEXT_POOL_TAG 'tpcb'

// The WSK application uses version 1.0 of WSK
#define WSK_APP_WSK_VERSION MAKE_WSK_VERSION(1,0)

// Structure for the WSK application's dispatch table
const WSK_CLIENT_DISPATCH WskAppDispatch = {
  WSK_APP_WSK_VERSION,
  0,
  NULL  // No WskClientEvent callback
};

// ClientAttachProvider NMR API callback function
NTSTATUS
  ClientAttachProvider(
    IN HANDLE NmrBindingHandle,
    IN PVOID ClientContext,
    IN PNPI_REGISTRATION_INSTANCE ProviderRegistrationInstance
    )
{
  PNPI_MODULEID WskProviderModuleId;
  PWSK_PROVIDER_CHARACTERISTICS WskProviderCharacteristics;
  PWSK_APP_BINDING_CONTEXT BindingContext;
  PWSK_CLIENT WskClient;
  PWSK_PROVIDER_DISPATCH WskProviderDispatch;
  NTSTATUS Status;

  // Get pointers to the WSK subsystem's identification and
  // characteristics structures
  WskProviderModuleId = ProviderRegistrationInstance->ModuleId;
  WskProviderCharacteristics =
    (PWSK_PROVIDER_CHARACTERISTICS)
      ProviderRegistrationInstance->NpiSpecificCharacteristics;

  //
  // The WSK application can use the data in the structures pointed
  // to by ProviderRegistrationInstance, WskProviderModuleId, and
  // WskProviderCharacteristics to determine if the WSK application
  // can attach to the WSK subsystem.
  //
  // In this example, the WSK application does not perform any
  // checks to determine if it can attach to the WSK subsystem.
  //

  // Allocate memory for the WSK application's binding
  // context structure
  BindingContext =
    (PWSK_APP_BINDING_CONTEXT)
      ExAllocatePoolWithTag(
        NonPagedPool,
        sizeof(WSK_APP_BINDING_CONTEXT),
        BINDING_CONTEXT_POOL_TAG
        );

  // Check result of allocation
  if (BindingContext == NULL)
  {
    // Return error status code
    return STATUS_INSUFFICIENT_RESOURCES;
  }

  // Initialize the binding context structure
  ...
 
  // Continue with the attachment to the WSK subsystem
  Status = NmrClientAttachProvider(
    NmrBindingHandle,
    BindingContext,
    &WskAppDispatch,
    &WskClient,
    &WskProviderDispatch
    );

  // Check result of attachment
  if (Status == STATUS_SUCCESS)
  {
    // Save NmrBindingHandle, WskClient, and
    // WskProviderDispatch for future reference
    BindingContext->NmrBindingHandle = NmrBindingHandle;
    BindingContext->WskClient = WskClient;
    BindingContext->WskProviderDispatch = WskProviderDispatch;
  }

  // Attachment did not succeed
  else
  {
    // Free memory for application's binding context structure
    ExFreePoolWithTag(
      BindingContext,
      BINDING_CONTEXT_POOL_TAG
      );
  }

  // Return result of attachment
  return Status;
}
```

 

 





