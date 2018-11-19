---
Description: You need to write a driver for the connector if your USB Type-C system does not include an embedded controller, otherwise you can load the Microsoft-provided UCSI driver.
title: Developing Windows drivers for USB Type-C connectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developing Windows drivers for USB Type-C connectors
You need to write a driver for the connector if your USB Type-C system does not implement PD state machine or it implements state machine but does not support UCSI over non-ACPI transport. If it does, you can load the Microsoft-provided [UCSI driver](ucsi.md).

**Intended audience**

-   Driver development guidance for a USB Type-C system does not include an embedded controller.

**Last Updated**

-   September 2018

**Windows version**

-   Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)
-   Windows 10 Mobile

**Important APIs**

-   [USB Type-C driver reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#type-c-driver-reference)

![drivers](images/drivers-c.png)


|             Hardware/Firmware capabilities             |                                                                                                                                                    Non-detachable                                                                                                                                                    |                                                                                                                              Add-on card                                                                                                                               |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USB Type-C connector does not have a PD state machine. |        [Write a client driver to UcmTcpciCx](https://docs.microsoft.com/windows-hardware/drivers/usbcon/write-a-usb-type-c-port-controller-driver). <p>Start with [UcmTcpciCx Port Controller Client Driver](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/UcmTcpciCxClientSample) </p>        | [Write a client driver to UcmCx](https://docs.microsoft.com/windows-hardware/drivers/usbcon/bring-up-a-usb-type-c-connector-on-a-windows-system). <p>Start with the [UcmCx sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/UcmCxUcsi).</p> |
|         Connector is UCSI-compliant with ACPI.         |                                                          Load the in-box driver, UcmUcsiCx.sys and UcmUcsiAcpiClient. See [USB Type-C Connector System Software Interface (UCSI) driver](https://docs.microsoft.com/windows-hardware/drivers/usbcon/ucsi).                                                           |                                                                                                                                  N/A                                                                                                                                   |
|       Connector is UCSI-compliant without ACPI.        | Write a client driver to UcmUcsiCx. For more information, see [Write a UCSI client driver](write-a-ucsi-driver.md). <p>Start with [this sample template](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/UcmCxUcsi) and replace the ACPI portions with your implementation for the required bus. |                                                           [Write a client driver to UcmCx](https://docs.microsoft.com/windows-hardware/drivers/usbcon/bring-up-a-usb-type-c-connector-on-a-windows-system).                                                            |
|    Has PD state machine but is not UCSI-compliant.     |                          [Write a client driver to UcmCx](https://docs.microsoft.com/windows-hardware/drivers/usbcon/bring-up-a-usb-type-c-connector-on-a-windows-system). <p>Start with the [UcmCx sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/UcmCxUcsi).                          | [Write a client driver to UcmCx](https://docs.microsoft.com/windows-hardware/drivers/usbcon/bring-up-a-usb-type-c-connector-on-a-windows-system)<p>Start with the [UcmCx sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/UcmCxUcsi). </p>  |

## In this section
To implementation the proposed solutions in the preceding table, read these topics:
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="architecture--usb-type-c-in-a-windows-system.md" data-raw-source="[Architecture: USB Type-C design for a Windows system](architecture--usb-type-c-in-a-windows-system.md)">Architecture: USB Type-C design for a Windows system</a></p></td>
<td><p>Describes a typical hardware design of a USB Type-C system and the Microsoft-provided drivers that support the hardware components.</p></td>
</tr>
<tr class="even">
<td><p><a href="function-controller-bringup-for-a-usb-type-c-system.md" data-raw-source="[Bring up the function controller on a USB Type-C Windows system](function-controller-bringup-for-a-usb-type-c-system.md)">Bring up the function controller on a USB Type-C Windows system</a></p></td>
<td><p>The driver for the function controller informs the operating system about the charging levels that its USB Type-C connector supports and notifies the battery subsystem when it can begin charging and the maximum amount of current the device can draw.</p></td>
</tr>
<tr class="odd">
<td><p><a href="dual-role-controller-bringup-for-a-usb-type-c-system.md" data-raw-source="[Bring up the dual-role controller for a USB Type-C Windows system](dual-role-controller-bringup-for-a-usb-type-c-system.md)">Bring up the dual-role controller for a USB Type-C Windows system</a></p></td>
<td><p>The USB role-switch drivers (URS) are a set of WDF class extension and its client driver that handles the role-switching capability of a dual-role controller. If your system has a dual role controller, you can switch the role of the system depending on the device that is attached to the partner port of the USB Type-C connector of the system. This allows interesting scenarios such as wired docking.</p></td>
</tr>
<tr class="even">
<td><p><a href="bring-up-a-usb-type-c-connector-on-a-windows-system.md" data-raw-source="[Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md)">Write a USB Type-C connector driver</a></p></td>
<td><p>Describes the USB connector manager (UCM) that manages a USB Type-C connector and the expected behavior of a connector driver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="write-a-usb-type-c-port-controller-driver.md" data-raw-source="[Write a USB Type-C port controller driver](write-a-usb-type-c-port-controller-driver.md)">Write a USB Type-C port controller driver</a></p></td>
<td><p>Describes how to write a the USB Type-C port controller driver that communicates with a USB Type-C connector without PD state machine. </p></td>

</tr>
<tr class="even">
<td><p><a href="write-a-ucsi-driver.md" data-raw-source="[Write a UCSI client driver](write-a-ucsi-driver.md)">Write a UCSI client driver</a></p></td>
<td><p>Describes how to write a driver for a UCSI-compliant controller that uses non-ACPI transport. </p></td>

</tr>

<tr>
<tr class="odd">
<td><a href="policy-manager-client.md" data-raw-source="[Write a USB Type-C Policy Manager client driver](policy-manager-client.md)">Write a USB Type-C Policy Manager client driver</a></td>
<td>The Microsoft-provided USB Type-C Policy Manager monitors the activities of USB Type-C connectors. Windows, version 1809, introduces a set of programming interfaces that you can use to write a client driver to Policy Manager. The client driver can participate in the policy decisions for USB Type-C connectors. With this set, you can choose to write a kernel-mode export driver or a user-mode driver. </td>
</tbody>
</table>



**Related sections**

[Write a USB role-switch (URS) client driver ](usb-dual-role-driver-stack-architecture.md)

[USB dual-role controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt628026)

[Write a USB function client driver](developing-windows-drivers-for-usb-function-controllers.md)  

[USB function controller programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188013)

## Related topics

[Windows support for USB Type-C connectors](oem-tasks-for-bringing-up-a-usb-typec.md)  





