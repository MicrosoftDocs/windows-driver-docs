---
title: Common WIA Security Problems
author: windows-driver-content
description: Common WIA Security Problems
ms.assetid: d3f7d6e9-1ac4-4209-92bb-d08e4e13a4ad
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Common WIA Security Problems


## <a href="" id="ddk-common-wia-security-problems-si"></a>


There are several common problems that could prevent an existing WIA driver (which ran fine under **LocalSystem**) from running successfully under the **LocalService** account.

The most common problems occur with:

-   File system access

    The **LocalService** account has severely restricted file access. For example, drivers can no longer write to the %*windir*% directory.

-   Registry access

    Many registry keys that were open to **LocalSystem** accounts are read-only to **LocalService**. For example, drivers are no longer able to write to registry keys under the HKLM subtree.

-   Named kernel objects

    Make sure that named objects (for example, events and mutexes) accessed by both the WIA driver and external components, such as bundled applications, have the appropriate ACLs. If an application creates a named event object, but does not specifically grant access to a **LocalService** account, the driver will not be able to use it. Similarly, if a minidriver creates a named event object it must grant the same access or the application will not be able to use the event object.

-   Out-of-process COM objects

    Any attempt to either create or use an out-of-process COM interface will fail unless that component explicitly grants the appropriate permissions to a **LocalService** account. For example, calls to **CoCreateInstance** or **CoCreateInstanceEx** (both are described in the Microsoft Windows SDK documentation) with the CLSCTX\_LOCAL\_SERVER flag set can fail if the component does not grant permission to a **LocalService** account. Similarly, the driver attempting to use a pointer to a COM interface that is not in-process to the driver can fail. This can occur if a component calls the driver and hands it a pointer to an interface by which the driver can call back to the interface.

-   Creating and opening processes

    WIA drivers should not manually start other processes (for example, by calling **CreateProcess** or **CreateProcessAsUser**). Although this behavior would have succeeded for drivers under **LocalSystem** accounts, it is no longer possible for drivers to do so under the new **LocalService** account. For more information about **CreateProcess** and **CreateProcessAsUser**, see the Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Common%20WIA%20Security%20Problems%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


