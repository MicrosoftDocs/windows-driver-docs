---
title: IPsec functions
description: This section describes IPsec functions for Windows Filtering Platform callout drivers.
ms.assetid: c457f036-84be-47fd-8cfe-9ac867111ca5
keywords:
- IPsec functions network drivers
ms.date: 11/07/2017
ms.localizationpriority: medium
---

# IPsec functions

The semantics of the following functions are exactly the same when called from a callout driver as when called from a user-mode application except that the return type is an NTSTATUS code instead of a Win32 error code. For a description of each of these functions, see the [Windows Filtering Platform](http://go.microsoft.com/fwlink/p/?linkid=210226) section in the Microsoft Windows SDK documentation.

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

