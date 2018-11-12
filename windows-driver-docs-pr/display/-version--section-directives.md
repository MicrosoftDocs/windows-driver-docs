---
title: '[Version] section directives'
description: This topic describes [Version] section directives in the INF.
ms.assetid: 76AC10DC-AECC-4C35-8BEE-4B2E8B06FEE0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \[Version\] section directives


This topic describes *\[Version\]* section directives in the INF.

All inbox drivers must not reference the Layout.inf file.

All inbox drivers must not reference any catalog files.

For example:

``` syntax
[Version]
Signature="$Windows NT$"
Provider=%MSFT%
ClassGUID={4D36E968-E325-11CE-BFC1-08002BE10318}
Class=Display
DriverVer=11/22/2004, 6.14.10.7000

Note: 
no line item for LayoutFile=layout.inf
no line item for CatalogFile=delta.cat
```

WHQL display drivers must not reference the Layout.inf file.

For example:

``` syntax
[Version]
Signature="$Windows NT$"
Provider=%IHV%
ClassGUID={4D36E968-E325-11CE-BFC1-08002BE10318}
Class=Display
DriverVer=11/22/2004, 6.14.10.7000

Note: 
no line item for LayoutFile=layout.inf
```

 

 





