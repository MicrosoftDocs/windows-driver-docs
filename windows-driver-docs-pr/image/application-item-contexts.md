---
title: Application Item Contexts
description: Application Item Contexts
ms.date: 04/20/2017
---

# Application Item Contexts





An application item context, also known as a *WIA service context*, is a reference to a root or child item that the WIA service passes to the minidriver in a call to one of several [IWiaMiniDrv interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv) methods. The minidriver then uses this reference when it calls certain WIA service library functions. The application item context for the item indicates which item is to be processed in the method. The minidriver should not attempt to directly access the application item context. A minidriver can determine whether the item is a root item or a child item by calling the driver services library function, [**wiasGetItemType**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetitemtype).

When an application requests a data transfer from the device to a WIA item it created, it calls on the WIA service to initiate the transfer. The WIA service passes the application item's context to a minidriver entry point such as the [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) method. Subsequently, when the minidriver uses a WIA service library function, such as [**wiasReadPropLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadproplong), and passes in the application item context, the WIA service reads the specified property from the property storage associated with that application item.

 

