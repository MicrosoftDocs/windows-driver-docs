---
title: Creating and Opening Processes by WIA Drivers
author: windows-driver-content
description: Creating and Opening Processes by WIA Drivers
ms.assetid: c939eb25-b92b-41ef-ade0-98c2a707fee6
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating and Opening Processes by WIA Drivers


## <a href="" id="ddk-creating-and-opening-processes-by-wia-drivers-si"></a>


WIA drivers should not start other processes on the system. The two most important reasons for this are the following:

1.  Calling **CreateProcess** (described in the Microsoft Windows SDK documentation) starts the process under the same account in which the service was launched. In Windows XP, this is the **LocalSystem** account, which is a significant security risk.

2.  Calling **CreateProcessAsUser** (described in the Windows SDK documentation) can be difficult in a Fast User Switching (FUS) or Terminal Services (TS) environment. Incorrectly implemented components at this level can easily lead to successful escalation of privilege or information disclosure attacks.

The **LocalService** account does not have sufficient privileges to start other processes. Therefore, on Microsoft Windows Server 2003 and later, WIA drivers cannot create processes.

If another process is required for device functionality, it is recommended that it be implemented as a system service or local COM server. See the MSDN documentation for specific security information related to the creation of system services and COM servers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20and%20Opening%20Processes%20by%20WIA%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


