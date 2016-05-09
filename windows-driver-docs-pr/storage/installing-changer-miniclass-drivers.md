---
title: Installing Changer Miniclass Drivers
author: windows-driver-content
description: Installing Changer Miniclass Drivers
ms.assetid: 923e1128-bacc-450b-b250-bc666951965d
keywords: ["changer drivers WDK storage , miniclass drivers", "storage changer drivers WDK , miniclass drivers", "miniclass drivers WDK changer"]
---

# Installing Changer Miniclass Drivers


## <span id="ddk_installing_changer_miniclass_drivers_kg"></span><span id="DDK_INSTALLING_CHANGER_MINICLASS_DRIVERS_KG"></span>


This section provides installation information, specific to changer miniclass drivers in Windows 2000 and later operating systems.

Vendors supplying their own controller minidriver should make that minidriver a member of the MediumChanger setup class in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the driver's INF file. For example:

```
[version]
Signature="$WINDOWS NT$"
Class=MediumChanger
ClassGuid={CE5939AE-EBDE-11d0-B181-0000F8753EC4}
```

There are no other special requirements associated with installing changer miniclass drivers.

For more installation information, see the INF files that are supplied with the media changer samples that are included in the Windows Driver Kit (WDK).

For general information about device installation in Windows 2000 and later operating systems, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Installing%20Changer%20Miniclass%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


