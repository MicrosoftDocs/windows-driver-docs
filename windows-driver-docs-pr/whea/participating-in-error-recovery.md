---
title: Participating in Error Recovery
author: windows-driver-content
description: Participating in Error Recovery
ms.assetid: 79f534b2-a5eb-4249-bfff-2f40c25805a6
keywords: ["Windows Hardware Error Architecture WDK , error recovery", "WHEA WDK , error recovery", "hardware errors WDK WHEA , error recovery", "errors WDK WHEA , error recovery", "platform-specific hardware error driver plug-ins WDK WHEA , error recovery", "PSHED plug-ins WDK WHEA , error recovery", "error recovery WDK WHEA"]
---

# Participating in Error Recovery


To participate in error recovery, a PSHED plug-in must implement an [*AttemptRecovery*](https://msdn.microsoft.com/library/windows/hardware/ff559257) callback function.

The following code example shows how to implement this callback function.

```
//
// The PSHED plug-in&#39;s AttemptRecovery callback function
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Participating%20in%20Error%20Recovery%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


