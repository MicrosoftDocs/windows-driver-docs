---
title: Obtaining a PCMCIA_INTERFACE_STANDARD Interface
description: Obtaining a PCMCIA_INTERFACE_STANDARD Interface
ms.assetid: 475bf66a-5b6e-4a06-95f7-b7280dd7276d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining a PCMCIA\_INTERFACE\_STANDARD Interface





This section describes how a driver can obtain a PCMCIA\_INTERFACE\_STANDARD interface for a PCMCIA memory card from the PCMCIA bus driver.

A driver obtains a PCMCIA\_INTERFACE\_STANDARD interface by creating and sending an IRP\_MJ\_PNP request that specifies a [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) minor function code. The driver carries out the following operations:

-   Allocates and zero-fills a [PCMCIA\_INTERFACE\_STANDARD Interface Memory Card Routines](https://msdn.microsoft.com/library/windows/hardware/ff537607) structure in the paged memory pool.

-   Creates an IRP for the query interface request and gets the next stack location for the new IRP.

-   Sets the following members in the new stack location:
    -   The **Parameters.QueryInterface.Interface** member points to the driver-allocated PCMCIA\_INTERFACE\_STANDARD structure that was allocated by the driver.
    -   The **Parameters.QueryInterface.InterfaceType** member specifies a standard PCMCIA interface by the GUID value GUID\_PCMCIA\_INTERFACE\_STANDARD.
-   Sets a completion routine and sends the request down the driver stack.

If the request is successful, the PCMCIA bus driver fills in the PCMCIA\_INTERFACE\_STANDARD structure pointed to by **Parameters.QueryInterface.Interface**.

A driver must be running at IRQL &lt; DISPATCH\_LEVEL to send this request down the driver stack.

 

 





