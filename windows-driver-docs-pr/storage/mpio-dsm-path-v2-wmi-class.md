---
title: MPIO\_DSM\_Path\_V2 WMI Class
description: MPIO\_DSM\_Path\_V2 WMI Class
ms.assetid: ec7d75a0-cb40-46e8-ab1d-137a9331193e
---

# MPIO\_DSM\_Path\_V2 WMI Class


MPIO publishes the MPIO\_DSM\_Path\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. An MPIO driver uses the MPIO\_DSM\_Path\_V2 WMI class to identify the path ID as reported by a DSM.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MPIO_DSM_Path_V2%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




