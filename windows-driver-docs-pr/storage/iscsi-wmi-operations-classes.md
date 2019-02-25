---
title: iSCSI WMI Operations Classes
description: iSCSI WMI Operations Classes
ms.assetid: de8b31f8-e5dc-4ac0-8bd4-6912868310a0
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# iSCSI WMI Operations Classes


## <span id="ddk_iscsi_wmi_classes_that_define_the_interface_between_the_iscsi_disc"></span><span id="DDK_ISCSI_WMI_CLASSES_THAT_DEFINE_THE_INTERFACE_BETWEEN_THE_ISCSI_DISC"></span>


The iSCSI operations classes are internal, unpublished WMI classes that the iSCSI initiator service uses to communicate with iSCSI initiators. A storage miniport driver must implement these classes to communicate with the iSCSI discovery library. For more information about what is required to support these classes in a miniport driver, see the reference pages for the structures that are associated with the classes. These structures are defined in *Iscsiop.h*.

The iSCSI operations classes are not part of the user-mode WMI schema, and WMI management applications must not attempt to call their methods directly.

Initiator miniport drivers must support the following WMI tool classes:

[ISCSI\_Persistent\_Login WMI Class](iscsi-persistent-login-wmi-class.md)

[MSiSCSI\_AdapterEvent WMI Class](msiscsi-adapterevent-wmi-class.md)

[MSiSCSI\_BootInformation WMI Class](msiscsi-bootinformation-wmi-class.md)

[MSiSCSI\_LUNMappingInformation WMI Class](msiscsi-lunmappinginformation-wmi-class.md)

[MSiSCSI\_Operations WMI Class](msiscsi-operations-wmi-class.md)

[MSiSCSI\_PersistentLogins WMI Class](msiscsi-persistentlogins-wmi-class.md)

[MSiSCSI\_SecurityConfigOperations WMI Class](msiscsi-securityconfigoperations-wmi-class.md)

[MSiSCSI\_TargetMappings WMI Class](msiscsi-targetmappings-wmi-class.md)

 

 





