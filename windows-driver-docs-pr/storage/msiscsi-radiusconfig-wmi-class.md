---
title: MSiSCSI\_RADIUSConfig WMI Class
description: MSiSCSI\_RADIUSConfig WMI Class
ms.assetid: e0fd1fea-3d8c-4d25-a9fd-0e115ecb8163
---

# MSiSCSI\_RADIUSConfig WMI Class


## <span id="ddk_msiscsi_radiusconfig_wmi_class_kr"></span><span id="DDK_MSISCSI_RADIUSCONFIG_WMI_CLASS_KR"></span>


The MSiSCSI\_RADIUSConfig WMI class indicates whether an initiator uses the remote authentication dial-in user service (RADIUS) and provides information that the initiator requires to use the service.

Initiators use RADIUS servers to perform authentication during the challenge handshake of the challenge handshake authentication protocol (CHAP).

A miniport driver must implement the MSiSCSI\_RADIUSConfig class if the HBA that it manages supports using RADIUS for CHAP authentication.

You should use RADIUS whenever possible, because it allows centralized management of CHAP credentials.

Because the MSiSCSI\_RADIUSConfig WMI class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_RADIUSConfig class is defined in *Config.mof*.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_RADIUSConfig%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




