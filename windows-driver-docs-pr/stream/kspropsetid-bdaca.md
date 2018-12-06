---
title: KSPROPSETID\_BdaCA
description: KSPROPSETID\_BdaCA
ms.assetid: 2ceb54ff-f111-4cf7-8c8e-f9a4dce42d4e
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_BdaCA


## <span id="ddk_kspropsetid_bdaca_ks"></span><span id="DDK_KSPROPSETID_BDACA_KS"></span>


KSPROPSETID\_BdaCA is the BDA conditional access (CA) property set. It is used to query Entitlement Control Message (ECM) map nodes for status of those nodes and for status of associated CA modules and smart card readers. This property set can also query for user interface (UI) that CA plugins can display and control access to programs processed through an ECM map node.

The following properties are available:

<span id="KSPROPERTY_BDA_ECM_MAP_STATUS"></span><span id="ksproperty_bda_ecm_map_status"></span>[**KSPROPERTY\_BDA\_ECM\_MAP\_STATUS**](ksproperty-bda-ecm-map-status.md)  
Returns status on an ECM map node.

<span id="KSPROPERTY_BDA_CA_MODULE_STATUS"></span><span id="ksproperty_bda_ca_module_status"></span>[**KSPROPERTY\_BDA\_CA\_MODULE\_STATUS**](ksproperty-bda-ca-module-status.md)  
Returns status on the CA module associated with an ECM map node.

<span id="KSPROPERTY_BDA_CA_SMART_CARD_STATUS"></span><span id="ksproperty_bda_ca_smart_card_status"></span>[**KSPROPERTY\_BDA\_CA\_SMART\_CARD\_STATUS**](ksproperty-bda-ca-smart-card-status.md)  
Returns status on the smart card reader associated with an ECM map node.

<span id="KSPROPERTY_BDA_CA_MODULE_UI"></span><span id="ksproperty_bda_ca_module_ui"></span>[**KSPROPERTY\_BDA\_CA\_MODULE\_UI**](ksproperty-bda-ca-module-ui.md)  
Returns UI that a CA plugin can display.

<span id="KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS"></span><span id="ksproperty_bda_ca_set_program_pids"></span>[**KSPROPERTY\_BDA\_CA\_SET\_PROGRAM\_PIDS**](ksproperty-bda-ca-set-program-pids.md)  
Sets the list of packet identifiers in a particular program.

<span id="KSPROPERTY_BDA_CA_REMOVE_PROGRAM"></span><span id="ksproperty_bda_ca_remove_program"></span>[**KSPROPERTY\_BDA\_CA\_REMOVE\_PROGRAM**](ksproperty-bda-ca-remove-program.md)  
Prevents access to a specific program.

### Comments

Properties in this property set correspond to events in the KSEVENTSETID\_BdaCAEvent event set. BDA minidrivers signal events in this event set to notify CA plugins. Those CA plugins then query corresponding properties in KSPROPSETID\_BdaCA. BDA minidrivers signal these events either whenever a significant status change occurs or to interact with a user. BDA minidrivers interact with a user, for example, to present a message to the user or to negotiate a transaction with a user. A significant status change is, for example, when a user removes a smart card from the smart card reader.

### See Also

[KSEVENTSETID\_BdaCAEvent](kseventsetid-bdacaevent.md)

 

 





