# Porting NDIS miniport drivers to NetAdapter class extension

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

This page describes how to convert an NDIS 6.x miniport driver into a Windows Driver Framework (WDF) networking client miniport driver.

For general information about WDF, please review the [WDF Driver Development Guide](../wdf/index.md).

## Compilation settings

1. First, ensure that your project links against the latest version of KMDF.  To do so in Visual Studio, navigate to **Configuration Properties->Driver Settings->Driver Model** and verify that **Type of driver** is set to KMDF, and that **KMDF Version Major** and **KMDF Version Minor** are both empty.
2. Also link against NetAdapterCxStub.lib (located in `Windows Kits\10\Lib\<latest_windows_version>\km\<architecture>\netadaptercx\1.0`).
    * If your driver calls NDIS APIs, link against `ndis.lib`.
3. Remove NDIS preprocessor macros, like NDIS650_MINIPORT=1.
4. Add the following headers to every source file (or to your common/precompiled header):
```cpp
#include <ntddk.h>
#include <wdf.h>
#include <netadaptercx.h>
```
5. Add [standard WDF decorations](../wdf/specifying-wdf-directives-in-inf-files.md) to your INF:

Finally, add [standard WDF decorations](../wdf/specifying-wdf-directives-in-inf-files.md) to your INF:

```Inf
[Yourdriver.Wdf]
KmdfService = Yourdriverservice, Yourdriver.wdfsect

[Yourdriver.wdfsect]
KmdfLibraryVersion = <insert here>
```

## Driver initialization

Remove the call to [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) from [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff540807), and add the following:

```cpp
WDF_DRIVER_CONFIG_INIT(&config, EvtDriverDeviceAdd);
status = WdfDriverCreate(. . . );
if (!NT_SUCCESS(status)) {
    return status;
}
```

If it is set, remove the **WdfDriverInitNoDispatchOverride** flag from the call to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175).

*DriverUnload* is an optional routine for a WDF networking client driver, so you can remove it if you like.  Do not call [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) from *DriverUnload*.

## Device initialization

Next, you'll distribute code from *MiniportInitializeEx* into the appropriate WDF event callback handlers, several of which are optional.  For details on the callback sequence, see [Power-Up Sequence for an Network Adapter WDF Client Driver](power-up-sequence-for-ndis-wdf-client-driver.md).

In general, you'll need to provide these callbacks:

- [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693)
- [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880)
- [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848)

While you may need to provide optional event handlers specific to your device, there are only a few requirements that the client driver must meet in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693).

### Creating the NETADAPTER object

In [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), your driver should do the following:

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

Typically, you'll have one NETADAPTER per WDFDEVICE, with the WDFDEVICE being the parent object of the NETADAPTER.

Optionally, you can add context space to the object.   Since you can set a context on any WDF object, you could add separate context space for the WDFDEVICE and the NETADAPTER objects.  In the example in step 4, the client adds `MYDRIVER_ADAPTER_CONTEXT` to the NETADAPTER object.  For more info, see [Framework Object Context Space](../wdf/framework-object-context-space.md).

We recommend that you put device-related data in the context for your WDFDEVICE, and networking-related data into your NETADAPTER context.  If you are porting an existing NDIS 6.x driver, you'll likely have a single MiniportAdapterContext that combines networking-related and device-related data into a single data structure.  To simplify the porting process, just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER's context be a small structure that points to the WDFDEVICE's context.

You'll provide 3 callbacks to [**NET_ADAPTER_CONFIG_INIT method**](net-adapter-config-init.md):

* [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md)
* [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md)
* [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md)

The first two are specific to the NetAdapter data path programming model.

The third is where the client calls the methods equivalent to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).  However, instead of calling one routine with a generic [**NDIS_MINIPORT_ADAPTER_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565920) structure, the client driver calls different functions to set different types of capabilities.  For example, your [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md) might call some or all of the following:

* [**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)
* [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)
* [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)
* [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

To set an attribute that does not have equivalent NetAdapter functionality, call [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) from [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md).

### Creating queues to manage control requests

Next, still in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), set up the object identifier (OID) path.  The OID path is modeled like a WDF queue.  But you'll be getting OIDs instead of WDFREQUESTs.

There are two high level approaches you might take when porting this.  The first option is to register a default handler that receives OID requests in a very similar way to how a miniport driver receives requests from NDIS.  This is the easiest port, since you'll likely just need to adjust a function signature from your old MiniportOidRequest handler.

