---
title: Required Flatbed Item Properties
description: Required Flatbed Item Properties
MS-HAID:
- 'WIA\_scanner\_tree\_8d13912b-5bca-48fd-ba60-83bb6a6bd03c.xml'
- 'image.required\_flatbed\_item\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5af295de-b5ad-47c7-b1db-9d5685ed8d19
---

# Required Flatbed Item Properties


## <a href="" id="ddk-required-wia-item-properties-for-flatbed-scanners-si"></a>


The WIA flatbed scanner item is required to support the following WIA properties:

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff551518)

[**WIA\_IPA\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551526)

[**WIA\_IPA\_BUFFER\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551527)

[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](https://msdn.microsoft.com/library/windows/hardware/ff551535)

[**WIA\_IPA\_COLOR\_PROFILE**](https://msdn.microsoft.com/library/windows/hardware/ff551536)

[**WIA\_IPA\_COMPRESSION**](https://msdn.microsoft.com/library/windows/hardware/ff551540)

[**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543)

[**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546)

[**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553)

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551561)

[**WIA\_IPA\_ICM\_PROFILE\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551571)

[**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581)

[**WIA\_IPA\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551590)

[**WIA\_IPA\_ITEM\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551594)

[**WIA\_IPS\_MAX\_HORIZONTAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552607)

[**WIA\_IPS\_MAX\_VERTICAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552611)

[**WIA\_IPS\_MIN\_HORIZONTAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552612)

[**WIA\_IPS\_MIN\_VERTICAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552614)

[**WIA\_IPA\_NUMBER\_OF\_LINES**](https://msdn.microsoft.com/library/windows/hardware/ff551611)

[**WIA\_IPA\_PIXELS\_PER\_LINE**](https://msdn.microsoft.com/library/windows/hardware/ff551615)

[**WIA\_IPA\_PLANAR**](https://msdn.microsoft.com/library/windows/hardware/ff551617)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551623)

[**WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551628)

[**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656)

[**WIA\_IPS\_BRIGHTNESS**](https://msdn.microsoft.com/library/windows/hardware/ff552567)

[**WIA\_IPS\_CONTRAST**](https://msdn.microsoft.com/library/windows/hardware/ff552573)

[**WIA\_IPS\_CUR\_INTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552579)

[**WIA\_IPS\_OPTICAL\_XRES**](https://msdn.microsoft.com/library/windows/hardware/ff552620)

[**WIA\_IPS\_OPTICAL\_YRES**](https://msdn.microsoft.com/library/windows/hardware/ff552622)

[**WIA\_IPS\_PREVIEW**](https://msdn.microsoft.com/library/windows/hardware/ff552643)

[**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661)

[**WIA\_IPS\_XPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552663)

[**WIA\_IPS\_XRES**](https://msdn.microsoft.com/library/windows/hardware/ff552665)

[**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669)

[**WIA\_IPS\_YPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552671)

[**WIA\_IPS\_YRES**](https://msdn.microsoft.com/library/windows/hardware/ff552673)

**Note**   The [**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641) property is required if the WiaImgFmt\_RAW format is supported. The [**WIA\_IPA\_Format**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property must support the WiaImgFmt\_BMP format. The [**WIA\_IPS\_THRESHOLD**](https://msdn.microsoft.com/library/windows/hardware/ff552655) property is required when the [**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546) property is set to 1 bits per pixel (BPP) or when the [**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543) property is set to WIA\_DATA\_THRESHOLD.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Required%20Flatbed%20Item%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




