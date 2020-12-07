---
title: ISCSI\_Persistent\_Login WMI Class
description: ISCSI\_Persistent\_Login WMI Class
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_Persistent\_Login WMI Class


## <span id="ddk_iscsi_persistent_login_wmi_class_kr"></span><span id="DDK_ISCSI_PERSISTENT_LOGIN_WMI_CLASS_KR"></span>


The ISCSI\_Persistent\_Login WMI class defines a persistent logon. Miniport drivers that manage iSCSI initiators automatically establish persistent logon connections as soon as they are loaded into the storage driver stack. This timing guarantees that targets for which the initiator maintains persistent logons will be available to the system as early in the startup process as possible.

The ISCSI\_Persistent\_Login class is unpublished and is defined in *Operations.mof*.

When the WMI tool suite compiles this class definition, it produces the [**ISCSI\_Persistent\_Login**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_iscsi_persistent_login) data structure.

 

