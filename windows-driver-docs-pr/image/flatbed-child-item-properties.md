---
title: Flatbed Child Item Properties
description: Flatbed Child Item Properties
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flatbed Child Item Properties


The child items of a WIA flatbed scanner item are required to support the following WIA properties:

[**WIA\_IPA\_ITEM\_CATEGORY**](./wia-ipa-item-category.md)

[**WIA\_IPA\_ITEM\_NAME**](./wia-ipa-item-name.md)

[**WIA\_IPA\_FULL\_ITEM\_NAME**](./wia-ipa-full-item-name.md)

[**WIA\_IPA\_ACCESS\_RIGHTS**](./wia-ipa-access-rights.md)

[**WIA\_IPS\_XEXTENT**](./wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](./wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](./wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](./wia-ips-ypos.md)

**Note**   The [**WIA\_IPA\_ITEM\_CATEGORY**](./wia-ipa-item-category.md) property must be set to WIA\_CATEGORY\_FLATBED for both flatbed items and flatbed child items.

 

Child items can optionally support any other property that is supported by the parent item, except for the [**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](./wia-ips-supports-child-item-creation.md) and [**WIA\_IPS\_SEGMENTATION**](./wia-ips-segmentation.md) properties.

 

