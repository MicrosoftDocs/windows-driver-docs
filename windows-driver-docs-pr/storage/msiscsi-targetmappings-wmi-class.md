---
title: MSiSCSI\_TargetMappings WMI Class
description: MSiSCSI\_TargetMappings WMI Class
ms.assetid: 12bfe80a-8431-4607-99f5-ddd6815aecc6
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 





