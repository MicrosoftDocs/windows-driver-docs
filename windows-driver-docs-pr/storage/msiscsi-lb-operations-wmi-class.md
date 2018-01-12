---
title: MSiSCSI\_LB\_Operations WMI Class
description: MSiSCSI\_LB\_Operations WMI Class
ms.assetid: 75c93040-52bf-4e9c-a503-a87f382ee1c9
---

# MSiSCSI\_LB\_Operations WMI Class


The MSiSCSI\_LB\_Operations WMI class contains methods to set and retrieve the load balance policies. This class is defined as follows in Mgmt.mof.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_LB_Operations%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




