---
title: Modifying Storage Miniport Driver Routines to Support WMI SRBs
description: Modifying Storage Miniport Driver Routines to Support WMI SRBs
keywords:
- WMI SRBs WDK storage , modifying routines to support
ms.date: 10/08/2019
---

# Modifying Storage Miniport Driver Routines to Support WMI SRBs

Before the miniport driver can support WMI SRBs, you must ensure that the miniport driver contains the required [*HwScsiWmiQueryReginfo*](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_reginfo) routine and that it performs the indicated actions for the following routines:

The [**DriverEntry of SCSI Miniport Driver**](driverentry-of-scsi-miniport-driver.md) routine:

- If the miniport driver uses the SCSI Port WMI library, initialize the [SCSI_WMILIB_CONTEXT](/windows-hardware/drivers/ddi/scsiwmi/ns-scsiwmi-_scsiwmilib_context) structure as indicated in [Using the SCSI Port WMI Library](using-the-scsi-port-wmi-library.md).

- Indicate to the port driver whether it should allocate memory for SRB extensions. The miniport driver indicates that SRB extensions should be allocated by setting the **SrbExtensionSize** member of the [**HW_INITIALIZATION_DATA (SCSI)**](/windows-hardware/drivers/ddi/srb/ns-srb-_hw_initialization_data) structure to a nonzero value.

The [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) routine:

- Set the **WmiDataProvider** member of the [PORT_CONFIGURATION_INFORMATION (SCSI)](/windows-hardware/drivers/ddi/srb/ns-srb-_port_configuration_information) structure equal to **TRUE**.

The [*HwScsiStartIo*](/previous-versions/windows/hardware/drivers/ff557323(v=vs.85)) routine:

- Test **Function** member of the SRB to see if it is equal to SRB_FUNCTION_WMI. If this condition is **TRUE**, the miniport driver must process an SRB of type [**SCSI_WMI_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_wmi_request_block) rather than an SRB of type [**SCSI_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_request_block).

- Allocate memory for an [SCSIWMI_REQUEST_CONTEXT](/windows-hardware/drivers/ddi/scsiwmi/ns-scsiwmi-scsiwmi_request_context) structure to hold SRB context. If the miniport driver might pend WMI requests, allocate memory from the SRB extension so that the miniport driver can maintain request context throughout the processing of an SRB. Otherwise, if there is no chance that the request will ever pend, allocate the memory for the context from the stack.

- Check **Srb->WMIFlags** to determine whether the request is for the adapter or for a logical unit.

- Call the SCSI Port WMI library dispatch routine, [**ScsiPortWmiDispatchFunction**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmidispatchfunction). For an explanation of how to call this dispatch routine, see [Using the SCSI Port WMI Library](using-the-scsi-port-wmi-library.md).

- Call [**ScsiPortWmiPostProcess**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmipostprocess) after processing the request if it was pended by the driver. If the driver did not pend the request, then **ScsiPortWmiPostProcess** should be called in the miniport driver callback routine, rather than the miniport driver's start I/O routine.

- Set **Srb->DataTransferLength** and **Srb->SrbStatus** to the values returned by [**ScsiPortWmiGetReturnSize**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmigetreturnsize) and [**ScsiPortWmiGetReturnStatus**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmigetreturnstatus) respectively.

- Call [**ScsiPortNotification**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportnotification) with **RequestComplete** and again with **NextRequest** or (**NextLuRequest**).
