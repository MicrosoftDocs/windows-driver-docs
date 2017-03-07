---
title: Network Adapter WDF Class Extension (Cx) Reference
---

# Network Adapter WDF Class Extension (Cx) Reference


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Starting in Windows 10, version 1703, the Windows Driver Kit (WDK) includes a class extension module (NetAdapterCx) that enables you to write a KMDF-based driver (called the client driver in this section) for a network adapter.
In previous versions of Windows, you needed to write an NDIS miniport driver.

## Event callback functions


These event callback functions that are defined by NetAdapterCx and implemented by your client driver. NetAdapterCx invokes these functions to notify the client driver about events.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<em>EVT_NET_ADAPTER_CREATE_RXQUEUE</em>](evt-net-adapter-create-rxqueue.md)</p></td>
<td align="left"><p>The client driver's implementation of the [<em>EVT_NET_ADAPTER_CREATE_RXQUEUE</em>](evt-net-adapter-create-rxqueue.md) event callback function that sets up a receive queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_NET_ADAPTER_CREATE_TXQUEUE</em>](evt-net-adapter-create-txqueue.md)</p></td>
<td align="left"><p>The client driver's implementation of the [<em>EVT_NET_ADAPTER_CREATE_TXQUEUE</em>](evt-net-adapter-create-txqueue.md) event callback function that sets up a transmit queue.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD</em>](evt-net-adapter-preview-protocol-offload.md)</p></td>
<td align="left"><p>The client driver's implementation of the [<em>EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD</em>](evt-net-adapter-preview-protocol-offload.md) event callback function that accepts or rejects an incoming protocol offload.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN</em>](evt-net-adapter-preview-wake-pattern.md)</p></td>
<td align="left"><p>The client driver's implementation of the [<em>EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN</em>](evt-net-adapter-preview-wake-pattern.md) event callback function that accepts or rejects an incoming wake-on-LAN (WOL) pattern.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EVT_NET_ADAPTER_SET_CAPABILITIES</em>](evt-net-adapter-set-capabilities.md)</p></td>
<td align="left"><p>The client driver's implementation of the [<em>EVT_NET_ADAPTER_SET_CAPABILITIES</em>](evt-net-adapter-set-capabilities.md) event callback function that sets the capabilities of the network adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_NET_REQUEST_DEFAULT</em>](evt-net-request-default.md)</p></td>
<td align="left"><p>The client driver's implementation of the [<em>EVT_NET_REQUEST_DEFAULT</em>](evt-net-request-default.md) event callback function to handle an object identifier (OID) request to query or set information in the driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EVT_NET_REQUEST_DEFAULT_METHOD</em>](evt-net-request-default-method.md)</p></td>
<td align="left"><p>Implemented by the client driver to ... handler for method OIDs</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_NET_REQUEST_DEFAULT_QUERY_DATA</em>](evt-net-request-default-query-data.md)</p></td>
<td align="left"><p>Implemented by the client driver to ... handler for query OIDs</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EVT_NET_REQUEST_DEFAULT_SET_DATA</em>](evt-net-request-default-set-data.md)</p></td>
<td align="left"><p>Implemented by the client driver to ... handler for set OIDs</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_NET_REQUEST_METHOD</em>](evt-net-request-method.md)</p></td>
<td align="left"><p>Implemented by the client driver to ... custom method handler callback</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EVT_NET_REQUEST_QUERY_DATA</em>](evt-net-request-query-data.md)</p></td>
<td align="left"><p>Implemented by the client driver to ... custom query handler callback</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_NET_REQUEST_SET_DATA</em>](evt-net-request-set-data.md)</p></td>
<td align="left"><p>Implemented by the client driver to ... set handler callback</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EVT_RXQUEUE_ADVANCE</em>](evt-rxqueue-advance.md)</p></td>
<td align="left"><p>Implemented by the client driver to process receive packets provided by NetAdapterCx.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_RXQUEUE_CANCEL</em>](evt-rxqueue-cancel.md)</p></td>
<td align="left"><p>Implemented by the client driver to handle operations that must be performed before a receive queue is deleted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EVT_RXQUEUE_SET_NOTIFICATION_ENABLED</em>](evt-rxqueue-set-notification-enabled.md)</p></td>
<td align="left"><p>Implemented by the client driver to perform client-specific processing when there are new packets received in the specified queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_TXQUEUE_ADVANCE</em>](evt-txqueue-advance.md)</p></td>
<td align="left"><p>Implemented by the client driver to process transmit packets provided by NetAdapterCx.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EVT_TXQUEUE_CANCEL</em>](evt-txqueue-cancel.md)</p></td>
<td align="left"><p>Implemented by the client driver to handle operations that must be performed before a transmit queue is deleted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EVT_TXQUEUE_SET_NOTIFICATION_ENABLED</em>](evt-txqueue-set-notification-enabled.md)</p></td>
<td align="left"><p>Implemented by the client driver to perform client-specific processing when there are new packets received in the specified queue's ring buffer.</p></td>
</tr>
</tbody>
</table>

 

