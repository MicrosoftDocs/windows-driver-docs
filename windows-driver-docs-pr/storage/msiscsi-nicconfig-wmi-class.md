---
title: MSiSCSI\_NICConfig WMI Class
description: MSiSCSI\_NICConfig WMI Class
ms.assetid: 9b7a466d-a9bb-41c5-8f38-e5baf21e863a
---

# MSiSCSI\_NICConfig WMI Class


## <span id="ddk_msiscsi_nicconfig_wmi_class_kr"></span><span id="DDK_MSISCSI_NICCONFIG_WMI_CLASS_KR"></span>


The MSiSCSI\_NICConfig WMI class describes a network interface card (NIC) port.

The miniport driver for the HBA initiator must create one instance of the MSiSCSI\_NICConfig class for each port on the HBA.

The MSiSCSI\_NICConfig class is defined in *Config.mof*.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_NICConfig%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




