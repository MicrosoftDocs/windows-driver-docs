---
title: MPIO\_DSM\_Path WMI Class
description: MPIO\_DSM\_Path WMI Class
ms.assetid: 4f8d7fb0-2b9a-44dc-bb87-f70285f1b47c
---

# MPIO\_DSM\_Path WMI Class


MPIO publishes the MPIO\_DSM\_Path\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. An MPIO driver uses the MPIO\_DSM\_Path\_V2 WMI class to identify a path ID as reported by a DSM.

```
class MPIO_DSM_Path
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
    //
    [WmiDataId(4),
     Description("Flag set to TRUE if the path is a primary path. Else FALSE.") : amended
    ]
    uint32 PrimaryPath;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_DSM\_Path**](https://msdn.microsoft.com/library/windows/hardware/ff562382) data structure. There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MPIO_DSM_Path%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




