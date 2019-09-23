---
title: WFP user mode management functions
description: This topic describes WFP user mode management functions.
ms.assetid: 14accd49-5b96-40]()e6-b9d7-6638a4e5c2dc
keywords:
- WFP user mode management functions network drivers
ms.date: 11/07/2017
ms.localizationpriority: medium
---

# WFP user mode management functions

The semantics of the Windows Filtering Platform user-mode management functions are exactly the same when called from a callout driver as when called from a user-mode application, except that the return type is an **NTSTATUS** code instead of a Win32 error code. 

These functions are documented in the [Management Functions](https://docs.microsoft.com/windows/desktop/FWP/fwp-mgmt-functions) section of the user-mode [WFP Functions](https://docs.microsoft.com/windows/desktop/FWP/fwp-functions) documentation. 

> [!NOTE]
> The kernel-mode version of each function is defined in fwpmk.h. The user-mode version of each function is defined in fwpmu.h.
 
Callers of all of these functions except [FwpmFreeMemory0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfreememory0) must be running at IRQL = PASSIVE_LEVEL. Callers of **FwpmFreeMemory0** must be running at IRQL <= DISPATCH_LEVEL.

## Callout Management

- [FwpmCalloutAdd0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutadd0) 
- [FwpmCalloutCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutcreateenumhandle0) 
- [FwpmCalloutDeleteById0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutdeletebyid0) 
- [FwpmCalloutDeleteByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutdeletebykey0) 
- [FwpmCalloutDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutdestroyenumhandle0) 
- [FwpmCalloutEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutenum0) 
- [FwpmCalloutGetById0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutgetbyid0) 
- [FwpmCalloutGetByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutgetbykey0) 
- [FwpmCalloutGetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutgetsecurityinfobykey0) 
- [FwpmCalloutSetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmcalloutsetsecurityinfobykey0) 

## Connection Object Management

- [FwpmConnectionCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmconnectioncreateenumhandle0) 
- [FwpmConnectionDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmconnectiondestroyenumhandle0) 
- [FwpmConnectionEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmconnectionenum0) 
- [FwpmConnectionGetById0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmconnectiongetbyid0) 
- [FwpmConnectionGetSecurityInfo0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmconnectiongetsecurityinfo0) 
- [FwpmConnectionSetSecurityInfo0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmconnectionsetsecurityinfo0) 

## Event Management

- [FwpmNetEventCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventcreateenumhandle0) 
- [FwpmNetEventDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventdestroyenumhandle0) 
- FwpmNetEventEnum:
    - [FwpmNetEventEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventenum0) (Windows Vista)
    - [FwpmNetEventEnum1](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventenum1) (Windows 7)
    - [FwpmNetEventEnum2](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventenum2) (Windows 8)
- [FwpmNetEventsGetSecurityInfo0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventsgetsecurityinfo0) 
- [FwpmNetEventsSetSecurityInfo0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmneteventssetsecurityinfo0) 

## Filter Management

- [FwpmFilterAdd0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfilteradd0) 
- [FwpmFilterCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfiltercreateenumhandle0) 
- [FwpmFilterDeleteById0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfilterdeletebyid0) 
- [FwpmFilterDeleteByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfilterdeletebykey0) 
- [FwpmFilterDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfilterdestroyenumhandle0) 
- [FwpmFilterEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfilterenum0) 
- [FwpmFilterGetById0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfiltergetbyid0) 
- [FwpmFilterGetByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfiltergetbykey0) 
- [FwpmFilterGetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfiltergetsecurityinfobykey0) 
- [FwpmFilterSetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmfiltersetsecurityinfobykey0) 

## Layer Management

- [FwpmLayerCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmlayercreateenumhandle0) 
- [FwpmLayerDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmlayerdestroyenumhandle0) 
- [FwpmLayerEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmlayerenum0) 
- [FwpmLayerGetById0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmlayergetbyid0) 
- [FwpmLayerGetByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmlayergetbykey0) 
- [FwpmLayerGetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmlayergetsecurityinfobykey0) 
- [FwpmLayerSetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmlayersetsecurityinfobykey0) 

## Provider Context Management

- [FwpmProviderContextAdd:
    - [FwpmProviderContextAdd0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextadd0) (Windows Vista)
    - [FwpmProviderContextAdd1](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextadd1) (Windows 7)
    - [FwpmProviderContextAdd2](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextadd2) (Windows 8)
- [FwpmProviderContextCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextcreateenumhandle0) 
- [FwpmProviderContextDeleteById0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextdeletebyid0) 
- [FwpmProviderContextDeleteByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextdeletebykey0) 
- [FwpmProviderContextDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextdestroyenumhandle0) 
- FwpmProviderContextEnum:
    - [FwpmProviderContextEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextenum0) (Windows Vista)
    - [FwpmProviderContextEnum1](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextenum1) (Windows 7)
    - [FwpmProviderContextEnum2](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextenum2) (Windows 8)
- FwpmProviderContextGetById:
    - [FwpmProviderContextGetById0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid0) (Windows Vista)
    - [FwpmProviderContextGetById1](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid1) (Windows 7)
    - [FwpmProviderContextGetById2](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid2) (Windows 8)
- FwpmProviderContextGetByKey:
    - [FwpmProviderContextGetByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey0) (Windows Vista)
    - [FwpmProviderContextGetByKey1](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey1) (Windows 7)
    - [FwpmProviderContextGetByKey2](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey2) (Windows 8)
- [FwpmProviderContextGetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetsecurityinfobykey0) 
- [FwpmProviderContextSetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercontextsetsecurityinfobykey0) 

## Provider Management

- [FwpmProviderAdd0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovideradd0) 
- [FwpmProviderCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidercreateenumhandle0) 
- [FwpmProviderDeleteByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmproviderdeletebykey0) 
- [FwpmProviderDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmproviderdestroyenumhandle0) 
- [FwpmProviderEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmproviderenum0) 
- [FwpmProviderGetByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidergetbykey0) 
- [FwpmProviderGetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidergetsecurityinfobykey0) 
- [FwpmProviderSetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmprovidersetsecurityinfobykey0) 

## Session Management

- [FwpmEngineClose0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmengineclose0) 
- [FwpmEngineGetOption0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmenginegetoption0) 
- [FwpmEngineGetSecurityInfo0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmenginegetsecurityinfo0) 
- [FwpmEngineOpen0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmengineopen0) 
- [FwpmEngineSetOption0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmenginesetoption0) 
- [FwpmEngineSetSecurityInfo0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmenginesetsecurityinfo0) 
- [FwpmSessionCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsessioncreateenumhandle0) 
- [FwpmSessionDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsessiondestroyenumhandle0) 
- [FwpmSessionEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsessionenum0) 

## Sublayer Management

- [FwpmSubLayerAdd0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsublayeradd0) 
- [FwpmSubLayerCreateEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsublayercreateenumhandle0) 
- [FwpmSubLayerDeleteByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsublayerdeletebykey0) 
- [FwpmSubLayerDestroyEnumHandle0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsublayerdestroyenumhandle0) 
- [FwpmSubLayerEnum0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsublayerenum0) 
- [FwpmSubLayerGetByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsublayergetbykey0) 
- [FwpmSubLayerGetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsublayergetsecurityinfobykey0) 
- [FwpmSubLayerSetSecurityInfoByKey0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmsublayersetsecurityinfobykey0) 

## Transaction Management

- [FwpmTransactionAbort0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmtransactionabort0) 
- [FwpmTransactionBegin0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmtransactionbegin0) 
- [FwpmTransactionCommit0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmtransactioncommit0) 

## vSwitch Management

- [FwpmvSwitchEventsGetSecurityInfo0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmvswitcheventsgetsecurityinfo0) 
- [FwpmvSwitchEventsSetSecurityInfo0](https://docs.microsoft.com/windows/desktop/api/fwpmu/nf-fwpmu-fwpmvswitcheventssetsecurityinfo0) 

