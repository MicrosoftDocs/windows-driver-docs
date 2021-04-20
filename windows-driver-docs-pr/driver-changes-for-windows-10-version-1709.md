---
title: Driver development changes for Windows 10, version 1709
description: Learn about new features for driver development in Windows 10, such as new content sets for Windows debugger.
ms.date: 04/15/2020
author: EliotSeattle
ms.localizationpriority: medium
---

# Driver development additions for Windows 10, version 1709

This topic provides information about the features and updates to Windows driver development in Windows 10, version 1709.

## Feature areas updated in Windows 10, version 1709

The following features have documented updates in Windows 10, version 1709.

- [Audio](#audio)
- [ACPI](#acpi)
- [Biometric](#biometric)
- [Windows debugger](#windows-debugger)
- [Display](#display)
- [Driver verifier](#driver-verifier)
- [Hardware notifications](#hardware-notifications)
- [Windows Kernel](#windows-kernel)
- [Mobile broadband](#mobile-broadband)
- [Networking](#networking)
- [Virtualized PCI](#virtualized-pci)
- [Pulse Width Modulation](#pulse-width-modulation-controllers)
- [File Systems & Storage](#file-systems-and-storage)
- [USB](#usb)
- [Universal Windows drivers](#universal-windows-drivers)
- [WPP Software Tracing](#wpp-software-tracing)

### Windows debugger

The following is a list of new content sets for the Debugger in Windows 10, version 1709:

- [Debugging Using WinDbg Preview](./debugger/debugging-using-windbg-preview.md) - A preview into the next generation debugger.
- [Time Travel Debugging - Overview](./debugger/time-travel-debugging-overview.md) - Record and replay an execution of your process.

### Driver Verifier

Driver verifier includes new driver validation rules for the following technologies:

- New [Rules for Audio Drivers](./devtest/rules-for-audio-drivers.md)
- New [Rules for AVStream Drivers](./devtest/rules-for-avstream-drivers.md)
- Four new [Rules for KMDF Drivers](./devtest/sdv-rules-for-kmdf-drivers.md)
- Three new [Rules for NDIS Drivers](./devtest/sdv-rules-for-ndis-drivers.md)
- New [Nullcheck rules](./devtest/nullcheck.md) *Added in version 1703*

### Universal Windows drivers

The following is a list of new features to Universal Drivers in Windows 10, version 1709:

- [Updating Device Firmware using Windows Update](./install/updating-device-firmware-using-windows-update.md) - Describes how to update a removable or in-chassis device's firmware by using the Windows Update (WU) service.
- [Reg2inf](./devtest/reg2inf.md) - The Driver Package INF Registry Conversion Tool (reg2inf.exe) converts a registry key and its values or a COM .dll implementing a DLL RegisterServer routine, into a set of INF AddReg directives. These directives are included in the driver package INF file.

The following is a list of updates to Universal Drivers in Windows 10, version 1709:

- The [Universal Drivers Scenario](./develop/dch-example.md) has a new COM component example
- [INF AddComponent Directive](./install/inf-addcomponent-directive.md)
- [Using an Extension INF file](./install/using-an-extension-inf-file.md)
- [Using a Component INF file](./install/using-a-component-inf-file.md)

### WPP Software Tracing

[WPP Software Tracing](./devtest/wpp-software-tracing.md) introduces a new feature: *Inflight Trace Recorder*, in Windows 10, version 1709. If the driver enables WPP tracing and WPP Recorder, trace logging is turned on automatically and you can easily view messages without starting or stopping trace sessions. For more fine tuned control over the log, WPP Recorder allows a KMDF driver to create and manage custom buffers.

- [WPP Recorder for logging traces](./devtest/using-wpp-recorder.md)
- [WppRecorderLogGetDefault](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-imp_wpprecorderloggetdefault)
- [WppRecorderLogCreate](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderlogcreate) (KMDF only)
- [WppRecorderDumpLiveDriverData](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderdumplivedriverdata)

### Audio

The following is a list of updates to Windows Audio driver development in Windows 10, version 1709:

- New [Configure and query audio device modules](./audio/configure-and-query-audiodevicemodules.md)
- Extensive updates to [voice activation](./audio/voice-activation.md)
  - More details on chained and keyword only activation
  - A new glossary of terms
  - Additional information on training and recognition, such as pin and audio format information
  - An updated keyword system overview
  - Updated information on wake on voice

### ACPI

The following is a list of new Advanced Configuration and Power Interface (ACPI) DDIs to support input/output buffers in Windows 10, version 1709.

- [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_complex_v1)
- [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_complex_v1_ex)
- [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_complex_v2)
- [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_complex_v2_ex)
- [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_integer_v1)
- [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_integer_v2)
- [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_integer_v2_ex)
- [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_string_v1)
- [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_string_v1_ex)
- [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_string_v2)
- [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_string_v2_ex)
- [ACPI_EVAL_INPUT_BUFFER_V1](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v1)
- [ACPI_EVAL_INPUT_BUFFER_V1_EX](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v1_ex)
- [ACPI_EVAL_INPUT_BUFFER_V2](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v2)
- [ACPI_EVAL_INPUT_BUFFER_V2_EX](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v2_ex)
- [ACPI_EVAL_OUTPUT_BUFFER_V1](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_output_buffer_v1)
- [ACPI_EVAL_OUTPUT_BUFFER_V2](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_output_buffer_v2)
- [ACPI_METHOD_ARGUMENT_V1](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1)
- [ACPI_METHOD_ARGUMENT_V2](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v2)
- [GIC_ITS](/windows-hardware/drivers/ddi/acpitabl/ns-acpitabl-_gic_its)

### Biometric

There were new signing requirements for Windows Biometric Drivers introduced in Windows 10, version 1709. For more information, see [Signing WBDI Drivers](./biometric/signing-wbdi-drivers.md).

### Display

The following new features were introduced for Windows Display driver development in Windows 10, version 1709.

- Display ColorSpace Transform DDIs provide additional control over color space transforms applied in the post-composition display pipeline.
- The D3D12 Copy Queue Timestamp Queries feature will allow applications to issue timestamp queries on COPY command lists/queues. These timestamps are specified to function identically to timestamps on other engines.
- Enhanced Video integration into Direct3D12 Runtime through:
    1. Hardware accelerated video decoding
    2. Content protection
    3. Video processing

### Hardware notifications

Windows 10, version 1709 added support for hardware-agnostic notification components such for hardware such as LEDs and vibration mechanisms. For more information, see:

- [Hardware notifications support](./gpiobtn/hardware-notifications-support.md)
- [Hardware notifications reference](/windows-hardware/drivers/ddi/_gpiobtn/)

### Windows kernel

In Windows 10, version 1709, several new routines to the Windows Kernel for drivers have been added.

- ExGetFirmwareType and ExIsSoftBoot &ndash; Executive library support routines.
- [PsSetLoadImageNotifyRoutineEx](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetloadimagenotifyroutineex) &ndash; An extended image notify routine for all executable images, including images that have a different architecture from the native architecture of the operating system.
- [MmMapMdl](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapmdl) &ndash; A [memory manager](./kernel/windows-kernel-mode-memory-manager.md) routine for mapping physical pages described by a memory descriptor list (MDL) into the system virtual address space.
- [PoFxSetTargetDripsDevicePowerState](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxsettargetdripsdevicepowerstate) &ndash; A PoFx routine to notify the power manager of the device's target device power state for DRIPS.
- The following options were added for the [ZwSetInformationThread](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwsetinformationthread) routine, that are related to process policies:

  - [PROCESS_MITIGATION_CHILD_PROCESS_POLICY](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_process_mitigation_child_process_policy)
  - [PROCESS_MITIGATION_PAYLOAD_RESTRICTION_POLICY](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_process_mitigation_payload_restriction_policy)
  - PROCESS_READWRITEVM_LOGGING_INFORMATION

- [PsGetServerSiloActiveConsoleId](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetserversiloactiveconsoleid) and [PsGetParentSilo](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetparentsilo) &ndash; Silo APIs to get information about server silos that are created and destroyed on a machine.
- The following is a list of new RTL functions for using correlation vector to reference events and the generated logs for diagnostic purposes.
  - [CORRELATION_VECTOR](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-correlation_vector)
  - [RtlExtendCorrelationVector](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlextendcorrelationvector)
  - [RtlIncrementCorrelationVector](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlincrementcorrelationvector)
  - [RtlInitializeCorrelationVector](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlinitializecorrelationvector)
  - [RtlValidateCorrelationVector](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlvalidatecorrelationvector)

### Mobile broadband

The following features were added for Windows Mobile Broadband and Mobile Operator Scenarios for driver development in Windows 10, version 1709:

- [UICC reset](./network/mb-low-level-uicc-access.md) and [modem reset](./network/mb-modem-reset-operations.md)
- [Protocol Configuration Operations (PCO)](./network/mb-protocol-configuration-options-pco-operations.md)
- [Base stations information query](./network/mb-base-stations-information-query-support.md)
- [eSIM and MBIM ReadyState guidance](./network/mb-esim-mbim-ready-state-guidance.md)

In Windows 10, version 1709, the [desktop COSA documentation](./mobilebroadband/planning-your-desktop-cosa-apn-database-submission.md) was updated to include new branding-related fields.
See the list of [deprecated features](what-s-new-in-driver-development.md#deprecated-features) for other changes to Mobile Operator Scenarios.

### Networking

These new features and improvements for Windows Networking driver development were added in Windows 10, version 1709.

The following is a list of new and updated features for NDIS:

- Introduction to NetAdapterCx 1.1, which includes new NewAdapterCx features:
  - More packet context options
  - Finer link state control
  - Improved receive buffer management and performance
  - General performance improvements
- New [Synchronous OID request interface](./network/synchronous-oid-request-interface-in-ndis-6-80.md) in NDIS 6.80
- New [Receive Side Scaling Version 2 (RSSv2)](./network/receive-side-scaling-version-2-rssv2-in-ndis-6-80.md) in NDIS 6.80
- [Introduction to NDIS 6.80](./network/introduction-to-ndis-6-80.md)
- [Porting NDIS 6.x drivers to NDIS 6.80](./network/porting-ndis-6-x-drivers-to-ndis-6-80.md)

### Virtualized PCI

In Windows 10, version 1709, new programming interfaces for writing a Physical Function driver for devices that conform to the PCI Express Single-Root I/O Virtualization (SR-IOV) specification were added. The interfaces are declared in Pcivirt.h. For more information, see [PCI virtualization](/windows-hardware/drivers/ddi/pcivirt/).

### Pulse Width Modulation Controllers

In Windows 10, version 1709, to provide access to a Pulse width modulation (PWM) controller that is part of the SoC and memory-mapped to the SoC address space, you need to write a kernel-mode driver. For more information, see [PWM driver for an on-SoC PWM module](/windows-hardware/drivers/spb/pulse-width-controller driver?branch=spb).

To parse and validate pin paths and extract the pin number, kernel mode drivers should use [PwmParsePinPath](/windows-hardware/drivers/ddi/pwmutil/nf-pwmutil-pwmparsepinpath).

An app can send requests to the controller driver by sending [PWM IOCTLs](/windows-hardware/drivers/spb/pulse-width-controller driver#pwm-ioctl-requests) requests.

### File Systems and Storage

In File Systems and Storage, the ufs.h header was added in Windows 10, version 1709 to provide additional support to Universal Flash Storage.

Posix updates include new functions **delete** and **rename**.

The following is a list of headers that were updated in Windows 10, version 1709:

- ata.h
- fltKernel.h
- minitape.h
- ntddscsi.h
- ntddstor.h
- ntddvol.h
- ntifs.h
- scsi.h
- storport.h

### USB

These new features for USB were added in Windows 10, version 1709.

#### Media Agnostic USB (MA-USB) protocol

The USB driver stack can send USB packets over non-USB physical mediums such as Wi-Fi by using the Media Agnostic USB (MA-USB) protocol. To implement this feature, new programming interfaces have been released. The new DDIs allow the driver to determine the delays associated with the [_URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_get_isoch_pipe_transfer_path_delays). That information can be retrieved by building a new URB request.
For information about this new feature, see the following topics:

- [USB client drivers for Media-Agnostic (MA-USB)](./usbcon/usb-client-drivers-for-ma-usb.md)
- [_URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_get_isoch_pipe_transfer_path_delays)
- [USB Request Blocks (URBs)](./usbcon/communicating-with-a-usb-device.md)

To support MA-USB, the host controller driver must provide the transport characteristics by implementing specific callback functions. The following table shows the callback functions and structures that support MA-USB.

| Callback Functions | Structures |
| ----- | ----- |
| [EVT_UCX_USBDEVICE_GET_CHARACTERISTIC](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_get_characteristic) | [UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS](/windows-hardware/drivers/ddi/ucxendpoint/ns-ucxendpoint-_ucx_endpoint_isoch_transfer_path_delays) |
| [EVT_UCX_USBDEVICE_RESUME](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_resume) | [UCX_CONTROLLER_ENDPOINT_CHARACTERISTIC_PRIORITY](/windows-hardware/drivers/ddi/ucxendpoint/ne-ucxendpoint-_ucx_endpoint_characteristic_priority) |
| [EVT_UCX_USBDEVICE_SUSPEND](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_suspend) | [UCX_ENDPOINT_CHARACTERISTIC](/windows-hardware/drivers/ddi/ucxendpoint/ns-ucxendpoint-_ucx_endpoint_characteristic) |
| [EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_get_isoch_transfer_path_delays) | [UCX_ENDPOINT_CHARACTERISTIC_TYPE](/windows-hardware/drivers/ddi/ucxendpoint/ne-ucxendpoint-_ucx_endpoint_characteristic_type) |
| [EVT_UCX_ENDPOINT_SET_CHARACTERISTIC](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_set_characteristic) | [UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS](/windows-hardware/drivers/ddi/ucxendpoint/ns-ucxendpoint-_ucx_endpoint_isoch_transfer_path_delays) |

#### Synchronized system QPC with USB frame and microframes

New programming interfaces were added that retrieve the system query performance counter (QPC) value synchronized with the frame and microframe.

This information is retrieved only when the caller enables the feature in the host controller. To enable the feature, a host controller driver must implement the following callback functions.

- [EVT_UCX_CONTROLLER_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_get_frame_number_and_qpc_for_time_sync)
- [EVT_UCX_CONTROLLER_START_TRACKING_FOR_TIME_SYNC](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_start_tracking_for_time_sync)
- [EVT_UCX_CONTROLLER_STOP_TRACKING_FOR_TIME_SYNC](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_stop_tracking_for_time_sync)

An application can use these APIs to enable/disable the feature and retrieve the information:

- [WinUsb_GetCurrentFrameNumberAndQpc](/windows/win32/api/winusb/nf-winusb-winusb_getcurrentframenumberandqpc)
- [WinUsb_StartTrackingForTimeSync](/windows/win32/api/winusb/nf-winusb-winusb_starttrackingfortimesync)
- [WinUsb_StopTrackingForTimeSync](/windows/win32/api/winusb/nf-winusb-winusb_stoptrackingfortimesync)

Other drivers can send these IOCTL requests to enable/disable the feature and retrieve the information:

- [IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_get_frame_number_and_qpc_for_time_sync)
- [IOCTL_USB_START_TRACKING_FOR_TIME_SYNC](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_start_tracking_for_time_sync)
- [IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_stop_tracking_for_time_sync)

These supporting structures are for synchronized system OPC with USB frame and microframes:

- [USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION](/windows-hardware/drivers/ddi/usbioctl/ns-usbioctl-_usb_start_tracking_for_time_sync_information)
- [USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION](/windows-hardware/drivers/ddi/usbioctl/ns-usbioctl-_usb_stop_tracking_for_time_sync_information)
- [USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION](/windows-hardware/drivers/ddi/usbioctl/ns-usbioctl-_usb_frame_number_and_qpc_for_time_sync_information)

#### IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED

The [IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED](/windows-hardware/drivers/ddi/ucmtcpciportcontrollerrequests/ni-ucmtcpciportcontrollerrequests-ioctl_ucmtcpci_port_controller_displayport_display_out_status_changed) request is a new request in USB Type-C Port Controller Interface framework extension. This request notifies the client driver that the display out status of the DisplayPort connection has changed.

These structures support the IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED request:

- [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS](/windows-hardware/drivers/ddi/ucmtcpciportcontrollerrequests/ns-ucmtcpciportcontrollerrequests-_ucmtcpci_port_controller_displayport_display_out_status_changed_in_params)
- [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS](/windows-hardware/drivers/ddi/ucmtcpciportcontrollerrequests/ne-ucmtcpciportcontrollerrequests-_ucmtcpci_port_controller_displayport_display_out_status)
