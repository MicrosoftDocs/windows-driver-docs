---
title: iSCSI WMI Operations Classes
description: iSCSI WMI Operations Classes
ms.assetid: de8b31f8-e5dc-4ac0-8bd4-6912868310a0
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20iSCSI%20WMI%20Operations%20Classes%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




