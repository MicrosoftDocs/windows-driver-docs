---
title: New Information for Windows Hardware Error Architecture
description: New Information for Windows Hardware Error Architecture
ms.assetid: 258dca19-3988-4fab-bc9f-a93035cbbd0e
keywords:
- Windows Hardware Error Architecture WDK , new information
- WHEA WDK , new information
- hardware errors WDK WHEA , new information
- errors WDK WHEA , new information about WHEA
- source information WDK WHEA , new
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# New Information for Windows Hardware Error Architecture


This section summarizes major additions and revisions to the Windows Hardware Error Architecture (WHEA). Each topic in this section describes the changes that have been made to WHEA for each Windows operating system release.

This section includes the following topics:

[WHEA Changes for Windows Server 2008 and Windows Vista SP1](whea-changes-for-windows-server-2008-and-windows-vista-sp1.md)

[WHEA Changes for Windows 7](whea-changes-for-windows-7.md)

## (*New*) WHEA Changes for Windows 8


Starting with Windows 8, the following changes have been made to Windows Hardware Error Architecture (WHEA)

-   A new WMI provider class [**WHEAPolicyManagementMethods**](https://msdn.microsoft.com/library/windows/hardware/hh451252).
-   WHEA policies can be managed either though [**WHEAPolicyManagementMethods**](https://msdn.microsoft.com/library/windows/hardware/hh451252) or through the WHEA Powershell module. If the policy is updated through either of these modes, the policy values take effect immediately.
-   The WHEA WMI Method [**WHEAErrorSourceMethods::SetErrorSourceInfoRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559531) is deprecated.

 

 




