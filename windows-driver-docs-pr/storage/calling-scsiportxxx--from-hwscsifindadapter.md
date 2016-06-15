---
title: Calling ScsiPortXxx from HwScsiFindAdapter
author: windows-driver-content
description: Calling ScsiPortXxx from HwScsiFindAdapter
ms.assetid: 17cfca31-ff93-4882-872c-ab8af6cdc3cf
keywords: ["HwScsiFindAdapter", "SCSI miniport drivers WDK storage , HwScsiFindAdapter", "calling ScsiPortXxx routines WDK storage", "ScsiPortXxx calls"]
---

# Calling ScsiPortXxx from HwScsiFindAdapter


## <span id="ddk_calling_scsiportxxx_from_hwscsifindadapter_kg"></span><span id="DDK_CALLING_SCSIPORTXXX_FROM_HWSCSIFINDADAPTER_KG"></span>


Certain **ScsiPort***Xxx* routines can be called *only* from the miniport driver's *HwScsiFindAdapter* routine(s), in particular, the following:

-   [**ScsiPortValidateRange**](https://msdn.microsoft.com/library/windows/hardware/ff564761) to verify that a miniport driver-supplied, bus-relative access range has not already been claimed in the registry by another driver for its device.

-   [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629) to map the (bus-relative) "physical" address range for an HBA to a system-assigned logical address range that the driver can use to communicate with the HBA by calling the **ScsiPortRead***Xxx* and **ScsiPortWrite***Xxx* routines with the mapped logical range addresses.

-   [**ScsiPortFreeDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564623) to release such a mapped range if *HwScsiFindAdapter* does not find an HBA it can support on a given I/O bus, as indicated by the PORT\_CONFIGURATION\_INFORMATION **SystemIoBusNumber** value.

-   [**ScsiPortGetUncachedExtension**](https://msdn.microsoft.com/library/windows/hardware/ff564639) to allocate a DMA buffer shared between the system and a bus-master HBA.

In addition to these four routines, there is one routine that can only be called from the miniport driver's *HwScsiFindAdapter* routine *or* from *HwScsiAdapterControl* when the control type is **ScsiSetRunningConfig**:

-   [**ScsiPortGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff564624) to get BUS\_DATA\_TYPE-specific configuration information, such as bus-relative device memory (access) ranges, interrupt vector or IRQL, and DMA channel or port.

For more information about these **ScsiPort***Xxx* routines, see [SCSI Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff565375).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Calling%20ScsiPortXxx%20%20from%20HwScsiFindAdapter%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


