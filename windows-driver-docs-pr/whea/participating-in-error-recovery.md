---
title: Participating in Error Recovery
description: Participating in Error Recovery
keywords:
- Windows Hardware Error Architecture WDK , error recovery
- WHEA WDK , error recovery
- hardware errors WDK WHEA , error recovery
- errors WDK WHEA , error recovery
- platform-specific hardware error driver plug-ins WDK WHEA , error recovery
- PSHED plug-ins WDK WHEA , error recovery
- error recovery WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Participating in Error Recovery


To participate in error recovery, a PSHED plug-in must implement an [*AttemptRecovery*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-pshed_pi_attempt_error_recovery) callback function.

The following code example shows how to implement this callback function.

```cpp
//
// The PSHED plug-in's AttemptRecovery callback function
//
NTSTATUS
  AttemptRecovery(
    IN OUT PVOID PluginContext,
    IN ULONG BufferLength,
    IN PWHEA_ERROR_RECORD ErrorRecord
    )
{
  // Check if the error condition was not corrected by the
  // operating system or by the PSHED.
  if (ErrorRecord->Header.Severity != WheaErrSevCorrected)
  {
    // Attempt to correct the error condition.
    ...

    // If not successful, return failure status
    if (...)
    {
      return STATUS_UNSUCCESSFUL;
    }
  }

  // Perform any additional operations that are required
  // to fully recover from the error condition.
  ...

  // If successful, return success status
  if (...)
  {
    return STATUS_SUCCESS;
  }

  // Failed to fully recover from the error condition
  else
  {
    return STATUS_UNSUCCESSFUL;
  }
}
```

A PSHED plug-in that participates in error recovery must specify the **PshedFAErrorRecovery** flag when it [registers](registering-a-pshed-plug-in.md) itself with the operating system.

 

