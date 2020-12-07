---
title: WFP Changes for Windows 8
description: WFP Changes for Windows 8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WFP Changes for Windows 8


Several changes have been made in the available functions and behavior of the Windows Filtering Platform that begin with Windows 8. Frequently, to take advantage of the new features, you must compile or recompile a callout driver that has the NTDDI\_VERSION macro set to NTDDI\_WIN8.

-   New features:
    - [Using Layer 2 Filtering](using-layer-2-filtering.md)
    - [Using Proxied Connections Tracking](using-proxied-connections-tracking.md)
    - [Using Virtual Switch Filtering](using-virtual-switch-filtering.md)
-   New functions:
    - [**FwpsCalloutRegister2**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpscalloutregister2)
    - [**FwpsFlowAbort0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsflowabort0)
    - [**FwpsInjectMacReceiveAsync0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsinjectmacreceiveasync0)
    - [**FwpsInjectMacSendAsync0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsinjectmacsendasync0)
    - [**FwpsNetBufferListAssociateContext1**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistassociatecontext1)
    - [**FwpsQueryConnectionRedirectState0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsqueryconnectionredirectstate0)
    - [**FwpsRedirectHandleCreate0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsredirecthandlecreate0)
    - [**FwpsRedirectHandleDestroy0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsredirecthandledestroy0)
    - [**FwpsvSwitchEventsSubscribe0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsvswitcheventssubscribe0)
    - [**FwpsvSwitchEventsUnsubscribe0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsvswitcheventsunsubscribe0)
    - [**FwpsvSwitchNotifyComplete0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsvswitchnotifycomplete0)
-   New callback functions:
    - [*FWPS\_CALLOUT\_CLASSIFY\_FN2*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_classify_fn2)
    - [*FWPS\_CALLOUT\_NOTIFY\_FN2*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_notify_fn2)
    - [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn1)
    - [*FWPS\_VSWITCH\_FILTER\_ENGINE\_REORDER\_CALLBACK0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_vswitch_filter_engine_reorder_callback0)
    - [*FWPS\_VSWITCH\_INTERFACE\_EVENT\_CALLBACK0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_vswitch_interface_event_callback0)
    - [*FWPS\_VSWITCH\_LIFETIME\_EVENT\_CALLBACK0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_vswitch_lifetime_event_callback0)
    - [*FWPS\_VSWITCH\_POLICY\_EVENT\_CALLBACK0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_vswitch_policy_event_callback0)
    - [*FWPS\_VSWITCH\_PORT\_EVENT\_CALLBACK0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_vswitch_port_event_callback0)
    - [*FWPS\_VSWITCH\_RUNTIME\_STATE\_RESTORE\_CALLBACK0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_vswitch_runtime_state_restore_callback0)
    - [*FWPS\_VSWITCH\_RUNTIME\_STATE\_SAVE\_CALLBACK0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_vswitch_runtime_state_save_callback0)
-   New structures:
    - [**FWPS\_FILTER2**](/windows/win32/api/fwpstypes/ns-fwpstypes-fwps_filter2)
    - [**FWPS\_VSWITCH\_EVENT\_DISPATCH\_TABLE0**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-fwps_vswitch_event_dispatch_table0_)
-   New enumerations:
    - [**FWPS\_CONNECTION\_REDIRECT\_STATE**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_connection_redirect_state_)
    - [**FWPS\_FIELDS\_EGRESS\_VSWITCH\_ETHERNET**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_egress_vswitch_ethernet_)
    - [**FWPS\_FIELDS\_EGRESS\_VSWITCH\_TRANSPORT\_V4**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_egress_vswitch_transport_v4_)
    - [**FWPS\_FIELDS\_EGRESS\_VSWITCH\_TRANSPORT\_V6**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_egress_vswitch_transport_v6_)
    - [**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_NATIVE**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_mac_frame_native_)
    - [**FWPS\_FIELDS\_INGRESS\_VSWITCH\_ETHERNET**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ingress_vswitch_ethernet_)
    - [**FWPS\_FIELDS\_INGRESS\_VSWITCH\_TRANSPORT\_V4**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ingress_vswitch_transport_v4_)
    - [**FWPS\_FIELDS\_INGRESS\_VSWITCH\_TRANSPORT\_V6**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ingress_vswitch_transport_v6_)
    - [**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_NATIVE**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_mac_frame_native_)
    - [**FWPS\_VSWITCH\_EVENT\_TYPE**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_vswitch_event_type_)
-   Renamed enumerations:
    - [**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_ETHERNET**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_mac_frame_ethernet_) (was **FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_802\_3**)
    - [**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_ETHERNET**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_mac_frame_ethernet_) (was **FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_802\_3**)

 

