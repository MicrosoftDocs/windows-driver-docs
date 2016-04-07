---
title: NFP power management
author: windows-driver-content
description: NFP power management
ms.assetid: A47F4B01-A912-410A-8CF8-656D2C125148
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# NFP power management


NFP devices operate in one of three power modes. These modes are *active*, *idle*, *standby*, and *power-removed*. The NFP device can enter a low-power mode when publications or subscriptions to the device are disabled. The NFP driver will transition the device to one of the power modes in response to an enable or disable notification from Windows.

The NFP driver will receive an [**IOCTL\_NFP\_ENABLE**](https://msdn.microsoft.com/library/windows/hardware/jj853316) or an [**IOCTL\_NFP\_DISABLE**](https://msdn.microsoft.com/library/windows/hardware/jj853315) control code to enable or disable subscriptions, publications, and presence events. These control codes will also trigger a power mode change for the device. The [Near-field proximity (NFP) power management for connected standby platforms](https://msdn.microsoft.com/library/windows/hardware/mt614845) topic provides detailed description of power mode changes for NFP devices.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFP%20power%20management%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




