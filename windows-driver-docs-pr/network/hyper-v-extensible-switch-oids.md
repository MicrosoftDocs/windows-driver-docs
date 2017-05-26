---
title: Hyper-V Extensible Switch OIDs
description: This section describes Hyper-V Extensible Switch OIDs and their characteristics.
keywords: ["Hyper-V Extensible Switch OIDs", "Hyper-V Switch OIDs", "WDK Hyper-V Extensible Switch OIDs", "Hyper-V Extensible Switch object identifiers"]
ms.assetid: A97C5BF0-7319-4BEE-ABF7-12B11CEAF3DB"
ms.author: windowsdriverdev
ms.date: 04/24/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")