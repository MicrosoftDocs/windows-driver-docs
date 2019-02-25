---
title: WFP Changes for Windows 8
description: WFP Changes for Windows 8
ms.assetid: B83EC5A5-6169-49AB-A7EC-F2078AA0735E
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
    - [**FwpsCalloutRegister2**](https://msdn.microsoft.com/library/windows/hardware/hh439576)
    - [**FwpsFlowAbort0**](https://msdn.microsoft.com/library/windows/hardware/hh439582)
    - [**FwpsInjectMacReceiveAsync0**](https://msdn.microsoft.com/library/windows/hardware/hh439588)
    - [**FwpsInjectMacSendAsync0**](https://msdn.microsoft.com/library/windows/hardware/hh439593)
    - [**FwpsNetBufferListAssociateContext1**](https://msdn.microsoft.com/library/windows/hardware/hh439674)
    - [**FwpsQueryConnectionRedirectState0**](https://msdn.microsoft.com/library/windows/hardware/hh439677)
    - [**FwpsRedirectHandleCreate0**](https://msdn.microsoft.com/library/windows/hardware/hh439681)
    - [**FwpsRedirectHandleDestroy0**](https://msdn.microsoft.com/library/windows/hardware/hh439684)
    - [**FwpsvSwitchEventsSubscribe0**](https://msdn.microsoft.com/library/windows/hardware/hh439687)
    - [**FwpsvSwitchEventsUnsubscribe0**](https://msdn.microsoft.com/library/windows/hardware/hh439691)
    - [**FwpsvSwitchNotifyComplete0**](https://msdn.microsoft.com/library/windows/hardware/hh439695)
-   New callback functions:
    - [*FWPS\_CALLOUT\_CLASSIFY\_FN2*](https://msdn.microsoft.com/library/windows/hardware/hh439337)
    - [*FWPS\_CALLOUT\_NOTIFY\_FN2*](https://msdn.microsoft.com/library/windows/hardware/hh439963)
    - [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](https://msdn.microsoft.com/library/windows/hardware/hh451260)
    - [*FWPS\_VSWITCH\_FILTER\_ENGINE\_REORDER\_CALLBACK0*](https://msdn.microsoft.com/library/windows/hardware/hh451267)
    - [*FWPS\_VSWITCH\_INTERFACE\_EVENT\_CALLBACK0*](https://msdn.microsoft.com/library/windows/hardware/hh451269)
    - [*FWPS\_VSWITCH\_LIFETIME\_EVENT\_CALLBACK0*](https://msdn.microsoft.com/library/windows/hardware/hh451271)
    - [*FWPS\_VSWITCH\_POLICY\_EVENT\_CALLBACK0*](https://msdn.microsoft.com/library/windows/hardware/hh451272)
    - [*FWPS\_VSWITCH\_PORT\_EVENT\_CALLBACK0*](https://msdn.microsoft.com/library/windows/hardware/hh451276)
    - [*FWPS\_VSWITCH\_RUNTIME\_STATE\_RESTORE\_CALLBACK0*](https://msdn.microsoft.com/library/windows/hardware/hh451281)
    - [*FWPS\_VSWITCH\_RUNTIME\_STATE\_SAVE\_CALLBACK0*](https://msdn.microsoft.com/library/windows/hardware/hh451286)
-   New structures:
    - [**FWPS\_FILTER2**](https://msdn.microsoft.com/library/windows/hardware/hh439768)
    - [**FWPS\_VSWITCH\_EVENT\_DISPATCH\_TABLE0**](https://msdn.microsoft.com/library/windows/hardware/hh451263)
-   New enumerations:
    - [**FWPS\_CONNECTION\_REDIRECT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh439704)
    - [**FWPS\_FIELDS\_EGRESS\_VSWITCH\_ETHERNET**](https://msdn.microsoft.com/library/windows/hardware/hh439709)
    - [**FWPS\_FIELDS\_EGRESS\_VSWITCH\_TRANSPORT\_V4**](https://msdn.microsoft.com/library/windows/hardware/hh439715)
    - [**FWPS\_FIELDS\_EGRESS\_VSWITCH\_TRANSPORT\_V6**](https://msdn.microsoft.com/library/windows/hardware/hh439721)
    - [**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_NATIVE**](https://msdn.microsoft.com/library/windows/hardware/hh439728)
    - [**FWPS\_FIELDS\_INGRESS\_VSWITCH\_ETHERNET**](https://msdn.microsoft.com/library/windows/hardware/hh439733)
    - [**FWPS\_FIELDS\_INGRESS\_VSWITCH\_TRANSPORT\_V4**](https://msdn.microsoft.com/library/windows/hardware/hh439738)
    - [**FWPS\_FIELDS\_INGRESS\_VSWITCH\_TRANSPORT\_V6**](https://msdn.microsoft.com/library/windows/hardware/hh439745)
    - [**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_NATIVE**](https://msdn.microsoft.com/library/windows/hardware/hh439757)
    - [**FWPS\_VSWITCH\_EVENT\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh451265)
-   Renamed enumerations:
    - [**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_ETHERNET**](https://msdn.microsoft.com/library/windows/hardware/ff551291) (was **FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_802\_3**)
    - [**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_ETHERNET**](https://msdn.microsoft.com/library/windows/hardware/ff551334) (was **FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_802\_3**)

 

 





