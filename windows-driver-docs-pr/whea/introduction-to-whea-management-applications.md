---
title: Introduction to WHEA Management Applications
author: windows-driver-content
description: Introduction to WHEA Management Applications
ms.assetid: d0c487bd-dfa8-43f2-a494-0ed95d767bfb
keywords:
- management applications WDK WHEA , about management applications
- user-mode applications WDK WHEA , management applications
- WHEA WDK , management applications
- Windows Hardware Error Architecture WDK , management applications
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Introduction%20to%20WHEA%20Management%20Applications%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


