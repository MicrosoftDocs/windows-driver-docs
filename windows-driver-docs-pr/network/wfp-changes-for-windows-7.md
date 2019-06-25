---
title: WFP Changes for Windows 7
description: WFP Changes for Windows 7
ms.assetid: c7b15182-592a-4cdb-98aa-5283ed2f51a0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WFP Changes for Windows 7


Several changes have been made in the available functions and behavior of the Windows Filtering Platform that begin with Windows 7. Frequently, to take advantage of the new features, you must compile or recompile a callout driver that has the NTDDI\_VERSION macro set to NTDDI\_WIN7.

-   New functions:
    - [**FwpsAcquireClassifyHandle0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsacquireclassifyhandle0)
    - [**FwpsAcquireWritableLayerDataPointer0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsacquirewritablelayerdatapointer0)
    - [**FwpsApplyModifiedLayerData0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsapplymodifiedlayerdata0)
    - [**FwpsCalloutRegister1**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpscalloutregister1)
    - [**FwpsCompleteClassify0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpscompleteclassify0)
    - [**FwpsPendClassify0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpspendclassify0)
    - [**FwpsReleaseClassifyHandle0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsreleaseclassifyhandle0)
    - [*classifyFn1*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nc-fwpsk-fwps_callout_classify_fn1)
    - [*notifyFn1*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nc-fwpsk-fwps_callout_notify_fn1)
    - [**FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn0)
    - [**FwpsInjectTransportSendAsync1**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsinjecttransportsendasync1)
    - [**FwpsNetBufferListAssociateContext0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsnetbufferlistassociatecontext0)
    - [**FwpsNetBufferListGetTagForContext0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsnetbufferlistgettagforcontext0)
    - [**FwpsNetBufferListRemoveContext0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsnetbufferlistremovecontext0)
    - [**FwpsNetBufferListRetrieveContext0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsnetbufferlistretrievecontext0)
    - [**FwpsAleEndpointCreateEnumHandle0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsaleendpointcreateenumhandle0)
    - [**FwpsAleEndpointDestroyEnumHandle0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsaleendpointdestroyenumhandle0)
    - [**FwpsAleEndpointEnum0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsaleendpointenum0)
    - [**FwpsAleEndpointGetById0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsaleendpointgetbyid0)
    - [**FwpsAleEndpointGetSecurityInfo0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsaleendpointgetsecurityinfo0)
    - [**FwpsAleEndpointSetSecurityInfo0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsaleendpointsetsecurityinfo0)
-   New structures and enumerations:
    - [**FWPS\_ALE\_ENDPOINT\_ENUM\_TEMPLATE0**](https://docs.microsoft.com/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_enum_template0_)
    - [**FWPS\_ALE\_ENDPOINT\_PROPERTIES0**](https://docs.microsoft.com/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_properties0_)
    - [**FWPS\_BIND\_REQUEST0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ns-fwpsk-_fwps_bind_request0)
    - [**FWPS\_CALLOUT1**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ns-fwpsk-fwps_callout1_)
    - [**FWPS\_CONNECT\_REQUEST0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ns-fwpsk-_fwps_connect_request0)
    - [**FWPS\_FIELDS\_ALE\_BIND\_REDIRECT\_V4**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_ale_bind_redirect_v4_)
    - [**FWPS\_FIELDS\_ALE\_BIND\_REDIRECT\_V6**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_ale_bind_redirect_v6_)
    - [**FWPS\_FIELDS\_ALE\_CONNECT\_REDIRECT\_V4**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_ale_connect_redirect_v4_)
    - [**FWPS\_FIELDS\_ALE\_CONNECT\_REDIRECT\_V6**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_ale_connect_redirect_v6_)
    - [**FWPS\_FIELDS\_ALE\_ENDPOINT\_CLOSURE\_V4**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_ale_endpoint_closure_v4_)
    - [**FWPS\_FIELDS\_ALE\_ENDPOINT\_CLOSURE\_V6**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_ale_endpoint_closure_v6_)
    - [**FWPS\_FIELDS\_ALE\_RESOURCE\_RELEASE\_V4**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_ale_resource_release_v4_)
    - [**FWPS\_FIELDS\_ALE\_RESOURCE\_RELEASE\_V6**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_ale_resource_release_v6_)
    - [**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_802\_3**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_inbound_mac_frame_ethernet_)
    - [**FWPS\_FIELDS\_KM\_AUTHORIZATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_km_authorization_)
    - [**FWPS\_FIELDS\_NAME\_RESOLUTION\_CACHE\_V4**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_name_resolution_cache_v4_)
    - [**FWPS\_FIELDS\_NAME\_RESOLUTION\_CACHE\_V6**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_name_resolution_cache_v6_)
    - [**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_802\_3**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_outbound_mac_frame_ethernet_)
    - [**FWPS\_FIELDS\_STREAM\_PACKET\_V4**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_stream_packet_v4_)
    - [**FWPS\_FIELDS\_STREAM\_PACKET\_V6**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_fields_stream_packet_v6_)
    - [**FWPS\_FILTER1**](https://docs.microsoft.com/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter1_)
    - [**FWPS\_NET\_BUFFER\_LIST\_EVENT\_TYPE0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ne-fwpsk-fwps_net_buffer_list_event_type0_)
    - [**FWPS\_TRANSPORT\_SEND\_PARAMS1**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ns-fwpsk-fwps_transport_send_params1_)
-   New documentation topics:
    - [Using Bind or Connect Redirection](using-bind-or-connect-redirection.md)
    - [Using Packet Tagging](using-packet-tagging.md)
    - [ALE Endpoint Lifetime Management](ale-endpoint-lifetime-management.md)

 

 





