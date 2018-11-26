---
title: Transferring Data from Scanner Storage
description: Transferring Data from Scanner Storage
ms.assetid: 6fc9c825-509c-4c18-a859-e1f5504879b8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transferring Data from Scanner Storage


To transfer data from the scanner storage item, a WIA application should enumerate the storage folder and file items that are contained by the root storage items and use each individual file item as the transfer source (to transfer the data that is contained by that particular item).

For a **WiaItemTypeImage** file item, the application may read the existing WIA\_IPS\_*Xxx* or WIA\_IPA\_*Xxx* (or both) properties that describe the image format (if supported). The application may also use this information to select images to be downloaded from the scanner storage.

To transfer data to one of the scanner storage folder items, a WIA application should enumerate the available storage folder items, select a folder or create a new folder item, and upload data to it.

**Note**  This enumeration operation should not be permitted outside the root storage folder.

 

 

 




