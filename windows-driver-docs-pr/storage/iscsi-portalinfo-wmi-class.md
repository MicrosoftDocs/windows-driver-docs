---
title: ISCSI\_PortalInfo WMI Class
description: ISCSI\_PortalInfo WMI Class
ms.assetid: b38aa87c-00a5-483e-aa44-23f359783829
---

# ISCSI\_PortalInfo WMI Class


## <span id="ddk_iscsi_portalinfo_wmi_class_kr"></span><span id="DDK_ISCSI_PORTALINFO_WMI_CLASS_KR"></span>


The ISCSI\_PortalInfo WMI class contains information that is related to an iSCSI portal. This class is defined as follows in *Mgmt.mof*.

```
class ISCSI_PortalInfo
{
    [read,
     WmiDataId(1),
     description("An integer used to uniquely identify a paticular port"),
     WmiVersion(1)] uint32 Index;

    [read,
     WmiDataId(2),
     ISCSI_PORTAL_TYPE_QUALIFIERS,
     description("**typedef** The type of portal (Initiator or Target) \n"),
     WmiVersion(1)] ISCSI_PORTAL_TYPE PortalType;

    [read,
     WmiDataId(3),
     ISCSI_CONNECTION_PROTOCOL_TYPE_QUALIFIERS,
     //Description("The portal&#39;s transport protocol"): amended,
     description("The portal&#39;s transport protocol"),
     WmiVersion(1)] ISCSI_CONNECTION_PROTOCOL_TYPE Protocol;

    [read,
     WmiDataId(4),
     WmiVersion(1)] uint8 Reserved1;

    [read,
     WmiDataId(5),
     WmiVersion(1)] uint8 Reserved2;
 
    [read,
     WmiDataId(6),
     description("The portal&#39;s network address"),
     WmiVersion(1)] ISCSI_IP_Address IPAddr;

    [read,
     WmiDataId(7),
     description("The portal&#39;s socket number"),
     WmiVersion(1)] uint32 Port;

    [read,
     WmiDataId(8),
     description("The portal&#39;s aggregation tag"),
     WmiVersion(1)] uint16 PortalTag;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_PortalInfo**](https://msdn.microsoft.com/library/windows/hardware/ff561557) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ISCSI_PortalInfo%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




