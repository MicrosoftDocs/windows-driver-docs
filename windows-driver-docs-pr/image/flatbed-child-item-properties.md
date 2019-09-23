---
title: Flatbed Child Item Properties
description: Flatbed Child Item Properties
ms.assetid: ad13e4a2-0c5c-43a5-ab83-fc2ef65b4467
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flatbed Child Item Properties


The child items of a WIA flatbed scanner item are required to support the following WIA properties:

[**WIA\_IPA\_ITEM\_CATEGORY**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-category)

[**WIA\_IPA\_ITEM\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-name)

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-full-item-name)

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-access-rights)

[**WIA\_IPS\_XEXTENT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xextent)

[**WIA\_IPS\_XPOS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xpos)

[**WIA\_IPS\_YEXTENT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-yextent)

[**WIA\_IPS\_YPOS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-ypos)

**Note**   The [**WIA\_IPA\_ITEM\_CATEGORY**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-category) property must be set to WIA\_CATEGORY\_FLATBED for both flatbed items and flatbed child items.

 

Child items can optionally support any other property that is supported by the parent item, except for the [**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-supports-child-item-creation) and [**WIA\_IPS\_SEGMENTATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-segmentation) properties.

 

 




