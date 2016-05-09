---
title: Unsynchronized IdeHwBuildIo Routine
description: Unsynchronized IdeHwBuildIo Routine
ms.assetid: 47e32f05-5c89-4423-b515-c774b94a9b84
keywords: ["ATA Port drivers WDK , synchronization", "synchronization WDK ATA Port driver", "AtaHwBuildIo", "unsynchronized processing WDK ATA Port driver"]
---

# Unsynchronized IdeHwBuildIo Routine


## <span id="ddk_unsynchronized_atahwbuildio_routine_kg"></span><span id="DDK_UNSYNCHRONIZED_ATAHWBUILDIO_ROUTINE_KG"></span>


The ATA port driver raises the IRQL of the processor to DISPATCH\_LEVEL or above before it calls the ATA miniport driver's start I/O routine, [**IdeHwStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff559003). The ATA port driver raises the IRQL of the processor to mask out interrupts and to guarantee that the start I/O routine and the interrupt handler synchronize access to critical operating system structures. To reduce the time that the miniport driver spends in the start I/O routine at an IRQL &gt;= DISPATCH\_LEVEL, the miniport driver provides the [**IdeHwBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557462) routine. The ATA port driver calls *IdeHwBuildIo* at IRQL &lt;= DISPATCH\_LEVEL, so that the miniport driver can preprocess as much of the I/O request as possible at the lower IRQL and avoid monopolizing control of the processor.

The Storport I/O model uses a similar technique to minimize the time that is spent in its start I/O routine. For more information about how the Storport driver uses [**HwStorBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557369), see the [Unsynchronized HwStorBuildIo Routine](unsynchronized-hwstorbuildio-routine.md).

All processing of an I/O request that requires access to critical system structures, such as the device extension, should be done within the [**IdeHwStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff559003) routine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Unsynchronized%20IdeHwBuildIo%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




