# Porting NDIS Miniport Drivers to NetAdapter Class Extension

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

This page describes how to convert an NDIS 6.x miniport driver into a Windows Driver Framework (WDF) networking client miniport driver.

For general information about WDF, please review the [WDF Driver Development Guide](../wdf/index.md).

## Compilation Settings

First, ensure that your project links against the latest version of KMDF.  Also link against NetAdapterCxStub.lib (located in `Windows Kits\10\Lib\<latest_windows_version>\km\<architecture>\netadaptercx\1.0`).

It is no longer strictly necessary to link against `ndis.lib`, although you may still want to use some NDIS APIs, so you may still link against it.

It is no longer necessary to set NDIS preprocessor macros, like NDIS650_MINIPORT=1.

Add these headers to every source file (or to your common/precompiled header):

```ManagedCPlusPlus
#include <ntddk.h>
#include <wdf.h>
#include <netadaptercx.h>
```

Ensure that you have the [standard WDF decorations](../wdf/specifying-wdf-directives-in-inf-files.md) in your INF:

```Inf
[Yourdriver.Wdf]
KmdfService = Yourdriverservice, Yourdriver.wdfsect

[Yourdriver.wdfsect]
KmdfLibraryVersion = <insert here>
```

## Driver Initialization

Remove the call to [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) from [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff540807), and add the following:

```ManagedCPlusPlus
WDF_DRIVER_CONFIG_INIT(&config, EvtDriverDeviceAdd);
status = WdfDriverCreate(. . . );
if (!NT_SUCCESS(status)) {
    return status;
}
```

Do not specify the **WdfDriverInitNoDispatchOverride** flag in the call to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175). Remove this flag if you were using WDF in miniport mode in your NDIS 6.x driver.

*DriverUnload* is an optional routine for a WDF networking client driver, so you can remove it if you like.  If you keep it, remove the call to [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578).

## Device Initialization

Next, we need to break *MiniportInitializeEx* into several pieces, each of which is a standard WDF event.  The full sequence includes many events, several of which are optional.  See [Power-Up Sequence for a Function or Filter Driver](../wdf/power-up-sequence-for-a-function-or-filter-driver.md).

You should move code into the most logical place, based on the WDF semantics of each state.

In general, callbacks you'll need to provide are:

- [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693)
- [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880)
- [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848)

While you may need to handle several events to properly manage your device, the system requires only that the client driver do a few things in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693).

## Creating the NETADAPTER Object

In [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), your driver should do the following:

