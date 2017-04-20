---
title: Using IWiaItem CreateChildItem to Create Selection Areas
author: windows-driver-content
description: Using IWiaItem CreateChildItem to Create Selection Areas
ms.assetid: c430d15b-51e9-4419-9cdb-904a0f5ef09b
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using IWiaItem::CreateChildItem to Create Selection Areas


## <a href="" id="ddk-using-iwiaitem-createchilditem-to-create-selection-areas-si"></a>


WIA applications should read the [**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](https://msdn.microsoft.com/library/windows/hardware/ff552653) property to determine whether the film scanning item supports creating of child items. The film scanner items can contain child items (that is, frames) in the item tree that *cannot* be deleted. The application can delete WIA items that are marked with the [**WIA\_IPA\_ACCESS\_RIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff551518) settings of (WIA\_PROP\_READ | WIA\_ITEM\_WRITE | WIA\_ITEM\_CAN\_BE\_DELETED).

### Creating Dynamic Film Items

A WIA application calls **IWiaItem::CreateChildItem** (described in the Microsoft Windows SDK documentation) to create a new WIA application item (or frame) that is located under the film scanner item. The WIA driver should initialize the required WIA properties and the WIA application should set the extent settings and any other properties to configure the new frame. For more information about required WIA properties, see [Required WIA Item Properties for Film Scanners](required-wia-item-properties-for-film-scanners.md).

**Note**   WIA film items must have only one level of WIA child items. The film item can be set to be a folder, but folder items *cannot* be created under the film scanner item.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Using%20IWiaItem::CreateChildItem%20to%20Create%20Selection%20Areas%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


