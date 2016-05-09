---
title: Handling SRB\_FUNCTION\_WMI
author: windows-driver-content
description: Handling SRB\_FUNCTION\_WMI
ms.assetid: df20b9dc-1b67-4044-8abe-3cf5714076b3
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "SRB_FUNCTION_WMI", "WMI WDK SCSI"]
---

# Handling SRB\_FUNCTION\_WMI


## <span id="ddk_handling_srb_function_wmi_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_WMI_KG"></span>


If the HBA supports [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI), the port driver will send WMI requests to the miniport driver. The HBA indicates that it supports WMI by setting the WmiDataProvider field of the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) structure to **TRUE** in its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine.

The writer of a miniport driver prepares the miniport to handle WMI requests as follows:

-   If the miniport exposes custom data blocks or event blocks, it should define such blocks in a MOF file and compile it as a binary resource in the miniport's binary image. For more information, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139).

-   Implement required and optional *HwScsiWmiXxx* callback routines, as described in [SCSI Miniport Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff565312).

-   Handle SRB\_FUNCTION\_WMI.

If a miniport driver might pend WMI requests, its **DriverEntry** routine should request that memory be allocated for SRB extensions so the miniport driver can maintain request context throughout the processing of an SRB.

Before the miniport driver handles its first WMI request, it must allocate a SCSI\_WMILIB\_CONTEXT structure in its device extension and initialize the structure with the following:

-   The number of data and event blocks supported by the miniport driver, including standard blocks defined by the system in *wmicore.mof* as well as the miniport driver's custom blocks, if any.

-   A pointer to an array of SCSIWMIGUIDREGINFO structures, one for each block supported.

-   Entry points to the miniport driver's *HwScsiWmiXxx* callback routines. At a minimum, a miniport driver must provide entry points to an [**HwScsiWmiQueryReginfo**](https://msdn.microsoft.com/library/windows/hardware/ff557344) routine and an [**HwScsiWmiQueryDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff557340) routine.

A miniport driver is not required to take any action to register its data and event blocks other than setting the WmiDataProvider field of the PORT\_CONFIGURATION\_INFO structure to **TRUE** and implement the required *HwScsiWmiQueryReginfo* routine. The port driver is responsible for registering the miniport driver's blocks with the WMI kernel component.

On receipt of an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, a miniport driver's [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine does the following:

-   Allocates a SCSIWMI\_REQUEST\_CONTEXT structure from the SRB extension if the request might pend, or from the stack if the request could never pend.

-   Checks **Srb**-**&gt;WMIFlags** to determine whether the request is for the adapter or a logical unit.

-   Calls [**ScsiPortWmiDispatchFunction**](https://msdn.microsoft.com/library/windows/hardware/ff564766) with pointers to the miniport driver's SCSI\_WMILIB\_CONTEXT, its device extension, and the request context, and the following parameters from the SRB:

    **Srb**-**&gt;WMISubFunction**

    **Srb**-**&gt;DataPath**

    **Srb**-**&gt;DataTransferLength**

    **Srb**-**&gt;DataBuffer**

-   Calls [**ScsiPortWmiPostProcess**](https://msdn.microsoft.com/library/windows/hardware/ff564796) when the driver has finished processing the request. If the driver does not pend the request, then **ScsiPortWmiPostProcess** would most likely be called in the callback. If the driver pends the request then **ScsiPortWmiPostProcess** should be called when the request is completed.

-   Sets **Srb**-**&gt;DataTransferLength** and **Srb**-**&gt;SrbStatus** to the values returned by [**ScsiPortWmiGetReturnSize**](https://msdn.microsoft.com/library/windows/hardware/ff564789) and [**ScsiPortWmiGetReturnStatus**](https://msdn.microsoft.com/library/windows/hardware/ff564791), respectively,

-   Calls [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with **RequestComplete** and again with **NextRequest** or (**NextLuRequest**).

For more information about WMI, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SRB_FUNCTION_WMI%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


