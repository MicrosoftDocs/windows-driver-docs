---
title: MS\_SMHBA\_PORTLUN WMI Class
description: MS\_SMHBA\_PORTLUN WMI Class
ms.assetid: 28473b3b-2b88-4abc-81b5-9a6a7f8166e3
---

# MS\_SMHBA\_PORTLUN WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_PORTLUN class to expose the mapping between the target LUN and SAS adapter.

The MS\_SMHBA\_PORTLUN class is defined as follows in *Hbaapi.mof*:

```
class MS_SMHBA_PORTLUN 
{
    [HBAType("HBA_WWN"), WmiDataId(1)]
    uint8   PortWWN[8];

    [HBAType("HBA_WWN"), WmiDataId(2)]
    uint8   domainPortWWN[8];

    [HBAType("HBA_SCSILUN"), WmiDataId(3)]
    uint64  TargetLun;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_PORTLUN**](https://msdn.microsoft.com/library/windows/hardware/ff563169)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MS_SMHBA_PORTLUN%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




