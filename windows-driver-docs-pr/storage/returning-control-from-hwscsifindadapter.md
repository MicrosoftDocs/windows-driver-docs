---
title: Returning Control from HwScsiFindAdapter
author: windows-driver-content
description: Returning Control from HwScsiFindAdapter
ms.assetid: 689eae76-9b5b-438f-bbdc-5ee11c6fe737
keywords: ["HwScsiFindAdapter", "SCSI miniport drivers WDK storage , HwScsiFindAdapter", "return values WDK SCSI", "status values WDK SCSI"]
---

# Returning Control from HwScsiFindAdapter


## <span id="ddk_returning_control_from_hwscsifindadapter_kg"></span><span id="DDK_RETURNING_CONTROL_FROM_HWSCSIFINDADAPTER_KG"></span>


When a legacy miniport driver's [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) routine returns control, [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645) returns to the **DriverEntry** routine if the call(s) to *HwScsiFindAdapter* indicated that the miniport driver could not support an HBA. Otherwise, **ScsiPortInitialize** claims resources in the registry and sets up necessary system resources, such as interrupt and adapter objects, on behalf of the miniport driver. Then, it calls the miniport driver's *HwScsiInitialize* routine, described in [SCSI Miniport Driver's HwScsiInitialize Routine](scsi-miniport-driver-s-hwscsiinitialize-routine.md).

When a Plug and Play miniport driver's *HwScsiFindAdapter* routine returns control, the Plug and Play manager is allowed to unload the miniport driver if the call(s) to *HwScsiFindAdapter* indicated that the miniport driver could not support an HBA. Otherwise, the port driver connects interrupts (other resources having been claimed and set up before the *HwScsiFindAdapter* call) and calls the miniport driver's [*HwScsiInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff557302) routine, which initializes the HBA.

Currently, in addition to the values it sets in the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900), the port driver also checks the registry for user-set values that disable any or all of the following:

-   Synchronous transfers on the HBA

    The port driver ORs the default **SrbFlags** that it maintains for the HBA with SRB\_FLAGS\_DISABLE\_SYNCH\_TRANSFER.

-   Bus-disconnect operations on the HBA

    The port driver ORs the default **SrbFlags** with SRB\_FLAGS\_DISABLE\_DISCONNECT.

-   Tagged queuing

    The port driver sets the **TaggedQueuing** Boolean that it maintains for the HBA to **FALSE**.

-   Internal queuing of requests on the HBA

    The port driver sets to **FALSE** the **MultipleRequestPerLu** Boolean that it maintains about the HBA.

Any of the immediately preceding "disable" values in the registry overrides whatever the *HwScsiFindAdapter* routine sets in the PORT\_CONFIGURATION\_INFORMATION buffer. Note that temporarily disabling synchronous transfers, bus-disconnect operations, tagged queuing, and HBA internal request queuing can simplify using a debugger to trace request handling in a miniport driver that is under development.

Note also that the NT-based operating system port driver uses values from the PORT\_CONFIGURATION\_INFORMATION provided by a miniport driver's *HwScsiFindAdapter* routine or from other sources (such as the registry for a legacy miniport driver) to fill in the IO\_SCSI\_CAPABILITIES data for use by storage class drivers, as described in [Storage Class Drivers](storage-class-drivers.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Returning%20Control%20from%20HwScsiFindAdapter%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


