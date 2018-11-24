---
title: Create a hardware notification client driver
description: This section provides general guidance on the development of a hardware notification client driver that utilizes the KMDF class extension provided by Microsoft.
ms.assetid: 348950d3-fb80-4800-a606-290d473aa412
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Create a hardware notification client driver


This section provides general guidance on the development of a hardware notification client driver that utilizes the KMDF class extension provided by Microsoft.

1.  Create a file for your client driver implementation that links to Mshwnclxstub.lib and includes the headers hwn.h and hwnclx.h.

2.  Define instances of the required KMDF and hardware notification class extension callback functions. Specifically, you must implement and register these callback functions as shown in the following example code.

    ```cpp
    DRIVER_INITIALIZE DriverEntry;
    EVT_WDF_DRIVER_DEVICE_ADD HwnClientEvtDeviceAdd;
    HWN_CLIENT_INITIALIZE_DEVICE HwnClientInitializeDevice;
    HWN_CLIENT_UNINITIALIZE_DEVICE HwnClientUnInitializeDevice;
    HWN_CLIENT_QUERY_DEVICE_INFORMATION HwnClientQueryDeviceInformation;
    HWN_CLIENT_START_DEVICE HwnClientStartDevice;
    HWN_CLIENT_STOP_DEVICE HwnClientStopDevice;
    HWN_CLIENT_SET_STATE HwnClientSetState;
    HWN_CLIENT_GET_STATE HwnClientGetState;
    ```

3.  Implement the [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, which is the client driver entry point and responsible for initialization. For the hardware notification client driver, this function should handle the following:

    -   Calling [**WDF\_DRIVER\_CONFIG\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff551302) to initialize the driver’s [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300) structure.

    -   Calling [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) to create a framework driver object for the client driver.

    -   Defining the contents of the [**HWN\_CLIENT\_REGISTRATION\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/mt843560), including the callback function pointers for use by the class extension. For more information about the required callback functions, see [Hardware notifications reference](https://msdn.microsoft.com/library/windows/hardware/dn789336).

    -   Calling [HwNRegisterClient](https://msdn.microsoft.com/library/windows/hardware/mt843550) to register the client driver with the class extension.

4.  Implement the [*EVT\_WDF\_DRIVER\_DEVICE\_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) function, which is responsible for performing device initialization operations when the PnP manager reports the existence of a device. For the hardware notification client driver, this function should handle the following:

    -   Calling [**HwNProcessAddDevicePreDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/mt843549), which supplies the device prepare/release and entry/exit callbacks needed by the KMDF to transition the device into different states.

    -   Calling [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create a framework device object.

    -   Calling [**HwNProcessAddDevicePostDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/mt843548) to create I/O queues.

5.  Implement the defined [**HWN\_CLIENT\_INITIALIZE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/mt843553) function, which is called by the class extension to prepare the hardware notification controller for use.

6.  Implement the defined [**HWN\_CLIENT\_UNINITIALIZE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/mt827292) function, which is called by the class extension to uninitialize the hardware notification controller.

7.  Implement the defined [**HWN\_CLIENT\_QUERY\_DEVICE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/mt843554) function, which is called by the class extension. This function is responsible for retrieving the attributes of a hardware notification component.

8.  Implement the defined [**HWN\_CLIENT\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/mt843557) function, which is called by the class extension. This function is responsible for starting the hardware notification controller and for allocating ACPI resources for the client driver.

9.  Implement the defined [**HWN\_CLIENT\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/mt843558) function, which is called by the class extension. This function is responsible for stopping the hardware notification controller and for releasing ACPI resources used by the client driver.

10. Implement the defined [**HWN\_CLIENT\_SET\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt843556), which is called by the class extension. This function is responsible for setting hardware notification component states.

11. Implement the defined [**HWN\_CLIENT\_GET\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt843552), which is called by the class extension. This function is responsible for getting the current values of the hardware notification components. When the input buffer is NULL, meaning the user did not specify the specific hardware notification state, this function should return state information for all hardware notification components.

## <span id="related_topics"></span>Related topics
[Hardware notifications](hardware-notifications-support.md)

[Hardware notifications reference](https://msdn.microsoft.com/library/windows/hardware/dn789336)



