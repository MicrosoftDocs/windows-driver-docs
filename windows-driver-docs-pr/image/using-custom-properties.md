---
title: Using Custom Properties
description: Using Custom Properties
ms.assetid: cf4e728f-7900-4849-ab1c-135f9fec9713
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Custom Properties





A WIA driver can define its own custom properties. Callers can manipulate custom properties just as they would normal WIA properties. However, only your application or custom UI module can access these custom properties.

WIA drivers should define the custom properties to have property identifiers that are offset by WIA\_PRIVATE\_DEVPROP for device properties, and use WIA\_PRIVATE\_ITEMPROP for normal item properties, such as inside [**IWiaMiniDrv::drvInitItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff544989). For more information, see [Defining Custom Properties](defining-custom-properties.md).

There are two ways to pass custom parameters to WIA drivers.

The first option is to use the **IWiaItemExtras::Escape** method (described in the Microsoft Windows SDK documentation). This is similar to the [**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815) method, but it allows callers to use WIA directly, instead of using STI methods. Using **IWiaItemExtras::Escape**, you can pass any information to the driver, and the driver can pass any information back. The WIA service manages only those buffers passed between the caller and the driver.

The second option is to use custom properties. Using the **IWiaItemExtras::Escape** method is more flexible than using custom WIA properties, but custom WIA properties allow you to store information in the item's property stream so that the driver can read the information at another time.

The following two sample code snippets show how to use custom properties to pass custom parameters to and from your driver.

[Sample Code to Create Custom Properties](sample-code-to-create-custom-properties.md)

[Sample Code to Set Custom Properties](sample-code-to-set-custom-properties.md)

 

 




