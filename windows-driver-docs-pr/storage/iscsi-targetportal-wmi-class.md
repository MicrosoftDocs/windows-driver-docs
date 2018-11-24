---
title: ISCSI\_TargetPortal WMI Class
description: ISCSI\_TargetPortal WMI Class
ms.assetid: b163b2e7-8f12-4cd2-a682-7b755f28792e
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_TargetPortal WMI Class


## <span id="ddk_iscsi_targetportal_wmi_class_kr"></span><span id="DDK_ISCSI_TARGETPORTAL_WMI_CLASS_KR"></span>


The ISCSI\_TargetPortal class defines a target portal. This definition includes a socket number and an IP address that is independent of the version of the IP protocol that the initiator and the target use.

This class is defined as follows in *Common.mof*.

```cpp
class ISCSI_TargetPortal {
  [WmiDataId(1), Description("Network Address") : amended]
    ISCSI_IP_Address  Address;
  [WmiDataId(2), Description("Socket number") : amended]
    uint16 Socket;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_TargetPortal**](https://msdn.microsoft.com/library/windows/hardware/ff561574) data structure.

 

 





