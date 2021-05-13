---
title: NDIS Poll Mode
description: Introduction to NDIS Poll Mode
keywords:
- NDIS Poll Mode
ms.date: 05/28/2021
ms.localizationpriority: medium
---

# NDIS Poll Mode

## Overview of NDIS Poll Mode

NDIS Poll Mode is an OS controlled polling execution model that drives the network interface datapath.

((Main problem is solves: improves the system function so it doesn't get overwhelmed?
-does it provide faster packet processing? when would onewantsot use this?

OR (for ex) How RSS improves system performance))

NDIS Poll Mode offers an alternative to the traditional NDIS datapath model where I/O operations are deferred to DPCs. In place of DPCs, NDIS polls the miniport driver for receive indications and send completions. 

Poll Mode gives the OS more flexibility when making scheduling decisions and moves the complexity of those decisions away from NIC drivers into NDIS. To achieve this, Poll Mode provides the following functionality:
1. A mechanism for the OS to exert back pressure on the NIC. 
2. A mechanism for the OS to finely control interrupts. 

NDIS Poll Mode is available to NDIS 6.0 and later miniport drivers.

### The traditional NDIS datapath model
The following sequence diagram illustrates how the hardware and the driver coordinate to handle a burst of Rx packets in the traditional NDIS datapath model. In this example, the hardware is standard in terms of PCIe NICs. It has a receive hardware queue and an interrupt mask for that queue. 

[DPC model diagram]

When there's no network activity the hardware has the Rx interrupt enabled. When an Rx packet arrives:
1. The hardware generates an interrupt and NDIS calls the driver’s [*MiniportInterrupt*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_isr) function (ISR).

1. The driver does very little work in the ISR because they run at a very high IRQL. The driver disables the interrupt from the ISR and defers the hardware processing to a DPC. 

1. NDIS eventually calls the driver's [*MiniportInterruptDPC*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_interrupt_dpc) function and the driver drains any completions from the hardware queue and indicates them to the OS. 
 
Deferring I/O operations to DPCs results in two pain points that can affect the network stack: 
1. The driver has no idea if the system is capable of processing the data that is being indicated, which results in the driver having no choice other than draining as many elements as possible from is hardware queue and indicating up the stack. (What is the consequence of this?)

1. Since the driver is using a DPC to defer work from its ISR all the indications are made at DISPATCH_LEVEL, which can overwhelm the system when longs indication chains are made.  

### Introducing Poll objects 

NDIS Poll Mode resolves the two pain points associated with DPCs by introducing the Poll object. A Poll object is an execution context construct. Miniport drivers can use Poll objects in place of DPCs when dealing with datapath operations. 

The Poll object: 

* Has serialization guarantees. Once you are running code from within a Poll object's execution context you are guaranteed that no other code related to the same execution context will run. This allows a NIC driver to have a lock free implementation of its datapath. 

* Is closely tied to a notification mechanism. This keeps the OS and the NIC in sync regarding when work needs to be processed. 

* The execution can move between IRQL levels transparently to the driver 
* Has a concept of iteration and interrupts built in, so the driver is not forced to reenable interrupts every time it has finished the deferred procedure call (but we aren't using DPCss. )
* Offers a way for NDIS to set work limits per iteration 

### Polling model

The following sequence diagram illustrates how the same hypothetical PCIe NIC driver handles a burst of Rx packets using a Poll object instead of a DPC. 

[Polling diagram]

When an Rx packet arrives:
1. Like the traditional NDIS datapath model, the hardware generates an interrupt and NDIS calls the driver’s [*MiniportInterrupt*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_isr) function (ISR).

1. The driver disables the interrupt from the ISR.

1. Instead of queueing a DPC the driver queues a pre-created and initialized Poll object to notify NDIS that new work is ready to be processed. Specify ndisrequestpoll function? 

1. At some point in the future NDIS calls the driver's [*NdisPoll*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_poll) routine to process the work. However unlike a DPC, the driver is not allowed to indicate as many Rx NBLs as there are elements ready in its hardware queue. Instead the driver should check one of the poll function (speify? or maybe don't mention specifics until below) parameters to know what is the limit. 

Once the driver fetches up to the maximum number of Rx packets it should initialize NBLs and add them to the NBL queue provided by the poll function and exit the callback. Notice how the driver should not enable the interrupt before exiting the poll function. The OS will keep polling the driver until it assesses no forward progress is being made, at which point the OS stops the polling and asks the driver to reenable the interrupt. 

## Creating a Poll object

To create a Poll object, the miniport driver does the following in its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) callback function:
1. Allocates a private miniport context.
1. Allocates an [**NDIS_POLL_CHARACTERISTICS**](/windows-hardware/drivers/ddi/poll/ns-poll-ndis_poll_characteristics) structure to specify entry points for the [*NdisPoll*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_poll) and [*NdisSetPollNotification*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_set_poll_notification) callback functions.
1. Calls [**NdisRegisterPoll**](/windows-hardware/drivers/ddi/poll/nf-poll-ndisregisterpoll) to create the Poll object and store it in the miniport context.


** The following code example provides the implementation for the receive queue flow presented in Section 3. 

The following example shows how a miniport driver might create a Poll object. Note that error handling is omitted for simplicity.

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

In the ISR miniport routine the driver calls [**NdisRequestPoll**](/windows-hardware/drivers/ddi/poll/nf-poll-ndisrequestpoll) to queue the Poll object for execution. For simplicity this example only shows receive handling and ignores the sharing of interrupt lines. 

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

## Poll iteration handler

Miniport drivers implement the [*NdisPoll*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_poll) callback function that NDIS will poll for receive indications and send completions.

**grab decription from ndispoll ddi.

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

## Enabling and disabling Poll notification

or 


## Transferring/Polling? network data (how is this different from ndis?)

## Managing/Handling interrupts

Miniport drivers implement the [*NdisSetPollNotification*](/windows-hardware/drivers/ddi/poll/nc-poll-ndis_set_poll_notification) callback function to enable or disable the interrupt associated with a Poll object.
(to et the OS.NDIS control the interrupt associated with a Poll)

NDIS typically invokes the NdisSetPollNotification callback when it detects that the miniport driver is not making forward progress in NdisPoll. NDIS uses NdisSetPollNotification to tell the driver that it will stop invoking NdisPoll. The driver should invoke NdisRequestPoll when new work is ready to be processed.

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
