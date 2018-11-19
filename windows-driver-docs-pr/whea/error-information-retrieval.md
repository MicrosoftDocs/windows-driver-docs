---
title: Error Information Retrieval
description: Error Information Retrieval
ms.assetid: 4af06727-9660-4bbc-8c9e-a50c8f2d566d
keywords:
- Windows Hardware Error Architecture WDK , error information retrieval
- WHEA WDK , error information retrieval
- hardware errors WDK WHEA , error information retrieval
- errors WDK WHEA , error information retrieval
- platform-specific hardware error driver plug-ins WDK WHEA , error information retrieval
- PSHED plug-ins WDK WHEA , error information retrieval
- error information retrieval WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