1. Call [**NetAdapterDeviceInitConfig**](netadapterdeviceinitconfig.md).
2. Load pointers to your driver's callbacks and call [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135), as shown here:

    ```ManagedCPlusPlus
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

4. Next you'll create the NETADAPTER object.  This object represents your NIC, which is the endpoint for all networking I/O.  To create it, the client typically calls [**NET_ADAPTER_CONFIG_INIT method**](net-adapter-config-init.md), followed by [**NetAdapterCreate method**](netadaptercreate.md):

    ```ManagedCPlusPlus
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attribs, MYDRIVER_ADAPTER_CONTEXT);

    NET_ADAPTER_CONFIG_INIT (
        &config,
        EvtAdapterSetCapabilities,
        EvtAdapterCreateTxQueue,
        EvtAdapterCreateRxQueue);

    status = NetAdapterCreate(device, &attribs, &config, &adapter);
    ```

Typically, you'll have one NETADAPTER per WDFDEVICE, with the WDFDEVICE being the parent object of the NETADAPTER.

Optionally, you can add context space to the object.   Since WDF allows you to set a context on any WDF object, you could add separate context space for the WDFDEVICE and the NETADAPTER objects.  In the example above, the client adds `MYDRIVER_ADAPTER_CONTEXT` to the NETADAPTER object.  For more info, see [Framework Object Context Space](../wdf/framework-object-context-space.md).

We recommend that you put device-related data in your WDFDEVICE's context, and networking-related data into your NETADAPTER context.  If you are porting an existing NDIS 6.x driver, you'll likely have a single MiniportAdapterContext that combines networking- and device-related data into a single data structure.  To simplify the porting process, you can just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER's context be a small structure that points to the WDFDEVICE's context.

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

To set an attribute that does not have equivalent NetAdapter functionality, call [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) from this callback.

## Initializing the Control Request Path

Next, while we're still in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), we're going to set up the object identifier (OID) path.  The OID path is modeled like a WDF queue.  Except instead of WDFREQUESTs, you'll be getting OIDs.

There are two high level approaches you might take when porting this.  The first option is to register a default handler that receives OID requests in a very similar way to how a miniport driver receives requests from NDIS.  This is the easiest port, since you'll likely just need to adjust a function signature from your old MiniportOidRequest handler.

The other option is to break apart your OID handler's switch statement and provide a separate handler for each individual OID.

You might even use both approaches in the same driver, providing custom handlers for some OIDs while using a default handler with a switch statement for the remainder.

To register default handlers for all query OIDs and all set OIDs, provide [**EVT_NET_REQUEST_DEFAULT_QUERY_DATA callback function**](evt-net-request-default-query-data.md) and [**EVT_NET_REQUEST_DEFAULT_SET_DATA callback function**](evt-net-request-default-set-data.md):

```ManagedCPlusPlus
NET_REQUEST_QUEUE_CONFIG config;
NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL(&config, NetAdapter);
config.EvtRequestDefaultQueryData = MyQueryHandler;
config.EvtRequestDefaultSetData = MySetHandler;
```

To add an OID-specific handler, call [**NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER method**](net-request-queue-config-add-query-data-handler.md) with a pointer to the client driver's implementation of a [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md) event callback function :

```ManagedCPlusPlus
NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER(
    &config, OID_GEN_VENDOR_DESCRIPTION,
    EvtQueryGenVendorDescription, sizeof(NIC_VENDOR_DESC));
```

Once you've set up the OID queue the way you like, call [**NetRequestQueueCreate method**](netrequestqueuecreate.md) to create the queue:

```ManagedCPlusPlus
status = NetRequestQueueCreate(&config, WDF_NO_OBJECT_ATTRIBUTES, NULL);

if(!NT_SUCCESS(status))
{
    return status;
}
```

## Querying Network Advanced Keywords

Next we'll replace [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/hh975122) and related calls with the `NetConfiguration*` methods.  The methods are similar, and you won't need to restructure your code.

Start by calling [**NetAdapterOpenConfiguration method**](netadapteropenconfiguration.md) to get a handle to a configuration object.  Then, you can query it:

```ManagedCPlusPlus
NETCONFIGURATION config = NULL;

status = NetAdapterOpenConfiguration(NetAdapter, WDF_NO_OBJECT_ATTRIBUTES, &config);
if (!NT_SUCCESS(status)) {
    return status;
}

status = NetConfigurationQueryUlong(config, 0, &SomeValue, &myvalue);

NetConfigurationClose(configuration);
```

There are configuration functions for querying ULONG data, strings, multi-strings (similar to REG_MULTI_SZ), binary blobs, and MAC addresses.

## Creating Device Interfaces

Read this section if your NDIS driver calls [**NdisRegisterDeviceEx**](https://msdn.microsoft.com/library/windows/hardware/ff564518).  An NDIS driver typically uses this routine to create a control device object (CDO) so that it can receive IOCTLs from user mode.

Here are two ways to do this in your WDF networking client driver.

The first option is to create a control device object by calling [**WdfControlDeviceInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff545841).

Alternatively, create a device interface by calling [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) with a reference string, as shown here:

```ManagedCPlusPlus
DECLARE_CONST_UNICODE_STRING(c_RefString, L"MyRefString");
status = WdfDeviceCreateDeviceInterface(
            device, 
            &GUID_MY_DEVICE_INTERFACE, 
            &c_RefString);
