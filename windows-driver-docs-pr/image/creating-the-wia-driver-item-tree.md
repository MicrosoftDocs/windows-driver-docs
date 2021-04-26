---
title: Creating the WIA Driver Item Tree
description: Creating the WIA Driver Item Tree
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating the WIA Driver Item Tree





After the minidriver is initialized, it must create the driver item tree in the [**IWiaMiniDrv::drvInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia) method by:

1.  Creating the driver item tree if it does not already exist. The minidriver sets the root item flags and creates the root item by calling the driver services library function [**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem). The minidriver stores the returned pointer to the root item in a private member variable.

2.  Creating child items for each item on the device using the [**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem) function. This function creates a device-specific context where the minidriver can store information about the item.

3.  Calling the [**IWiaDrvItem::AddItemToFolder**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-additemtofolder) method on each child item to add the item to the driver item tree.

 

