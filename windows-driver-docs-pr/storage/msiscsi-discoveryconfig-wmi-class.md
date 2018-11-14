---
title: MSiSCSI\_DiscoveryConfig WMI Class
description: MSiSCSI\_DiscoveryConfig WMI Class
ms.assetid: dbf170ba-92ab-47bd-a076-5f54129305a5
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_DiscoveryConfig WMI Class


## <span id="ddk_msiscsi_discoveryconfig_wmi_class_kr"></span><span id="DDK_MSISCSI_DISCOVERYCONFIG_WMI_CLASS_KR"></span>


The MSiSCSI\_DiscoveryConfig WMI class reports what methods an initiator uses to do discovery.

This class is defined as follows in *Config.mof*.

```cpp
class MSiSCSI_DiscoveryConfig {
  [key] string  InstanceName;
  boolean  Active;
  [WmiDataId(1), read, write, description("HBA should
    perform target discovery via iSNS") : amended] 
    boolean  PerformiSNSDiscovery;
  [WmiDataId(2), read, write, description("HBA should 
    perform target discovery via SLP") : amended] 
    boolean  PerformSLPDiscovery;
  [WmiDataId(3), read, write, description("Automatic 
    discovery of iSNS server") : amended] 
    boolean  AutomaticiSNSDiscovery;
  [WmiDataId(4), read, write, MaxLen(256), 
    description("Default initiator name for registering with 
    iSNS") : amended] 
    string  InitiatorName;
  [WmiDataId(5), read, write, description("Fixed Addresses 
    of iSNS servers") : amended] 
    ISCSI_IP_Address  iSNSServer;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_DiscoveryConfig**](https://msdn.microsoft.com/library/windows/hardware/ff562991) data structure.

 

 





