---
title: NDKPI Completion Handling Requirements
description: NDK consumers and NDK providers must follow these requirements for NDKPI completion handling.
ms.date: 04/20/2017
---

# NDKPI Completion Handling Requirements


NDK consumers and NDK providers must follow these requirements for NDKPI completion handling.

## The Rules for NdkGetCqResults, NdkGetCqResultsEx, and NdkArmCq Functions


The consumer will always serialize its calls to these provider functions on the same completion queue (CQ) object ([**NDK\_CQ**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_cq)):

-   *NdkGetCqResults* ([*NDK\_FN\_GET\_CQ\_RESULTS*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_get_cq_results))
-   *NdkGetCqResultsEx* ([*NDK\_FN\_GET\_CQ\_RESULTS\_EX*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_get_cq_results_ex))
-   *NdkArmCq* ([*NDK\_FN\_ARM\_CQ*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_arm_cq))

This means not only that the consumer will never call the same provider function multiple times concurrently, but also that it will never call any combination of these functions concurrently on the same CQ from multiple threads.

An **NdkOperationTypeReceiveAndInvalidate** completion that occurs as a result of a remote *NdkSendAndInvalidate* ([*NDK\_FN\_SEND\_AND\_INVALIDATE*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_send_and_invalidate)) call must still be retrievable using *NdkGetCqResults* (not *NdkGetCqResultsEx*n). Doing so must still invalidate the specified token on the receiver, but will not notify the receiving consumer of this invalidation (the consumer must use *NdkGetCqResultsEx* to get this information). A later *NdkInvalidate* ([*NDK\_FN\_INVALIDATE*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_invalidate)) for the same token will fail, as usual.

## The Rules for Notification Callbacks


The provider must call the *NdkCqNotificationCallback* ([*NDK\_FN\_CQ\_NOTIFICATION\_CALLBACK*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_cq_notification_callback)) callback only once, and only after the consumer has armed the *NdkCqNotificationCallback* callback by calling *NdkArmCq*. That is, the provider must clear the arm and call the *NdkCqNotificationCallback* callback when the conditions for calling the *NdkCqNotificationCallback* callback occur (in other words, when request completions are queued in the CQ).

If there are completions already present in the CQ when the consumer calls *NdkArmCq*, the provider will behave as follows:

-   If at least one of the completions was newly placed into the CQ since the last *NdkCqNotificationCallback* callback was called, the provider must satisfy the arm request immediately (see below for serialization requirements).
-   However, if all completions in the CQ were present also when the last *NdkCqNotificationCallback* callback was called (in other words, the consumer called *NdkArmCq* without removing all the completions and no new completions got placed into the CQ), then the provider may satisfy the arm request immediately.

When the provider needs to call the *NdkCqNotificationCallback* callback, if there's already a *NdkCqNotificationCallback* callback in progress, then the provider must defer the invocation of the *NdkCqNotificationCallback* callback until after the existing call to the *NdkCqNotificationCallback* callback returns control to the provider. In other words, the provider is responsible for serializing the *NdkCqNotificationCallback* callbacks.

The following table shows the resulting arm type if *NdkArmCq* is called a second time before a previous *NdkArmCq* request is satisfied:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">2nd arm ANY</th>
<th align="left">2nd arm ERRORS</th>
<th align="left">2nd arm SOLICITED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1st arm ANY</p></td>
<td align="left"><p>ANY</p></td>
<td align="left"><p>ANY</p></td>
<td align="left"><p>ANY</p></td>
</tr>
<tr class="even">
<td align="left"><p>1st arm ERRORS</p></td>
<td align="left"><p>ANY</p></td>
<td align="left"><p>ERRORS</p></td>
<td align="left"><p>SOLICITED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1st arm SOLICITED</p></td>
<td align="left"><p>ANY</p></td>
<td align="left"><p>SOLICITED</p></td>
<td align="left"><p>SOLICITED</p></td>
</tr>
</tbody>
</table>

 

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](./overview-of-network-direct-kernel-provider-interface--ndkpi-.md)

 

