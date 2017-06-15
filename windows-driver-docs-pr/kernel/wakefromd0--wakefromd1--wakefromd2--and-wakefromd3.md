---
title: WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3
author: windows-driver-content
description: WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3
MS-HAID:
- 'PwrMgmt\_fadf36d0-c8da-4915-b08d-ceaf5534184e.xml'
- 'kernel.wakefromd0\_\_wakefromd1\_\_wakefromd2\_\_and\_wakefromd3'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f01aaceb-babf-42da-bc4b-1a846c84a313
keywords: ["WakeFromD0", "WakeFromD1", "WakeFromD2", "WakeFromD3"]
---

# WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3


## <a href="" id="ddk-wakefromd0-wakefromd1-wakefromd2-and-wakefromd3-kg"></a>


Each of these [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure members indicates whether the device can awaken in response to an external signal that arrives when the device is in the specified state.

For a device that supports all four device power states (D0, D1, D2, D3) but can awaken only from states D0 and D1, the **WakeFromD0** and **WakeFromD1** bits are set, and the **WakeFromD2** and **WakeFromD3** bits are clear.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WakeFromD0,%20WakeFromD1,%20WakeFromD2,%20and%20WakeFromD3%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


