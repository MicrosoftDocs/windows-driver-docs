---
title: Initializing and Registering a Provider Module
description: Initializing and Registering a Provider Module
ms.assetid: 967271ce-e4f5-45ce-9249-746d2fe698c1
keywords:
- provider modules WDK Network Module Registrar , initializing
- provider modules WDK Network Module Registrar , registering
- registering provider modules
- initializing provider modules
- NmrRegisterProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing and Registering a Provider Module


A provider module must initialize a number of data structures before it can register itself with the Network Module Registrar (NMR). These structures include an [**NPI\_MODULEID**](https://msdn.microsoft.com/library/windows/hardware/ff568813) structure, an [**NPI\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff568814) structure, an [**NPI\_REGISTRATION\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff568815) structure (contained within the NPI\_PROVIDER\_CHARACTERISTICS structure), and a structure defined by the provider module that is used for the provider module's registration context.

If a provider module registers itself with the NMR as a provider of a [Network Programming Interface (NPI)](network-programming-interface.md) that defines NPI-specific provider characteristics, the provider module must also initialize an instance of the provider characteristics structure that are defined by the NPI.

All of these data structures must remain valid and resident in memory as long as the provider module is registered with the NMR.

For example, suppose the "EXNPI" NPI defines the following in header file Exnpi.h:

```C++
// EXNPI NPI identifier
const NPIID EXNPI_NPIID = { ... };

// EXNPI provider characteristics structure
typedef struct EXNPI_PROVIDER_CHARACTERISTICS_
{
  .
  . // NPI-specific members
  .
} EXNPI_PROVIDER_CHARACTERISTICS, *PEXNPI_PROVIDER_CHARACTERISTICS;
```

The following shows how a provider module that registers itself as a provider of the EXNPI NPI can initialize all of these data structures:

```C++
// Include the NPI specific header file
#include "exnpi.h"

// Structure for the provider module's NPI-specific characteristics
const EXNPI_PROVIDER_CHARACTERISTICS NpiSpecificCharacteristics =
{
  .
  . // The NPI-specific characteristics of the provider module
  .
};

// Structure for the provider module's identification
const NPI_MODULEID ProviderModuleId =
{
  sizeof(NPI_MODULEID),
  MIT_GUID,
  { ... }  // A GUID that uniquely identifies the provider module
};

// Prototypes for the provider module's callback functions
NTSTATUS
  ProviderAttachClient(
    IN HANDLE NmrBindingHandle,
    IN PVOID ProviderContext,
    IN PNPI_REGISTRATION_INSTANCE ClientRegistrationInstance,
    IN PVOID ClientBindingContext,
    IN CONST VOID *ClientDispatch,
    OUT PVOID *ProviderBindingContext,
    OUT PVOID *ProviderDispatch
    );

NTSTATUS
  ProviderDetachClient(
    IN PVOID ProviderBindingContext
    );

VOID
  ProviderCleanupBindingContext(
    IN PVOID ProviderBindingContext
    );

// Structure for the provider module's characteristics
const NPI_PROVIDER_CHARACTERISTICS ProviderCharacteristics =
{
  0,
  sizeof(NPI_PROVIDER_CHARACTERISTICS),
  ProviderAttachClient,
  ProviderDetachClient,
  ProviderCleanupBindingContext,
  {
    0,
    sizeof(NPI_REGISTRATION_INSTANCE),
    &EXNPI_NPIID,
    &ProviderModuleId,
    0,
    &NpiSpecificCharacteristics
  }
};

// Context structure for the provider module's registration
typedef struct PROVIDER_REGISTRATION_CONTEXT_ {
  .
  . // Provider-specific members
  .
} PROVIDER_REGISTRATION_CONTEXT, *PPROVIDER_REGISTRATION_CONTEXT;

// Structure for the provider's registration context
PROVIDER_REGISTRATION_CONTEXT ProviderRegistrationContext =
{
  .
  . // Initial values for the registration context
  .
};
```

A provider module typically initializes itself within its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function. The main initialization tasks for a provider module are:

-   Specify an [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function. The operating system calls this function when the provider module is unloaded from the system. If a provider module does not provide an unload function, the provider module cannot be unloaded from the system.

-   Call the [**NmrRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568784) function to register the provider module with the NMR.

For example:

```C++
// Prototype for the provider module's unload function
VOID
  Unload(
    PDRIVER_OBJECT DriverObject
   );

// Variable to contain the handle for the registration
HANDLE ProviderHandle;

// DriverEntry function
NTSTATUS
  DriverEntry(
    PDRIVER_OBJECT DriverObject,
    PUNICODE_STRING RegistryPath
    )
{
  NTSTATUS Status;

  // Specify the unload function
  DriverObject->DriverUnload = Unload;

  .
  . // Other initialization tasks
  .

  // Register the provider module with the NMR
  Status = NmrRegisterProvider(
    &ProviderCharacteristics,
    &ProviderRegistrationContext,
    &ProviderHandle
    );

  // Return the result of the registration
  return Status;
}
```

If a provider module is a provider of more than one NPI, it must initialize an independent set of data structures and call [**NmrRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568784) for each NPI that it supports. If a network module is both a provider module and a client module (that is, it is a provider of one NPI and a client of another NPI), it must initialize two independent sets of data structures, one for the provider interface and one for the client interface, and call both **NmrRegisterProvider** and [**NmrRegisterClient**](https://msdn.microsoft.com/library/windows/hardware/ff568782).

A provider module is not required to call [**NmrRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568784) from within its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function. For example, in the situation where a provider module is a subcomponent of a complex driver, the registration of the provider module might occur only when the provider module subcomponent is activated.

For more information about implementing a provider module's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function, see [Unloading a Provider Module](unloading-a-provider-module.md).

 

 





