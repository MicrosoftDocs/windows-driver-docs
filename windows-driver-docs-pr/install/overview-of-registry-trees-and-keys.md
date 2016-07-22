---
title: Registry Trees for Devices and Drivers
description: Registry Trees for Devices and Drivers
ms.assetid: 74dc1889-26a9-47ba-8c8d-3cd6ed95cb68
keywords: ["hardware keys WDK device installations", "registry WDK device installations", "software keys WDK device installations", "device installations WDK , registry", "installing devices WDK , registry", "Device setup WDK device installations , registry", "debugging device"]
---

# Registry Trees for Devices and Drivers


## <a href="" id="ddk-driver-information-in-the-registry-dg"></a>


The following trees in the registry are of particular interest to driver writers (where **HKLM** represents **HKEY\_LOCAL\_MACHINE**):

-   [HKLM\\SYSTEM\\CurrentControlSet\\Services Registry Tree](hklm-system-currentcontrolset-services-registry-tree.md)

-   [HKLM\\SYSTEM\\CurrentControlSet\\Control Registry Tree](hklm-system-currentcontrolset-control-registry-tree.md)

-   [HKLM\\SYSTEM\\CurrentControlSet\\Enum Registry Tree](hklm-system-currentcontrolset-enum-registry-tree.md)

-   [HKLM\\SYSTEM\\CurrentControlSet\\HardwareProfiles Registry Tree](hklm-system-currentcontrolset-hardwareprofiles-registry-tree.md)

**Note**  The keys under **HKLM\\SYSTEM\\CurrentControlSet** are a safe place to preserve data that is important to your driver because the data is stored in the system hive. The system takes additional precautions to protect the system hive (for example, keeping multiple copies).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Registry%20Trees%20for%20Devices%20and%20Drivers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




