---
Description: Describes the USB connector manager (UCM) that manages a USB Type-C connector and the expected behavior of a connector driver.
title: Write a USB Type-C connector driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Write a USB Type-C connector driver

You need to write a USB Type-C connector driver in these scenarios:

-   If your USB Type-C hardware has the capability of handling the power delivery (PD) state machine. Otherwise, consider writing a USB Type-C port controller driver. For more information, see [Write a USB Type-C port controller driver](write-a-usb-type-c-port-controller-driver.md).

-   If your hardware does not have an embedded controller. Otherwise load the Microsoft provided in-box driver, UcmUcsi.sys. (See [UCSI driver](ucsi.md)) for ACPI transports or [write a UCSI client driver](write-a-ucsi-driver.md) for non-ACPI transports. 

**Summary**

-   UCM object used by the class extension and client driver
-   Services provided by the UCM class extension
-   Expected behavior of the client driver

**Official specifications**

-   [USB 3.1 and USB Type-C specifications](http://go.microsoft.com/fwlink/p/?LinkId=699515)
-   [USB Power Delivery](http://go.microsoft.com/fwlink/p/?LinkID=623310)

**Applies to:**

-   Windows 10

**WDF version**

-   KMDF version 1.15
-   UMDF version 2.15

**Last updated:**

-   November 2015

**Important APIs**

-  [USB Type-C connector driver programming reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#type-c-driver-reference)

Describes the USB connector manager (UCM) that manages a USB Type-C connector and the expected behavior of a connector driver.

UCM is designed by using the WDF class extension-client driver model. The class extension (UcmCx) is a Microsoft-provided WDF driver that provides interfaces that the client driver can call to report information about the connector. The UCM client driver uses the hardware interfaces of the connector and keeps the class extension aware of events that occur on the connector. Conversely, the class extension invokes callback functions implemented by the client driver in response to operating system events.

To enable a USB Type-C connector on a system, you must write the client driver.

![usb connector manager](images/type-c-devnode.png)

## Before you begin...


-   [Install](http://go.microsoft.com/fwlink/p/?LinkID=623310) the latest Windows Driver Kit (WDK) on your development computer. The kit has the required header files and libraries for writing a UCM client driver, specifically, you'll need:

    -   The stub library, (UcmCxstub.lib). The library translates calls made by the client driver and pass them up to UcmCx.
    -   The header file, UcmCx.h.

    You can write a UCM client driver that runs in user mode or kernel mode. For user mode, it binds with the UMDF 2.x library; for kernel mode it's KMDF 1.15. Programming interfaces are identical for either mode.

    ![visual studio configuration for ucm](images/ucm-vs.png)

-   Decide whether your client driver will support advanced features of the USB Type-C connector and the [USB Power Delivery](http://go.microsoft.com/fwlink/p/?LinkID=623310).

    This support enables you to build Windows devices with USB Type-C connectors, USB Type-C docks and accessories, and USB Type-C chargers. The client driver reports connector events that allow the operating system to implement policies around USB and power consumption in the system.

-   Install Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) on your target computer or Windows 10 Mobile with a USB Type-C connector.
-   Familiarize yourself with UCM and how it interacts with other Windows drivers. See [Architecture: USB Type-C design for a Windows system](architecture--usb-type-c-in-a-windows-system.md).
-   Familiarize yourself with Windows Driver Foundation (WDF). Recommended reading: [Developing Drivers with Windows Driver Foundation]( http://go.microsoft.com/fwlink/p/?LinkId=691676), written by Penny Orwick and Guy Smith.

## Summary of the services provided by the UCM class extension


The UCM class extension keeps the operating system informed about the changes in data and power role, charging levels, and the negotiated PD contract. While the client driver interacts with the hardware, it must notify the class extension when those changes occur. The class extension provides a set of methods that the client driver can use to send the notifications (discussed in this topic). Here are the services provided:

-   **Data role configuration**

    On USB Type-C systems, the data role (host or function) depends on the status of the CC pins of the connector. Your client driver reads the CC line (see [Architecture: USB Type-C design for a Windows system](architecture--usb-type-c-in-a-windows-system.md)) status from your port controller to determine whether the port has resolved to an Upstream Facing Port (UFP) or Downstream Facing Port (UFP). It reports that information to the class extension so that it can report the current role to USB role-switch drivers.

    **Note**  USB role-switch drivers are used on Windows 10 Mobile systems. On Windows 10 for desktop editions systems, communication between the class extension and the role-switch drivers is optional. Such systems might not use a dual-role controller, in which case, the role-switch drivers are not used.



-   **Power role and charging**

    Your client driver reads the USB Type-C current advertisement, or negotiates a PD power contract with the partner connector.

    -   On a Windows 10 Mobile system, the decision to choose the appropriate charger is software-assisted. The client driver reports the contract information to the class extension so that it can send the charging levels to the charging arbitration driver (CAD.sys). CAD selects the current level to use and forwards the charging level information to the battery subsystem.
    -   On a Windows 10 for desktop editions system, the appropriate charger is selected by the hardware. The client driver may choose to get that information and forward it to the class extension. Alternately, that logic may be implemented by a different driver.
-   **Data and power role changes**

    After a PD contract has been negotiated, data roles and power roles might change. That change might be initiated by your client driver or the partner connector. The client driver reports that information to the class extension, so that it may re-configure things accordingly.

-   **Data and/or power role update**

    The operating system might decide that the current data role is not correct. In that case the class extension calls your driver's callback function to perform necessary role swap operations.

> The Microsoft-provided USB Type-C Policy Manager monitors the activities of USB Type-C connectors. Windows, version 1809, introduces a set of programming interfaces that you can use to write a client driver to Policy Manager. The client driver can participate in the policy decisions for USB Type-C connectors. With this set, you can choose to write a kernel-mode export driver or a user-mode driver. For more information, see [Write a USB Type-C Policy Manager client driver](policy-manager-client.md).

## Expected behavior of the client driver


Your client driver is responsible for these tasks:

-   Detect changes on CC line and determine the type of partner, such as UFP, DFP, and others. To do this, the driver must implement the full Type-C state machine as defined in the USB Type-C specification.
-   Configure your Mux based on the orientation detected on the CC line. This includes turning on your PD transmitter/receiver and handling and responding to PD messages. To do this, the driver must implement the full PD receiver and transmitter state machines as defined in the USB Power Delivery 2.0 specification.
-   Make PD policy decisions, such as negotiating a contract (as source or sink), role swaps, and others. The client driver is responsible for determining the most appropriate contract.
-   Advertise and negotiate alternate modes, and configure the Mux if an alternate mode is detected. The client driver is responsible for deciding the alternate mode to negotiate.
-   Control of VBus/VConn over the connector.

## 1. Initialize the UCM connector object (UCMCONNECTOR)


The UCM connector object (UCMCONNECTOR) represents the USB Type-C connector and is the main handle between the UCM class extension and the client driver. The object tracks the connector's operating modes and power sourcing capabilities.

Here is the summary of the sequence in which the client driver retrieves a UCMCONNECTOR handle for the connector. Perform these tasks in your driver's

1.  Call [**UcmInitializeDevice**](https://msdn.microsoft.com/library/windows/hardware/mt187920) by passing the reference to a [**UCM\_MANAGER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/mt187932) structure. The driver must call this method in the [**EVT_WDF_DRIVER_DEVICE_ADD**](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function before calling [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

2.  Specify the initialization parameters for the USB Type-C connector in a [**UCM\_CONNECTOR\_TYPEC\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/mt187930) structure. This includes the operating mode of the connector, whether it's a downstream-facing port, upstream-facing port, or is dual-role capable. It also specifies the USB Type-C current levels when the connector is a power source. A USB Type-C connector can be designed such that it can act a 3.5 mm audio jack. If the hardware supports the feature, the connector object must be initialized accordingly.

    In the structure, you must also register the client driver's callback function for handling data roles.

    This callback function is associated with the connector object, which is invoked by UCM class extension. This function must be implemented by the client driver.

    [*EVT\_UCM\_CONNECTOR\_SET\_DATA\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187818)  
    Swaps the data role of the connector to the specified role when attached to a partner connector.

3.  If your client driver wants to be PD-capable, that is, handle the Power Delivery 2.0 hardware implementation of the connector, you must also initialize a [**UCM\_CONNECTOR\_PD\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/mt187924) structure that specifies the PD initialization parameters. This includes the flow of power, whether the connector is a power sink or source.

    In structure, you must also register the client driver's callback function for handling power roles.

    This callback function is associated with the connector object, which is invoked by UCM class extension. This function must be implemented by the client driver.

    [*EVT\_UCM\_CONNECTOR\_SET\_POWER\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187819)  
    Sets the power role of the connector to the specified role when attached to a partner connector.

4.  Call [**UcmConnectorCreate**](https://msdn.microsoft.com/library/windows/hardware/mt187909) and retrieve a UCMCONNECTOR handle for the connector. Make sure you call this method after the client driver has created the framework device object by calling [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926). An appropriate place for this call can be in driver's [**EVT_WDF_DEVICE_PREPARE_HARDWARE**](https://msdn.microsoft.com/library/windows/hardware/ff540880) or [**EVT_WDF_DEVICE_D0_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff540848).

```cpp
EVT_UCM_CONNECTOR_SET_DATA_ROLE     EvtSetDataRole;

NTSTATUS
EvtDevicePrepareHardware(
    WDFDEVICE Device,
    WDFCMRESLIST ResourcesRaw,
    WDFCMRESLIST ResourcesTranslated
    )
{
    NTSTATUS status = STATUS_SUCCESS;
    PDEVICE_CONTEXT devCtx;
    UCM_MANAGER_CONFIG ucmCfg;
    UCM_CONNECTOR_CONFIG connCfg;
    UCM_CONNECTOR_TYPEC_CONFIG typeCConfig;
    UCM_CONNECTOR_PD_CONFIG pdConfig;
    WDF_OBJECT_ATTRIBUTES attr;
    PCONNECTOR_CONTEXT connCtx;

    UNREFERENCED_PARAMETER(ResourcesRaw);
    UNREFERENCED_PARAMETER(ResourcesTranslated);

    TRACE_FUNC_ENTRY();

    devCtx = GetDeviceContext(Device);

    if (devCtx->Connector)
    {
        goto Exit;
    }

    //
    // Initialize UCM Manager
    //
    UCM_MANAGER_CONFIG_INIT(&ucmCfg);

    status = UcmInitializeDevice(Device, &ucmCfg);
    if (!NT_SUCCESS(status))
    {
        TRACE_ERROR(
            "UcmInitializeDevice failed with %!STATUS!.",
            status);
        goto Exit;
    }

    TRACE_INFO("UcmInitializeDevice() succeeded.");

    //
    // Create a USB Type-C connector #0 with PD
    //
    UCM_CONNECTOR_CONFIG_INIT(&connCfg, 0);

    UCM_CONNECTOR_TYPEC_CONFIG_INIT(
        &typeCConfig,
        UcmTypeCOperatingModeDrp,
        UcmTypeCCurrentDefaultUsb | UcmTypeCCurrent1500mA | UcmTypeCCurrent3000mA);

    typeCConfig.EvtSetDataRole = EvtSetDataRole;

    UCM_CONNECTOR_PD_CONFIG_INIT(&pdConfig, UcmPowerRoleSink | UcmPowerRoleSource);

    connCfg.TypeCConfig = &typeCConfig;
    connCfg.PdConfig = &pdConfig;

    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attr, CONNECTOR_CONTEXT);

    status = UcmConnectorCreate(Device, &connCfg, &attr, &devCtx->Connector);
    if (!NT_SUCCESS(status))
    {
        TRACE_ERROR(
            "UcmConnectorCreate failed with %!STATUS!.",
            status);
        goto Exit;
    }

    connCtx = GetConnectorContext(devCtx->Connector);

    UcmEventInitialize(&connCtx->EventSetDataRole);

    TRACE_INFO("UcmConnectorCreate() succeeded.");

Exit:

    TRACE_FUNC_EXIT();
    return status;
}
```

## 2. Report the partner connector attach event


The client driver must call [**UcmConnectorTypeCAttach**](https://msdn.microsoft.com/library/windows/hardware/mt187915) when a connection to a partner connector is detected. This call notifies the UCM class extension, which further notifies the operating system. At this point the system may start charging at USB Type-C levels.

The UCM class extension also notifies the USB role-switch drivers (URS). Based on the type of partner, URS configures the controller in host role or function role. Before calling this method, make sure the Mux on your system is configured correctly. Otherwise, if the system is in function role, it will connect at an incorrect speed (high-speed instead of SuperSpeed).

```cpp
        UCM_CONNECTOR_TYPEC_ATTACH_PARAMS attachParams;

        UCM_CONNECTOR_TYPEC_ATTACH_PARAMS_INIT(
            &attachParams,
            UcmTypeCPortStateDfp);
        attachParams.CurrentAdvertisement = UcmTypeCCurrent1500mA;

        status = UcmConnectorTypeCAttach(
                    Connector,
                    &attachParams);
        if (!NT_SUCCESS(status))
        {
            TRACE_ERROR(
                "UcmConnectorTypeCAttach() failed with %!STATUS!.",
                status);
            goto Exit;
        }

        TRACE_INFO("UcmConnectorTypeCAttach() succeeded.");
```

## 3. Report USB Type-C advertisement changes


In the initial attach event, the partner connector sends a current advertisement. If the advertisement specifies the current level of the partner connector when partner is a USB Type-C downstream-facing port. Otherwise, the advertisement specifies the current level of the local connector, represented by the UCMCONNECTOR handle (local connector). This initial advertisement might change during the lifetime of the connection. Those changes must be monitored by the client driver.

If the local connector is the power sink and the current advertisement changes, the client driver must detect changes in the current advertisement and report them to the class extension. On Windows 10 Mobile systems, that information is used by CAD.sys and the battery subsystem to adjust the amount of current it is drawing from the source. To report the change in current level to the class extension, the client driver must call [**UcmConnectorTypeCCurrentAdChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187916).

## 4. Report the new negotiated PD contract


If your connector supports PD, after the initial attach event, there are PD messages transferred between the connector and its partner connector. Between both partners, a PD contract is negotiated that determines the current levels that the connector can draw or allow the partner to draw. Each time the PD contract changes, the client driver must call these methods to report the change to the class extension.

-   The client driver must call these methods whenever it gets a source capabilities advertisement (unsolicited or otherwise) from the partner. The local connector (sink) gets an unsolicited advertisement from the partner only when the partner is the source. Also, the local connector can explicitly request source capabilities from the partner that is capable of being the source (even when the partner is currently the sink). That exchanged is done by sending a **Get\_Source\_Caps** message to the partner.
    -   [**UcmConnectorPdPartnerSourceCaps**](https://msdn.microsoft.com/library/windows/hardware/mt187912) to report the source capabilities advertised by the partner connector.
    -   [**UcmConnectorPdConnectionStateChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187911) to report the details of the contract. The contract is described in a Request Data Object, defined in the Power Delivery 2.0 specification.
-   Conversely, the client driver must call these methods each time the local connector (source) advertises source capabilities to the partner. Also, when the local connector receives a **Get\_Source\_Caps** message from the partner, it must respond with the local connector's source capabilities.
    -   [**UcmConnectorPdSourceCaps**](https://msdn.microsoft.com/library/windows/hardware/mt187913) to report the source capabilities that was advertised by the system to the partner connector.
    -   [**UcmConnectorPdConnectionStateChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187911) to report connection capabilities of the currently negotiated PD contract .

## 5. Report battery charging status


The client driver can notify the UCM class extension if the charging level is not adequate. The class extension reports this information to the operating system. The system uses that information to show a user notification that the charger is not optimally charging the system. The charging status can be reported by these methods:

-   [**UcmConnectorChargingStateChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187908)
-   [**UcmConnectorTypeCAttach**](https://msdn.microsoft.com/library/windows/hardware/mt187915)
-   [**UcmConnectorPdConnectionStateChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187911)

Those methods specify charging state. If the reported levels are **UcmChargingStateSlowCharging** or **UcmChargingStateTrickleCharging** (see [**UCM\_CHARGING\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt187921)), the operating system shows the user notification.

## 6. Report PR\_Swap/DR\_Swap events


If the connector receives a power role (PR\_Swap) or data role (DR\_Swap) swap message from partner, the client driver must notify the UCM class extension.

-   [**UcmConnectorDataDirectionChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187910)

    Call this method after a PD DR\_Swap message has been processed. After this call, the operating system reports the new role to URS, which tears down the existing role drivers and loads drivers for the new role.

-   [**UcmConnectorPowerDirectionChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187914)

    Call this method after a PD PR\_Swap message has been processed. After a PR\_Swap, the PD contract needs to be renegotiated. The client driver must report that PD contract negotiation by calling the methods described in [step 4](#pd-contract).

## 7. Implement callback functions to handle power and data role swap requests


The UCM class extension might get requests to change data or power direction of the connector. In that case, it invokes client driver's implementation of [*EVT\_UCM\_CONNECTOR\_SET\_DATA\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187818) and [*EVT\_UCM\_CONNECTOR\_SET\_POWER\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187819) callback functions (if the connector implements PD). The client driver previously registered those functions in its call to [**UcmConnectorCreate**](https://msdn.microsoft.com/library/windows/hardware/mt187909).

The client driver performs role swap operations by using hardware interfaces.

-   [*EVT\_UCM\_CONNECTOR\_SET\_DATA\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187818)

    In the callback implementation, the client driver is expected to:

    1.  Send a PD DR\_Swap message to the port-partner.
    2.  Call [**UcmConnectorDataDirectionChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187910) to notify the class extension that the message sequence has completed successfully or unsuccessfully.

    ```cpp
    EVT_UCM_CONNECTOR_SET_DATA_ROLE     EvtSetDataRole;  

    NTSTATUS  
    EvtSetDataRole(  
        UCMCONNECTOR  Connector,  
        UCM_TYPE_C_PORT_STATE DataRole  
        )  
    {  
        PCONNECTOR_CONTEXT connCtx;  

        TRACE_INFO("EvtSetDataRole(%!UCM_TYPE_C_PORT_STATE!) Entry", DataRole);  

        connCtx = GetConnectorContext(Connector);



    TRACE_FUNC_EXIT();  
    return STATUS_SUCCESS;  
}  
```


-   [*EVT\_UCM\_CONNECTOR\_SET\_POWER\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187819)

    In the callback implementation, the client driver is expected to:

    1.  Send a PD PR\_Swap message to the port-partner.
    2.  Call [**UcmConnectorPowerDirectionChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187914) to notify the class extension that the message sequence has completed successfully or unsuccessfully.

    ```cpp
    EVT_UCM_CONNECTOR_SET_POWER_ROLE     EvtSetPowerRole;  

    NTSTATUS  
    EvtSetPowerRole(  
        UCMCONNECTOR Connector,  
        UCM_POWER_ROLE PowerRole  
        )  
    {  
        PCONNECTOR_CONTEXT connCtx;  

        TRACE_INFO("EvtSetPowerRole(%!UCM_POWER_ROLE!) Entry", PowerRole);  

        connCtx = GetConnectorContext(Connector);  

        //PR_Swap operation.  



    TRACE_FUNC_EXIT();  
    return STATUS_SUCCESS;  
}  
```


**Note**  
The client driver can call [**UcmConnectorDataDirectionChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187910) and [**UcmConnectorPowerDirectionChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187914) asynchronously, that is not from the callback thread. In a typical implementation, the class extension invokes the callback functions causing the client driver to initiate a hardware transaction to send the message. When the transaction completes, the hardware notifies the driver. The driver calls those methods to notify the class extension.



## 8. Report the partner connector detach event


The client driver must call [**UcmConnectorTypeCDetach**](https://msdn.microsoft.com/library/windows/hardware/mt187918) when the connection to a partner connector ends. This call notifies the UCM class extension, which further notifies the operating system.

## Use case example: Mobile device connected to a PC


When a device running Windows 10 Mobile is connected to a PC running Windows 10 for desktop editions over a USB Type-C connection, the operating system makes sure that mobile device is the Upstream Facing Port (UFP) because MTP is functional only in that direction. In this scenario, here is the sequence for data role correction:

1.  The client driver, running on the mobile device, reports an attach event by calling [**UcmConnectorTypeCAttach**](https://msdn.microsoft.com/library/windows/hardware/mt187915) and reports the partner connector as the Downstream Facing Port (UFP).
2.  The client driver reports the PD contract by calling [**UcmConnectorPdPartnerSourceCaps**](https://msdn.microsoft.com/library/windows/hardware/mt187912) and [**UcmConnectorPdConnectionStateChanged**](https://msdn.microsoft.com/library/windows/hardware/mt187911).
3.  The UCM class extension notifies the USB device-side drivers causing those drivers to respond to enumeration from the host. The operating system information is exchanged over USB.
4.  The UCM class extension UcmCx invokes the client driver's callback functions to change roles: [*EVT\_UCM\_CONNECTOR\_SET\_DATA\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187818) and [*EVT\_UCM\_CONNECTOR\_SET\_POWER\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187819).

**Note**  If two Windows 10 Mobile devices are connected to each other, a role swap is not performed, and the user is notified that the connection is not a valid connection.



## Related topics
[Developing Windows drivers for USB Type-C connectors](developing-windows-drivers-for-usb-type-c-connectors.md)  



