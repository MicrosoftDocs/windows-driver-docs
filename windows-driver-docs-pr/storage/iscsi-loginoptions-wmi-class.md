---
title: ISCSI\_LoginOptions WMI Class
description: ISCSI\_LoginOptions WMI Class
ms.assetid: dc05f8e9-599d-4963-98a8-64e1d23c37a1
---

# ISCSI\_LoginOptions WMI Class


## <span id="ddk_iscsi_loginoptions_wmi_class_kr"></span><span id="DDK_ISCSI_LOGINOPTIONS_WMI_CLASS_KR"></span>


The ISCSI\_LoginOptions class describes the characteristics of a target logon session. This class is defined as follows in *Common.mof*.

```
class ISCSI_LoginOptions {
  [WmiDataId(1),
     description("Bit flags that specify which login 
     option values are specified") : amended,
     ISCSI_LOGIN_OPTIONS_INFO_QUALIFIERS,
     cpp_quote(ISCSI_LOGIN_OPTIONS_INFO_CPPQUOTE)]
     ISCSI_LOGIN_OPTIONS_INFO_SPECIFIED  
       InformationSpecified;
  [WmiDataId(2), 
     ValueMap{ ISCSI_DIGEST_TYPE_NONE,
               ISCSI_DIGEST_TYPE_CRC32C }, 
     Values{ "None", "CRC32C" },
     description("cyclic integrity checksums that can 
     be negotiated for the header digests") : amended]
     uint32  HeaderDigest;
  [WmiDataId(3),
     ValueMap{ ISCSI_DIGEST_TYPE_NONE,
               ISCSI_DIGEST_TYPE_CRC32C },
     Values{ "None", "CRC32C" },
     description("cyclic integrity checksums that can 
     be negotiated for the header digests") : amended]
     uint32  DataDigest;
  [WmiDataId(4),
    Description("Maximum number of connections, 0 implies 
    no limit") : amended]
    uint32  MaximumConnections;
  [WmiDataId(5),
    Description("The initiator and target negotiate 
    the minimum time, in seconds, to wait before 
    attempting an explicit/implicit logout or active 
    task reassignment after an unexpected connection
    termination or a connection reset.") : amended]
    uint32  DefaultTime2Wait;
  [WmiDataId(6),
    Description(" The initiator and target negotiate the
    maximum time, in seconds after an initial wait
    (Time2Wait), before which an explicit/implicit
    connection Logout or active task reassignment is still
    possible after an unexpected connection termination or
    a connection reset.") : amended]
    uint32  DefaultTime2Retain;
  [WmiDataId(7),
    Description("Flags that affect how login occurs") :
    amended, cpp_quote(ISCSI_LOGIN_FLAGS_CPPQUOTE),
                       ISCSI_LOGIN_FLAGS_QUALIFIERS]
    ISCSI_LOGIN_FLAGS  LoginFlags;
  [WmiDataId(8),
    Description("Authentication method specified for login")
    : amended, ISCSI_AUTH_TYPES_QUALIFIERS]
    ISCSI_AUTH_TYPES  AuthType;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_LoginOptions**](https://msdn.microsoft.com/library/windows/hardware/ff561541) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ISCSI_LoginOptions%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




