---
title: WIA Data Item
description: WIA Data Item
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Data Item





This topic applies to Windows Vista and later.

Any item that can be used to transfer data is considered a data item. This includes items marked with the **WiaItemTypeProgrammableDataSource** flag. Any item marked with the **WiaItemTypeTransfer** flag can expose the ability to transfer data. Any item with this flag set must provide the following WIA properties:

[**WIA\_IPA\_ACCESS\_RIGHTS**](./wia-ipa-access-rights.md)

[**WIA\_IPA\_ITEM\_SIZE**](./wia-ipa-item-size.md)

[**WIA\_IPA\_BUFFER\_SIZE**](./wia-ipa-buffer-size.md)

[**WIA\_IPA\_FORMAT**](./wia-ipa-format.md)

[**WIA\_IPA\_PREFERRED\_FORMAT**](./wia-ipa-preferred-format.md)

[**WIA\_IPA\_TYMED**](./wia-ipa-tymed.md)

[**WIA\_IPA\_FILENAME\_EXTENSION**](./wia-ipa-filename-extension.md)

Programmable data source items marked with the **WiaItemTypeTransfer** flag must supply these WIA properties. For example, a flatbed scanner item must have these properties to be properly configured for data transfer.

WIA data items may have additional properties depending on the item's flag settings. For example, WIA items marked with the **WiaItemTypeImage** flag should have image-specific information properties, such as [**WIA\_IPA\_DEPTH**](./wia-ipa-depth.md) and [**WIA\_IPA\_NUMBER\_OF\_LINES**](./wia-ipa-number-of-lines.md).

 

