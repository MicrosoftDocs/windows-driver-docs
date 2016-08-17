---
title: Implementing Image Color Management
description: Implementing Image Color Management
MS-HAID:
- 'WIA\_drv\_basic\_6fc82f0f-f049-4ca7-a139-836104d63bc9.xml'
- 'image.implementing\_image\_color\_management'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b3184a8b-4f32-4cb0-8f68-777d85110142
---

# Implementing Image Color Management


## <a href="" id="ddk-implementing-image-color-management-si"></a>


WIA relies on the Image Color Management (ICM) system provided in Microsoft Windows. ICM is described in the Microsoft Windows SDK documentation.

For best application compatibility, all minidrivers are expected to return data in the sRGB color space. If a device natively produces data in a different color space, the minidriver should use the ICM functions to map its output to sRGB. Some applications implement ICM and may want to retrieve data in the native color space. Minidrivers can allow this functionality by specifying the native color space in the setup information (INF) file and specifying a valid value of 1 for the [**WIA\_IPA\_APP\_COLOR\_MAPPING**](https://msdn.microsoft.com/library/windows/hardware/ff551521) property.

When the application sets the property to 1, the minidriver should stop mapping to sRGB and allow the application to handle the mapping. The application uses the current value of the [**WIA\_IPA\_ICM\_PROFILE\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551571) property as the profile for the data from the device. The user sets the property using system dialogs and it should not be changed by the minidriver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Implementing%20Image%20Color%20Management%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




