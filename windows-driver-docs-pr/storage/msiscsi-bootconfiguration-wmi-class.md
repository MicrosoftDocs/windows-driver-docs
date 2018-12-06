---
title: MSiSCSI\_BootConfiguration WMI Class
description: MSiSCSI\_BootConfiguration WMI Class
ms.assetid: 5ca350ba-8689-46c2-8313-8f523354db98
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_BootConfiguration WMI Class


## <span id="ddk_msiscsi_bootconfiguration_wmi_class_kr"></span><span id="DDK_MSISCSI_BOOTCONFIGURATION_WMI_CLASS_KR"></span>


The MSiSCSI\_BootConfiguration WMI class describes how a boot device is configured.

This class is defined as follows in *Config.mof*.

```cpp
class MSiSCSI_BootConfiguration {
  [key] string  InstanceName;
  boolean  Active;
  [read, write, WmiDataId(1), Description("LUN on target of 
    boot device") : amended, DisplayName("Target LUN") : 
    amended] 
    uint64  LUN;
  [read, write, WmiDataId(2), SECURITY_FLAG_QUALIFIERS] 
    ISCSI_SECURITY_FLAGS  SecurityFlags;
  [read, write, WmiDataId(3), description("Size in bytes of 
    Target Username") : amended] 
    uint32  UsernameSize;
  [read, write, WmiDataId(4), description("Size in bytes of 
    Target Password") : amended] 
    uint32  PasswordSize;
  [read, write, WmiDataId(5), description("If TRUE 
    dynamically discover boot device") : amended] 
    boolean  DiscoverBootDevice;
  [read, write, WmiDataId(6), MaxLen(MAX_ISCSI_NAME_LEN), 
    description("The InitiatorNode specifies the iScsi name 
    of the initiator node to use for the connection. If 
    empty, then the HBA can choose any initiator node") : 
    amended] 
    string  InitiatorNode;
  [read, write, WmiDataId(7), MaxLen(MAX_ISCSI_NAME_LEN), 
    description("TargetName specifies the iScsi target name 
    to which a session should be established.") : amended] 
    string TargetName;
  [read, write, WmiDataId(8), description("Portal to use for 
    initial connection") : amended] 
    ISCSI_TargetPortal  TargetPortal;
  [read, write, WmiDataId(9), description("Login options") : 
    amended] 
    ISCSI_LoginOptions  LoginOptions;
  [read, write, WmiDataId(10), WmiSizeIs("UsernameSize"),
    description("Authentication Username, for CHAP this 
    is the CHAP Name (CHAP_N) when authenticating the 
    target") : amended] 
    uint8  Username[];
  [read, write, WmiDataId(11), WmiSizeIs("PasswordSize"), 
    description("Authentication Password, for CHAP this is 
    the shared secret to use when generating the response to 
    the target challenge") : amended] 
    uint8  Password[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_BootConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff562976) data structure.

 

 





