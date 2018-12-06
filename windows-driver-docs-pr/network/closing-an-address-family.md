---
title: Closing an Address Family
description: Closing an Address Family
ms.assetid: 0533bc31-dd4c-42c4-8170-8201e32e1026
keywords:
- address families WDK networking
- AFs WDK networking
- closing address families
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing an Address Family





A connection-oriented client calls [**NdisClCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff561626) to delete the association between itself, a call manager, and a particular underlying NIC.

When a CoNDIS stand-alone call manager is closing a binding to an underlying miniport adapter, or a miniport call manager (MCM) is halting a miniport adapter, the call manager or the MCM must notify NDIS if an associated address family (AF) should be closed. NDIS then notifies each CoNDIS client that has the AF open that the client should close the AF.

This section includes the following topics:

[Closing a CoNDIS Call Manager or MCM](closing-a-condis-call-manager-or-mcm.md)

[Closing an Address Family in a CoNDIS Client](closing-an-address-family-in-a-condis-client.md)

 

 





