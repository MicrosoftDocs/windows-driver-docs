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
    [**FwpsConstructIpHeaderForTransportPacket0**](https://msdn.microsoft.com/library/windows/hardware/ff551154)
    [**FwpsReassembleForwardFragmentGroup0**](https://msdn.microsoft.com/library/windows/hardware/ff551205)
-   New FWPS\_STREAM\_FLAG\_RECEIVE\_PUSH flag option that is described in [**FwpsStreamInjectAsync0**](https://msdn.microsoft.com/library/windows/hardware/ff551213)

-   Updated and renamed filtering conditions, listed in [Filtering Conditions Available at Each Filtering Layer](https://msdn.microsoft.com/library/windows/hardware/ff549939)

-   Updated and renamed data field identifiers that were added to FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_*XXX* and FWPS\_LAYER\_INBOUND\_ICMP\_ERROR\_*XXX* layers, listed in [Data Field Identifiers](https://msdn.microsoft.com/library/windows/hardware/ff546312), together with behavior changes

-   Additional metadata field identifiers, listed in [Metadata Fields](https://msdn.microsoft.com/library/windows/hardware/ff559174) and [Metadata Fields at Each Filtering Layer](https://msdn.microsoft.com/library/windows/hardware/ff559179)

-   The following documentation topics are new:
    -   [Developing IPsec-Compatible Callout Drivers](developing-ipsec-compatible-callout-drivers.md)
    -   [Processing Classify Callouts Asynchronously](processing-classify-callouts-asynchronously.md)
-   The following topics contain additional updates:
    [Processing Notify Callouts](processing-notify-callouts.md)
    [Stream Inspection](stream-inspection.md)
    [**FwpsFlowAssociateContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551165)
    [**FwpsFlowRemoveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551169)
    [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890)
    [*notifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff568803)
    [**FWPS\_CALLOUT0**](https://msdn.microsoft.com/library/windows/hardware/ff551224)
    [**FWPS\_INCOMING\_METADATA\_VALUES0**](https://msdn.microsoft.com/library/windows/hardware/ff552397)

 

 





