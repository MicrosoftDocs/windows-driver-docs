---
title: ISCSI\_TargetMapping WMI Class
description: ISCSI\_TargetMapping WMI Class
ms.assetid: b2c4634a-852b-471a-8764-025780e36c0f
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_TargetMapping WMI Class


## <span id="ddk_iscsi_targetmapping_wmi_class_kr"></span><span id="DDK_ISCSI_TARGETMAPPING_WMI_CLASS_KR"></span>


The ISCSI\_TargetMapping WMI class maps a collection of logical unit numbers (LUNs) that are locally defined on the initiator's host system to a group of 64-bit iSCSI LUNs. A 64-bit iSCSI LUN by itself does not uniquely identify the logical unit that it represents. However, an iSCSI LUN and the name of the target that the logical unit belongs to does uniquely identify the logical unit anywhere in the network.

Management applications can use the ISCSI\_TargetMapping WMI class to specify what LUNs will be assigned to a remote logical unit when it is enumerated locally.

The mapping that this class defines is associated with a particular target logon session. The [MSiSCSI\_TargetMappings WMI class](msiscsi-targetmappings-wmi-class.md) describes all of the mappings that are associated with a particular adapter instance.

This class is defined as follows in *Common.mof*.

```cpp
class ISCSI_TargetMapping {
  [WmiDataId(1), description("OS Scsi bus number target 
    is mapped to. If 0xffffffff then any value can be picked
    by the miniport.") : amended]
    uint32  OSBus;
  [WmiDataId(2), description("OS Scsi Target number target
    is mapped to. If 0xffffffff then any value can be picked
    by the miniport.") : amended]
    uint32  OSTarget;
  [WmiDataId(3), Description("Unique Session ID for the 
    target mapping") : amended] 
    uint64  UniqueSessionId;
  [WmiDataId(4), description("Count of LUNs mapped for this 
    target") : amended]
    uint32  LUNCount;
  [WmiDataId(5), MaxLen(MAX_ISCSI_NAME_LEN),
     description("Target Name") : amended]
    string  TargetName;
  [WmiDataId(6), Description("TRUE if session created from a
    persistent login") : amended]
    boolean  FromPersistentLogin;
  [WmiDataId(7), WmiSizeIs("LunCount"),
    description("List of LUNs mapped for this target") : 
    amended]
    ISCSI_LUNList  LUNList[];
};
```

 

 





