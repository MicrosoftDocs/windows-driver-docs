---
title: Setting Up the System DMA Controller for Common-Buffer DMA
description: Setting Up the System DMA Controller for Common-Buffer DMA
ms.assetid: 279776e0-dead-4763-9aae-33950837c27c
keywords: ["system DMA WDK kernel , common buffer", "common buffer DMA WDK kernel", "DMA transfers WDK kernel , common buffer", "AllocateAdapterChannel", "MapTransfer"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Setting Up the System DMA Controller for Common-Buffer DMA





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

 

 




