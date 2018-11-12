---
title: Implementation Tips and Requirements for WDM Lower Edge
description: Implementation Tips and Requirements for WDM Lower Edge
ms.assetid: 760c62ec-eeca-4b62-97ec-7cda5ee353a8
keywords:
- NDIS-WDM miniport drivers WDK networking , implemention tips
- lower edge of NDIS miniport drivers WDK networking , driver implemention
- WDM lower edge WDK networking , driver implemention
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementation Tips and Requirements for WDM Lower Edge





This topic describes tips and requirements for implementing an NDIS-WDM miniport driver. An NDIS-WDM miniport driver can call both NDIS and non-NDIS functions. These non-NDIS functions include, for example, WDM-kernel-mode support routines and functions for a particular bus-driver interface.

When implementing an NDIS-WDM miniport driver, keep the following in mind:

-   Building an NDIS-WDM miniport driver requires that the NDIS\_WDM flag is defined before the Ndis.h header file is included. Defining the NDIS\_WDM flag ensures that Ndis.h automatically includes the appropriate WDM header file. The NDIS\_WDM flag should be either embedded at the start of the miniport driver's source code or set in the miniport driver's Sources file. An NDIS-WDM miniport driver requires a WDM header file to call kernel-mode routines such as [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) and [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257).

-   Function calls for a particular bus-driver interface require the header files for that bus driver.

-   Including NDIS and non-NDIS headers in the same source file is not recommended because they might not be compatible. That is, separate source files should be created for code that calls NDIS functions and for code that calls non-NDIS functions.

-   An NDIS-WDM miniport driver should call appropriate NDIS functions to allocate and release resources unless the NDIS-WDM miniport driver allocates and releases resources in one of the following scenarios:

    -   A resource, typically a memory resource, is allocated by the NDIS-WDM miniport driver and is later released by a non-NDIS entity such as a bus-driver interface,
    -   A resource, typically a memory resource, is allocated by a non-NDIS entity and is later released by the NDIS-WDM miniport driver.

    For the preceding scenarios, the NDIS-WDM miniport driver should call the appropriate WDM routines to allocate or release resources for the non-NDIS entity.

 

 





