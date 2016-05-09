---
title: Error Handling in Storport Miniport Drivers
description: Error Handling in Storport Miniport Drivers
ms.assetid: 23ea8c36-56cf-45ae-a066-765d3a91b542
---

# Error Handling in Storport Miniport Drivers


Every Storport miniport driver must notify the system port driver about the following kinds of SCSI errors. These errors should be set in the **SrbStatus** member before the driver completes the SRB it was processing when the error occurred:

-   SRB\_STATUS\_ERROR (if the HBA returns a nonspecific bus error)

-   SRB\_STATUS\_PARITY\_ERROR

-   SRB\_STATUS\_UNEXPECTED\_BUS\_FREE

-   SRB\_STATUS\_SELECTION\_TIMEOUT

-   SRB\_STATUS\_COMMAND\_TIMEOUT

-   SRB\_STATUS\_MESSAGE\_REJECTED

-   SRB\_STATUS\_NO\_DEVICE

-   SRB\_STATUS\_NO\_HBA

-   SRB\_STATUS\_DATA\_OVERRUN (also returned for underruns)

-   SRB\_STATUS\_PHASE\_SEQUENCE\_FAILURE

-   SRB\_STATUS\_BUSY (TID busy)

For a data underrun, the miniport driver must update the SRB's **DataTransferLength** to indicate how much data actually was transferred.

In addition, the miniport driver should use the following guidelines to log some of the preceding errors by passing the SRB to [**StorPortLogError**](https://msdn.microsoft.com/library/windows/hardware/ff567426):

Log an error at the discretion of the driver writer for SRB\_STATUS\_ERROR.

Always log an error for SRB\_STATUS\_PARITY\_ERROR.

Always log an error for SRB\_STATUS\_UNEXPECTED\_BUS\_FREE.

Always log an error for SRB\_STATUS\_SELECTION\_TIMEOUT.

Always log an error for SRB\_STATUS\_COMMAND\_TIMEOUT.

Log an error for SRB\_STATUS\_DATA\_OVERRUN whenever an overrun occurs, but not when an underrun occurs.

Always log an error for SRB\_STATUS\_PHASE\_SEQUENCE\_FAILURE.

Always log an error for SRB\_STATUS\_BUSY for hardware errors.

To log an error, a miniport driver calls [**StorPortLogError**](https://msdn.microsoft.com/library/windows/hardware/ff567426) by using one of the following system-defined error or warning codes:

SP\_BUS\_PARITY\_ERROR maps to SRB\_STATUS\_PARITY\_ERROR

SP\_UNEXPECTED\_DISCONNECT (by the target logical unit)

SP\_INVALID\_RESELECTION maps to SRB\_STATUS\_PHASE\_SEQUENCE\_FAILURE or SRB\_STATUS\_ERROR

SP\_BUS\_TIME\_OUT maps to SRB\_STATUS\_SELECTION\_TIMEOUT

SP\_REQUEST\_TIMEOUT maps to SRB\_STATUS\_COMMAND\_TIMEOUT

SP\_PROTOCOL\_ERROR maps to SRB\_STATUS\_PHASE\_SELECTION\_FAILURE, SRB\_STATUS\_UNEXPECTED\_BUS\_FREE, or SRB\_STATUS\_DATA\_OVERRUN for an overrun condition

SP\_INTERNAL\_ADAPTER\_ERROR maps to SRB\_STATUS\_ERROR

SP\_IRQ\_NOT\_RESPONDING (warning that the miniport driver has detected that the HBA is no longer generating interrupt requests)

SP\_BAD\_FW\_ERROR where FW is *firmware*)

SP\_BAD\_FW\_WARNING

[**StorPortLogError**](https://msdn.microsoft.com/library/windows/hardware/ff567426) allocates an error-log packet, sets it up, and logs the I/O error in the event log on behalf of the miniport driver. System administrators or users can monitor the condition of an HBA by examining the system event log and, if necessary, reconfiguring, repairing, or replacing the HBA before it fails.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Error%20Handling%20in%20Storport%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




