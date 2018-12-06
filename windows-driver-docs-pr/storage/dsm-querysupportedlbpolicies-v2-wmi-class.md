---
title: DSM\_QuerySupportedLBPolicies\_V2 WMI Class
description: DSM\_QuerySupportedLBPolicies\_V2 WMI Class
ms.assetid: d60cf06d-595b-425d-bf22-f0986267ba09
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DSM\_QuerySupportedLBPolicies\_V2 WMI Class


MPIO publishes the DSM\_QuerySupportedLBPolicies\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. A WMI client uses the DSM\_QuerySupportedLBPolicies\_V2 WMI class to query all the load balance policies that a DSM supports.

```cpp
class DSM_QuerySupportedLBPolicies_V2
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
    DSM_Load_Balance_Policy_V2 Supported_LB_Policies[];
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**DSM\_QuerySupportedLBPolicies\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff552735) data structure. There are no methods associated with this WMI class.

 

 





