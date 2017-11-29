---
title: WIA\_IPA\_FULL\_ITEM\_NAME
description: The WIA\_IPA\_FULL\_ITEM\_NAME property contains the full item name (the item name with path information).
ms.assetid: ba034507-264a-4960-80ab-d5cb0daa5c1a
keywords: ["WIA_IPA_FULL_ITEM_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_FULL_ITEM_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_IPA\_FULL\_ITEM\_NAME


The WIA\_IPA\_FULL\_ITEM\_NAME property contains the full item name (the item name with path information).

## <span id="ddk_wia_ipa_full_item_name_si"></span><span id="DDK_WIA_IPA_FULL_ITEM_NAME_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The *full item name* is the same as the *bstrFullItemName* parameter of the [**wiasCreateDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549160) service utility function. An application reads the WIA\_IPA\_FULL\_ITEM\_NAME property to determine which item it is currently using and where that item is located in the WIA item tree. Each item should have a unique name. Applications commonly use the full item name to search for items in the WIA item tree. The WIA service creates and maintains WIA\_IPA\_FULL\_ITEM\_NAME.

An application reads WIA\_IPA\_FULL\_ITEM\_NAME to determine the format of the image that it is about to receive. An application writes this property to set the format. WIA\_IPA\_FULL\_ITEM\_NAME depends on the [**WIA\_IPA\_TYMED**](wia-ipa-tymed.md) property. The WIA minidriver creates and maintains WIA\_IPA\_FULL\_ITEM\_NAME.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**IWiaMiniDrvTransferCallback::GetNextStream**](https://msdn.microsoft.com/library/windows/hardware/jj151551)

[**WIA\_IPA\_TYMED**](wia-ipa-tymed.md)

[**wiasCreateDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549160)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_FULL_ITEM_NAME%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





