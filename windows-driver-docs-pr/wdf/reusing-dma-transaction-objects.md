---
title: Reusing DMA Transaction Objects
description: Reusing DMA Transaction Objects
ms.assetid: 4adb8653-48b6-4e22-aba3-b909c95b8d15
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




After a driver processes all of the DMA transfers that are associated with a DMA transaction, the driver can delete or reuse the transaction object. Typically, the driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function deletes the transaction object (by calling [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)). Subsequently, when the driver creates a new DMA transaction, it calls [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027) to create a new transaction object.

However, sometimes it is beneficial for the driver to reuse transaction objects. In such cases, the driver calls [**WdfDmaTransactionRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547114) instead of [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734).

For example, suppose your driver and device must operate when computer memory resources are low. To handle this memory issue, your driver can use the following procedure:

1.  The driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function can call [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027) to create one or more transaction objects. The driver saves the handles to these transaction objects.

2.  Each time the driver is ready to create and initialize a new transaction, it calls [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027). If this method returns STATUS\_INSUFFICIENT\_RESOURCES, the driver can use one of the stored transaction objects.

3.  If the driver uses one of its stored transaction objects, it should reuse the transaction object, instead of deleting it, when the transaction is completed. The driver sets up the transaction object for re-use by calling [**WdfDmaTransactionRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547114) instead of [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734).

The [PLX9x5x](sample-kmdf-drivers.md) sample reuses DMA transaction objects.

 

 





