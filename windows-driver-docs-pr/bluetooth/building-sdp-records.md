---
title: Building SDP Records
description: Building SDP Records
ms.assetid: ca3c0483-6193-4683-94bb-15466a8f332e
keywords:
- Bluetooth WDK , SDP server communication
- SDP WDK Bluetooth
- Service Discovery Protocol WDK Bluetooth
- browsing services WDK Bluetooth
- searching services WDK Bluetooth
- services browsing WDK Bluetooth
- advertising services WDK Bluetooth
- services advertising WDK Bluetooth
- SdpCreateNodeTree
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Building SDP Records


Profile drivers that advertise their services can build Service Discovery Protocol (SDP) tree hierarchies from scratch and then convert them to an SDP record stream. A profile driver must first call the [**SdpCreateNodeTree**](https://msdn.microsoft.com/library/windows/hardware/ff536818) function. The **SdpCreateNodeTree** function returns an allocated and empty [**SDP\_TREE\_ROOT\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff536851) structure that the profile driver can populate by using the following functions:

[**SdpAddAttributeToTree**](https://msdn.microsoft.com/library/windows/hardware/ff536784)

[**SdpAppendNodeToContainerNode**](https://msdn.microsoft.com/library/windows/hardware/ff536786)

[**SdpCreateNodeAlternative**](https://msdn.microsoft.com/library/windows/hardware/ff536798)

[**SdpCreateNodeBoolean**](https://msdn.microsoft.com/library/windows/hardware/ff536801)

[**SdpCreateNodeInt128**](https://msdn.microsoft.com/library/windows/hardware/ff536802)

[**SdpCreateNodeInt16**](https://msdn.microsoft.com/library/windows/hardware/ff536804)

[**SdpCreateNodeInt32**](https://msdn.microsoft.com/library/windows/hardware/ff536806)

[**SdpCreateNodeInt64**](https://msdn.microsoft.com/library/windows/hardware/ff536808)

[**SdpCreateNodeInt8**](https://msdn.microsoft.com/library/windows/hardware/ff536811)

[**SdpCreateNodeNil**](https://msdn.microsoft.com/library/windows/hardware/ff536812)

[**SdpCreateNodeSequence**](https://msdn.microsoft.com/library/windows/hardware/ff536814)

[**SdpCreateNodeString**](https://msdn.microsoft.com/library/windows/hardware/ff536816)

[**SdpCreateNodeUInt128**](https://msdn.microsoft.com/library/windows/hardware/ff536819)

[**SdpCreateNodeUInt16**](https://msdn.microsoft.com/library/windows/hardware/ff536822)

[**SdpCreateNodeUInt32**](https://msdn.microsoft.com/library/windows/hardware/ff536824)

[**SdpCreateNodeUInt64**](https://msdn.microsoft.com/library/windows/hardware/ff536827)

[**SdpCreateNodeUInt8**](https://msdn.microsoft.com/library/windows/hardware/ff536828)

[**SdpCreateNodeUrl**](https://msdn.microsoft.com/library/windows/hardware/ff536831)

[**SdpCreateNodeUUID128**](https://msdn.microsoft.com/library/windows/hardware/ff536833)

[**SdpCreateNodeUUID16**](https://msdn.microsoft.com/library/windows/hardware/ff536835)

[**SdpCreateNodeUUID32**](https://msdn.microsoft.com/library/windows/hardware/ff536836)

After the profile driver finishes building the tree-based SDP record, it calls the [**SdpConvertTreeToStream**](https://msdn.microsoft.com/library/windows/hardware/ff536796) function to produce a raw byte stream version of the SDP record. In this form, the SDP record is ready for the profile driver to publish it to the local SDP server. This process can be more convenient for profile drivers to use than constructing an SDP record as a stream.

The **SdpConvertTreeToStream** function allocates the necessary memory to store the stream version of the SDP record. When the profile driver no longer requires an SDP record, it must free the memory using [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590).

Additionally, when a profile driver no longer requires the tree-based version of an SDP record, it must call [**SdpFreeTree**](https://msdn.microsoft.com/library/windows/hardware/ff536839) to free the memory allocated with the associated SDP\_TREE\_ROOT\_NODE structure.

Profile drivers can obtain a pointer to all of the functions discussed in this topic by querying for the [**BTHDDI\_SDP\_PARSE\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536636) and [**BTHDDI\_SDP\_NODE\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536635) interfaces. For more information about how to query for these interfaces, see [Querying for Bluetooth Interfaces](querying-for-bluetooth-interfaces.md).

 

 





