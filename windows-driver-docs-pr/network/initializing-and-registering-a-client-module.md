---
title: Initializing and Registering a Client Module
description: Initializing and Registering a Client Module
keywords:
- client modules WDK Network Module Registrar , initializing
- client modules WDK Network Module Registrar , registering
- registering client modules
- initializing client modules
- NmrRegisterClient
ms.date: 04/20/2017
---

# Initializing and Registering a Client Module


A client module must initialize a number of data structures before it can register itself with the Network Module Registrar (NMR). These structures include an [**NPI\_MODULEID**](/previous-versions/windows/hardware/drivers/ff568813(v=vs.85)) structure, an [**NPI\_CLIENT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/netioddk/ns-netioddk-_npi_client_characteristics) structure, an [**NPI\_REGISTRATION\_INSTANCE**](/windows-hardware/drivers/ddi/netioddk/ns-netioddk-_npi_registration_instance) structure (contained within the NPI\_CLIENT\_CHARACTERISTICS structure), and a structure defined by the client module that is used for the client module's registration context.

If a client module registers itself with the NMR as a client of a [Network Programming Interface (NPI)](network-programming-interface.md) that defines NPI-specific client characteristics, the client module must also initialize an instance of the client characteristics structure defined by the NPI.

All of these data structures must remain valid and resident in memory as long as the client module is registered with the NMR.

For example, suppose the "EXNPI" NPI defines the following in header file Exnpi.h:

```C++
// EXNPI NPI identifier
const NPIID EXNPI_NPIID = { ... };

// EXNPI client characteristics structure
typedef struct EXNPI_CLIENT_CHARACTERISTICS_
{
  .
  . // NPI-specific members
  .
} EXNPI_CLIENT_CHARACTERISTICS, *PEXNPI_CLIENT_CHARACTERISTICS;
```

The following shows how a client module that registers itself as a client of the EXNPI NPI can initialize all of these data structures:

```C++
// Include the NPI specific header file
#include "exnpi.h"

// Structure for the client module's NPI-specific characteristics
const EXNPI_CLIENT_CHARACTERISTICS NpiSpecificCharacteristics =
{
  .
  . // The NPI-specific characteristics of the client module
  .
};

// Structure for the client module's identification
const NPI_MODULEID ClientModuleId =
{
  sizeof(NPI_MODULEID),
  MIT_GUID,
  { ... }  // A GUID that uniquely identifies the client module
};

// Prototypes for the client module's callback functions
NTSTATUS
  ClientAttachProvider(
    IN HANDLE NmrBindingHandle,
    IN PVOID ClientContext,
    IN PNPI_REGISTRATION_INSTANCE ProviderRegistrationInstance
    );

NTSTATUS
  ClientDetachProvider(
    IN PVOID ClientBindingContext
    );

VOID
  ClientCleanupBindingContext(
    IN PVOID ClientBindingContext
    );

// Structure for the client module's characteristics
const NPI_CLIENT_CHARACTERISTICS ClientCharacteristics =
{
  0,
  sizeof(NPI_CLIENT_CHARACTERISTICS),
  ClientAttachProvider,
  ClientDetachProvider,
  ClientCleanupBindingContext,
  {
    0,
    sizeof(NPI_REGISTRATION_INSTANCE),
    &EXNPI_NPIID,
    &ClientModuleId,
    0,
    &NpiSpecificCharacteristics
  }
};

// Context structure for the client module's registration
typedef struct CLIENT_REGISTRATION_CONTEXT_ {
  .
  . // Client-specific members
  .
} CLIENT_REGISTRATION_CONTEXT, *PCLIENT_REGISTRATION_CONTEXT;

// Structure for the client's registration context
CLIENT_REGISTRATION_CONTEXT ClientRegistrationContext =
{
  .
  . // Initial values for the registration context
  .
};
```

A client module typically initializes itself within its [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function. The main initialization tasks for a client module are:

-   Specify an [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) function. The operating system calls this function when the client module is unloaded from the system. If a client module does not provide an unload function, the client module cannot be unloaded from the system.

-   Call the [**NmrRegisterClient**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrregisterclient) function to register the client module with the NMR.

For example:

```C++
// Prototype for the client module's unload function
VOID
  Unload(
    PDRIVER_OBJECT DriverObject
    );

// Variable to contain the handle for the registration
HANDLE ClientHandle;

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

  // Register the client module with the NMR
  Status = NmrRegisterClient(
    &ClientCharacteristics,
    &ClientRegistrationContext,
    &ClientHandle
    );

  // Return the result of the registration
  return Status;
}
```

If a client module is a client of more than one NPI, it must initialize an independent set of data structures and call [**NmrRegisterClient**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrregisterclient) for each NPI that it supports. If a network module is both a client module and a provider module (that is, it is a client of one NPI and a provider of another NPI), it must initialize two independent sets of data structures, one for the client interface and one for the provider interface, and call both **NmrRegisterClient** and [**NmrRegisterProvider**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrregisterprovider).

A client module is not required to call [**NmrRegisterClient**](/windows-hardware/drivers/ddi/netioddk/nf-netioddk-nmrregisterclient) from within its [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function. For example, in the situation where a client module is a subcomponent of a complex driver, the registration of the client module might occur only when the client module subcomponent is activated.

For more information about implementing a client module's [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) function, see [Unloading a Client Module](unloading-a-client-module.md).

 

