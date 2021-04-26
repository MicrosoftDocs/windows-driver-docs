---
title: Closing an Address Family Overview
description: Closing an Address Family Overview
keywords:
- address families WDK networking
- AFs WDK networking
- closing address families
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing an Address Family Overview

A connection-oriented client calls [**NdisClCloseAddressFamily**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclcloseaddressfamily) to delete the association between itself, a call manager, and a particular underlying NIC.

When a CoNDIS stand-alone call manager is closing a binding to an underlying miniport adapter, or a miniport call manager (MCM) is halting a miniport adapter, the call manager or the MCM must notify NDIS if an associated address family (AF) should be closed. NDIS then notifies each CoNDIS client that has the AF open that the client should close the AF.

This section includes the following topics:

[Closing a CoNDIS Call Manager or MCM](closing-a-condis-call-manager-or-mcm.md)

[Closing an Address Family in a CoNDIS Client](closing-an-address-family-in-a-condis-client.md)

 

