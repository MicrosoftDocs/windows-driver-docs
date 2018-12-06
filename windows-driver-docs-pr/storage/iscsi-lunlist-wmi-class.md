---
title: ISCSI\_LUNList WMI Class
description: ISCSI\_LUNList WMI Class
ms.assetid: 2ad0dabe-54b3-4075-966b-491e078f2c8b
ms.localizationpriority: medium
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

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_LUNList**](https://msdn.microsoft.com/library/windows/hardware/ff561544) data structure.

 

 





