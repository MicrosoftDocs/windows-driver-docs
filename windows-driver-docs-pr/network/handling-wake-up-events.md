---
title: Handling Wake-Up Events
description: Handling Wake-Up Events
keywords:
- wake-up capabilities WDK networking , handling wake-up events
- bus-specific wake-up lines WDK networking
ms.date: 04/20/2017
---

# Handling Wake-Up Events





A miniport driver does not handle a wake-up event detected by a NIC. When a NIC detects an enabled wake-up event, it asserts a bus-specific wake-up line. The power manager then sends a power IRP to NDIS, which, in response, sends the miniport driver an [OID\_PNP\_SET\_POWER](./oid-pnp-set-power.md) OID that requests the miniport driver to put a NIC in the highest-powered (D0) state.

 

