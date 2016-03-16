---
title: Testing DMA in KMDF Drivers
description: Testing DMA in KMDF Drivers
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 1D37F8B3-EAFC-4BB0-988D-64ADF30DBC40
---

# Testing DMA in KMDF Drivers


\[Applies to KMDF only\]

The following tools can help debug framework-based drivers that support DMA:

-   [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) includes specific verification tests that detect improper use of various DMA operations. For more information about DMA-specific verification, see [DMA Verification](https://msdn.microsoft.com/library/windows/hardware/ff544915).

-   The [**!dma**](https://msdn.microsoft.com/library/windows/hardware/ff562369) kernel debugger extension displays information about the DMA subsystem and DMA device drivers that are being verified by [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).

-   The [Kernel-Mode Driver Framework Extensions](https://msdn.microsoft.com/library/windows/hardware/ff551876) include the following DMA-specific commands:

    <a href="" id="-wdfcommonbuffer"></a>[**!wdfcommonbuffer**](https://msdn.microsoft.com/library/windows/hardware/ff565679)  
    Dumps information about a given common buffer object.

    <a href="" id="-wdfdmaenabler"></a>[**!wdfdmaenabler**](https://msdn.microsoft.com/library/windows/hardware/ff565717)  
    Dumps information about a specific DMA enabler object and its transactions and common buffer objects.

    <a href="" id="-wdfdmaenablers"></a>[**!wdfdmaenablers**](https://msdn.microsoft.com/library/windows/hardware/ff565719)  
    Lists all of the DMA enablers and their transactions and common buffer objects.

    <a href="" id="-wdfdmatransaction"></a>[**!wdfdmatransaction**](https://msdn.microsoft.com/library/windows/hardware/ff565721)  
    Dumps information about a given transaction object.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Testing%20DMA%20in%20KMDF%20Drivers%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




