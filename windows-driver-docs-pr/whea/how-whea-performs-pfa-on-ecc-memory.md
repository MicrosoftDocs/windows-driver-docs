---
title: How WHEA Performs PFA on ECC Memory
description: How WHEA Performs PFA on ECC Memory
ms.assetid: def94688-9ca6-4146-8d5b-4c3550d3d272
keywords:
- predictive failure analysis (PFA) WDK WHEA , Error Correction Code memory
- PFA WDK WHEA , Error Correction Code memory
- Error Correction Code memory WDK WHEA
- Error Correction Code memory WDK WHEA , predictive failure analysis
- low-level hardware error handler WDK WHEA
- LLHEH WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How WHEA Performs PFA on ECC Memory


Starting with Windows 7, the Windows Hardware Error Architecture (WHEA) supports Predictive Failure Analysis (PFA) for Error Correction Code (ECC) memory.

WHEA performs PFA on ECC memory pages only if the following are true:

-   The registry value **MemPfaDisable** is not set to 1.

-   A [platform-specific hardware error driver (PSHED) plug-in](platform-specific-hardware-error-driver-plug-ins2.md) had not previously set the **PlatformPfaControl** bit in the [**WHEA\_ERROR\_PACKET\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff560472) member of the [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure to 1. The plug-in sets this bit if it is performing PFA. For more information about how PFA is performed by this plug-in, see [PFA Performed by a PSHED Plug-In](pfa-performed-by-a-pshed-plug-in.md).

When an ECC memory error occurs on a memory page, WHEA performs PFA on the ECC memory page by following these steps:

1.  If WHEA is currently not monitoring the ECC memory page, WHEA adds the page to its monitoring database and clears the error count and tick count for the new entry.

    **Note**  WHEA will stop monitoring an ECC memory page when its tick count exceeds the **MemPfaTimeout** registry value. When this happens, WHEA removes the entry from its monitoring database.



2.  WHEA increments the error count for the ECC memory page.

3.  If the error count exceeds the **MemPfaThreshold** registry value, WHEA first calls the system memory manager to take the ECC memory page offline.

    **Note**  When the system memory manager is called, there is no guarantee that the ECC memory page will actually be taken offline.




WHEA then adds the memory page into the Boot Configuration Data (BCD) in the system store. This prevents the memory page from being used after the next system restart.

**Note**  WHEA will not take a hardware component, such as an ECC memory page, offline if the registry value **DisableOffline** is set to a nonzero value. Also, WHEA will not add the ECC memory page to the BCD store if the registry value **MemPersistOffline** is set to 0.




For more information about the PFA registry values for WHEA, see [WHEA Policy Settings](whea-pfa-registry-settings.md).

For more information about the system memory manager, see the [Memory Management](http://go.microsoft.com/fwlink/p/?linkid=140723) in the Windows SDK documentation.