if (!NT_SUCCESS(status)) {
    return status;
}
```

When a component sends requests to a handle opened on this device interface, your device driver receives I/O requests.  You can use [WDF queue objects](../wdf/framework-queue-objects.md) to handle the incoming I/O requests.

## Finishing Device Initialization

At this point in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), you can do anything else you'd like to initialize your device, like allocate interrupts.

## Power Management

While your NDIS 6.x driver received [**OID_PNP_SET_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff569780) for power state changes, your WDF client never receives this OID.

Instead, a WDF client registers optional callback functions to receive power state change notifications.  For an overview, see [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).

Typically, the code in your [**OID_PNP_SET_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff569780) handler moves to [*EVT_WDF_DEVICE_D0_EXIT*](https://msdn.microsoft.com/library/windows/hardware/ff540855) and [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848).

Because the WDF power state machine is slightly different, you might need to make minor modifications to the code.

In particular, NDIS assumes that a device initializes in D0.
However, WDF assumes that a device initializes in D3, and supports an explicit [**EVT_WDF_DEVICE_D0_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function as part of device initialization. 

Similarly, a WDF client driver never receives OID_PM_PARAMETERS.

Instead, the driver queries the necessary WoL configuration from the NETPOWERSETTINGS object.  To access this object, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md) from [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) and related callback functions.  For example:

```ManagedCPlusPlus
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

The actual flags you get back have the same semantics as they do for an NDIS 6 miniport, so you don't need to make deep changes to the logic.  The main difference is that you can now query these flags during the power-down sequence.

Once you've moved this code around, you can delete your OID handlers for OID_PNP_SET_POWER and OID_PM_PARAMETERS.

Because the client is the [power policy owner](../wdf/power-policy-ownership.md) for the NIC's device stack, it can use WDF's built-in power management functionality.  For example, you might want to add your own idle logic. For info, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

Because the NetAdapter framework keeps your device at D0 while the host uses the network interface, the client typically does not implement power logic; the default NetAdapter power behavior is sufficient.

## Data Path

The data path programming model has changed significantly and requires a more in-depth explanation. This section explains the minimum you'll need to install and remove your device.

The NetAdapter model introduces the following new structures for use with the data path:

|New data path structures|Description|
|-|-|
|[**NET_PACKET**](net-packet.md)|Similar to a NET_BUFFER|
|[**NET_PACKET_FRAGMENT**](net-packet-fragment.md)|Similar to a memory descriptor list (MDL). Each NET_PACKET has one or more of these.|
|[**NET_RING_BUFFER**](net-ring-buffer.md)|Ring buffer shared between the host and a client, a container for one or more NET_PACKET structures|

In the NetAdapter model, network traffic is no longer per adapter, as in NDIS, but rather per queue.  Each queue is associated with a ring buffer, which contains a group of packets and pointers to indicate where in the ring to read and write next.

When your client driver calls [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md), it provides two queue creation callbacks: [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md) and [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md).  In these callbacks, the client creates transmit and receive queues.

The client creates a transmit queue as follows:

