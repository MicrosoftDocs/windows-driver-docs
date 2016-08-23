---
title: Scanner Storage Architecture
author: windows-driver-content
description: Scanner Storage Architecture
MS-HAID:
- 'WIA\_scanner\_tree\_70d7f80e-d685-4964-bf2f-c82433b60af8.xml'
- 'image.scanner\_storage\_architecture'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 90b2367f-c611-47c6-bd60-4125bd7ca709
---

# Scanner Storage Architecture


Scanner devices that are equipped with one or more storage units should implement at least one root storage folder scanner item (WIA\_CATEGORY\_FOLDER) in their WIA item tree to represent either one individual storage unit or the logical root for all available storage units. Under a storage root item, there could be subfolder items (WIA\_CATEGORY\_FOLDER) that represent individual storage units (if all storage units are mapped under this unique storage root item) or file folders on a storage unit and individual file items (WIA\_CATEGORY\_FINISHED\_FILE).

**Note**   The root storage folder scanner items should be located directly off of the WIA root item. The root storage folder items may contain other folder items and files or it may be empty.

 

A scanner that is equipped with just an empty storage unit (for example, an internal hard disk drive that does not contain any data) should have a WIA item tree that looks like the following figure.

![diagram illustrating the item tree of a scanner with an empty storage unit](images/wia-storage-tree-simple.png)

The preceding figure is a simplified graphic without a scanner item. A scanner will have at least one scanner item (flatbed, feeder, or film) and any type of scanner may be equipped with storage, as the following figure shows.

![diagram illustrating the item tree of a flatbed scanner with storage](images/wia-storage-tree1.png)

The preceding figure shows a WIA item tree for a scanner that supports flatbed platen scanning and a storage unit that contains one subfolder and two files.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Scanner%20Storage%20Architecture%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


