---
title: Using Packet Tagging
description: Using Packet Tagging
ms.assetid: a151256b-d69f-4abb-bf68-644f157dfdd7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Packet Tagging


A callout driver can tag packets of interest and receive notification of events that happen to the tagged packets. Packet tagging is supported in Windows 7 and later versions of Windows.

To use packet tagging, the callout driver must implement the [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0*](https://msdn.microsoft.com/library/windows/hardware/ff552406) or [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](https://msdn.microsoft.com/library/windows/hardware/hh451260) callback function. This function will receive all of the status notifications for the tagged packets. Before individual packets can be tagged, the callout driver must obtain a special context tag by calling [**FwpsNetBufferListGetTagForContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551192). The callout driver can use the same context tag for some or all of the tagged packets. For example, a callout driver might differentiate between types of tagged packets by using different context tags.

To tag packets, the callout driver uses [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. The callout driver makes calls to [**FwpsNetBufferListAssociateContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551191) to tag individual **NET\_BUFFER\_LIST** structures. The context the callout driver associates with the packet is an arbitrary unsigned 64-bit value. When an event is triggered, the [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0*](https://msdn.microsoft.com/library/windows/hardware/ff552406) or [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](https://msdn.microsoft.com/library/windows/hardware/hh451260) callback passes the context as an input parameter so that the callout driver can identify individual tagged packets. The context is not used or evaluated by the filtering engine. It is only passed to the callback for use by the callout driver.

Contexts are removed from tagged packets automatically when the packets leave the stack. However, if the packets never enter the TCP/IP stack — for example, in the case of an NDIS filter driver — the contexts will need to be removed manually by calling [**FwpsNetBufferListRemoveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551194) with the *netBufferList* parameter set to **NULL**.

If a callout needs to abort tagging operations early, contexts can be removed by calling [**FwpsNetBufferListRemoveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551194). Removing a context generally triggers an **FWPS\_NET\_BUFFER\_LIST\_CONTEXT\_REMOVED** event. For more information about the events that can be triggered, see the [**FWPS\_NET\_BUFFER\_LIST\_EVENT\_TYPE0**](https://msdn.microsoft.com/library/windows/hardware/ff552403) enumeration. In some cases no event will be triggered, such as when the packet never enters the TCP/IP stack for processing.

When a tagged packet is cloned, the callout driver can move or copy the context to the clone packet. To move the context (in the case of a clone), the callout driver must call [**FwpsNetBufferListRetrieveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551196) with the *removeContext* parameter set to **TRUE**. Then the context can be associated with the new packet. The process for copying the context (in the case of a duplication) is the same except that the *removeContext* parameter of **FwpsNetBufferListRetrieveContext0** must be set to **FALSE**.

Packets tagged from TCP/IP layers can be retrieved from an [NDIS filter driver](ndis-filter-drivers2.md). The reverse is also true. Packet tagging is not available from stream layers where no packets are indicated except data segments.

A callout driver can retrieve the context for a packet outside of the [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0*](https://msdn.microsoft.com/library/windows/hardware/ff552406) or [*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](https://msdn.microsoft.com/library/windows/hardware/hh451260) function by calling [**FwpsNetBufferListRetrieveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551196). Typically, a callout driver will retrieve the context in its [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callback.

## Related topics


[classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887)

[**FWPS\_NET\_BUFFER\_LIST\_EVENT\_TYPE0**](https://msdn.microsoft.com/library/windows/hardware/ff552403)

[*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0*](https://msdn.microsoft.com/library/windows/hardware/ff552406)

[*FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN1*](https://msdn.microsoft.com/library/windows/hardware/hh451260)

[**FwpsNetBufferListAssociateContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551191)

[**FwpsNetBufferListGetTagForContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551192)

[**FwpsNetBufferListRemoveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551194)

[**FwpsNetBufferListRetrieveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551196)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

[NDIS Filter Drivers](ndis-filter-drivers2.md)

 

 






