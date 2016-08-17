---
title: Flatbed Child Item Properties
description: Flatbed Child Item Properties
MS-HAID:
- 'WIA\_scanner\_tree\_b8d8eb93-591d-474a-888c-ad386ea79688.xml'
- 'image.flatbed\_child\_item\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ad13e4a2-0c5c-43a5-ab83-fc2ef65b4467
---

# Flatbed Child Item Properties


The child items of a WIA flatbed scanner item are required to support the following WIA properties:

[**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581)

[**WIA\_IPA\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551590)

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551561)

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff551518)

[**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661)

[**WIA\_IPS\_XPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552663)

[**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669)

[**WIA\_IPS\_YPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552671)

**Note**   The [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property must be set to WIA\_CATEGORY\_FLATBED for both flatbed items and flatbed child items.

 

Child items can optionally support any other property that is supported by the parent item, except for the [**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](https://msdn.microsoft.com/library/windows/hardware/ff552653) and [**WIA\_IPS\_SEGMENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552649) properties.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Flatbed%20Child%20Item%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




