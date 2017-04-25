---
title: Custom and Auto Page Sizes
author: windows-driver-content
description: Custom and Auto Page Sizes
ms.assetid: a1f5f78d-fc05-4a7e-9d19-c7f40302b85f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Custom and Auto Page Sizes


An application can set page size either through automatic detection by the scanner or through custom values. The approach used by the application is determined by the [**WIA\_IPS\_PAGE\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552634) property, which can take the values WIA\_PAGE\_AUTO or WIA\_PAGE\_CUSTOM.

If an application sets WIA\_IPS\_PAGE\_SIZE to any value other than WIA\_PAGE\_CUSTOM, the WIA minidriver should adjust the values of WIA\_IPS\_PAGE\_WIDTH and WIA\_IPS\_PAGE\_HEIGHT to the page's dimensions in thousandths of an inch (.001). The minidriver should also adjust the values of WIA\_IPS\_XEXTENT and WIA\_IPS\_YEXTENT to the page's dimensions, in pixels.

If an extent setting (WIA\_IPS\_XEXTENT or WIA\_IPS\_YEXTENT) is changed to a value that does *not* match the current page-size setting, the minidriver should change the value of the WIA\_IPS\_PAGE\_SIZE property to WIA\_PAGE\_CUSTOM. The minidriver should also modify WIA\_IPS\_PAGE\_WIDTH or WIA\_IPS\_PAGE\_HEIGHT to agree with the new extent setting.

If an application sets the WIA\_IPS\_PAGE\_SIZE property to WIA\_PAGE\_CUSTOM, the current selection area is not affected. The WIA minidriver should obtain the current image layout, starting from the current settings of the [**WIA\_IPS\_XPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552663) and [**WIA\_IPS\_YPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552671) properties. If the page-size setting cause the selection area to be outside the scanner's bed, the minidriver must automatically adjust the values of the WIA\_IPS\_XPOS and WIA\_IPS\_YPOS properties to valid settings. If the WIA\_IPS\_PAGE\_SIZE and WIA\_IPS\_ORIENTATION properties are set at the same time and they are invalid when they are applied in combination, the minidriver should fail the application's settings by returning an error in the [**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017) method.

When automatic page size detection is enabled, the driver should provide accurate image dimension information only after completing the transfer of the image data. For stream-based transfers, the driver is expected to update the image dimensions in the image header at the end of the transfer. At the beginning of a new session, the value for the WIA\_IPS\_PAGE\_SIZE property should be always set to a value other than WIA\_PAGE\_AUTO.

When WIA\_PAGE\_AUTO is set as the current WIA\_IPS\_PAGE\_SIZE value, the driver might need to first transfer an image header that contains generic image dimensions, then transfer the image data, and then go back to the beginning of the transfer stream, update the image header with the actual image dimensions (found after the scan completed), and move the stream index back to the end of the stream.

When WIA\_PAGE\_AUTO is set (chosen as the default value by the driver or set by the application), the application should not attempt to process the image dimensions that the image header describes until the entire image transfer is completed.

**Note**  The compatibility layer within the WIA service does not add support for WIA\_IPS\_PAGE\_SIZE to the ADF item that is translated from a Windows XP WIA device if the property is not supported on the child item of the device. Applications should not expect an ADF item to always support this property and should always check if WIA\_IPS\_PAGE\_SIZE is supported at run time. (Typically, applications should check the support for any property that is to be negotiated.)

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Custom%20and%20Auto%20Page%20Sizes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


