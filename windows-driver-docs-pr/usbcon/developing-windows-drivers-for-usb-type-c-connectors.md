---
description: You need to write a driver for the connector if your USB Type-C system does not include an embedded controller, otherwise you can load the Microsoft-provided UCSI driver.
title: Overview of developing Windows drivers for USB Type-C connectors
ms.date: 09/13/2022
---

# Overview of developing Windows drivers for USB Type-C connectors

You need to write a driver for the connector if your USB Type-C system does not implement a PD state machine, or it implements the state machine but does not support UCSI over a non-ACPI transport. If it does, you can load the Microsoft-provided [UCSI driver](./ucsi.md).

:::image type="content" source="images/drivers-c.png" alt-text="Flow chart showing the decision process for implementing a UcmTcpciCx client driver.":::

## Proposed solutions

The following table recommends solutions based on hardware or firmware capabilities:

| Hardware/Firmware capabilities | Non-detachable | Add-on card |
|--|--|--|
| USB Type-C connector does not have a PD state machine. | [Write a client driver to UcmTcpciCx](./write-a-usb-type-c-port-controller-driver.md). </br></br>Start with [UcmTcpciCx Port Controller Client Driver](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/UcmTcpciCxClientSample) | [Write a client driver to UcmCx](./bring-up-a-usb-type-c-connector-on-a-windows-system.md). </br></br>Start with the [UcmCx sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/UcmCxUcsi). |
| Connector is UCSI-compliant with ACPI. | Load the in-box driver, UcmUcsiCx.sys and UcmUcsiAcpiClient. See [USB Type-C Connector System Software Interface (UCSI) driver](./ucsi.md). | N/A |
| Connector is UCSI-compliant without ACPI. | Write a client driver to UcmUcsiCx. For more information, see [Write a UCSI client driver](./write-a-ucsi-driver.md). </br></br>Start with the [UcmCx sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/UcmCxUcsi) and replace the ACPI portions with your implementation for the required bus. | [Write a client driver to UcmCx](./bring-up-a-usb-type-c-connector-on-a-windows-system.md). |
| Has PD state machine but is not UCSI-compliant. | [Write a client driver to UcmCx](./bring-up-a-usb-type-c-connector-on-a-windows-system.md). </br></br>Start with the [UcmCx sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/UcmCxUcsi). | [Write a client driver to UcmCx](./bring-up-a-usb-type-c-connector-on-a-windows-system.md) </br</br>Start with the [UcmCx sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/UcmCxUcsi). |

## In this section

To implement the solutions proposed in the preceding table, read these topics:

| Topic | Description |
|--|--|
| [Architecture: USB Type-C design for a Windows system](./architecture--usb-type-c-in-a-windows-system.md) | Describes a typical hardware design of a USB Type-C system and the Microsoft-provided drivers that support the hardware components. |
| [Bring up the function controller on a USB Type-C Windows system](./function-controller-bringup-for-a-usb-type-c-system.md) | The driver for the function controller informs the operating system about the charging levels that its USB Type-C connector supports and notifies the battery subsystem when it can begin charging and the maximum amount of current the device can draw. |
| [Bring up the dual-role controller for a USB Type-C Windows system](./dual-role-controller-bringup-for-a-usb-type-c-system.md) | The USB role-switch drivers (URS) are a set of WDF class extension and its client driver that handles the role-switching capability of a dual-role controller. If your system has a dual role controller, you can switch the role of the system depending on the device that is attached to the partner port of the USB Type-C connector of the system. This allows interesting scenarios such as wired docking. |
| [Write a USB Type-C connector driver](./bring-up-a-usb-type-c-connector-on-a-windows-system.md) | Describes the USB connector manager (UCM) that manages a USB Type-C connector and the expected behavior of a connector driver. |
| [Write a USB Type-C port controller driver](./write-a-usb-type-c-port-controller-driver.md) | Describes how to write a the USB Type-C port controller driver that communicates with a USB Type-C connector without PD state machine. |
| [Write a UCSI client driver](./write-a-ucsi-driver.md) | Describes how to write a driver for a UCSI-compliant controller that uses non-ACPI transport. |
| [Write a USB Type-C Policy Manager client driver](./policy-manager-client.md) | The Microsoft-provided USB Type-C Policy Manager monitors the activities of USB Type-C connectors. Windows, version 1809, introduces a set of programming interfaces that you can use to write a client driver to Policy Manager. The client driver can participate in the policy decisions for USB Type-C connectors. With this set, you can choose to write a kernel-mode export driver or a user-mode driver. |

## Related sections

- [Write a USB role-switch (URS) client driver ](./usb-dual-role-driver-stack-architecture.md)
- [USB dual-role controller driver programming reference](/previous-versions/windows/hardware/drivers/mt628026(v=vs.85))
- [Write a USB function client driver](./developing-windows-drivers-for-usb-function-controllers.md)
- [USB function controller programming reference](/windows-hardware/drivers/ddi/usbfnbase)

## See also

[Windows support for USB Type-C connectors](./oem-tasks-for-bringing-up-a-usb-typec.md)
- [USB Type-C driver reference](/windows-hardware/drivers/ddi/_usbref/#type-c-driver-reference)
