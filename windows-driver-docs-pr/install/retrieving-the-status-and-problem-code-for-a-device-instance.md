---
title: Retrieving the Status and Problem Code for a Device Instance
description: Retrieving the Status and Problem Code for a Device Instance
ms.assetid: 22ca9ac2-fe67-427d-a6e4-f1d9cbbede52
---

# Retrieving the Status and Problem Code for a Device Instance


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes a [device status property and a problem code property](https://msdn.microsoft.com/library/windows/hardware/ff542254). The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 do not support the property keys of the unified property model, nor do they support corresponding registry entry values that represent these properties. However, the corresponding information can be retrieved by calling the [**CM\_Get\_DevNode\_Status**](https://msdn.microsoft.com/library/windows/hardware/ff538514) function. To maintain compatibility with earlier versions of Windows, Windows Vista and later versions also support **CM\_Get\_DevNode\_Status**. However, you should use the property keys of the unified device property model to access the device driver properties.

The device driver properties are listed by the property key identifiers that you use to access the property in Windows Vista and later versions.

For information about how to use property keys to access device driver properties in Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

To access the status and problem code for a device instance on Windows Server 2003, Windows XP, and Windows 2000, call **CM\_Get\_DevNode\_Status** and supply the following parameters:

-   Set *pulStatus* to a pointer to a ULONG-typed value that receives the status bit flags that are set for a device instance. The status value can be any combination of the bit flags with prefix "DN\_" that are defined in *Cfg.h*.

-   Set *pulProblemNumber* to a pointer to a ULONG-typed value that receives the problem number that is set for a device instance. The problem number is one of the constants with the prefix "CM\_PROB\_" that are defined in *Cfg.h*. **CM\_Get\_DevNode\_Status** sets the problem number only if DN\_HAS\_PROBLEM is set in *pulStatus*.

-   Set *dnDevInst* to a device instance handle to the device for which to retrieve the status and problem code.

-   Set *ulFlags* to zero.

If the call to **CM\_Get\_DevNode\_Status** succeeds, **CM\_Get\_DevNode\_Status** retrieves the requested status and problem code for the device instance and returns CR\_SUCCESS. If the function call fails, **CM\_Get\_DevNode\_Status** returns one of the error codes with prefix "CR\_" that are defined in *Cfgmgr32.h*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Retrieving%20the%20Status%20and%20Problem%20Code%20for%20a%20Device%20Instance%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




