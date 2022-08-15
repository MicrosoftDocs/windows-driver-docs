---
title: Copying INF Files
description: Copying INF Files
keywords:
- INF files WDK device installations , copying
- copying INF files
ms.date: 01/21/2022
---

# Copying INF Files

It is sometimes necessary to stage other [driver packages](driver-packages.md) into the [Driver Store](driver-store.md) of the system as part of staging a primary driver package.  For example, the driver package for the root of a multifunction device might stage the driver packages for the device's individual functions so that Windows has these driver packages available as it installs the device's functions.

To stage other [driver packages](driver-packages.md) into the [Driver Store](driver-store.md) of the system, an INF file can use the [**INF CopyINF directive**](inf-copyinf-directive.md).

Installation software must never copy INF files directly into a system's *%SystemRoot%/inf* directory or Driver Store directory.

 

 





