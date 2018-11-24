---
title: SerCx2 PIO-Receive Transactions
description: SerCx2 requires all serial controller drivers to implement support for receive transactions that use programmed I/O (PIO).
ms.assetid: 00C43A55-ACAF-4AB6-BDFB-F3D9350C4536
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SerCx2 PIO-Receive Transactions


SerCx2 requires all serial controller drivers to implement support for receive transactions that use programmed I/O (PIO). To start a PIO-receive transaction, SerCx2 calls the driver's [*EvtSerCx2PioReceiveReadBuffer*](https://msdn.microsoft.com/library/windows/hardware/dn265214) event callback function and supplies a read buffer as a parameter.

During this call, the *EvtSerCx2PioReceiveReadBuffer* function transfers data to the read buffer from the receive FIFO in the serial controller hardware. This data transfer continues until either the read buffer is full or no more data is immediately available from the receive FIFO. When the transfer ends, the function returns the number of bytes that were successfully transferred to the read buffer from the FIFO. This function never waits for more data to be received.

## Creating the PIO-receive object


Before SerCx2 can call any of the serial controller driver's *EvtSerCx2PioReceive*Xxx** functions, the driver must call the [**SerCx2PioReceiveCreate**](https://msdn.microsoft.com/library/windows/hardware/dn265264) method to register these functions with SerCx2. This method accepts, as an input parameter, a pointer to a [**SERCX2\_PIO\_RECEIVE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/dn265330) structure that contains pointers to the driver's *EvtSerCx2PioReceive*Xxx** functions.

The driver is required to implement all three of the following functions:

-   [*EvtSerCx2PioReceiveReadBuffer*](https://msdn.microsoft.com/library/windows/hardware/dn265214)
-   [*EvtSerCx2PioReceiveEnableReadyNotification*](https://msdn.microsoft.com/library/windows/hardware/dn265212)
-   [*EvtSerCx2PioReceiveCancelReadyNotification*](https://msdn.microsoft.com/library/windows/hardware/dn265210)

As an option, the driver can implement one or both of the following functions:

-   [*EvtSerCx2PioReceiveInitializeTransaction*](https://msdn.microsoft.com/library/windows/hardware/dn265213)
-   [*EvtSerCx2PioReceiveCleanupTransaction*](https://msdn.microsoft.com/library/windows/hardware/dn265211)

The **SerCx2PioReceiveCreate** method creates a PIO-receive object and supplies the calling driver with a [**SERCX2PIORECEIVE**](https://msdn.microsoft.com/library/windows/hardware/dn265267) handle to this object. The driver's *EvtSerCx2PioReceive*Xxx** functions all take this handle as their first parameter. The following SerCx2 methods take this handle as their first parameter:

-   [**SerCx2PioReceiveReady**](https://msdn.microsoft.com/library/windows/hardware/dn265266)
-   [**SerCx2PioReceiveInitializeTransactionComplete**](https://msdn.microsoft.com/library/windows/hardware/dn265265)
-   [**SerCx2PioReceiveCleanupTransactionComplete**](https://msdn.microsoft.com/library/windows/hardware/dn265263)

## Hardware initialization and clean-up


Some serial controller drivers might need to initialize the serial controller hardware at the start of a PIO-receive transaction, or to clean up the hardware state of the serial controller at the end of the transaction.

If a driver implements an [*EvtSerCx2PioReceiveInitializeTransaction*](https://msdn.microsoft.com/library/windows/hardware/dn265213) event callback function, SerCx2 calls this function to initialize the serial controller before the *EvtSerCx2PioReceiveReadBuffer* call that starts the transaction. If implemented, the *EvtSerCx2PioReceiveInitializeTransaction* function must call the [**SerCx2PioReceiveInitializeTransactionComplete**](https://msdn.microsoft.com/library/windows/hardware/dn265265) method to inform SerCx2 when the driver finishes initializing the serial controller.

If the driver implements an [*EvtSerCx2PioReceiveCleanupTransaction*](https://msdn.microsoft.com/library/windows/hardware/dn265211) event callback function, SerCx2 calls this function to clean up the hardware state after the final *EvtSerCx2PioReceiveReadBuffer* call in the transaction. If implemented, the *EvtSerCx2PioReceiveInitializeTransaction* function must call the [**SerCx2PioReceiveCleanupTransactionComplete**](https://msdn.microsoft.com/library/windows/hardware/dn265263) method to inform SerCx2 when the driver finishes cleaning up the serial controller.

## Ready notifications


When an *EvtSerCx2PioReceiveReadBuffer* call ends because no more data is immediately available to read from the receive FIFO, SerCx2 cannot finish the PIO-receive transaction until, at some later time, the serial controller receives more data. In this case, SerCx2 calls the [*EvtSerCx2PioReceiveEnableReadyNotification*](https://msdn.microsoft.com/library/windows/hardware/dn265212) event callback function to enable a ready notification. This function typically enables an interrupt to be triggered when one or more bytes of data are available to be read from the receive FIFO. If and only if this notification is enabled, the serial controller driver calls the [**SerCx2PioReceiveReady**](https://msdn.microsoft.com/library/windows/hardware/dn265266) method to notify SerCx2 when the driver detects that the receive FIFO is no longer empty. In response to this notification, SerCx2 calls the *EvtSerCx2PioReceiveReadBuffer* function to read the newly received data.

SerCx2 additionally uses ready notifications to efficiently manage time-outs during the handling of read requests that are processed as PIO-receive transactions. For more information about these time-outs, see [**SERIAL\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/hh439614).

If the ready notification is enabled when the read request times out or is canceled, SerCx2 calls the [*EvtSerCx2PioReceiveCancelReadyNotification*](https://msdn.microsoft.com/library/windows/hardware/dn265210) event callback function to cancel the pending notification. If this function successfully cancels the pending notification, it returns **TRUE**. A return value of **TRUE** guarantees that the serial controller driver will not call [**SerCx2PioReceiveReady**](https://msdn.microsoft.com/library/windows/hardware/dn265266). A return value of **FALSE** indicates that the controller driver has already called or will soon call **SerCx2PioReceiveReady**.

 

 




