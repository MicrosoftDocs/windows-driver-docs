---
title: WHEA Changes for Windows 7
description: WHEA Changes for Windows 7
ms.assetid: d92c2be0-732b-4fcd-b517-5cb9eccf962b
keywords:
- Windows Hardware Error Architecture WDK , Windows 7 changes
- WHEA WDK , Windows 7 changes
- Windows 7 WDK WHEA
- Windows 7 WDK WHEA , WHEA changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WHEA Changes for Windows 7


Starting with Windows 7, the following changes have been made to Windows Hardware Error Architecture (WHEA):

-   A new error record format ([**WHEA\_ERROR\_PACKET\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff560480)) is used to report a hardware error in Windows 7 and later versions of Windows. The previous error record format ([WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465)) has been renamed to [**WHEA\_ERROR\_PACKET\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff560476), and is only used to report a hardware error in Windows Server 2008 and Windows Vista SP1.

    Starting with the Windows 7 Windows Driver Kit (WDK), WHEA\_ERROR\_PACKET is a macro that, depending on the build target, references either the WHEA\_ERROR\_PACKET\_V1 or WHEA\_ERROR\_PACKET\_V2 structures.

    For more information about this change, see [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465).

-   Various Windows Hardware Error Architecture (WHEA) data types have been renamed in the Windows 7 Windows Driver Kit (WDK). For more information about these changes, see [Renamed WHEA Data Types](renamed-whea-data-types.md).

-   WHEA supports Predictive Failure Analysis (PFA) for Error Correction Code (ECC) memory. Through PFA, WHEA can monitor one or more ECC memory pages that have encountered previous errors. When too many errors have occurred, WHEA attempts to bring the memory page into an offline state.

    A [platform-specific hardware error driver (PSHED) plug-in](platform-specific-hardware-error-driver-plug-ins2.md) can extend WHEA's PFA support by performing PFA itself on ECC memory. In this way, the plug-in must decide when to bring a memory page into an offline state.

-   Additional WHEA error-specific hardware errors have been defined. For more information about these errors, see [WHEA Hardware Error Events (Windows Server 2008, Windows Vista SP1 and Later)](https://msdn.microsoft.com/library/windows/hardware/ff560537).

 

 




