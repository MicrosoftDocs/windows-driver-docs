---
title: How WHEA Performs PFA on ECC Memory
author: windows-driver-content
description: How WHEA Performs PFA on ECC Memory
ms.assetid: def94688-9ca6-4146-8d5b-4c3550d3d272
keywords:
- predictive failure analysis (PFA) WDK WHEA , Error Correction Code memory
- PFA WDK WHEA , Error Correction Code memory
- Error Correction Code memory WDK WHEA
- Error Correction Code memory WDK WHEA , predictive failure analysis
- low-level hardware error handler WDK WHEA
- LLHEH WDK WHEA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# How WHEA Performs PFA on ECC Memory


Starting with Windows 7, the Windows Hardware Error Architecture (WHEA) supports Predictive Failure Analysis (PFA) for Error Correction Code (ECC) memory.

WHEA performs PFA on ECC memory pages only if the following are true:

-   The registry value **MemPfaDisable** is not set to 1.

-   A [platform-specific hardware error driver (PSHED) plug-in](platform-specific-hardware-error-driver-plug-ins2.md) had not previously set the **PlatformPfaControl** bit in the [**WHEA\_ERROR\_PACKET\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff560472) member of the [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure to 1. The plug-in sets this bit if it is performing PFA. For more information about how PFA is performed by this plug-in, see [PFA Performed by a PSHED Plug-In](pfa-performed-by-a-pshed-plug-in.md).

When an ECC memory error occurs on a memory page, WHEA performs PFA on the ECC memory page by following these steps:

1.  If WHEA is currently not monitoring the ECC memory page, WHEA adds the page to its monitoring database and clears the error count and tick count for the new entry.

    **Note**  WHEA will stop monitoring an ECC memory page when its tick count exceeds the **MemPfaTimeout** registry value. When this happens, WHEA removes the entry from its monitoring database.

     

2.  WHEA increments the error count for the ECC memory page.

3.  If the error count exceeds the **MemPfaThreshold** registry value, WHEA first calls the system memory manager to take the ECC memory page offline.

    **Note**  When the system memory manager is called, there is no guarantee that the ECC memory page will actually be taken offline.

     

    WHEA then adds the memory page into the Boot Configuration Data (BCD) in the system store. This prevents the memory page from being used after the next system restart.

    **Note**  WHEA will not take a hardware component, such as an ECC memory page, offline if the registry value **DisableOffline** is set to a nonzero value. Also, WHEA will not add the ECC memory page to the BCD store if the registry value **MemPersistOffline** is set to 0.

     

For more information about the PFA registry values for WHEA, see [WHEA Policy Settings](whea-pfa-registry-settings.md).

For more information about the system memory manager, see the [Memory Management](http://go.microsoft.com/fwlink/p/?linkid=140723) in the Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20How%20WHEA%20Performs%20PFA%20on%20ECC%20Memory%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


