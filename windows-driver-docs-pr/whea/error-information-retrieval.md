---
title: Error Information Retrieval
author: windows-driver-content
description: Error Information Retrieval
MS-HAID:
- 'whea\_af09d2b8-ae01-4619-89c2-e378ca5feaba.xml'
- 'whea.error\_information\_retrieval'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4af06727-9660-4bbc-8c9e-a50c8f2d566d
keywords: ["Windows Hardware Error Architecture WDK , error information retrieval", "WHEA WDK , error information retrieval", "hardware errors WDK WHEA , error information retrieval", "errors WDK WHEA , error information retrieval", "platform-specific hardware error driver plug-ins WDK WHEA , error information retrieval", "PSHED plug-ins WDK WHEA , error information retrieval", "error information retrieval WDK WHEA"]
---

# Error Information Retrieval


During the handling of a hardware error condition, the PSHED is called at three separate points in the error handling process.

-   The low-level hardware error handler (LLHEH) calls into the PSHED so that it can add any supplementary information about the error condition to the hardware error packet before the LLHEH reports the error to the operating system.

-   The Windows kernel calls into the PSHED so that it can add any supplementary error record sections to the error record that describes the error condition.

-   For corrected errors, the Windows kernel calls into the PSHED so that it can clear the error source's error status registers after the processing of the error is complete.

The PSHED supports error information retrieval operations for error conditions that are reported by the standard error sources that the PSHED discovers. If a PSHED plug-in is implemented that participates in [error source discovery](error-source-discovery.md) and reports additional error sources to the operating system that the PSHED does not support, the PSHED plug-in must also participate in error information retrieval to support the error information retrieval operations for these error sources. A PSHED plug-in can also optionally participate in error information retrieval to provide additional error information for error conditions that are reported by the standard error sources.

**Note**   A PSHED plug-in that participates in error information retrieval must also participate in [error source discovery](error-source-discovery.md) if either of the following is true:
-   The PSHED plug-in provides additional error information to the hardware error packets that are reported by a particular error source. In this situation, the PSHED plug-in must modify the value that is contained in the **MaxRawDataLength** member of the [**WHEA\_ERROR\_SOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff560505) structure for that error source during error source discovery to account for the additional error information.

-   The PSHED plug-in provides additional error record sections to the error records for hardware errors that are reported by a particular error source. In this situation, the PSHED plug-in must modify the value that is contained in the **MaxSectionsPerRecord** member of the WHEA\_ERROR\_SOURCE\_DESCRIPTOR structure for that error source during error source discovery to account for the additional error record sections.

 

For more information about how to implement a PSHED plug-in that participates in error information retrieval, see [Participating in Error Information Retrieval](participating-in-error-information-retrieval.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Error%20Information%20Retrieval%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


