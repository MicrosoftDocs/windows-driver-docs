---
title: Error Processing
description: Error Processing
ms.assetid: d9cb2f62-1ccf-4ab6-b547-dc54f6d07820
keywords:
- Windows Hardware Error Architecture WDK , error processing
- WHEA WDK , error processing
- hardware errors WDK WHEA , error processing
- errors WDK WHEA , error processing
- corrected errors WDK WHEA
- uncorrected errors WDK WHEA
- fatal hardware errors WDK WHEA
- non-fatal hardware errors WDK WHEA
- low-level hardware error handlers WDK WHEA
- LLHEHs WDK WHEA
- platform-specific hardware error drivers WDK WHEA
- PSHED WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Processing


The Windows Hardware Error Architecture (WHEA) processes hardware errors in different ways depending on the classification of the error condition. For more information about the different classifications of hardware errors, see [Hardware Errors and Error Sources](hardware-errors-and-error-sources.md).

The following describes the sequence of actions taken by WHEA in response to each type of hardware error condition. For more information about the WHEA components that are referenced in these actions, see [Components of the Windows Hardware Error Architecture](components-of-the-windows-hardware-error-architecture.md).

### **Corrected Hardware Error**

1.  The *low-level hardware error handler* (*LLHEH*) is notified about the presence of the hardware error condition.

2.  The LLHEH verifies the presence of the hardware error.

3.  The LLHEH retrieves hardware error information from the error source and uses the error data to fill in a hardware error packet. This packet is formatted as a [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure.

4.  The LLHEH calls into the *platform-specific hardware error driver* (PSHED) to retrieve any platform-specific hardware error information. If a PSHED plug-in is installed and is registered to participate in error information retrieval, the PSHED will in turn call into the PSHED plug-in so that it can further augment the error information that is returned to the LLHEH.

5.  The LLHEH calls the Windows operating system kernel, passing it the error packet.

6.  The Windows kernel creates an [error record](error-records.md) and fills it in with the information from the error packet that was received from the LLHEH as well as other information about the error, such as the error source, the severity of the error, and how many times the error has occurred.

7.  The Windows kernel calls into the PSHED to allow the PSHED to add sections to the error record. If a PSHED plug-in is installed and is registered to participate in error information retrieval, the PSHED will in turn call into the PSHED plug-in so that it can further augment the information in the error record.

8.  The Windows kernel calls into the PSHED to clear the error source's status registers. If a PSHED plug-in is installed and is registered to participate in error information retrieval, the PSHED will in turn call into the PSHED plug-in so that it can clear the error source's status registers.

9.  If the hardware error condition exceeds the error threshold of the error source, the Windows kernel generates an ETW event and logs the error information in the system event log.

### **Nonfatal Uncorrected Hardware Error**

1.  The LLHEH is notified about the presence of the hardware error condition.

2.  The LLHEH verifies the presence of the hardware error.

3.  The LLHEH retrieves hardware error information from the error source and uses the error data to fill in a hardware error packet.

4.  The LLHEH calls into the PSHED to retrieve any platform-specific hardware error information. If a PSHED plug-in is installed and is registered to participate in error information retrieval, the PSHED will in turn call into the PSHED plug-in so that it can further augment the error information that is returned to the LLHEH.

5.  The LLHEH calls the Windows operating system kernel, passing it the error packet.

6.  The Windows kernel creates an [error record](error-records.md) and fills it in with the information from the error packet that was received from the LLHEH as well as other information about the error, such as the error source, the severity of the error, and how many times the error has occurred.

7.  The Windows kernel calls into the PSHED to allow the PSHED to add sections to the error record. If a PSHED plug-in is installed and is registered to participate in error information retrieval, the PSHED will in turn call into the PSHED plug-in so that it can further augment the information in the error record.

8.  The Windows kernel attempts to recover from the error by trying to correct the hardware error condition. The Windows kernel then calls into the PSHED to give it an opportunity to perform any required recovery operations. If a PSHED plug-in is installed and is registered to participate in error recovery, the PSHED will in turn call into the PSHED plug-in so that it can try to correct the error and/or perform any additional operations required to fully recover from the error condition.

9.  If the hardware error was successfully corrected, the Windows kernel generates an ETW event and logs the error information in the system event log. If the hardware error was not corrected, the Windows kernel calls into the PSHED to save the error record. If a PSHED plug-in is installed and is registered to participate in error record persistence, the PSHED will in turn call into the PSHED plug-in so that it can save the error record. After the error record has been saved, the Windows kernel generates a bug check.

### **Fatal Uncorrected Hardware Error**

1.  The LLHEH is notified about the presence of the hardware error condition.

2.  The LLHEH verifies the presence of the hardware error.

3.  The LLHEH retrieves hardware error information from the error source and uses the error data to fill in a hardware error packet.

4.  The LLHEH calls into the PSHED to retrieve any platform-specific hardware error information. If a PSHED plug-in is installed and is registered to participate in error information retrieval, the PSHED will in turn call into the PSHED plug-in so that it can further augment the error information that is returned to the LLHEH.

5.  The LLHEH calls the Windows operating system kernel, passing it the error packet.

6.  The Windows kernel creates an [error record](error-records.md) and fills it in with the information from the error packet that was received from the LLHEH as well as other information about the error, such as the error source, the severity of the error, and how many times the error has occurred.

7.  The Windows kernel calls into the PSHED to save the error record. If a PSHED plug-in is installed and is registered to participate in error record persistence, the PSHED will in turn call into the PSHED plug-in so that it can save the error record.

8.  The Windows kernel generates a bug check.

 

 




