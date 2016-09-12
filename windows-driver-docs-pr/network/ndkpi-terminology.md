---
title: NDKPI Terminology
description: The NDKPI documentation uses the following terms to describe NDK providers and consumers.
ms.assetid: 740A78B3-B7AD-4A8C-8097-D49B39BC9F47
---

# NDKPI Terminology


The NDKPI documentation uses the following terms to describe NDK providers and consumers.

-   [provider function](#provider-function)
-   [consumer callback](#consumer-callback)
-   [completion callback](#completion-callback)
-   [event callback](#event-callback)
-   [parent object](#parent-object)
-   [child object](#child-object)
-   [antecedent object](#antecedent-object)
-   [successor object](#successor-object)
-   [endpoint](#endpoint)
-   [Related topics](#related-topics)

## provider function


An NDKPI function in the function dispatch table of an NDK object. Provider functions are implemented by NDK providers and called by NDK consumers. All provider functions have as the first parameter a pointer to the object on which they operate. This pointer is similar to the "this" pointer in C++. This pointer is always passed explicitly by the consumer to the provider function.

## consumer callback


An NDKPI function implemented by NDK consumers and called by NDK providers. There are 2 types of consumer callbacks: completion callbacks and event callbacks.

## completion callback


A consumer callback that is called by the NDK provider to signal the completion of an asynchronous provider function. In NDKPI 1.1 and 1.2, there are 3 completion callbacks:

-   *NdkCloseCompletion* ([*NDK\_FN\_CLOSE\_COMPLETION*](https://msdn.microsoft.com/library/windows/hardware/hh439862))
-   *NdkCreateCompletion* ([*NDK\_FN\_CREATE\_COMPLETION*](https://msdn.microsoft.com/library/windows/hardware/hh439871))
-   *NdkRequestCompletion* ([*NDK\_FN\_REQUEST\_COMPLETION*](https://msdn.microsoft.com/library/windows/hardware/hh439912))

## event callback


A consumer callback that can be called by the NDK provider to indicate certain events on an NDK object asynchronously without being triggered by an asynchronous provider function. In NDKPI 1.1 and 1.2, there are 4 event callbacks:

-   *NdkCqNotificationCallback* ([*NDK\_FN\_CQ\_NOTIFICATION\_CALLBACK*](https://msdn.microsoft.com/library/windows/hardware/hh439870))
-   *NdkConnectEventCallback* ([*NDK\_FN\_CONNECT\_EVENT\_CALLBACK*](https://msdn.microsoft.com/library/windows/hardware/hh439867))
-   *NdkDisconnectEventCallback* ([*NDK\_FN\_DISCONNECT\_EVENT\_CALLBACK*](https://msdn.microsoft.com/library/windows/hardware/hh439886))
-   *NdkSrqNotificationCallback* ([*NDK\_FN\_SRQ\_NOTIFICATION\_CALLBACK*](https://msdn.microsoft.com/library/windows/hardware/hh439915))

## parent object


An NDK object whose function dispatch table contains one or more *NdkCreate*Xxx** provider functions to create other objects. in NDKPI versions 1.1 and 1.2, there are 2 parent objects:

The NDK adapter object ([**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848)) is the parent of:

-   [**NDK\_CONNECTOR**](https://msdn.microsoft.com/library/windows/hardware/hh439852)
-   [**NDK\_CQ**](https://msdn.microsoft.com/library/windows/hardware/hh439854)
-   [**NDK\_LISTENER**](https://msdn.microsoft.com/library/windows/hardware/hh439918)
-   [**NDK\_LOGICAL\_ADDRESS\_MAPPING**](https://msdn.microsoft.com/library/windows/hardware/hh439920)
-   [**NDK\_PD**](https://msdn.microsoft.com/library/windows/hardware/hh439931)
-   [**NDK\_SHARED\_ENDPOINT**](https://msdn.microsoft.com/library/windows/hardware/hh439937)

The NDK protection domain (PD) object ([**NDK\_PD**](https://msdn.microsoft.com/library/windows/hardware/hh439931)) is the parent of:

-   [**NDK\_MR**](https://msdn.microsoft.com/library/windows/hardware/hh439922)
-   [**NDK\_MW**](https://msdn.microsoft.com/library/windows/hardware/hh439926)
-   [**NDK\_QP**](https://msdn.microsoft.com/library/windows/hardware/hh439933)
-   [**NDK\_SRQ**](https://msdn.microsoft.com/library/windows/hardware/hh439939)

## child object


An NDK object which is created by calling one of the *NdkCreate*Xxx** provider functions in a parent object's dispatch table.

## antecedent object


An NDK object that another object relies on in order to provide functionality. The antecedent object must be created before the successor object. Note that all parent objects are antecedent objects, but the reverse is not true.

## successor object


An NDK object that relies on an antecedent object. The antecedent object must be created before the successor object. Note that all child objects are successor objects but the reverse is not true. Note that an antecedent/successor relationship may be required, optional, and/or deferred to a point after the successor creation in some cases.

The following antecedent/successor relationships are defined by NDKPI versions 1.1 and 1.2 (in addition to the parent/child relationships, which are antecedent/successor relationships by definition):

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Antecedent</th>
<th align="left">Successor</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>NDK_CQ</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439854)</p></td>
<td align="left"><p>[<strong>NDK_QP</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439933)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NDK_MR</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439922)</p></td>
<td align="left"><p>[<strong>NDK_MW</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439926) (See <em>NdkBind</em> ([<em>NDK_FN_BIND</em>](https://msdn.microsoft.com/library/windows/hardware/hh439859)).)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NDK_SRQ</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439939)</p></td>
<td align="left"><p>[<strong>NDK_QP</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439933)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NDK_QP</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439933)</p></td>
<td align="left"><p>[<strong>NDK_CONNECTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439852) (See <em>NdkConnect</em> ([<em>NDK_FN_CONNECT</em>](https://msdn.microsoft.com/library/windows/hardware/hh439865)), <em>NdkAccept</em> ([<em>NDK_FN_ACCEPT</em>](https://msdn.microsoft.com/library/windows/hardware/hh439857)), and <em>NdkConnectWithSharedEndpoint</em> ([<em>NDK_FN_CONNECT_WITH_SHARED_ENDPOINT</em>](https://msdn.microsoft.com/library/windows/hardware/hh439868)).)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NDK_SHARED_ENDPOINT</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439937)</p></td>
<td align="left"><p>[<strong>NDK_CONNECTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439852) (See <em>NdkConnectWithSharedEndpoint</em> ([<em>NDK_FN_CONNECT_WITH_SHARED_ENDPOINT</em>](https://msdn.microsoft.com/library/windows/hardware/hh439868)).)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NDK_LISTENER</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439918)</p></td>
<td align="left"><p>[<strong>NDK_CONNECTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439852) (See <em>NdkConnectEventCallback</em> ([<em>NDK_FN_CONNECT_EVENT_CALLBACK</em>](https://msdn.microsoft.com/library/windows/hardware/hh439867)).)</p></td>
</tr>
</tbody>
</table>

 

## endpoint


An implicit or explicit representation of a local address and NetworkDirect port number that identify the local point over which connections can be initiated or accepted, for example, 10.1.1.1:445:

-   An [**NDK\_LISTENER**](https://msdn.microsoft.com/library/windows/hardware/hh439918) has an implicit endpoint (which the consumer specifies when calling *NdkListen* ([*NDK\_FN\_LISTEN*](https://msdn.microsoft.com/library/windows/hardware/hh439902))).
-   An [**NDK\_CONNECTOR**](https://msdn.microsoft.com/library/windows/hardware/hh439852) that is connected by calling *NdkConnect* ([*NDK\_FN\_CONNECT*](https://msdn.microsoft.com/library/windows/hardware/hh439865)) also has an implicit endpoint.
-   An [**NDK\_SHARED\_ENDPOINT**](https://msdn.microsoft.com/library/windows/hardware/hh439937) represents an explicit endpoint. The NDK consumer directly creates the endpoint and uses it explicitly to initiate one or more connections by calling *NdkConnectWithSharedEndpoint* ([*NDK\_FN\_CONNECT\_WITH\_SHARED\_ENDPOINT*](https://msdn.microsoft.com/library/windows/hardware/hh439868)).

**Note**  An NDK endpoint is not the same as the NDSPI version 1 [**INDEndpoint**](https://msdn.microsoft.com/library/cc904370) interface or the NDSPI version 2 **INDQueuePair** interface.

 

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






