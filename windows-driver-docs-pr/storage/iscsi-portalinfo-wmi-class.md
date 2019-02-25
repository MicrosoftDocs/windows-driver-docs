---
title: ISCSI\_PortalInfo WMI Class
description: ISCSI\_PortalInfo WMI Class
ms.assetid: b38aa87c-00a5-483e-aa44-23f359783829
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_PortalInfo WMI Class


## <span id="ddk_iscsi_portalinfo_wmi_class_kr"></span><span id="DDK_ISCSI_PORTALINFO_WMI_CLASS_KR"></span>


The ISCSI\_PortalInfo WMI class contains information that is related to an iSCSI portal. This class is defined as follows in *Mgmt.mof*.

```cpp
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

 

 





