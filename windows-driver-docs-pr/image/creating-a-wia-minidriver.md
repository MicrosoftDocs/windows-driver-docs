---
title: Creating a WIA Minidriver
description: Creating a WIA Minidriver
MS-HAID:
- 'WIA\_drv\_basic\_b8b5df0d-6dd1-40d5-bd73-ddf5591b4c44.xml'
- 'image.creating\_a\_wia\_minidriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7ed02bcd-cacf-4a29-9f3f-1972c39ff0ae
---

# Creating a WIA Minidriver


## <a href="" id="ddk-creating-a-wia-minidriver-si"></a>


A WIA minidriver should be able to do the following:

[Provide a COM interface](providing-a-com-interface.md)

[Provide an IStiUSD interface](providing-an-istiusd-interface.md)

[Initialize itself](initializing-the-wia-minidriver.md)

[Build a driver item tree](creating-the-wia-driver-item-tree.md)

[Inform an application of item tree changes](informing-an-application-of-item-tree-changes.md)

[Use WIA properties](using-wia-properties.md)

[Access kernel-mode drivers](accessing-kernel-mode-drivers-for-still-image-devices.md)

[Implement image color management](implementing-image-color-management.md)

The following sections describe how a WIA minidriver performs these tasks.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20a%20WIA%20Minidriver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




