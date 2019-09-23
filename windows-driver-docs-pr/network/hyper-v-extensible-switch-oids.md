---
title: Hyper-V Extensible Switch OIDs
description: This section describes Hyper-V Extensible Switch OIDs and their characteristics.
keywords: ["Hyper-V Extensible Switch OIDs", "Hyper-V Switch OIDs", "WDK Hyper-V Extensible Switch OIDs", "Hyper-V Extensible Switch object identifiers"]
ms.assetid: A97C5BF0-7319-4BEE-ABF7-12B11CEAF3DB"
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
| [OID_SWITCH_FEATURE_STATUS_QUERY](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-feature-status-query)      |   |   | X | X |   | 
| [OID_SWITCH_NIC_ARRAY](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-array)                 | X |   |   |   | X | 
| [OID_SWITCH_NIC_CONNECT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-connect)               |   | X |   | X |   |
| [OID_SWITCH_NIC_CREATE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-create)                |   | X |   | X |   |
| [OID_SWITCH_NIC_DELETE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-delete)                |   | X |   | X |   |  
| [OID_SWITCH_NIC_DISCONNECT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-disconnect)            |   | X |   | X |   | 
| [OID_SWITCH_NIC_REQUEST](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-request)               |   |   | X |   | X |   
| [OID_SWITCH_NIC_RESTORE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-restore)               |   | X |   | X |   |   
| [OID_SWITCH_NIC_SAVE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-save)                  | X |   |   | X |   |
| [OID_SWITCH_NIC_SAVE_COMPLETE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-nic-save-complete)         |   | X |   | X |   | 
| [OID_SWITCH_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-parameters)                | X |   |   |   | X |
| [OID_SWITCH_PORT_ARRAY](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-array)                | X |   |   |   | X | 
| [OID_SWITCH_PORT_CREATE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-create)               |   | X |   | X |   | 
| [OID_SWITCH_PORT_DELETE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-delete)               |   | X |   | X |   | 
| [OID_SWITCH_PORT_FEATURE_STATUS_QUERY](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-feature-status-query) |   |   | X | X |   | 
| [OID_SWITCH_PORT_PROPERTY_ADD](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-property-add)         |   | X |   | X |   |
| [OID_SWITCH_PORT_PROPERTY_DELETE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-property-delete)      |   | X |   | X |   |   
| [OID_SWITCH_PORT_PROPERTY_ENUM](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-property-enum)        |   |   | X |   | X |   
| [OID_SWITCH_PORT_PROPERTY_UPDATE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-property-update)      |   | X |   | X |   | 
| [OID_SWITCH_PORT_TEARDOWN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-port-teardown)             |   | X |   | X |   |
| [OID_SWITCH_PROPERTY_ADD](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-property-add)              |   | X |   | X |   | 
| [OID_SWITCH_PROPERTY_DELETE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-property-delete)           |   | X |   | X |   | 
| [OID_SWITCH_PROPERTY_ENUM](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-property-enum)             |   |   | X |   | X |
| [OID_SWITCH_PROPERTY_UPDATE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-switch-property-update)           |   | X |   | X |   | 


