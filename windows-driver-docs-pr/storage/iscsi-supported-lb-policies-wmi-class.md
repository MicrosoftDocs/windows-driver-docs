---
title: ISCSI\_Supported\_LB\_Policies WMI Class
description: ISCSI\_Supported\_LB\_Policies WMI Class
ms.assetid: c11eebe8-519a-473d-9e9c-8a787333223e
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_Supported\_LB\_Policies WMI Class


The ISCSI\_Supported\_LB\_Policies WMI class contains information about the supported load balance policy for a multi connection iSCSI session. This class is defined as follows in *Mgmt.mof.*

```cpp
class ISCSI_Supported_LB_Policies {

    [WmiDataId(1),
     description("Id that is unique to this session within this adapter. ") : amended
    ]
    uint64 UniqueSessionId;

    [WmiDataId(2),
     Description("Load Balance policy supported by the iSCSI Initiator") : amended,
     Values{"Fail Over Only",
            "Round Robin",
            "Round Robin with Subset",
            "Dynamic Least Queue Depth",
            "Weighted Paths",
            "Vendor Specific"} : amended,
     DefineValues{"MSiSCSI_LB_FAILOVER",
                  "MSiSCSI_LB_ROUND_ROBIN",
                  "MSiSCSI_LB_ROUND_ROBIN_WITH_SUBSET",
                  "MSiSCSI_LB_DYN_LEAST_QUEUE_DEPTH",
                  "MSiSCSI_LB_WEIGHTED_PATHS",
                  "MSiSCSI_LB_VENDOR_SPECIFIC"},
     ValueMap{"1", "2", "3", "4", "5", "6"}
    ] 
    uint32 LoadBalancePolicy;
 
    //
    // If load balance policy is MSiSCSI_LB_VENDOR_SPECIFIC then 
    // the following properties are not used. Instead the caller would 
    // need to provide data for setting the vendor specific
    // Load Balance policy.
    //
    [WmiDataId(3),
     Description("Number of entries in MSiSCSI_Paths array") : amended
    ]

    uint32 iSCSI_PathCount;

    [WmiDataId(4),
     WmiSizeIs("iSCSI_PathCount"),
     Description("Describes iSCSI Initiator Paths") : amended
    ]
    ISCSI_Path iSCSI_Paths[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_Supported\_LB\_Policies**](https://msdn.microsoft.com/library/windows/hardware/ff561570) data structure.

 

 





