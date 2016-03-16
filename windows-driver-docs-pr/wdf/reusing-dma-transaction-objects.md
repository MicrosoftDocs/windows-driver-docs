---
title: Reusing DMA Transaction Objects
description: Reusing DMA Transaction Objects
ms.assetid: 4adb8653-48b6-4e22-aba3-b909c95b8d15
keywords: ["DMA transactions WDK KMDF reusing transaction objects", "DMA operations WDK KMDF transactions", "bus master DMA WDK KMDF transactions", "reusing DMA transaction objects WDK KMDF"]
---

# Reusing DMA Transaction Objects


\[Applies to KMDF only\]

## <a href="" id="ddk-reusing-dma-transaction-objects-df"></a>


After a driver processes all of the DMA transfers that are associated with a DMA transaction, the driver can delete or reuse the transaction object. Typically, the driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function deletes the transaction object (by calling [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)). Subsequently, when the driver creates a new DMA transaction, it calls [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027) to create a new transaction object.

However, sometimes it is beneficial for the driver to reuse transaction objects. In such cases, the driver calls [**WdfDmaTransactionRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547114) instead of [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734).

For example, suppose your driver and device must operate when computer memory resources are low. To handle this memory issue, your driver can use the following procedure:

1.  The driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function can call [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027) to create one or more transaction objects. The driver saves the handles to these transaction objects.

2.  Each time the driver is ready to create and initialize a new transaction, it calls [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027). If this method returns STATUS\_INSUFFICIENT\_RESOURCES, the driver can use one of the stored transaction objects.

3.  If the driver uses one of its stored transaction objects, it should reuse the transaction object, instead of deleting it, when the transaction is completed. The driver sets up the transaction object for re-use by calling [**WdfDmaTransactionRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547114) instead of [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734).

The [PLX9x5x](sample-kmdf-drivers.md) sample reuses DMA transaction objects.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Reusing%20DMA%20Transaction%20Objects%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




