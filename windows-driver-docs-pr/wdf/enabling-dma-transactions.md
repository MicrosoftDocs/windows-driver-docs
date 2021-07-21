---
title: Enabling DMA Transactions
description: Enabling DMA Transactions
keywords:
- DMA transactions WDK KMDF , enabling
- DMA operations WDK KMDF , transactions
- bus-master DMA WDK KMDF , transactions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling DMA Transactions


\[Applies to KMDF only\]




If your framework-based driver handles I/O operations for DMA devices, your driver must enable the framework's DMA features for each DMA device. To enable these features, your driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) or [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function must:

1.  Call [**WdfDeviceSetAlignmentRequirement**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetalignmentrequirement) to specify the device's requirement for buffer alignment.

2.  Call [**WdfDmaEnablerCreate**](/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablercreate) to specify the type of DMA operations (single packet or scatter/gather) and the maximum transfer size that the device supports. Starting in KMDF version 1.11, the framework supports [system-mode DMA](supporting-system-mode-dma.md) on System on a Chip (SoC)–based systems running on Windows 8 or later versions of the operating system.

3.  Call [**WdfDmaEnablerSetMaximumScatterGatherElements**](/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablersetmaximumscattergatherelements) to specify the maximum number of elements that the device can support in a scatter/gather list, if the device supports scatter/gather operations.

The following code example from the [PLX9x5x](/samples/browse/) sample illustrates how to enable the framework's DMA features. This code appears in the *Init.c file*.

```cpp
WDF_DMA_ENABLER_CONFIG   dmaConfig;

WdfDeviceSetAlignmentRequirement( DevExt->Device, PCI9656_DTE_ALIGNMENT_16 );
WDF_DMA_ENABLER_CONFIG_INIT( &dmaConfig,
                             WdfDmaProfileScatterGather64Duplex,
                             DevExt->MaximumTransferLength );
status = WdfDmaEnablerCreate( DevExt->Device,
                              &dmaConfig, 
                              WDF_NO_OBJECT_ATTRIBUTES,
                              &DevExt->DmaEnabler );
```

If your driver requires common buffers, the driver's *EvtDriverDeviceAdd* callback function typically sets them up. For more information about these buffers, see [Using Common Buffers](using-common-buffers.md).

After a driver has called **WdfDmaEnablerCreate**, it can call [**WdfDmaEnablerWdmGetDmaAdapter**](/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablerwdmgetdmaadapter) to obtain pointers to WDM [**DMA\_ADAPTER**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_dma_adapter) structures that the framework creates for the device's input and output directions. However, most framework-based drivers do not need to access these structures.
