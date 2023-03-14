---
title: NDIS Poll Mode
description: NDIS Poll Mode is an OS controlled polling execution model that drives the network interface datapath.
keywords:
- NDIS Poll Mode
ms.date: 03/02/2023
ms.localizationpriority: medium
---

# NDIS Poll Mode

## Overview of NDIS Poll Mode

NDIS Poll Mode is an OS controlled polling execution model that drives the network interface datapath.

Previously, NDIS had no formal definition of a datapath execution context. NDIS drivers typically relied on Deferred Procedure Calls (DPCs) to implement their execution model. However using DPCs can overwhelm the system when long indication chains are made and avoiding this problem requires a lot of code that's tricky to get right. NDIS Poll Mode offers an alternative to DPCs and similar execution tools.

NDIS Poll Mode moves the complexity of scheduling decisions away from NIC drivers and into NDIS, where NDIS sets work limits per iteration. To achieve this Poll Mode provides:

1. A mechanism for the OS to exert back pressure on the NIC.

1. A mechanism for the OS to finely control interrupts. 

NDIS Poll Mode is available to NDIS 6.85 and later miniport drivers.

### Problems with the DPC model

The following sequence diagram illustrates a typical example of how an NDIS miniport driver handles a burst of Rx packets using a DPC. In this example the hardware is standard in terms of PCIe NICs. It has a receive hardware queue and an interrupt mask for that queue. 

:::image type="content" source="./images/ndis-traditional-dpc-diagram.png" alt-text="Diagram illustrating the NDIS DPC model.":::

When there's no network activity the hardware has the Rx interrupt enabled. When an Rx packet arrives:
1. The hardware generates an interrupt and NDIS calls the driver’s [*MiniportInterrupt*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_isr) function (ISR).

1. The driver does very little work in the ISR because they run at a very high IRQL. The driver disables the interrupt from the ISR and defers the hardware processing to a [*MiniportInterruptDPC*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_interrupt_dpc) function (DPC). 

1. NDIS eventually calls the driver's DPC and the driver drains any completions from the hardware queue and indicates them to the OS. 
 
Two pain points can affect the network stack when the driver defers I/O operations to a DPC:
 
1. The driver doesn't know if the system is capable of processing all of the data that is being indicated, so the driver has no choice but to drain as many elements as possible from its hardware queue and indicate them up the stack. 

1. Since the driver is using a DPC to defer work from its ISR, all the indications are made at DISPATCH_LEVEL. This can overwhelm the system when long indication chains are made and cause [Bug Check 0x133 DPC_WATCHDOG_VIOLATION](../debugger/bug-check-0x133-dpc-watchdog-violation.md).
 
Avoiding these pain points requires a lot of tricky code in your driver. While you can check if the DPC watchdog is close to the limit with the [**KeQueryDpcWatchdogInformation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerydpcwatchdoginformation) function and break out of the DPC, you still need to build an infrastructure around this in your driver: You need some way to pause for a bit, then continue to indicate the packets, and at the same time you need to synchronize all this with the lifetime of the datapath.

### Introduction to Poll objects 

NDIS Poll Mode introduces the Poll object to resolve the pain points associated with DPCs. A Poll object is an execution context construct. Miniport drivers can use a Poll object in place of a DPC when dealing with datapath operations.

A Poll object offers the following: 

* It provides a way for NDIS to set work limits per iteration. 

* It is closely tied to a notification mechanism. This keeps the OS and the NIC in sync regarding when work needs to be processed. 

* It has a concept of iteration and interrupts built in. When using DPCs, drivers are forced to re-enable the interrupt every time they finish a DPC. When using Poll objects, drivers don't need to re-enable the interrupt each polling iteration because Poll Mode will let your driver know when it's done polling and it's time to re-enable the interrupt again.

* When making scheduling decisions, the system can be smart about whether to run at DISPATCH_LEVEL or PASSIVE_LEVEL. This can allow fine-tuned prioritization of traffic from different NICs and lead to a fairer workload distribution on the machine.

* It has serialization guarantees. Once you are running code from within a Poll object's execution context you are guaranteed that no other code related to the same execution context will run. This allows a NIC driver to have a lock free implementation of its datapath. 

### The NDIS Poll Mode model

The following sequence diagram illustrates how the same hypothetical PCIe NIC driver handles a burst of Rx packets using a Poll object instead of a DPC. 

:::image type="content" source="./images/ndis-poll-mode-sequence-diagram.png" alt-text="Diagram illustrating NDIS Poll Mode.":::