## Client driver support methods


These driver support methods that are implemented by NetAdapterCx. Your client driver calls these methods to communicate with NetAdapterCx.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Method</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_CONFIG_INIT method</strong>](net-adapter-config-init.md)</p></td>
<td align="left"><p>Initializes the [NET_ADAPTER_CONFIG](net-adapter-config.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_DATAPATH_CAPABILITIES_INIT method</strong>](net-adapter-datapath-capabilities-init.md)</p></td>
<td align="left"><p>Initializes the [<strong>NET_ADAPTER_DATAPATH_CAPABILITIES</strong>](net-adapter-datapath-capabilities.md) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_LINK_STATE_INIT method</strong>](net-adapter-link-state-init.md)</p></td>
<td align="left"><p>Initializes a [NET_ADAPTER_LINK_STATE](net-adapter-link-state.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED method</strong>](net-adapter-link-state-init-disconnected.md)</p></td>
<td align="left"><p>Initializes a [<strong>NET_ADAPTER_LINK_STATE</strong>](net-adapter-link-state.md) structure for an adapter that is disconnected from the network.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_PHYSICAL_ADDRESS_INIT method</strong>](net-adapter-physical-address-init.md)</p></td>
<td align="left"><p>Initializes the [<strong>NET_ADAPTER_PHYSICAL_ADDRESS</strong>](net-adapter-physical-address.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_POWER_CAPABILITIES_INIT method</strong>](net-adapter-power-capabilities-init.md)</p></td>
<td align="left"><p>Initializes the [<strong>NET_ADAPTER_POWER_CAPABILITIES</strong>](net-adapter-power-capabilities.md) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER method</strong>](net-request-queue-config-add-initialized-method-handler.md)</p></td>
<td align="left"><p>Adds a caller-provided custom request handler to a [<strong>NET_REQUEST_QUEUE_CONFIG</strong>](net-request-queue-config.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_QUERY_DATA_HANDLER method</strong>](net-request-queue-config-add-initialized-query-data-handler.md)</p></td>
<td align="left"><p>Adds a caller-provided query data handler to a [<strong>NET_REQUEST_QUEUE_CONFIG</strong>](net-request-queue-config.md) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_SET_DATA_HANDLER method</strong>](net-request-queue-config-add-initialized-set-data-handler.md)</p></td>
<td align="left"><p>Adds a caller-provided custom request handler to a [<strong>NET_REQUEST_QUEUE_CONFIG</strong>](net-request-queue-config.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_CONFIG_INIT method</strong>](net-request-queue-config-init.md)</p></td>
<td align="left"><p>Initializes the caller-allocated [NET_REQUEST_QUEUE_CONFIG](net-request-queue-config.md) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_PARALLEL method</strong>](net-request-queue-config-init-default-parallel.md)</p></td>
<td align="left"><p>Initializes the caller-allocated [<strong>NET_REQUEST_QUEUE_CONFIG</strong>](net-request-queue-config.md) structure to create a direct default request queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL method</strong>](net-request-queue-config-init-default-sequential.md)</p></td>
<td align="left"><p>Initializes the caller-allocated [<strong>NET_REQUEST_QUEUE_CONFIG</strong>](net-request-queue-config.md) structure to create a default request queue.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_METHOD_HANDLER_INIT method</strong>](net-request-queue-method-handler-init.md)</p></td>
<td align="left"><p>Initializes the [NET_REQUEST_QUEUE_METHOD_HANDLER](net-request-queue-method-handler.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_QUERY_DATA_HANDLER_INIT method</strong>](net-request-queue-query-data-handler-init.md)</p></td>
<td align="left"><p>Initializes the [NET_REQUEST_QUEUE_QUERY_DATA_HANDLER](net-request-queue-query-data-handler.md) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_SET_DATA_HANDLER_INIT method</strong>](net-request-queue-set-data-handler-init.md)</p></td>
<td align="left"><p>Initializes the [NET_REQUEST_QUEUE_SET_DATA_HANDLER](net-request-queue-set-data-handler.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_RXQUEUE_CONFIG_INIT method</strong>](net-rxqueue-config-init.md)</p></td>
<td align="left"><p>Initializes the [NET_RXQUEUE_CONFIG](net-rxqueue-config.md) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_TXQUEUE_CONFIG_INIT method</strong>](net-txqueue-config-init.md)</p></td>
<td align="left"><p>Initializes the [NET_TXQUEUE_CONFIG](net-txqueue-config.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetAdapterCreate method</strong>](netadaptercreate.md)</p></td>
<td align="left"><p>Creates a net adapter object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetAdapterDeviceInitConfig method</strong>](netadapterdeviceinitconfig.md)</p></td>
<td align="left"><p>Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetAdapterDriverWdmGetHandle method</strong>](netadapterdriverwdmgethandle.md)</p></td>
<td align="left"><p>A WDF client driver calls [<strong>NetAdapterDriverWdmGetHandle</strong>](netadapterdriverwdmgethandle.md) to get a handle that can be used with NDIS APIs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetAdapterGetNetLuid method</strong>](netadaptergetnetluid.md)</p></td>
<td align="left"><p>Retrieves the NET_LUID that is assigned to a net adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetAdapterGetPowerSettings method</strong>](netadaptergetpowersettings.md)</p></td>
<td align="left"><p>Retrieves the NETPOWERSETTINGS that is associated with a net adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetAdapterOpenConfiguration method</strong>](netadapteropenconfiguration.md)</p></td>
<td align="left"><p>Opens the adapter’s configuration database.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetAdapterSetCurrentLinkState method</strong>](netadaptersetcurrentlinkstate.md)</p></td>
<td align="left"><p>Set the current link state of the of the network adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetAdapterSetDataPathCapabilities method</strong>](netadaptersetdatapathcapabilities.md)</p></td>
<td align="left"><p>Sets the data path capabilities of the network adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetAdapterSetLinkLayerCapabilities method</strong>](netadaptersetlinklayercapabilities.md)</p></td>
<td align="left"><p>Sets the link capabilities of the network adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetAdapterSetLinkLayerMtuSize method</strong>](netadaptersetlinklayermtusize.md)</p></td>
<td align="left"><p>Overrides the maximum transfer unit (MTU) size that the client driver provided to [<strong>NetAdapterSetLinkLayerCapabilities</strong>](netadaptersetlinklayercapabilities.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetAdapterSetPowerCapabilities method</strong>](netadaptersetpowercapabilities.md)</p></td>
<td align="left"><p>Sets the power capabilities of the network adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetAdapterWdmGetNdisHandle method</strong>](netadapterwdmgetndishandle.md)</p></td>
<td align="left"><p>Retrieves the NDIS adapter handle for a specified net adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetConfigurationAssignBinary method</strong>](netconfigurationassignbinary.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetConfigurationAssignMultiString method</strong>](netconfigurationassignmultistring.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetConfigurationAssignUlong method</strong>](netconfigurationassignulong.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetConfigurationAssignUnicodeString method</strong>](netconfigurationassignunicodestring.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetConfigurationClose method</strong>](netconfigurationclose.md)</p></td>
<td align="left"><p>Releases the handle to the registry key that is associated with an adapter configuration object and then deletes the adapter configuration object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetConfigurationOpenSubConfiguration method</strong>](netconfigurationopensubconfiguration.md)</p></td>
<td align="left"><p>Opens a sub configuration of a specified adapter configuration object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetConfigurationQueryBinary method</strong>](netconfigurationquerybinary.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetConfigurationQueryMultiString method</strong>](netconfigurationquerymultistring.md)</p></td>
<td align="left"><p>Retrieves the strings that are currently assigned to the adapter configuration object, creates a WDFSTRING object for each string, and adds each string object to a specified collection object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetConfigurationQueryNetworkAddress method</strong>](netconfigurationquerynetworkaddress.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetConfigurationQueryString method</strong>](netconfigurationquerystring.md)</p></td>
<td align="left"><p>Retrieves the specified string value from the adapter configuration object and assigns the string to a specified framework string object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetConfigurationQueryUlong method</strong>](netconfigurationqueryulong.md)</p></td>
<td align="left"><p>Retrieves the specified unsigned long word (REG_DWORD) data from the adapter configuration object and copies the data to a specified location.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetPacketGetTypedContext method</strong>](netpacketgettypedcontext.md)</p></td>
<td align="left"><p>Client drivers should not call this function directly. Instead, use [<strong>NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME</strong>](net-packet-declare-context-type-with-name.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents method</strong>](netpowersettingsgetenabledmediaspecificwakeupevents.md)</p></td>
<td align="left"><p>Retrieves the media-specific wake-up events that a network adapter supports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetPowerSettingsGetEnabledProtocolOffloads method</strong>](netpowersettingsgetenabledprotocoloffloads.md)</p></td>
<td align="left"><p>Retrieves the low power protocol offload capabilities of a network adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetPowerSettingsGetEnabledWakePatterns method</strong>](netpowersettingsgetenabledwakepatterns.md)</p></td>
<td align="left"><p>Retrieves the wake-on-LAN (WOL) patterns that a network adapter supports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetPowerSettingsGetEnabledWakeUpFlags method</strong>](netpowersettingsgetenabledwakeupflags.md)</p></td>
<td align="left"><p>Retrieves the media-independent wake-up events that a network adapter supports.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetPowerSettingsGetProtocolOffload method</strong>](netpowersettingsgetprotocoloffload.md)</p></td>
<td align="left"><p>Retrieves a structure that specifies parameters for a low power protocol offload to a network adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetPowerSettingsGetProtocolOffloadCount method</strong>](netpowersettingsgetprotocoloffloadcount.md)</p></td>
<td align="left"><p>Retrieves the number of protocol offload structures associated with a NETPOWERSETTINGS object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetPowerSettingsGetProtocolOffloadCountForType method</strong>](netpowersettingsgetprotocoloffloadcountfortype.md)</p></td>
<td align="left"><p>Retrieves the number of protocol offload structures in the NETPOWERSETTINGS object for the particular offload type.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetPowerSettingsGetWakePattern method</strong>](netpowersettingsgetwakepattern.md)</p></td>
<td align="left"><p>Retrieves a wake-on-LAN (WoL) pattern structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetPowerSettingsGetWakePatternCount method</strong>](netpowersettingsgetwakepatterncount.md)</p></td>
<td align="left"><p>Retrieves the number of wake-on-LAN (WoL) patterns stored in a NETPOWERSETTINGS object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetPowerSettingsGetWakePatternCountForType method</strong>](netpowersettingsgetwakepatterncountfortype.md)</p></td>
<td align="left"><p>Retrieves the number of wake-on-LAN (WoL) patterns stored in the NETPOWERSETTINGS object for a particular WoL pattern type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetPowerSettingsIsProtocolOffloadEnabled method</strong>](netpowersettingsisprotocoloffloadenabled.md)</p></td>
<td align="left"><p>Determines if a protocol offload structure is enabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetPowerSettingsIsWakePatternEnabled method</strong>](netpowersettingsiswakepatternenabled.md)</p></td>
<td align="left"><p>Determines if a wake-on-LAN (WoL) pattern is enabled for a network adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRequestCompleteWithoutInformation method</strong>](netrequestcompletewithoutinformation.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRequestGetId method</strong>](netrequestgetid.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRequestGetPortNumber method</strong>](netrequestgetportnumber.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRequestGetSwitchId method</strong>](netrequestgetswitchid.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRequestGetType method</strong>](netrequestgettype.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRequestGetVPortId method</strong>](netrequestgetvportid.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRequestMethodComplete method</strong>](netrequestmethodcomplete.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRequestQueryDataComplete method</strong>](netrequestquerydatacomplete.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRequestQueueCreate method</strong>](netrequestqueuecreate.md)</p></td>
<td align="left"><p>Creates a net request queue object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRequestQueueGetAdapter method</strong>](netrequestqueuegetadapter.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRequestRetrieveInputOutputBuffer method</strong>](netrequestretrieveinputoutputbuffer.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRequestSetBytesNeeded method</strong>](netrequestsetbytesneeded.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRequestSetDataComplete method</strong>](netrequestsetdatacomplete.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRequestWdmGetNdisOidRequest method</strong>](netrequestwdmgetndisoidrequest.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRingBufferAdvanceNextPacket method</strong>](netringbufferadvancenextpacket.md)</p></td>
<td align="left"><p>Increments the NextIndex value of the ring buffer and then returns a pointer to the net packet at the new NextIndex value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRingBufferGetElementAtIndex method</strong>](netringbuffergetelementatindex.md)</p></td>
<td align="left"><p>Returns the element at the specified index in the ring buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRingBufferGetNextPacket method</strong>](netringbuffergetnextpacket.md)</p></td>
<td align="left"><p>Returns a pointer to the net packet at the NextIndex value of the ring buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRingBufferGetNumberOfElementsInRange method</strong>](netringbuffergetnumberofelementsinrange.md)</p></td>
<td align="left"><p>Calculates the number of elements contained in a range of the specified net ring buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRingBufferGetPacketAtIndex method</strong>](netringbuffergetnumberofelementsinrange.md)</p></td>
<td align="left"><p>Returns a pointer to the net packet at the specified index value of the ring buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRingBufferIncrementIndex method</strong>](netringbufferincrementindex.md)</p></td>
<td align="left"><p>Returns the next index value after the specified index value, wrapping around to the beginning of the ring buffer if necessary.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRingBufferReturnCompletedPackets method</strong>](netringbufferreturncompletedpackets.md)</p></td>
<td align="left"><p>Calls [<strong>NetRingBufferReturnCompletedPacketsThroughIndex</strong>](netringbufferreturncompletedpacketsthroughindex.md) with the NextIndex value of the specified ring buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRingBufferReturnCompletedPacketsThroughIndex method</strong>](netringbufferreturncompletedpacketsthroughindex.md)</p></td>
<td align="left"><p>Sets the BeginIndex value of the specified ring buffer to the first packet that is not completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRxQueueConfigureDmaAllocator</strong>](netrxqueueconfiguredmaallocator.md)</p></td>
<td align="left"><p>Associates a WDFDMAENABLER object with a receive queue.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRxQueueCreate method</strong>](netrxqueuecreate.md)</p></td>
<td align="left"><p>Creates a net receive queue object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRxQueueGetRingBuffer method</strong>](netrxqueuegetringbuffer.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetRxQueueInitGetQueueId method</strong>](netrxqueueinitgetqueueid.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetRxQueueNotifyMoreReceivedPacketsAvailable method</strong>](netrxqueuenotifymorereceivedpacketsavailable.md)</p></td>
<td align="left"><p>The client driver calls [<strong>NetRxQueueNotifyMoreReceivedPacketsAvailable</strong>](netrxqueuenotifymorereceivedpacketsavailable.md) to resume queue operations after NetAdapterCx calls the client's [<em>EVT_RXQUEUE_SET_NOTIFICATION_ENABLED</em>](evt-rxqueue-set-notification-enabled.md) event callback routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetTxQueueCreate method</strong>](nettxqueuecreate.md)</p></td>
<td align="left"><p>Creates a net transmit queue object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetTxQueueGetRingBuffer method</strong>](nettxqueuegetringbuffer.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NetTxQueueInitGetQueueId method</strong>](nettxqueueinitgetqueueid.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NetTxQueueNotifyMoreCompletedPacketsAvailable method</strong>](nettxqueuenotifymorecompletedpacketsavailable.md)</p></td>
<td align="left"><p>The client driver calls [<strong>NetTxQueueNotifyMoreCompletedPacketsAvailable</strong>](nettxqueuenotifymorecompletedpacketsavailable.md) to resume queue operations after NetAdapterCx calls the client's [<em>EVT_TXQUEUE_SET_NOTIFICATION_ENABLED</em>](evt-txqueue-set-notification-enabled.md) event callback routine.</p></td>
</tr>
</tbody>
</table>

 

