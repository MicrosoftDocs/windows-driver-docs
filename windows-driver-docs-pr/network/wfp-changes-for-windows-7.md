---
title: WFP Changes for Windows 7
description: WFP Changes for Windows 7
ms.date: 04/20/2017
---

# WFP Changes for Windows 7


Several changes have been made in the available functions and behavior of the Windows Filtering Platform that begin with Windows 7. Frequently, to take advantage of the new features, you must compile or recompile a callout driver that has the NTDDI\_VERSION macro set to NTDDI\_WIN7.

-   New functions:
    - [**FwpsAcquireClassifyHandle0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsacquireclassifyhandle0)
    - [**FwpsAcquireWritableLayerDataPointer0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsacquirewritablelayerdatapointer0)
    - [**FwpsApplyModifiedLayerData0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsapplymodifiedlayerdata0)
    - [**FwpsCalloutRegister1**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpscalloutregister1)
    - [**FwpsCompleteClassify0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpscompleteclassify0)
    - [**FwpsPendClassify0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpspendclassify0)
    - [**FwpsReleaseClassifyHandle0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsreleaseclassifyhandle0)
    - [*classifyFn1*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_classify_fn1)
    - [*notifyFn1*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_notify_fn1)
    - [**FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0**](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn0)
    - [**FwpsInjectTransportSendAsync1**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsinjecttransportsendasync1)
    - [**FwpsNetBufferListAssociateContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistassociatecontext0)
    - [**FwpsNetBufferListGetTagForContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistgettagforcontext0)
    - [**FwpsNetBufferListRemoveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistremovecontext0)
    - [**FwpsNetBufferListRetrieveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistretrievecontext0)
    - [**FwpsAleEndpointCreateEnumHandle0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsaleendpointcreateenumhandle0)
    - [**FwpsAleEndpointDestroyEnumHandle0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsaleendpointdestroyenumhandle0)
    - [**FwpsAleEndpointEnum0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsaleendpointenum0)
    - [**FwpsAleEndpointGetById0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsaleendpointgetbyid0)
    - [**FwpsAleEndpointGetSecurityInfo0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsaleendpointgetsecurityinfo0)
    - [**FwpsAleEndpointSetSecurityInfo0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsaleendpointsetsecurityinfo0)
-   New structures and enumerations:
    - [**FWPS\_ALE\_ENDPOINT\_ENUM\_TEMPLATE0**](/windows/win32/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_enum_template0)
    - [**FWPS\_ALE\_ENDPOINT\_PROPERTIES0**](/windows/win32/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_properties0)
    - [**FWPS\_BIND\_REQUEST0**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-_fwps_bind_request0)
    - [**FWPS\_CALLOUT1**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-fwps_callout1_)
    - [**FWPS\_CONNECT\_REQUEST0**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-_fwps_connect_request0)
    - [**FWPS\_FIELDS\_ALE\_BIND\_REDIRECT\_V4**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_bind_redirect_v4_)
    - [**FWPS\_FIELDS\_ALE\_BIND\_REDIRECT\_V6**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_bind_redirect_v6_)
    - [**FWPS\_FIELDS\_ALE\_CONNECT\_REDIRECT\_V4**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_connect_redirect_v4_)
    - [**FWPS\_FIELDS\_ALE\_CONNECT\_REDIRECT\_V6**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_connect_redirect_v6_)
    - [**FWPS\_FIELDS\_ALE\_ENDPOINT\_CLOSURE\_V4**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_endpoint_closure_v4_)
    - [**FWPS\_FIELDS\_ALE\_ENDPOINT\_CLOSURE\_V6**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_endpoint_closure_v6_)
    - [**FWPS\_FIELDS\_ALE\_RESOURCE\_RELEASE\_V4**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_resource_release_v4_)
    - [**FWPS\_FIELDS\_ALE\_RESOURCE\_RELEASE\_V6**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_resource_release_v6_)
    - [**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_802\_3**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_mac_frame_ethernet_)
    - [**FWPS\_FIELDS\_KM\_AUTHORIZATION**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_km_authorization_)
    - [**FWPS\_FIELDS\_NAME\_RESOLUTION\_CACHE\_V4**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_name_resolution_cache_v4_)
    - [**FWPS\_FIELDS\_NAME\_RESOLUTION\_CACHE\_V6**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_name_resolution_cache_v6_)
    - [**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_802\_3**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_mac_frame_ethernet_)
    - [**FWPS\_FIELDS\_STREAM\_PACKET\_V4**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_stream_packet_v4_)
    - [**FWPS\_FIELDS\_STREAM\_PACKET\_V6**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_stream_packet_v6_)
    - [**FWPS\_FILTER1**](/windows/win32/api/fwpstypes/ns-fwpstypes-fwps_filter1)
    - [**FWPS\_NET\_BUFFER\_LIST\_EVENT\_TYPE0**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_net_buffer_list_event_type0_)
    - [**FWPS\_TRANSPORT\_SEND\_PARAMS1**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-fwps_transport_send_params1_)
-   New documentation topics:
    - [Using Bind or Connect Redirection](using-bind-or-connect-redirection.md)
    - [Using Packet Tagging](using-packet-tagging.md)
    - [ALE Endpoint Lifetime Management](ale-endpoint-lifetime-management.md)

 

