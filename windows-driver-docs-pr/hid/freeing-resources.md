---
title: Freeing Resources
author: windows-driver-content
description: User-mode applications and kernel-mode drivers that are HID clients should always free any resources that are no longer required.
ms.assetid: 19cbc443-cc25-448f-92dc-d9586c1fd5a7
keywords: ["collections WDK HID , free resources", "HID collections WDK , free resources", "freeing HID resources"]
---

# Freeing Resources


User-mode applications and kernel-mode drivers that are HID clients should always free any resources that are no longer required.

## <a href="" id="ddk-freeing-resources-kg"></a>


For example, a user-mode application must call [**SetupDiDestroyDeviceInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550996) with the handle to the device list that it obtained from [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) after completing its initialization and connection operations for a HIDClass device. Failure to call **SetupDiDestroyDeviceInfoList** causes a memory leak.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Freeing%20Resources%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


