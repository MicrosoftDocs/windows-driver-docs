---
title: Participating in Error Source Control
description: Participating in Error Source Control
ms.assetid: 4b2e3431-348f-48b1-924e-14b9fb5a48f0
keywords:
- Windows Hardware Error Architecture WDK , error source control
- WHEA WDK , error source control
- hardware errors WDK WHEA , error source control
- errors WDK WHEA , error source control
- platform-specific hardware error driver plug-ins WDK WHEA , error source control
- PSHED plug-ins WDK WHEA , error source control
- error source control WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Participating in Error Source Control


To participate in error source control, a PSHED plug-in must implement the following callback functions:

[*SetErrorSourceInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559489)

[*EnableErrorSource*](https://msdn.microsoft.com/library/windows/hardware/ff559304)

[*DisableErrorSource*](https://msdn.microsoft.com/library/windows/hardware/ff559294)

The following code example shows how to implement these callback functions.

```cpp
//
// The PSHED plug-in&#39;s SetErrorSourceInfo callback function
//
NTSTATUS
  SetErrorSourceInfo(
    IN OUT PVOID PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource
    )
{
  // Check if the plug-in supports configuring
  // the specified error source.
  if (...)
  {
    // Save the new configuration data for the error
    // source in nonvolatile storage and apply the
    // configuration changes to the error source such
    // that they will become effective after the
    // system is restarted.
    ...

    // If successful, return success status
    if (...)
    {
      return STATUS_SUCCESS;
    }

    // Failed to configure the error source
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

//
// The PSHED plug-in&#39;s EnableErrorSource callback function
//
NTSTATUS
  EnableErrorSource(
    IN OUT PVOID PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource
    )
{
  // Check if the plug-in supports enabling
  // the specified error source.
  if (...)
  {
    // Enable the error source
    ...

    // If successful
    if (...)
    {
      // Return success status
      return STATUS_SUCCESS;
    }

    // Failed to enable the error source
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

//
// The PSHED plug-in&#39;s DisableErrorSource callback function
//
NTSTATUS
  DisableErrorSource(
    IN OUT PVOID PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource
    )
{
  // Check if the plug-in supports disabling
  // the specified error source.
  if (...)
  {
    // Disable the error source
    ...

    // If successful
    if (...)
    {
      // Return success status
      return STATUS_SUCCESS;
    }

    // Failed to disable the error source
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

A PSHED plug-in that participates in error source control must specify the **PshedFAErrorSourceControl** flag when it [registers](registering-a-pshed-plug-in.md) itself with the operating system.

 

 




