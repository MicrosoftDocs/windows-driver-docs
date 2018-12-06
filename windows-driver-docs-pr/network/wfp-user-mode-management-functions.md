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

These functions are documented in the [Management Functions](https://msdn.microsoft.com/library/windows/hardware/aa364943) section of the user-mode [WFP Functions](https://msdn.microsoft.com/library/windows/hardware/aa364931) documentation. 

> [!NOTE]
> The kernel-mode version of each function is defined in fwpmk.h. The user-mode version of each function is defined in fwpmu.h.
 
Callers of all of these functions except [FwpmFreeMemory0](https://msdn.microsoft.com/library/windows/hardware/aa364071) must be running at IRQL = PASSIVE_LEVEL. Callers of **FwpmFreeMemory0** must be running at IRQL <= DISPATCH_LEVEL.

## Callout Management

- [FwpmCalloutAdd0](https://msdn.microsoft.com/library/windows/hardware/aa364010) 
- [FwpmCalloutCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364012) 
- [FwpmCalloutDeleteById0](https://msdn.microsoft.com/library/windows/hardware/aa364013) 
- [FwpmCalloutDeleteByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364016) 
- [FwpmCalloutDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364017) 
- [FwpmCalloutEnum0](https://msdn.microsoft.com/library/windows/hardware/aa364020) 
- [FwpmCalloutGetById0](https://msdn.microsoft.com/library/windows/hardware/aa364022) 
- [FwpmCalloutGetByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364024) 
- [FwpmCalloutGetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364026) 
- [FwpmCalloutSetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364027) 

## Connection Object Management

- [FwpmConnectionCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/hh447303) 
- [FwpmConnectionDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/hh447304) 
- [FwpmConnectionEnum0](https://msdn.microsoft.com/library/windows/hardware/hh447305) 
- [FwpmConnectionGetById0](https://msdn.microsoft.com/library/windows/hardware/hh447307) 
- [FwpmConnectionGetSecurityInfo0](https://msdn.microsoft.com/library/windows/hardware/hh447308) 
- [FwpmConnectionSetSecurityInfo0](https://msdn.microsoft.com/library/windows/hardware/hh447309) 

## Event Management

- [FwpmNetEventCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364175) 
- [FwpmNetEventDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364176) 
- FwpmNetEventEnum:
    - [FwpmNetEventEnum0](https://msdn.microsoft.com/library/windows/hardware/aa364177) (Windows Vista)
    - [FwpmNetEventEnum1](https://msdn.microsoft.com/library/windows/hardware/dd744936) (Windows 7)
    - [FwpmNetEventEnum2](https://msdn.microsoft.com/library/windows/hardware/hh447314) (Windows 8)
- [FwpmNetEventsGetSecurityInfo0](https://msdn.microsoft.com/library/windows/hardware/aa814094) 
- [FwpmNetEventsSetSecurityInfo0](https://msdn.microsoft.com/library/windows/hardware/aa814095) 

## Filter Management

- [FwpmFilterAdd0](https://msdn.microsoft.com/library/windows/hardware/aa364046) 
- [FwpmFilterCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364048) 
- [FwpmFilterDeleteById0](https://msdn.microsoft.com/library/windows/hardware/aa364050) 
- [FwpmFilterDeleteByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364053) 
- [FwpmFilterDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364055) 
- [FwpmFilterEnum0](https://msdn.microsoft.com/library/windows/hardware/aa364058) 
- [FwpmFilterGetById0](https://msdn.microsoft.com/library/windows/hardware/aa364059) 
- [FwpmFilterGetByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364060) 
- [FwpmFilterGetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364061) 
- [FwpmFilterSetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364064) 

## Layer Management

- [FwpmLayerCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364167) 
- [FwpmLayerDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364168) 
- [FwpmLayerEnum0](https://msdn.microsoft.com/library/windows/hardware/aa364169) 
- [FwpmLayerGetById0](https://msdn.microsoft.com/library/windows/hardware/aa364170) 
- [FwpmLayerGetByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364171) 
- [FwpmLayerGetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364172) 
- [FwpmLayerSetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364174) 

## Provider Context Management

- [FwpmProviderContextAdd:
    - [FwpmProviderContextAdd0](https://msdn.microsoft.com/library/windows/hardware/aa364181) (Windows Vista)
    - [FwpmProviderContextAdd1](https://msdn.microsoft.com/library/windows/hardware/dd744940) (Windows 7)
    - [FwpmProviderContextAdd2](https://msdn.microsoft.com/library/windows/hardware/hh447316) (Windows 8)
- [FwpmProviderContextCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364182) 
- [FwpmProviderContextDeleteById0](https://msdn.microsoft.com/library/windows/hardware/aa364183) 
- [FwpmProviderContextDeleteByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364184) 
- [FwpmProviderContextDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364185) 
- FwpmProviderContextEnum:
    - [FwpmProviderContextEnum0](https://msdn.microsoft.com/library/windows/hardware/aa364186) (Windows Vista)
    - [FwpmProviderContextEnum1](https://msdn.microsoft.com/library/windows/hardware/dd744941) (Windows 7)
    - [FwpmProviderContextEnum2](https://msdn.microsoft.com/library/windows/hardware/hh447332) (Windows 8)
- FwpmProviderContextGetById:
    - [FwpmProviderContextGetById0](https://msdn.microsoft.com/library/windows/hardware/aa364187) (Windows Vista)
    - [FwpmProviderContextGetById1](https://msdn.microsoft.com/library/windows/hardware/dd744942) (Windows 7)
    - [FwpmProviderContextGetById2](https://msdn.microsoft.com/library/windows/hardware/hh447335) (Windows 8)
- FwpmProviderContextGetByKey:
    - [FwpmProviderContextGetByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364188) (Windows Vista)
    - [FwpmProviderContextGetByKey1](https://msdn.microsoft.com/library/windows/hardware/dd744943) (Windows 7)
    - [FwpmProviderContextGetByKey2](https://msdn.microsoft.com/library/windows/hardware/hh447337) (Windows 8)
- [FwpmProviderContextGetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364189) 
- [FwpmProviderContextSetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364190) 

## Provider Management

- [FwpmProviderAdd0](https://msdn.microsoft.com/library/windows/hardware/aa364180) 
- [FwpmProviderCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364194) 
- [FwpmProviderDeleteByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364195) 
- [FwpmProviderDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364196) 
- [FwpmProviderEnum0](https://msdn.microsoft.com/library/windows/hardware/aa364197) 
- [FwpmProviderGetByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364198) 
- [FwpmProviderGetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364199) 
- [FwpmProviderSetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364200) 

## Session Management

- [FwpmEngineClose0](https://msdn.microsoft.com/library/windows/hardware/aa364034) 
- [FwpmEngineGetOption0](https://msdn.microsoft.com/library/windows/hardware/aa364035) 
- [FwpmEngineGetSecurityInfo0](https://msdn.microsoft.com/library/windows/hardware/aa364038) 
- [FwpmEngineOpen0](https://msdn.microsoft.com/library/windows/hardware/aa364040) 
- [FwpmEngineSetOption0](https://msdn.microsoft.com/library/windows/hardware/aa364042) 
- [FwpmEngineSetSecurityInfo0](https://msdn.microsoft.com/library/windows/hardware/aa364044) 
- [FwpmSessionCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364204) 
- [FwpmSessionDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364205) 
- [FwpmSessionEnum0](https://msdn.microsoft.com/library/windows/hardware/aa364206) 

## Sublayer Management

- [FwpmSubLayerAdd0](https://msdn.microsoft.com/library/windows/hardware/aa364207) 
- [FwpmSubLayerCreateEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364208) 
- [FwpmSubLayerDeleteByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364209) 
- [FwpmSubLayerDestroyEnumHandle0](https://msdn.microsoft.com/library/windows/hardware/aa364210) 
- [FwpmSubLayerEnum0](https://msdn.microsoft.com/library/windows/hardware/aa364211) 
- [FwpmSubLayerGetByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364212) 
- [FwpmSubLayerGetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364213) 
- [FwpmSubLayerSetSecurityInfoByKey0](https://msdn.microsoft.com/library/windows/hardware/aa364235) 

## Transaction Management

- [FwpmTransactionAbort0](https://msdn.microsoft.com/library/windows/hardware/aa364242) 
- [FwpmTransactionBegin0](https://msdn.microsoft.com/library/windows/hardware/aa364243) 
- [FwpmTransactionCommit0](https://msdn.microsoft.com/library/windows/hardware/aa364245) 

## vSwitch Management

- [FwpmvSwitchEventsGetSecurityInfo0](https://msdn.microsoft.com/library/windows/hardware/hh447339) 
- [FwpmvSwitchEventsSetSecurityInfo0](https://msdn.microsoft.com/library/windows/hardware/hh447341) 

