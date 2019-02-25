---
title: MSiSCSI\_RADIUSConfig WMI Class
description: MSiSCSI\_RADIUSConfig WMI Class
ms.assetid: e0fd1fea-3d8c-4d25-a9fd-0e115ecb8163
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_RADIUSConfig WMI Class


## <span id="ddk_msiscsi_radiusconfig_wmi_class_kr"></span><span id="DDK_MSISCSI_RADIUSCONFIG_WMI_CLASS_KR"></span>


The MSiSCSI\_RADIUSConfig WMI class indicates whether an initiator uses the remote authentication dial-in user service (RADIUS) and provides information that the initiator requires to use the service.

Initiators use RADIUS servers to perform authentication during the challenge handshake of the challenge handshake authentication protocol (CHAP).

A miniport driver must implement the MSiSCSI\_RADIUSConfig class if the HBA that it manages supports using RADIUS for CHAP authentication.

You should use RADIUS whenever possible, because it allows centralized management of CHAP credentials.

Because the MSiSCSI\_RADIUSConfig WMI class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_RADIUSConfig class is defined in *Config.mof*.

```cpp
class MSiSCSI_RADIUSConfig {
  [key] string  InstanceName;
  boolean  Active;
  [WmiDataId(1), read, write, description("HBA should use 
    RADIUS for CHAP authentication") : amended] 
    boolean  UseRADIUSForCHAP;
  [WmiDataId(2), read, write, description("Size in bytes of 
    shared secret for RADIUS servers") : amended] 
    uint32  SharedSecretSizeInBytes;
  [WmiDataId(3), read, write, description("Fixed Addresses 
    of RADIUS server") : amended] 
    ISCSI_IP_Address  RADIUSServer;
  [WmiDataId(4), read, write, description("Fixed Addresses 
    of backup RADIUS server") : amended] 
    ISCSI_IP_Address  BackupRADIUSServer;
  [WmiDataId(5), read, write, 
    WmiSizeIs("SharedSecretSizeInBytes"), 
    description("Shared secret for RADIUS servers") :
    amended] 
    uint8 SharedSecret[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_RADIUSConfig**](https://msdn.microsoft.com/library/windows/hardware/ff563112) data structure.

 

 





