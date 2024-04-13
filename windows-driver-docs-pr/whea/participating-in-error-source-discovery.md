---
title: Participating in Error Source Discovery
description: Participating in Error Source Discovery
keywords:
- Windows Hardware Error Architecture WDK , error source discovery
- WHEA WDK , error source discovery
- hardware errors WDK WHEA , error source discovery
- errors WDK WHEA , error source discovery
- platform-specific hardware error driver plug-ins WDK WHEA , error source discovery
- PSHED plug-ins WDK WHEA , error source discovery
- error source discovery WDK WHEA
ms.date: 03/03/2023
---

# Participating in Error Source Discovery


To participate in error source discovery, a PSHED plug-in must implement a [*GetAllErrorSources*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-pshed_pi_get_all_error_sources) callback function. A PSHED plug-in that participates in error source discovery can also implement an optional [*GetErrorSourceInfo*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-pshed_pi_get_error_source_info) callback function.

The following code example shows how to implement these callback functions.

```cpp
//
// The PSHED plug-in's GetAllErrorSources callback function
//
NTSTATUS
  GetAllErrorSources(
    IN OUT PVOID PluginContext,
    IN OUT PULONG Count,
    IN OUT PWHEA_ERROR_SOURCE_DESCRIPTOR *ErrorSources,
    IN OUT PULONG Length
    )
{
  // Check if there is enough space remaining in the buffer
  // that contains the array of error source descriptors to 
  // include any additional error sources to be reported by
  // the PSHED plug-in.
  if (...)
  {
    // Update the list of error sources by modifying the
    // existing error sources in the list and adding any
    // additional error sources to the list.
    ...

    // If the number of error sources in the list has changed
    // update the count that is returned back to the kernel.
    *Count = ...;

    // If successful, return success status
    if (...)
    {
      return STATUS_SUCCESS;
    }

    // Failed to update the list of error sources
    else
    {
      return STATUS_UNSUCCESSFUL;
    }
  }

  // Insufficient space in the buffer.
  else
  {
    // Set the length the necessary buffer size
    *Length = ...;

    return STATUS_BUFFER_TOO_SMALL;
  }
}

//
// The PSHED plug-in's GetErrorSourceInfo callback function
//
NTSTATUS
  GetErrorSourceInfo(
    IN OUT PVOID PluginContext,
    IN OUT PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource
    )
{
  // Modify the information contained in the
  // error source descriptor as appropriate.
  ...

  // If successful, return success status
  if (...)
  {
    return STATUS_SUCCESS;
  }

  // Failed to update the error source information
  else
  {
    return STATUS_UNSUCCESSFUL;
  }
}
```

A PSHED plug-in that participates in error source discovery must specify the **PshedFADiscovery** flag when it [registers](registering-a-pshed-plug-in.md) itself with the operating system.

 

