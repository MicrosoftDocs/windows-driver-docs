---
title: Handling an OID_PNP_QUERY_POWER OID
description: Handling an OID_PNP_QUERY_POWER OID
keywords:
- OID_PNP_QUERY_POWER
- network interface cards WDK networking , transitioning power states
- NICs WDK networking , transitioning power states
- power management WDK NDIS miniport , transitioning power states
- device power states WDK networking
- power states WDK networking
- transitioning power states WDK networking
ms.date: 04/20/2017
---

# Handling an OID\_PNP\_QUERY\_POWER OID





The [OID\_PNP\_QUERY\_POWER](./oid-pnp-query-power.md) OID requests a miniport driver to indicate whether it can transition a network adapter to a low-power state. A miniport driver must always return NDIS\_STATUS\_SUCCESS in response to a query of OID\_PNP\_QUERY\_POWER. By returning NDIS\_STATUS\_SUCCESS to this OID request, the miniport driver guarantees that it will transition the network adapter to the specified device power state on receipt of a subsequent [OID\_PNP\_SET\_POWER](./oid-pnp-set-power.md) request. The miniport driver, in this case, must do nothing to jeopardize the transition.

An [OID\_PNP\_QUERY\_POWER](./oid-pnp-query-power.md) request is always followed by an OID\_PNP\_SET\_POWER request. The [OID\_PNP\_SET\_POWER](./oid-pnp-set-power.md) request can immediately follow the OID\_PNP\_QUERY\_POWER request or can arrive at an unspecified interval after the OID\_PNP\_QUERY\_POWER request. A device state of D0, which is specified in the OID\_PNP\_SET\_POWER request, effectively cancels a preceding OID\_PNP\_QUERY\_POWER request.

 

