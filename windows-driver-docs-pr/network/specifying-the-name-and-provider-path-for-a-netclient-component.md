---
title: Specifying the Name and Provider Path for a NetClient Component
description: Specifying the Name and Provider Path for a NetClient Component
ms.assetid: 4c9c2162-8e7e-44dc-a97c-81074071664b
keywords:
- add-registry-sections WDK networking , NetClient component name and path
- NetClient component name and path WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying the Name and Provider Path for a NetClient Component





An INF file that installs a NetClient component must add a **NetworkProvider** key to the *service* key for the component. The INF file adds the **NetworkProvider** key through an *add-registry-section* that is referenced by an **AddReg** directive in the *service-install* section for the component.

The **NetworkProvider** key has two values: a **Name** that specifies the name of the network provider, and a **ProviderPath** that specifies the full path to the network provider DLL.

The following is an example of an *add-registry-section* that adds the **NetworkProvider** key to the instance key for a component:

```INF
[NWCWorkstation.AddReg]
HKR, NetworkProvider, Name, 0, "NetWare or Compatible Network"
HKR, NetworkProvider, ProviderPath, 0x20000, "%11%\nwprovau.dll"
```

**Note**  An INF file that installs a **NetClient** component does not have to update the **ProviderOrder** value under the component's ... **Control\\Network\\Provider\\Order** key. This is done automatically by the network class installer.

 

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

 

 





