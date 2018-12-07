---
Description: Frequently asked questions for OEMs who want to build Windows systems with USB Type-C connectors.
title: FAQ - USB Type-C connector on a Windows system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# FAQ: USB Type-C connector on a Windows system


**Last Updated**

-   December 2016

**Windows version**

-   Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)
-   Windows 10 Mobile

Frequently asked questions for OEMs who want to build Windows systems with USB Type-C connectors.

-   [USB Type-C connector features](#features)
-   [Does the operating system have any input into which alternate mode needs to be negotiated? For instance, DP 2-lane vs. DP 4-lane?](#does-the-operating-system-have-any-input-into-which-alternate-mode-needs-to-be-negotiated--for-instance--dp-2-lane-vs--dp-4-lane-)
-   [How does pre-OS charging with Type-C and PD work?](#how-does-pre-os-charging-with-type-c-and-pd-work-)
-   [How can I charge the phone when it is a USB host, to enable docking scenarios like Continuum?](#how-can-i-charge-the-phone-when--it-is-a-usb-host--to-enable-docking-scenarios-like-continuum-)
-   [Does Windows 10 Mobile support USB billboard devices?](#does-windows-10-mobile-support-usb-billboard-devices--)
-   [Do Windows 8.1, Windows 8, Windows 7 support USB Type-C?](#do-windows-8-1--windows-8--windows-7-support-usb-type-c--)
-   [Is UCSI supported on Windows 8.1, Windows 8, Windows 7?](#is-ucsi-supported-on-windows-8-1--windows-8--windows-7-)
-   [How do we test our implementation of UCSI?](#how-do-we-test-our-implementation-of-ucsi-----)
-   [What is the exact condition and UI for the different errors?](#what-is-the-exact-condition-and-ui-for-the-different-errors-)
-   [What happens when a non-PD port is connected to PD provider? Conversely, what happens when a PD consumer is connected to a system that is not a PD provider?](#what-happens-when-a-non-pd-port-is-connected-to-pd-provider-----conversely--what-happens-when-a-pd-consumer-is-connected-to-a-system-that-is-not-a-pd-provider-----)
-   [What happens when Thunderbolt, SuperMHL, or PCI express, is connected to a PC that does not support those capabilities?](#what-happens-when-thunderbolt--supermhl--or-pci-express--is-connected-to-a-pc-that-does-not-support-those-capabilities-----)
-   [Is MTP over USB Type-C supported in Windows? Are there any limitations?](#is--mtp-over-usb-type-c-supported-in-windows--are--there-any-limitations-)
-   [How do downstream devices and hubs connect and communicate with USB Connector Manager (UCM)?](#how-do-downstream-devices-and-hubs-connect-and-communicate-with-usb-connector-manager--ucm------)
-   [Do I need a USB Type-C MUTT for HLK tests?](#do-i-need-a-usb-type-c-mutt-for-hlk-tests-)
-   [Will Microsoft support P2P data transfer between same Windows 10 SKU?](#will-microsoft-support-p2p-data-transfer-between-same-windows-10-sku-----)
-   [Does UCM class extension (UcmCx) communicate with PMIC or battery driver to get/set charging status or does the client driver that supports PD need to communicate with the PMIC or battery driver directly?](#does-ucm-class-extension--ucmcx--communicate-with-pmic-or-battery-driver-to-get-set-charging-status-or-does-the-client-driver-that-supports-pd-need-to-communicate-with-the-pmic-or-battery-driver-directly-----)
-   [Does the HLK support USB Type-C?](#does-the-hlk-support-usb-type-c-----)
-   [What is UCSI?](#what-is-ucsi-)
-   [How can we check if our UCSI implementation works correctly with Windows 10?](#how-can-we-check-if-our-ucsi-implementation-works-correctly-with-windows-10-----)
-   [How do I test my UCMCx client driver on Windows 10 to make sure it meets Windows's requirement? What's tool or method can be used to test on Windows by user?](#how-do-i-test-my-ucmcx-client-driver-on-windows-10-to-make-sure-it-meets-windows-s-requirement--what-s-tool-or-method-can-be-used-to-test-on-windows-by-user-----)
-   [Is VBus/VConn control and role switch operations handled by the UCM class extension? Or partner would need to implement Event callback function to handle VBUS control and USB mode switch.](#is-vbus-vconn-control-and-role-switch-operations-handled-by-the-ucm-class-extension--or-partner-would-need-to-implement-event-callback-function-to-handle-vbus-control-and-usb-mode-switch-----)

## USB Type-C connector features


-   **Symmetric and reversible design**
    -   The connector is *symmetric*. The cable has a USB Type-C connector on each end allowing the host and function device to use USB Type-C connectors. Here is an image that compares the connectors:
    -   The connector is designed to be *reversible*. Traditional connectors had to be connected the "right-side-up". With the reversible design, the connector can be flipped.

-   **Supports all USB device speeds**

    The connector can support USB devices that are low-speed, full-speed, high-speed, SuperSpeed (including SS+).

-   **Alternate modes**

    The connector can support *alternate modes*. The alternate mode feature allows non-USB protocols to run over the USB cable, while simultaneously preserving USB 2.0 and charging functionality. Currently, the most popular alternate modes are DisplayPort/DockPort and MHL.

    -   **DisplayPort** /**DockPort**

        This alternate mode allows the user to project audio/video to external DisplayPort displays over a USB connector.

    -   **MHL**

        The MHL alternate mode is allows the user to project video/audio to external displays that support MHL.

-   **Billboard error messages**

    If a user connects a USB Type-C alternate mode device or adapter that is not supported by the attached PC or phone, the device or adapter can expose a Billboard device that contains information about the error condition to help the user troubleshoot issues.

-   **Increased power limits**

    A system with USB Type-C connectors has higher power limits, it can support up to 5V, 3A, 15W.

    In addition, the connector can optionally support the *power delivery* feature as defined by the [USB Power Delivery](http://go.microsoft.com/fwlink/p/?LinkID=623310) OEM . If the connector supports power delivery, a USB Type-C system can be a power source provider or a consumer and support up to 100W.

-   **Supports USB dual roles**

    Peripheral devices can connect to a mobile system with USB Type-C connectors, changing the traditional role of a mobile system from function to host. When the same system is connected to a PC, the system resumes the role of a function and PC becomes the host.

## Does the operating system have any input into which alternate mode needs to be negotiated? For instance, DP 2-lane vs. DP 4-lane?


No. The operating system (or any Microsoft-provided software component) plays no part in selecting an alternate mode. The decision is made by the driver for the connector, specifically the USB connector manager (UCM) client driver. The driver does so by communicating with the connector's firmware by using hardware interfaces.

## How does pre-OS charging with Type-C and PD work?


Enabling pre-OS charging is owned by the OEM. You can choose to not implement [USB Power Delivery](http://go.microsoft.com/fwlink/p/?LinkID=623310), and charge at USB Type-C power levels until you boot into the operating system.

## How can I charge the phone when it is a USB host, to enable docking scenarios like Continuum?


Here are a few things to consider:

-   You must to implement [USB Power Delivery](http://go.microsoft.com/fwlink/p/?LinkID=623310), so that power and data roles can be swapped independently.
-   Your dock’s upstream port should be implemented as a Charging UFP, defined in the USB Type-C specification. For details, see section 4.8.4, version 1.1.
-   Your dock should request a DR\_Swap if it resolved to a DFP, or a PR\_Swap if it resolved to a UFP.

    The initial DFP is the power source, so you must change the data role. The initial UFP is the power sink, so you must change the power role. You can perform those operations in your implementation of these callback functions:

## Does Windows 10 Mobile support USB billboard devices?


Yes, if you connect the phone to a device that supports a USB Billboard, as per the [USB Device Class Definition for Billboard Devices specification](http://go.microsoft.com/fwlink/p/?linkid=620207), the user is notified. Your USB connector manager (UCM) client driver is not required to handle the notification. If your system does not recognize the alternate mode, do not enter the mode.

## Do Windows 8.1, Windows 8, Windows 7 support USB Type-C?


No. USB Type-C is not supported on versions of Windows prior to Windows 10.

## Is UCSI supported on Windows 8.1, Windows 8, Windows 7?


No. UCSI is not supported on versions of Windows prior to Windows 10.

## How do we test our implementation of UCSI?


To test your implementation, follow the guidelines given in [USB Type-C manual interoperability test procedures](type.md). We recommend running USB tests in Windows Hardware Lab Kit (HLK) for Windows 10. These tests are listed in [Windows Hardware Certification Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md).

## What is the exact condition and UI for the different errors?


Windows 10 can show a set of USB Type-C error messages to help educate users about the limitations with different combinations of USB Type-C hardware and software. For example, the user might get "Device is charging slowly" message if the charger connected to the USB Type-C connector is not powerful enough, not compatible with the system, or is connected to a non-charging port. For more information, see [Troubleshoot messages for a USB Type-C Windows system](http://go.microsoft.com/fwlink/?LinkId=526894).

## What happens when a non-PD port is connected to PD provider? Conversely, what happens when a PD consumer is connected to a system that is not a PD provider?


The non-PD port attempts to charge the system by using USB Type-C current levels. For more information, see [USB 3.1 and USB Type-C specifications](http://go.microsoft.com/fwlink/p/?LinkId=699515).

## What happens when Thunderbolt, SuperMHL, or PCI express, is connected to a PC that does not support those capabilities?


The alternate mode feature allows non-USB protocols (such as Thunderbolt, SuperMHL) to run over the USB cable, while simultaneously preserving USB 2.0 and charging functionality. If a user connects a USB Type-C alternate mode device or adapter that is not supported by the attached PC or phone running Windows 10, an error condition is detected and a message is shown to the user.

-   If the device or adapter exposes a Billboard device, the user sees information about the error condition to help the troubleshoot issues. Windows 10 provides an in-box driver for a Billboard device and notifies the user that an error has occurred.
-   The user might see an error notification, "Try improving the USB connection". For more information, see [Error messages for a USB Type-C Windows system](introduction-to-usb-type-c-connectors.md#-4).

For the best results, make sure that the alternate mode device or adapter’s requirements are met by PC or phone or cable.

## Is MTP over USB Type-C supported in Windows? Are there any limitations?


Windows 10 for desktop editions supports MTP in the initiator role; Windows 10 Mobile supports MTP in the responder role.

## How do downstream devices and hubs connect and communicate with USB Connector Manager (UCM)?


UCM is its own device stack (see [Architecture: USB Type-C design for a Windows system](architecture--usb-type-c-in-a-windows-system.md)). Windows 10 support for USB Type-C includes the required plumbing to make sure that the different class drivers know how to communicate with the different USB Type-C connectors. In order to get Windows 10 support for USB Type-C, you must plug into the UCM device stack.

## Do I need a USB Type-C MUTT for HLK tests?


The Windows HLK for Windows 10 contains tests for USB host and function controllers. To test your system, use a USB C-A adapter. These tests are listed in [Windows Hardware Certification Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md).

## Will Microsoft support P2P data transfer between same Windows 10 SKU?


This is not a valid connection.

-   You cannot connect two PCs running Windows 10 for desktop editions.
-   You cannot connect two mobile devices running Windows 10 Mobile.

If the user attempts to make such a connection, Windows shows an error message. For more information, see [Error messages for a USB Type-C Windows system](introduction-to-usb-type-c-connectors.md#-6).

The only valid connection is between a Windows Mobile device and Windows desktop device.

## Does UCM class extension (UcmCx) communicate with PMIC or battery driver to get/set charging status or does the client driver that supports PD need to communicate with the PMIC or battery driver directly?


On software-assisted charging platforms, UcmCx communicates with PMIC and the battery subsystem. The client driver may determine the charging levels by communicating with the hardware through hardware interfaces. On hardware-assisted platforms, the embedded controller is responsible for charging. UcmCx takes no part in the process.

## Does the HLK support USB Type-C?


In Windows HLK for Windows 10, there are no USB Type-C specific tests. We recommend running USB tests in Windows HLK for Windows 10. These tests are listed in [Windows Hardware Certification Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md).

## What is UCSI?


USB Type-C Connector System Software Interface (UCSI) Specification describes the capabilities of the USB Type-C Connector System software Interface (UCSI), and explains the registers and data structures, for hardware component designers, system builders, and device driver developers. Get the specification from [this site](http://go.microsoft.com/fwlink/p/?LinkId=703713).

Microsoft provides an in-box driver with Windows, UcmUcsi.sys, that implements the features defined by the specification. This driver is intended for systems with embedded controllers.

## How can we check if our UCSI implementation works correctly with Windows 10?


We recommend running USB tests in Windows HLK for Windows 10. These tests are listed in [Windows Hardware Certification Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md).

## How do I test my UCMCx client driver on Windows 10 to make sure it meets Windows's requirement? What's tool or method can be used to test on Windows by user?


We recommend running USB tests in Windows HLK for Windows 10. These tests are listed in [Windows Hardware Certification Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md).

## Is VBus/VConn control and role switch operations handled by the UCM class extension? Or partner would need to implement Event callback function to handle VBUS control and USB mode switch.


The UCM class extension might get requests from the operating system to change data or power direction of the connector. When it gets those requests, it invokes client driver's implementation of [*EVT\_UCM\_CONNECTOR\_SET\_DATA\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187818) and [*EVT\_UCM\_CONNECTOR\_SET\_POWER\_ROLE*](https://msdn.microsoft.com/library/windows/hardware/mt187819) callback functions (if the connector implements PD). In the implementation, the client driver is expected control the VBUS and VCONN pins. For more information about those callback functions, see [Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md).

 

 




