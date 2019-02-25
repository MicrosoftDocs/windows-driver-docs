---
title: Return from HwScsiStartIo
description: Return from HwScsiStartIo
ms.assetid: e3d5e21a-4dc2-41bf-97a2-9ac2aa5a1af2
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- return values WDK SCSI
- status values WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Return from HwScsiStartIo


## <span id="ddk_return_from_hwscsistartio_kg"></span><span id="DDK_RETURN_FROM_HWSCSISTARTIO_KG"></span>


Every [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine must return **TRUE**, indicating that the input request was processed.

If the *HwScsiStartIo* routine cannot carry out a requested operation when it is called, *HwScsiStartIo* should do the following:

1.  Set the input SRB's **SrbStatus** to SRB\_STATUS\_BUSY.

2.  Call [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with the *NotificationType***RequestComplete** and with the input SRB.

3.  Call **ScsiPortNotification** with the *NotificationType***NextRequest** if the driver can accept a request to a different target logical unit than the one in the just completed SRB.

4.  Return **TRUE**.

The port driver resubmits any request returned with the **SrbStatus** value SRB\_STATUS\_BUSY to the miniport driver's *HwScsiStartIo* routine later.

Eventually, every miniport driver must call **ScsiPortNotification** twice for each SRB input to its *HwScsiStartIo* routine: first, to complete the request (*NotificationType***RequestComplete**) and, second, to tell the port driver to call the *HwScsiStartIo* routine again with the next SRB (*NotificationType***NextRequest** or **NextLuRequest**).

The *HwScsiStartIo* routine of a miniport driver that manages its HBA exclusively by polling calls **ScsiPortNotification** with the *NotificationType***RequestTimerCall** and a pointer to its *HwScsiTimer* routine. For more information about the *HwScsiTimer* routine, see [SCSI Miniport Driver's HwScsiTimer Routine](scsi-miniport-driver-s-hwscsitimer-routine.md).

 

 




