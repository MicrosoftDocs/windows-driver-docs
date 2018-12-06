---
title: MSiSCSI\_TCPIPConfig WMI Class
description: MSiSCSI\_TCPIPConfig WMI Class
ms.assetid: 57451576-a900-4eaa-b229-bda79a81d014
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_TCPIPConfig WMI Class


## <span id="ddk_msiscsi_tcpipconfig_wmi_class_kr"></span><span id="DDK_MSISCSI_TCPIPCONFIG_WMI_CLASS_KR"></span>


The MSiSCSI\_TCPIPConfig WMI class reports TCP/IP configuration information about one of the HBA's IP addresses.

The adapter's miniport driver should create one instance of this class for each IP address that the adapter supports.

Because the MSiSCSI\_TCPIPConfig class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_TCPIPConfig class is defined in *Config.mof*.

```cpp
class MSiSCSI_TCPIPConfig {
  [key] string  InstanceName;
  boolean  Active;
  [read, write, WmiDataId(1), DisplayName("Use Link Local 
    Address") : amended, description("TRUE if the HBA should 
    use a link local address as its ip address") : amended] 
    boolean  UseLinkLocalAddress;
  [read, write, WmiDataId(2), displayName("DHCP Enabled") : 
    amended, description("TRUE if the HBA should use DHCP") 
    : amended] 
    boolean  EnableDHCP;
  [read, WmiDataId(3), description("IP Versions supported") 
    : amended, 
    BitValues{ "IPV4", "IPV6"},
    BitMap{"0x00000001", "0x00000002"}] 
    uint32  IPVersions;
  [read, write, WmiDataId(4), DisplayName("Static IP 
    Address") : amended, description("Static IP address for 
    the HBA") : amended]
    ISCSI_IP_Address  StaticIpAddress;
  [read, write, WmiDataId(5), DisplayName("Default Gateway") 
    : amended, Description("Static Default Gateway IP 
    address") : amended]
    ISCSI_IP_Address  DefaultGateway;
  [read, write, WmiDataId(6), DisplayName("Subnet Mask") : 
    amended, Description("Static Subnet Mask") : amended] 
    ISCSI_IP_Address  SubnetMask;
  [read, write, WmiDataId(7), DisplayName("Preferred DNS 
    Server") : amended, Description("Preferred DNS Server") 
    : amended] 
    ISCSI_IP_Address  PreferredDNSServer;
  [read, write, WmiDataId(8), DisplayName("Alternate DNS 
    Server") : amended, Description("Alternate DNS Server") 
    : amended] 
    ISCSI_IP_Address  AlternateDNSServer;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_TCPIPConfig**](https://msdn.microsoft.com/library/windows/hardware/ff563149) data structure.

 

 





