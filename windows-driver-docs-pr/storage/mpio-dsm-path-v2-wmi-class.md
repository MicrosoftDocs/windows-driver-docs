---
title: MPIO\_DSM\_Path\_V2 WMI Class
description: MPIO\_DSM\_Path\_V2 WMI Class
ms.assetid: ec7d75a0-cb40-46e8-ab1d-137a9331193e
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_DSM\_Path\_V2 WMI Class


MPIO publishes the MPIO\_DSM\_Path\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. An MPIO driver uses the MPIO\_DSM\_Path\_V2 WMI class to identify the path ID as reported by a DSM.

```cpp
class MPIO_DSM_Path_V2
{
    //
    // Unique identifier to distinguish paths known to the DSM.
    // This is what is returned to MPIO during DsmSetDeviceInfo.
    //
    [WmiDataId(1),
     Description("DSM Path Id") : amended
    ]
    uint64 DsmPathId;

    //
    // Reserved.
    //
    [WmiDataId(2),
     Description("Reserved field") : amended
    ]
    uint64 Reserved;

    //
    // Value that determines which path the DSM picks if the load balance is
    // Weighted Paths.
    //
    [WmiDataId(3),
     Description("Weight assigned to the path") : amended
    ]
    uint32 PathWeight;

    //
    // Flag to indicate if this is a primary path.
    // ActiveOptimized and ActiveUnoptimized paths must set this to TRUE.
    //
    [WmiDataId(4),
     Description("Flag set to TRUE if the path is a primary path. Else FALSE. Used in conjunction with the OptimizedPath flag.") : amended
    ]
    uint32 PrimaryPath;

    //
    // Flag to indicate if this is an optimized path.
    // ActiveOptimized and StandBy paths must set this to TRUE.
    // Even though a StandBy path doesn&#39;t actually provide optimal access to the
    // device, it must set this flag to TRUE. This is due to the fact that this
    // flag is used in conjunction with the PrimaryPath flag to form a two bit
    // boolean representation of the access states (AO, AU, SB, UA).
    //
    [WmiDataId(5),
     Description("Flag set to TRUE if access to device is optimized through this path. Else FALSE. Used in conjunction with the PrimaryPath flag.") : amended
    ]
    uint32 OptimizedPath;

    //
    // Flag to indicate whether this is the Preferred Path for access device. It
    // has relevance only in the Failover-only Load Balance policy. If this path
    // fails and then comes back online after failover to another path completes,
    // failback to this path will occur.
    //
    [WmiDataId(6),
     Description("Flag set to TRUE if this path is the preferred path for the device. It has relevance only in the FailOver-Only Load Balance Policy.") : amended
    ]
    uint32 PreferredPath;

    //
    // Flag to indicate if the path is currently in a Failed state.
    //
    [WmiDataId(7),
     Description("Flag set to TRUE if the path is online but in a Failed state.") : amended
    ]
    uint32 FailedPath;

    //
    // TargetPortGroup&#39;s asymmetric access state
    //
    [WmiDataId(8),
     Description("Target Port Group&#39;s Asymmetric Access State") : amended,
     Values{"Active/Optimized",
            "Active/Unoptimized",
            "Standby",
            "Unavailable",
            "Not Used"} : amended,

     DefineValues{"STATE_ACTIVE_OPTIMIZED",
                  "STATE_ACTIVE_UNOPTIMIZED",
                  "STATE_STANDBY",
                  "STATE_UNAVAILABLE",
                  "STATE_NOT_USED"},
     ValueMap{"0", "1", "2", "3", "16"}
    ]
    uint32 TargetPortGroup_State;

    //
    // Indicates the device&#39;s ALUA transition support
    //
    [WmiDataId(9),
     Description("Device&#39;s Asymmetric Logical Unit Access state transition support") : amended,
     Values{"ALUA Not Supported",
            "ALUA Implicit Only",
            "ALUA Explicit Only",
            "ALUA Implicit and Explicit"} : amended,

     DefineValues{"ALUA_NOT_SUPPORTED",
                  "ALUA_IMPLICIT_ONLY",
                  "ALUA_EXPLICIT_ONLY",
                  "ALUA_IMPLICIT_AND_EXPLICIT"},
     ValueMap{"0", "1", "2", "3"}
    ]
    uint32 ALUASupport;

    //
    // Flag to indicate if LU access is symmetric or asymmetric
    //
    [WmiDataId(10),
     Description("Flag set to TRUE if access to logical unit is symmetric") : amended
    ]
    uint8 SymmetricLUA;

    //
    // Flag to indicate if the Target Port Group is preferred
    //
    [WmiDataId(11),
     Description("Flag set to TRUE if the Target Port Group is preferred for the logical unit") : amended
    ]
    uint8 TargetPortGroup_Preferred;

    //
    // Target Port Group Identifier
    //
    [WmiDataId(12),
     Description("Target Port Group Identifier") : amended
    ]
    uint16 TargetPortGroup_Identifier;

    //
    // Identifier of the Target Port corresponding to this path through which the LUN is exposed
    //
    [WmiDataId(13),
     Description("Target Port Identifier") : amended
    ]
    uint32 TargetPort_Identifier;

    //
    // Reserved.
    //
    [WmiDataId(14),
     Description("Reserved field") : amended
    ]
    uint32 Reserved32;

    //
    // Reserved.
    //
    [WmiDataId(15),
     Description("Reserved field") : amended
    ]
    uint64 Reserved64;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_DSM\_Path\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff562386) data structure. There are no methods associated with this WMI class.

 

 





