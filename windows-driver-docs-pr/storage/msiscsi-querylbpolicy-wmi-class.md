---
title: MSiSCSI_QueryLBPolicy WMI Class
description: MSiSCSI\_QueryLBPolicy WMI Class
ms.date: 10/17/2018
---

# MSiSCSI\_QueryLBPolicy WMI Class


The MSiSCSI\_QueryLBPolicy WMI class contains information about the load balance policies. This class is defined as follows in *Mgmt.mof.*

```cpp
class MSiSCSI_QueryLBPolicy 
{
    [key]
    string InstanceName;

    boolean Active;

    [WmiDataId(1),
     DisplayName("Adapter Id") : amended,
     DisplayInHex,
     Description("Id that is globally unique to each instance of each adapter. Using the address of the Adapter Extension is a good idea.") : amended
    ]
    uint64 UniqueAdapterId;

    [WmiDataId(2),
     read,
     DisplayName("Reserved field") : amended
    ] uint32 Reserved;

    [WmiDataId(3),
     read,
     DisplayName("Count of Elements in LoadBalancePolicies array") : amended,
     cpp_quote("\n    // Number of elements in LoadBalancePolicies array\n"),
     Description("Number of elements in LoadBalancePolicies array") : amended
    ] uint32 SessionCount;

    [WmiDataId(4),
     DisplayName("Load Balance Policy for each session") : amended,
     description("Load Balance Policy that is currently being used by iSCSI Initiator - one element for each session on the adapter") : amended,
     WmiSizeIs("SessionCount")
    ]
    ISCSI_Supported_LB_Policies LoadBalancePolicies[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_QueryLBPolicy**](/windows-hardware/drivers/ddi/iscsimgt/ns-iscsimgt-_msiscsi_querylbpolicy) data structure.

 

