---
title: ISCSI\_TargetPortalGroup WMI Class
description: ISCSI\_TargetPortalGroup WMI Class
ms.assetid: dff17d52-b308-49cc-97ec-d54eddb4e747
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_TargetPortalGroup WMI Class


## <span id="ddk_iscsi_targetportalgroup_wmi_class_kr"></span><span id="DDK_ISCSI_TARGETPORTALGROUP_WMI_CLASS_KR"></span>


The ISCSI\_TargetPortalGroup class defines a target portal group.

This class is defined as follows in *Common.mof*.

```cpp
class ISCSI_TargetPortalGroup {
  [WmiDataId(1), description("Number of portals in group") :
    amended]
    uint32  PortalCount;
  [WmiDataId(2), WmiSizeIs("PortalCount"),
    description("Target portals in group") : amended]
    ISCSI_TargetPortal  Portals[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_TargetPortalGroup**](https://msdn.microsoft.com/library/windows/hardware/ff561575) data structure.

 

 





