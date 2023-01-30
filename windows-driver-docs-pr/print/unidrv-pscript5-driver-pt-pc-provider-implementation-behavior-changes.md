---
title: Unidrv/PScript5 driver PT/PC provider implementation behavior
description: Unidrv and PScript5 driver PrintTicket or print provider (PT/PC) implementation behavior changes
ms.date: 01/30/2023
---

# Unidrv/PScript5 driver PT/PC provider implementation behavior changes

[!include[Print Support Apps](../includes/print-support-apps.md)]

When running in XPSDrv mode, a Unidrv or PScript5 driver's PrintTicket or print provider (PT/PC) implementation must also disable any Unidrv/PScript5 hard-coded features.

The PrintCapabilities XML should not contain any hard-coded capability, and the default PrintTicket or validated PrintTicket should not contain any hardcoded features.
