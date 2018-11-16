---
title: PFA Performed by a PSHED Plug-In
description: PFA Performed by a PSHED Plug-In
ms.assetid: e9876c86-b059-406f-a01a-7670ab294098
keywords:
- predictive failure analysis (PFA) WDK WHEA , PSHED plug-in
- PFA WDK WHEA , PSHED plug-in
- platform-specific hardware error driver (PSHED) WDK WHEA
- platform-specific hardware error driver (PSHED) WDK WHEA , predictive failure analysis
- PSHED plug-in WDK WHEA
- PSHED plug-in WDK WHEA , predictive failure analysis
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PFA Performed by a PSHED Plug-In


A [platform-specific hardware error driver (PSHED) plug-in](platform-specific-hardware-error-driver-plug-ins2.md) can perform Predictive Failure Analysis (PFA) on ECC memory. When this occurs, the plug-in and not WHEA must monitor ECC memory pages. If the plug-in determines that an ECC memory page has exceeded an error threshold, it indicates this status to WHEA. WHEA then attempts to take the memory page offline.

**Note**  If the PSHED plug-in performs PFA and uses the registry to store its configuration settings, such as error thresholds and monitoring timeouts, it should not rely on or use the WHEA PFA configuration settings described in [WHEA Policy Settings](whea-pfa-registry-settings.md).



When an ECC memory error occurs, WHEA and the plug-in perform the following steps:

1.  The *low-level hardware error handler* (*LLHEH*) is notified about the presence of the memory error condition.

2.  The LLHEH retrieves information about the memory error from the error source and uses the error data to complete a hardware error packet. This packet is formatted as a [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure.

3.  The LLHEH calls into the PSHED to retrieve any platform-specific hardware error information. If a PSHED plug-in in installed and is registered to retrieve information about errors, the PSHED will call into the PSHED plug-in so that the plug-in can modify the information about the error that is returned to the LLHEH.

4.  The LLHEH calls the Windows operating system kernel and passes it the error packet.

5.  The Windows kernel creates an [error record](error-records.md) and adds to it the information from the error packet that was received from the LLHEH. Additionally, the Windows kernel adds other information about the error, such as the error source, the severity of the error, and how many times the error has occurred to the error record.

6.  The Windows kernel calls into the PSHED to allow the PSHED to add sections to the error record.

7.  If a PSHED plug-in is installed and is registered to retrieve error information, the PSHED will call into the PSHED plug-in so that it can modify the information in the error record.

8.  If the PSHED plug-in is performing PFA on the ECC memory page, it must do the following:

    -   Set the **PlatformPfaControl** bit in the [**WHEA\_ERROR\_PACKET\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff560472) member of the [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure. If this bit is set, WHEA is no longer responsible for PFA on that memory page.
    -   If the plug-in determines that the ECC memory page that encountered the error should be taken offline, set the **PlatformDirectedOffline** bit in the [**WHEA\_ERROR\_PACKET\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff560472) member. If this bit is set, WHEA attempts to take the memory page offline.

    Otherwise, the PSHED plug-in must clear the **PlatformPfaControl** and **PlatformDirectedOffline** bits in the [**WHEA\_ERROR\_PACKET\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff560472) member of the [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure.

    **Note**  If the **PlatformPfaControl** bit is cleared, WHEA performs PFA if configured to do so and will determine whether the ECC memory page that encountered the error should be taken offline. For more information about this process, see [PFA Performed by WHEA](pfa-performed-by-whea.md).



9.  If the ECC memory page should be taken offline, WHEA first calls the system memory manager to perform this operation.

    **Note**  When the system memory manager is called, there is no guarantee that the ECC memory page will actually be taken offline.




WHEA then adds the memory page into the Boot Configuration Data (BCD) store on the system. This prevents the memory page from being used after the next system restart.

**Note**  WHEA will not take a hardware component, such as an ECC memory page, offline if the registry value **DisableOffline** is set to a nonzero value. Also, WHEA will not add the memory page to the BCD store if the registry value **MemPersistOffline** is set to 0. For more information about the registry values, see [WHEA Policy Settings](whea-pfa-registry-settings.md).



For more information about the system memory manager, see [Memory Management](http://go.microsoft.com/fwlink/p/?linkid=140723) in the Windows SDK documentation.


10. The Windows kernel generates an ETW event and logs the error information in the system event log.








