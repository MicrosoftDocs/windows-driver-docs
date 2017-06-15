---
title: Setting Up the System DMA Controller for Common-Buffer DMA
author: windows-driver-content
description: Setting Up the System DMA Controller for Common-Buffer DMA
MS-HAID:
- 'ioprogdma\_e9bfc3a8-a644-40bb-b017-d482fc7064b9.xml'
- 'kernel.setting\_up\_the\_system\_dma\_controller\_for\_common\_buffer\_dma'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 279776e0-dead-4763-9aae-33950837c27c
keywords: ["system DMA WDK kernel , common buffer", "common buffer DMA WDK kernel", "DMA transfers WDK kernel , common buffer", "AllocateAdapterChannel", "MapTransfer"]
---

# Setting Up the System DMA Controller for Common-Buffer DMA


## <a href="" id="ddk-setting-up-the-system-dma-controller-for-common-buffer-dma-kg"></a>


When **AllocateAdapterChannel** transfers control to a driver's [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine, the driver "owns" the system DMA controller and a set of map registers. Then, the driver must call [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402) to set up the system DMA controller to use the driver-allocated common buffer before the driver sets up its device for the transfer operation.

The driver supplies the following parameters to **MapTransfer**:

-   The adapter object pointer returned by **IoGetDmaAdapter**

-   A pointer to the MDL describing the driver-allocated common buffer

-   The *MapRegisterBase* handle passed to the driver's *AdapterControl* routine by **AllocateAdapterChannel**

-   A pointer to a variable (*Length*) indicating the size in bytes of the driver-allocated common buffer

-   A Boolean value, indicating the direction of the transfer operation (TRUE for a requested transfer from system memory to the device)

**MapTransfer** returns a logical address, which drivers that use system DMA must ignore. When **MapTransfer** returns control, the driver should set up its device for the DMA operation. The driver calls **MapTransfer** only once but continues to copy data between its common buffer and a locked-down user buffer until the requested transfer is done.

The driver can call [**ReadDmaCounter**](https://msdn.microsoft.com/library/windows/hardware/ff560782) to determine how many bytes currently remain to be transferred in the common buffer; the driver can then continue to fill its common buffer with user data or copy data from its common buffer to the user buffer, depending on the direction of the DMA operation.

When the transfer is complete or if the driver must return an error status for the IRP, the driver calls [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) to ensure that any data cached in the system DMA controller is read into system memory or written out to the device. Then the driver should call [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) promptly to release the system DMA controller for use by any driver (including itself).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Setting%20Up%20the%20System%20DMA%20Controller%20for%20Common-Buffer%20DMA%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


