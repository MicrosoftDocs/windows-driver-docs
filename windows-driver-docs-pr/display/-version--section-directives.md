---
title: '[Version] Section Directives'
description: This topic describes [Version] section directives in the INF.
ms.date: 01/12/2024
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
PnpLockdown=1

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
CatalogFile=ExampleCatalog.cat
PnpLockdown=1

Note:
no line item for LayoutFile=layout.inf
```
