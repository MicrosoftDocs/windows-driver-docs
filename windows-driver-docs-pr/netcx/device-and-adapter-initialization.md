---
title: Device and adapter initialization
description: Device and adapter initialization
keywords:
- NetAdapterCx device initialization, NetCx device initialization, NetAdapterCx adapter initialization, NetCx adapter initialization
ms.date: 01/07/2019
ms.localizationpriority: medium
ms.custom: Vib
---

# Device and adapter initialization

This topic describes the steps for a NetAdapterCx client driver to initialize and start WDFDEVICE and NETADAPTER objects. For more info about these objects and their relationship, see [Summary of NetAdapterCx objects](summary-of-netadaptercx-objects.md).

## EVT_WDF_DRIVER_DEVICE_ADD

A NetAdapterCx client driver registers its [*EVT_WDF_DRIVER_DEVICE_ADD*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function when it calls [**WdfDriverCreate**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate) from its [*DriverEntry*](../wdf/driverentry-for-kmdf-drivers.md) routine.

In [*EVT_WDF_DRIVER_DEVICE_ADD*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add), a NetAdapterCx client driver should do the following in order:

1. Call [**NetDeviceInitConfig**](/windows-hardware/drivers/ddi/netdevice/nf-netdevice-netdeviceinitconfig).

    ```C++
    status = NetDeviceInitConfig(DeviceInit);
    if (!NT_SUCCESS(status)) 
    {
        return status;
    }
    ```

2. Call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate). 

    > [!TIP]
    > If your device supports more than one NETADAPTER, we recommend storing pointers to each adapter in your device context.

3. Create the NETADAPTER object. To do so, the client calls [**NetAdapterInitAllocate**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterinitallocate), followed by optional **NetAdapterInitSetXxx** methods to initailize the adapter's attributes. Finally, the client calls [**NetAdapterCreate**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadaptercreate). 

    The following example shows how a client driver might initialize a NETADAPTER object. Note that error handling is simplified in this example.

    ```C++
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attribs, MY_ADAPTER_CONTEXT);

    //
    // Allocate the initialization structure
    //
    PNETADAPTER_INIT adapterInit = NetAdapterInitAllocate(device);
    if(adapterInit == NULL)
    {
        return status;
    }        

    //
    // Optional: set additional attributes
    //

    // Datapath callbacks for creating packet queues
    NET_ADAPTER_DATAPATH_CALLBACKS datapathCallbacks;
    NET_ADAPTER_DATAPATH_CALLBACKS_INIT(&datapathCallbacks,
                                        MyEvtAdapterCreateTxQueue,
                                        MyEvtAdapterCreateRxQueue);
    NetAdapterInitSetDatapathCallbacks(adapterInit,
                                       datapathCallbacks);
    // 
    // Required: create the adapter
    //
    NETADAPTER* netAdapter;
    status = NetAdapterCreate(adapterInit, &attribs, netAdapter);
    if(!NT_SUCCESS(status))
    {
        NetAdapterInitFree(adapterInit);
        adapterInit = NULL;
        return status;
    }

    //
    // Required: free the adapter initialization object even 
    // if adapter creation succeeds
    //
    NetAdapterInitFree(adapterInit);
    adapterInit = NULL;

    //
    // Optional: initialize the adapter's context
    //
    PMY_ADAPTER_CONTEXT adapterContext = GetMyAdapterContext(&netAdapter);
    ...
    ```

Optionally, you can add context space to the NETADAPTER object. Since you can set a context on any WDF object, you could add separate context space for the WDFDEVICE and the NETADAPTER objects. In the example in step 3, the client adds `MY_ADAPTER_CONTEXT` to the NETADAPTER object. For more info, see [Framework Object Context Space](../wdf/framework-object-context-space.md).

