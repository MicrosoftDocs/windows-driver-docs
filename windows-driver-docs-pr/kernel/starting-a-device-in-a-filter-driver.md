---
title: Starting a Device in a Filter Driver
author: windows-driver-content
description: Starting a Device in a Filter Driver
MS-HAID:
- 'PlugPlay\_78f0a683-4efa-43f4-9032-bd9a981021ce.xml'
- 'kernel.starting\_a\_device\_in\_a\_filter\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d7c527b6-a5fb-4c4f-a8bc-29f961d31125
keywords: ["filter drivers WDK PnP"]
---

# Starting a Device in a Filter Driver


## <a href="" id="ddk-starting-a-device-in-a-filter-driver-kg"></a>


An upper-level filter driver might augment any of the start activities of the function driver.

A lower-level filter typically augments the features of the device and might participate in starting the device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Starting%20a%20Device%20in%20a%20Filter%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


