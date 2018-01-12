---
title: DSM\_Load\_Balance\_Policy\_V2 WMI Class
description: DSM\_Load\_Balance\_Policy\_V2 WMI Class
ms.assetid: 8895d0ca-b9bd-4f8d-bf8f-4ba2f459c264
---

# DSM\_Load\_Balance\_Policy\_V2 WMI Class


MPIO publishes the DSM\_LOAD\_Balance\_Policy\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. An MPIO driver uses the DSM\_LOAD\_Balance\_Policy\_V2 WMI class to identify the load balance policy that is applied to an MPIO disk.

```
class DSM_Load_Balance_Policy_V2
{

    //
    // Version information for futher changes.
    //
    [WmiDataId(1),
     read,
     Description("Version Number") : amended
    ]
    uint32 Version;

    //
    // Load Balance type.
    //
    [WmiDataId(2),
     Description("Load Balance Policy implemented by the DSM") : amended,
     Values{"Fail Over Only",
            "Round Robin",
            "Round Robin with Subset",
            "Dynamic Least Queue Depth",
            "Weighted Paths",
            "Least Blocks",
            "Vendor Specific"} : amended,

     DefineValues{"DSM_LB_FAILOVER",
                  "DSM_LB_ROUND_ROBIN",
                  "DSM_LB_ROUND_ROBIN_WITH_SUBSET",
                  "DSM_LB_DYN_LEAST_QUEUE_DEPTH",
                  "DSM_LB_WEIGHTED_PATHS",
                  "DSM_LB_LEAST_BLOCKS",
                  "DSM_LB_VENDOR_SPECIFIC"},
     ValueMap{"1", "2", "3", "4", "5", "6", "7"}
    ]
    uint32 LoadBalancePolicy;

    //
    // If load balance policy is DSM_LB_VENDOR_SPECIFIC then the following
    // properties are not used. The caller would need to provide data for
    // setting the vendor specific Load Balance policy.
    //

    //
    // Number of paths.
    //
    [WmiDataId(3),
     Description("Number of entries in DSM_Paths array") : amended
    ]
    uint32 DSMPathCount;

    [WmiDataId(4),
     Description("Reserved field") : amended
    ]
    uint32 Reserved;

    //
    // Paths&#39; array.
    //
    [WmiDataId(5),
     WmiSizeIs("DSMPathCount"),
     Description("DSM_Paths array") : amended
    ]
    MPIO_DSM_Path_V2 DSM_Paths[];
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**DSM\_Load\_Balance\_Policy\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff552698) data structure. There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20DSM_Load_Balance_Policy_V2%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




