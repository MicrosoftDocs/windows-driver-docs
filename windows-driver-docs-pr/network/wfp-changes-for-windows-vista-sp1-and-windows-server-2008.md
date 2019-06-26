---
title: WFP Changes for Windows Vista SP1 and Windows Server 2008
description: WFP Changes for Windows Vista SP1 and Windows Server 2008
ms.assetid: c901dbed-639d-473b-aaf0-8470e9c04009
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WFP Changes for Windows Vista SP1 and Windows Server 2008


Several changes have been made in the available functions and behavior of the Windows Filtering Platform that begin with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008. Frequently, to take advantage of the new features, you must compile or recompile a callout driver that has the NTDDI\_VERSION macro set to NTDDI\_WIN6SP1.

-   New functions:
    [**FwpsConstructIpHeaderForTransportPacket0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsconstructipheaderfortransportpacket0)
    [**FwpsReassembleForwardFragmentGroup0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsreassembleforwardfragmentgroup0)
-   New FWPS\_STREAM\_FLAG\_RECEIVE\_PUSH flag option that is described in [**FwpsStreamInjectAsync0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsstreaminjectasync0)

-   Updated and renamed filtering conditions, listed in [Filtering Conditions Available at Each Filtering Layer](https://docs.microsoft.com/windows-hardware/drivers/network/filtering-conditions-available-at-each-filtering-layer)

-   Updated and renamed data field identifiers that were added to FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_*XXX* and FWPS\_LAYER\_INBOUND\_ICMP\_ERROR\_*XXX* layers, listed in [Data Field Identifiers](https://docs.microsoft.com/windows-hardware/drivers/network/data-field-identifiers), together with behavior changes

-   Additional metadata field identifiers, listed in [Metadata Fields](https://docs.microsoft.com/windows-hardware/drivers/network/metadata-fields) and [Metadata Fields at Each Filtering Layer](https://docs.microsoft.com/windows-hardware/drivers/network/metadata-fields-at-each-filtering-layer)

-   The following documentation topics are new:
    -   [Developing IPsec-Compatible Callout Drivers](developing-ipsec-compatible-callout-drivers.md)
    -   [Processing Classify Callouts Asynchronously](processing-classify-callouts-asynchronously.md)
-   The following topics contain additional updates:
    [Processing Notify Callouts](processing-notify-callouts.md)
    [Stream Inspection](stream-inspection.md)
    [**FwpsFlowAssociateContext0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsflowassociatecontext0)
    [**FwpsFlowRemoveContext0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsflowremovecontext0)
    [*classifyFn*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nc-fwpsk-fwps_callout_classify_fn0)
    [*notifyFn*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/nc-fwpsk-fwps_callout_notify_fn0)
    [**FWPS\_CALLOUT0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ns-fwpsk-fwps_callout0_)
    [**FWPS\_INCOMING\_METADATA\_VALUES0**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fwpsk/ns-fwpsk-fwps_incoming_metadata_values0_)

 

 





