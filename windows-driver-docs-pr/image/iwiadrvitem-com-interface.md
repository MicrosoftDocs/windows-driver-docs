---
title: IWiaDrvItem COM Interface
description: IWiaDrvItem COM interface
ms.date: 05/03/2023
---

# IWiaDrvItem COM interface

The [IWiaDrvItem interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiadrvitem) provides methods that a WIA minidriver uses to manage a tree of **IWiaDrvItem** items. These methods allow a WIA minidriver to manipulate **IWiaDrvItem** objects.

The **IWiaDrvItem** interface supplies the following methods.

| Method | Description |
|--|--|
| [**IWiaDrvItem::AddItemToFolder**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-additemtofolder) | Adds the **IWiaDrvItem** object to a folder. |
| [**IWiaDrvItem::DumpItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-dumpitemdata) | Dumps private driver item data. |
| [**IWiaDrvItem::FindChildItemByName**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-findchilditembyname) | Locates a child item by full item name. |
| [**IWiaDrvItem::FindItemByName**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-finditembyname) | Locates an item by full item name. |
| [**IWiaDrvItem::GetDeviceSpecContext**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getdevicespeccontext) | Retrieves a pointer to a device-specific context. |
| [**IWiaDrvItem::GetFirstChildItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getfirstchilditem) | Returns the first child of this folder item. |
| [**IWiaDrvItem::GetFullItemName**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getfullitemname) | Retrieves full item name and hierarchy information. |
| [**IWiaDrvItem::GetItemFlags**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getitemflags) | Returns WIA item flags. |
| [**IWiaDrvItem::GetItemName**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getitemname) | Retrieves the item name. |
| [**IWiaDrvItem::GetNextSiblingItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getnextsiblingitem) | Finds the next sibling of this item. |
| [**IWiaDrvItem::GetParentItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getparentitem) | Retrieves the parent item of this item. |
| [**IWiaDrvItem::RemoveItemFromFolder**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-removeitemfromfolder) | Removes an item from parent folder. |
| [**IWiaDrvItem::UnlinkItemTree**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-unlinkitemtree) | Unlinks the driver item tree. |
