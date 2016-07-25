---
title: CM\_PROB\_UNSIGNED\_DRIVER
description: CM\_PROB\_UNSIGNED\_DRIVER
ms.assetid: 91d37d25-ca0d-413f-9e6f-5a22a0406714
---

# CM\_PROB\_UNSIGNED\_DRIVER


The device did not start on a 64-bit version of Windows because it has a driver that is not digitally signed. For more information about how to sign drivers, see [Driver Signing](driver-signing.md).

### Error

52

### Display Message (Windows 7 and later versions of Windows)

"Windows cannot verify the digital signature for the drivers required for this device. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source. (Code 52)"

### Recommended Resolution (Windows 7 and later versions of Windows)

The driver does not comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).

For end-users, the only way to avoid this error is to obtain and install a digitally signed driver for the device.

For driver developers, you can use various methods to load an unsigned driver on a 64-bit version of Windows. For more information, see [Installing an Unsigned Driver during Development and Test](installing-an-unsigned-driver-during-development-and-test.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_UNSIGNED_DRIVER%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




