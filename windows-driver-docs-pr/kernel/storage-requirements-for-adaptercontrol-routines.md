---
title: Storage Requirements for AdapterControl Routines
description: Storage Requirements for AdapterControl Routines
keywords: ["AdapterControl routines, storage", "AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines", "storage WDK DMA"]
ms.date: 06/16/2017
---

# Storage Requirements for AdapterControl Routines





If it has an [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine, a driver must provide resident storage for the following:

-   Context information to be used in its DMA operations

-   An adapter object pointer returned by [**IoGetDmaAdapter**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdmaadapter)

-   A ULONG-type variable to hold the system-determined maximum *NumberOfMapRegisters* available for any given DMA transfer request

The driver can provide the necessary storage in a device extension, in a controller extension, or in nonpaged pool allocated by the driver.

 

