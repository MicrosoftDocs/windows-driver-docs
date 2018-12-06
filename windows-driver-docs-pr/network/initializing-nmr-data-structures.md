---
title: Initializing NMR Data Structures
description: Initializing NMR Data Structures
ms.assetid: 84241ff4-f6ae-4c71-a9e3-1a6615e41293
keywords:
- Network Module Registrar WDK Winsock Kernel
- NMR WDK Winsock Kernel
- initializing NMR data structures
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing NMR Data Structures


Before a Winsock Kernel (WSK) application can register with the [Network Module Registrar (NMR)](network-module-registrar2.md), the application must first initialize the following structures.

-   [**NPI\_MODULEID**](https://msdn.microsoft.com/library/windows/hardware/ff568813)

-   [**NPI\_CLIENT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff568812)

-   [**NPI\_REGISTRATION\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff568815) contained within the [**NPI\_CLIENT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff568812) structure

All of these data structures must remain valid and resident in memory as long as the WSK application is registered with the NMR.

The following code example shows how a WSK application can initialize all of the data structures listed previously.

```C++
// Include the WSK header file
#include "wsk.h"

// Structure for the WSK application&#39;s network module identification
const NPI_MODULEID ModuleId =
{
  sizeof(NPI_MODULEID),
  MIT_GUID,
  { ... }  // A GUID that uniquely identifies the WSK application
};

// Prototypes for the WSK application&#39;s NMR API callback functions
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

// Structure for the WSK application&#39;s characteristics
const NPI_CLIENT_CHARACTERISTICS Characteristics =
{
  0,
  sizeof(NPI_CLIENT_CHARACTERISTICS),
  ClientAttachProvider,
  ClientDetachProvider,
  ClientCleanupBindingContext,
  {
    0,
    sizeof(NPI_REGISTRATION_INSTANCE),
    &NPI_WSK_INTERFACE_ID,
    &ModuleId,
    0,
    NULL
  }
};
```

A WSK application calls the [**NmrRegisterClient**](https://msdn.microsoft.com/library/windows/hardware/ff568782) function to register the application with the NMR.

For example:

```C++
// Variable to contain the handle for the registration with the NMR
HANDLE RegistrationHandle;

// DriverEntry function
NTSTATUS
  DriverEntry(
    PDRIVER_OBJECT DriverObject,
    PUNICODE_STRING RegistryPath
    )
{
  NTSTATUS Status;

  .
  .
  .

  // Register the WSK application with the NMR
  Status = NmrRegisterClient(
    &Characteristics,
    NULL,
    &RegistrationHandle
    );

  if(!NT_SUCCESS(Status)) {
      .
      .
      .
      return Status;
  }

  .
  .
  .
}
```

A WSK application is not required to call **NmrRegisterClient** from within its **DriverEntry** function. For example, if a WSK application is a subcomponent of a complex driver, the registration of the application might occur only when the WSK application subcomponent is activated.

 

 





