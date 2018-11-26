---
title: Error Record Persistence Mechanism
description: Error Record Persistence Mechanism
ms.assetid: f361c966-7ed4-4676-afa9-75268196c0e4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Record Persistence Mechanism


Error record persistence is a mechanism by which [error records](error-records.md) can be stored in nonvolatile storage. As a result, error records are retained if the operating system must restart due to a fatal hardware error condition. This mechanism preserves the error records so that none of the captured error data related to the fatal hardware error condition is lost when the system is restarted.

After the system is restarted following a fatal hardware error, the operating system looks for and retrieves all of the error records that were stored prior to restarting the system. In situations where a system cannot be restarted back into the operating system, the system firmware or remote management software that has access to the failed system can retrieve the stored error records in order to perform error analysis.

The platform-specific hardware error driver (PSHED) implements an error record persistence interface between the operating system and the hardware platform to save and retrieve error records. For x64-based and x86-based systems, the PSHED supports the ACPI error record serialization table (ERST). For Itanium-based systems, the PSHED supports the hardware error record extension to the extensible firmware interface (EFI) runtime variable services. We recommend that platform vendors implement these error record persistence mechanisms in their hardware or firmware.

If a hardware platform does not implement hardware or firmware that is compatible with the error record persistence mechanisms that are supported by the PSHED, the platform vendor must implement a PSHED plug-in that participates in error record persistence. This PSHED plug-in interfaces with the error record persistence mechanism that is implemented by the hardware platform. For more information about how to implement a PSHED plug-in, see [Platform-Specific Hardware Error Driver Plug-Ins](platform-specific-hardware-error-driver-plug-ins2.md).

Error record persistence is supported in Windows Server 2008, Windows Vista SP1 and later versions of Windows.

 

 




