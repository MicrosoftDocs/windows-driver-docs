---
title: Deleting an Item from the Driver Tree
description: Deleting an Item from the Driver Tree
ms.assetid: eea7565c-be15-4610-a1b4-16596d1daca2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting an Item from the Driver Tree





In order to delete a driver item, the WIA service calls the minidriver entry point [**IWiaMiniDrv::drvDeleteItem**](https://msdn.microsoft.com/library/windows/hardware/ff543961). In this method, the minidriver attempts to delete the item to which the WIA service context parameter *pWiasContext* points. If the item is successfully deleted, the method returns S\_OK and sets the device error value parameter, *plDevErrVal*, to zero. If a device error occurs, the method returns FAILED and a device-specific error value in *plDevErrVal*. The minidriver should call the [**wiasQueueEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549296) function to inform all connected applications that an item has been deleted.

After the root item has been deleted, the WIA service calls [**IWiaMiniDrv::drvFreeDrvItemContext**](https://msdn.microsoft.com/library/windows/hardware/ff543972) to free the resources used by the driver-specific context. The WIA service then deletes the item and the driver-specific context.

 

 




