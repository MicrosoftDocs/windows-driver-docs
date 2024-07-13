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
ms.date: 06/04/2020
---

# Using boot parameters

Driver developers and testers often have to add, delete, and change the parameters of boot entries to test their drivers under variable conditions. This section describes a few common scenarios and suggests strategies for configuring boot parameters in the BCD store file.

From Windows Vista to Windows 11, "BCD store" refers to a file named `BCD` , yes, just `BCD` no extension name.

- For a legacy (BIOS) boot, the `BCD` file used is at `X:\Boot\BCD` .
- For a UEFI boot, the `BCD` file used is at `X:\EFI\Microsoft\Boot\BCD` .

The X: drive letter above refers to:

- (for legacy boot) the partition where the `bootmgr` program resides, which is normally the "active" partition from the MBR partition table,
- (for UEFI boot) the EFI system partition marked in GPT partition table.


> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803.
> Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.

This section contains the following topics:

[Boot Parameters to Enable Debugging](boot-parameters-to-enable-debugging.md)

[Boot Parameters to Manipulate Memory](boot-parameters-to-manipulate-memory.md)

[Boot Parameters to Load a Partial Checked Build](boot-parameters-to-load-a-partial-checked-build.md)

[Boot Parameters to Enable EMS Redirection](boot-parameters-to-enable-ems-redirection.md)

[Boot Parameters to Configure DEP and PAE](boot-parameters-to-configure-dep-and-pae.md)
