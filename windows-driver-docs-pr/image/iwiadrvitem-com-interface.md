---
title: IWiaDrvItem COM Interface
author: windows-driver-content
description: IWiaDrvItem COM Interface
MS-HAID:
- 'WIA\_arch\_04b2f58c-337b-49d0-8e0c-fc779a92d442.xml'
- 'image.iwiadrvitem\_com\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1be2265b-7ae8-4935-9559-588b885526d4
---

# IWiaDrvItem COM Interface


## <a href="" id="ddk-iwiadrvitem-com-interface-si"></a>


The [IWiaDrvItem interface](https://msdn.microsoft.com/library/windows/hardware/ff543896) provides methods that a WIA minidriver uses to manage a tree of **IWiaDrvItem** items. These methods allow a WIA minidriver to manipulate **IWiaDrvItem** objects. The **IWiaDrvItem** interface supplies the following methods.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaDrvItem::AddItemToFolder</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543856)</p></td>
<td><p>Adds the <strong>IWiaDrvItem</strong> object to a folder.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaDrvItem::DumpItemData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543863)</p></td>
<td><p>Dumps private driver item data.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaDrvItem::FindChildItemByName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543867)</p></td>
<td><p>Locates a child item by full item name.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaDrvItem::FindItemByName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543870)</p></td>
<td><p>Locates an item by full item name.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaDrvItem::GetDeviceSpecContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543873)</p></td>
<td><p>Retrieves a pointer to a device-specific context.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaDrvItem::GetFirstChildItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543878)</p></td>
<td><p>Returns the first child of this folder item.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaDrvItem::GetFullItemName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543881)</p></td>
<td><p>Retrieves full item name and hierarchy information.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaDrvItem::GetItemFlags</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543883)</p></td>
<td><p>Returns WIA item flags.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaDrvItem::GetItemName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543885)</p></td>
<td><p>Retrieves the item name.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaDrvItem::GetNextSiblingItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543889)</p></td>
<td><p>Finds the next sibling of this item.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaDrvItem::GetParentItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543892)</p></td>
<td><p>Retrieves the parent item of this item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaDrvItem::RemoveItemFromFolder</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543899)</p></td>
<td><p>Removes an item from parent folder.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaDrvItem::UnlinkItemTree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543901)</p></td>
<td><p>Unlinks the driver item tree.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20IWiaDrvItem%20COM%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


