---
title: WIA Data Item
author: windows-driver-content
description: WIA Data Item
ms.assetid: 3ce01393-4a0b-4b70-8087-abe989aa00a9
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Data Item


## <a href="" id="ddk-wia-data-item-si"></a>


This topic applies to Windows Vista and later.

Any item that can be used to transfer data is considered a data item. This includes items marked with the **WiaItemTypeProgrammableDataSource** flag. Any item marked with the **WiaItemTypeTransfer** flag can expose the ability to transfer data. Any item with this flag set must provide the following WIA properties:

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff551518)

[**WIA\_IPA\_ITEM\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551594)

[**WIA\_IPA\_BUFFER\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551527)

[**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551623)

[**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656)

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff551549)

Programmable data source items marked with the **WiaItemTypeTransfer** flag must supply these WIA properties. For example, a flatbed scanner item must have these properties to be properly configured for data transfer.

WIA data items may have additional properties depending on the item's flag settings. For example, WIA items marked with the **WiaItemTypeImage** flag should have image-specific information properties, such as [**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546) and [**WIA\_IPA\_NUMBER\_OF\_LINES**](https://msdn.microsoft.com/library/windows/hardware/ff551611).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Data%20Item%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


