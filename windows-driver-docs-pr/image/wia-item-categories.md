---
title: WIA Item Categories
description: WIA Item Categories
ms.assetid: b201e365-60d8-4c3b-a9cf-4bbaa318337f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Item Categories





This topic applies to Windows Vista and later.

All items in a WIA item tree must support the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property. This property identifies the functional category that an item belongs to. The category determines the set of WIA item flags and WIA properties that are associated with the item.

WIA defines the following item categories:

<a href="" id="wia-category-root"></a>WIA\_CATEGORY\_ROOT  
The *root item* in the item tree for a WIA scanner device represents the device as a whole. If the device includes a flatbed, ADF, or film scanning function, the items that represent these input sources are children of the root item. If the device contains storage, the topmost folder item in the device's storage hierarchy is a child of the root item. An application can access information about the device, including status, identification, and access rights, through the WIA properties implemented on the root item. For more information, see the discussions of root item properties in [Implementing Flatbed Scanner Item Trees](implementing-flatbed-scanner-item-trees.md), [Implementing Feeder Scanner Item Trees](implementing-feeder-scanner-item-trees.md), and [Implementing Film Scanner Item Trees](implementing-film-scanner-item-trees.md).

<a href="" id="wia-category-flatbed"></a>WIA\_CATEGORY\_FLATBED  
A *flatbed item* represents a scan flatbed (also called a scan platen) on a WIA scanner device. The WIA item tree for a device with a scan flatbed should include a flatbed item that is a child of the root item. In addition, if the WIA device supports segmentation (for example, by a [segmentation filter](wia-segmentation-filter.md)) or multiregion scanning, this flatbed item should have children, which are also flatbed items, to represent the individual scan regions on the flatbed. The child items, when present, should belong to the same WIA\_CATEGORY\_FLATBED category as their parent, and they should support the same WIA properties (and have the same initial property values) as their parent--except that the positions and extents of the child items are limited to the scan regions that they represent. An application can use the WIA driver's segmentation filter (if one is provided) to create scan regions, or the minidriver can automatically detect and create the scan regions itself. An application can access the device's flatbed scanning function through the WIA properties implemented on the flatbed item (or items). For more information, see [Implementing Flatbed Scanner Item Trees](implementing-flatbed-scanner-item-trees.md).

<a href="" id="wia-category-feeder"></a>WIA\_CATEGORY\_FEEDER  
A *feeder item* represents an automatic document feeder (ADF) on a WIA scanner device. (This item category can also represent a feeder that is not fully automatic and that requires manual assistance from the user, but, in this case, the WIA minidriver is responsible for verifying that the next document page has advanced through the feeder before it scans the page.) A device with an ADF should include a feeder item in its WIA item tree. A feeder item is a child of the root item. An application can access the device's ADF scanning function through the WIA properties implemented on the feeder item. For more information, see [Implementing Feeder Scanner Item Trees](implementing-feeder-scanner-item-trees.md).

If the ADF can perform duplex scanning (that is, scan both sides of a document page), and it supports different control settings for scanning the front and back sides of document pages, the WIA minidriver should implement a feeder front item and a feeder back item as children of the feeder item. An application can access the ADF front and back scanning functions through the WIA properties implemented on the feeder front item and on the feeder back item. For more information about these two items, see the following category descriptions.

<a href="" id="wia-category-feeder-front"></a>WIA\_CATEGORY\_FEEDER\_FRONT  
A *feeder front item* represents the ADF settings for scanning the front side of the pages in a document. This item should be implemented by the WIA minidriver for a scanner device that has an ADF that can perform duplex scanning and that supports different control settings for scanning the front and back sides of document pages. A device that has an ADF that always uses the same settings for both sides of document pages does not need this item. A feeder front item is a child of a feeder item. An application can access the ADF front scanning function through the WIA properties implemented on the feeder front item. For more information, see [Implementing Feeder Scanner Item Trees](implementing-feeder-scanner-item-trees.md).

<a href="" id="wia-category-feeder-back"></a>WIA\_CATEGORY\_FEEDER\_BACK  
A *feeder back item* represents the ADF settings for scanning the back side of the pages in a document. This item should be implemented by the WIA minidriver for a scanner device that has an ADF that can perform duplex scanning and that supports different control settings for scanning the front and back sides of document pages. A device that has an ADF that always uses the same settings for both sides of document pages does not need this item. A feeder back item is a child of a feeder item. An application can access the ADF back scanning function through the WIA properties implemented on the feeder back item. For more information, see [Implementing Feeder Scanner Item Trees](implementing-feeder-scanner-item-trees.md).

<a href="" id="wia-category-film"></a>WIA\_CATEGORY\_FILM  
A *film item* represents a film scanning function on a WIA scanner device. A device that is a dedicated film scanner, or that is a flatbed scanner equipped with a transparency adapter (TPA), should include one or more film items in its WIA item tree. A film item is a child of the root item, or of another film item. A film item that is a child of the root item represents the entire scanning surface, and this film item might have children that are film items that represent the regions of the scanning surface that correspond to individual film frames. An application can access the device's film scanning function through the WIA properties implemented on the film item (or items). For more information, see [Implementing Film Scanner Item Trees](implementing-film-scanner-item-trees.md).

<a href="" id="wia-category-folder"></a>WIA\_CATEGORY\_FOLDER  
A *folder item* represents a folder located in the internal storage of the WIA scanner device. A folder item is a child of the root item or of another folder item. If a folder item has children, the children are a combination of finished file items and folder items. The topmost folder item in an item tree is a child of the root item. An application can access the folder contents and information about the folder through the WIA properties implemented on the folder item. For more information, see [WIA Scanner Storage](wia-scanner-storage.md).

<a href="" id="wia-category-finished-file"></a>WIA\_CATEGORY\_FINISHED\_FILE  
A *finished file item* represents a finished file stored in a folder on a WIA scanner device. A finished file is a file whose contents will not change. This definition excludes files whose contents can change dynamically, for example, as the scanner acquires and processes image data. A finished file item is a child of a folder item. An application can access a finished file and information about the file through the WIA properties implemented on the finished file item. For more information, see [WIA Scanner Storage](wia-scanner-storage.md).

<a href="" id="wia-category-auto"></a>WIA\_CATEGORY\_AUTO  
In Windows 7 and later, an [auto item](auto-item.md) represents the automatic configuration settings for a WIA scanner device that supports [auto-configured scanning](auto-configured-scanning.md). This type of device can configure its own scan settings instead of requiring the settings to be configured by a WIA application running on a desktop computer. For example, if the device enables the user to initiate a scanning operation from the device (instead of from the application's user interface) and to select the input source for the operation from the device, the application can use the auto item to offload, to the device, the task of configuring the selected input source. An auto item is a child of the root item. A WIA tree that contains an auto item must also contain one or more of the following: flatbed item, feeder item, or film item. An application can access the auto-configured scanning function of a device through the WIA properties implemented on the root item and on the auto item. For more information, see [WIA Properties Supported by an Auto Item](wia-properties-supported-by-an-auto-item.md).

Each WIA item category has a set of required WIA item flags and WIA properties that an item in the category must support, and, in addition, a set of flags and properties that the item can support as options. For a summary of the flags and properties associated with the various item categories, see [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581). For a complete list of the WIA item flags, see [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585).

 

 




