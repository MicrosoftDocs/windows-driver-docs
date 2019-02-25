---
title: WIA Item Flags for Scanner Storage
description: WIA Item Flags for Scanner Storage
ms.assetid: 493b7c4f-d36a-4447-92a3-34b42ef58397
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




