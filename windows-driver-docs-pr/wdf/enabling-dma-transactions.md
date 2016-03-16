---
title: Enabling DMA Transactions
description: Enabling DMA Transactions
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 87735776-c371-425b-bc53-0c68375c9562
keywords: ["DMA transactions WDK KMDF enabling", "DMA operations WDK KMDF transactions", "bus master DMA WDK KMDF transactions"]
---

# Enabling DMA Transactions


\[Applies to KMDF only\]

## <a href="" id="ddk-enabling-dma-transactions-df"></a>


If your framework-based driver handles I/O operations for DMA devices, your driver must enable the framework's DMA features for each DMA device. To enable these features, your driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) or [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function must:

1.  Call [**WdfDeviceSetAlignmentRequirement**](https://msdn.microsoft.com/library/windows/hardware/ff546861) to specify the device's requirement for buffer alignment.

2.  Call [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983) to specify the type of DMA operations (single packet or scatter/gather) and the maximum transfer size that the device supports. Starting in KMDF version 1.11, the framework supports [system-mode DMA](supporting-system-mode-dma.md) on System on a Chip (SoC)–based systems running on Windows 8 or later versions of the operating system.

3.  Call [**WdfDmaEnablerSetMaximumScatterGatherElements**](https://msdn.microsoft.com/library/windows/hardware/ff547014) to specify the maximum number of elements that the device can support in a scatter/gather list, if the device supports scatter/gather operations.

The following code example from the [PLX9x5x](http://go.microsoft.com/fwlink/p/?linkid=256157) sample illustrates how to enable the framework's DMA features. This code appears in the *Init.c file*.

```
WDF_DMA_ENABLER_CONFIG   dmaConfig;

WdfDeviceSetAlignmentRequirement( DevExt->Device, PCI9656_DTE_ALIGNMENT_16 );
WDF_DMA_ENABLER_CONFIG_INIT( &amp;dmaConfig,
                             WdfDmaProfileScatterGather64Duplex,
                             DevExt->MaximumTransferLength );
status = WdfDmaEnablerCreate( DevExt->Device,
                              &amp;dmaConfig, 
                              WDF_NO_OBJECT_ATTRIBUTES,
                              &amp;DevExt->DmaEnabler );

```

If your driver requires common buffers, the driver's *EvtDriverDeviceAdd* callback function typically sets them up. For more information about these buffers, see [Using Common Buffers](using-common-buffers.md).

After a driver has called **WdfDmaEnablerCreate**, it can call [**WdfDmaEnablerWdmGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff547020) to obtain pointers to WDM [**DMA\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff544062) structures that the framework creates for the device's input and output directions. However, most framework-based drivers do not need to access these structures.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Enabling%20DMA%20Transactions%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