We recommend that you put device-related data in the context for your WDFDEVICE, and networking-related data such as link layer addresses into your NETADAPTER context. If you are porting an existing NDIS 6.x driver, you'll likely have a single MiniportAdapterContext that combines networking-related and device-related data into a single data structure. To simplify the porting process, just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER's context a small structure that points to the WDFDEVICE's context.

You can optionally provide 2 callbacks to the [**NET_ADAPTER_DATAPATH_CALLBACKS_INIT**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-net_adapter_datapath_callbacks_init) method:

* [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](/windows-hardware/drivers/ddi/netadapter/nc-netadapter-evt_net_adapter_create_txqueue)
* [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](/windows-hardware/drivers/ddi/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue)

For details on what to provide in your implementations of these callbacks, see the individual reference pages.

## EVT_WDF_DEVICE_PREPARE_HARDWARE

Many NetAdapterCx client drivers start their adapters from within their [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function, with the notable exception of [Mobile Broadband class extension client drivers](mobile-broadband-mbb-wdf-class-extension-mbbcx.md). To register an *EVT_WDF_DEVICE_PREPARE_HARDWARE* callback function, a NetAdapterCx client driver must call [**WdfDeviceInitSetPnpPowerEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks).

 Within [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware), in addition to other hardware preparation tasks the client driver sets the adapter's required and optional capabilities.

NetAdapterCx requires the client driver to set the following capabilities:

* Data path capabilities. The driver calls [**NetAdapterSetDataPathCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadaptersetdatapathcapabilities) to set these capabilities. For more information, see [Network data buffer management](./network-data-buffer-management.md).

* Link layer capabilities. The driver calls [**NetAdapterSetDataPathCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadaptersetlinklayercapabilities) to set these capabilities.

* Link layer maximum transfer unit (MTU) size. The driver calls [**NetAdapterSetDataPathCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadaptersetlinklayercapabilities) to set the MTU size.

The driver must then call [**NetAdapterStart**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart) to start their adapter.

The following example shows how a client driver might start a NETADAPTER object. Note that code required for setting up each adapter capabilities method is left out for brevity and clarity, and error handling is simplified.

```C++
PMY_DEVICE_CONTEXT deviceContext = GetMyDeviceContext(device);

NETADAPTER netAdapter = deviceContext->NetAdapter;

PMY_ADAPTER_CONTEXT adapterContext = GetMyAdapterContext(netAdapter);

//
// Set required adapter capabilities
//

// Link layer capabilities
...
NetAdapterSetDatapathCapabilities(netAdapter,
                                  &txCapabilities,
                                  &rxCapabilities);
...
NetAdapterSetLinkLayerCapabilities(netAdapter,
                                   &linkLayerCapabilities);
...
NetAdapterSetLinkLayerMtuSize(netAdapter,
                              MY_MAX_PACKET_SIZE - ETHERNET_HEADER_LENGTH);

//
// Set optional adapter capabilities
//

// Link layer capabilities
...
NetAdapterSetPermanentLinkLayerAddress(netAdapter,
                                       &adapterContext->PermanentAddress);
...
NetAdapterSetCurrentLinkLayerAddress(netAdapter,
                                     &adapterContext->CurrentAddress);

// Datapath capabilities
...
NetAdapterSetDatapathCapabilities(netAdapter,
                                  &txCapabilities,
                                  &rxCapabilities);

// Receive scaling capabilities
...
NetAdapterSetReceiveScalingCapabilities(netAdapter,
                                        &receiveScalingCapabilities);

// Hardware offload capabilities
...
NetAdapterOffloadSetChecksumCapabilities(netAdapter,
                                         &checksumCapabilities);
...
NetAdapterOffloadSetLsoCapabilities(netAdapter,
                                    &lsoCapabilities);
...
NetAdapterOffloadSetRscCapabilities(netAdapter,
                                    &rscCapabilities);

//
// Required: start the adapter
//
status = NetAdapterStart(netAdapter);
if(!NT_SUCCESS(status))
{
    return status;
}
```
