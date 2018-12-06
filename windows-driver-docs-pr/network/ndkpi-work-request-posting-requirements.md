---
title: NDKPI Work Request Posting Requirements
description: This section describes requirements for NDKPI work request posting
ms.assetid: 2BF6F253-FCB4-4A61-9A67-81092F3C44E4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDKPI Work Request Posting Requirements


## Work Request Posting Rules for the Consumer


The NDK consumer will post the following types of work requests on the initiator queue:

-   *NdkBind* ([*NDK\_FN\_BIND*](https://msdn.microsoft.com/library/windows/hardware/hh439859))
-   *NdkFastRegister* ([*NDK\_FN\_FAST\_REGISTER*](https://msdn.microsoft.com/library/windows/hardware/hh439887))
-   *NdkInvalidate* ([*NDK\_FN\_INVALIDATE*](https://msdn.microsoft.com/library/windows/hardware/hh439901))
-   *NdkRead* ([*NDK\_FN\_READ*](https://msdn.microsoft.com/library/windows/hardware/hh439906))
-   *NdkSend* ([*NDK\_FN\_SEND*](https://msdn.microsoft.com/library/windows/hardware/hh439914))
-   *NdkSendAndInvalidate* ([*NDK\_FN\_SEND\_AND\_INVALIDATE*](https://msdn.microsoft.com/library/windows/hardware/dn265507))
-   *NdkWrite* ([*NDK\_FN\_WRITE*](https://msdn.microsoft.com/library/windows/hardware/hh439917))

The consumer will post *NdkReceive* ([*NDK\_FN\_RECEIVE*](https://msdn.microsoft.com/library/windows/hardware/hh439907)) requests on the receive queue.

The consumer will post all of these requests to the same individual queue on an [**NDK\_QP**](https://msdn.microsoft.com/library/windows/hardware/hh439933) or [**NDK\_SRQ**](https://msdn.microsoft.com/library/windows/hardware/hh439939) in a serialized fashion. In other words, the consumer will never have two concurrent calls to any work request functions on the same individual queue belonging to an **NDK\_QP** or **NDK\_SRQ**.

This means, for example, that concurrent *NdkReceive* calls won't be issued, concurrent *NdkSend* and *NdkWrite* calls won't be issued, but concurrent *NdkReceive* and *NdkWrite* calls may be issued on the same [**NDK\_QP**](https://msdn.microsoft.com/library/windows/hardware/hh439933).

## Work Request Posting Rules for the Provider


The provider should not have any redundant locks inside the above work request functions, because they are guaranteed to be serialized by the consumer.

The provider must be able to handle *NdkFlush* ([*NDK\_FN\_FLUSH*](https://msdn.microsoft.com/library/windows/hardware/hh439889)) calls that may be called concurrently with a work request call on the same [**NDK\_QP**](https://msdn.microsoft.com/library/windows/hardware/hh439933).

The provider must be able to handle an **NdkCloseConnector** call (on the successor [**NDK\_CONNECTOR**](https://msdn.microsoft.com/library/windows/hardware/hh439852) object for the [**NDK\_QP**](https://msdn.microsoft.com/library/windows/hardware/hh439933)) that may be called concurrently with a work request call on the same **NDK\_QP**.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






