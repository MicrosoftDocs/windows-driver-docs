---
title: WIA\_IPS\_DESKEW\_X and WIA\_IPS\_DESKEW\_Y Properties
description: WIA\_IPS\_DESKEW\_X and WIA\_IPS\_DESKEW\_Y Properties
MS-HAID:
- 'WIA\_tree\_4bd778e1-a74d-4c64-8885-dea276d5dab1.xml'
- 'image.wia\_ips\_deskew\_x\_and\_wia\_ips\_deskew\_y\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 748b08f7-e838-4df8-abcb-4ff1cdd20f7e
---

# WIA\_IPS\_DESKEW\_X and WIA\_IPS\_DESKEW\_Y Properties


## <a href="" id="ddk-wia-ips-deskew-x-and-wia-ips-deskew-y-properties-si"></a>


The [**WIA\_IPS\_DESKEW\_X**](https://msdn.microsoft.com/library/windows/hardware/ff552581) and [**WIA\_IPS\_DESKEW\_Y**](https://msdn.microsoft.com/library/windows/hardware/ff552587) properties are implemented by the scanner driver if the driver supports deskewing. These two properties describe where the two upper corners of the skewed image are located within the bounding rectangle defined by [**WIA\_IPS\_XPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552663), [**WIA\_IPS\_YPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552671), [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661), and [**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669) properties.

The valid values for WIA\_IPS\_DESKEW\_X must be between 0 and (WIA\_IPS\_XEXTENT − 1). The valid values for WIA\_IPS\_DESKEW\_Y must be between 0 and (WIA\_IPS\_YEXTENT − 1). A value of 0 for both properties means that no skew correction should be performed.

Only rectangular scanning areas are supported, so these two values uniquely define the position of the image to be deskewed. A deskew angle can be calculated from these two values.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_DESKEW_X%20and%20WIA_IPS_DESKEW_Y%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




