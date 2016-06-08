---
title: Creating an FDO in the Battery Miniclass Driver
description: Creating an FDO in the Battery Miniclass Driver
ms.assetid: 3178710b-8e4a-4f9c-893b-1d06c4a3f7ff
keywords: ["battery miniclass drivers WDK , FDOs", "FDOs WDK battery", "functional device objects WDK battery"]
---

# Creating an FDO in the Battery Miniclass Driver


## <span id="ddk_creating_an_fdo_in_the_battery_miniclass_driver_dg"></span><span id="DDK_CREATING_AN_FDO_IN_THE_BATTERY_MINICLASS_DRIVER_DG"></span>


The miniclass driver should create an FDO and attach it to the device stack for the device, as follows:

1.  Call [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) to create an FDO for the current device, as follows:

    ```
    Status = IoCreateDevice(
             DriverObject,
             sizeof (DeviceExtension),
             NULL,
             FILE_DEVICE_BATTERY,
             0,
             FALSE,
             &amp;Fdo
             );
    ```

    The input parameters to [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) are a pointer to the driver object that was passed to the *AddDevice* routine, the size of the device extension, NULL in place of a device name, and the system-defined device type (FILE\_DEVICE\_BATTERY). Battery miniclass drivers can specify zero for the *DeviceCharacteristics* parameter, which is irrelevant to these drivers. More than one thread can send I/O requests to the battery, so the miniclass driver passes FALSE as the *Exclusive* parameter. **IoCreateDevice** returns a pointer to the created FDO.

2.  In the returned FDO, set flags and the stack size. For example:

    ```
    Fdo->Flags |= DO_BUFFERED_IO;
    Fdo->Flags |= DO_POWER_PAGABLE;
    Fdo->StackSize = Pdo->StackSize + 2;
    ```

    Setting the DO\_BUFFERED\_IO flag allows the miniclass driver to use buffered I/O for IRPs. Setting the DO\_POWER\_PAGABLE flag indicates that the driver is pageable and prevents it from getting power IRPs at IRQL &gt;= DISPATCH\_LEVEL. Finally, because battery IRPs require an additional stack location, miniclass drivers should set **StackSize** to the PDO stack size plus two, so that the driver can pass the IRP down to the PDO.

3.  Store the pointer to the device's PDO, the pointer to the FDO, the device type, the device name, and any other necessary state in the device extension. For example:

    ```
    NewBatt = (PNEW_BATT) Fdo->DeviceExtension;
    NewBatt->Type = NEW_BATTERY_TYPE;
    NewBatt->Fdo = Fdo;
    NewBatt->Pdo = Pdo;
    NewBatt->IsCacheValid = FALSE;
    ```

    The example stores the pointers to the FDO and PDO in the device extension. (The PnP Manager supplied a pointer to the PDO as the *PhysicalDeviceObject* pointer input to *AddDevice*.) In addition, the example above keeps track of its own battery type (NEW\_BATTERY\_TYPE, defined elsewhere in this hypothetical miniclass driver) and whether any cached information is valid.

    You determine the information stored in the device extension. For example, a smart battery driver might retain the number of batteries, a Boolean value indicating whether a battery selector is present, and, optionally, information about that battery selector.

4.  Call [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) to attach the FDO to the device stack, then store the returned pointer, as follows:

    ```
    NewBatt->LowerDO = IoAttachDeviceToDeviceStack(Fdo,Pdo);
    ```

    The call returns a pointer to the next-lower device object, which this example stores in the device extension.

5.  Clear the DO\_DEVICE\_INITIALIZING flag in the FDO, as follows:

    ```
    Fdo->Flags &amp;= ~DO_DEVICE_INITIALIZING;
    ```

    Clearing the DO\_DEVICE\_INITIALIZING flag allows the device object to be opened subsequently by components higher in the device stack.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Creating%20an%20FDO%20in%20the%20Battery%20Miniclass%20Driver%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




