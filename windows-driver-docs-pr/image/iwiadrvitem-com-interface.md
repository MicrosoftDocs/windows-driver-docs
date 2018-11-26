---
title: IWiaDrvItem COM Interface
description: IWiaDrvItem COM Interface
ms.assetid: 1be2265b-7ae8-4935-9559-588b885526d4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IWiaDrvItem COM Interface





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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543856" data-raw-source="[&lt;strong&gt;IWiaDrvItem::AddItemToFolder&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543856)"><strong>IWiaDrvItem::AddItemToFolder</strong></a></p></td>
<td><p>Adds the <strong>IWiaDrvItem</strong> object to a folder.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543863" data-raw-source="[&lt;strong&gt;IWiaDrvItem::DumpItemData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543863)"><strong>IWiaDrvItem::DumpItemData</strong></a></p></td>
<td><p>Dumps private driver item data.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543867" data-raw-source="[&lt;strong&gt;IWiaDrvItem::FindChildItemByName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543867)"><strong>IWiaDrvItem::FindChildItemByName</strong></a></p></td>
<td><p>Locates a child item by full item name.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543870" data-raw-source="[&lt;strong&gt;IWiaDrvItem::FindItemByName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543870)"><strong>IWiaDrvItem::FindItemByName</strong></a></p></td>
<td><p>Locates an item by full item name.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543873" data-raw-source="[&lt;strong&gt;IWiaDrvItem::GetDeviceSpecContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543873)"><strong>IWiaDrvItem::GetDeviceSpecContext</strong></a></p></td>
<td><p>Retrieves a pointer to a device-specific context.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543878" data-raw-source="[&lt;strong&gt;IWiaDrvItem::GetFirstChildItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543878)"><strong>IWiaDrvItem::GetFirstChildItem</strong></a></p></td>
<td><p>Returns the first child of this folder item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543881" data-raw-source="[&lt;strong&gt;IWiaDrvItem::GetFullItemName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543881)"><strong>IWiaDrvItem::GetFullItemName</strong></a></p></td>
<td><p>Retrieves full item name and hierarchy information.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543883" data-raw-source="[&lt;strong&gt;IWiaDrvItem::GetItemFlags&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543883)"><strong>IWiaDrvItem::GetItemFlags</strong></a></p></td>
<td><p>Returns WIA item flags.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543885" data-raw-source="[&lt;strong&gt;IWiaDrvItem::GetItemName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543885)"><strong>IWiaDrvItem::GetItemName</strong></a></p></td>
<td><p>Retrieves the item name.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543889" data-raw-source="[&lt;strong&gt;IWiaDrvItem::GetNextSiblingItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543889)"><strong>IWiaDrvItem::GetNextSiblingItem</strong></a></p></td>
<td><p>Finds the next sibling of this item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543892" data-raw-source="[&lt;strong&gt;IWiaDrvItem::GetParentItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543892)"><strong>IWiaDrvItem::GetParentItem</strong></a></p></td>
<td><p>Retrieves the parent item of this item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543899" data-raw-source="[&lt;strong&gt;IWiaDrvItem::RemoveItemFromFolder&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543899)"><strong>IWiaDrvItem::RemoveItemFromFolder</strong></a></p></td>
<td><p>Removes an item from parent folder.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543901" data-raw-source="[&lt;strong&gt;IWiaDrvItem::UnlinkItemTree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543901)"><strong>IWiaDrvItem::UnlinkItemTree</strong></a></p></td>
<td><p>Unlinks the driver item tree.</p></td>
</tr>
</tbody>
</table>

 

 

 




