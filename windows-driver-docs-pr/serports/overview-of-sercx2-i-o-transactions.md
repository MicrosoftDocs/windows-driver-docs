---
title: Overview of SerCx2 I/O Transactions
description: SerCx2 handles a read or write request from a client by issuing one or more I/O transactions to the serial controller driver.
ms.assetid: 04DDFE53-4855-4029-BE1E-9D184B02A998
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of SerCx2 I/O Transactions


SerCx2 handles a read or write request from a client by issuing one or more I/O transactions to the serial controller driver. This driver treats each transaction as a self-contained I/O operation that transfers data between the serial controller and the data buffer in the request.

System on a Chip (SoC) integrated circuits frequently include serial controllers (or UARTs) to enable high-speed serial communication with other integrated circuits that are soldered to the same printed circuit board. The processors on these SoCs can use programmed I/O (PIO) to directly transfer data to or from the memory-mapped data registers in these serial controllers. In addition, these SoCs typically provide advanced DMA hardware to move data between the serial controllers and memory.

PIO might be sufficient for short data transfers, but using PIO for longer transfers at high data rates places too great a burden on the processor. DMA is needed to offload such transfers from the processor.

## Types of I/O transactions


SerCx2 defines the following three general types of I/O transactions:

-   PIO
-   System DMA
-   Custom

All serial controller drivers must support I/O transactions that use PIO to transfer data. A serial controller driver might also support I/O transactions that use system DMA or a custom data transfer mechanism, depending on the capabilities of the serial controller and associated hardware. The driver can support either system DMA transactions or custom transactions, but not both.

For each type of I/O transaction supported by the serial controller hardware, the serial controller driver registers a support package with SerCx2. This package describes the relevant hardware capabilities, and includes a set of driver-implemented event callback functions that SerCx2 calls to initiate and control this type of I/O transaction.

If a serial controller can use a system DMA controller, which might be shared with other devices, the serial controller driver might support system DMA transactions. For these transactions, SerCx2 sets up the system DMA controller and initiates the DMA transfers. The serial controller driver does relatively little work during system DMA transactions.

If a serial controller has some custom hardware mechanism for transferring data, the serial controller driver might support custom transactions that use this mechanism. For example, if the serial controller hardware has built-in bus-master DMA capability, the serial controller driver can support custom transactions to make this capability available to SerCx2.

Custom transactions are flexible in terms of the types of data transfer mechanisms they can support. However, these transactions are more difficult to implement than PIO transactions or system DMA transactions. To support custom transactions, the serial controller driver must typically set up and initialize the hardware used to transfer data. In addition, if a pending read or write request is canceled before the associated custom-receive or custom-transmit transaction finishes, the driver must terminate the transaction and complete the request.

Each I/O transaction is a relatively simple operation. An I/O transaction either reads data from the serial controller or writes data to the controller, and never mixes reads and writes. An I/O transaction uses a single transfer mode—PIO, system DMA, or custom—and never mixes transfer modes.

SerCx2 can intelligently decide whether to use PIO or DMA to satisfy a read or write request. For example, SerCx2 might choose to present a very short read or write request to the serial controller driver as a PIO transaction. Or, SerCx2 might present a longer read or write request to the serial controller as a DMA transaction.

## Breaking a read or write request into multiple transactions


Some system DMA controllers might have limitations that require SerCx2 to break a longer read or write request into two or more I/O transactions. For example, if a system DMA controller requires DMA transfers to start and end on even byte boundaries in memory, but the data buffer in a read request starts and ends on odd byte boundaries, SerCx2 might use PIO to transfer the first and last bytes to the buffer, and use system DMA to transfer all the data between the first and last bytes. For this example, SerCx2 issues the following three I/O transactions to the serial controller driver in the order shown:

1.  A PIO-receive transaction for the first byte.
2.  A system-DMA-receive transaction for the in-between bytes.
3.  A PIO-receive transaction for the last byte.

Similarly, if a custom data-transfer mechanism can start and end a custom-transmit transaction on an arbitrary byte boundary in memory, but the buffer size in a write request exceeds the maximum transfer length of a custom-transmit transaction, SerCx2 partitions the write request into two (or more) custom-transmit transactions, each of which does not exceed the maximum transfer length.

If SerCx2 needs to split a read or write request into two or more I/O transactions, the serial controller driver can safely ignore the relationship of these transactions to each other and to the request. SerCx2 serializes the transactions to guarantee that the data is received or transmitted in the correct order.

When the serial controller driver registers a set of callback functions to support system-DMA transactions or custom transactions, the driver supplies parameter values that describe the capabilities of the hardware that will be performing these transactions. For example, for system-DMA transactions, the parameters include the alignment requirements, and the minimum and maximum transfer lengths that the system DMA controller supports. SerCx2 uses these parameters to decide whether to process a read or write request as a PIO transaction or a system-DMA transaction, and whether to split the request into two or more I/O transactions.

However, a serial controller might have special hardware capabilities that cannot adequately be described by the parameters that the serial controller driver supplies to SerCx2. Thus, the driver might have access to hardware-dependent information that enables the driver to make better decisions than SerCx2 about how to partition a read or write request into one or more I/O transactions. As an option, such a driver can implement [*EvtSerCx2SelectNextReceiveTransactionType*](https://msdn.microsoft.com/library/windows/hardware/dn265225) and [*EvtSerCx2SelectNextTransmitTransactionType*](https://msdn.microsoft.com/library/windows/hardware/dn265226) event callback functions. SerCx2 calls these functions, if they are implemented, to let the driver decide what I/O transactions to use to satisfy a read or write request.

 

 




