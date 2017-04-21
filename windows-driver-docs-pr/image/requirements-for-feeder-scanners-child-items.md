---
title: Requirements for Feeder Scanners Child Items
author: windows-driver-content
description: Requirements for Feeder Scanners Child Items
ms.assetid: 069ce228-ac73-42b5-9f1b-528ee6fe6a92
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Requirements for Feeder Scanners Child Items


Child items in a feeder scanner item tree (that is, front and back items) are required to support most of the item properties and flags that the feeder item (that is, the parent item of the front and back items) supports.

### Item Flags

The child items must support all of the required item flags that are supported by the parent item, except for **WiaItemTypeTransfer**. The **WiaItemTypeTransfer** flag may optionally be supported; however, data transfers from automatic document feeders are completed off of the feeder item and not the child items.

### Item Properties

Child items in a feeder scanner item tree (or front and back items) are required to support most of the item properties that the parent feeder item supports. The child item must support [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) and all of the WIA\_IPS\_*Xxx* and WIA\_IPA\_*Xxx* properties that the feeder item supports that relate to scan configuration parameters for the current document side. These properties include both the required and optional properties on the feeder item. When a scaner performs advanced duplex scans, the image quality settings (or scan configuration parameters) set on the child item are used and those set on the feeder item are ignored.

**Note**   The property item settings for the child items must match the settings for the parent item properties. The only exception is the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property for child items; this property must be set to WIA\_CATEGORY\_FEEDER\_FRONT or WIA\_CATEGORY\_FEEDER\_BACK instead of to WIA\_CATEGORY\_FEEDER.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Requirements%20for%20Feeder%20Scanners%20Child%20Items%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


