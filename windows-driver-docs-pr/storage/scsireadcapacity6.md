---
title: ScsiReadCapacity
description: ScsiReadCapacity
ms.assetid: ee4a0d3f-028b-4d25-badf-393198da3191
---

# ScsiReadCapacity


The **ScsiReadCapacity** method instructs the miniport driver that manages an iSCSI initiator HBA to log on to the target and issue a SCSI read capacity command to a logical unit on the target and then return the results.

This WMI method belongs to the unpublished [MSiSCSI\_Operations WMI Class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **ScsiReadCapacity** method, see the member descriptions for the [**ScsiReadCapacity\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564897) and [**ScsiReadCapacity\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564906) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class must support **ScsiReadCapacity**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ScsiReadCapacity%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




