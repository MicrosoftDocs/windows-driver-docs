---
title: Registering the WAN Address Family
description: Registering the WAN Address Family
ms.assetid: 31443e99-24d8-4276-8345-004b0eeb05d7
keywords:
- CoNDIS WAN drivers WDK networking , TAPI address family
- NdisCmRegisterAddressFamilyEx
- TAPI WDK networking
- registering WAN address family
- WAN address family WDK networking
- address families WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering the WAN Address Family





This topic describes how to register the TAPI address family from a CoNDIS WAN miniport call manager (MCM) or a separate call manager.

Either type of call manager calls the [**NdisCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff561685) function to register its call manager entry points and the address family type CO\_ADDRESS\_FAMILY\_TAPI\_PROXY. By doing so, the driver indicates that it provides TAPI services. For more information about registering an address family in a CoNDIS driver, see [Registering and Opening an Address Family](registering-and-opening-an-address-family.md).

NDIS notifies NDPROXY of the newly-registered address family. NDPROXY determines that it can use the TAPI services that the call manager provides. NDPROXY opens the TAPI-proxy address family that is associated with the driver and registers NDPROXY's connection-oriented entry points with NDIS. These entry points are used to communicate with the driver.

NDPROXY can enumerate the TAPI capabilities of the miniport driver and later send TAPI requests that are encapsulated in NDIS structures. For details about using CoNDIS extensions for TAPI support, see [CoNDIS WAN Operations That Support Telephonic Services](condis-wan-operations-that-support-telephonic-services.md).

 

 





