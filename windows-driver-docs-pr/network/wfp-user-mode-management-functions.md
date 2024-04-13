---
title: WFP user mode management functions
description: This topic describes WFP user mode management functions.
keywords:
- WFP user mode management functions network drivers
ms.date: 11/07/2017
---

# WFP user mode management functions

The semantics of the Windows Filtering Platform user-mode management functions are exactly the same when called from a callout driver as when called from a user-mode application, except that the return type is an **NTSTATUS** code instead of a Win32 error code. 

These functions are documented in the [Management Functions](/windows/desktop/FWP/fwp-mgmt-functions) section of the user-mode [WFP Functions](/windows/desktop/FWP/fwp-functions) documentation. 

> [!NOTE]
> The kernel-mode version of each function is defined in fwpmk.h. The user-mode version of each function is defined in fwpmu.h.
 
Callers of all of these functions except [FwpmFreeMemory0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfreememory0) must be running at IRQL = PASSIVE_LEVEL. Callers of **FwpmFreeMemory0** must be running at IRQL <= DISPATCH_LEVEL.

## Callout Management

- [FwpmCalloutAdd0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutadd0) 
- [FwpmCalloutCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutcreateenumhandle0) 
- [FwpmCalloutDeleteById0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutdeletebyid0) 
- [FwpmCalloutDeleteByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutdeletebykey0) 
- [FwpmCalloutDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutdestroyenumhandle0) 
- [FwpmCalloutEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutenum0) 
- [FwpmCalloutGetById0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutgetbyid0) 
- [FwpmCalloutGetByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutgetbykey0) 
- [FwpmCalloutGetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutgetsecurityinfobykey0) 
- [FwpmCalloutSetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmcalloutsetsecurityinfobykey0) 

## Connection Object Management

- [FwpmConnectionCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmconnectioncreateenumhandle0) 
- [FwpmConnectionDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmconnectiondestroyenumhandle0) 
- [FwpmConnectionEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmconnectionenum0) 
- [FwpmConnectionGetById0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmconnectiongetbyid0) 
- [FwpmConnectionGetSecurityInfo0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmconnectiongetsecurityinfo0) 
- [FwpmConnectionSetSecurityInfo0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmconnectionsetsecurityinfo0) 

## Event Management

- [FwpmNetEventCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmneteventcreateenumhandle0) 
- [FwpmNetEventDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmneteventdestroyenumhandle0) 
- FwpmNetEventEnum:
    - [FwpmNetEventEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmneteventenum0) (Windows Vista)
    - [FwpmNetEventEnum1](/windows/win32/api/fwpmu/nf-fwpmu-fwpmneteventenum1) (Windows 7)
    - [FwpmNetEventEnum2](/windows/win32/api/fwpmu/nf-fwpmu-fwpmneteventenum2) (Windows 8)
- [FwpmNetEventsGetSecurityInfo0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmneteventsgetsecurityinfo0) 
- [FwpmNetEventsSetSecurityInfo0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmneteventssetsecurityinfo0) 

## Filter Management

- [FwpmFilterAdd0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfilteradd0) 
- [FwpmFilterCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfiltercreateenumhandle0) 
- [FwpmFilterDeleteById0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfilterdeletebyid0) 
- [FwpmFilterDeleteByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfilterdeletebykey0) 
- [FwpmFilterDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfilterdestroyenumhandle0) 
- [FwpmFilterEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfilterenum0) 
- [FwpmFilterGetById0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfiltergetbyid0) 
- [FwpmFilterGetByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfiltergetbykey0) 
- [FwpmFilterGetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfiltergetsecurityinfobykey0) 
- [FwpmFilterSetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmfiltersetsecurityinfobykey0) 

## Layer Management

- [FwpmLayerCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmlayercreateenumhandle0) 
- [FwpmLayerDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmlayerdestroyenumhandle0) 
- [FwpmLayerEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmlayerenum0) 
- [FwpmLayerGetById0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmlayergetbyid0) 
- [FwpmLayerGetByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmlayergetbykey0) 
- [FwpmLayerGetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmlayergetsecurityinfobykey0) 
- [FwpmLayerSetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmlayersetsecurityinfobykey0) 

