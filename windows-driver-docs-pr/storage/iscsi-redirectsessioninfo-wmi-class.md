---
title: ISCSI_RedirectSessionInfo WMI Class
description: ISCSI\_RedirectSessionInfo WMI Class
ms.date: 10/17/2018
---

# ISCSI\_RedirectSessionInfo WMI Class


The ISCSI\_RedirectSessionInfo WMI class contains a collection of connections for an iSCSI session. This class is defined as follows in *Mgmt.mof.*

```cpp
class ISCSI_RedirectSessionInfo
{
    [read,
     WmiDataId(1),
     Description("A uniquely generated session ID, it is the same id returned by the LoginToTarget method.  Do not confuse this with ISID or SSID."): amended,
     WmiVersion(1)] uint64 UniqueSessionId;

    [read,
     WmiDataId(2),
     Description("Target portal group tag for this Session "): amended,
     WmiVersion(1)] uint32 TargetPortalGroupTag;

    [read,
     WmiDataId(3),
     DisplayName("Number of elements in RedirectPortalList array") : amended,
     cpp_quote("\n    // Number of elements in RedirectPortalList array\n"),
     Description("Number of elements in RedirectPortalList array") : amended,
     WmiVersion(1)
    ] uint32 ConnectionCount;

    [read,
     WmiDataId(4),
     DisplayName("Redirect Portal info for each connection") : amended,
     Description("Redirect portal info - one element for each connection in the session") : amended,
     WmiSizeIs("ConnectionCount"),
     WmiVersion(1)
    ] ISCSI_RedirectPortalInfo RedirectPortalList[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_RedirectSessionInfo**](/windows-hardware/drivers/ddi/iscsimgt/ns-iscsimgt-_iscsi_redirectsessioninfo) data structure.

 

