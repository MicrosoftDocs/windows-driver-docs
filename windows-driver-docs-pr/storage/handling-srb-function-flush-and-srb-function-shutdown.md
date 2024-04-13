---
title: Handling SRB_FUNCTION_FLUSH and SRB_FUNCTION_SHUTDOWN
description: Handling SRB_FUNCTION_FLUSH and SRB_FUNCTION_SHUTDOWN
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_FLUSH
- SRB_FUNCTION_SHUTDOWN
ms.date: 04/20/2017
---

# Handling SRB\_FUNCTION\_FLUSH and SRB\_FUNCTION\_SHUTDOWN


## <span id="ddk_handling_srb_function_flush_and_srb_function_shutdown_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_FLUSH_AND_SRB_FUNCTION_SHUTDOWN_KG"></span>


If the HBA caches data internally, as indicated when [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) sets up the [**PORT\_CONFIGURATION\_INFORMATION**](/windows-hardware/drivers/ddi/srb/ns-srb-_port_configuration_information), the [**HwScsiStartIo**](/previous-versions/windows/hardware/drivers/ff557323(v=vs.85)) routine must support the SRB\_FUNCTION\_FLUSH and SRB\_FUNCTION\_SHUTDOWN requests as follows:

-   An SRB with its **Function** member set to SRB\_FUNCTION\_FLUSH tells the miniport driver to transfer data cached in the HBA, usually to a disk. The miniport driver must hold on to the flush request until all cached data has been transferred and, then, complete the flush request.

-   Such a flush request might originate when an application closes a file or the application itself is terminated.

-   An SRB with its **Function** member set to SRB\_FUNCTION\_SHUTDOWN tells the miniport driver to complete transferring data, including flushing all cached data, out to the target device. The miniport driver must hold on to the shutdown request until no data remains in the HBA's internal cache for the target logical unit and, then, complete the shutdown request.

    Note that a miniport driver can be called with more than one shutdown request, possibly for the same logical unit or with several shutdown requests for different logical units, before the system itself is actually shut down.

 

