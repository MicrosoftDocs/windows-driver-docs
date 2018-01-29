---
title: ISCSI\_IP\_Address WMI Class
description: ISCSI\_IP\_Address WMI Class
ms.assetid: 3ceeb54f-ecc5-40c5-b0a8-8c6f86203f1c
---

# ISCSI\_IP\_Address WMI Class


## <span id="ddk_iscsi_ip_address_wmi_class_kr"></span><span id="DDK_ISCSI_IP_ADDRESS_WMI_CLASS_KR"></span>


The ISCSI\_IP\_Address class provides a definition of IP addresses that is independent of the version of the IP protocol that is in use. This class is defined in *Common.mof*.

```
class ISCSI_IP_Address {
  [WmiDataId(1), read, write, DisplayName("Address Format")
    : amended, description("Type of address specified. 
    It can be text: a DNS or dotted address or it can be
    a binary ipv4 or ipv6 address") : amended,
    Values{ "Text Address", "IpV4 Address",
            "IpV6 Address", "Empty Address"},
    ValueMap{"0", "1", "2", "3"}]
#define ISCSIIPADDRESSTYPE  uint32
  ISCSIIPADDRESSTYPE  Type;
  [WmiDataId(2), read, write, DisplayInHex,
    DisplayName("IPV4 Address"): amended,
    description("If IPV4 Address is specified as the 
    Address Format then this contains the binary IPv4 
    ip address") : amended]
    uint32  IpV4Address;
  [WmiDataId(3), DisplayName("IPV6 Address"): amended,
    read, write, description("If IPV6 Address is 
    specified as the Address Format then this contains 
    the binary IPv6 ip address") : amended]
    uint8  IpV6Address[16];
  [WmiDataId(4), read, write,
    DisplayName("IPV6 Flow Information") : amended,
    description("IPV6 flow information") : amended]
    uint32  IpV6FlowInfo;
  [WmiDataId(5), read, write,
    DisplayName("IPV6 Scope Id") : amended,
    description("IPV6 scope id") : amended]
    uint32  IpV6ScopeId;
  [WmiDataId(6), read, write,
    DisplayName("Text Address") : amended,
    description("Text address, either a DNS address or
    dotted address") : amended, 
    MaxLen(MAX_ISCSI_TEXT_ADDRESS_LEN)]
    string  TextAddress;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_IP\_Address**](https://msdn.microsoft.com/library/windows/hardware/ff561536) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ISCSI_IP_Address%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




