---
title: MSiSCSI\_NICConfig WMI Class
description: MSiSCSI\_NICConfig WMI Class
ms.assetid: 9b7a466d-a9bb-41c5-8f38-e5baf21e863a
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_NICConfig WMI Class


## <span id="ddk_msiscsi_nicconfig_wmi_class_kr"></span><span id="DDK_MSISCSI_NICCONFIG_WMI_CLASS_KR"></span>


The MSiSCSI\_NICConfig WMI class describes a network interface card (NIC) port.

The miniport driver for the HBA initiator must create one instance of the MSiSCSI\_NICConfig class for each port on the HBA.

The MSiSCSI\_NICConfig class is defined in *Config.mof*.

```cpp
class MSiSCSI_NICConfig {
  [key] string  InstanceName;
  boolean  Active;
  [read, WmiDataId(1), DisplayName("Link Speed") : amended, 
    Description("Speed of network link in megabits per 
    second") : amended] 
    uint32  LinkSpeed;
  [read, WmiDataId(2), DisplayName("Max Link Speed") : 
    amended, Description("Maximum Speed of network link in 
    megabits per second") : amended] 
    uint32  MaxLinkSpeed;
  [read, WmiDataId(3), DisplayName("Link State") : amended, 
    description("Link State") : amended, 
    Values{"Media Disconnected", "Media Connected"} : 
    amended,
    ValueMap{"0", "1"}] 
    uint32  LinkState;
  [read, WmiDataId(4), DisplayName("Max Frame Size") : 
    amended, description("Maximum frame size") : amended] 
    uint32  MaxFrameSize;
  [read, WmiDataId(5), DisplayName("MAC Address") : amended, 
    description("Ethernet MAC Address") : amended] 
    uint8  MacAddress[6];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_NICConfig**](https://msdn.microsoft.com/library/windows/hardware/ff563079) data structure.

 

 





