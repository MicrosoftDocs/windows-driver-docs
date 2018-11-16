---
title: Installing Changer Miniclass Drivers
description: Installing Changer Miniclass Drivers
ms.assetid: 923e1128-bacc-450b-b250-bc666951965d
keywords:
- changer drivers WDK storage , miniclass drivers
- storage changer drivers WDK , miniclass drivers
- miniclass drivers WDK changer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Changer Miniclass Drivers


## <span id="ddk_installing_changer_miniclass_drivers_kg"></span><span id="DDK_INSTALLING_CHANGER_MINICLASS_DRIVERS_KG"></span>


This section provides installation information, specific to changer miniclass drivers in Windows 2000 and later operating systems.

Vendors supplying their own controller minidriver should make that minidriver a member of the MediumChanger setup class in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the driver's INF file. For example:

```cpp
[version]
Signature="$WINDOWS NT$"
Class=MediumChanger
ClassGuid={CE5939AE-EBDE-11d0-B181-0000F8753EC4}
```

There are no other special requirements associated with installing changer miniclass drivers.

For more installation information, see the INF files that are supplied with the media changer samples that are included in the Windows Driver Kit (WDK).

For general information about device installation in Windows 2000 and later operating systems, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 




