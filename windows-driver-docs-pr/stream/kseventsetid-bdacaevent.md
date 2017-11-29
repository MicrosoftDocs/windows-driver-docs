---
title: KSEVENTSETID\_BdaCAEvent
description: KSEVENTSETID\_BdaCAEvent
ms.assetid: e748a8a1-9aa4-41da-8cc2-02beb89a8887
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSEVENTSETID\_BdaCAEvent


## <span id="ddk_kseventsetid_bdacaevent_ks"></span><span id="DDK_KSEVENTSETID_BDACAEVENT_KS"></span>


KSEVENTSETID\_BdaCAEvent is the BDA conditional access (CA) event set. It is used to notify CA plugins of changes in status of CA modules and smart card readers associated with Entitlement Control Message (ECM) map nodes. This event set can also notify CA plugins about the existence of user interface (UI) that those plugins should retrieve and display and about changes in program information.

The following events are available:

<span id="KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED"></span><span id="ksevent_bda_program_flow_status_changed"></span>[**KSEVENT\_BDA\_PROGRAM\_FLOW\_STATUS\_CHANGED**](ksevent-bda-program-flow-status-changed.md)  
Notifies of a status change in program information.

<span id="KSEVENT_BDA_CA_MODULE_STATUS_CHANGED"></span><span id="ksevent_bda_ca_module_status_changed"></span>[**KSEVENT\_BDA\_CA\_MODULE\_STATUS\_CHANGED**](ksevent-bda-ca-module-status-changed.md)  
Notifies of a status change on the CA module associated with an ECM map node.

<span id="KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED"></span><span id="ksevent_bda_ca_smart_card_status_changed"></span>[**KSEVENT\_BDA\_CA\_SMART\_CARD\_STATUS\_CHANGED**](ksevent-bda-ca-smart-card-status-changed.md)  
Notifies of a status change on the smart card reader associated with an ECM map node.

<span id="KSEVENT_BDA_CA_MODULE_UI_REQUESTED"></span><span id="ksevent_bda_ca_module_ui_requested"></span>[**KSEVENT\_BDA\_CA\_MODULE\_UI\_REQUESTED**](ksevent-bda-ca-module-ui-requested.md)  
Notifies of the existence of UI that a CA plugin can retrieve and display.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Each event in this event set corresponds to a property in the KSPROPSETID\_BdaCA property set. CA plugins request to be notified when events in a BDA component occur. BDA minidrivers signal events in this event set to notify CA plugins. Those CA plugins then query corresponding properties in KSPROPSETID\_BdaCA. BDA minidrivers signal these events either whenever a significant status change occurs or to interact with a user. BDA minidrivers interact with a user, for example, to present a message to the user or to negotiate a transaction with a user. A significant status change is, for example, when a user removes a smart card from the smart card reader.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[KSPROPSETID\_BdaCA](kspropsetid-bdaca.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENTSETID_BdaCAEvent%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




