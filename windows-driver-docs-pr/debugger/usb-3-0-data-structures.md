---
title: USB 3.0 Data Structures
description: This topic describes the data structures used by the USB 3.0 host controller driver.
ms.assetid: 39BD7413-48A5-4199-BA8E-D2A77E4D23F1
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# USB 3.0 Data Structures


This topic describes the data structures used by the USB 3.0 host controller driver. Understanding these data structures will help you use the [USB 3.0](usb-3-extensions.md) and [RCDRKD](rcdrkd-extensions.md) debugger extension commands effectively. The data structures presented here have names that are consistent with the [USB 3.0 specification](https://go.microsoft.com/fwlink/p?LinkID=224892). Familiarity with the USB 3.0 specification will further enhance your ability to use the extension commands to debug USB 3.0 drivers.

The USB 3.0 host controller driver is part of the USB 3.0 core driver stack. For more information, see [USB Driver Stack Architecture](https://go.microsoft.com/fwlink/p?LinkID=251983).

Each USB 3.0 host controller can have up to 255 devices, and each device can have up to 31 endpoints. The following diagram shows some of the data structures that represent one host controller and the connected devices.

![usb 3.0 data structures that represent one host controller and the connected devices that have device context that in turn have slot and end point context](images/usb3structures01.png)

## <span id="Device_Context_Base_Array"></span><span id="device_context_base_array"></span><span id="DEVICE_CONTEXT_BASE_ARRAY"></span>Device Context Base Array


The Device Context Base Array is an array of pointers to Device Context structures. There is one Device Context structure for each device connected to the host controller. Elements 1 through 255 point to Device Context structures. Element 0 points to a context structure for the host controller.

## <span id="Device_Context_and_Slot_Context"></span><span id="device_context_and_slot_context"></span><span id="DEVICE_CONTEXT_AND_SLOT_CONTEXT"></span>Device Context and Slot Context


A Device Context structure holds an array of pointers to Endpoint Context structures. There is one Endpoint Context structure for each endpoint on the device. Elements 1 through 31 point to Endpoint Context structures. Element 0 points to a Slot Context structure, which holds context information for the device.

## <span id="Command_Ring"></span><span id="command_ring"></span><span id="COMMAND_RING"></span>Command Ring


The Command Ring is used by software to pass commands to the host controller. Some of these commands are directed at the host controller, and some are directed at particular devices connected to the host controller.

## <span id="Event_Ring"></span><span id="event_ring"></span><span id="EVENT_RING"></span>Event Ring


The Event Ring is used by the host controller to pass events to software. That is, the Event Ring is a structure that the host controller uses to inform drivers that an action has completed.

## <span id="Doorbell_Register_Array"></span><span id="doorbell_register_array"></span><span id="DOORBELL_REGISTER_ARRAY"></span>Doorbell Register Array


The Doorbell Register Array is an array of doorbell registers, one for each device connected to the host controller. Elements 1 through 255 are doorbell registers. Element 0 indicates whether there is a pending command in the Command Ring.

Software notifies the host controller that it has device-related or endpoint-related work to perform by writing context information into the doorbell register for the device.

The following diagram continues to the right of the preceding diagram. It shows additional data structures that represent a single endpoint.

![usb 3.0 data structure showing end point context that has multiple trbs that have data and tds](images/usb3structures02.png)

## <span id="Transfer_Ring"></span><span id="transfer_ring"></span><span id="TRANSFER_RING"></span>Transfer Ring


Each endpoint has one or more Transfer Rings. A Transfer Ring is an array of Transfer Request Blocks (TRBs). Each TRB points to a block of contiguous data (up to 64 KB) that will be transferred between hardware and memory as a single unit.

When the USB 3.0 core stack receives a transfer request from a USB client driver, it identifies the Endpoint Context for the transfer, and then breaks the transfer request into one or more Transfer Descriptors (TDs). Each TD contains one or more TRBs.

## <span id="Endpoint_Context"></span><span id="endpoint_context"></span><span id="ENDPOINT_CONTEXT"></span>Endpoint Context


An Endpoint Context structure holds context information for a single endpoint. It also has **Dequeue** and **Enqueue** members, which are used to track where TRBs are being consumed by the hardware and where TRBs are being added by software.

## <span id="related_topics"></span>Related topics


[USB Debugging Innovations in Windows 8](https://go.microsoft.com/fwlink/p/?LinkID=249153)

 

 