The other option is to break apart your OID handler's switch statement and provide a separate handler for each individual OID.  You might choose this option if your device requires OID-specific functionality.

You might even use both approaches in the same driver, providing custom handlers for some OIDs while using a default handler with a switch statement for the remainder.

To register default handlers for all query OIDs and all set OIDs, provide an [**EVT_NET_REQUEST_DEFAULT_QUERY_DATA callback function**](evt-net-request-default-query-data.md) and an [**EVT_NET_REQUEST_DEFAULT_SET_DATA callback function**](evt-net-request-default-set-data.md):

```cpp
NET_REQUEST_QUEUE_CONFIG config;
NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL(&config, NetAdapter);
config.EvtRequestDefaultQueryData = MyQueryHandler;
config.EvtRequestDefaultSetData = MySetHandler;
```

To add an OID-specific handler, call the [**NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER**](net-request-queue-config-add-query-data-handler.md) method with a pointer to the client driver's implementation of an [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md) event callback function:

```cpp
NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER(
    &config, OID_GEN_VENDOR_DESCRIPTION,
    EvtQueryGenVendorDescription, sizeof(NIC_VENDOR_DESC));
```

Once you've set up the OID queue the way you like, call [**NetRequestQueueCreate method**](netrequestqueuecreate.md) to create the queue:

```cpp
status = NetRequestQueueCreate(&config, WDF_NO_OBJECT_ATTRIBUTES, NULL);

if(!NT_SUCCESS(status))
{
    return status;
}
```

### Accessing configuration parameters in the registry

Next, replace calls to [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) and related functions with the `NetConfiguration*` methods.  The `NetConfiguration*` methods are similar to the `Ndis*Configuration*` functions, and you won't need to restructure your code.

Start by calling [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) to get a handle to a configuration object.  You can then query it:

```cpp
NETCONFIGURATION config = NULL;

status = NetAdapterOpenConfiguration(NetAdapter, WDF_NO_OBJECT_ATTRIBUTES, &config);
if (!NT_SUCCESS(status)) {
    return status;
}

status = NetConfigurationQueryUlong(config, 0, &SomeValue, &myvalue);

NetConfigurationClose(configuration);
```

There are `NetConfiguration` functions for querying ULONG data, strings, multi-strings (similar to REG_MULTI_SZ), binary blobs, and MAC addresses.

### Receiving I/O control codes (IOTCLs) from user mode

Read this section if your NDIS driver calls [**NdisRegisterDeviceEx**](https://msdn.microsoft.com/library/windows/hardware/ff564518), a routine used to create a control device object (CDO) to receive IOCTLs from user mode.

Here are two ways to do this in your WDF networking client driver.

The most straightforward port is to create a control device object by calling [**WdfControlDeviceInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff545841) from the client's [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback.  For more info, see [Using Control Device Objects](../wdf/using-control-device-objects.md).

However, the recommended solution is to create a device interface by calling [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) with a reference string, as shown here:

```cpp
DECLARE_CONST_UNICODE_STRING(c_RefString, L"MyRefString");
status = WdfDeviceCreateDeviceInterface(
            device, 
            &GUID_MY_DEVICE_INTERFACE, 
            &c_RefString);
if (!NT_SUCCESS(status)) {
    return status;
}
```

For more info, see [Using Device Interfaces](../wdf/using-device-interfaces.md).

When a user-mode application sends requests to a handle opened on a device interface with a reference string, your client driver receives I/O requests.  You can use [WDF queue objects](../wdf/framework-queue-objects.md) to handle the incoming I/O requests.

### Finishing device initialization

At this point in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), you can do anything else you'd like to initialize your device, like allocating interrupts.

## Power management

A WDF client driver does not receive [**OID_PNP_SET_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff569780) for power state changes.

Instead, a WDF client registers optional callback functions to receive power state change notifications.  For an overview, see [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).

