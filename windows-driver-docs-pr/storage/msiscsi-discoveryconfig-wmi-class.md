---
title: MSiSCSI\_DiscoveryConfig WMI Class
description: MSiSCSI\_DiscoveryConfig WMI Class
ms.assetid: dbf170ba-92ab-47bd-a076-5f54129305a5
---

# MSiSCSI\_DiscoveryConfig WMI Class


## <span id="ddk_msiscsi_discoveryconfig_wmi_class_kr"></span><span id="DDK_MSISCSI_DISCOVERYCONFIG_WMI_CLASS_KR"></span>


The MSiSCSI\_DiscoveryConfig WMI class reports what methods an initiator uses to do discovery.

This class is defined as follows in *Config.mof*.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_DiscoveryConfig%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




