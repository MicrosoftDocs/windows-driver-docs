---
title: WIA Data Item
description: WIA Data Item
ms.assetid: 3ce01393-4a0b-4b70-8087-abe989aa00a9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Data Item





This topic applies to Windows Vista and later.

Any item that can be used to transfer data is considered a data item. This includes items marked with the **WiaItemTypeProgrammableDataSource** flag. Any item marked with the **WiaItemTypeTransfer** flag can expose the ability to transfer data. Any item with this flag set must provide the following WIA properties:

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-access-rights)

[**WIA\_IPA\_ITEM\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-size)

[**WIA\_IPA\_BUFFER\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-buffer-size)

[**WIA\_IPA\_FORMAT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-format)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-preferred-format)

[**WIA\_IPA\_TYMED**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-tymed)

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-filename-extension)

Programmable data source items marked with the **WiaItemTypeTransfer** flag must supply these WIA properties. For example, a flatbed scanner item must have these properties to be properly configured for data transfer.

WIA data items may have additional properties depending on the item's flag settings. For example, WIA items marked with the **WiaItemTypeImage** flag should have image-specific information properties, such as [**WIA\_IPA\_DEPTH**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-depth) and [**WIA\_IPA\_NUMBER\_OF\_LINES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-number-of-lines).

 

 




