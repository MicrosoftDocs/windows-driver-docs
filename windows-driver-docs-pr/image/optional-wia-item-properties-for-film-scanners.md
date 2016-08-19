---
title: Optional WIA Item Properties for Film Scanners
author: windows-driver-content
description: Optional WIA Item Properties for Film Scanners
MS-HAID:
- 'WIA\_scanner\_tree\_fba6e9c8-f336-4149-a32b-e70149066c24.xml'
- 'image.optional\_wia\_item\_properties\_for\_film\_scanners'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6c17deed-7840-4ec0-bc19-d695b3e80c38
---

# Optional WIA Item Properties for Film Scanners


## <a href="" id="ddk-optional-wia-item-properties-for-film-scanners-si"></a>


The WIA film scanner item can optionally support the following WIA properties:

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff551549)

[**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641)

[**WIA\_IPS\_AUTO\_DESKEW**](https://msdn.microsoft.com/library/windows/hardware/ff552564)

[**WIA\_IPS\_DESKEW\_X**](https://msdn.microsoft.com/library/windows/hardware/ff552581)

[**WIA\_IPS\_DESKEW\_Y**](https://msdn.microsoft.com/library/windows/hardware/ff552587)

[**WIA\_IPS\_LAMP**](https://msdn.microsoft.com/library/windows/hardware/ff552603)

[**WIA\_IPS\_LAMP\_AUTO\_OFF**](https://msdn.microsoft.com/library/windows/hardware/ff552605)

[**WIA\_IPS\_PREVIEW\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff552646)

[**WIA\_IPS\_ROTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552648)

[**WIA\_IPS\_SEGMENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552649)

[**WIA\_IPS\_SHOW\_PREVIEW\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff552652)

[**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](https://msdn.microsoft.com/library/windows/hardware/ff552653)

[**WIA\_IPS\_THRESHOLD**](https://msdn.microsoft.com/library/windows/hardware/ff552655)

[**WIA\_IPS\_WARM\_UP\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff552660)

[**WIA\_IPS\_XSCALING**](https://msdn.microsoft.com/library/windows/hardware/ff552667)

[**WIA\_IPS\_YSCALING**](https://msdn.microsoft.com/library/windows/hardware/ff552676)

**Note**   The [**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641) property is required if the WiaImgFmt\_RAW format is supported. The [**WIA\_IPA\_Format**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property must support the WiaImgFmt\_BMP format. The [**WIA\_IPS\_THRESHOLD**](https://msdn.microsoft.com/library/windows/hardware/ff552655) property is required when the [**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546) property is set to 1 BPP or when the [**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543) property is set to WIA\_DATA\_THRESHOLD.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Optional%20WIA%20Item%20Properties%20for%20Film%20Scanners%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


