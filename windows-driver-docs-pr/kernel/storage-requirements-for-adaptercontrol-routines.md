---
title: Storage Requirements for AdapterControl Routines
description: Storage Requirements for AdapterControl Routines
ms.assetid: 5e5711df-9acd-4ac5-b6b2-4e90299afb24
keywords: ["AdapterControl routines, storage", "AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines", "storage WDK DMA"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Storage Requirements for AdapterControl Routines





If it has an [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine, a driver must provide resident storage for the following:

-   Context information to be used in its DMA operations

-   An adapter object pointer returned by [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220)

-   A ULONG-type variable to hold the system-determined maximum *NumberOfMapRegisters* available for any given DMA transfer request

The driver can provide the necessary storage in a device extension, in a controller extension, or in nonpaged pool allocated by the driver.

 

 




