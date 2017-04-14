---
title: Transferring Data from Scanner Storage
author: windows-driver-content
description: Transferring Data from Scanner Storage
ms.assetid: 6fc9c825-509c-4c18-a859-e1f5504879b8
---

# Transferring Data from Scanner Storage


To transfer data from the scanner storage item, a WIA application should enumerate the storage folder and file items that are contained by the root storage items and use each individual file item as the transfer source (to transfer the data that is contained by that particular item).

For a **WiaItemTypeImage** file item, the application may read the existing WIA\_IPS\_*Xxx* or WIA\_IPA\_*Xxx* (or both) properties that describe the image format (if supported). The application may also use this information to select images to be downloaded from the scanner storage.

To transfer data to one of the scanner storage folder items, a WIA application should enumerate the available storage folder items, select a folder or create a new folder item, and upload data to it.

**Note**  This enumeration operation should not be permitted outside the root storage folder.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Transferring%20Data%20from%20Scanner%20Storage%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


