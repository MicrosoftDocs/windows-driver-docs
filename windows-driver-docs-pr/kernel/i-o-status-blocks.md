---
title: I/O Status Blocks
description: I/O Status Blocks
keywords: ["IRPs WDK kernel , I/O status blocks", "I/O status blocks WDK kernel", "status blocks WDK kernel", "IO_STATUS_BLOCK structure", "status information WDK IRPs", "IRPs WDK kernel , status information"]
ms.date: 06/16/2017
---

# I/O Status Blocks





An I/O status block, which consists of an [**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure, is a part of each [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp). An I/O status block serves two purposes:

-   It provides a higher-level driver's [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine a way of determining whether the service worked when the IRP is completed.

-   It provides more information about why the service either worked or did not work.

Upon completion of an IRP, the **Status** field indicates whether the drivers that processed the IRP actually satisfied the request or failed the IRP with an error status. The **Information** field supplies the caller with more information about what actually occurred. For example, it contains the number of bytes actually transferred after a read or write operation.

For more information, see [Setting the I/O Status Block in an IRP](processing-irps-in-a-lowest-level-driver.md#ddk-setting-the-i-o-status-block-in-an-irp-kg).

 

