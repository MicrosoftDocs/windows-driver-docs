---
title: Modifying Storage Miniport Driver Routines to Support WMI SRBs
description: Modifying Storage Miniport Driver Routines to Support WMI SRBs
ms.assetid: c3a222e8-dd02-4e45-b3e2-cec35d3abfdc
keywords: ["WMI SRBs WDK storage , modifying routines to support"]
---

# Modifying Storage Miniport Driver Routines to Support WMI SRBs


## <span id="ddk_modifying_storage_miniport_driver_routines_to_support_wmi_srbs_kg"></span><span id="DDK_MODIFYING_STORAGE_MINIPORT_DRIVER_ROUTINES_TO_SUPPORT_WMI_SRBS_KG"></span>


Before the miniport driver can support WMI SRBs, you must ensure that the miniport driver contains the required [**HwScsiWmiQueryReginfo**](https://msdn.microsoft.com/library/windows/hardware/ff557344) routine and that it performs the indicated actions for the following routines:

The [**DriverEntry of SCSI Miniport Driver**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine:

-   If the miniport driver uses the SCSI Port WMI library, initialize the [**SCSI\_WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565395) structure as indicated in [Using the SCSI Port WMI Library](using-the-scsi-port-wmi-library.md).

-   Indicate to the port driver whether it should allocate memory for SRB extensions. The miniport driver indicates that SRB extensions should be allocated by setting the **SrbExtensionSize** member of the [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) structure to a nonzero value.

The [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) routine:

-   Set the **WmiDataProvider** member of the [**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff563900) structure equal to **TRUE**.

The [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine:

-   Test **Function** member of the SRB to see if it is equal to SRB\_FUNCTION\_WMI. If this condition is **TRUE**, the miniport driver must process an SRB of type [**SCSI\_WMI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565397) rather than an SRB of type [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393).

-   Allocate memory for an [**SCSIWMI\_REQUEST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff564946) structure to hold SRB context. If the miniport driver might pend WMI requests, allocate memory from the SRB extension so that the miniport driver can maintain request context throughout the processing of an SRB. Otherwise, if there is no chance that the request will ever pend, allocate the memory for the context from the stack.

-   Check **Srb**-&gt;**WMIFlags** to determine whether the request is for the adapter or for a logical unit.

-   Call the SCSI Port WMI library dispatch routine, [**ScsiPortWmiDispatchFunction**](https://msdn.microsoft.com/library/windows/hardware/ff564766). For an explanation of how to call this dispatch routine, see [Using the SCSI Port WMI Library](using-the-scsi-port-wmi-library.md).

-   Call [**ScsiPortWmiPostProcess**](https://msdn.microsoft.com/library/windows/hardware/ff564796) after processing the request if it was pended by the driver. If the driver did not pend the request, then **ScsiPortWmiPostProcess** should be called in the miniport driver callback routine, rather than the miniport driver's start I/O routine.

-   Set **Srb**-&gt;**DataTransferLength** and **Srb**-&gt;**SrbStatus** to the values returned by [**ScsiPortWmiGetReturnSize**](https://msdn.microsoft.com/library/windows/hardware/ff564789) and [**ScsiPortWmiGetReturnStatus**](https://msdn.microsoft.com/library/windows/hardware/ff564791) respectively.

-   Call [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with **RequestComplete** and again with **NextRequest** or (**NextLuRequest**).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Modifying%20Storage%20Miniport%20Driver%20Routines%20to%20Support%20WMI%20SRBs%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




