---
title: Requirements for Feeder Scanners Child Items
description: Requirements for Feeder Scanners Child Items
ms.assetid: 069ce228-ac73-42b5-9f1b-528ee6fe6a92
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements for Feeder Scanners Child Items


Child items in a feeder scanner item tree (that is, front and back items) are required to support most of the item properties and flags that the feeder item (that is, the parent item of the front and back items) supports.

### Item Flags

The child items must support all of the required item flags that are supported by the parent item, except for **WiaItemTypeTransfer**. The **WiaItemTypeTransfer** flag may optionally be supported; however, data transfers from automatic document feeders are completed off of the feeder item and not the child items.

### Item Properties

Child items in a feeder scanner item tree (or front and back items) are required to support most of the item properties that the parent feeder item supports. The child item must support [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) and all of the WIA\_IPS\_*Xxx* and WIA\_IPA\_*Xxx* properties that the feeder item supports that relate to scan configuration parameters for the current document side. These properties include both the required and optional properties on the feeder item. When a scaner performs advanced duplex scans, the image quality settings (or scan configuration parameters) set on the child item are used and those set on the feeder item are ignored.

**Note**   The property item settings for the child items must match the settings for the parent item properties. The only exception is the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property for child items; this property must be set to WIA\_CATEGORY\_FEEDER\_FRONT or WIA\_CATEGORY\_FEEDER\_BACK instead of to WIA\_CATEGORY\_FEEDER.

 

 

 




