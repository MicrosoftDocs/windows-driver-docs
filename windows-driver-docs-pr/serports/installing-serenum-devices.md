---
title: Installing Serenum Devices
author: windows-driver-content
description: Installing Serenum Devices
ms.assetid: abb58ce0-7afb-43eb-81e0-1942d451355a
keywords: ["Serenum driver WDK , device installations"]
---

# Installing Serenum Devices


## <a href="" id="ddk-installing-serenum-devices-kg"></a>


To install a device that is enumerated by Serenum, use the following [*hardware ID*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) format for the device:

Serenum\\*XxxxYyyy*

Where: *Xxxx* is a field of four ASCII characters that specify the EISA Manufacturing ID; *Yyyy* is a field of four ASCII characters that specify the Product ID. Serenum IDs are documented in the [Plug and Play External COM Device Specification](http://msdn.microsoft.com/windows/hardware/gg463189.aspx).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Installing%20Serenum%20Devices%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