Like the DPC model, when an Rx packet arrives the hardware generates an interrupt, NDIS calls the driver’s ISR, and the driver disables the interrupt from the ISR. At this point the Poll Mode model diverges:

1. Instead of queueing a DPC, the driver [queues a Poll object](#queuing-a-poll-object-for-execution) (that it [previously created](#creating-a-poll-object)) from the ISR to notify NDIS that new work is ready to be processed.

1. At some point in the future NDIS calls the driver's [poll iteration handler](#implementing-the-poll-iteration-handler) to process the work. Unlike a DPC, the driver is not allowed to indicate as many Rx NBLs as there are elements ready in its hardware queue. The driver should instead check the handler's poll data parameter to get the maximum number of NBLs it can indicate.
 
    Once the driver fetches up to the maximum number of Rx packets it should initialize NBLs, add them to the NBL queue provided by the poll handler, and exit the callback. The driver shouldn't enable the interrupt before exiting.

1. NDIS continues to poll the driver until it assesses that the driver is no longer making forward progress. At this point NDIS will stop polling and ask the driver to [re-enable the interrupt](#managing-interrupts).

## Creating a Poll object

To create a Poll object, the miniport driver does the following in its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) callback function:
1. Allocates a private miniport context.
1. Allocates an [**NDIS_POLL_CHARACTERISTICS**](/windows-hardware/drivers/ddi/poll/ns-poll-ndis_poll_characteristics) structure to specify entry points for the [*NdisPoll*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_poll) and [*NdisSetPollNotification*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_set_poll_notification) callback functions.
1. Calls [**NdisRegisterPoll**](/windows-hardware/drivers/ddi/poll/nf-poll-ndisregisterpoll) to create the Poll object and store it in the miniport context.

The following example shows how a miniport driver might create a Poll object for a receive queue flow. Error handling is omitted for simplicity.

```C++
NDIS_SET_POLL_NOTIFICATION NdisSetPollNotification; 
NDIS_POLL NdisPoll; 

NDIS_STATUS 
MiniportInitialize( 
    _In_ NDIS_HANDLE NdisAdapterHandle, 
    _In_ NDIS_HANDLE MiniportDriverContext, 
    _In_ NDIS_MINIPORT_INIT_PARAMETERS * MiniportInitParameters 
) 
{ 
    // Allocate a private miniport context 
    MINIPORT_CONTEXT * miniportContext = ...;
 
    NDIS_POLL_CHARACTERISTICS pollCharacteristics; 
    pollCharacteristics.Header.Type = NDIS_OBJECT_TYPE_DEFAULT; 
    pollCharacteristics.Header.Revision = NDIS_POLL_CHARACTERISTICS_REVISION_1; 
    pollCharacteristics.Header.Size = NDIS_SIZEOF_NDIS_POLL_CHARACTERISTICS_REVISION_1; 
    pollCharacteristics.SetPollNotificationHandler = NdisSetPollNotification; 
    pollCharacteristics.PollHandler = NdisPoll; 

    // Create a Poll object and store it in the miniport context 
    NdisRegisterPoll( 
        NdisAdapterHandle, 
        miniportContext, 
        &pollCharacteristics, 
        &miniportContext->RxPoll); 
 
    return NDIS_STATUS_SUCCESS; 
} 
```

## Queuing a Poll object for execution 

From an ISR, miniport drivers call [**NdisRequestPoll**](/windows-hardware/drivers/ddi/poll/nf-poll-ndisrequestpoll) to  queue a Poll object for execution. The following example shows receive handling but ignores the sharing of interrupt lines for simplicity.  

```C++
BOOLEAN 
MiniportIsr( 
  KINTERRUPT * Interrupt, 
  void * Context 
) 
{ 
    auto miniportContext = static_cast<MINIPORT_CONTEXT *>(Context); 
    auto hardwareContext = miniportContext->HardwareContext; 

    // Check if this interrupt is due to a received packet 
    if (hardwareContext->ISR & RX_OK) 
    { 
        // Disable the receive interrupt and queue the Poll 
        hardwareContext->IMR &= ~RX_OK; 
        NdisRequestPoll(miniportContext->RxPoll, nullptr); 
    }

    return TRUE; 
} 
```

## Implementing the Poll iteration handler

NDIS invokes the miniport driver's [*NdisPoll*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_poll) callback to poll for receive indications and send completions. NDIS first invokes *NdisPoll* when the driver calls [**NdisRequestPoll**](/windows-hardware/drivers/ddi/poll/nf-poll-ndisrequestpoll) to queue a Poll object.
NDIS will keep invoking *NdisPoll* while the driver is making forward progress on receive indications or transmit completions. 

For receive indications, the driver should do the following in *NdisPoll*:
1. Check the **receive** parameter of the [**NDIS_POLL_DATA**](/windows-hardware/drivers/ddi/poll/ns-poll-ndis_poll_data) structure to get the maximum number of NBLs it can indicate.
1. Fetch up to the maximum number of Rx packets.
1. Initialize the NBLs.
1. Add them to the NBL queue provided by the [**NDIS_POLL_RECEIVE_DATA**](/windows-hardware/drivers/ddi/poll/ns-poll-ndis_poll_receive_data) structure (located in the [**NDIS_POLL_DATA**](/windows-hardware/drivers/ddi/poll/ns-poll-ndis_poll_data) structure of the *NdisPoll* **PollData** parameter). 
1. Exit the callback. 

For transmit completions, the driver should do the following in *NdisPoll*:
1. Check the **transmit** parameter of the [**NDIS_POLL_DATA**](/windows-hardware/drivers/ddi/poll/ns-poll-ndis_poll_data) structure to get the maximum number of NBLs it can complete.
1. Fetch up to the maximum number of Tx packets. 
1. Complete the NBLs.
1. Add them to the NBL queue provided by the [**NDIS_POLL_TRANSMIT_DATA**](/windows-hardware/drivers/ddi/poll/ns-poll-ndis_poll_transmit_data) structure (located in the [**NDIS_POLL_DATA**](/windows-hardware/drivers/ddi/poll/ns-poll-ndis_poll_data) structure of the *NdisPoll* **PollData** parameter).
1. Exit the callback. 

The driver shouldn't enable the Poll object's interrupt before exiting the *NdisPoll* function. NDIS will keep polling the driver until it assesses that no forward progress is being made. At this point NDIS will stop polling and ask the driver to [re-enable the interrupt](#managing-interrupts).

Here's how a driver might implement *NdisPoll* for a receive queue flow.

```C++
_Use_decl_annotations_ 
void 
NdisPoll( 
    void * Context, 
    NDIS_POLL_DATA * PollData 
) 
{ 
    auto miniportContext = static_cast<MINIPORT_CONTEXT *>(Context); 
    auto hardwareContext = miniportContext->HardwareContext; 

    // Drain received frames 
    auto & receive = PollData->Receive; 
    receive.NumberOfRemainingNbls = NDIS_ANY_NUMBER_OF_NBLS; 
    receive.Flags = NDIS_RECEIVE_FLAGS_SHARED_MEMORY_VALID; 

    while (receive.NumberOfIndicatedNbls < receive.MaxNblsToIndicate) 
    { 
        auto rxDescriptor = HardwareQueueGetNextDescriptorToCheck(hardwareContext->RxQueue); 

        // If this descriptor is still owned by hardware stop draining packets 
        if ((rxDescriptor->Status & HW_OWN) != 0) 
            break; 

        auto nbl = MakeNblFromRxDescriptor(miniportContext->NblPool, rxDescriptor); 

        AppendNbl(&receive.IndicatedNblChain, nbl); 
        receive.NumberOfIndicatedNbls++; 

        // Move to next descriptor 
        HardwareQueueAdvanceNextDescriptorToCheck(hardwareContext->RxQueue); 
    } 
} 
```

## Managing interrupts

Miniport drivers implement the [*NdisSetPollNotification*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_set_poll_notification) callback to enable or disable the interrupt associated with a Poll object. NDIS typically invokes the *NdisSetPollNotification* callback when it detects that the miniport driver is not making forward progress in [*NdisPoll*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_poll). NDIS uses *NdisSetPollNotification* to tell the driver that it will stop invoking *NdisPoll*. The driver should invoke [**NdisRequestPoll**](/windows-hardware/drivers/ddi/poll/nf-poll-ndisrequestpoll) when new work is ready to be processed.

Here's how a driver might implement *NdisSetPollNotification* for a receive queue flow.

```C++
_Use_decl_annotations_ 
void 
NdisSetPollNotification( 
    void * Context, 
    NDIS_POLL_NOTIFICATION * Notification 
) 
{ 
    auto miniportContext = static_cast<MINIPORT_CONTEXT *>(Context); 
    auto hardwareContext = miniportContext->HardwareContext; 

    if (Notification->Enabled) 
    { 
        hardwareContext->IMR |= RX_OK; 
    } 
    else 
    { 
        hardwareContext->IMR &= ~RX_OK; 
    } 
} 
```
