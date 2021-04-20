---
title: Internet Key Exchange functions
description: This section describes Internet Key Exchange functions.
keywords:
- Internet Key Exchange functions network drivers
ms.date: 11/07/2017
ms.localizationpriority: medium
---

# Internet Key Exchange functions

The semantics of the following functions are exactly the same when called from a callout driver as when called from a user-mode application except that the return type is an NTSTATUS code instead of a Win32 error code. For a description of each of these functions, see the [Windows Filtering Platform](/windows/win32/fwp/windows-filtering-platform-start-page) section in the Microsoft Windows SDK documentation.

Callers of these functions must be running at IRQL = PASSIVE_LEVEL.

- IkeextGetStatistics0
- IkeextSaCreateEnumHandle0
- IkeextSaDbGetSecurityInfo0
- IkeextSaDbSetSecurityInfo0
- IkeextSaDeleteById0
- IkeextSaDestroyEnumHandle0
- IkeextSaEnum0
- IkeextSaGetById0