Typically, the code in your [**OID_PNP_SET_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff569780) handler moves to [*EVT_WDF_DEVICE_D0_EXIT*](https://msdn.microsoft.com/library/windows/hardware/ff540855) and [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848).

Because the WDF power state machine is slightly different, you might need to make minor modifications to the code.

Specifically, in its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) callback function, an NDIS miniport driver performs one-time initialization tasks as well as work to bring the device to the D0 state.  Then, it repeats the work to go to D0 in its [*OID_PNP_SET_POWER*](https://msdn.microsoft.com/library/windows/hardware/ff569780) handler.

In contrast, a WDF client performs one-time initialization tasks in event callbacks before [**EVT_WDF_DEVICE_D0_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff540848), during which the device is in a low-power state.  Then it does the work to go to D0 in [**EVT_WDF_DEVICE_D0_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff540848).

To summarize, in WDF, you put your "go to D0" code in one place, instead of two.

For details on the callback sequence, see [Power-Up Sequence for an Network Adapter WDF Client Driver](power-up-sequence-for-ndis-wdf-client-driver.md).

Similarly, a WDF client driver never receives [**OID_PM_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff569768).

Instead, the driver queries the necessary wake-on-LAN (WoL) configuration from the NETPOWERSETTINGS object.  To access this object, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md) from [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) and related callback functions.  For example:

```cpp
NTSTATUS
EvtDeviceArmWakeFromS0(WDFDEVICE Device)
{
    NETPOWERSETTINGS powerSettings = NetAdapterGetPowerSettings(Adapter->NetAdapter);

    ULONG EnabledWakePatterns = NetPowerSettingsGetEnabledWakePatterns(powerSettings);
    ULONG EnabledProtocolOffloads = NetPowerSettingsGetEnabledProtocolOffloads(powerSettings);
    ULONG WakeUpFlags = NetPowerSettingsGetEnabledWakeUpFlags(powerSettings);

    // ...
}
```

The actual flags you get back have the same semantics as they do for an NDIS 6 miniport, so you don't need to make deep changes to the logic.  The main difference is that you can now query these flags during the power-down sequence.  See [Power-Down Sequence for an Network Adapter WDF Client Driver](power-down-sequence-for-ndis-wdf-client-driver.md).

Once you've moved this code around, you can delete your OID handlers for [*OID_PNP_SET_POWER*](https://msdn.microsoft.com/library/windows/hardware/ff569780) and [*OID_PM_PARAMETERS*](https://msdn.microsoft.com/library/windows/hardware/ff569768).

Because the client is the [power policy owner](../wdf/power-policy-ownership.md) for the NIC's device stack, it can use WDF's built-in power management functionality.  For example, you might want to add your own idle logic. For info, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

Because the NetAdapter framework keeps your device at D0 while the host uses the network interface, the client typically does not implement power logic; the default NetAdapter power behavior is sufficient.

## Data path

The data path programming model has changed significantly. This section explains the minimum you'll need to install and remove your device.

The NetAdapter model introduces the following new structures for use with the data path:

|New data path structures|Description|
|-|-|
|[**NET_PACKET**](net-packet.md)|Similar to a NET_BUFFER|
|[**NET_PACKET_FRAGMENT**](net-packet-fragment.md)|Similar to a memory descriptor list (MDL). Each NET_PACKET has one or more of these.|
|[**NET_RING_BUFFER**](net-ring-buffer.md)|Ring buffer shared between the host and a client, a container for one or more NET_PACKET structures|

In the NetAdapter model, network traffic is no longer per adapter, as in NDIS, but rather per queue.  Each queue is associated with a ring buffer, which contains a group of packets and pointers to indicate where in the ring to read and write next.

When your client driver calls [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md), it provides two queue creation callbacks: [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md) and [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md).  The client creates transmit and receive queues in these callbacks.

The client creates a transmit queue by calling [**NetTxQueueCreate**](nettxqueuecreate.md) as follows:

```cpp
NTSTATUS
EvtAdapterCreateTxQueue(NETADAPTER Adapter, PNETTXQUEUE_INIT NetTxQueueInit)
{
    NETTXQUEUE txQueue;

    NET_TXQUEUE_CONFIG txQueueConfig;
    NET_TXQUEUE_CONFIG_INIT(&txQueueConfig, 
                            EvtTxQueueAdvance,
                            EvtTxQueueSetNotificationEnabled,
                            EvtTxQueueCancel);
    NTSTATUS status = NetTxQueueCreate(
        NetTxQueueInit,
        WDF_NO_OBJECT_ATTRIBUTES,
        &txQueueConfig,
        &txQueue);

    return status;
}
```

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md), use the same pattern to call [**NetRxQueueCreate**](netrxqueuecreate.md).

Because the NETRXQUEUE and NETTXQUEUE objects are parented to the NETADAPTER, WDF automatically deletes the queues when the adapter is deleted.  Also, the client does not need to handle start and pause semantics (unlike in NDIS 6.x where the miniport does need to handle them).

