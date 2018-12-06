---
title: MSiSCSI\_LB\_Operations WMI Class
description: MSiSCSI\_LB\_Operations WMI Class
ms.assetid: 75c93040-52bf-4e9c-a503-a87f382ee1c9
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_LB\_Operations WMI Class


The MSiSCSI\_LB\_Operations WMI class contains methods to set and retrieve the load balance policies. This class is defined as follows in Mgmt.mof.

```cpp
class MSiSCSI_LB_Operations {

    [key, read]
    string InstanceName;

    [read] 
    boolean Active;

    //
    // Method to set load balance policy for the iSCSI Initiator
    //
    [WmiMethodId(10),
     Implemented,
     Description("Sets Load Balance Policy for the iSCSI Initiator") : amended,
     cpp_quote(
       "//\n"
       "// SetLoadBalancePolicy instructs the iSCSI Initiator what Load Balance\n"
       "// policy to use.\n"
       "//\n"
              )            
    ]
    void SetLoadBalancePolicy(
        [in,
         Description("New Load Balance policy to be set")
        ] ISCSI_Supported_LB_Policies LoadBalancePolicies,

        [out,
         Description("Status of the operation")
        ] uint32 Status
    );
};
```

When the WMI tool suite compiles the preceding class definition, it produces one of the [MSiSCSI\_LB\_Operations](https://msdn.microsoft.com/library/windows/hardware/ff563059) data structures.

 

 





