---
title: Deleting an Item from the Driver Tree
author: windows-driver-content
description: Deleting an Item from the Driver Tree
ms.assetid: eea7565c-be15-4610-a1b4-16596d1daca2
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Deleting an Item from the Driver Tree


## <a href="" id="ddk-deleting-an-item-from-the-driver-tree-si"></a>


In order to delete a driver item, the WIA service calls the minidriver entry point [**IWiaMiniDrv::drvDeleteItem**](https://msdn.microsoft.com/library/windows/hardware/ff543961). In this method, the minidriver attempts to delete the item to which the WIA service context parameter *pWiasContext* points. If the item is successfully deleted, the method returns S\_OK and sets the device error value parameter, *plDevErrVal*, to zero. If a device error occurs, the method returns FAILED and a device-specific error value in *plDevErrVal*. The minidriver should call the [**wiasQueueEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549296) function to inform all connected applications that an item has been deleted.

After the root item has been deleted, the WIA service calls [**IWiaMiniDrv::drvFreeDrvItemContext**](https://msdn.microsoft.com/library/windows/hardware/ff543972) to free the resources used by the driver-specific context. The WIA service then deletes the item and the driver-specific context.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Deleting%20an%20Item%20from%20the%20Driver%20Tree%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


