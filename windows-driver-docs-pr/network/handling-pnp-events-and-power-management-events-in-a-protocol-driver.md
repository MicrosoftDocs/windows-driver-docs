---
title: Handling PnP and power management events in a protocol driver
description: Handling PnP Events and Power Management Events in a Protocol Driver
ms.assetid: 97cc51f1-7d83-4bf1-87e3-7d986f54e7a1
keywords:
- protocol drivers WDK networking , power management
- NDIS protocol drivers WDK , power management
- protocol drivers WDK networking , Plug and Play
- NDIS protocol drivers WDK , Plug and Play
- power management WDK NDIS protocol
- Plug and Play WDK NDIS protocol
- notifications WDK PnP , NDIS protocol drivers
- event notifications WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling PnP Events and Power Management Events in a Protocol Driver

When the operating system issues a Plug and Play (PnP) I/O request packet (IRP) or a power management IRP to a target device object that represents a network interface card (NIC), NDIS intercepts the IRP. NDIS indicates the event to each bound protocol driver and each bound intermediate driver by calling the driver's [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function. In the call to *ProtocolNetPnPEvent*, NDIS passes a pointer to a [**NET\_PNP\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff568752) that contains a NET\_PNP\_EVENT structure. The NET\_PNP\_EVENT structure describes the PnP event or power management event being indicated. For more information about the protocol driver PnP interface, see [Handling PnP Event Notifications in a Protocol Driver](handling-pnp-event-notifications-in-a-protocol-driver.md).

The following list contains PnP and power management events, as indicated by the **NetEvent** code in the NET\_PNP\_EVENT structure:

-   **NetEventSetPower**

    Indicates a Set Power request, which specifies that the miniport adapter should transition to a particular power state. A power management–aware protocol driver should always succeed this event by returning NDIS\_STATUS\_SUCCESS. An old protocol driver can return NDIS\_STATUS\_NOT\_SUPPORTED to indicate that NDIS should unbind it from the miniport adapter.

    After issuing the set power request, NDIS pauses the driver stack if the miniport adapter is transitioning to a low-power state. NDIS restarts the driver stack before the set-power request if the miniport adapter is transitioning to the working state (D0). For more information about pausing and restarting the driver stack, see [Pausing a Driver Stack](pausing-a-driver-stack.md).

    If the miniport adapter is in a low-power state, the protocol driver cannot issue any OID requests. This requirement is an additional power management restriction that is added to the other restrictions that apply when the driver stack is in the Paused state.

    If the underlying miniport adapter is not power management–aware, the miniport driver sets the **PowerManagementCapabilities** member of [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) to **NULL** and NDIS sets the **PowerManagementCapabilities** member of [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) to **NULL**.

    **Note**  Starting with NDIS 6.30, after being notified of this event, the protocol driver must stop generating new I/O requests and should not wait for the completion of any pending I/O requests within the context of the call to [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263).

    For more information about set-power events, see [Handling PnP Events and Power Management Events in an Intermediate Driver](handling-pnp-events-and-power-management-events-in-an-intermediate-dri.md).

