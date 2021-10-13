---
title: OID_WWAN_PIN_EX2
description: OID_WWAN_PIN_EX2 accesses a UICC linear fixed or cyclic file, the structure type of which is WwanUiccFileStructureCyclic or WwanUiccFileStructureLinear.
ms.date: 04/10/2019
keywords: 
- OID_WWAN_PIN_EX2 Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID_WWAN_PIN_EX2

OID_WWAN_PIN_EX2 sets or returns expanded information related to Personal Identification Numbers (PINs). OID_WWAN_PIN_EX2 is similar to [OID_WWAN_PIN_EX](oid-wwan-pin-ex.md), but extends it to support multi-app UICC cards.

Query payloads contain an [**NDIS_WWAN_PIN_APP**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_app) structure specifying the target application ID whose PIN is being queried. Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_PIN_INFO](ndis-status-wwan-pin-info.md) status notification containing an [**NDIS_WWAN_PIN_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_info) structure that describes the PIN for the application. 

Set payloads contain an [**NDIS_WWAN_SET_PIN_EX2**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_pin_ex2) structure specifying the PIN action to take for the application. Miniport drivers must process Set requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_PIN_INFO](ndis-status-wwan-pin-info.md) status notification containing an [**NDIS_WWAN_PIN_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_info) structure that describes the PIN state for the application.

## Remarks

Only single verification-capable UICCs are supported. Multi-verification-capable UICCs that support more than one application PIN are not supported. One application PIN (PIN1) is assigned to all ADFs/DFs and files on the UICC. However, each application can specify a local PIN (PIN2) as a level 2 user verification requirement, resulting in the need for additional validation for every access command. This scenario is what OID_WWAN_PIN_EX2 supports.

Just like [OID_WWAN_PIN_EX](oid-wwan-pin-ex.md), with OID_WWAN_PIN_EX2 the device only reports one PIN at a time. If multiple PINs are enabled and reporting multiple PINs is enabled, then miniport drivers must report PIN1 first. For example, if subsidy lock reporting is enabled and the SIM's PIN1 is enabled, then the subsidy lock PIN should be reported in a subsequent query request only after PIN1 is specified by setting the **PinSize** to zero (0). In this case, a Set request is similar to a Query and returns the state of the PIN referenced. This is fully aligned to the behavior of the VERIFY command as specified in Section 11.1.9 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594).

For more information about usage of this OID, see [MB UICC application and file system access](mb-uicc-application-and-file-system-access.md).

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB UICC application and file system access](mb-uicc-application-and-file-system-access.md)

[NDIS_STATUS_WWAN_PIN_INFO](ndis-status-wwan-pin-info.md)

[**NDIS_WWAN_PIN_APP**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_app)

[**NDIS_WWAN_SET_PIN_EX2**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_pin_ex2)

[**NDIS_WWAN_PIN_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_info)
