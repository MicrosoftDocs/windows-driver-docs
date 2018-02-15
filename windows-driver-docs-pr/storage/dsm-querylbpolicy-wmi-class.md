---
title: DSM\_QueryLBPolicy WMI Class
description: DSM\_QueryLBPolicy WMI Class
ms.assetid: b7fc0d38-feaa-46c5-bcde-fcd6c71b329b
---

# DSM\_QueryLBPolicy WMI Class


MPIO publishes the DSM\_QUERYLBPolicy\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. A WMI client uses the DSM\_QUERYLBPolicy\_V2 WMI class to query the load balance policy set for an MPIO disk.

```
class DSM_QueryLBPolicy
{

    [key, read]
    string InstanceName;

    [read]
    boolean Active;

    [WmiDataId(1),
     DisplayName("Load Balance Policy") : amended,
     Description("Load Balance Policy that is currently being used by DSM") : amended
    ]
    DSM_Load_Balance_Policy LoadBalancePolicy;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**DSM\_QueryLBPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff552719) data structure. There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20DSM_QueryLBPolicy%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




