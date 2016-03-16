---
title: Handling DMA Operations in KMDF Drivers
description: This section describes how a Kernel Mode Driver Framework (KMDF) driver converts I/O requests into direct memory access (DMA) operations. KMDF supports bus master and system mode DMA.
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 1ca8ba66-201d-42f2-a6f1-6184a9d7c2a6
keywords: ["kernel mode drivers WDK KMDF DMA operations", "KMDF WDK DMA operations", "Kernel Mode Driver Framework WDK DMA operations", "framework based drivers WDK KMDF DMA operations", "DMA operations WDK KMDF", "bus master DMA WDK KMDF", "Direct Memory Access WDK KMDF"]
---

# Handling DMA Operations in KMDF Drivers


\[Applies to KMDF only\]

This section describes how a Kernel-Mode Driver Framework (KMDF) driver converts I/O requests into direct memory access (DMA) operations. KMDF supports bus-master and system-mode DMA.

## <a href="" id="ddk-handling-dma-operations-in-framework-based-drivers-df"></a>


## In this section


-   [Introduction to DMA in Windows Driver Framework](introduction-to-dma-in-windows-driver-framework.md)
-   [Framework DMA Objects](framework-dma-objects.md)
-   [DMA Transactions and DMA Transfers](dma-transactions-and-dma-transfers.md)
-   [Sample Drivers That Use Framework DMA](sample-drivers-that-use-framework-dma.md)
-   [Handling I/O Requests in a KMDF Driver for a Bus-Master DMA Device](handling-i-o-requests-in-a-kmdf-driver-for-a-bus-master-dma-device.md)
-   [Supporting System-Mode DMA](supporting-system-mode-dma.md)
-   [Canceling DMA Transactions](canceling-dma-transactions.md)
-   [Reserving DMA Resources](reserving-dma-resources.md)
-   [Testing DMA in KMDF Drivers](testing-dma-in-kmdf-drivers.md)

For information on how support DMA operations in WDM drivers, see [DMA Programming Techniques](https://msdn.microsoft.com/library/windows/hardware/ff544074).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20DMA%20Operations%20in%20KMDF%20Drivers%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




