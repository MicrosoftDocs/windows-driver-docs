---
Description: Here are some example designs for USB Type-C system.
title: Hardware design: USB Type-C systems
---

# Hardware design: USB Type-C systems


**Last Updated**

-   December 2016

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Here are some example designs for USB Type-C system.

A typical USB Type-C system has these components:

-   **USB Dual-Role controller** is capable of operating either in host role or in function/device/peripheral role. This component is integrated into SoC.
-   **Battery Charging 1.2 detection** might be integrated in certain SoCs. Some SoC vendors provide a PMIC module that implements detection logic, others implement in software. Windows 10 Mobile supports all those options. Contact your SoC vendor to get details about this component.
-   **Type-C -PD Port controller** manages CC pins on the USB Type-C connector. Supports BMC encoding/decoding of power delivery messages. This component is usually not integrated in most SoCs.
-   **Mux** SuperSpeed USB pairs to a port on the controller depending on the orientation detected by Type-C port controller. Mux SuperSpeed pairs and possibly SBU lines elsewhere (usually the Display module) when entering an alternate mode.
-   **VBus/VConn** source is required. Most PMICs implement VBus/VConn control. Contact your SoC/PMIC vendor for details.

## <a href="" id="emb"></a>USB Type-C system design with an embedded controller


In addition to the components in the preceding list, a USB Type-C system can have an embedded controller. This intelligent microcontroller that acts as the Type-C and Power Delivery policy manager for the system.

Here is an example of a USB Type-C system with an embedded controller:

![usb type-c hardware design example for embedded controller devices](images/type-c-hw1.png)

Here is another view:

![usb type-c hardware design example for embedded controller devices](images/type-c-hw1-1.png)

For a system that has an embedded controller, load the Microsoft provided in-box driver, UcmUcsi.sys, that implements USB Type-C Connector System Software Interface (UCSI) Specification.

[UCSI driver](ucsi.md). For information about the device stacks loaded for the driver, see [Drivers for supporting USB Type-C components for systems with embedded controllers](architecture--usb-type-c-in-a-windows-system.md#drivers).

## <a href="" id="hardware"></a>USB Type-C system design


Here is an example of a USB Type-C system for a mobile device that does not have an embedded controller:

![usb type-c hardware design example for mobile devices](images/type-c-hw2.png)

Here is another view:

![usb type-c hardware design example device without an embedded controller](images/type-c-hw2-1.png)

For the preceding design, implement a driver that communicates with the connector and keeps the operating system informed about USB Type-C events on the connector.

[Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md)

[UCmCx client driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188011)

## Related topics


[Windows support for USB Type-C connectors](oem-tasks-for-bringing-up-a-usb-typec.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Hardware%20design:%20USB%20Type-C%20systems%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




