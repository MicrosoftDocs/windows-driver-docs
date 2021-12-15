---
title: Using Custom Properties
description: Using Custom Properties
ms.date: 04/20/2017
---

# Using Custom Properties





A WIA driver can define its own custom properties. Callers can manipulate custom properties just as they would normal WIA properties. However, only your application or custom UI module can access these custom properties.

WIA drivers should define the custom properties to have property identifiers that are offset by WIA\_PRIVATE\_DEVPROP for device properties, and use WIA\_PRIVATE\_ITEMPROP for normal item properties, such as inside [**IWiaMiniDrv::drvInitItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinititemproperties). For more information, see [Defining Custom Properties](defining-custom-properties.md).

There are two ways to pass custom parameters to WIA drivers.

The first option is to use the **IWiaItemExtras::Escape** method (described in the Microsoft Windows SDK documentation). This is similar to the [**IStiUSD::Escape**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-escape) method, but it allows callers to use WIA directly, instead of using STI methods. Using **IWiaItemExtras::Escape**, you can pass any information to the driver, and the driver can pass any information back. The WIA service manages only those buffers passed between the caller and the driver.

The second option is to use custom properties. Using the **IWiaItemExtras::Escape** method is more flexible than using custom WIA properties, but custom WIA properties allow you to store information in the item's property stream so that the driver can read the information at another time.

The following two sample code snippets show how to use custom properties to pass custom parameters to and from your driver.

[Sample Code to Create Custom Properties](sample-code-to-create-custom-properties.md)

[Sample Code to Set Custom Properties](sample-code-to-set-custom-properties.md)

 

