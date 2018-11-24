---
title: Windows Kernel-Mode Safe String Library
description: Windows Kernel-Mode Safe String Library
ms.assetid: a54cd20c-2c2d-462d-b9fc-112e99562e52
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode Safe String Library


One of the major problems in software security is related to the vulnerability of working with strings. To provide greater security, Windows provides a safe string library.

Safe string library routines are prefixed with the letters "**Rtl**"; for a list of all safe string library routines for the kernel, see [Safe String Functions for Unicode and ANSI Characters](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_kernel/#safe-string-functions-for-unicode-and-ansi-characters) and [Safe String Functions for UNICODE_STRING Structures](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_kernel/#safe-string-functions-for-unicodestring-structures).

For more information about using safe strings, see [Using Safe String Functions](using-safe-string-functions.md).

Note that there is also a separate run-time library for general C programming in the kernel that has string functionality as well. For more information about the run-time library (RTL), see [Windows Kernel-Mode Run-Time Library](windows-kernel-mode-run-time-library.md). Note that even though both libraries are prefixed with "**Rtl**" they are not the same library.

 

 