## Enumerations


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Enumeration</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_AUTO_NEGOTIATION_FLAGS</strong>](net-adapter-auto-negotiation-flags.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_DRIVER_TYPE</strong>](net-adapter-driver-type.md)</p></td>
<td align="left"><p>The [<strong>NET_ADAPTER_DRIVER_TYPE</strong>](net-adapter-driver-type.md) enumeration identifies the type of network adapter driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS</strong>](net-adapter-media-specific-wakeup-events-flags.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_PAUSE_FUNCTIONS</strong>](net-adapter-pause-functions.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_POWER_FLAGS</strong>](net-adapter-power-flags.md)</p></td>
<td align="left"><p>Defines flags that are used in a client driver's [<strong>NET_ADAPTER_POWER_CAPABILITIES</strong>](net-adapter-power-capabilities.md) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS</strong>](net-adapter-protocol-offloads-flags.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_STATISTICS_FLAGS</strong>](net-adapter-statistics-flags.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_WAKE_PATTERN_FLAGS</strong>](net-adapter-wake-pattern-flags.md)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_WAKEUP_EVENTS_FLAGS</strong>](net-adapter-wakeup-events-flags.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_CONFIGURATION_QUERY_ULONG_FLAGS</strong>](net-configuration-query-ulong-flags.md)</p></td>
<td align="left"><p>The [<strong>NET_CONFIGURATION_QUERY_ULONG_FLAGS</strong>](net-configuration-query-ulong-flags.md) enumeration is used as an input parameter to the [<strong>NetConfigurationQueryUlong</strong>](netconfigurationqueryulong.md) method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_PACKET_FILTER_TYPES_FLAGS</strong>](net-packet-filter-types-flags.md)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_TYPE</strong>](net-request-queue-type.md)</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

