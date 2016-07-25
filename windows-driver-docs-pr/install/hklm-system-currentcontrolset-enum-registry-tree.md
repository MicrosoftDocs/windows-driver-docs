---
title: HKLM\\SYSTEM\\CurrentControlSet\\Enum Registry Tree
description: HKLM\\SYSTEM\\CurrentControlSet\\Enum Registry Tree
ms.assetid: 9de3ca54-d23f-4ee6-a638-27e52a60dfdd
---

# HKLM\\SYSTEM\\CurrentControlSet\\Enum Registry Tree


## <a href="" id="ddk-the-hklm-system-currentcontrolset-enum-tree-dg"></a>


The **HKLM\\SYSTEM\\CurrentControlSet\\Enum** registry tree contains information about the devices on the system. The PnP manager creates a subkey for each device, with a name in the form of **HKLM\\SYSTEM\\CurrentControlSet\\Enum\\***Enumerator***\\***deviceID*. Under each of these keys is a subkey for each device instance present on the system. This subkey has information such as the device description, hardware IDs, compatible IDs, and resource requirements.

The **Enum** tree is reserved for use by operating system components, and its layout is subject to change. Drivers and user-mode [Device Installation Components](https://msdn.microsoft.com/library/windows/hardware/ff541277) must use system-supplied functions, such as [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) and [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967), to extract information from this tree. *Drivers and Windows applications must not access the* ***Enum*** *tree directly.* You can view the **Enum** tree directly by using Registry Editor when you debug drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20HKLM\SYSTEM\CurrentControlSet\Enum%20Registry%20Tree%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




