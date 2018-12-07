---
title: MSiSCSI\_LUNMappingInformation WMI Class
description: MSiSCSI\_LUNMappingInformation WMI Class
ms.assetid: 646add52-f946-4169-9f6b-974253ec30af
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 





