---
title: Opening, Initializing and Closing an SD Card Bus Interface
description: Opening, Initializing and Closing an SD Card Bus Interface
ms.assetid: 986a352e-c479-444d-9c65-7958dd638bbb
keywords:
- SD WDK buses , opening interfaces
- SD WDK buses , initializing interfaces
- SD WDK buses , closing interfaces
- initializing SD bus interfaces
- SdBusOpenInterface
- SDBUS_INTERFACE_STANDARD
- interfaces WDK SD bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening, Initializing and Closing an SD Card Bus Interface


Secure Digital (SD) device drivers must open and initialize an SD bus interface to interact with the devices they manage or the host controller. This requires two calls to the SD bus library: a call to [**SdBusOpenInterface**](https://msdn.microsoft.com/library/windows/hardware/ff537906) followed by a call to a routine supplied by the bus driver that initializes the interface. **SdBusOpenInterface** returns a pointer to the routine that initializes the interface in the **InterfaceReference** member of the [**SDBUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff537923) structure. The device driver must call this initialization routine to supply the bus driver with a pointer to an interrupt notification callback routine. The bus driver uses this callback to notify the device driver of a hardware interrupt. For more information about the routine that initializes an SD bus interface, see [**PSDBUS\_INITIALIZE\_INTERFACE\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff537618). The device driver normally opens and initializes an SD bus interface from within its [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

The following code example illustrates the sequence of calls that open and initialize an SD bus interface:

```cpp
  status = SdBusOpenInterface (pDevExt->UnderlyingPDO,
    &pDevExt->BusInterface,
    sizeof(SDBUS_INTERFACE_STANDARD),
    SDBUS_INTERFACE_VERSION);

  if (NT_SUCCESS(status)) {
    SDBUS_INTERFACE_PARAMETERS interfaceParameters = {0};
    interfaceParameters.Size = 
      sizeof(SDBUS_INTERFACE_PARAMETERS);
    interfaceParameters.TargetObject = 
      DeviceExtension->TargetObject;
    interfaceParameters.DeviceGeneratesInterrupts = TRUE;
    interfaceParameters.CallbackRoutine = pMyDriverCallback;
    status = STATUS_UNSUCCESSFUL;
    if (DeviceExtension->BusInterface.InitializeInterface) {
      status = (pDevExt->BusInterface.InitializeInterface)
        (pDevExt->BusInterface.Context, &interfaceParameters);
    }
      }
```

In this code example, the device driver calls **SdBusOpenInterface** to open the interface, and the bus driver stores a pointer to the initialization routine in the device extension (**DeviceExtension-&gt;BusInterface.InitializeInterface**). After **SdBusOpenInterface** returns, the driver retrieves this pointer from the device extension. Next, the driver puts a pointer to its own interrupt callback routine, **pMyDriverCallback,** in the [**SDBUS\_INTERFACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff537919) structure and passes this structure to the initialization routine.

The device driver must also retrieve the context information that **SdBusOpenInterface** returns in the **Context** member of the SDBUS\_INTERFACE\_STANDARD structure. Whenever the driver calls an SD bus interface routine, it must pass in this context data.

### Closing an SD Interface

To close an SD interface, drivers must dereference the interface by calling the routine in the **InterfaceDereference** member of the SDBUS\_INTERFACE\_STANDARD structure, which frees all resources allocated by the **SdBusOpenInterface** routine. SD device drivers should close all open SD interfaces when receiving any of the following IRPs:

[**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705)

[**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738)

[**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760)

The following code example illustrates how a driver can dereference an SD card bus interface:

```cpp
if (pDevExt->BusInterface.InterfaceDereference) {
    (pDevExt->BusInterface.InterfaceDereference) (pDevExt->BusInterface.Context);
    RtlZeroMemory(&pDevExt->BusInterface, sizeof(SDBUS_INTERFACE_STANDARD));
}
```

The **SdBusOpenInterface** call stores a pointer to the interface dereference routine in the SDBUS\_INTERFACE\_STANDARD structure. However, drivers should verify that the pointer is not **NULL** before attempting to call the routine.

 

 




