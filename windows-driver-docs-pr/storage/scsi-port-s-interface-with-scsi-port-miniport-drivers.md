---
title: SCSI Port's Interface with SCSI Port Miniport Drivers
description: SCSI Port's Interface with SCSI Port Miniport Drivers
ms.assetid: e6bd9861-5b89-40cc-92ab-0d23f18ba805
---

# SCSI Port's Interface with SCSI Port Miniport Drivers


## <span id="ddk_scsi_port_s_interface_with_scsi_port_miniport_drivers_kg"></span><span id="DDK_SCSI_PORT_S_INTERFACE_WITH_SCSI_PORT_MINIPORT_DRIVERS_KG"></span>


Communication between the SCSI Port driver and the SCSI Port miniport drivers takes place by means of SCSI request blocks (SRBs) and miniport driver callback routines. For a detailed discussion of the SCSI Port miniport driver callback routines, see [SCSI Miniport Drivers](scsi-miniport-drivers.md).

For an overview and definition of the individual SRB functions, SRB flags, and SRB status values, see [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393).

For discussions about how miniport drivers must respond to each individual SRB function, see [SCSI Miniport Driver's HwScsiStartIo Routine](scsi-miniport-driver-s-hwscsistartio-routine.md).

SCSI Port forwards SRBs to SCSI Port miniport drivers synchronously, except when the adapter supports tagged queuing. Host bus adapters that support tagged queuing can queue requests internally and process them in the order that is indicated by the tags that SCSI Port assigns to each request. The [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393) (SRB) structure contains two members that the SCSI Port driver uses to specify how SRBs should be ordered in the host adapter's internal queue: **QueuedTag** and **QueueAction**. SCSI Port assigns a count, or *"tag"* value, to the **QueuedTag** member of each SRB that indicates the order in which the adapter should process the packets. The tag values also allow SCSI Port to track which SRBs have completed successfully and which SRBs have timed out.

The **QueueAction** member is assigned one of the following values:

SRB\_SIMPLE\_TAG\_REQUEST

SRB\_HEAD\_OF\_QUEUE\_TAG\_REQUEST

SRB\_ORDERED\_QUEUE\_TAG\_REQUEST

For an explanation of these values, see the SCSI-2 specification.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Port's%20Interface%20with%20SCSI%20Port%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




