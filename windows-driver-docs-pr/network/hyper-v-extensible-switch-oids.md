---
title: Hyper-V Extensible Switch OIDs
description: This section describes Hyper-V Extensible Switch OIDs and their characteristics.
keywords: ["Hyper-V Extensible Switch OIDs", "Hyper-V Switch OIDs", "WDK Hyper-V Extensible Switch OIDs", "Hyper-V Extensible Switch object identifiers"]
ms.date: 04/24/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch OIDs

This section describes the Hyper-V extensible switch object identifiers (OIDs). These OIDs may be issued by either the extensible switch extension or a Hyper-V extensible switch extension.

The following table defines the characteristics of the extensible switch OIDs. The following abbreviations are used to specify the OIDs' characteristics in the table.

- Q  
The OID is used only in query requests.
- S  
The OID is used only in set requests.
- M  
The OID is used only in method requests. These requests could be issued for set or query operations.
- P  
The OID request is issued by the protocol edge of the extensible switch. The extension can inspect the results of the OID request to obtain information about the extensible switch, its ports, or virtual network adapters connected to the ports.
- E  
The OID request is issued by an extension.

| Name                                                                                                 | Q | S | M | P | E |
|---                                                                                                   |---|---|---|---|---|
| [OID_SWITCH_FEATURE_STATUS_QUERY](./oid-switch-feature-status-query.md)      |   |   | X | X |   | 
| [OID_SWITCH_NIC_ARRAY](./oid-switch-nic-array.md)                 | X |   |   |   | X | 
| [OID_SWITCH_NIC_CONNECT](./oid-switch-nic-connect.md)               |   | X |   | X |   |
| [OID_SWITCH_NIC_CREATE](./oid-switch-nic-create.md)                |   | X |   | X |   |
| [OID_SWITCH_NIC_DELETE](./oid-switch-nic-delete.md)                |   | X |   | X |   |  
| [OID_SWITCH_NIC_DISCONNECT](./oid-switch-nic-disconnect.md)            |   | X |   | X |   | 
| [OID_SWITCH_NIC_REQUEST](./oid-switch-nic-request.md)               |   |   | X |   | X |   
| [OID_SWITCH_NIC_RESTORE](./oid-switch-nic-restore.md)               |   | X |   | X |   |   
| [OID_SWITCH_NIC_SAVE](./oid-switch-nic-save.md)                  | X |   |   | X |   |
| [OID_SWITCH_NIC_SAVE_COMPLETE](./oid-switch-nic-save-complete.md)         |   | X |   | X |   | 
| [OID_SWITCH_PARAMETERS](./oid-switch-parameters.md)                | X |   |   |   | X |
| [OID_SWITCH_PORT_ARRAY](./oid-switch-port-array.md)                | X |   |   |   | X | 
| [OID_SWITCH_PORT_CREATE](./oid-switch-port-create.md)               |   | X |   | X |   | 
| [OID_SWITCH_PORT_DELETE](./oid-switch-port-delete.md)               |   | X |   | X |   | 
| [OID_SWITCH_PORT_FEATURE_STATUS_QUERY](./oid-switch-port-feature-status-query.md) |   |   | X | X |   | 
| [OID_SWITCH_PORT_PROPERTY_ADD](./oid-switch-port-property-add.md)         |   | X |   | X |   |
| [OID_SWITCH_PORT_PROPERTY_DELETE](./oid-switch-port-property-delete.md)      |   | X |   | X |   |   
| [OID_SWITCH_PORT_PROPERTY_ENUM](./oid-switch-port-property-enum.md)        |   |   | X |   | X |   
| [OID_SWITCH_PORT_PROPERTY_UPDATE](./oid-switch-port-property-update.md)      |   | X |   | X |   | 
| [OID_SWITCH_PORT_TEARDOWN](./oid-switch-port-teardown.md)             |   | X |   | X |   |
| [OID_SWITCH_PROPERTY_ADD](./oid-switch-property-add.md)              |   | X |   | X |   | 
| [OID_SWITCH_PROPERTY_DELETE](./oid-switch-property-delete.md)           |   | X |   | X |   | 
| [OID_SWITCH_PROPERTY_ENUM](./oid-switch-property-enum.md)             |   |   | X |   | X |
| [OID_SWITCH_PROPERTY_UPDATE](./oid-switch-property-update.md)           |   | X |   | X |   |
