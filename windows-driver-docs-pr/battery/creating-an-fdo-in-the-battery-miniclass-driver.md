---
title: Creating an FDO in the Battery Miniclass Driver
description: Creating an FDO in the Battery Miniclass Driver
ms.assetid: 3178710b-8e4a-4f9c-893b-1d06c4a3f7ff
keywords:
- battery miniclass drivers WDK , FDOs
- FDOs WDK battery
- functional device objects WDK battery
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an FDO in the Battery Miniclass Driver


## <span id="ddk_creating_an_fdo_in_the_battery_miniclass_driver_dg"></span><span id="DDK_CREATING_AN_FDO_IN_THE_BATTERY_MINICLASS_DRIVER_DG"></span>


The miniclass driver should create an FDO and attach it to the device stack for the device, as follows:

1.  Call [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) to create an FDO for the current device, as follows:

    ```cpp
    Status = IoCreateDevice(
             DriverObject,
             sizeof (DeviceExtension),
             NULL,
             FILE_DEVICE_BATTERY,
             0,
             FALSE,
             &Fdo
             );
    ```

    The input parameters to [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) are a pointer to the driver object that was passed to the *AddDevice* routine, the size of the device extension, NULL in place of a device name, and the system-defined device type (FILE\_DEVICE\_BATTERY). Battery miniclass drivers can specify zero for the *DeviceCharacteristics* parameter, which is irrelevant to these drivers. More than one thread can send I/O requests to the battery, so the miniclass driver passes FALSE as the *Exclusive* parameter. **IoCreateDevice** returns a pointer to the created FDO.

2.  In the returned FDO, set flags and the stack size. For example:

    ```cpp
    Fdo->Flags |= DO_BUFFERED_IO;
    Fdo->Flags |= DO_POWER_PAGABLE;
    Fdo->StackSize = Pdo->StackSize + 2;
    ```

    Setting the DO\_BUFFERED\_IO flag allows the miniclass driver to use buffered I/O for IRPs. Setting the DO\_POWER\_PAGABLE flag indicates that the driver is pageable and prevents it from getting power IRPs at IRQL &gt;= DISPATCH\_LEVEL. Finally, because battery IRPs require an additional stack location, miniclass drivers should set **StackSize** to the PDO stack size plus two, so that the driver can pass the IRP down to the PDO.

3.  Store the pointer to the device's PDO, the pointer to the FDO, the device type, the device name, and any other necessary state in the device extension. For example:

    ```cpp
    NewBatt = (PNEW_BATT) Fdo->DeviceExtension;
    NewBatt->Type = NEW_BATTERY_TYPE;
    NewBatt->Fdo = Fdo;
    NewBatt->Pdo = Pdo;
    NewBatt->IsCacheValid = FALSE;
    ```

    The example stores the pointers to the FDO and PDO in the device extension. (The PnP Manager supplied a pointer to the PDO as the *PhysicalDeviceObject* pointer input to *AddDevice*.) In addition, the example above keeps track of its own battery type (NEW\_BATTERY\_TYPE, defined elsewhere in this hypothetical miniclass driver) and whether any cached information is valid.

    You determine the information stored in the device extension. For example, a smart battery driver might retain the number of batteries, a Boolean value indicating whether a battery selector is present, and, optionally, information about that battery selector.

4.  Call [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) to attach the FDO to the device stack, then store the returned pointer, as follows:

    ```cpp
    NewBatt->LowerDO = IoAttachDeviceToDeviceStack(Fdo,Pdo);
    ```

    The call returns a pointer to the next-lower device object, which this example stores in the device extension.

5.  Clear the DO\_DEVICE\_INITIALIZING flag in the FDO, as follows:

    ```cpp
    Fdo->Flags &= ~DO_DEVICE_INITIALIZING;
    ```

    Clearing the DO\_DEVICE\_INITIALIZING flag allows the device object to be opened subsequently by components higher in the device stack.

 

 




