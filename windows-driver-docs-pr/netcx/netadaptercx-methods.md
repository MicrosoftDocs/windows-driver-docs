---
title: NetAdapterCx methods
description: NetAdapterCx methods
ms.assetid: A9D14552-0083-4066-987F-2327BB339223
keywords:
- Network Adapter WDF Class Extension methods, NetAdapterCx methods, NetCx methods
ms.author: windowsdriverdev
ms.date: 08/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetAdapterCx methods

This section contains methods for Network Adapter WDF Class Extension (NetAdapterCx) client drivers.

## Initialize or add methods

The following methods are used to initialize structures or add handlers to a NetAdapterCx client driver.

[NET_ADAPTER_CONFIG_INIT method](net-adapter-config-init.md)

[NET_ADAPTER_DATAPATH_CAPABILITIES_INIT method](net-adapter-datapath-capabilities-init.md)

[NET_ADAPTER_LINK_LAYER_ADDRESS_INIT](net-adapter-link-layer-address-init.md)

[NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT_NO_PHYSICAL_ADDRESS](net-adapter-link-layer-capabilities-init-no-physical-address.md)

[NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT](net-adapter-link-layer-capabilities-init.md)

[NET_ADAPTER_LINK_STATE_INIT method](net-adapter-link-state-init.md)

[NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED method](net-adapter-link-state-init-disconnected.md)

[NET_ADAPTER_PHYSICAL_ADDRESS_INIT method](net-adapter-physical-address-init.md)

[NET_ADAPTER_POWER_CAPABILITIES_INIT method](net-adapter-power-capabilities-init.md)

[NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER method](net-request-queue-config-add-initialized-method-handler.md)

[NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_QUERY_DATA_HANDLER method](net-request-queue-config-add-initialized-query-data-handler.md)

[NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_SET_DATA_HANDLER method](net-request-queue-config-add-initialized-set-data-handler.md)

[NET_REQUEST_QUEUE_CONFIG_ADD_METHOD_HANDLER method](net-request-queue-config-add-method-handler.md)

[NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER method](net-request-queue-config-add-query-data-handler.md)

[NET_REQUEST_QUEUE_CONFIG_ADD_SET_DATA_HANDLER method](net-request-queue-config-add-set-data-handler.md)

[NET_REQUEST_QUEUE_CONFIG_INIT method](net-request-queue-config-init.md)

[NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_PARALLEL method](net-request-queue-config-init-default-parallel.md)

[NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL method](net-request-queue-config-init-default-sequential.md)

[NET_REQUEST_QUEUE_METHOD_HANDLER_INIT method](net-request-queue-method-handler-init.md)

[NET_REQUEST_QUEUE_QUERY_DATA_HANDLER_INIT method](net-request-queue-query-data-handler-init.md)

[NET_REQUEST_QUEUE_SET_DATA_HANDLER_INIT method](net-request-queue-set-data-handler-init.md)

[NET_RXQUEUE_CONFIG_INIT method](net-rxqueue-config-init.md)

[NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT method](net-rxqueue-dma-allocator-config-init.md)

[NET_TXQUEUE_CONFIG_INIT method](net-txqueue-config-init.md)

## All other methods

The following methods are used for all other functionality in a NetAdapterCx client driver other than initializing a structure or adding a handler.

[NetAdapterCreate method](netadaptercreate.md)

[NetAdapterDeviceInitConfig method](netadapterdeviceinitconfig.md)

[NetAdapterDriverWdmGetHandle method](netadapterdriverwdmgethandle.md)

[NetAdapterGetNetLuid method](netadaptergetnetluid.md)

[NetAdapterGetPowerSettings method](netadaptergetpowersettings.md)

[NetAdapterOpenConfiguration method](netadapteropenconfiguration.md)

[NetAdapterSetCurrentLinkLayerAddress method](netadaptersetcurrentlinklayeraddress.md)

[NetAdapterSetCurrentLinkState method](netadaptersetcurrentlinkstate.md)

[NetAdapterSetDataPathCapabilities method](netadaptersetdatapathcapabilities.md)

[NetAdapterSetLinkLayerCapabilities method](netadaptersetlinklayercapabilities.md)

[NetAdapterSetLinkLayerMtuSize method](netadaptersetlinklayermtusize.md)

[NetAdapterSetPermanentLinkLayerAddress method](netadaptersetpermanentlinklayeraddress.md)

[NetAdapterSetPowerCapabilities method](netadaptersetpowercapabilities.md)

[NetAdapterWdmGetNdisHandle method](netadapterwdmgetndishandle.md)

[NetConfigurationAssignBinary method](netconfigurationassignbinary.md)

[NetConfigurationAssignMultiString method](netconfigurationassignmultistring.md)

[NetConfigurationAssignUlong method](netconfigurationassignulong.md)

[NetConfigurationAssignUnicodeString method](netconfigurationassignunicodestring.md)

[NetConfigurationClose method](netconfigurationclose.md)

[NetConfigurationOpenSubConfiguration method](netconfigurationopensubconfiguration.md)

[NetConfigurationQueryBinary method](netconfigurationquerybinary.md)

[NetConfigurationQueryMultiString method](netconfigurationquerymultistring.md)

