---
title: Advanced Duplex-Capable Document Feeder
description: Advanced Duplex-Capable Document Feeder
ms.assetid: 05b91864-7573-4d99-8a03-701d6cdd650b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Advanced Duplex-Capable Document Feeder





Advanced duplex scanning allows the application to independently configure the front and back page settings.

The following diagram illustrates the WIA item tree of a flatbed scanner that supports advanced duplex and document feeder scanning.

![diagram illustrating the item tree of a flatbed scanner that supports advanced duplex and document feeder scanning](images/wia-feeder-tree3.png)

Note that the front and back of the page that is being scanned are represented by separate child items in the item tree. This differentiation includes separate categories in the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property: WIA\_CATEGORY\_FRONT and WIA\_CATEGORY\_BACK. In a scanner that performs advanced duplex scanning, the front and back items are set separately; they may be set to different values. However, even on a scanner that is capable of advanced duplex scanning, there cannot be only a front or back item; if there is either a front or back item, the other item must also be present.

The driver indicates that there are independent settings for the front and back items (that is, an advanced duplex scan is to be performed) by setting the ADVANCED\_DUP flag in the feeder's [**WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551379) property.

### Scanning

Applications navigate to the feeder item to perform document feeder scans. The WIA properties on the feeder item should be a subset of the supported property values that are common to both the front and back pages. Applications can choose to use two types of data transfers (standard image acquisition or folder acquisition) that affect which document feeder settings are used.

### Standard Image Acquisition

In standard acquisition or non-folder acquisition, the WIA feeder item property settings are used for both front and back pages (the same as the simple duplex and non-duplex scanner models).

### Folder Image Acquisition

In folder acquisition, the WIA feeder item's image settings are ignored and settings for the front and back items are used instead. Advanced applications use the individual configurable settings for the document feeder transfer. On a feeder scanner, the image data is always acquired off the feeder item, even when there are child items (front and back items).

 

 




