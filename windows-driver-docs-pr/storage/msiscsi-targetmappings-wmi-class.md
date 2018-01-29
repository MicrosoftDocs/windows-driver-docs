---
title: MSiSCSI\_TargetMappings WMI Class
description: MSiSCSI\_TargetMappings WMI Class
ms.assetid: 12bfe80a-8431-4607-99f5-ddd6815aecc6
---

# MSiSCSI\_TargetMappings WMI Class


## <span id="ddk_msiscsi_targetmappings_wmi_class_kr"></span><span id="DDK_MSISCSI_TARGETMAPPINGS_WMI_CLASS_KR"></span>


The MSiSCSI\_TargetMappings WMI class contains a set of iSCSI logical unit number (LUN) mappings that are associated with a session. There is a mapping for each LUN that is exposed by a login session that the initiator established. Each session's mapping is described by an instance of the [ISCSI\_TargetMapping WMI class](iscsi-targetmapping-wmi-class.md) that is an embedded class within the MSiSCSI\_TargetMappings WMI class.

Every iSCSI initiator must implement the MSiSCSI\_TargetMappings class. The iSCSI initiator service relies on this class to communicate with the HBA initiator.

There should be one instance of the MSiSCSI\_TargetMappings WMI class for each loaded instance of the miniport driver that manages the initiator HBA. The miniport driver must register the MSiSCSI\_TargetMappings class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_TargetMappings class is unpublished and is defined in *Operations.mof*.

When the WMI tool suite compiles this class definition, it produces the [**MSiSCSI\_TargetMappings**](https://msdn.microsoft.com/library/windows/hardware/ff563144) data structure.

Initiators are required to implement the MSiSCSI\_TargetMappings class.

The iSCSI initiator service relies on the MSiSCSI\_TargetMappings class to communicate with an HBA initiator. Miniport drivers that manage HBA initiators must implement one instance of the MSiSCSI\_TargetMappings class per HBA.

Initiators must register the MSiSCSI\_TargetMappings class using the name of the PDO for the HBA.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_TargetMappings%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




