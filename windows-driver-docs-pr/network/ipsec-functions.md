---
title: IPsec functions
description: This section describes IPsec functions for Windows Filtering Platform callout drivers.
keywords:
- IPsec functions network drivers
ms.date: 11/07/2017
---

# IPsec functions

The semantics of the following functions are exactly the same when called from a callout driver as when called from a user-mode application except that the return type is an NTSTATUS code instead of a Win32 error code. For a description of each of these functions, see the [Windows Filtering Platform](/windows/win32/fwp/windows-filtering-platform-start-page).

Callers of these functions must be running at IRQL = PASSIVE_LEVEL.

- FwpmIPsecTunnelAdd0
- FwpmIPsecTunnelDeleteByKey0
- IPsecGetStatistics0
- IPsecSaContextAddInbound0
- IPsecSaContextAddOutbound0
- IPsecSaContextCreate0
- IPsecSaContextCreateEnumHandle0
- IPsecSaContextDeleteById0
- IPsecSaContextDestroyEnumHandle0
- IPsecSaContextEnum0
- IPsecSaContextExpire0
- IPsecSaContextGetById0
- IPsecSaContextGetSpi0
- IPsecSaCreateEnumHandle0
- IPsecSaDbGetSecurityInfo0
- IPsecSaDbSetSecurityInfo0
- IPsecSaDestroyEnumHandle0
- IPsecSaEnum0
