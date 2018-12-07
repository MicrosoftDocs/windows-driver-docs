---
title: Participating in Error Information Retrieval
description: Participating in Error Information Retrieval
ms.assetid: ed0ad20b-d978-4650-b3a0-6b0795323c77
keywords:
- Windows Hardware Error Architecture WDK , error information retrieval
- WHEA WDK , error information retrieval
- hardware errors WDK WHEA , error information retrieval
- errors WDK WHEA , error information retrieval
- platform-specific hardware error driver plug-ins WDK WHEA , error information retrieval
- PSHED plug-ins WDK WHEA , error information retrieval
- error information retrieval WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Participating in Error Information Retrieval


To participate in error information retrieval, a PSHED plug-in must implement the following callback functions:

[*RetrieveErrorInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559483)

[*FinalizeErrorRecord*](https://msdn.microsoft.com/library/windows/hardware/ff559357)

[*ClearErrorStatus*](https://msdn.microsoft.com/library/windows/hardware/ff559275)

The following code example shows how to implement these callback functions.

```cpp
//
// The PSHED plug-in&#39;s RetrieveErrorInfo callback function
//
NTSTATUS
  RetrieveErrorInfo(
    IN OUT PVOID PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource,
    IN ULONGLONG BufferLength,
    IN OUT PWHEA_ERROR_PACKET Packet
    )
{
  // Check if the plug-in supports retrieving error
  // information from the specified error source.
  if (...)
  {
    // Check if there is enough space remaining in the hardware
    // error packet to update it with the platform-specific
    // error information.
    if (...)
    {
      // Retrieve the platform-specific error information from
      // the error source and update the hardware error packet.
      ...

      // If successful, return success status
      if (...)
      {
        return STATUS_SUCCESS;
      }

      // Failed to retrieve the platform-specific error information
      else
      {
        return STATUS_UNSUCCESSFUL;
      }
    }

    // Insufficient space in the hardware error packet.
    else
    {
      return STATUS_BUFFER_TOO_SMALL;
    }
  }

  // Not supported by the plug-in
  else
  {
    return STATUS_NOT_SUPPORTED;
  }
}

//
// The PSHED plug-in&#39;s FinalizeErrorRecord callback function
//
NTSTATUS
  FinalizeErrorRecord(
    IN OUT PVOID PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource,
    IN ULONG BufferLength,
    IN OUT PWHEA_ERROR_RECORD ErrorRecord
    )
{
  // Check if the plug-in supports finalizing the error
  // record for errors from the specified error source.
  if (...)
  {
    // Check if there is enough space remaining in the
    // error record to update it with the supplementary
    // platform-specific error record sections.
    if (...)
    {
      // Update the error record with the supplementary
      // platform-specific error record sections.
      ...

      // If successful, return success status
      if (...)
      {
        return STATUS_SUCCESS;
      }

      // Failed to update the error record
      else
      {
        return STATUS_UNSUCCESSFUL;
      }
    }

    // Insufficient space in the error record.
    else
    {
      return STATUS_BUFFER_TOO_SMALL;
    }
  }

  // Not supported by the plug-in
  else
  {
    return STATUS_NOT_SUPPORTED;
  }
}

//
// The PSHED plug-in&#39;s ClearErrorStatus callback function
//
NTSTATUS
  ClearErrorStatus(
    IN OUT PVOID PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource,
    IN ULONG BufferLength,
    IN PWHEA_ERROR_RECORD ErrorRecord
    )
{
  // Check if the plug-in supports clearing the error
  // status for errors from the specified error source.
  if (...)
  {
    // Clear the error status for the error source
    ...

    // If successful, return success status
    if (...)
    {
      return STATUS_SUCCESS;
    }

    // Failed to clear the error status
    else
    {
      return STATUS_UNSUCCESSFUL;
    }
  }

  // Not supported by the plug-in
  else
  {
    return STATUS_NOT_SUPPORTED;
  }
}
```

A PSHED plug-in that participates in error information retrieval must specify the **PshedFAErrorInfoRetrieval** flag when it [registers](registering-a-pshed-plug-in.md) itself with the operating system.

 

 




