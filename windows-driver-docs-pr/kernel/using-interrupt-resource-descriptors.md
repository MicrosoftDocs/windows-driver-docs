---
title: Using Interrupt Resource Descriptors
description: Using Interrupt Resource Descriptors
ms.assetid: 0e9aa9a1-c1aa-42e1-9c0b-a91a2424ad1a
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Using Interrupt Resource Descriptors


The Plug and Play (PnP) manager assigns interrupt messages to a device using two passes. First, the PnP manager sends an [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874) request to the driver with a list of hardware resources, including interrupt messages, that it intends to assign to the device. The driver can modify this list to change the number of interrupt messages, as well as some per-message settings. Then, after the PnP manager actually assigns the resources, it sends an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request and supplies a complete list of the hardware resources, including interrupt messages, assigned to the driver's device.

The **IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS** request supplies a list of [**IO\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff550598) structures. If the device has an MSI (message-signaled interrupt) capability structure as defined in the PCI 2.2 specification, the PnP manager supplies a single interrupt message descriptor. If the device has an MSI-X capability structure as defined in the PCI 3.0 specification, the PnP manager supplies one structure for each interrupt message. Interrupt message descriptors have **Type** = **CmResourceTypeInterrupt** and **Flags** = CM\_RESOURCE\_INTERRUPT\_LATCHED | CM\_RESOURCE\_INTERRUPT\_MESSAGE. Drivers can also change settings such as the interrupt affinity by changing the **u.Interrupt** members of the structure. Note that when using MSI, interrupts all have same affinity, while when using MSI-X they can have different affinities. For more information, see [Interrupt Affinity and Priority](interrupt-affinity-and-priority.md).

For MSI, as defined in PCI 2.2, **u.Interrupt.MaximumVector** - **u.Interrupt.MinimumVector** + 1 is the number of interrupt messages allocated for the device. Drivers can change the number of interrupt messages by modifying **u.Interrupt.MinimumVector**. For MSI interrupt messages, **u.Interrupt.MaximumVector** is always CM\_RESOURCE\_INTERRUPT\_MESSAGE\_TOKEN. To allocate *MessageCount* interrupt messages, set **u.Interrupt.MinimumVector** to equal CM\_RESOURCE\_INTERRUPT\_MESSAGE\_TOKEN - *MessageCount* + 1.

For MSI-X, as defined in PCI 3.0, drivers can change the number of interrupt messages allocated by adding or removing entries from the list. Note that interrupt message resources added this way must not be subsequently removed in response to the [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. For MSI-X, the PnP manager supplies one descriptor per message interrupt, and the **u.Interrupt.MinimumVector** and **u.Interrupt.MaximumVector** members of this descriptor are both set to CM\_RESOURCE\_INTERRUPT\_MESSAGE\_TOKEN.

Once the Plug and Play manager has assigned all hardware resources for the device, including interrupt messages, it sends the **IRP\_MN\_START\_DEVICE** request to the driver. This request supplies two lists of [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structures, one each for raw and translated resources. For interrupt messages, the PnP manager supplies one structure for each allocated memory address with **Type** = **CmResourceTypeInterrupt** and **Flags** = CM\_RESOURCE\_INTERRUPT\_LATCHED | CM\_RESOURCE\_INTERRUPT\_MESSAGE.

Note that when using MSI, the driver only receives one interrupt resource descriptor, since all messages share the same address. The **MessageCount** member of **u.InterruptMessage.Raw** can be used to determine the number of messages assigned. When using MSI-X, the driver receives a separate resource descriptor for each interrupt message.

In Windows 8, the operating system does not support resource requests for more than 2048 interrupt messages per device function. In Windows 7 and Windows Vista, the operating system does not support resource requests for more than 910 interrupt messages per device function. If the device driver exceeds this limit, the device might fail to start. To enable a driver to operate in a computer that contains many logical processors, the driver should avoid requesting more than one interrupt per processor.

During system rebalancing of interrupt resources, the PnP manager might ask a driver to select a preferred set of alternate interrupt resources from a resource requirements list. However, the PnP manager cannot always assign to a driver the resources that the driver prefers. The driver must therefore tolerate, without failures, the assignment of any set of alternate interrupt resources from the resource requirements list. For example, the device might be assigned a smaller number of message interrupts than the driver requested. In the worst case, the driver must be prepared to operate the device with just one line-based interrupt.

 

 