## Provider Context Management

- [FwpmProviderContextAdd:
    - [FwpmProviderContextAdd0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextadd0) (Windows Vista)
    - [FwpmProviderContextAdd1](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextadd1) (Windows 7)
    - [FwpmProviderContextAdd2](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextadd2) (Windows 8)
- [FwpmProviderContextCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextcreateenumhandle0) 
- [FwpmProviderContextDeleteById0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextdeletebyid0) 
- [FwpmProviderContextDeleteByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextdeletebykey0) 
- [FwpmProviderContextDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextdestroyenumhandle0) 
- FwpmProviderContextEnum:
    - [FwpmProviderContextEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextenum0) (Windows Vista)
    - [FwpmProviderContextEnum1](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextenum1) (Windows 7)
    - [FwpmProviderContextEnum2](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextenum2) (Windows 8)
- FwpmProviderContextGetById:
    - [FwpmProviderContextGetById0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid0) (Windows Vista)
    - [FwpmProviderContextGetById1](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid1) (Windows 7)
    - [FwpmProviderContextGetById2](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbyid2) (Windows 8)
- FwpmProviderContextGetByKey:
    - [FwpmProviderContextGetByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey0) (Windows Vista)
    - [FwpmProviderContextGetByKey1](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey1) (Windows 7)
    - [FwpmProviderContextGetByKey2](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetbykey2) (Windows 8)
- [FwpmProviderContextGetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextgetsecurityinfobykey0) 
- [FwpmProviderContextSetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercontextsetsecurityinfobykey0) 

## Provider Management

- [FwpmProviderAdd0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovideradd0) 
- [FwpmProviderCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidercreateenumhandle0) 
- [FwpmProviderDeleteByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmproviderdeletebykey0) 
- [FwpmProviderDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmproviderdestroyenumhandle0) 
- [FwpmProviderEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmproviderenum0) 
- [FwpmProviderGetByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidergetbykey0) 
- [FwpmProviderGetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidergetsecurityinfobykey0) 
- [FwpmProviderSetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmprovidersetsecurityinfobykey0) 

## Session Management

- [FwpmEngineClose0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmengineclose0) 
- [FwpmEngineGetOption0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmenginegetoption0) 
- [FwpmEngineGetSecurityInfo0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmenginegetsecurityinfo0) 
- [FwpmEngineOpen0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmengineopen0) 
- [FwpmEngineSetOption0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmenginesetoption0) 
- [FwpmEngineSetSecurityInfo0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmenginesetsecurityinfo0) 
- [FwpmSessionCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsessioncreateenumhandle0) 
- [FwpmSessionDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsessiondestroyenumhandle0) 
- [FwpmSessionEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsessionenum0) 

## Sublayer Management

- [FwpmSubLayerAdd0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsublayeradd0) 
- [FwpmSubLayerCreateEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsublayercreateenumhandle0) 
- [FwpmSubLayerDeleteByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsublayerdeletebykey0) 
- [FwpmSubLayerDestroyEnumHandle0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsublayerdestroyenumhandle0) 
- [FwpmSubLayerEnum0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsublayerenum0) 
- [FwpmSubLayerGetByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsublayergetbykey0) 
- [FwpmSubLayerGetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsublayergetsecurityinfobykey0) 
- [FwpmSubLayerSetSecurityInfoByKey0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmsublayersetsecurityinfobykey0) 

## Transaction Management

- [FwpmTransactionAbort0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmtransactionabort0) 
- [FwpmTransactionBegin0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmtransactionbegin0) 
- [FwpmTransactionCommit0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmtransactioncommit0) 

## vSwitch Management

- [FwpmvSwitchEventsGetSecurityInfo0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmvswitcheventsgetsecurityinfo0) 
- [FwpmvSwitchEventsSetSecurityInfo0](/windows/win32/api/fwpmu/nf-fwpmu-fwpmvswitcheventssetsecurityinfo0)
