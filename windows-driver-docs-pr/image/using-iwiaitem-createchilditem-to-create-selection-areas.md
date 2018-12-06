---
title: Using IWiaItem CreateChildItem to Create Selection Areas
description: Using IWiaItem CreateChildItem to Create Selection Areas
ms.assetid: c430d15b-51e9-4419-9cdb-904a0f5ef09b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using IWiaItem::CreateChildItem to Create Selection Areas





WIA applications should read the [**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](https://msdn.microsoft.com/library/windows/hardware/ff552653) property to determine whether the film scanning item supports creating of child items. The film scanner items can contain child items (that is, frames) in the item tree that *cannot* be deleted. The application can delete WIA items that are marked with the [**WIA\_IPA\_ACCESS\_RIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff551518) settings of (WIA\_PROP\_READ | WIA\_ITEM\_WRITE | WIA\_ITEM\_CAN\_BE\_DELETED).

### Creating Dynamic Film Items

A WIA application calls **IWiaItem::CreateChildItem** (described in the Microsoft Windows SDK documentation) to create a new WIA application item (or frame) that is located under the film scanner item. The WIA driver should initialize the required WIA properties and the WIA application should set the extent settings and any other properties to configure the new frame. For more information about required WIA properties, see [Required WIA Item Properties for Film Scanners](required-wia-item-properties-for-film-scanners.md).

**Note**   WIA film items must have only one level of WIA child items. The film item can be set to be a folder, but folder items *cannot* be created under the film scanner item.

 

 

 




