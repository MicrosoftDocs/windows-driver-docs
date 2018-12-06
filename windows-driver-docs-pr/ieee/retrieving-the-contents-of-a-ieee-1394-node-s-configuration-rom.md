---
title: Retrieving the Contents of a IEEE 1394 Node's Configuration ROM
description: Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver, that is implemented by using the kernel-mode driver framework (KMDF).
ms.assetid: AC327938-A813-4665-8E2E-43BEE11D4AA9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving the Contents of a IEEE 1394 Node's Configuration ROM


Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver, that is implemented by using the kernel-mode driver framework (KMDF). The 1394ohci.sys bus driver replaces the legacy IEEE bus driver in port/miniport configuration-- 1394bus.sys and ochi1394.sys. It is backward compatible with the legacy 1394 bus driver. For information about some known differences in behavior between the new and the legacy 1394 bus driver, see [IEEE 1394 Bus Driver in Windows 7](https://msdn.microsoft.com/library/windows/hardware/gg266402).

This topic provides details about how the 1394ohci.sys bus driver retrieves the contents of a node's configuration ROM, which is later used for device enumeration. Processing the contents of a node's configuration ROM for device discovery has not changed for Windows 7. For more information about how the contents of a node's configuration ROM is processed, see [Modifying the 1394 Configuration ROM](https://msdn.microsoft.com/library/windows/hardware/ff537433).

The 1394ohci.sys bus driver retrieves the contents of a node's configuration ROM after a 1394 bus reset by sending asynchronous read transactions to the node. It tries to reduce the number of asynchronous read transactions that are sent to a node to retrieve the contents of the node's configuration ROM.

This topic contains the following sections:

-   [Retrieving the Configuration ROM Header](#retrieving-the-configuration-rom-header)
-   [New Configuration ROM](#new-configuration-rom)
-   [Previously Retrieved Configuration ROM](#previously-retrieved-configuration-rom)
-   [Related topics](#related-topics)

## Retrieving the Configuration ROM Header


To retrieve the contents of a node's configuration ROM, a client driver sends a [**REQUEST\_GET\_LOCAL\_HOST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537644) request to the IEEE 1394 driver stack by specifying the **u.GetLocalHostInformation.nLevel** to GET\_HOST\_CONFIG\_ROM. Upon completing the request, the bus driver retrieves the node's configuration ROM header in a [**GET\_LOCAL\_HOST\_INFO5**](https://msdn.microsoft.com/library/windows/hardware/ff537152) structure. The configuration ROM header is in the first five quadlets of a node's configuration ROM. This header includes the contents of the bus information block, as defined in the IEEE-1394a specification.

The 1394ohci.sys bus driver tries to retrieve the configuration ROM header in a single asynchronous block read transaction. However, certain 1394 devices might not respond to this transaction correctly. In this situation, the new 1394 bus driver uses five asynchronous quadlet read transactions to retrieve the configuration ROM header.

The speed of communication with a node is determined during the retrieval of the node's configuration ROM header. The 1394ohci.sys bus driver sends the asynchronous read transaction to the node at the fastest supported speed and considers any slower nodes between the local node and the target node. If the asynchronous read transaction does not complete successfully at the fastest supported speed, then the 1394ohci.sys bus driver sends another asynchronous read transaction to the node at a slower speed. The 1394ohci.sys bus driver continues to send asynchronous read transactions to the node at slower and slower speeds until a transaction is completed successfully. After the asynchronous transaction is complete at a particular speed, that speed is used for all additional communication with the node until another 1394 bus reset occurs. If the asynchronous read transaction does not complete at the slowest possible speed, then the 1394ohci.sys bus driver does not retrieve the contents of the node's configuration ROM.

After the configuration ROM header is retrieved, the 1394ohci.sys bus driver checks whether the contents of the node's configuration ROM were previously retrieved. If so, it can reuse its cached version. Otherwise, it must retrieve the remaining contents of the node's configuration ROM.

## New Configuration ROM


If the 1394ohci.sys bus driver determines that the contents of the node's configuration ROM was not previously retrieved, it proceeds to retrieve the remaining contents of the node's configuration ROM.

The 1394ohci.sys bus driver uses the **max\_rom** value in the bus information block of the configuration ROM header to determine the size of the asynchronous read transactions to send to the node to retrieve the remaining contents of the configuration ROM. If any asynchronous read transaction fails—regardless of the **max\_rom** value—the new 1394 bus driver uses asynchronous quadlet read transactions to retrieve the remaining contents of the node's configuration ROM.

## Previously Retrieved Configuration ROM


After the 1394ohci.sys bus driver retrieves the contents of a node's configuration ROM header, it determines whether the header matches the header of one of the cached copies of configuration ROM contents that the driver previously retrieved. If the it finds a matching configuration ROM header, then it reuses the cached configuration ROM contents.

The 1394ohci.sys bus driver uses the following steps to determine whether it can reuse a cached copy of the contents of a node's configuration ROM:

1.  The bus driver determines whether the **node\_vendor\_id**, **chip\_id hi**, and **chip\_id lo** values in the bus information block of the node's configuration ROM header match those same values in the header of one of the driver's cached copies of configuration ROM contents.
2.  If a match is found in step 1, then the bus driver determines whether the generation value in the bus information block also matches. If the generation value has not changed (or if it is set to 1, which indicates that it never changes), then the bus driver reuses the cached contents of the configuration ROM.

You can find descriptions of the configuration ROM values in the previous steps in the IEEE 1394 specifications. If the 1394ohci.sys bus driver fails to find a matching cached configuration ROM header or if it must reread the contents of the node's configuration ROM because the **generation** value changed, then it follows the previous steps to retrieve the contents of a new configuration ROM.

## Related topics
[The IEEE 1394 Driver Stack](https://msdn.microsoft.com/library/windows/hardware/ff538867)  
[Modifying the 1394 Configuration ROM](https://msdn.microsoft.com/library/windows/hardware/ff537433)  
[**REQUEST\_GET\_CONFIG\_ROM**](https://msdn.microsoft.com/library/windows/hardware/gg266404)  



