---
title: KSPROPSETID\_BdaCA
description: KSPROPSETID\_BdaCA
ms.assetid: 2ceb54ff-f111-4cf7-8c8e-f9a4dce42d4e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Properties in this property set correspond to events in the KSEVENTSETID\_BdaCAEvent event set. BDA minidrivers signal events in this event set to notify CA plugins. Those CA plugins then query corresponding properties in KSPROPSETID\_BdaCA. BDA minidrivers signal these events either whenever a significant status change occurs or to interact with a user. BDA minidrivers interact with a user, for example, to present a message to the user or to negotiate a transaction with a user. A significant status change is, for example, when a user removes a smart card from the smart card reader.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[KSEVENTSETID\_BdaCAEvent](kseventsetid-bdacaevent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaCA%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




