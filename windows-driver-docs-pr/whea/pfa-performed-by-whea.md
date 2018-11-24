---
title: PFA Performed by WHEA
description: PFA Performed by WHEA
ms.assetid: c93b15aa-9b99-4dfa-8c97-b503654e44f2
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

# PFA Performed by WHEA


Starting with Windows 7, the Windows Hardware Error Architecture (WHEA) supports Predictive Failure Analysis (PFA) for Error Correction Code (ECC) memory.

**Important**  A [platform-specific hardware error driver (PSHED) plug-in](platform-specific-hardware-error-driver-plug-ins2.md) can perform PFA on ECC memory instead of WHEA. If the plug-in performs PFA, it must follow the steps that are described in [PFA Performed by a PSHED Plug-In](pfa-performed-by-a-pshed-plug-in.md). The plug-in must not follow the steps that are described in this topic.

 

When an ECC memory error occurs, WHEA performs the following steps:

1.  The *low-level hardware error handler* (*LLHEH*) is notified about the presence of the memory error condition.

2.  The LLHEH retrieves memory error information from the error source and uses the error data to fill in a hardware error packet. This packet is formatted as a [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure.

3.  The LLHEH calls into the PSHED to retrieve any platform-specific hardware error information. If a PSHED plug-in in installed and is registered to retrieve information about the error, the PSHED will call into the PSHED plug-in so that the plug-in can modify the error information that is returned to the LLHEH.

4.  The LLHEH calls the Windows operating system kernel, passing it the error packet.

5.  The Windows kernel creates an [error record](error-records.md) and adds to it the information from the error packet that was received from the LLHEH. Additionally, the Windows kernel adds other information about the error (such as the error source, the severity of the error, and how many times the error has occurred) to the error record.

6.  The Windows kernel calls into the PSHED to allow the PSHED to add sections to the error record.

7.  If a PSHED plug-in is installed and is registered to retrieve information about the error, the PSHED will call into the PSHED plug-in so that the plug-in can modify the information in the error record.

    **Note**  If the PSHED plug-in is not performing PFA, it must not set the **PlatformPfaControl** bit in the [**WHEA\_ERROR\_PACKET\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff560472) member of the [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure.

     

8.  If PFA is enabled, WHEA performs PFA on the ECC memory page. For more information about this process, see [How WHEA Performs PFA on ECC Memory](how-whea-performs-pfa-on-ecc-memory.md).

9.  The Windows kernel generates an ETW event and logs the error information in the system event log.

 

 




