---
title: Device Initialization
---

# Device Initialization

<!--does VS provide WdfDriverCreate in stubs?-->

In general, you'll need to provide these callbacks:

- [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693)
- [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880)
- [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848)

While you may need to provide optional event handlers specific to your device, there are only a few requirements that the client driver must meet in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693).

## EVT_WDF_DRIVER_DEVICE_ADD

In [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), a NetAdapterCx client driver should do the following:

1. Call [**NetAdapterDeviceInitConfig**](netadapterdeviceinitconfig.md).
2. Load pointers to your driver's callbacks and call [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135), as shown here:

    ```cpp
    status = NetAdapterDeviceInitConfig(DeviceInit);
    if (!NT_SUCCESS(status)) {
        return status;
    }

    WDF_PNPPOWER_EVENT_CALLBACKS_INIT(&pnpPowerCallbacks);
    pnpPowerCallbacks.EvtDevicePrepareHardware      = ...;
    pnpPowerCallbacks.EvtDeviceD0Entry              = ...;
    pnpPowerCallbacks.EvtDeviceD0Exit               = ...;
    pnpPowerCallbacks.EvtDeviceReleaseHardware      = ...;

    WdfDeviceInitSetPnpPowerEventCallbacks(DeviceInit, &pnpPowerCallbacks);
    ```

3. Call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

4. Create the NETADAPTER object.  This object represents your NIC, which is the endpoint for all networking I/O.  To create the NETADAPTER object, the client typically calls [**NET_ADAPTER_CONFIG_INIT method**](net-adapter-config-init.md), followed by [**NetAdapterCreate method**](netadaptercreate.md):

    ```cpp
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attribs, MYDRIVER_ADAPTER_CONTEXT);

    NET_ADAPTER_CONFIG_INIT (
        &config,
        EvtAdapterSetCapabilities,
        EvtAdapterCreateTxQueue,
        EvtAdapterCreateRxQueue);

    status = NetAdapterCreate(device, &attribs, &config, &adapter);
    ```

Typically, you'll have one NETADAPTER per WDFDEVICE, with the WDFDEVICE being the parent object of the NETADAPTER.  You can find the object hierarchy in [Summary of Objects](summary-of-objects.md).

Optionally, you can add context space to the object.   Since you can set a context on any WDF object, you could add separate context space for the WDFDEVICE and the NETADAPTER objects.  In the example in step 4, the client adds `MYDRIVER_ADAPTER_CONTEXT` to the NETADAPTER object.  For more info, see [Framework Object Context Space](../wdf/framework-object-context-space.md).

We recommend that you put device-related data in the context for your WDFDEVICE, and networking-related data into your NETADAPTER context.  If you are porting an existing NDIS 6.x driver, you'll likely have a single MiniportAdapterContext that combines networking-related and device-related data into a single data structure.  To simplify the porting process, just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER's context a small structure that points to the WDFDEVICE's context.

You'll provide 3 callbacks to [**NET_ADAPTER_CONFIG_INIT method**](net-adapter-config-init.md):

* [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md)
* [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md)
* [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md)

For details on what to provide in your implementations of these callbacks, see the individual reference pages.
