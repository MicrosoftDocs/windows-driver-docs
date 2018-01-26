---
title: MS\_SM\_HbaApiVersion WMI Class
description: MS\_SM\_HbaApiVersion WMI Class
ms.assetid: 3d0591e5-ed95-4509-bd27-e122ac9186d2
---

# MS\_SM\_HbaApiVersion WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SM\_HbaApiVersion class to report the current HBA API version.

The MS\_SM\_HbaApiVersion class is defined as follows in *Hbaapi.mof*:

```
class MS_SM_HbaApiVersion
{
    uint32 WmiHbaApiVersion;  
    uint32 HbaApiVersion;  
    string Description;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SM\_HbaApiVersion**](https://msdn.microsoft.com/library/windows/hardware/ff563211)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MS_SM_HbaApiVersion%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




