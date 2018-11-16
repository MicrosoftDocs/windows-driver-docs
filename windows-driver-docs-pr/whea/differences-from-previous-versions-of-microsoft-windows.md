---
title: Differences from Previous Versions of Microsoft Windows
description: Differences from Previous Versions of Microsoft Windows
ms.assetid: 9c30c5c6-27a7-424e-b5f0-ab625eed4b8a
keywords:
- Windows Hardware Error Architecture WDK , earlier Windows versions
- WHEA WDK , comparison with earlier Windows versions
- hardware errors WDK WHEA , earlier Windows versions
- errors WDK WHEA , earlier Windows versions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences from Previous Versions of Microsoft Windows


The following lists summarize the differences between the Windows Hardware Error Architecture (WHEA) and the hardware error handling in versions of Microsoft Windows prior to Windows Vista.

### **Error handling in previous versions of Windows**

-   Includes numerous unrelated error reporting mechanisms

-   Has different error signaling and reporting mechanisms for each processor architecture

-   Has no means for the operating system to determine what error sources are supported by a particular hardware platform

-   Does not capture all of the available error information

-   Does not effectively use existing or future hardware error standards

-   Does not effectively take advantage of any platform-specific capabilities

-   Offers no common error record format for reporting error data

-   Offers no error record persistence mechanism for fatal hardware errors; significant error data is lost when the system is restarted

-   Offers poor support for handling I/O hardware errors

-   Offers little support for error recovery

-   Offers little support for error management applications

-   Difficult to determine the root cause of hardware errors

-   Offers little flexibility for platform and firmware vendors' hardware error handling implementations

### **Windows Hardware Error Architecture**

-   Includes a common error reporting infrastructure for all hardware errors on all processor architectures and hardware platforms

-   Includes an error source discovery mechanism for determining the error sources that are supported by a particular hardware platform\*

-   Enables the operating system to capture all of the available error information

-   Makes full use of existing hardware error standards and allows for supporting future hardware error standards by using new Platform Specific Hardware Error Drivers (PSHEDs)

-   Allows you to use PSHED plug-ins to take advantage of platform-specific capabilities

-   Uses a common [error record](error-records.md) format for all types of hardware errors

-   Includes an error record persistence mechanism for fatal hardware errors that preserves the complete error record while the system is restarted\*

-   Provides enhanced support for handling I/O hardware errors

-   Includes an infrastructure for recovery from nonfatal hardware errors\*

-   Provides support for error management applications through ETW-based error event reporting and a user-mode error management API\*

-   Easier to determine the root cause of hardware errors

-   Offers new alternatives for platform and firmware vendors' hardware error implementations\*

**Note**   Items identified with an asterisk (\*) are supported in Windows Server 2008, Windows Vista SP1 and later versions of Windows.

 

 

 




