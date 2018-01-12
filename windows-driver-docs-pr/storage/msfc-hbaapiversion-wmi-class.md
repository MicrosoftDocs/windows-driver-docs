---
title: MSFC\_HbaApiVersion WMI Class
description: MSFC\_HbaApiVersion WMI Class
ms.assetid: 642b8313-d1ca-4c07-9c39-b49ef65b4438
---

# MSFC\_HbaApiVersion WMI Class


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_HbaApiVersion class to report the HBA API version that is currently supported.

The MSFC\_HbaApiVersion class is defined as follows in *Hbaapi.mof*:

```
class MSFC_HbaApiVersion
{
    uint32 WmiHbaApiVersion;
    uint32 HbaApiVersion;
    string Description;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MSFC\_HbaApiVersion**](https://msdn.microsoft.com/library/windows/hardware/ff562507)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_HbaApiVersion%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




