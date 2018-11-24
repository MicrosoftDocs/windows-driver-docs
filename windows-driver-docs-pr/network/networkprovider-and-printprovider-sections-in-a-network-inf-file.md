---
title: NetworkProvider and PrintProvider Sections in a Network INF File
description: NetworkProvider and PrintProvider Sections in a Network INF File
ms.assetid: 9ce32644-2b11-4c03-9743-d678ff8de229
keywords:
- INF files WDK network , PrintProvider section
- network INF files WDK , PrintProvider section
- INF files WDK network , NetworkProvider section
- network INF files WDK , NetworkProvider section
- PrintProvider section WDK networking
- NetworkProvider section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NetworkProvider and PrintProvider Sections in a Network INF File





**NetClient** components are considered to be network providers because they provide network services to user applications. The Microsoft Client for Networks and the NetWare Client are examples of **NetClient** components.

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

In addition to being a network provider, a **NetClient** component can also be a print provider. A print provider provides print services to user applications over a network.

A **NetClient** component is always installed as a network provider. An INF file that installs a **NetClient** component does not require a NetworkProvider section for that component unless at least one of the following is true:

-   An alternative device name is specified for the component.

-   A short name for the component is specified for use with the **net view** command. For more information, see [Including a NetworkProvider Section](including-a-networkprovider-section.md).

An INF that installs a **NetClient** component that is a print provider must contain a **PrintProvider** section for that component. For more information, see [Including a PrintProvider Section](including-a-printprovider-section.md).

An INF file that installs a **NetClient** component must also contain an *add-registry-section* (referenced by a **AddReg** directive in the *service-install-section* for a component) that adds a **NetworkProvider** key to the component's **service** key. For more information, see [Specifying the Name and Provider Path for a NetClient Component](specifying-the-name-and-provider-path-for-a-netclient-component.md).

 

 