-   **NetEventQueryPower**

    Indicates a Query Power request, which queries whether the underlying miniport adapter can make a transition to a particular power state. A protocol driver should always succeed a **NetEventQueryPower** . After establishing an active connection, a protocol driver can call [**PoRegisterSystemState**](https://msdn.microsoft.com/library/windows/hardware/ff559731) to register a continuous busy state. As long as the state registration is in effect, the power manager does not attempt to put the system to sleep. After the connection becomes inactive, the protocol driver cancels the state registration by calling [**PoUnregisterSystemState**](https://msdn.microsoft.com/library/windows/hardware/ff559794). A protocol driver should never try to prevent the system from transitioning to the sleeping state by failing a **NetEventQueryRemoveDevice**. Note that a **NetEventQueryPower** is always followed by a **NetEventSetPower**. A **NetEventSetPower** that sets the device's current power state in effect cancels the **NetEventQueryPower**.

    **Note**  Starting with NDIS 6.30, after being notified of this event, the protocol driver should not wait for the completion of any pending I/O requests within the context of the call to [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263).

-   **NetEventQueryRemoveDevice**

    Indicates a Query Remove Device request, which queries whether the NIC can be removed without disrupting operations. If a protocol driver cannot release a device (for example, because the device is in use), it must fail a **NetEventQueryRemoveDevice** by returning NDIS\_STATUS\_FAILURE.

-   **NetEventCancelRemoveDevice**

    Indicates a Cancel Remove Device request, which cancels the removal of an underlying NIC. The protocol driver should always succeed this event by returning NDIS\_STATUS\_SUCCESS.

-   **NetEventReconfigure**

    Indicates that the configuration has changed for a network component. For example, if a user changes the IP address for TCP/IP, NDIS indicates this event to the TCP/IP protocol with the **NetEventReconfigure** code. The protocol driver can, in rare circumstances, return a failure code if it is not able to apply the indicated configuration changes and there are no available default values. A failed attempt to allocate memory is an example of a case in which the protocol returns a failure code. Returning an error code can result in prompting the user to restart the system.

    A protocol should validate **NetEventReconfigure**-related data passed to its [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function. For more information about such data, see [**NET\_PNP\_EVENT for Protocol Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff568751).

-   **NetEventBindList**

    Indicates to a protocol driver that its bind list processing order has been reconfigured. This list indicates a relative order to be applied to the protocol's bindings when processing, for example, a user request that might be routed to one of several bindings. The buffer passed with this event contains a list of device names formatted as NULL-terminated Unicode strings. The format of each device name is identical to the *DeviceName* parameter that is passed to a call to [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220).

    A protocol should validate **NetEventBindList**-related data passed to its *ProtocolNetPnPEvent* function. For more information about such data, see [**NET\_PNP\_EVENT for Protocol Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff568751).

    A protocol should validate **NetEventBindList**-related data passed to its *ProtocolNetPnPEvent* function. For more information about such data, see [**NET\_PNP\_EVENT for Protocol Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff568751).

-   **NetEventBindsComplete**

    Indicates that a protocol driver has bound to all the NICs to which it can bind. NDIS will not indicate any more bindings to the protocol driver unless, for example, a PnP NIC is plugged into the system.

-   **NetEventPnPCapabilities**

    Indicates that the user enabled or disabled the wake-up capabilities of the underlying adapter. (The *ProtocolBindingContext* parameter that NDIS passes to *ProtocolNetPnPEvent* specifies the binding .)

-   **NetEventPause**

    Indicates that the specified protocol binding should enter thePausing state. The binding will enter the Paused state after NDIS has completed all of the outstanding send requests for the binding. For more information about pausing a binding, see [Pausing a Binding](pausing-a-binding.md).

-   **NetEventRestart**

    Indicates that the specified protocol binding has entered the Restarting state. After the protocol driver is ready to resume send and receive operations for the binding, the binding enters the Running state. For more information about restarting a binding, see [Restarting a Binding](restarting-a-binding.md).

-   **NetEventPortActivation**

    Indicates the activation of a list of ports that are associated with the specified binding. For more information about pausing a binding, see [Handling the Port Activation PnP Event](handling-the-port-activation-pnp-event.md).

-   **NetEventPortDeactivation**

    Indicates the deactivation of a list of ports that are associated with the specified binding. For more information about pausing a binding, see [Handling the Port Deactivation PnP Event](handling-the-port-deactivation-pnp-event.md).

-   **NetEventIMReEnableDevice**

    Indicates that the configuration has changed for a virtual miniport of an NDIS 6.0 or later intermediate driver. **NetEventIMReEnableDevice** is similar to the **NetEventReconfigure** event except that the intermediate driver receives this event for a single virtual miniport and the **NetEventReconfigure** event applies to all of the intermediate driver's virtual miniports. For example, an intermediate driver receives the **NetEventIMReEnableDevice** event when a user disables and then enables a single virtual miniport from the Device Manager or another source. For examples of intermediate driver power management, see the [NDIS MUX Intermediate Driver and Notify Object](http://go.microsoft.com/fwlink/p/?LinkId=617916) driver sample available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

The **Buffer** member of the NET\_PNP\_EVENT structure points to a buffer that contains information specific to the event being indicated.

A protocol driver can complete the call to *ProtocolNetPnPEvent* asynchronously with [**NdisCompleteNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561705).