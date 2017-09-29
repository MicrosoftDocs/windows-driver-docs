---
title: Create a hardware notification client driver
author: windows-driver-content
description: This section provides general guidance on the development of a hardware notification client driver that utilizes the KMDF class extension provided by Microsoft.
ms.assetid: 348950d3-fb80-4800-a606-290d473aa412
---

# Create a hardware notification client driver


This section provides general guidance on the development of a hardware notification client driver that utilizes the KMDF class extension provided by Microsoft.

1.  Create a file for your client driver implementation that links to Mshwnclxstub.lib and includes the headers hwn.h and hwnclx.h.

2.  Define instances of the required KMDF and hardware notification class extension callback functions. Specifically, you must implement and register these callback functions as shown in the following example code.

    ```
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

    -   Defining the contents of the [**HWN\_CLIENT\_REGISTRATION\_PACKET**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843560), including the callback function pointers for use by the class extension. For more information about the required callback functions, see [Hardware notifications reference](https://msdn.microsoft.com/en-us/library/windows/hardware/dn789336).

    -   Calling [HwNRegisterClient](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843550) to register the client driver with the class extension.

4.  Implement the [*EVT\_WDF\_DRIVER\_DEVICE\_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) function, which is responsible for performing device initialization operations when the PnP manager reports the existence of a device. For the hardware notification client driver, this function should handle the following:

    -   Calling [**HwNProcessAddDevicePreDeviceCreate**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843549), which supplies the device prepare/release and entry/exit callbacks needed by the KMDF to transition the device into different states.

    -   Calling [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create a framework device object.

    -   Calling [**HwNProcessAddDevicePostDeviceCreate**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843548) to create I/O queues.

5.  Implement the defined [**HWN\_CLIENT\_INITIALIZE\_DEVICE**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843553) function, which is called by the class extension to prepare the hardware notification controller for use.

6.  Implement the defined [**HWN\_CLIENT\_UNINITIALIZE\_DEVICE**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt827292) function, which is called by the class extension to uninitialize the hardware notification controller.

7.  Implement the defined [**HWN\_CLIENT\_QUERY\_DEVICE\_INFORMATION**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843554) function, which is called by the class extension. This function is responsible for retrieving the attributes of a hardware notification component.

8.  Implement the defined [**HWN\_CLIENT\_START\_DEVICE**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843557) function, which is called by the class extension. This function is responsible for starting the hardware notification controller and for allocating ACPI resources for the client driver.

9.  Implement the defined [**HWN\_CLIENT\_STOP\_DEVICE**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843558) function, which is called by the class extension. This function is responsible for stopping the hardware notification controller and for releasing ACPI resources used by the client driver.

10. Implement the defined [**HWN\_CLIENT\_SET\_STATE**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843556), which is called by the class extension. This function is responsible for setting hardware notification component states.

11. Implement the defined [**HWN\_CLIENT\_GET\_STATE**](https://msdn.microsoft.com/en-us/library/windows/hardware/mt843552), which is called by the class extension. This function is responsible for getting the current values of the hardware notification components. When the input buffer is NULL, meaning the user did not specify the specific hardware notification state, this function should return state information for all hardware notification components.

## <span id="related_topics"></span>Related topics
[Hardware notifications](hardware-notifications-support.md)

[Hardware notifications reference](https://msdn.microsoft.com/en-us/library/windows/hardware/dn789336)

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Create%20a%20hardware%20notification%20client%20driver%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


