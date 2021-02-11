---
title: DSM\_QueryLBPolicy\_V2 WMI Class
description: DSM\_QueryLBPolicy\_V2 WMI Class
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DSM\_QueryLBPolicy\_V2 WMI Class


MPIO publishes the DSM\_QUERYLBPolicy\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. A WMI client uses the DSM\_QUERYLBPolicy\_V2 WMI class to query the load balance policy that is set for an MPIO disk.

```cpp
class DSM_QueryLBPolicy_V2
{

    [key, read]
    string InstanceName;

    [read]
    boolean Active;

    [WmiDataId(1),
     DisplayName("Load Balance Policy") : amended,
     Description("Load Balance Policy that is currently being used by DSM") : amended
    ]
    DSM_Load_Balance_Policy_V2 LoadBalancePolicy;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**DSM\_QueryLBPolicy\_V2**](/windows-hardware/drivers/ddi/mpiodisk/ns-mpiodisk-_dsm_querylbpolicy_v2) data structure. There are no methods associated with this WMI class.

 

