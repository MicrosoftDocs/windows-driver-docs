---
title: Driver type is " xyz ". This driver is not supported by SDV
description: Static Driver Verifier must be able to interpret the driver code, specifically, the driver's entry points and the code in functions and routines that support required driver functionality.
ms.assetid: A8126F46-3CC8-45A8-A16B-884B07C59688
---

# Driver type is "&lt;xyz&gt;". This driver is not supported by SDV


Static Driver Verifier must be able to interpret the driver code, specifically, the driver's entry points and the code in functions and routines that support required driver functionality. Static Driver Verifier supports driver that comply with the Windows Driver Model (WDM), the Kernel Mode Driver Framework (KMDF), NDIS, and Storport.

For more information, see [Supported Drivers](supported-drivers.md).

**Note**  If you see this error message and you are running SDV as part of the requirement for [Static Tools Logo Test](https://msdn.microsoft.com/library/windows/hardware/mt219212), it does not mean that the driver will fail the Static Tools Logo Test. You can still create a Driver Verification Log and run the Static Tools Logo Test. See [Creating a Driver Verification Log](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_verification_log). Having a driver model that SDV does not supported does not preclude certification of the driver.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Driver%20type%20is%20"<xyz>".%20This%20driver%20is%20not%20supported%20by%20SDV%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




