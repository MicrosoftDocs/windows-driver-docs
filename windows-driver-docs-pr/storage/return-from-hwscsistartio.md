---
title: Return from HwScsiStartIo
author: windows-driver-content
description: Return from HwScsiStartIo
ms.assetid: e3d5e21a-4dc2-41bf-97a2-9ac2aa5a1af2
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "return values WDK SCSI", "status values WDK SCSI"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Return%20from%20HwScsiStartIo%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


