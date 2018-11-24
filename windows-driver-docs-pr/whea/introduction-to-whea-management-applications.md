---
title: Introduction to WHEA Management Applications
description: Introduction to WHEA Management Applications
ms.assetid: d0c487bd-dfa8-43f2-a494-0ed95d767bfb
keywords:
- management applications WDK WHEA , about management applications
- user-mode applications WDK WHEA , management applications
- WHEA WDK , management applications
- Windows Hardware Error Architecture WDK , management applications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to WHEA Management Applications


The Windows Hardware Error Architecture (WHEA) provides a Windows Management Instrumentation (WMI) interface that allows user-mode applications to perform WHEA management operations. The WHEA management interface is composed of the following WMI provider classes:

<a href="" id="wheaerrorsourcemethods"></a>[WHEAErrorSourceMethods](https://msdn.microsoft.com/library/windows/hardware/ff559521)  
This class implements methods for managing the [error sources](hardware-errors-and-error-sources.md) in the system.

<a href="" id="wheaerrorinjectionmethods"></a>[WHEAErrorInjectionMethods](https://msdn.microsoft.com/library/windows/hardware/ff559513)  
This class implements methods for injecting hardware errors into the hardware platform.

A user-mode application calls the methods in these classes indirectly by calling the **IWbemServices::ExecMethod** method. For more information about how to call methods in WMI provider classes, see the [Calling a Provider Method](http://go.microsoft.com/fwlink/p/?linkid=80945) topic in the Microsoft Windows SDK documentation.

For more information about WMI, see the [Windows Management Instrumentation](http://go.microsoft.com/fwlink/p/?linkid=80947) section of the Windows SDK documentation.

**Note**  The WHEA WMI provider classes are supported in Windows Server 2008, Windows Vista SP1 and later versions of Windows.

 

 

 




