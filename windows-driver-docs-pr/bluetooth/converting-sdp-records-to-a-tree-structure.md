---
title: Converting SDP Records to a Tree Structure
description: Converting SDP Records to a Tree Structure
ms.assetid: 762cf68b-0082-4b9e-8f24-ff19ecf6f8bd
keywords:
- Bluetooth WDK , SDP server communication
- SDP WDK Bluetooth
- Service Discovery Protocol WDK Bluetooth
- browsing services WDK Bluetooth
- searching services WDK Bluetooth
- services browsing WDK Bluetooth
- converting SDP records
- tree structures from SDP records WDK Bluetooth
- SdpConvertStreamToTree
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Converting SDP Records to a Tree Structure


Service Discovery Protocol (SDP) records are encoded in a complex binary stream. To enable profile drivers to parse SDP records more easily, the Bluetooth driver stack provides a number of functions that profile drivers can use to convert the SDP record stream into a hierarchical tree structure and back again.

Client profile drivers can use the [**SdpConvertStreamToTree**](https://msdn.microsoft.com/library/windows/hardware/ff536794) function to convert an SDP record into a tree structure. The tree representation of the SDP record that results from calling the **SdpConvertStreamToTree** function consists of a root node that contains all information associated with the SDP record, defined by an [**SDP\_TREE\_ROOT\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff536851) structure. The root node contains a series of interconnected [**SDP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff536848) structures, each of which contains information about a single SDP attribute.

Each SDP\_NODE structure contains an [**SDP\_NODE\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff536850) structure and an [**SDP\_NODE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff536849) union. The header structure specifies the type of data that is contained in the node. Profile drivers use the [**LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff554296) structure to access links to peer SDP\_NODE structures. By using the SDP\_NODE structure's **hdr.Link.Flink** and **hdr.Link.Blink** members, profile drivers can obtain the addresses of peer nodes in the tree. Keep in mind that LIST\_ENTRY pointers hold addresses to other LIST\_ENTRY structures, and that profile drivers must use the [**CONTAINING\_RECORD**](https://msdn.microsoft.com/library/windows/hardware/ff542043) macro to extract the address that contains the node record. For more information, see the [**SdpConvertStreamToTree**](https://msdn.microsoft.com/library/windows/hardware/ff536794) topic.

After the SDP record stream is converted to a tree representation, a profile driver can call the [**SdpFindAttributeInTree**](https://msdn.microsoft.com/library/windows/hardware/ff536838) function to obtain the address of a specified node in the tree.

Profile drivers can obtain a pointer to all of the functions discussed in this topic by querying for the [**BTHDDI\_SDP\_PARSE\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536636) and [**BTHDDI\_SDP\_NODE\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536635) interfaces. For more information about how to query for these interfaces, see [Querying for Bluetooth Interfaces](querying-for-bluetooth-interfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Converting%20SDP%20Records%20to%20a%20Tree%20Structure%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




