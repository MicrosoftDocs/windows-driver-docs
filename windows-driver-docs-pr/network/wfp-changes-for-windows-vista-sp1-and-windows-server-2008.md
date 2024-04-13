---
title: WFP Changes for Windows Vista SP1 and Windows Server 2008
description: WFP Changes for Windows Vista SP1 and Windows Server 2008
ms.date: 04/20/2017
---

# WFP Changes for Windows Vista SP1 and Windows Server 2008


Several changes have been made in the available functions and behavior of the Windows Filtering Platform that begin with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008. Frequently, to take advantage of the new features, you must compile or recompile a callout driver that has the NTDDI\_VERSION macro set to NTDDI\_WIN6SP1.

-   New functions:
    [**FwpsConstructIpHeaderForTransportPacket0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsconstructipheaderfortransportpacket0)
    [**FwpsReassembleForwardFragmentGroup0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsreassembleforwardfragmentgroup0)
-   New FWPS\_STREAM\_FLAG\_RECEIVE\_PUSH flag option that is described in [**FwpsStreamInjectAsync0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsstreaminjectasync0)

-   Updated and renamed filtering conditions, listed in [Filtering Conditions Available at Each Filtering Layer](./filtering-conditions-available-at-each-filtering-layer.md)

-   Updated and renamed data field identifiers that were added to FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_*XXX* and FWPS\_LAYER\_INBOUND\_ICMP\_ERROR\_*XXX* layers, listed in [Data Field Identifiers](./data-field-identifiers.md), together with behavior changes

-   Additional metadata field identifiers, listed in [Metadata Fields](./metadata-field-identifiers.md) and [Metadata Fields at Each Filtering Layer](./metadata-fields-at-each-filtering-layer.md)

-   The following documentation topics are new:
    -   [Developing IPsec-Compatible Callout Drivers](developing-ipsec-compatible-callout-drivers.md)
    -   [Processing Classify Callouts Asynchronously](processing-classify-callouts-asynchronously.md)
-   The following topics contain additional updates:
    [Processing Notify Callouts](processing-notify-callouts.md)
    [Stream Inspection](stream-inspection.md)
    [**FwpsFlowAssociateContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsflowassociatecontext0)
    [**FwpsFlowRemoveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsflowremovecontext0)
    [*classifyFn*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_classify_fn0)
    [*notifyFn*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_notify_fn0)
    [**FWPS\_CALLOUT0**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-fwps_callout0_)
    [**FWPS\_INCOMING\_METADATA\_VALUES0**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-fwps_incoming_metadata_values0_)

