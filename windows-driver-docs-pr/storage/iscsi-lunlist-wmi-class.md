---
title: ISCSI_LUNList WMI Class
description: ISCSI\_LUNList WMI Class
ms.date: 10/17/2018
---

# ISCSI\_LUNList WMI Class


## <span id="ddk_iscsi_lunlist_wmi_class_kr"></span><span id="DDK_ISCSI_LUNLIST_WMI_CLASS_KR"></span>


The ISCSI\_LUNList WMI class describes a mapping from a logical unit number (LUN) that the operating system defines locally to be a 64-bit number that, together with the name of the target that the logical unit belongs to, uniquely identifies the logical unit and is globally valid anywhere in the network. This class is defined as follows in *Common.mof*.

```cpp
class ISCSI_LUNList {
  [WmiDataId(1), description("Target LUN") : amended]
    uint64  TargetLUN;
  [WmiDataId(2), description("OS Scsi bus number target
  is mapped to") : amended]
    uint32  OSLUN;
  [WmiDataId(3), description("Reserved") : amended]
    uint32  Reserved;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_LUNList**](/windows-hardware/drivers/ddi/iscsidef/ns-iscsidef-_iscsi_lunlist) data structure.

 

