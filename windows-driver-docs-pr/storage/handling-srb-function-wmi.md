---
title: Handling SRB_FUNCTION_WMI
description: Handling SRB_FUNCTION_WMI
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_WMI
- WMI WDK SCSI
ms.date: 10/08/2019
---

# Handling SRB_FUNCTION_WMI

If the host bus adapter (HBA) supports [Windows Management Instrumentation](../kernel/implementing-wmi.md) (WMI), the port driver will send WMI requests to the miniport driver. The HBA indicates that it supports WMI by setting the WmiDataProvider field of the [*PORT_CONFIGURATION_INFORMATION*](/windows-hardware/drivers/ddi/srb/ns-srb-_port_configuration_information) structure to **TRUE** in its [**DriverEntry**](driverentry-of-scsi-miniport-driver.md) routine.

The writer of a miniport driver prepares the miniport to handle WMI requests as follows:

- If the miniport exposes custom data blocks or event blocks, it should define such blocks in a MOF file and compile it as a binary resource in the miniport's binary image. For more information, see [Windows Management Instrumentation](../kernel/implementing-wmi.md).

- Implement required and optional *HwScsiWmiXxx* callback routines, as described in [SCSI Miniport Driver Routines](scsi-miniport-driver-routines.md).

- Handle SRB_FUNCTION_WMI.

If a miniport driver might pend WMI requests, its **DriverEntry** routine should request that memory be allocated for SRB extensions so the miniport driver can maintain request context throughout the processing of an SRB.

Before the miniport driver handles its first WMI request, it must allocate a SCSI_WMILIB_CONTEXT structure in its device extension and initialize the structure with the following:

- The number of data and event blocks supported by the miniport driver, including standard blocks defined by the system in *wmicore.mof* as well as the miniport driver's custom blocks, if any.

- A pointer to an array of SCSIWMIGUIDREGINFO structures, one for each block supported.

- Entry points to the miniport driver's *HwScsiWmiXxx* callback routines. At a minimum, a miniport driver must provide entry points to an [*HwScsiWmiQueryReginfo*](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_reginfo) routine and an [*HwScsiWmiQueryDataBlock*](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_datablock) routine.

A miniport driver is not required to take any action to register its data and event blocks other than setting the WmiDataProvider field of the PORT_CONFIGURATION_INFO structure to **TRUE** and implement the required *HwScsiWmiQueryReginfo* routine. The port driver is responsible for registering the miniport driver's blocks with the WMI kernel component.

On receipt of an SRB in which the **Function** member is set to SRB_FUNCTION_WMI, a miniport driver's [*HwScsiStartIo*](/previous-versions/windows/hardware/drivers/ff557323(v=vs.85)) routine does the following:

- Allocates a SCSIWMI_REQUEST_CONTEXT structure from the SRB extension if the request might pend, or from the stack if the request could never pend.

- Checks **Srb->WMIFlags** to determine whether the request is for the adapter or a logical unit.

- Calls [**ScsiPortWmiDispatchFunction**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmidispatchfunction) with pointers to the miniport driver's SCSI_WMILIB_CONTEXT, its device extension, and the request context, and the following parameters from the SRB:

    **Srb->WMISubFunction**

    **Srb->DataPath**

    **Srb->DataTransferLength**

    **Srb->DataBuffer**

- Calls [**ScsiPortWmiPostProcess**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmipostprocess) when the driver has finished processing the request. If the driver does not pend the request, then **ScsiPortWmiPostProcess** would most likely be called in the callback. If the driver pends the request then **ScsiPortWmiPostProcess** should be called when the request is completed.

- Sets **Srb->DataTransferLength** and **Srb->SrbStatus** to the values returned by [**ScsiPortWmiGetReturnSize**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmigetreturnsize) and [**ScsiPortWmiGetReturnStatus**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmigetreturnstatus), respectively,

- Calls [**ScsiPortNotification**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportnotification) with **RequestComplete** and again with **NextRequest** or (**NextLuRequest**).

For more information about WMI, see [Windows Management Instrumentation](../kernel/implementing-wmi.md).
