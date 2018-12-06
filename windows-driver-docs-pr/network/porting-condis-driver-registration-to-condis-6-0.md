---
title: Porting CoNDIS Driver Registration to CoNDIS 6.0
description: Porting CoNDIS Driver Registration to CoNDIS 6.0
ms.assetid: 2dea71a8-b48b-440e-a5de-9177865e7188
keywords:
- CoNDIS drivers WDK networking , registering CoNDIS drivers
- connection-oriented drivers WDK networking , registering
- registering CoNDIS drivers
- entry points WDK networking
- registration porting WDK CoNDIS
- porting CoNDIS drivers WDK networking , r
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS Driver Registration to CoNDIS 6.0





In NDIS 5.*x*, CoNDIS drivers register the primary *ProtocolXxx* and *MiniportXxx* functions during normal driver registration. To support CoNDIS, NDIS 6.0 drivers must register the CoNDIS function entry points by calling the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function. NDIS 6.0 protocol drivers must provide an [**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566817) structure, And NDIS 6.0 miniport drivers must provide an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565948) structure.

In NDIS 5.*x*, protocol drivers and miniport call managers (MCMs) register additional entry points when they register an address family (AF). In NDIS 6.0, drivers register these additional entry points by calling **NdisSetOptionalHandlers**.

This section includes the following topics:

[Porting CoNDIS Miniport Driver Registration](porting-condis-miniport-driver-registration.md)

[Porting CoNDIS Client Registration](porting-condis-client-registration.md)

[Porting CoNDIS Call Manager Registration](porting-condis-call-manager-registration.md)

[Porting CoNDIS MCM Registration](porting-condis-mcm-registration.md)

 

 





