---
title: Freeing an NDIS Port
description: Freeing an NDIS Port
keywords:
- ports WDK NDIS , freeing
- NDIS ports WDK , freeing
- freeing NDIS ports
ms.date: 03/02/2023
---

# Freeing an NDIS Port





Your miniport driver must free all NDIS ports that it [allocates](allocating-an-ndis-port.md) for miniport adapters in its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. It can free a port any time by calling [**NdisMFreePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreeport), except for the two cases noted below.

Your miniport driver must free all allocated ports in these cases:

-   If your driver’s [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function fails, it must free all allocated ports.
-   If a miniport adapter is halted, your driver’s [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function must free all allocated ports.

Your miniport driver cannot simply call [**NdisMFreePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreeport) in these cases:

-   If the port is the default port, NDIS frees it automatically, so your miniport driver must not free it. If you try to free the [default port](default-ndis-port.md), [**NdisMFreePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreeport) returns an NDIS\_STATUS\_INVALID\_PORT error.
-   If the port is active, your miniport driver will need to deactivate it before calling [**NdisMFreePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreeport).

## Related topics


[Allocating NDIS Ports](allocating-an-ndis-port.md)

[Deactivating NDIS Ports](deactivating-an-ndis-port.md)

[Default NDIS Port](default-ndis-port.md)

 

