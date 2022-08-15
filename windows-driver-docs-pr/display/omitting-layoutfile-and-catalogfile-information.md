---
title: Omitting LayoutFile and CatalogFile Information
description: Omitting LayoutFile and CatalogFile Information
keywords:
- INF files WDK display , LayoutFile directive
- INF files WDK display , CatalogFile directive
- CatalogFile directive WDK display
- LayoutFile directive WDK display
ms.date: 04/20/2017
---

# Omitting LayoutFile and CatalogFile Information


You must not specify any information for the **LayoutFile** and **CatalogFile** directives in the **Version** section. The following example shows a typical **Version** section:

```inf
[Version]
Signature="$Windows NT$"
Provider=%MSFT%
ClassGUID={4D36E968-E325-11CE-BFC1-08002BE10318}
Class=Display
DriverVer=11/22/2004, 6.14.10.7000
```

For more information about the **Version** section and directives that are associated with **Version**, see [**INF Version Section**](../install/inf-version-section.md).

 

