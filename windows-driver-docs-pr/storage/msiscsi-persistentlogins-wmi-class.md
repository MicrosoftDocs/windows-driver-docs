---
title: MSiSCSI\_PersistentLogins WMI Class
description: MSiSCSI\_PersistentLogins WMI Class
ms.assetid: 259220f8-af38-42b4-a0e3-88b4c396173d
---

# MSiSCSI\_PersistentLogins WMI Class


## <span id="ddk_msiscsi_persistentlogins_wmi_class_kr"></span><span id="DDK_MSISCSI_PERSISTENTLOGINS_WMI_CLASS_KR"></span>


The MSiSCSI\_PersistentLogins WMI class reports a list of persistent target logon sessions for the indicated initiator instance. The information that is associated with each particular persistent logon session is defined by the [ISCSI\_Persistent\_Login WMI class](iscsi-persistent-login-wmi-class.md).

Miniport drivers that manage HBA initiators are required to implement the MSiSCSI\_PersistentLogins WMI class.

The MSiSCSI\_PersistentLogins class is unpublished and is defined in *Operations.mof*.

When the WMI tool suite compiles this class definition, it produces the [**MSiSCSI\_PersistentLogins**](https://msdn.microsoft.com/library/windows/hardware/ff563093) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_PersistentLogins%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