```ManagedCPlusPlus
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

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md), use the same pattern.

Because the NETRXQUEUE and NETTXQUEUE objects are parented to the NETADAPTER, WDF automatically deletes the queues when the adapter is deleted.  Also, unlike in NDIS 6.x, the client does not need to handle start and pause semantics.

When creating transmit and receive queues, the client provides pointers to the following callbacks:

### EVT_TXQUEUE_ADVANCE

The [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) callback is similar to [**MINIPORT_SEND_NET_BUFFER_LISTS**](https://msdn.microsoft.com/library/windows/hardware/ff559440) in NDIS 6.x.

In a production driver, the client would call ring buffer macros to retrieve packets from the queue, send the data, and then complete the packets. The following example simply completes incoming transmit packets:

```ManagedCPlusPlus
VOID
EvtTxQueueAdvance(NETTXQUEUE TxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetTxQueueGetRingBuffer(TxQueue);
    NET_PACKET *netPacket;

    while ((netPacket = NetRingBufferGetNextPacket(ringBuffer)) != nullptr)
    {
        netPacket->Data.Completed = TRUE;

        NetRingBufferAdvanceNextPacket(ringBuffer);
    }

    NetRingBufferReturnCompletedPackets(ringBuffer);
}
```

### EVT_TXQUEUE_SET_NOTIFICATION_ENABLED

For info, see [**EVT_TXQUEUE_SET_NOTIFICATION_ENABLED**](evt-txqueue-set-notification-enabled.md).

### EVT_TXQUEUE_CANCEL

In its [**EVT_TXQUEUE_CANCEL**](evt-txqueue-cancel.md) callback function, the client driver should complete the buffers as soon as possible, regardless of whether pending transmit packets have been successfully transmitted.

You can safely ignore this handler for now.

### EVT_RXQUEUE_ADVANCE

In the new programming model there are no NET_BUFFER_LIST or NET_BUFFER pools.

For more info and an example, see [**EVT_RXQUEUE_ADVANCE callback function**](evt-rxqueue-advance.md).

### EVT_RXQUEUE_SET_NOTIFICATION_ENABLED

The purpose of the [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md) callback is the same of [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md).

### EVT_RXQUEUE_CANCEL

The [*EVT_RXQUEUE_CANCEL*](evt-rxqueue-cancel.md) callback is similar to [*EVT_TXQUEUE_CANCEL*](evt-txqueue-cancel.md), a suggestion from the host that the client driver should return all the buffers as soon as possible. 
In this example we're didn't give the buffers to any hardware, so it's safe to immediately return all the buffers to the host in the cancellation handler.
The fastest way to do that is to adjust the [*NET_RING_BUFFER*](net-ring-buffer.md) pointers like this:

```ManagedCPlusPlus
VOID
EvtRxQueueCancel(NETRXQUEUE RxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);

    ringBuffer->BeginIndex = ringBuffer->NextIndex = ringBuffer->EndIndex;
}
```

### Conclusion

At this point, you should have a working driver that starts and stops your device. To receive and transmit data, you need to understand how the ring buffer works, which is out of scope for this porting guide.

## Stopping the Device

Device removal for a WDF NIC driver is the same as in any other WDF device driver, with no networking specific processing required.  The network data path shuts down first, followed by the WDF device.  For info on WDF shutdown, see [A User Unplugs a Device](../wdf/a-user-unplugs-a-device.md).

Your *MiniportHaltEx* handler will likely be distributed between [*EVT_WDF_DEVICE_D0_EXIT*](https://msdn.microsoft.com/library/windows/hardware/ff540855) and [*EVT_WDF_DEVICE_RELEASE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540890).

The WDF client does not need to delete the NetAdapter or any of the OID and datapath queues that it created.  WDF deletes these objects automatically.

You can delete MiniportShutdownEx, MiniportResetEx and MiniportCheckForHangEx.  These callbacks are no longer supported.

## General Purpose Functions

Most `NdisXxx` functions can be replaced with a WDF equivalent.  This table lists a few examples:

Generally, you should find that you need very little functionality that is imported from `NDIS.SYS`.

|NDIS API Family|WDF Equivalent|
|-|-|
|NdisAllocateIoWorkItem|[**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201)|
|NdisAllocateTimerObject|[**WdfTimerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550050)|
|NdisAcquireSpinLock|[**WdfSpinLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff550040)|
|NdisInterlockedIncrement|InterlockedIncrement (compiler intrinsic)|
|NdisInitialzeEvent|[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)|
|NdisMInitializeScatterGatherDma|[**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983)|
|NdisInitializeString|[**WdfStringCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550046)|
|NdisSystemActiveProcessorCount|[**KeGetCurrentProcessorNumberEx**](https://msdn.microsoft.com/library/windows/hardware/ff552076) (kernel)|
|NdisWriteRegisterUchar|[**WDF_WRITE_REGISTER_UCHAR**](https://msdn.microsoft.com/library/windows/hardware/dn265684)|

In cases with no WDF equivalent, you can call [**NetAdapterWdmGetNdisHandle**](netadapterwdmgetndishandle.md) to retrieve an NDIS_HANDLE that works in many NDIS APIs as if it were a handle for an NDIS 6 miniport adapter.  For example:

```Management
NdisGetRssProcessorInformation(NetAdapterWdmGetNdisHandle(NetAdapter), . . .);
```

Debugging
---------

Since your driver is now a full-featured WDF driver, you can use !wdfkd commands to debug it.  In addition, the latest version of !ndiskd.netadapter can display networking-specifc properties of your driver, and shows similar results to what [**!ndiskd.miniport**](https://msdn.microsoft.com/library/windows/hardware/ff564142) shows for an NDIS 6 driver.  Also, !ndiskd.netadapter accepts a WDF-style NETADAPTER handle.
