---
title: Reusing DMA Transaction Objects
description: Reusing DMA Transaction Objects
keywords:
- DMA transactions WDK KMDF , reusing transaction objects
- DMA operations WDK KMDF , transactions
- bus-master DMA WDK KMDF , transactions
- reusing DMA transaction objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reusing DMA Transaction Objects


\[Applies to KMDF only\]




After a driver processes all of the DMA transfers that are associated with a DMA transaction, the driver can delete or reuse the transaction object. Typically, the driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function deletes the transaction object (by calling [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete)). Subsequently, when the driver creates a new DMA transaction, it calls [**WdfDmaTransactionCreate**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncreate) to create a new transaction object.

However, sometimes it is beneficial for the driver to reuse transaction objects. In such cases, the driver calls [**WdfDmaTransactionRelease**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionrelease) instead of [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

For example, suppose your driver and device must operate when computer memory resources are low. To handle this memory issue, your driver can use the following procedure:

1.  The driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function can call [**WdfDmaTransactionCreate**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncreate) to create one or more transaction objects. The driver saves the handles to these transaction objects.

2.  Each time the driver is ready to create and initialize a new transaction, it calls [**WdfDmaTransactionCreate**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncreate). If this method returns STATUS\_INSUFFICIENT\_RESOURCES, the driver can use one of the stored transaction objects.

3.  If the driver uses one of its stored transaction objects, it should reuse the transaction object, instead of deleting it, when the transaction is completed. The driver sets up the transaction object for re-use by calling [**WdfDmaTransactionRelease**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionrelease) instead of [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

The [PLX9x5x](sample-kmdf-drivers.md) sample reuses DMA transaction objects.

 

