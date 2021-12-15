---
title: KSEVENTSETID_BdaCAEvent
description: KSEVENTSETID_BdaCAEvent is the BDA conditional access (CA) event set.
ms.date: 10/12/2021
---

# KSEVENTSETID_BdaCAEvent

**KSEVENTSETID_BdaCAEvent** is the BDA conditional access (CA) event set. It is used to notify CA plugins of changes in status of CA modules and smart card readers associated with Entitlement Control Message (ECM) map nodes. This event set can also notify CA plugins about the existence of user interface (UI) that those plugins should retrieve and display and about changes in program information.

The following events are available:

[**KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED**](ksevent-bda-program-flow-status-changed.md)  
Notifies of a status change in program information.

[**KSEVENT_BDA_CA_MODULE_STATUS_CHANGED**](ksevent-bda-ca-module-status-changed.md)  
Notifies of a status change on the CA module associated with an ECM map node.

[**KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED**](ksevent-bda-ca-smart-card-status-changed.md)  
Notifies of a status change on the smart card reader associated with an ECM map node.

[**KSEVENT_BDA_CA_MODULE_UI_REQUESTED**](ksevent-bda-ca-module-ui-requested.md)  
Notifies of the existence of UI that a CA plugin can retrieve and display.

## Comments

Each event in this event set corresponds to a property in the KSPROPSETID_BdaCA property set. CA plugins request to be notified when events in a BDA component occur. BDA minidrivers signal events in this event set to notify CA plugins. Those CA plugins then query corresponding properties in KSPROPSETID_BdaCA. BDA minidrivers signal these events either whenever a significant status change occurs or to interact with a user. BDA minidrivers interact with a user, for example, to present a message to the user or to negotiate a transaction with a user. A significant status change is, for example, when a user removes a smart card from the smart card reader.

## See also

[KSPROPSETID_BdaCA](kspropsetid-bdaca.md)
