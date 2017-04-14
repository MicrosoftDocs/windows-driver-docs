---
title: WIA Item Flags for Scanner Storage
author: windows-driver-content
description: WIA Item Flags for Scanner Storage
ms.assetid: 493b7c4f-d36a-4447-92a3-34b42ef58397
---

# WIA Item Flags for Scanner Storage


This topic lists the required and optional WIA item flags for the root item and child items of a storage scanner item tree. For a complete list of the WIA item flags and their definitions, see [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585).

### Required WIA Item Flags for Scanners Storage

A WIA storage scanner folder item (WIA\_CATEGORY\_FOLDER) is required to support the following WIA item flags:

<a href="" id="wiaitemtypefolder"></a>**WiaItemTypeFolder**  
The item is a folder. This flag is required only for folder items.

<a href="" id="wiaitemtypestorage"></a>**WiaItemTypeStorage**  
The WIA item is a folder that may contain storage items. This flag is required only for folder items.

A WIA storage scanner file item (WIA\_CATEGORY\_FINISHED\_FILE) is required to support the following WIA item flags:

<a href="" id="wiaitemtypefile"></a>**WiaItemTypeFile**  
The item contains data available for transfer. This flag is also required by the **WiaItemTypeImage** flag.

<a href="" id="wiaitemtypetransfer"></a>**WiaItemTypeTransfer**  
The WIA item can be used to transfer data. This flag is required because the flatbed scanner item can be used to transfer data.

### Optional WIA Item Flags for Scanners Storage

A WIA storage scanner folder item (WIA\_CATEGORY\_FOLDER) can optionally support the following WIA item flags:

<a href="" id="wiaitemtypedeleted"></a>**WiaItemTypeDeleted**  
This flag may optionally be used when an item can be deleted.

A WIA storage scanner file item (WIA\_CATEGORY\_FINISHED\_FILE) can optionally support the following WIA item flags:

<a href="" id="wiaitemtypeaudio"></a>**WiaItemTypeAudio**  
The item is an audio file. This flag is required if the file contains audio data and is valid only for items that also have the **WiaItemTypeFile** flag set.

<a href="" id="wiaitemtypedeleted"></a>**WiaItemTypeDeleted**  
This flag may optionally be used when an item can be deleted.

<a href="" id="wiaitemtypeimage"></a>**WiaItemTypeImage**  
The item is an image. This flag is required if the file contains still image data and is valid only for items that also have the **WiaItemTypeFile** flag set.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Item%20Flags%20for%20Scanner%20Storage%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


