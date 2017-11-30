---
title: Button implementation
author: windows-driver-content
description: We recommend that you use a physical GPIO resource for both the buttons and state indicators.
ms.assetid: ECF0723A-1AF0-4608-88CC-6ACBD98DA03C
---

# Button implementation


We recommend that you use a physical GPIO resource for both the buttons and state indicators.

On systems that do not have a physical GPIO resource for a required/optional hardware button or for a GPIO indicator (laptop/slate mode indication or docked indication), a user mode or kernel mode driver can inject state changes directly to the inbox driver instead of a physical hardware resource that is attributed to the button array device (\_CID PNP0C40), laptop/slate mode state indicator (\_CID PNP0C60) or docking state indicator (\_CID PNP0C70).

To use an interface, an entry must exist in the ACPI table that defines each of the respective device(s) for which the interface is to be utilized. However, the existence of any GPIO resources for a device is optional. See [ACPI descriptor samples](acpi-descriptor-samples.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Button%20implementation%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


