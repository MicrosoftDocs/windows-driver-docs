---
title: Device Initialization
---

# Device Initialization

A NetAdapterCx driver registers its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function when it calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) from its [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine.

## EVT_WDF_DRIVER_DEVICE_ADD

In [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), a NetAdapterCx client driver should do the following:

1. Call [**NetAdapterDeviceInitConfig**](netadapterdeviceinitconfig.md) in the beginning of *EVT_WDF_DRIVER_DEVICE_ADD*.

    ```cpp
    status = NetAdapterDeviceInitConfig(DeviceInit);
    if (!NT_SUCCESS(status)) {
        return status;
    }
    ```

2. Call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

3. Create the NETADAPTER object.  This object represents your NIC, which is the endpoint for all networking I/O.  To create the NETADAPTER object, the client typically calls [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md), followed by [**NetAdapterCreate**](netadaptercreate.md):

    ```cpp
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attribs, MYDRIVER_ADAPTER_CONTEXT);

    NET_ADAPTER_CONFIG_INIT (
        &config,
        EvtAdapterSetCapabilities,
        EvtAdapterCreateTxQueue,
        EvtAdapterCreateRxQueue);

    status = NetAdapterCreate(device, &attribs, &config, &adapter);
    ```

    Currently you can have only one NETADAPTER per WDFDEVICE, with the WDFDEVICE being the parent object of the NETADAPTER.  You can find the object hierarchy in [Summary of Objects](summary-of-objects.md).

Optionally, you can add context space to the NETADAPTER object. Since you can set a context on any WDF object, you could add separate context space for the WDFDEVICE and the NETADAPTER objects. In the example in step 4, the client adds `MYDRIVER_ADAPTER_CONTEXT` to the NETADAPTER object. For more info, see [Framework Object Context Space](../wdf/framework-object-context-space.md).

We recommend that you put device-related data in the context for your WDFDEVICE, and networking-related data into your NETADAPTER context.  If you are porting an existing NDIS 6.x driver, you'll likely have a single MiniportAdapterContext that combines networking-related and device-related data into a single data structure.  To simplify the porting process, just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER's context a small structure that points to the WDFDEVICE's context.

You'll provide 3 callbacks to [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md) macro:

* [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md)
* [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md)
* [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md)

For details on what to provide in your implementations of these callbacks, see the individual reference pages.
