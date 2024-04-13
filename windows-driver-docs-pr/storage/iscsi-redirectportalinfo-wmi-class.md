---
title: ISCSI_RedirectPortalInfo WMI Class
description: ISCSI\_RedirectPortalInfo WMI Class
ms.date: 10/17/2018
---

# ISCSI\_RedirectPortalInfo WMI Class


The ISCSI\_RedirectPortalInfo WMI class contains information about a collection of iSCSI portals. This class is defined as follows in *Mgmt.mof*.

```cpp
class ISCSI_RedirectPortalInfo
{
    [read,
     WmiDataId(1),
     Description("A uniquely generated connection ID. Do not confuse this with CID."): amended,
     WmiVersion(1)
     ] uint64 UniqueConnectionId;

    [read,
     WmiDataId(2),
     Description("Original Target IP Address given in the login"): amended,
     WmiVersion(1)] ISCSI_IP_Address OriginalIPAddr;

    [read,
     WmiDataId(3),
     Description("Original Target portal's socket number given in the login"): amended,
     WmiVersion(1)] uint32 OriginalPort;

    [read,
     WmiDataId(4),
     Description("Redirected Target IP Address"): amended,
     WmiVersion(1)] ISCSI_IP_Address RedirectedIPAddr;

    [read,
     WmiDataId(5),
     Description("Redirected Target portal's socket number"): amended,
     WmiVersion(1)] uint32 RedirectedPort;

    [read,
     WmiDataId(6),
     Description("TRUE if login was redirected. RedirectedIPAddr and RedirectedPort are valid then."): amended,
     WmiVersion(1)] uint8 Redirected;

    [read,
     WmiDataId(7),
     Description("TRUE if the redirection is temporary. FALSE otherwise"): amended,
     WmiVersion(1)] uint8 TemporaryRedirect;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_RedirectPortalInfo**](/windows-hardware/drivers/ddi/iscsimgt/ns-iscsimgt-_iscsi_redirectportalinfo) data structure.

 

