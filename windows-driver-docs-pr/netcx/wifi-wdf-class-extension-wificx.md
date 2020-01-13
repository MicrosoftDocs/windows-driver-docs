
# Wi-Fi WDF class extension (WiFiCx)

## Introduction

This drop includes a Wi-Fi WDF class extension (WifiCx) that works with NetAdapterCx. This enables Wi-Fi network drivers to be fully fledged WDF client drivers. In addition, they are also NetAdapterCx client drivers just like other NIC drivers and also client drivers of Wifi class extension that provides Wi-Fi media-specific functionality. The following block diagram illustrates the WifiCx architecture:

![WiFiCx architecture](images/wificx.png)

A Wifi-NetAdapter client driver performs 3 categories of tasks based on its relationships with the framework:

- Call [standard WDF APIs](https://docs.microsoft.com/windows-hardware/drivers/ddi/_wdf/) for common device tasks like Pnp and Power management.
- Call [NetAdapterCx APIs](https://docs.microsoft.com/windows-hardware/drivers/ddi/_netvista/#netadaptercx) for common network device operations like transmitting or receiving network packets.
- Call [WiFiCx APIs] for for Wi-Fi-specific control path operations like WDI command handling.

## Device Initialization

In addition to those tasks required by NetAdapterCx for [NetAdapter device initialization](device-and-adapter-initialization.md), a WifiCx client driver must also perform the following tasks in its [EvtDriverDeviceAdd](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) callback function:
1.	Call  WifiDeviceInitConfig after calling NetDeviceInitConfig but before calling [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate), referencing the same [WDFDEVICE_INIT](https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/wdfdevice_init) object passed in by the framework.

2.	Call WifiDeviceInitialize to register WifCx device-specific callback functions using an initialized WIFI_DEVICE_CONFIG structure and the WDFDEVICE object obtained from WdfDeviceCreate.
The following example demonstrates how to initialize the WifiCx device. Error handling has been left out for clarity.

```C++
status = NetDeviceInitConfig(deviceInit);
status = WifiDeviceInitConfig(deviceInit);

// Set up other callbacks such as Pnp and Power policy

status = WdfDeviceCreate(&deviceInit, &deviceAttributes, &wdfDevice);
WIFI_DEVICE_CONFIG wifiDeviceConfig;
WIFI_DEVICE_CONFIG_INIT(&wifiDeviceConfig,
                        WDI_VERSION_LATEST,
                        EvtWifiDeviceSendCommand,
                        EvtWifiDeviceCreateAdapter,
                        EvtWifiDeviceCreateWifiDirectDevice,       //2001 (Drop 2) New Added Callback
                        EvtWifiDeviceCreateWifiDirectRoleAdapter); //2001 (Drop 2) New Added Callback

status = WifiDeviceInitialize(wdfDevice, &wifiDeviceConfig);
```

This message flow diagram illustrates the initialization process.

![WiFiCx client driver initialization process](images/wificx_initialization.png)

### **Default (station) adapter creation flow**

Next, the client driver must set all the WiFi specific device capabilities, typically in the [EvtDevicePrepareHardware](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function that follows. Note that WifiCx/WDI will no longer be querying for these capabilities via WDI_GET_ADAPTER_CAPABILITIES command. Also, unlike other types of NetAdapterCx drivers, WiFi client drivers must not create the NETADAPTER object from within the EvtDriverDeviceAdd callback function. Instead, it will be instructed by WifiCx to create the default NetAdapter (station) later using the EvtWifiCxDeviceCreateAdapter callback (after the client’s PrepareHardware WDF callback is successful). Note that WifiCx/WDI will no longer call WDI_TASK_CREATE_PORT command.

In this call, the client driver needs to call into NetAdapterCx to create the new NetAdapter object and then call into WifiCx (using WifiCxAdapterInitialize API) to initialize the WiFiCx context and associate it with this NetAdapter object.

If this succeeds, WifiCx will then go on to send initialization commands for the device/adapter (TASK_OPEN, SET_ADAPTER_CONFIGURATION, TASK_SET_RADIO_STATE if necessary etc).

![WiFiCx client driver station adapter creation](images/wificx_station.png)

## WDI Command flow via WifiCx APIs

WifiCx uses WDI commands for most control path operations as defined in the WDI spec. The commands are exchanged through a set of callback functions provided by the client driver and APIs provided by WifiCx. The following function calls are used by WifiCx to replicate WDI command handling:
- WifiCx sends a WDI command message to the client driver by invoking its EvtWifiDeviceSendCommand callback function. The client driver sends the M3 for the command asynchronously by calling WifiRequestComplete. The client driver calls API WifiRequestGetInOutBuffer to retrieve the input/output buffer and buffer lengths and WifiRequestGetMessageId to retrieve the WDI message ID of the command.
If this was a set command and the original request did not conatin a large enough buffer, the client should call WifiRequestSetBytesNeeded to set the needed buffer size and then fail the request with status BUFFER_OVERFLOW.

- If this is a task command, the client driver needs to later send the associated M4 indication by calling WifiDeviceReceiveIndication and pass the indication buffer with a WDI header that contains the same transaction ID as in the M1.

- Unsolicited indications are also notified via the WifiDeviceReceiveIndication API but with transaction ID set to 0.

![WiFiCx client driver command](images/wificx_command.png)
## Wi-Fi Direct (P2P) Support

Since 2001 (Drop 2) the Wi-Fi Direct Miracast scenario will be supported. To enable Miracast, the client driver must implement the following sections.
### Wi-Fi Direct Device Capabilities

WIFI_WIFIDIRECT_CAPABILITIES is an new introduced structure merged from the WDI_P2P_CAPABILITIES and WDI_AP_CAPABILITIES. The client driver need to call WifiDeviceSetWiFiDirectCapabilities API for updating WifiCx in the set device capabilities phase.
```C++
WIFI_WIFIDIRECT_CAPABILITIES wfdCapabilities = {};

// Set values
wfdCapabilities.ConcurrentGOCount = 1;
wfdCapabilities.ConcurrentClientCount = 1;

// Update back to WifiCx
WifiDeviceSetWiFiDirectCapabilities(Device, &wfdCapabilities);
```
### Wi-Fi Direct Event Callback For "WfdDevice"

For Wi-Fi Direct, the "WfdDevice" is a control concept with no data path support, therefore WifiCx has a new WDFObject named WIFIDIRECTDEVICE. WifiDirectDeviceGetPortId and WifiDirectDeviceSetCurrentLinkLayerAddress APIs created for this WIFIDIRECTDEVICE handle. 
```C++
NTSTATUS
EvtWifiDeviceCreateWifiDirectDevice(
    WDFDEVICE  Device,
    WIFIDIRECT_DEVICE_INIT * WfdDeviceInit
)
{
    WDF_OBJECT_ATTRIBUTES wfdDeviceAttributes;
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&wfdDeviceAttributes, WIFI_WFDDEVICE_CONTEXT);
    wfdDeviceAttributes.EvtCleanupCallback = EvtWifiDirectDeviceContextCleanup;

    WIFIDIRECTDEVICE wfdDevice;
    NTSTATUS ntStatus = WifiDirectDeviceCreate(WfdDeviceInit, &wfdDeviceAttributes, &wfdDevice);
    if (!NT_SUCCESS(ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_DEVICE, "%!FUNC!: WifiDirectDeviceCreate failed, status=0x%x\n", ntStatus);
        return ntStatus;
    }

    ntStatus = WifiDirectDeviceInitialize(wfdDevice);

    if (!NT_SUCCESS(ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_DEVICE, "%!FUNC!: WifiDirectDeviceInitialize failed with %!STATUS!\n", ntStatus);
        return ntStatus;
    }

    ntStatus = ClientDriverInitWifiDirectDeviceContext(
        Device,
        wfdDevice,
        WifiDirectDeviceGetPortId(wfdDevice));
    if (!NT_SUCCESS(ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_DEVICE, "%!FUNC!: ClientDriverInitWifiDirectDeviceContext failed with %!STATUS!\n", ntStatus);
        return ntStatus;
    }

    ntStatus = WifiDirectDeviceStart(wfdDevice); //!! This API will be removed in the DROP 3 !!
    if (!NT_SUCCESS(ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_DEVICE, "%!FUNC!: WifiDirectDeviceStart failed with %!STATUS!", ntStatus);
        return ntStatus;
    }

    return ntStatus;
}
```
### Wi-Fi Direct Event Callback For "WfdRole"

WfdRole is a data path support adapter, which is similar to the default (station) adapter creation flow. (Note this will be merged with the station adapter creation in a future drop).
```C++
NTSTATUS
EvtWifiDeviceCreateWifiDirectRoleAdapter(
    WDFDEVICE Device,
    NETADAPTER_INIT* AdapterInit
)
{
    NET_ADAPTER_DATAPATH_CALLBACKS datapathCallbacks;
    NET_ADAPTER_DATAPATH_CALLBACKS_INIT(&datapathCallbacks,
        EvtAdapterCreateTxQueue,
        EvtAdapterCreateRxQueue);

    NetAdapterInitSetDatapathCallbacks(AdapterInit, &datapathCallbacks);

    WDF_OBJECT_ATTRIBUTES adapterAttributes;
    WDF_OBJECT_ATTRIBUTES_INIT(&adapterAttributes);
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&adapterAttributes, WIFI_NETADAPTER_CONTEXT);
    adapterAttributes.EvtCleanupCallback = EvtAdapterContextCleanup;

    NETADAPTER netAdapter;
    NTSTATUS ntStatus = NetAdapterCreate(AdapterInit, &adapterAttributes, &netAdapter);
    if (!NT_SUCCESS(ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_DEVICE, "%!FUNC!: NetAdapterCreate failed, status=0x%x\n", ntStatus);
        return ntStatus;
    }

    ntStatus = WifiDirectRoleAdapterInitialize(netAdapter);

    if (!NT_SUCCESS(ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_DEVICE, "%!FUNC!: WifiDirectRoleAdapterInitialize failed with %!STATUS!\n", ntStatus);
        return ntStatus;
    }

    ntStatus = ClientDriverInitDataAdapterContext(
        Device,
        netAdapter,
        EXT_P2P_ROLE_PORT,
        WifiDirectRoleAdapterGetPortId(netAdapter));

    if (!NT_SUCCESS(ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_DEVICE, "%!FUNC!: ClientDriverInitDataAdapterContext failed with %!STATUS!\n", ntStatus);
        return ntStatus;
    }

    ntStatus = ClientDriverNetAdapterStart(netAdapter);
    if (!NT_SUCCESS(ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_DEVICE, "%!FUNC!: ClientDriverNetAdapterStart failed with %!STATUS!\n", ntStatus);
        return ntStatus;
    }

    return ntStatus;
}
```
### Wi-Fi Direct ExemptionAction support in TxQueue

ExemptionAction added as a NetAdapter packet extension in version 2.1, so please make sure bump the version and set Preview to true in the solution.
```C++
#include <net/wifi/exemptionaction.h>

typedef struct _WIFI_TXQUEUE_CONTEXT
{
    WIFI_NETADAPTER_CONTEXT* NetAdapterContext;
    LONG NotificationEnabled;
    NET_RING_COLLECTION const* Rings;
    NET_EXTENSION VaExtension;
    NET_EXTENSION LaExtension;
    NET_EXTENSION ExemptionActionExtension;
    CLIENTDRIVER_TCB* PacketContext;
} WIFI_TXQUEUE_CONTEXT, * PWIFI_TXQUEUE_CONTEXT;
WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(WIFI_TXQUEUE_CONTEXT, WifiGetTxQueueContext);

NTSTATUS
EvtAdapterCreateTxQueue(
    _In_ NETADAPTER NetAdapter,
    _Inout_ NETTXQUEUE_INIT* TxQueueInit
)
{
    TraceEvents(TRACE_LEVEL_VERBOSE, DBG_INIT, "-->%!FUNC!\n");

    NTSTATUS status = STATUS_SUCCESS;
    PWIFI_TXQUEUE_CONTEXT txQueueContext = NULL;
    PWIFI_NETADAPTER_CONTEXT netAdapterContext = WifiGetNetAdapterContext(NetAdapter);
    WDF_OBJECT_ATTRIBUTES txAttributes;

    WDF_OBJECT_ATTRIBUTES_INIT(&txAttributes);
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&txAttributes, WIFI_TXQUEUE_CONTEXT);

    txAttributes.EvtDestroyCallback = EvtTxQueueDestroy;

    NET_PACKET_QUEUE_CONFIG queueConfig;
    NET_PACKET_QUEUE_CONFIG_INIT(&queueConfig,
        EvtTxQueueAdvance,
        EvtTxQueueSetNotificationEnabled,
        EvtTxQueueCancel);
    queueConfig.EvtStart = EvtTxQueueStart;
    NETPACKETQUEUE txQueue;
    status =
        NetTxQueueCreate(TxQueueInit,
            &txAttributes,
            &queueConfig,
            &txQueue);

    if (!NT_SUCCESS(status))
    {
        TraceEvents(TRACE_LEVEL_ERROR, DBG_INIT, "NetTxQueueCreate failed, Adapter=0x%p status=0x%x\n", NetAdapter, status);
        goto Exit;
    }

    txQueueContext = WifiGetTxQueueContext(txQueue);

    TraceEvents(TRACE_LEVEL_INFORMATION, DBG_INIT, "NetTxQueueCreate succeeded, Adapter=0x%p, TxQueue=0x%p\n", NetAdapter, txQueue);

    txQueueContext->NetAdapterContext = netAdapterContext;
    txQueueContext->Rings = NetTxQueueGetRingCollection(txQueue);
    netAdapterContext->TxQueue = txQueue;

    NET_EXTENSION_QUERY extensionQuery;
    NET_EXTENSION_QUERY_INIT(
        &extensionQuery,
        NET_FRAGMENT_EXTENSION_VIRTUAL_ADDRESS_NAME,
        NET_FRAGMENT_EXTENSION_VIRTUAL_ADDRESS_VERSION_1,
        NetExtensionTypeFragment);

    NetTxQueueGetExtension(
        txQueue,
        &extensionQuery,
        &txQueueContext->VaExtension);

    if (!txQueueContext->VaExtension.Enabled)
    {
        TraceEvents(
            TRACE_LEVEL_ERROR,
            DBG_INIT,
            "%!FUNC!: Required virtual address extension is missing.");

        status = STATUS_UNSUCCESSFUL;
        goto Exit;
    }

    NET_EXTENSION_QUERY_INIT(
        &extensionQuery,
        NET_FRAGMENT_EXTENSION_LOGICAL_ADDRESS_NAME,
        NET_FRAGMENT_EXTENSION_LOGICAL_ADDRESS_VERSION_1,
        NetExtensionTypeFragment);

    NetTxQueueGetExtension(
        txQueue,
        &extensionQuery,
        &txQueueContext->LaExtension);

    if (!txQueueContext->LaExtension.Enabled)
    {
        TraceEvents(
            TRACE_LEVEL_ERROR,
            DBG_INIT,
            "%!FUNC!: Required logical address extension is missing.");

        status = STATUS_UNSUCCESSFUL;
        goto Exit;
    }

     NET_EXTENSION_QUERY_INIT(
        &extensionQuery,
        NET_PACKET_EXTENSION_WIFI_EXEMPTION_ACTION_NAME,
        NET_PACKET_EXTENSION_WIFI_EXEMPTION_ACTION_VERSION_1,
        NetExtensionTypePacket);

    NetTxQueueGetExtension(
        txQueue,
        &extensionQuery,
        &txQueueContext->ExemptionActionExtension);

    if (!txQueueContext->ExemptionActionExtension.Enabled)
    {
        TraceEvents(
            TRACE_LEVEL_ERROR,
            DBG_INIT,
            "%!FUNC!: Required Exemption Action extension is missing.");

        status = STATUS_UNSUCCESSFUL;
        goto Exit;
    }

    status = InitializeTCBs(txQueue, txQueueContext);

    if (status != STATUS_SUCCESS)
    {
        goto Exit;
    }

Exit:
    TraceEvents(TRACE_LEVEL_VERBOSE, DBG_INIT, "<--%!FUNC! with 0x%x\n", status);

    return status;
}

static
void
BuildTcbForPacket(
    _In_ WIFI_TXQUEUE_CONTEXT const * TxQueueContext,
    _Inout_ CLIENTDRIVER_TCB * Tcb,
    _In_ UINT32 PacketIndex,
    _In_ NET_RING_COLLECTION const * Rings
)
{
    auto const pr = NetRingCollectionGetPacketRing(Rings);
    auto const fr = NetRingCollectionGetFragmentRing(Rings);

    auto const packet = NetRingGetPacketAtIndex(pr, PacketIndex);

    auto const & vaExtension = TxQueueContext->VaExtension;
    auto const & laExtension = TxQueueContext->LaExtension;
    auto const & exemptionActionExtension = TxQueueContext->ExemptionActionExtension;



    auto const packageExemptionAction = WifiExtensionGetExemptionAction(&exemptionActionExtension, PacketIndex);
    Tcb->EncInfo.ExemptionActionType = packageExemptionAction->ExemptionAction;

}

```
### Wi-Fi Direct INI/INF file change

vWifi functionalities has been replaced by the NetAdapter, if porting from WDI based driver, the INI/INF should remove the vWIFI related information. 
```INF
Characteristics = 0x84
BusType         = 5
*IfType         = 71; IF_TYPE_IEEE80211
*MediaType      = 16; NdisMediumNative802_11
*PhysicalMediaType = 9; NdisPhysicalMediumNative802_11
NumberOfNetworkInterfaces   = 5; For WIFI DIRECT DEVICE AND ROLE ADAPTER

; TODO: Set this to 0 if your device is not a physical device.
*IfConnectorPresent     = 1     ; true

; In most cases, you can keep these at their default values.
*ConnectionType         = 1     ; NET_IF_CONNECTION_DEDICATED
*DirectionType          = 0     ; NET_IF_DIRECTION_SENDRECEIVE
*AccessType             = 2     ; NET_IF_ACCESS_BROADCAST
*HardwareLoopback       = 0     ; false

[ndi.NT.Wdf]
KmdfService = %ServiceName%, wdf

[wdf]
KmdfLibraryVersion      = $KMDFVERSION$

```
## Appendix

2001 (Drop 2):

**What’s new**:
-	Wi-Fi Direct related commands implemented. Tested with Miracast and P2PApplication.
-	Packet extension implemented. Encryption exclusion to support secure networks.

**Limitations**:
-	Direct OID commands not yet forwarded by NetAdapter to WifiCx (will be available in next drop).
-	API for IHV to query OS WDI version not implemented yet (please use WDI_VERSION_LATEST for now).
-	Wi-Fi requests are targeted towards device (in the future, this may be sent on the adapter object).
-	Reset recovery (PLDR) and aborting of commands not yet implemented.
-	Power related commands not yet implemented.
-	No support for FIPS.

1911 (Drop 1):

**What’s new**:
-	WifiCx Client APIs to initialize device, set capabilities, create default adapter and process WDI commands implemented.
-	Basic STA functionality including scan, connect, radio toggle etc supported.

**Limitations**:
-	Data path support (for STA) is limited and implemented using existing NetAdapterCx APIs. Packet extension for encryption exclusion policy etc is not implemented yet, therefore connection to only open networks has been tested.
-	Direct OID commands not yet forwarded by NetAdapter to WifiCx (will be available in next drop).
-	API for IHV to query OS WDI version not implemented yet (please use WDI_VERSION_LATEST for now).
-	Wi-Fi requests are targeted towards device (in the future, this may be sent on the adapter object).
-	Reset recovery (PLDR) and aborting of commands not yet implemented.
-	Wi-Fi Direct/power related commands not yet implemented.
-	No support for FIPS.
