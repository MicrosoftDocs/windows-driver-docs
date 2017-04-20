---
title: New Information for Windows Hardware Error Architecture
author: windows-driver-content
description: New Information for Windows Hardware Error Architecture
ms.assetid: 258dca19-3988-4fab-bc9f-a93035cbbd0e
keywords:
- Windows Hardware Error Architecture WDK , new information
- WHEA WDK , new information
- hardware errors WDK WHEA , new information
- errors WDK WHEA , new information about WHEA
- source information WDK WHEA , new
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# New Information for Windows Hardware Error Architecture


This section summarizes major additions and revisions to the Windows Hardware Error Architecture (WHEA). Each topic in this section describes the changes that have been made to WHEA for each Windows operating system release.

This section includes the following topics:

[WHEA Changes for Windows Server 2008 and Windows Vista SP1](whea-changes-for-windows-server-2008-and-windows-vista-sp1.md)

[WHEA Changes for Windows 7](whea-changes-for-windows-7.md)

## <a href="" id="-new--whea-changes-for-windows-8"></a>(*New*) WHEA Changes for Windows 8


Starting with Windows 8, the following changes have been made to Windows Hardware Error Architecture (WHEA)

-   A new WMI provider class [**WHEAPolicyManagementMethods**](https://msdn.microsoft.com/library/windows/hardware/hh451252).
-   WHEA policies can be managed either though [**WHEAPolicyManagementMethods**](https://msdn.microsoft.com/library/windows/hardware/hh451252) or through the WHEA Powershell module. If the policy is updated through either of these modes, the policy values take effect immediately.
-   The WHEA WMI Method [**WHEAErrorSourceMethods::SetErrorSourceInfoRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559531) is deprecated.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20New%20Information%20for%20Windows%20Hardware%20Error%20Architecture%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


