---
title: Using Common Buffers
description: Using Common Buffers
ms.assetid: 81a56f62-917e-4798-b2cc-6469c802fab8
keywords: ["DMA operations WDK KMDF , common buffers", "bus-master DMA WDK KMDF , common buffers", "common buffers WDK KMDF", "buffers WDK KMDF"]
---

# Using Common Buffers


\[Applies to KMDF only\]

## <a href="" id="ddk-using-common-buffers-df"></a>


Drivers for DMA devices sometimes must allocate buffer space that both a device and the driver can access. For example, a device might write transfer information, such as byte counts, into this buffer space and the driver can read it to determine the number of bytes that were transferred. This type of buffer space is called a *common buffer*.

To allocate a common buffer, your driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function:

-   Calls [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983) to create a DMA enabler object.

-   Calls [**WdfCommonBufferCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545800) or [**WdfCommonBufferCreateWithConfig**](https://msdn.microsoft.com/library/windows/hardware/ff545805) to create the buffer.

-   Calls [**WdfCommonBufferGetAlignedLogicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff545814) to obtain the buffer's logical address, which the device can access.

-   Calls [**WdfCommonBufferGetAlignedVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff545820) to obtain the buffer's virtual address, which the driver can access.

The following code example is taken from the *Init.c* file of the [PLX9x5x](http://go.microsoft.com/fwlink/p/?linkid=256157) sample. This code shows how a KMDF driver allocates common buffer space.

```
// Allocate common buffer for building writes
DevExt->WriteCommonBufferSize = 
         sizeof( DMA_TRANSFER_ELEMENT) * DevExt->WriteTransferElements;
status = WdfCommonBufferCreate( DevExt->DmaEnabler,
                                DevExt->WriteCommonBufferSize,
                                WDF_NO_OBJECT_ATTRIBUTES, 
                                &amp;DevExt->WriteCommonBuffer );
if (!NT_SUCCESS(status)) {
    . . . //Error-handling code omitted 
    }
DevExt->WriteCommonBufferBase = 
             WdfCommonBufferGetAlignedVirtualAddress(
                      DevExt->WriteCommonBuffer);
DevExt->WriteCommonBufferBaseLA = 
             WdfCommonBufferGetAlignedLogicalAddress(
                      DevExt->WriteCommonBuffer);
RtlZeroMemory( DevExt->WriteCommonBufferBase, DevExt->WriteCommonBufferSize);

```

If your driver calls [**WdfDeviceSetAlignmentRequirement**](https://msdn.microsoft.com/library/windows/hardware/ff546861) before calling [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983), the buffers that **WdfDmaEnablerCreate** creates are aligned to the memory address boundary that the driver specified to **WdfDeviceSetAlignmentRequirement**. Otherwise, common buffers are aligned to word address boundaries. Alternatively, the driver can call [**WdfCommonBufferCreateWithConfig**](https://msdn.microsoft.com/library/windows/hardware/ff545805) to specify an alignment for a single buffer.

To obtain the length of a common buffer that your driver has allocated, the driver can call [**WdfCommonBufferGetLength**](https://msdn.microsoft.com/library/windows/hardware/ff545828).

When the driver is finished using a common buffer, the driver calls [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20Common%20Buffers%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




