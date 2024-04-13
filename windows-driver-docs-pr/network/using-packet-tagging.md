---
title: Using Packet Tagging
description: Using Packet Tagging
ms.date: 04/20/2017
---

# Using Packet Tagging


A callout driver can tag packets of interest and receive notification of events that happen to the tagged packets. Packet tagging is supported in Windows 7 and later versions of Windows.

To use packet tagging, the callout driver must implement the [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn0) or [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn1) callback function. This function will receive all of the status notifications for the tagged packets. Before individual packets can be tagged, the callout driver must obtain a special context tag by calling [**FwpsNetBufferListGetTagForContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistgettagforcontext0). The callout driver can use the same context tag for some or all of the tagged packets. For example, a callout driver might differentiate between types of tagged packets by using different context tags.

To tag packets, the callout driver uses [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures. The callout driver makes calls to [**FwpsNetBufferListAssociateContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistassociatecontext0) to tag individual **NET\_BUFFER\_LIST** structures. The context the callout driver associates with the packet is an arbitrary unsigned 64-bit value. When an event is triggered, the [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn0) or [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn1) callback passes the context as an input parameter so that the callout driver can identify individual tagged packets. The context is not used or evaluated by the filtering engine. It is only passed to the callback for use by the callout driver.

Contexts are removed from tagged packets automatically when the packets leave the stack. However, if the packets never enter the TCP/IP stack — for example, in the case of an NDIS filter driver — the contexts will need to be removed manually by calling [**FwpsNetBufferListRemoveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistremovecontext0) with the *netBufferList* parameter set to **NULL**.

If a callout needs to abort tagging operations early, contexts can be removed by calling [**FwpsNetBufferListRemoveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistremovecontext0). Removing a context generally triggers an **FWPS\_NET\_BUFFER\_LIST\_CONTEXT\_REMOVED** event. For more information about the events that can be triggered, see the [**FWPS\_NET\_BUFFER\_LIST\_EVENT\_TYPE0**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_net_buffer_list_event_type0_) enumeration. In some cases no event will be triggered, such as when the packet never enters the TCP/IP stack for processing.

When a tagged packet is cloned, the callout driver can move or copy the context to the clone packet. To move the context (in the case of a clone), the callout driver must call [**FwpsNetBufferListRetrieveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistretrievecontext0) with the *removeContext* parameter set to **TRUE**. Then the context can be associated with the new packet. The process for copying the context (in the case of a duplication) is the same except that the *removeContext* parameter of **FwpsNetBufferListRetrieveContext0** must be set to **FALSE**.

Packets tagged from TCP/IP layers can be retrieved from an [NDIS filter driver](./roadmap-for-developing-ndis-filter-drivers.md). The reverse is also true. Packet tagging is not available from stream layers where no packets are indicated except data segments.

A callout driver can retrieve the context for a packet outside of the [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn0) or [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn1) function by calling [**FwpsNetBufferListRetrieveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistretrievecontext0). Typically, a callout driver will retrieve the context in its [classifyFn](/windows-hardware/drivers/ddi/_netvista/) callback.

## Related topics


[classifyFn](/windows-hardware/drivers/ddi/_netvista/)

[**FWPS\_NET\_BUFFER\_LIST\_EVENT\_TYPE0**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_net_buffer_list_event_type0_)

[*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn0)

[*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_net_buffer_list_notify_fn1)

[**FwpsNetBufferListAssociateContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistassociatecontext0)

[**FwpsNetBufferListGetTagForContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistgettagforcontext0)

[**FwpsNetBufferListRemoveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistremovecontext0)

[**FwpsNetBufferListRetrieveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsnetbufferlistretrievecontext0)

[**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list)

[NDIS Filter Drivers](./roadmap-for-developing-ndis-filter-drivers.md)

 

