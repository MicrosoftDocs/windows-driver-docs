---
title: PFA Performed by WHEA
author: windows-driver-content
description: PFA Performed by WHEA
ms.assetid: c93b15aa-9b99-4dfa-8c97-b503654e44f2
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20PFA%20Performed%20by%20WHEA%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


