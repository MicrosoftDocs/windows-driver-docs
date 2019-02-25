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
| [OID_SWITCH_FEATURE_STATUS_QUERY](https://msdn.microsoft.com/library/windows/hardware/hh598260)      |   |   | X | X |   | 
| [OID_SWITCH_NIC_ARRAY](https://msdn.microsoft.com/library/windows/hardware/hh598261)                 | X |   |   |   | X | 
| [OID_SWITCH_NIC_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598262)               |   | X |   | X |   |
| [OID_SWITCH_NIC_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598263)                |   | X |   | X |   |
| [OID_SWITCH_NIC_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598264)                |   | X |   | X |   |  
| [OID_SWITCH_NIC_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265)            |   | X |   | X |   | 
| [OID_SWITCH_NIC_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh598266)               |   |   | X |   | X |   
| [OID_SWITCH_NIC_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598267)               |   | X |   | X |   |   
| [OID_SWITCH_NIC_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268)                  | X |   |   | X |   |
| [OID_SWITCH_NIC_SAVE_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh598269)         |   | X |   | X |   | 
| [OID_SWITCH_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh598270)                | X |   |   |   | X |
| [OID_SWITCH_PORT_ARRAY](https://msdn.microsoft.com/library/windows/hardware/hh598271)                | X |   |   |   | X | 
| [OID_SWITCH_PORT_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272)               |   | X |   | X |   | 
| [OID_SWITCH_PORT_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598273)               |   | X |   | X |   | 
| [OID_SWITCH_PORT_FEATURE_STATUS_QUERY](https://msdn.microsoft.com/library/windows/hardware/hh598274) |   |   | X | X |   | 
| [OID_SWITCH_PORT_PROPERTY_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275)         |   | X |   | X |   |
| [OID_SWITCH_PORT_PROPERTY_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598276)      |   | X |   | X |   |   
| [OID_SWITCH_PORT_PROPERTY_ENUM](https://msdn.microsoft.com/library/windows/hardware/hh598277)        |   |   | X |   | X |   
| [OID_SWITCH_PORT_PROPERTY_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278)      |   | X |   | X |   | 
| [OID_SWITCH_PORT_TEARDOWN](https://msdn.microsoft.com/library/windows/hardware/hh598279)             |   | X |   | X |   |
| [OID_SWITCH_PROPERTY_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598280)              |   | X |   | X |   | 
| [OID_SWITCH_PROPERTY_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598281)           |   | X |   | X |   | 
| [OID_SWITCH_PROPERTY_ENUM](https://msdn.microsoft.com/library/windows/hardware/hh598282)             |   |   | X |   | X |
| [OID_SWITCH_PROPERTY_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598283)           |   | X |   | X |   | 


