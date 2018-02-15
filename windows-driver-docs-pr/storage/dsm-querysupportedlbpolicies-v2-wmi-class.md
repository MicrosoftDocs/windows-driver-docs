---
title: DSM\_QuerySupportedLBPolicies\_V2 WMI Class
description: DSM\_QuerySupportedLBPolicies\_V2 WMI Class
ms.assetid: d60cf06d-595b-425d-bf22-f0986267ba09
---

# DSM\_QuerySupportedLBPolicies\_V2 WMI Class


MPIO publishes the DSM\_QuerySupportedLBPolicies\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. A WMI client uses the DSM\_QuerySupportedLBPolicies\_V2 WMI class to query all the load balance policies that a DSM supports.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20DSM_QuerySupportedLBPolicies_V2%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




