---
title: Retrieving the Contents of a IEEE 1394 Node's Configuration ROM
description: Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver, that is implemented by using the kernel-mode driver framework (KMDF).
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: AC327938-A813-4665-8E2E-43BEE11D4AA9
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Retrieving%20the%20Contents%20of%20a%20IEEE%201394%20Node's%20Configuration%20ROM%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





