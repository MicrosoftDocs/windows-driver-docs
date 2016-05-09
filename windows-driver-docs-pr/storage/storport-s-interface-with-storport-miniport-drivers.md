---
title: Storport's Interface with Storport Miniport Drivers
author: windows-driver-content
description: Storport's Interface with Storport Miniport Drivers
ms.assetid: 8e09d6a6-7e4f-44fc-a2b0-5f21b4ac0593
---

# Storport's Interface with Storport Miniport Drivers


Communication between the Storport driver and the Storport miniport drivers takes place by means of SCSI request blocks (SRBs) and miniport driver callback routines. For a detailed discussion of the Storport miniport driver callback routines, see [Storport Driver Miniport Routines](https://msdn.microsoft.com/library/windows/hardware/ff567543).

For an overview and definition of the individual SRB functions, SRB flags, and SRB status values, see [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393).

For discussions about how miniport drivers must respond to each individual SRB function, see [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423).

Storport forwards SRBs to Storport miniport drivers for asynchronous processing. Typically, the miniport driver will take some time to actually complete the request. Host bus adapters that support tagged queuing can queue requests internally and process them in the order that is indicated by the tags that Storport assigns to each request. The [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393) (SRB) structure contains two members that the Storport driver uses to specify how SRBs should be ordered in the host adapter's internal queue: **QueuedTag** and **QueueAction**. Storport assigns a count, or *"tag"* value, to the **QueuedTag** member of each SRB that indicates the order in which the adapter should process the packets. The tag values also allow Storport to track which SRBs have completed successfully and which SRBs have timed out.

The **QueueAction** member is assigned one of the following values:

SRB\_SIMPLE\_TAG\_REQUEST

SRB\_HEAD\_OF\_QUEUE\_TAG\_REQUEST

SRB\_ORDERED\_QUEUE\_TAG\_REQUEST

For an explanation of these values, see the SCSI-3 specification.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storport's%20Interface%20with%20Storport%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


