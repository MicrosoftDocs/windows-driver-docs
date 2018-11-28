---
title: UMDF Based on COM Subset
description: UMDF Based on COM Subset
ms.assetid: 918459a9-a6a2-40b8-8b97-3aabe3e49bfb
keywords:
- UMDF objects WDK , COM subset
- framework objects WDK UMDF , COM subset
- COM WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UMDF Based on COM Subset


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework objects and interfaces are based on the Component Object Model (COM) for the following reasons:

-   COM is familiar to many applications programmers.

-   C++ is the preferred language for programming COM applications.

-   COM interfaces enable logical groupings of functions, so that the device driver interface (DDI) is easy to understand and navigate.

-   Using COM enables the DDI to extend and evolve without requiring existing driver DLLs to be recompiled.

-   Numerous tools, including Microsoft Visual Studio and active template library (ATL), support COM-based applications and objects.

The framework uses only a small subset of COM; it does not depend on the entire COM infrastructure and runtime library. Instead, the framework uses only the query-interface and reference-counting features. Every framework interface derives from **IUnknown** and therefore supports the **QueryInterface**, **AddRef**, and **Release** methods by default. The **AddRef** and **Release** methods manage object lifetime. The **QueryInterface** method enables other components to determine which interfaces the driver supports.

 

 





