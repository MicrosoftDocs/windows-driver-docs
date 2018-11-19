---
title: Common WIA Security Problems
description: Common WIA Security Problems
ms.assetid: d3f7d6e9-1ac4-4209-92bb-d08e4e13a4ad
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Common WIA Security Problems





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

 

 




