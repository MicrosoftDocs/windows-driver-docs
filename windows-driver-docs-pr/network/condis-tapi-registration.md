---
title: CoNDIS TAPI Registration
description: CoNDIS TAPI Registration
keywords:
- CoNDIS WAN drivers WDK networking , TAPI services
- telephonic services WDK WAN , registering
- CoNDIS TAPI WDK networking , registering
- registering CoNDIS TAPI
ms.date: 03/02/2023
---

# CoNDIS TAPI Registration





This section discusses how a CoNDIS WAN miniport driver indicates that it supports TAPI services and how it sets up TAPI-specific communications with the NDISWAN and NDPROXY drivers.

After a CoNDIS WAN miniport driver has registered its miniport driver entry points for one or more NICs, the following operations cause the NDISWAN and NDPROXY drivers to become associated, in a TAPI-specific way, with those NICs.

-   The CoNDIS WAN miniport driver calls the [**NdisMCmRegisterAddressFamilyEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmregisteraddressfamilyex) function from within its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function to register its call manager entry points and the address family type CO\_ADDRESS\_FAMILY\_TAPI\_PROXY. By doing so, the miniport driver advertises that it provides TAPI services.

-   NDIS calls NDPROXY's [**ProtocolCoAfRegisterNotify**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_af_register_notify) function to notify NDPROXY of the newly registered address family. NDPROXY's *ProtocolCoAfRegisterNotify* examines the address-family data and determines that it can use the TAPI services provided by the call manager that is integrated into the CoNDIS WAN miniport driver. A TAPI-capable CoNDIS WAN miniport driver is an integrated miniport call manager (MCM) driver.

-   NDPROXY calls the [**NdisClOpenAddressFamilyEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclopenaddressfamilyex) function to open the TAPI-proxy address family that is associated with the CoNDIS WAN miniport driver. **NdisClOpenAddressFamilyEx** registers NDPROXY's connection-oriented entry points with NDIS. These entry points are used to communicate with a TAPI-capable CoNDIS WAN miniport driver.

-   NDPROXY calls [**NdisCmRegisterAddressFamilyEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmregisteraddressfamilyex) to register its call manager entry points and the address family type CO\_ADDRESS\_FAMILY\_TAPI. By doing so, NDPROXY advertises that it implements TAPI services.

-   NDIS calls NDISWAN's *ProtocolCoAfRegisterNotify* function to notify NDISWAN of the newly registered address family. NDISWAN's *ProtocolCoAfRegisterNotify* examines the address-family data and determines that NDISWAN can use the TAPI services provided by NDPROXY.

-   NDISWAN calls the **NdisClOpenAddressFamilyEx** function to open the TAPI address family that is associated with NDPROXY. **NdisClOpenAddressFamilyEx** registers NDISWAN's connection-oriented entry points with NDIS. These entry points are used to communicate with NDPROXY.

-   NDISWAN calls the [**NdisClRegisterSap**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclregistersap) function to inform NDPROXY that NDISWAN can accept incoming calls on a particular Service Access Point (SAP). In this call, NDISWAN passes a [**CO\_SAP**](/previous-versions/windows/hardware/network/ff545392(v=vs.85)) structure that describes the SAP. NDISWAN sets the **SapType** member of CO\_SAP to AF\_TAPI\_SAP\_TYPE to specify that the SAP will be used for TAPI calls. NDISWAN sets the **Sap** member of CO\_SAP to a string for a particular TAPI device class. A TAPI application provides this string when the application calls the TAPI **lineGetID** function. NDPROXY should notify NDISWAN about all incoming calls addressed to the SAP.

 

