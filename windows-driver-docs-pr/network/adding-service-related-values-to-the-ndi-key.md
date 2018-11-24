---
title: Adding Service-Related Values to the Ndi Key
description: Adding Service-Related Values to the Ndi Key
ms.assetid: f967396c-6695-458c-a081-ef382ed7c9dd
keywords:
- add-registry-sections WDK networking , Ndi values and keys
- Nido keys and values WDK networking
- service-related values to Ndi key WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Service-Related Values to the Ndi Key





If a component has an associated service (device driver), the *add-registry-section* referenced by the *DDInstall* section for that component must add a **Service** value to the Ndi key. The **Service** value is a REG\_SZ value that specifies the primary service associated with the component. The **Service** value must match the *ServiceName* parameter of the **AddService** directive that references the *service-install-section* for the primary service. For more information, see [INF DDInstall.Services Section](ddinstall-services-section-in-a-network-inf-file.md).

If a component has one or more associated services, the *add-registry-section* referenced by the *DDInstall* section for that component must add a **CoServices** value to the **Ndi** key. The **CoServices** value is a MULTI\_SZ value that specifies all the services that the component installs, including the primary service specified by the **Service** value. The **CoServices** value is required for all **NetTrans**, **NetClient**, and **NetService** components.

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

**Note**  **Net** components (adapters) should not have a **CoServices** value, because only one service can be associated with an adapter.

 

Except for shutting down services, all service-related actions are performed on the **CoServices** in the order that they are listed. For example, services are started in the order that they are listed. Services are stopped, however, in reverse order. Service-related actions for a component are performed on a service only if that service is listed in **CoServices**.

 

 