When creating transmit and receive queues, the client provides pointers to the following callbacks:

* [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md)
* [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md)
* [*EVT_TXQUEUE_CANCEL*](evt-txqueue-cancel.md)
* [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md)
* [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md)
* [*EVT_RXQUEUE_CANCEL*](evt-rxqueue-cancel.md)

### EVT_TXQUEUE_ADVANCE

The [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) callback is similar to [**MINIPORT_SEND_NET_BUFFER_LISTS**](https://msdn.microsoft.com/library/windows/hardware/ff559440) in NDIS 6.x.


### EVT_RXQUEUE_ADVANCE

In the new programming model there are no NET_BUFFER_LIST or NET_BUFFER pools.

### EVT_RXQUEUE_CANCEL

Consider a simple example in which we have not provided buffers to any hardware.  In this case, it's safe to immediately return all the buffers to the host in the cancellation handler.

The fastest way to do that is to adjust the [*NET_RING_BUFFER*](net-ring-buffer.md) pointers like this:

```cpp
VOID
EvtRxQueueCancel(NETRXQUEUE RxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);

    ringBuffer->BeginIndex = ringBuffer->NextIndex = ringBuffer->EndIndex;
}
```

## Device removal

Device removal for a WDF NIC driver is the same as in any other WDF device driver, with no networking specific processing required.  The network data path shuts down first, followed by the WDF device.  For info about WDF shutdown, see [A User Unplugs a Device](../wdf/a-user-unplugs-a-device.md).

Your *MiniportHaltEx* handler will likely be distributed between [*EVT_WDF_DEVICE_D0_EXIT*](https://msdn.microsoft.com/library/windows/hardware/ff540855) and [*EVT_WDF_DEVICE_RELEASE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540890).

The WDF client does not need to delete the NetAdapter or any of the OID and datapath queues that it created.  WDF deletes these objects automatically.

You can delete *MiniportShutdownEx*, *MiniportResetEx* and *MiniportCheckForHangEx*.  These callbacks are no longer supported.

## NDIS-WDF function equivalents

Most `NdisXxx` functions can be replaced with a WDF equivalent.  In general, you should find that you need very little functionality that is imported from `NDIS.SYS`.

The following table lists NDIS functions and their WDF equivalents:

|NDIS API Family|WDF Equivalent|
|-|-|
|[**NdisAllocateIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff561604)|[**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201)|
|[**NdisAllocateTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561618)|[**WdfTimerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550050)|
|[**NdisAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff560699)|[**WdfSpinLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff550040)|
|[**NdisInterlockedIncrement**](https://msdn.microsoft.com/library/windows/hardware/ff562752)|[**InterlockedIncrement**](https://msdn.microsoft.com/library/windows/hardware/ff547910)|
|[**NdisInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562732)|[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)|
|[**NdisMInitializeScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff553543)|[**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983)|
|[**NdisInitializeString**](https://msdn.microsoft.com/library/windows/hardware/ff562741)|[**WdfStringCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550046)|
|[**NdisSystemActiveProcessorCount**](https://msdn.microsoft.com/library/windows/hardware/ff564577)|[**KeGetCurrentProcessorNumberEx**](https://msdn.microsoft.com/library/windows/hardware/ff552076) (kernel)|
|[**NdisWriteRegisterUchar**](https://msdn.microsoft.com/library/windows/hardware/ff564678)|[**WDF_WRITE_REGISTER_UCHAR**](https://msdn.microsoft.com/library/windows/hardware/dn265684)|

For functions with no WDF equivalent, the client can call [**NetAdapterWdmGetNdisHandle**](netadapterwdmgetndishandle.md) to retrieve an NDIS_HANDLE for use with NDIS functions.  For example:

```Management
NdisGetRssProcessorInformation(NetAdapterWdmGetNdisHandle(NetAdapter), . . .);
```

## Debugging

You can use [Windows Driver Framework Extensions (Wdfkd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff551876) commands to debug your client driver.  In addition, you can provide a NETADAPTER handle to !ndiskd.netadapter to see networking-specific properties of your driver.  This extension shows similar results to what [**!ndiskd.miniport**](https://msdn.microsoft.com/library/windows/hardware/ff564142) shows for an NDIS 6 driver.

## Conclusion

Using the steps in this topic, you should have a working driver that starts and stops your device. To receive and transmit data, you need to understand how the ring buffer works, which is out of scope for this porting guide.