[NetConfigurationQueryLinkLayerAddress method](netconfigurationquerylinklayeraddress.md)

[NetConfigurationQueryString method](netconfigurationquerystring.md)

[NetConfigurationQueryUlong method](netconfigurationqueryulong.md)

[NetPacketGetContextFromToken method](netpacketgetcontextfromtoken.md)

[NetPacketGetTypedContext method](netpacketgettypedcontext.md)

[NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents method](netpowersettingsgetenabledmediaspecificwakeupevents.md)

[NetPowerSettingsGetEnabledProtocolOffloadFlags method](netpowersettingsgetenabledprotocoloffloadflags.md)

[NetPowerSettingsGetEnabledWakePatterns method](netpowersettingsgetenabledwakepatterns.md)

[NetPowerSettingsGetEnabledWakeUpFlags method](netpowersettingsgetenabledwakeupflags.md)

[NetPowerSettingsGetProtocolOffload method](netpowersettingsgetprotocoloffload.md)

[NetPowerSettingsGetProtocolOffloadCount method](netpowersettingsgetprotocoloffloadcount.md)

[NetPowerSettingsGetProtocolOffloadCountForType method](netpowersettingsgetprotocoloffloadcountfortype.md)

[NetPowerSettingsGetWakePattern method](netpowersettingsgetwakepattern.md)

[NetPowerSettingsGetWakePatternCount method](netpowersettingsgetwakepatterncount.md)

[NetPowerSettingsGetWakePatternCountForType method](netpowersettingsgetwakepatterncountfortype.md)

[NetPowerSettingsIsProtocolOffloadEnabled method](netpowersettingsisprotocoloffloadenabled.md)

[NetPowerSettingsIsWakePatternEnabled method](netpowersettingsiswakepatternenabled.md)

[NetRequestCompleteWithoutInformation method](netrequestcompletewithoutinformation.md)

[NetRequestGetId method](netrequestgetid.md)

[NetRequestGetPortNumber method](netrequestgetportnumber.md)

[NetRequestGetSwitchId method](netrequestgetswitchid.md)

[NetRequestGetType method](netrequestgettype.md)

[NetRequestGetVPortId method](netrequestgetvportid.md)

[NetRequestMethodComplete method](netrequestmethodcomplete.md)

[NetRequestQueryDataComplete method](netrequestquerydatacomplete.md)

[NetRequestQueueCreate method](netrequestqueuecreate.md)

[NetRequestQueueGetAdapter method](netrequestqueuegetadapter.md)

[NetRequestRetrieveInputOutputBuffer method](netrequestretrieveinputoutputbuffer.md)

[NetRequestSetBytesNeeded method](netrequestsetbytesneeded.md)

[NetRequestSetDataComplete method](netrequestsetdatacomplete.md)

[NetRequestWdmGetNdisOidRequest method](netrequestwdmgetndisoidrequest.md)

[NetRingBufferAdvanceNextPacket method](netringbufferadvancenextpacket.md)

[NetRingBufferGetElementAtIndex method](netringbuffergetelementatindex.md)

[NetRingBufferGetNextPacket method](netringbuffergetnextpacket.md)

[NetRingBufferGetNumberOfElementsInRange method](netringbuffergetnumberofelementsinrange.md)

[NetRingBufferGetPacketAtIndex method](netringbuffergetpacketatindex.md)

[NetRingBufferIncrementIndex method](netringbufferincrementindex.md)

[NetRingBufferReturnCompletedPackets method](netringbufferreturncompletedpackets.md)

[NetRingBufferReturnCompletedPacketsThroughIndex method](netringbufferreturncompletedpacketsthroughindex.md)

[NetRxQueueCreate method](netrxqueuecreate.md)

[NetRxQueueGetPacketContextToken method](netrxqueuegetpacketcontexttoken.md)

[NetRxQueueGetBufferLayoutHint method](netrxqueuegetbufferlayouthint.md)

[NetRxQueueGetRingBuffer method](netrxqueuegetringbuffer.md)

[NetRxQueueInitAddPacketContextAttributes method](netrxqueueinitaddpacketcontextattributes.md)

[NetRxQueueInitGetQueueId method](netrxqueueinitgetqueueid.md)

[NetRxQueueInitSetDmaAllocatorConfig method](netrxqueueinitsetdmaallocatorconfig.md)

[NetRxQueueNotifyMoreReceivedPacketsAvailable method](netrxqueuenotifymorereceivedpacketsavailable.md)

[NetRxQueueQueryAllocatorCacheEnabled method](netrxqueuequeryallocatorcacheenabled.md)

[NetTxQueueCreate method](nettxqueuecreate.md)

[NetTxQueueGetPacketContextToken method](nettxqueuegetpacketcontexttoken.md)

[NetTxQueueGetRingBuffer method](nettxqueuegetringbuffer.md)

[NetTxQueueInitAddPacketContextAttributes](nettxqueueinitaddpacketcontextattributes.md)

[NetTxQueueInitGetQueueId method](nettxqueueinitgetqueueid.md)

[NetTxQueueNotifyMoreCompletedPacketsAvailable method](nettxqueuenotifymorecompletedpacketsavailable.md)

