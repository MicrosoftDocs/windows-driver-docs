---
title: Obtaining a PCMCIA_INTERFACE_STANDARD Interface
description: Obtaining a PCMCIA_INTERFACE_STANDARD Interface
ms.date: 03/03/2023
---

# Obtaining a PCMCIA\_INTERFACE\_STANDARD Interface





This section describes how a driver can obtain a PCMCIA\_INTERFACE\_STANDARD interface for a PCMCIA memory card from the PCMCIA bus driver.

A driver obtains a PCMCIA\_INTERFACE\_STANDARD interface by creating and sending an IRP\_MJ\_PNP request that specifies a [**IRP\_MN\_QUERY\_INTERFACE**](../kernel/irp-mn-query-interface.md) minor function code. The driver carries out the following operations:

-   Allocates and zero-fills a [PCMCIA\_INTERFACE\_STANDARD Interface Memory Card Routines](/windows-hardware/drivers/ddi/index) structure in the paged memory pool.

-   Creates an IRP for the query interface request and gets the next stack location for the new IRP.

-   Sets the following members in the new stack location:
    -   The **Parameters.QueryInterface.Interface** member points to the driver-allocated PCMCIA\_INTERFACE\_STANDARD structure that was allocated by the driver.
    -   The **Parameters.QueryInterface.InterfaceType** member specifies a standard PCMCIA interface by the GUID value GUID\_PCMCIA\_INTERFACE\_STANDARD.
-   Sets a completion routine and sends the request down the driver stack.

If the request is successful, the PCMCIA bus driver fills in the PCMCIA\_INTERFACE\_STANDARD structure pointed to by **Parameters.QueryInterface.Interface**.

A driver must be running at IRQL &lt; DISPATCH\_LEVEL to send this request down the driver stack.

 

