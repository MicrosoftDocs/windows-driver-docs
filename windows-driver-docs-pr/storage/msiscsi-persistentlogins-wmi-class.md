---
title: MSiSCSI\_PersistentLogins WMI Class
description: MSiSCSI\_PersistentLogins WMI Class
ms.assetid: 259220f8-af38-42b4-a0e3-88b4c396173d
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_PersistentLogins WMI Class


## <span id="ddk_msiscsi_persistentlogins_wmi_class_kr"></span><span id="DDK_MSISCSI_PERSISTENTLOGINS_WMI_CLASS_KR"></span>


The MSiSCSI\_PersistentLogins WMI class reports a list of persistent target logon sessions for the indicated initiator instance. The information that is associated with each particular persistent logon session is defined by the [ISCSI\_Persistent\_Login WMI class](iscsi-persistent-login-wmi-class.md).

Miniport drivers that manage HBA initiators are required to implement the MSiSCSI\_PersistentLogins WMI class.

The MSiSCSI\_PersistentLogins class is unpublished and is defined in *Operations.mof*.

When the WMI tool suite compiles this class definition, it produces the [**MSiSCSI\_PersistentLogins**](https://msdn.microsoft.com/library/windows/hardware/ff563093) data structure.

 

 





