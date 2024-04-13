---
title: NDKPI Work Request Posting Requirements
description: This section describes requirements for NDKPI work request posting
ms.date: 04/20/2017
---

# NDKPI Work Request Posting Requirements


## Work Request Posting Rules for the Consumer


The NDK consumer will post the following types of work requests on the initiator queue:

-   *NdkBind* ([*NDK\_FN\_BIND*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_bind))
-   *NdkFastRegister* ([*NDK\_FN\_FAST\_REGISTER*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_fast_register))
-   *NdkInvalidate* ([*NDK\_FN\_INVALIDATE*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_invalidate))
-   *NdkRead* ([*NDK\_FN\_READ*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_read))
-   *NdkSend* ([*NDK\_FN\_SEND*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_send))
-   *NdkSendAndInvalidate* ([*NDK\_FN\_SEND\_AND\_INVALIDATE*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_send_and_invalidate))
-   *NdkWrite* ([*NDK\_FN\_WRITE*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_write))

The consumer will post *NdkReceive* ([*NDK\_FN\_RECEIVE*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_receive)) requests on the receive queue.

The consumer will post all of these requests to the same individual queue on an [**NDK\_QP**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp) or [**NDK\_SRQ**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_srq) in a serialized fashion. In other words, the consumer will never have two concurrent calls to any work request functions on the same individual queue belonging to an **NDK\_QP** or **NDK\_SRQ**.

This means, for example, that concurrent *NdkReceive* calls won't be issued, concurrent *NdkSend* and *NdkWrite* calls won't be issued, but concurrent *NdkReceive* and *NdkWrite* calls may be issued on the same [**NDK\_QP**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp).

## Work Request Posting Rules for the Provider


The provider should not have any redundant locks inside the above work request functions, because they are guaranteed to be serialized by the consumer.

The provider must be able to handle *NdkFlush* ([*NDK\_FN\_FLUSH*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_flush)) calls that may be called concurrently with a work request call on the same [**NDK\_QP**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp).

The provider must be able to handle an **NdkCloseConnector** call (on the successor [**NDK\_CONNECTOR**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector) object for the [**NDK\_QP**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp)) that may be called concurrently with a work request call on the same **NDK\_QP**.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](./overview-of-network-direct-kernel-provider-interface--ndkpi-.md)

 

