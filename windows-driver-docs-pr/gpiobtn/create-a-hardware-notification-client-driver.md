---
title: Create a Hardware Notification Client Driver
description: This section provides general guidance on the development of a hardware notification client driver that utilizes the KMDF class extension provided by Microsoft.
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

3.  Implement the [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, which is the client driver entry point and responsible for initialization. For the hardware notification client driver, this function should handle the following:

    -   Calling [**WDF\_DRIVER\_CONFIG\_INIT**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdf_driver_config_init) to initialize the driver’s [**WDF\_DRIVER\_CONFIG**](/windows-hardware/drivers/ddi/wdfdriver/ns-wdfdriver-_wdf_driver_config) structure.

    -   Calling [**WdfDriverCreate**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate) to create a framework driver object for the client driver.

    -   Defining the contents of the [**HWN\_CLIENT\_REGISTRATION\_PACKET**](/windows-hardware/drivers/ddi/hwnclx/ns-hwnclx-_hwn_client_registration_packet), including the callback function pointers for use by the class extension. For more information about the required callback functions, see [Hardware notifications reference](/windows-hardware/drivers/ddi/index).

    -   Calling [HwNRegisterClient](/windows-hardware/drivers/ddi/hwnclx/nf-hwnclx-hwnregisterclient) to register the client driver with the class extension.

4.  Implement the [*EVT\_WDF\_DRIVER\_DEVICE\_ADD*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) function, which is responsible for performing device initialization operations when the PnP manager reports the existence of a device. For the hardware notification client driver, this function should handle the following:

    -   Calling [**HwNProcessAddDevicePreDeviceCreate**](/windows-hardware/drivers/ddi/hwnclx/nf-hwnclx-hwnprocessadddevicepredevicecreate), which supplies the device prepare/release and entry/exit callbacks needed by the KMDF to transition the device into different states.

    -   Calling [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a framework device object.

    -   Calling [**HwNProcessAddDevicePostDeviceCreate**](/windows-hardware/drivers/ddi/hwnclx/nf-hwnclx-hwnprocessadddevicepostdevicecreate) to create I/O queues.

5.  Implement the defined [**HWN\_CLIENT\_INITIALIZE\_DEVICE**](/windows-hardware/drivers/ddi/hwnclx/nc-hwnclx-hwn_client_initialize_device) function, which is called by the class extension to prepare the hardware notification controller for use.

6.  Implement the defined [**HWN\_CLIENT\_UNINITIALIZE\_DEVICE**](/windows-hardware/drivers/ddi/hwnclx/nc-hwnclx-hwn_client_uninitialize_device) function, which is called by the class extension to uninitialize the hardware notification controller.

7.  Implement the defined [**HWN\_CLIENT\_QUERY\_DEVICE\_INFORMATION**](/windows-hardware/drivers/ddi/hwnclx/nc-hwnclx-hwn_client_query_device_information) function, which is called by the class extension. This function is responsible for retrieving the attributes of a hardware notification component.

8.  Implement the defined [**HWN\_CLIENT\_START\_DEVICE**](/windows-hardware/drivers/ddi/hwnclx/nc-hwnclx-hwn_client_start_device) function, which is called by the class extension. This function is responsible for starting the hardware notification controller and for allocating ACPI resources for the client driver.

9.  Implement the defined [**HWN\_CLIENT\_STOP\_DEVICE**](/windows-hardware/drivers/ddi/hwnclx/nc-hwnclx-hwn_client_stop_device) function, which is called by the class extension. This function is responsible for stopping the hardware notification controller and for releasing ACPI resources used by the client driver.

10. Implement the defined [**HWN\_CLIENT\_SET\_STATE**](/windows-hardware/drivers/ddi/hwnclx/nc-hwnclx-hwn_client_set_state), which is called by the class extension. This function is responsible for setting hardware notification component states.

11. Implement the defined [**HWN\_CLIENT\_GET\_STATE**](/windows-hardware/drivers/ddi/hwnclx/nc-hwnclx-hwn_client_get_state), which is called by the class extension. This function is responsible for getting the current values of the hardware notification components. When the input buffer is NULL, meaning the user did not specify the specific hardware notification state, this function should return state information for all hardware notification components.

## <span id="related_topics"></span>Related topics
[Hardware notifications](hardware-notifications-support.md)

