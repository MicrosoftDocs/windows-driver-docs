---
title: Customizing the Component Firmware Update (CFU) driver
description: Customizing the Component Firmware Update (CFU) driver
ms.date: 07/20/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Customizing the Component Firmware Update (CFU) driver

The Microsoft Devices team has announced the release of an open-source model to update the firmware of peripheral devices– Component Firmware Update (CFU). The solution allows seamless and secure firmware update for components connected through interconnect buses such as USB, Bluetooth, I<sup>2</sup>C, and so on. As part of the open-source effort, we are sharing a CFU protocol specification, sample CFU driver, and firmware sample code to allow device manufacturers to push firmware updates over Windows Update.

## Contents

- [Before you begin](#before-you-begin)

- [Overview](#overview)

- [Customize the CFU driver sample](#customize-the-cfu-driver-sample)

  - [1 Choose a deployment approach](#1-choose-a-deployment-approach)

    - [Componentized packages approach (Recommended)](#componentized-packages-approach-recommended)

    - [Monolithic package approach](#monolithic-package-approach)

  - [2 Configure the CFU driver INF](#2-configure-the-cfu-driver-inf)

  - [3 Configure the diagnostic capabilities](#3-configure-the-diagnostic-capabilities)

  - [4 Deploy the package through Windows Update](#4-deploy-the-package-through-windows-update)

- [Firmware file format](#firmware-file-format)

  - [Offer format](#offer-format)

  - [Payload format](#payload-format)

  - [Configure device capabilities in the registry](#configure-device-capabilities-in-the-registry)

  - [Firmware update status provided by the driver](#firmware-update-status-provided-by-the-driver)

- [Troubleshooting tips](#troubleshooting-tips)

- [FAQ](#faq)

- [Additional resources](#additional-resources)

## Before you begin

The following resources will help you learn about the Component Firmware Update (CFU) protocol:

- [Introducing Component Firmware Update](https://blogs.windows.com/buildingapps/?p=54456)

- The [Component Firmware Update (CFU) Protocol Specification](cfu-specification.md) describes a generic HID protocol to update firmware for components present on a PC or accessories. The specification allows for a component to accept firmware without interrupting the device operation during a download.

- [CFU resources on GitHub](https://github.com/Microsoft/CFU)

  - The [CFU Driver](https://github.com/Microsoft/CFU/blob/master/Host) sample is a UMDF driver that talks to the device using the HID protocol. As a firmware developer, you can customize the driver for the purposes of adopting the CFU model to enable firmware updates for your component(s).

  - [CFU Firmware](https://github.com/Microsoft/CFU/blob/master/Firmware) sample code

## Overview

To update the firmware image for your device by using the CFU model, you should expect to meet the following requirements:

- Provide a CFU driver. This driver sends the firmware update to the device. We recommend that you customize the sample CFU driver to support your firmware update scenarios.

- Your device must ship with a firmware image that is compliant with the CFU protocol so that it can accept an update from the CFU driver.

- Your device must expose itself as a HID device to the operating system (running the CFU driver) and expose a HID Top-Level Collection (TLC). The CFU driver loads on the TLC and sends the firmware update to the device.

This allows you to service your in-market devices through Windows Update. To update the firmware for a component, you deploy the CFU driver through the Windows update, and the driver gets installed on a Windows host. When the driver detects the presence of a component, it performs the necessary actions on the host and transmits the firmware image to the primary component on the device.

![CFU firmware update](images/transfer-flowchart.png)

## Customize the CFU driver sample

Customize the CFU driver sample to meet your needs. To do so, choose a deployment package approach, modify the INF file, change the name of the driver binary, and update some logging GUIDs.

### 1 Choose a deployment approach

There are two deployment approaches to packaging the driver and the firmware for: componentized packages or monolithic package.

#### Componentized packages approach (Recommended)

Starting in Windows 10, version 1709, INF functionality can be split into different packages. Using that functionality, split the deployment package into one base package and several extension packages. The base package contains the driver binary and the driver INF that is common for all your devices. The extension package contains the firmware image files and an INF that describes those firmware files for a device.

Base package and extensions packages are serviced independently.

##### When to use the componentized packages approach

###### Componentized packages approach challenges

- This option is only available in Windows 10, version 1709 and later.

###### To create componentized packages

1. Define a base package that contains the common driver binary and an INF that describes the hardware IDs for each device that is going to use the CFU driver.

2. Define a separate extension package for each device, which contains:

    - The firmware image file(s) for the device.

    - An extension INF that describes the hardware ID for the specific device. The INF also specifies the path of the firmware files.

###### Componentized packages approach example

- Base Package
  - ComponentFirmwareUpdate.inf
  - ComponentFirmwareUpdate.dll

- Extension Package for a dock device
  - DockFirmwareUpdate.inf
  - Dock_Audio.offer.bin
  - Dock_Audio.payload.bin
  - Dock_MCU.offer.bin
  - Dock_MCU.payload.bin

- Extension Package for components of a Laptop
  - LaptopMCUFirmwareUpdate.inf
  - laptop_FPGA.offer.bin
  - laptop_FPGA.payload.bin
  - laptop_MCU.offer.bin
  - laptop_MCU.payload.bin
  - laptop_TCPM.offer.bin
  - laptop_TCPM.payload.bin

Reference sample: [ComponentizedPackageExample](https://github.com/Microsoft/CFU/tree/master/Host/ComponentizedPackageExample)

#### Monolithic package approach

In this approach, there is one driver package per CFU capable device. The package includes: INF, the CFU driver binary, and firmware files for the device.

##### When to use the monolithic package approach

- If your company ships only a handful of devices. Typically, a 1:1 mapping exists between the driver package and the device to which the driver is offering the updated firmware.
- To support updates for your devices on version of Windows earlier than Windows 10, version 1709.

###### Monolithic package approach challenges

- If you update multiple devices by using a single package, you will lose the ability to service each device independently. This approach can unnecessarily bloat the package.
- If you update each device by using its own single package, you must ensure that the package refers to different driver binary to avoid name conflicts, as shown in the example.

###### Monolithic package approach example

- Monolithic Package for a dock device
  - DockFirmwareUpdate.inf
  - DockFirmwareUpdate.dll
  - Dock_Audio.offer.bin
  - Dock_Audio.payload.bin
  - Dock_MCU.offer.bin
  - Dock_MCU.payload.bin

- Monolithic Package for components of a Laptop
  - LaptopMCUFirmwareUpdate.inf
  - LaptopMCUFirmwareUpdate.dll
  - laptop_FPGA.offer.bin
  - laptop_FPGA.payload.bin
  - laptop_MCU.offer.bin
  - laptop_MCU.payload.bin
  - laptop_TCPM.offer.bin
  - laptop_TCPM.payload.bin

Reference sample: [MonolithicPackageExample](https://github.com/Microsoft/CFU/tree/master/Host/MonolithicPackageExample)

### 2 Configure the CFU driver INF

The sample CFU driver is extensible. To tune the driver's behavior, change the driver INF instead of the source code.

1. Update the INF with the hardware ID of the HID TLC intended for firmware update.
Windows ensures that the driver is loaded when the component is enumerated on the host.

2. Update the INF with hardware IDs of your devices.

    **Componentized packages approach**

    1. Start with the ComponentFirmwareUpdate.inx as the base package INF. Replace the hardware ID in in this section with hardwareID(s) of all your supported devices.
  
        ```inf
        ; Target the Hardware ID for your devices.
        ;
        [Standard.NT$ARCH$]
        %ComponentFirmwareUpdate.DeviceDesc%=ComponentFirmwareUpdate, HID\HID\VID_abc&UP:def_U:ghi ; Your HardwareID- Laptop MCU

        %ComponentFirmwareUpdate.DeviceDesc%=ComponentFirmwareUpdate, HID\HID\VID_jkl&UP:mno_U:pqr ; Your HardwareID- Dock MCU
        ```

    2. Start with the DockFirmwareUpdate.inx as the extension package INF. Provide the hardware ID for your primary component in the device in this section.

        ```inf
        [Standard.NT$ARCH$]
        %DockFirmwareUpdate.ExtensionDesc%=DockFirmwareUpdate, HID\....; Your HardwareID for Dock MCU
        ```

    3. Add a new extension package for each component.

    **Monolithic package approach**

    1. Start with LaptopFirmwareUpdate.inx here. Replace the hardware ID with hardwareID of your primary component in the device.

        ```inf
        [Standard.NT$ARCH$]
        %LaptopFirmwareUpdate.DeviceDesc%=LaptopFirmwareUpdate, HID\.... ; Your HardwareID for Laptop MCU
        ```

    2. For each component, create the package and replace the hardware ID of the component. Rename the CFU driver to prevent a name conflict amongst packages.

3. Update the INF to specify the location of firmware file for each component on the device.

    The firmware files are not part of the driver binary. The driver needs to know the firmware file location at runtime so that it can transmit to the component. For a multi-component device, there may be more than one firmware file.

    The firmware has two files: an offer file and payload file. For each firmware file needed by the device, describe the offer and payload file as follows. You must only update _these_ entries.

    ```inf
    [FirmwareUpdate_Component1_HWAddReg]

    HKR,CFU\\_Dock_MCU_,Offer, 0x00000000,%13%\\_Dock_MCU.offer.bin_

    HKR,CFU\\_Dock_MCU_,Payload, 0x00000000, %13%\\_Dock_MCU.payload.bin_

    HKR,CFU\\_Dock_Audio_,Offer, 0x00000000, %13%\\_Dock_Audio.offer.bin_

    HKR,CFU\\_Dock_Audio_Sub_,Payload, 0x00000000, %13%\\_Dock_Audio.payload.bin_
    ```

    - For the multiple package approach, update the extension INF for each component with information about your firmware files.

    - For a monolithic package approach, update the INF file for the device.

4. Update the **SourceDisksFiles** and **CopyFiles** sections to reflect all the firmware files. To see an example, see [DockFirmwareUpdate.inx](https://github.com/Microsoft/CFU/blob/master/Host/ComponentizedPackageExample/DockFWUpdate/DockFirmwareUpdate.inx)

    > [!NOTE]
    > When the package(s) gets installed, the OS replaces the `%13%` with the full path to the files before creating the registry values. Thus, the driver able to enumerate the registry and identify all the firmware image and offer files.

5. Specify device capabilities in the INF.

    The sample driver provides a way to customize the driver behavior to optimize for certain scenarios. Those settings are controlled through registry settings, described [Configure device capabilities in the registry](#configure-device-capabilities-in-the-registry).

    For example, the sample driver requires information about the underlying bus protocol to which the device is connected. The protocol can be specified through registry settings.

    For the multiple package approach, device capabilities is specified in the device specific firmware file, and for a monolith package approach it is specified in the main INF file for the package.

### 3 Configure the diagnostic capabilities

1. The CFU driver sample uses [WPP Software Tracing](https://docs.microsoft.com/windows-hardware/drivers/devtest/wpp-software-tracing) for diagnostics. Update the trace with you own GUID to ensure that you can capture the WPP traces for your customized driver.

    Reference sample: [Trace.h](https://github.com/Microsoft/CFU/blob/master/Host/ComponentFirmwareUpdateDriver/Trace.h)

2. Update the EVENTLOG Provider in Device.h

    `EVENTLOG_PROVIDER_NAME L"SampleProvider"`

    Reference sample: [Device.h](https://github.com/Microsoft/CFU/blob/master/Host/ComponentFirmwareUpdateDriver/Device.h)

    ```cpp
    #define REPORT_ID_FW_VERSION_FEATURE      0x20
    #define REPORT_ID_PAYLOAD_CONTENT_OUTPUT  0x20
    #define REPORT_ID_PAYLOAD_RESPONSE_INPUT  0x22
    #define REPORT_ID_OFFER_CONTENT_OUTPUT    0x25
    #define REPORT_ID_OFFER_RESPONSE_INPUT    0x25
    ```

   If you need a different set of report IDs, modify [Dmf_ComponentFirmwareUpdateHidTransport.c](https://github.com/Microsoft/DMF/blob/master/Dmf/Modules.Library/Dmf_ComponentFirmwareUpdateHidTransport.c).

### 4 Deploy the package through Windows Update

Next, deploy the package through Windows Update. For information about deployment, see:

[Windows 10 Driver Publishing Workflow](https://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx)

[Using an Extension INF File](https://docs.microsoft.com/windows-hardware/drivers/install/using-an-extension-inf-file)

## Firmware file format

A firmware image has two parts: an offer file and a payload file. The offer contains necessary information about the payload to allow the primary component in the device that is receiving the update to decide if the payload is acceptable. The payload is a range of addresses and bytes that the primary component can consume.

### Offer format

The offer file is a 16-byte binary data whose structure must match the format specified in section 5.5.1 of the CFU protocol specification.

### Payload format

The payload file is a binary file which a collection of records that are stored contiguously. Each record is of the following format.

| Offset | Size | Value | Description |
|--|--|--|--|
| Byte 0 | DWORD | Firmware Address | Little Endian (LSB First) Address to write the data. The address is 0-based. Firmware could use this as an offset to determine the address as needed when placing the image in memory. |
| Byte 4 | Byte | Length | Length of payload data. |
| Byte 5-N | Bytes | Data | Byte array of payload data. |

### Configure device capabilities in the registry

You may configure each of these registries per component as needed.

| Registry Value | Description |
|--|--|
| **SupportResumeOnConnect** | Does this component support resume from a previously interrupted update?<p>You can enable this feature if the component can continue to receive payload data starting at a point where it was interrupted earlier. </p><p>When this value is set, during the payload transfer stage, the driver checks to see whether a previous transfer of this payload was interrupted. If it was interrupted, it the driver only sends the payload data from the interrupted point instead of the entire payload. </p><p>Set to 1 to enable and 0 (default) to disable.</p> |
| **SupportProtocolSkipOptimization** | <p>Does this component support skipping the entire protocol transaction for an already known all up to date firmware? </p><p>This is a driver side optimization option. If enabled, the driver checks these conditions during each initialization:<p><ul><li>Were all offers rejected in a previous cycle. </li><li>Does the current offers match the set of offers that the driver offered earlier.</li><ul></p><p>When the preceding conditions are satisfied, the driver skips the whole protocol transaction. <p>Set to 1 to enable and 0 (default) to disable.</p> |
| **Protocol** | Specify these values based on the underlying HID transport for your component.<p>If your component is connected by HID-Over-USB, specify 1. (Default)</p><p>If your component is connected by HID-Over-Bluetooth, specify value 2.</p> |

### Firmware update status provided by the driver

During the protocol transaction, the CFU driver writes registry entries to indicate the status.  This table describes the name, format of values and meaning of values that the driver touches during various stages of the protocol.

- \_ID_ in the table represents the Component ID, that is retrieved from the offer file. As specified in the specification, Component ID uniquely identify each component.

- For information about the DWORD, refer to the specification.

| Stage | Location | Reg Value Name | Value (DWORD) |
|--|--|--|--|
| Start; Pre Offer. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*CurrentFwVersion" | Version from device |
|  | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_NOT_STARTED |
| Offer; About to send offer. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*OfferFwVersion" | Version that is sent (or about to be send) to the device. |
| Offer Response (Rejected) | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatusRejectReason" | Reason for rejection returned by device. |
| Offer Response (Device Busy) | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_BUSY_PROCESSING_UPDATE |
| Offer Response (Accepted); About to send Payload. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_DOWNLOADING_UPDATE |  |
| Payload Accepted. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_PENDING_RESET |
| Error at any stage. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_ERROR |

## Troubleshooting tips

1. Check WPP logs to see the driver side interaction per component.

2. Check the event logs for any critical errors.

3. Check the book keeping registry entries described in Firmware update status provided by the driver.

## FAQ

**I have a component A that needs an update, how can I make the CFU driver aware of component A?**

You need to [configure the CFU driver INF](#2-configure-the-cfu-driver-inf) by using the hardware ID of the TLC created by component A.

**My company ships several independent components that I want to update by using the CFU model. Do I need separate drivers and package them individually?**

We recommend that you use the multiple packaging approach described  in [componentized packages](#componentized-packages-approach-recommended) .

**I have two components: component A, and a sub-component B. How should I make the CFU driver aware of component B?**

You don't need to. The driver doesn't need to know about the component hierarchy. It interacts with the primary component.

**How can I make the driver aware about my firmware files (offer, payload) file that I need to send to my component A?**

The firmware file information is set in the INF as registry values. [configure the CFU driver INF](#2-configure-the-cfu-driver-inf) .

**I have many firmware files, multiple offer, payload, for main component A and its subcomponents. How should I make the driver aware of which firmware file is meant for which component?**

The firmware file information is set in the INF as registry values. See Step 3 in [configure the CFU driver INF](#2-configure-the-cfu-driver-inf).

**I have an inbuilt components A and peripheral component B that needs an update. How Should I make this driver aware of this?**

You do not need to make the driver aware of the component in this case. The driver automatically handles this for you.

**Component A uses HID-Over-USB, component B is uses HID-Over-Bluetooth. How should I pass this information to the driver?**

Specify the correct capability by using the registry **Protocol** value. See [Configure device capabilities in the registry](#configure-device-capabilities-in-the-registry) for details.

**I am reusing the same driver for my components, are there any other customizations possible per usage scenarios?**

There are certain optimization settings that the driver allows. Those are configured in the registry. See [Configure device capabilities in the registry](#configure-device-capabilities-in-the-registry) for details.

**I am using the driver for firmware updates.  How do I know an update has succeeded?**

The firmware update status is updated by the driver in the registry as part of book-keeping.

## Additional resources

Learn about developing Windows drivers by using Windows Driver Foundation (WDF).

- [Developing Drivers with Windows Driver Foundation](https://go.microsoft.com/fwlink/p/?LinkId=691676), written by Penny Orwick and Guy Smith

- [Using WDF to Develop a Driver](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-the-framework-to-develop-a-driver)
