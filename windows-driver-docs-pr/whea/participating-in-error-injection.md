---
title: Participating in Error Injection
description: Participating in Error Injection
ms.assetid: 0bd9efbd-e98d-457a-a28f-e09dcb5ae24d
keywords:
- Windows Hardware Error Architecture WDK , error injection
- WHEA WDK , error injection
- hardware errors WDK WHEA , error injection
- errors WDK WHEA , error injection
- platform-specific hardware error driver plug-ins WDK WHEA , error injection
- PSHED plug-ins WDK WHEA , error injection
- error injection WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Participating in Error Injection


To participate in error information retrieval, a PSHED plug-in must implement the following callback functions:

[*GetInjectionCapabilities*](https://msdn.microsoft.com/library/windows/hardware/ff559372)

[*InjectError*](https://msdn.microsoft.com/library/windows/hardware/ff559397)

The following code example shows how to implement these callback functions.

```cpp
//
// The PSHED plug-in&#39;s GetInjectionCapabilities callback function
//
NTSTATUS
  GetInjectionCapabilities(
    IN OUT PVOID PluginContext,
    OUT PWHEA_ERROR_INJECTION_CAPABILITIES Capabilities
    )
{
  // Set the members in the structure pointed to by the
  // Capabilities parameter to indicate the error injection
  // capabilities supported by the PSHED plug-in.
  ...

  // Return success status
  return STATUS_SUCCESS;
}

//
// The PSHED plug-in&#39;s InjectError callback function
//
NTSTATUS
  InjectError(
    IN OUT PVOID PluginContext,
    IN ULONG ErrorType,
 IN ULONGLONG Parameter1,
    IN ULONGLONG Parameter2,
    IN ULONGLONG Parameter3,
    IN ULONGLONG Parameter4
    )
{
  // Inject the hardware error specified in the ErrorType
  // parameter into the hardware platform.
  // Parameter1 through Parameter4 contain any additional
  // data that is required to inject the error.
  ...

  // Note: For injected errors that are fatal or otherwise
  // unrecoverable, this callback function might not continue
  // execution past this point before the Windows kernel
  // generates a bug check in response to the error condition.

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
```

A PSHED plug-in that participates in error injection must specify the **PshedFAErrorInjection** flag when it [registers](registering-a-pshed-plug-in.md) itself with the operating system.

 

 