## Structures


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_CONFIG</strong>](net-adapter-config.md)</p></td>
<td align="left"><p>Describes the configuration options for a NetAdapterCx client driver. An initialized [<strong>NET_ADAPTER_CONFIG</strong>](net-adapter-config.md) structure is an input parameter to [<strong>NetAdapterCreate</strong>](netadaptercreate.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_DATAPATH_CAPABILITIES</strong>](net-adapter-datapath-capabilities.md)</p></td>
<td align="left"><p>Describes the data path capabilities of the adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_LINK_LAYER_CAPABILITIES</strong>](net-adapter-link-layer-capabilities.md)</p></td>
<td align="left"><p>Describes the MAC capabilities of the adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_LINK_STATE</strong>](net-adapter-link-state.md)</p></td>
<td align="left"><p>Describes the link state of the adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_ADAPTER_PHYSICAL_ADDRESS</strong>](net-adapter-physical-address.md)</p></td>
<td align="left"><p>Call [NET_ADAPTER_PHYSICAL_ADDRESS_INIT](net-adapter-physical-address-init.md) to initialize this structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_ADAPTER_POWER_CAPABILITIES</strong>](net-adapter-power-capabilities.md)</p></td>
<td align="left"><p>Describes the power capabilities of the adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_DRIVER_GLOBALS</strong>](net-driver-globals.md)</p></td>
<td align="left"><p>Call NET_DRIVER_GLOBALS_INIT to initialize this structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_PACKET</strong>](net-packet.md)</p></td>
<td align="left"><p>TBD</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_PACKET_FRAGMENT</strong>](net-packet-fragment.md)</p></td>
<td align="left"><p>TBD</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_CONFIG</strong>](net-request-queue-config.md)</p></td>
<td align="left"><p>Call [NET_REQUEST_QUEUE_CONFIG_INIT](net-request-queue-config-init.md) to initialize this structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_METHOD_HANDLER</strong>](net-request-queue-method-handler.md)</p></td>
<td align="left"><p>Call [NET_REQUEST_QUEUE_METHOD_HANDLER_INIT](net-request-queue-method-handler-init.md) to initialize this structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_QUERY_DATA_HANDLER</strong>](net-request-queue-query-data-handler.md)</p></td>
<td align="left"><p>Call [NET_REQUEST_QUEUE_QUERY_DATA_HANDLER_INIT](net-request-queue-query-data-handler-init.md) to initialize this structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_REQUEST_QUEUE_SET_DATA_HANDLER</strong>](net-request-queue-set-data-handler.md)</p></td>
<td align="left"><p>Call [NET_REQUEST_QUEUE_SET_DATA_HANDLER_INIT](net-request-queue-set-data-handler-init.md) to initialize this structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_RING_BUFFER</strong>](net-ring-buffer.md)</p></td>
<td align="left"><p>Call NET_RING_BUFFER_INIT to initialize this structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NET_RXQUEUE_CONFIG</strong>](net-rxqueue-config.md)</p></td>
<td align="left"><p>Describes the configuration options for a NetAdapterCx client driver's receive queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NET_TXQUEUE_CONFIG</strong>](net-txqueue-config.md)</p></td>
<td align="left"><p>Call [NET_TXQUEUE_CONFIG_INIT](net-txqueue-config-init.md) to initialize this structure.</p></td>
</tr>
</tbody>
</table>

 

 

 





