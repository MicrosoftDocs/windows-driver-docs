---
title: DSM\_QuerySupportedLBPolicies WMI Class
description: DSM\_QuerySupportedLBPolicies WMI Class
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DSM\_QuerySupportedLBPolicies WMI Class


MPIO publishes the DSM\_QuerySupportedLBPolicies\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. A WMI client uses the DSM\_QuerySupportedLBPolicies\_V2 WMI class to query all the load balance policies that a DSM supports.

```cpp
class DSM_QuerySupportedLBPolicies
{

    [key, read]
    string InstanceName;

    [read]
    boolean Active;

    [WmiDataId(1),
     Description("Number of supported Load Balance policies") : amended
    ]
    uint32 SupportedLBPoliciesCount;

    [WmiDataId(2),
     Description("Reserved") : amended
    ]
    uint32 Reserved;

    [WmiDataId(3),
     WmiSizeIs("SupportedLBPoliciesCount"),
     Description("Supported Load Balance Policies array") : amended
    ]
    DSM_Load_Balance_Policy Supported_LB_Policies[];
};
```

When this class definition compiled by the WMI tool suite, this class definition produces the [**DSM\_QuerySupportedLBPolicies**](/windows-hardware/drivers/ddi/mpiodisk/ns-mpiodisk-_dsm_querysupportedlbpolicies) data structure. There are no methods associated with this WMI class.

 

