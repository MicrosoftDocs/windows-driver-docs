---
title: MPIO\_ADAPTER\_INFORMATION WMI Class
description: MPIO\_ADAPTER\_INFORMATION WMI Class
ms.assetid: 748205a5-d37b-4080-b6ce-9176139cef4a
---

# MPIO\_ADAPTER\_INFORMATION WMI Class


An MPIO driver uses the MPIO\_ADAPTER\_INFORMATION WMI class to identify a path that is associated with an MPIO disk.

```
class MPIO_ADAPTER_INFORMATION
{
    //
    // Path ID. The PDO_INFORMATION class includes
    // it&#39;s pathId. These values can be used to find
    // which devices are on which path.
    //
    [WmiDataId(1)] uint64 PathId;

    //
    // Adapter Location.
    //
    [WmiDataId(2)] uint8 BusNumber;
    [WmiDataId(3)] uint8 DeviceNumber;
    [WmiDataId(4)] uint8 FunctionNumber;
    [WmiDataId(5)] uint8 Pad;

    //
    // Adapter Name.
    //
    [WmiDataId(6), MaxLen(63)] string AdapterName;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_ADAPTER\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff562313) data structure. There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MPIO_ADAPTER_INFORMATION%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




