---
title: NDKPI Terminology
description: The NDKPI documentation uses the following terms to describe NDK providers and consumers.
ms.date: 04/20/2017
ms.localizationpriority: medium
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

-   *NdkCloseCompletion* ([*NDK\_FN\_CLOSE\_COMPLETION*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_close_completion))
-   *NdkCreateCompletion* ([*NDK\_FN\_CREATE\_COMPLETION*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_completion))
-   *NdkRequestCompletion* ([*NDK\_FN\_REQUEST\_COMPLETION*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_request_completion))

## event callback


A consumer callback that can be called by the NDK provider to indicate certain events on an NDK object asynchronously without being triggered by an asynchronous provider function. In NDKPI 1.1 and 1.2, there are 4 event callbacks:

-   *NdkCqNotificationCallback* ([*NDK\_FN\_CQ\_NOTIFICATION\_CALLBACK*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_cq_notification_callback))
-   *NdkConnectEventCallback* ([*NDK\_FN\_CONNECT\_EVENT\_CALLBACK*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect_event_callback))
-   *NdkDisconnectEventCallback* ([*NDK\_FN\_DISCONNECT\_EVENT\_CALLBACK*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_disconnect_event_callback))
-   *NdkSrqNotificationCallback* ([*NDK\_FN\_SRQ\_NOTIFICATION\_CALLBACK*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_srq_notification_callback))

## parent object


An NDK object whose function dispatch table contains one or more *NdkCreate*Xxx** provider functions to create other objects. in NDKPI versions 1.1 and 1.2, there are 2 parent objects:

The NDK adapter object ([**NDK\_ADAPTER**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_adapter)) is the parent of:

-   [**NDK\_CONNECTOR**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector)
-   [**NDK\_CQ**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_cq)
-   [**NDK\_LISTENER**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_listener)
-   [**NDK\_LOGICAL\_ADDRESS\_MAPPING**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_logical_address_mapping)
-   [**NDK\_PD**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_pd)
-   [**NDK\_SHARED\_ENDPOINT**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_shared_endpoint)

The NDK protection domain (PD) object ([**NDK\_PD**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_pd)) is the parent of:

-   [**NDK\_MR**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mr)
-   [**NDK\_MW**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mw)
-   [**NDK\_QP**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp)
-   [**NDK\_SRQ**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_srq)

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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_cq" data-raw-source="[&lt;strong&gt;NDK_CQ&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_cq)"><strong>NDK_CQ</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp" data-raw-source="[&lt;strong&gt;NDK_QP&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp)"><strong>NDK_QP</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mr" data-raw-source="[&lt;strong&gt;NDK_MR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mr)"><strong>NDK_MR</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mw" data-raw-source="[&lt;strong&gt;NDK_MW&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mw)"><strong>NDK_MW</strong></a> (See <em>NdkBind</em> (<a href="/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_bind" data-raw-source="[&lt;em&gt;NDK_FN_BIND&lt;/em&gt;](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_bind)"><em>NDK_FN_BIND</em></a>).)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_srq" data-raw-source="[&lt;strong&gt;NDK_SRQ&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_srq)"><strong>NDK_SRQ</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp" data-raw-source="[&lt;strong&gt;NDK_QP&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp)"><strong>NDK_QP</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp" data-raw-source="[&lt;strong&gt;NDK_QP&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp)"><strong>NDK_QP</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector" data-raw-source="[&lt;strong&gt;NDK_CONNECTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector)"><strong>NDK_CONNECTOR</strong></a> (See <em>NdkConnect</em> (<a href="/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect" data-raw-source="[&lt;em&gt;NDK_FN_CONNECT&lt;/em&gt;](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect)"><em>NDK_FN_CONNECT</em></a>), <em>NdkAccept</em> (<a href="/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_accept" data-raw-source="[&lt;em&gt;NDK_FN_ACCEPT&lt;/em&gt;](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_accept)"><em>NDK_FN_ACCEPT</em></a>), and <em>NdkConnectWithSharedEndpoint</em> (<a href="/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect_with_shared_endpoint" data-raw-source="[&lt;em&gt;NDK_FN_CONNECT_WITH_SHARED_ENDPOINT&lt;/em&gt;](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect_with_shared_endpoint)"><em>NDK_FN_CONNECT_WITH_SHARED_ENDPOINT</em></a>).)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_shared_endpoint" data-raw-source="[&lt;strong&gt;NDK_SHARED_ENDPOINT&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_shared_endpoint)"><strong>NDK_SHARED_ENDPOINT</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector" data-raw-source="[&lt;strong&gt;NDK_CONNECTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector)"><strong>NDK_CONNECTOR</strong></a> (See <em>NdkConnectWithSharedEndpoint</em> (<a href="/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect_with_shared_endpoint" data-raw-source="[&lt;em&gt;NDK_FN_CONNECT_WITH_SHARED_ENDPOINT&lt;/em&gt;](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect_with_shared_endpoint)"><em>NDK_FN_CONNECT_WITH_SHARED_ENDPOINT</em></a>).)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_listener" data-raw-source="[&lt;strong&gt;NDK_LISTENER&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_listener)"><strong>NDK_LISTENER</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector" data-raw-source="[&lt;strong&gt;NDK_CONNECTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector)"><strong>NDK_CONNECTOR</strong></a> (See <em>NdkConnectEventCallback</em> (<a href="/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect_event_callback" data-raw-source="[&lt;em&gt;NDK_FN_CONNECT_EVENT_CALLBACK&lt;/em&gt;](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect_event_callback)"><em>NDK_FN_CONNECT_EVENT_CALLBACK</em></a>).)</p></td>
</tr>
</tbody>
</table>

 

## endpoint


An implicit or explicit representation of a local address and NetworkDirect port number that identify the local point over which connections can be initiated or accepted, for example, 10.1.1.1:445:

-   An [**NDK\_LISTENER**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_listener) has an implicit endpoint (which the consumer specifies when calling *NdkListen* ([*NDK\_FN\_LISTEN*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_listen))).
-   An [**NDK\_CONNECTOR**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector) that is connected by calling *NdkConnect* ([*NDK\_FN\_CONNECT*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect)) also has an implicit endpoint.
-   An [**NDK\_SHARED\_ENDPOINT**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_shared_endpoint) represents an explicit endpoint. The NDK consumer directly creates the endpoint and uses it explicitly to initiate one or more connections by calling *NdkConnectWithSharedEndpoint* ([*NDK\_FN\_CONNECT\_WITH\_SHARED\_ENDPOINT*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_connect_with_shared_endpoint)).

**Note**  An NDK endpoint is not the same as the NDSPI version 1 [**INDEndpoint**](/previous-versions/windows/desktop/cc904370(v=vs.85)) interface or the NDSPI version 2 **INDQueuePair** interface.

 

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](./overview-of-network-direct-kernel-provider-interface--ndkpi-.md)

