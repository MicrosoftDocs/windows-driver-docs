---
title: Using Boot Parameters
description: Using Boot Parameters
keywords:
- boot entries WDK
- boot options WDK , boot parameters
- driver testing WDK boot options
- testing drivers WDK boot options
- debugging drivers WDK boot options
- driver debugging WDK boot options
- NVRAM boot options WDK , boot parameters
- EFI NVRAM boot options WDK , boot parameters
- Boot.ini files WDK , boot parameters
ms.date: 07/19/2024
ms.topic: concept-article
---

# Using boot parameters

Driver developers and testers often have to add, delete, and change the parameters of boot entries to test their drivers under variable conditions. This section describes a few common scenarios and suggests strategies for configuring boot parameters.

For information on working with the BCD data store, see [Editing Boot Options](editing-boot-options.md).

This section contains the following topics:

[Boot Parameters to Enable Debugging](boot-parameters-to-enable-debugging.md)

[Boot Parameters to Manipulate Memory](boot-parameters-to-manipulate-memory.md)

[Boot Parameters to Load a Partial Checked Build](boot-parameters-to-load-a-partial-checked-build.md)

[Boot Parameters to Enable EMS Redirection](boot-parameters-to-enable-ems-redirection.md)

[Boot Parameters to Configure DEP and PAE](boot-parameters-to-configure-dep-and-pae.md)

> [!CAUTION]
> Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the **BCDEdit /set** command could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings. For more information, see *[How to open MSConfig in Windows 10](https://support.microsoft.com/help/4026130/windows-how-to-open-msconfig-in-windows-10)*.
