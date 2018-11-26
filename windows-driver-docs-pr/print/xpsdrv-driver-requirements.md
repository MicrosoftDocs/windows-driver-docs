---
title: XPSDrv Driver Requirements
description: XPSDrv Driver Requirements
ms.assetid: 382b53eb-a69a-452a-8403-876640a9129e
keywords:
- Version 3 XPS drivers WDK XPSDrv , requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XPSDrv Driver Requirements


For in-box and the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), the XPSDrv configuration module must meet the following requirements:

-   The XPSDrv printer driver must implement a Version 3 print driver configuration module.

-   The configuration module must support all PrintTicket and PrintCapabilities functionality. The Windows Vista version of the Unidrv and Pscript5 printer drivers provide this support automatically. For more information about how to add this support to monolithic, GDI-based version 3 printer drivers, see [Adding Print Ticket Support to Monolithic Print Drivers](adding-print-ticket-support-to-monolithic-print-drivers.md).

For the complete list of configuration module requirements, see [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613).

 

 




