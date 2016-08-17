---
title: Creating a User-Mode Still Image Minidriver
description: Creating a User-Mode Still Image Minidriver
MS-HAID:
- 'stillimg\_136a5b33-a779-4041-80f0-ed6741e78a6e.xml'
- 'image.creating\_a\_user\_mode\_still\_image\_minidriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 94fdbeba-5b4a-4b66-b381-ec362b6d38c9
---

# Creating a User-Mode Still Image Minidriver


## <a href="" id="ddk-creating-a-user-mode-still-image-minidriver-si"></a>


All user-mode still image minidrivers must implement the interface methods defined by [IStiUSD COM Interface](istiusd-com-interface.md). This implementation is relatively easy, using the following procedure.

**To implement the methods defined by the IStiUSD COM interface:**

1.  Obtain a GUID for the interface, and include it in a header file and a setup information (INF) file.

2.  Create a implementation file such as ( .cpp).

3.  Create a customized class definition, using **IStiUSD** as an inherited class.

4.  Implement all of the methods that have been defined for the [IStiUSD COM Interface](istiusd-com-interface.md). If a method is not needed, it must return STIERR\_UNSUPPORTED.

This section provides information about the following topics:

[Still Image Device Events](still-image-device-events.md)

[Transfer Modes](transfer-modes.md)

[Security Issues for Still Image Drivers](security-issues-for-still-image-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20a%20User-Mode%20Still%20Image%20Minidriver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




