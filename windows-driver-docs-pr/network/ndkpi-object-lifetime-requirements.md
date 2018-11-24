---
title: NDKPI Object Lifetime Requirements
description: This section describes NDKPI object lifetime requirements
ms.assetid: 94993523-D0D7-441E-B95C-417800840BAC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDKPI Object Lifetime Requirements


## How NDK Objects Are Created, Used, and Closed


An NDK consumer initiates a create request for an NDK object by calling the NDK provider's create function for that object.

When the consumer calls a create function, it passes an *NdkCreateCompletion* ([*NDK\_FN\_CREATE\_COMPLETION*](https://msdn.microsoft.com/library/windows/hardware/hh439871)) as a parameter.

The consumer initiates various requests by calling provider functions in the object's dispatch table, passing an *NdkRequestCompletion* ([*NDK\_FN\_REQUEST\_COMPLETION*](https://msdn.microsoft.com/library/windows/hardware/hh439912)) completion callback as a parameter.

When an object is no longer needed, the consumer calls the provider's *NdkCloseObject* ([*NDK\_FN\_CLOSE\_OBJECT*](https://msdn.microsoft.com/library/windows/hardware/hh439863)) function to initiate a close request for the object, passing an *NdkCloseCompletion* ([*NDK\_FN\_CLOSE\_COMPLETION*](https://msdn.microsoft.com/library/windows/hardware/hh439862)) callback as a parameter.

For all such functions, the provider calls the consumer's callback function to complete the request. This call indicates to the consumer that the provider has completed the operation (for example, closing the object) and is returning control to the consumer.

## The Rules for Completion Callbacks


When a provider has created an object at the request of a consumer, the provider calls the consumer's *NdkCreateCompletion* callback to indicate that the object is ready for use.

The consumer can call other provider functions for the same object without waiting for the first callback to return.

The consumer will not call the *NdkCloseObject* function for an object until all provider functions for that object have returned.

However, if the provider function initiates a completion request, the consumer is free to call *NdkCloseObject* from inside that completion callback, even if the provider function hasn't returned.

A provider function can initiate a completion request before returning from a callback by doing one of the following:

-   Calling the completion callback directly
-   Queuing the completion request to another thread

By initiating a completion request, the provider effectively returns control to the consumer. The provider must assume that the object can be closed at any time after the provider initiates the completion request.

**Note**  
To prevent deadlock after initiating a completion request, the provider must either:

-   Not perform other operations on the object until the completion callback returns.
-   Take the necessary measures to keep the object intact, if the provider absolutely must touch the object.

 

## Example: Consumer-Provider Interaction


Consider the following scenario:

1.  The consumer creates a connector ([**NDK\_CONNECTOR**](https://msdn.microsoft.com/library/windows/hardware/hh439852)) and then calls *NdkConnect* ([*NDK\_FN\_CONNECT*](https://msdn.microsoft.com/library/windows/hardware/hh439865)).
2.  The provider processes the connect request, hits a failure, and calls the consumer's completion callback in the context of the *NdkConnect* call (as opposed to returning inline failure due to an internal implementation choice).
3.  The consumer calls *NdkCloseObject* in the context of this completion callback, even though the *NdkConnect* call has not yet returned to the consumer.

To avoid deadlock, the provider must not touch the connector object after step 2 (the point when it initiated the completion callback inside the *NdkConnect* call).

## Closing Antecedent and Successor Objects


The provider must be prepared for the consumer to call the *NdkCloseObject* function to close an antecedent object before the consumer calls *NdkCloseObject* for successor objects. If the consumer does this, here's what the provider must do:

-   The provider must not close the antecedent object until all the successor objects are closed, i.e., provider must return STATUS\_PENDING from the close request and complete it (by calling the registered *NdkCloseCompletion* function for the close request) once all successor objects are closed.
-   The consumer will not use the antecedent object after calling *NdkCloseObject* on it, so the provider does not have to add any handling for failing further provider functions on the antecedent object (but it may if it chooses to).
-   The provider may treat the close request like a simple dereference which has no other side-effect until the last successor object is closed, unless otherwise required (see the NDK listener close case below which has a required side-effect).

The provider must not complete the close request on an antecedent object (including the [**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848) close request) before any in-progress close completion callback on any successor object returns to the provider. This is to allow NDK consumers to unload safely.

An NDK consumer will not call *NdkCloseObject* for an [**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848) object (which is a blocking call) from inside a consumer callback function.

## Closing Adapter Objects


Consider the following scenario:

1.  The consumer calls *NdkCloseObject* on a completion queue (CQ) object.
2.  The provider returns STATUS\_PENDING, and later calls the consumer's completion callback.
3.  Inside this completion callback, the consumer signals an event that it's now OK to close the NDK\_ADAPTER.
4.  Another thread wakes up upon this signal, and closes the [**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848) and proceeds to unload.
5.  However, the thread in which the consumer's CQ close completion callback was called might still be inside the consumer's callback function (for example, the function [epilog](https://msdn.microsoft.com/library/tawsa7cb.aspx)), so it's not safe for the consumer driver to unload.
6.  Because the completion callback context is the only context the consumer can signal the event, the consumer driver can't solve the safe-unload issue itself.

There must be a point at which the consumer can be assured that all of its callbacks have returned control. In NDKPI, this point is when the close request on a [**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848) returns control. Note that **NDK\_ADAPTER** close request is a blocking call. When an **NDK\_ADAPTER** close request returns, it's guaranteed that all callbacks on all objects that descend from that **NDK\_ADAPTER** object have returned control to the provider.

## Completing Close Requests


The provider must not complete a close request on an object until:

-   All pending asynchronous requests on the object have been completed (in other words, their completion callbacks have returned to the provider).
-   All of the consumer's event callbacks (for example, *NdkCqNotificationCallback* ([*NDK\_FN\_CQ\_NOTIFICATION\_CALLBACK*](https://msdn.microsoft.com/library/windows/hardware/hh439870)) on a CQ, *NdkConnectEventCallback* ([*NDK\_FN\_CONNECT\_EVENT\_CALLBACK*](https://msdn.microsoft.com/library/windows/hardware/hh439867)) on a Listener) have returned to the provider.

The provider must guarantee that no more callbacks will happen after the close completion callback is called or after the close request returns STATUS\_SUCCESS. Note that a close request must also initiate any needed flushing or cancellation of pending asynchronous requests.

**Note**  It logically follows from the above that an NDK consumer must not call *NdkCloseObject* for an [**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848) object (which is a blocking call) from inside a consumer callback function.

 

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






