---
title: NDKPI deferred processing scheme
description: This section describes the deferred processing used with NDKPI
ms.assetid: DA2D0FCA-D84B-4599-A560-8F87A0918D99
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDKPI Deferred Processing Scheme


There are many cases where an NDK consumer will post a chain of initiator requests to the queue pair (QP). For example, a consumer could post a number of fast register requests followed by a send request. The performance for such request patterns may be improved if the chain of requests is queued to the QP and then indicated to the hardware for processing as a batch, rather than indicating each request in the chain to the hardware, one by one.

The **NDK\_OP\_FLAG\_DEFER** flag value can be used for this purpose with the following request types:

-   *NdkBind* ([*NDK\_FN\_BIND*](https://msdn.microsoft.com/library/windows/hardware/hh439859))
-   *NdkFastRegister* ([*NDK\_FN\_FAST\_REGISTER*](https://msdn.microsoft.com/library/windows/hardware/hh439887))
-   *NdkInvalidate* ([*NDK\_FN\_INVALIDATE*](https://msdn.microsoft.com/library/windows/hardware/hh439901))
-   *NdkRead* ([*NDK\_FN\_READ*](https://msdn.microsoft.com/library/windows/hardware/hh439906))
-   *NdkSend* ([*NDK\_FN\_SEND*](https://msdn.microsoft.com/library/windows/hardware/hh439914))
-   *NdkSendAndInvalidate* ([*NDK\_FN\_SEND\_AND\_INVALIDATE*](https://msdn.microsoft.com/library/windows/hardware/dn265507))
-   *NdkWrite* ([*NDK\_FN\_WRITE*](https://msdn.microsoft.com/library/windows/hardware/hh439917))

The presence of the flag is a hint to the NDK provider that it may defer indicating the request to hardware for processing, but the provider may process the new request at any time.

The presence of the **NDK\_OP\_FLAG\_DEFER** flag on an initiator request does not change the NDK provider's existing responsibilities with respect to generating completions. A call to the initiator request that returns a failure status must not result in a completion being queued to the CQ for the failed request. Conversely, a call that returns a success status must eventually result in a completion being queued to the CQ as long as the consumer follows the additional requirements listed below.

In addition to all the existing NDK requirements, two additional requirements (one for the provider and one for the consumer) must be observed to prevent a situation in which requests are successfully posted to the QP with the **NDK\_OP\_FLAG\_DEFER** flag, but are never indicated to the hardware for processing:

-   When returning a failure status from a call to an initiator request, the provider must guarantee that all requests that were previously submitted with the **NDK\_OP\_FLAG\_DEFER** flag are indicated to the hardware for processing.
-   The consumer guarantees that, in the absence of an inline failure, all initiator request chains will be terminated by an initiator request that does not set the **NDK\_OP\_FLAG\_DEFER** flag.

For example, consider a case where a consumer has a chain of two fast register requests and a send that it needs to post to the QP:

1.  The consumer posts the first fast register with the **NDK\_OP\_FLAG\_DEFER** flag and *NdkFastRegister* returns STATUS\_SUCCESS.
2.  Again, the second fast register is posted with the **NDK\_OP\_FLAG\_DEFER** flag set but now *NdkFastRegister* returns a failure status. In this case, the consumer will not post the send request.
3.  When returning the inline failure for the second call to *NdkFastRegister*, the NDK provider makes sure that all previously unindicated requests (the first fast register in this case) are indicated to the hardware for processing.
4.  Because the first call to *NdkFastRegister* succeeded, a completion must be generated to the CQ.
5.  Because the second call to *NdkFastRegister* failed inline, a completion must not be generated to the CQ.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






