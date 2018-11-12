---
title: DDInstall.Services Section in a Network INF File
description: DDInstall.Services Section in a Network INF File
ms.assetid: 5d5cc0ac-fbe2-4791-9c74-fdf9906faff6
keywords:
- INF files WDK network , DDInstall.Services section
- network INF files WDK , DDInstall.Services section
- DDInstall.Services section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DDInstall.Services Section in a Network INF File





A *DDInstall*.**Services** section in a network INF file is based on the generic [**INF DDInstall.Services section**](https://msdn.microsoft.com/library/windows/hardware/ff547349).

A *DDInstall*.**Services** section contains one or more **AddService** directives, each of which references an INF-writer-defined *service-install- section* that specifies how and when the services of particular component drivers are loaded.

A *DDInstall*.**Services** section is required in an INF file that installs a Net component (adapter); it is optional in an INF file that installs a **NetTrans**, **NetClient**, or **NetService** component.

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

An **AddService** directive in a *DDInstall*.**Services** section can also reference an *error-log-install-section* that installs an error log for a component. An error log is optional for all network components.

For more information, see [**INF AddService Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326).

The following is an example of a *DDInstall*.**Services** section, a *service-install-section*, an *error-log-install-section*, and an *add-registry-section* that is referenced by an **AddReg** directive in the *error-log-install-section*:

```cpp
[a1.ndi.NT.Services]
AddService = a1, 2, a1.AddService, a1.AddEventLog
 
[a1.AddService]
DisplayName = %Adapter1.DispName%
ServiceType = 1 ;SERVICE_KERNEL_DRIVER
StartType = 2 ;SERVICE_AUTO_START
ErrorControl = 1 ;SERVICE_ERROR_NORMAL
ServiceBinary = %12%\a1.sys
LoadOrderGroup = NDIS
 
[a1.AddEventLog]
AddReg = a1.AddEventLog.reg
 
[a1.AddEventLog.reg]
HKR,,EventMessageFile,0x00020000,"%%SystemRoot%%\System32\netevent.dll"
HKR,,TypesSupported,0x00010001,7
```

The *ServiceName* parameter of the **AddService** directive, which in the above example is **a1**(the first **AddService** parameter), must match the component's **Ndi\\Service** value. For more information, see [Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md).

 

 





