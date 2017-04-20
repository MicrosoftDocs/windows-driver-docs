---
title: Participating in Error Source Discovery
author: windows-driver-content
description: Participating in Error Source Discovery
ms.assetid: 349c8f06-be79-4a40-8b9f-cbefc563f6de
keywords:
- Windows Hardware Error Architecture WDK , error source discovery
- WHEA WDK , error source discovery
- hardware errors WDK WHEA , error source discovery
- errors WDK WHEA , error source discovery
- platform-specific hardware error driver plug-ins WDK WHEA , error source discovery
- PSHED plug-ins WDK WHEA , error source discovery
- error source discovery WDK WHEA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Participating in Error Source Discovery


To participate in error source discovery, a PSHED plug-in must implement a [*GetAllErrorSources*](https://msdn.microsoft.com/library/windows/hardware/ff559366) callback function. A PSHED plug-in that participates in error source discovery can also implement an optional [*GetErrorSourceInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559368) callback function.

The following code example shows how to implement these callback functions.

```
//
// The PSHED plug-in&#39;s GetAllErrorSources callback function
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
// The PSHED plug-in&#39;s GetErrorSourceInfo callback function
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Participating%20in%20Error%20Source%20Discovery%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


