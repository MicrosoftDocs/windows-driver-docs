---
title: MSiSCSI\_LUNMappingInformation WMI Class
description: MSiSCSI\_LUNMappingInformation WMI Class
ms.assetid: 646add52-f946-4169-9f6b-974253ec30af
---

# MSiSCSI\_LUNMappingInformation WMI Class


## <span id="ddk_msiscsi_lunmappinginformation_wmi_class_kr"></span><span id="DDK_MSISCSI_LUNMAPPINGINFORMATION_WMI_CLASS_KR"></span>


The MSiSCSI\_LUNMappingInformation class exposes the SCSI address information that the operating system assigns to a particular logical unit. The SCSI address information must be consistent with the information that the [MSiSCSI\_TargetMappings WMI class](msiscsi-targetmappings-wmi-class.md) reports.

Miniport drivers must create one instance of the MSiSCSI\_LUNMappingInformation WMI class for each physical device object (PDO) that is associated with a logical unit.

Because this class is associated with a particular LUN, the miniport driver that manages the HBA must register this class using the name of the PDO for the LUN.

The MSiSCSI\_LUNMappingInformation class is unpublished and is defined in *Operations.mof*.

When the WMI tool suite compiles this class definition, it produces the [**MSiSCSI\_LUNMappingInformation**](https://msdn.microsoft.com/library/windows/hardware/ff563065) data structure.

The SCSI address information that MSiSCSI\_LUNMappingInformation exposes must be consistent with the information that the initiator's miniport driver provided to the port driver during enumeration of the logical unit.

Initiators are required to implement the MSiSCSI\_LUNMappingInformation class.

Initiators must register the MSiSCSI\_LUNMappingInformation class using the name of the PDO for the logical unit.

Initiators must create one instance of the MSiSCSI\_LUNMappingInformation class for each logical unit that it enumerates.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_LUNMappingInformation%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




