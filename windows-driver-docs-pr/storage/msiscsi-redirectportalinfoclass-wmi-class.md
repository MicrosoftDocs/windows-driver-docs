---
title: MSiSCSI\_RedirectPortalInfoClass WMI Class
description: MSiSCSI\_RedirectPortalInfoClass WMI Class
ms.assetid: 38f510ed-1f31-4b3c-84c6-515f5d42a1f8
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_RedirectPortalInfoClass WMI Class


The MSiSCSI\_RedirectPortalInfoClass WMI class contains a collection of sessions for an adapter ID. Additionally, it contains the portal redirect information for each of the sessions. This class is defined as follows in *Mgmt.mof.*

```cpp
class MSiSCSI_RedirectPortalInfoClass
{
    [read,key] String InstanceName;

    [read] boolean Active;

    [read,
     WmiDataId(1),
     DisplayName("Adapter Id") : amended,
     DisplayInHex,
     description("Id that is globally unique for all instances of iSCSI initiators.") : amended,
     WmiVersion(1)
    ]
    uint64 UniqueAdapterId;

    [read,
     WmiDataId(2),
     DisplayName("Number of session on the adapter : Number of elements in RedirectSessionInfo array") : amended,
     Description("Number of elements in RedirectSessionInfo array") : amended,
     WmiVersion(1)
    ] uint32 SessionCount;

    [read,
     WmiDataId(3),
     DisplayName("List Of ISCSI_RedirectSessionInfo ") : amended,
     Description("Variable length array of ISCSI_RedirectSessionInfo. SessionCount specifies the number of elements in the array. NOTE: this is a variable length array.") : amended,
     WmiSizeIs("SessionCount"),
     WmiVersion(1)
    ] ISCSI_RedirectSessionInfo RedirectSessionList[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_RedirectPortalInfoClass**](https://msdn.microsoft.com/library/windows/hardware/ff563117) data structure.

 

 





