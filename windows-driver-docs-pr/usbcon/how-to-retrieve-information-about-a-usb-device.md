---
title: USB hardware verifier (USB3HWVerifierAnalyzer.exe)
description: This article describes the USB hardware verifier tool (USB3HWVerifierAnalyzer.exe) that is used for testing and debugging specific hardware events.
ms.date: 02/02/2023
---

# USB hardware verifier (USB3HWVerifierAnalyzer.exe)

This article describes the USB hardware verifier tool (USB3HWVerifierAnalyzer.exe) that is used for testing and debugging specific hardware events.

Most hardware issues manifest in ways that lead to poor end-user experience and it's often difficult to determine the exact failure. The USB hardware verifier aims at capturing hardware failures that occur in a device, port, hub, controller, or a combination of them.

The USB hardware verifier can perform these tasks:

- Capture hardware events and display information in real time.
- Generate a trace file with information about all events.
- Parse an existing trace file for event information.

This article contains the following sections:

- [Getting the USB hardware verifier analyzer tool](#getting-the-usb-hardware-verifier-analyzer-tool)
- [How to capture events by using a USB hardware verifier](#how-to-capture-events-by-using-a-usb-hardware-verifier)
- [USB hardware verifier flags](#usb-hardware-verifier-flags)

## Getting the USB hardware verifier analyzer tool

The USB hardware verifier tool is included with the MUTT software package that is available for download at [Tools in the MUTT software package](mutt-software-package.md).

The tools package contains several tools that perform stress and transfer tests (including power transitions) and SuperSpeed tests. The package also has a Readme document (available as a separate download). The document gives you a brief overview of the types of MUTT hardware. It provides step-by-step guidance about various tests you should run, and suggests topologies for controller, hub, device, and BIOS/UEFI testing.

## How to capture events by using a USB hardware verifier

To capture events by using the hardware verifier, perform these steps:

1. Start a session by running this command at an elevated command prompt.

   ```console
   USB3HWVerifierAnalyzer.exe
   ```

   The tool supports these options:

   | Option | Description |
   |---|---|
   | -v &lt;VendorID&gt; | Logs all hardware verifier events for the specified VendorID. |
   | -p &lt;ProductID&gt; | Logs all hardware verifier events for the specified ProductID. |
   | -f &lt;ETL file&gt; | Parses the specified ETL file. Real-time parsing isn't supported. With this option, the tool parses the file offline. |
   | /v output | Displays all events to the console. |

1. Run the test scenario for which you want to capture hardware events.

   During a session, USB hardware verifier captures information about hardware events as they occur. If you want to filter events for a particular hardware, specify the VendorId and ProductId of the hardware. The tool might not capture some information (such as VID/PID) about events that occur before the device gets fully enumerated. The missing information is available in the detailed report that is generated at the end of the session (discussed next).

   > [!NOTE]
   > The AllEvents ETL file will always contain all ETW events for all devices. It is not affected by the **-v** and **-p** switches.

   Here's the command line to filter by VerndorId and ProductId:

   ```console
   USB3HWVerifierAnalyzer.exe -v 0781 -p 5595
   ```

   Here's an example output from the hardware verifier tool:

   ```console
   Session Name : TraceSessionFriJan271351112023

   Attempting to start session TraceSessionFriJan271351112023...
   Trace Session created...Status : 0

   Provider Enable Success, Status : 0

   Provider Enable Success, Status : 0

   Provider Enable Success, Status : 0

   Provider Enable Success, Status : 0

   Provider Enable Success, Status : 0

   Provider Enable Success, Status : 0
   13319329877.425596: (UsbHub3/179)
           Event Message: Client Initiated Recovery Action
           VendorID/ProductID: 0x5e3/0x612
           DeviceInterfacePath: \??\USB#VID_05E3&PID_0612#6&130491ac&0&4#{f18a0e88-c30c-11d0-8815-00a0c906bed8}
           DeviceDescription: Generic SuperSpeed USB Hub
           PortPath:  0x12, 0x4, 0x0, 0x0, 0x0, 0x0

   Provider disable Success, Status : 0

   Provider disable Success, Status : 0

   Provider disable Success, Status : 0

   Provider disable Success, Status : 0

   Provider disable Success, Status : 0

   Provider disable Success, Status : 0

   Session Stopped...Status : 0
   ```

1. Stop the session by pressing CTRL+C.

   At the end of the session, a file named AllEvents.etl is added in the current directory. This file contains trace information about all events that were captured during the session.

   In addition to AllEvents.etl, the command window shows a report. The report includes certain information that was missed in the real-time output. The following output shows an example test report for the preceding session. The report shows all events that the USB hardware verifier encountered.

   ```console
   Record #1 (Key = 0x57ff0de4858)
     VendorID/ProductID: 0x451/0x2077
     DeviceInterfacePath: \??\USB#VID_0451&PID_2077#6&c4be011&0&2#{f18a0e88-c30c-11d0-8815-00a0c906bed8}
     DeviceDescription: Generic USB Hub
     PortPath:  0x2, 0x0, 0x0, 0x0, 0x0, 0x0
     All errors encountered:
   #1: (UsbHub3/176): DescriptorValidationError20HubPortPwrCtrlMaskZero
   #2: (UsbHub3/179): Client Initiated Recovery Action
   #3: (UsbHub3/179): Client Initiated Recovery Action
   #4: (UsbHub3/179): Client Initiated Recovery Action
   #5: (UsbHub3/179): Client Initiated Recovery Action
   #6: (UsbHub3/179): Client Initiated Recovery Action
   #7: (UsbHub3/179): Client Initiated Recovery Action
   #8: (UsbHub3/179): Client Initiated Recovery Action
   #9: (UsbHub3/179): Client Initiated Recovery Action
   #10: (UsbHub3/179): Client Initiated Recovery Action
   #11: (UsbHub3/179): Client Initiated Recovery Action
   #12: (UsbHub3/179): Client Initiated Recovery Action
   #13: (UsbHub3/179): Client Initiated Recovery Action
   #14: (UsbHub3/179): Client Initiated Recovery Action

   Record #2 (Key = 0x57ff62a36a8)
     VendorID/ProductID: 0x1058/0x740
     DeviceInterfacePath: \??\USB#VID_1058&PID_0740#57583931453631414E5A3331#{a5dcbf10-6530-11d2-901f-00c04fb951ed}
     DeviceDescription: USB Mass Storage Device
     PortPath:  0x2, 0x4, 0x0, 0x0, 0x0, 0x0
     All errors encountered:
   #1: (UsbHub3/173): SuperSpeed Device is Connected on the 2.0 Bus

   Record #3 (Key = 0x57ff79fd4e8)
     VendorID/ProductID: 0x1edb/0xbd3b
     PortPath:  0x3, 0x0, 0x0, 0x0, 0x0, 0x0
     All errors encountered:
   #1: (UsbHub3/176): DescriptorValidationErrorCompanionIsochEndpointWBytesPerIntervalTooLarge
   #2: (UsbHub3/176): DescriptorValidationErrorCompanionIsochEndpointWBytesPerIntervalTooLarge
   #3: (UsbHub3/176): DescriptorValidationErrorCompanionIsochEndpointWBytesPerIntervalTooLarge
   #4: (UsbHub3/176): DescriptorValidationErrorCompanionIsochEndpointWBytesPerIntervalTooLarge
   #5: (UsbHub3/176): DescriptorValidationErrorCompanionIsochEndpointWBytesPerIntervalTooLarge
   #6: (UsbHub3/176): DescriptorValidationErrorCompanionIsochEndpointWBytesPerIntervalTooLarge
   #7: (UsbHub3/176): DescriptorValidationErrorStringMismatchBetweenBlengthAndBufferLength
   #8: (UsbHub3/176): DescriptorValidationErrorStringMismatchBetweenBlengthAndBufferLength

   ```

   In the preceding example report, note the **Key** field value for each record. The report categorizes the information by those **Key** values, making it easier to read. The same **Key** values are used in events captured in AllEvents.etl.

1. Convert AllEvents.etl to text format by running the following command:

   ```console
   USB3HWVerifierAnalyzer.exe -f AllEvents.etl /v > Output.txt 
   ```

   In the output file, search for the previously noted **Key** values. The values are associated with one of these fields: **fid_UcxController**, **fid_HubDevice**, and **fid_UsbDevice**.

1. Open AllEvents.etl in Netmon and select **Add &lt;field_name&gt; to display filter** to filter events by controller, hub, and device. For more information, see [How to install Netmon and USB ETW parsers](how-to-retrieve-information-about-a-usb-device.md).

## USB hardware verifier flags

| Flag | Indicates that... |
|---|---|
| DeviceHwVerifierClientInitiatedResetPipe | The client driver initiated a recovery action by resetting a particular pipe in response to I/O failures. Certain client drivers might perform error recovery in other scenarios. |
| DeviceHwVerifierClientInitiatedResetPort | The client driver initiated a recovery action by resetting the device in response to I/O failures. Certain client drivers might perform error recovery in other scenarios. |
| DeviceHwVerifierClientInitiatedCyclePort | The client driver initiated a recovery action by cycling the port. This flag causes the Plug and Play Manager to re-enumerate the device. |
| DeviceHwVerifierSetIsochDelayFailure | A USB 3.0 device failed the SET_ISOCH_DELAY request. The device can fail the request because either the driver doesn't require the request information or a transient error occurred. However, the driver can't differentiate between those reasons. This error isn't captured in the report. |
| DeviceHwVerifierSetSelFailure | A USB 3.0 device failed the SET_SEL request. The device uses the request information for Link Power Management (LPM). The device can fail the request because either the driver doesn't require the request information or a transient error occurred. However, the driver can't differentiate between those reasons. This error isn't captured in the report. |
| DeviceHwVerifierSerialNumberMismatchOnRenumeration | The device reported a different serial number during re-enumeration as opposed to the one it reported during initial enumeration. A re-enumeration can occur as a result of a reset port or system resume operation. |
| DeviceHwVerifierSuperSpeedDeviceWorkingAtLowerSpeed | The USB 3.0 device is operating a bus speed lower than SuperSpeed. |
| DeviceHwVerifierControlTransferFailure | A control transfer failed to the device's default endpoint failed. The transfer can fail as a result of device or controller error. The hub logs indicate the USBD status code for the transfer failure. This flag excludes SET_SEL and SET_ISOCH_DELAY control transfers failures. Those types of requests are covered by DeviceHwVerifierSetIsochDelayFailure and DeviceHwVerifierSetSelFailure flags. |
| DeviceHwVerifierDescriptorValidationFailure | A descriptor returned by the device doesn't conform to the USB specification. The hub log indicates the exact error. |
| DeviceHwVerifierInterfaceWakeCapabilityMismatch | The RemoteWake bit is incorrectly set in the device. USB 3.0 devices that support remote wake must also support function wake. There are two ways in which the device indicates its support for function wake. The first way is through the **bmAttributes** field of the configuration descriptor and the second way is in its response to the GET_STATUS request targeted to the interface. For a non-composite device, the RemoteWake bit value must match the value returned by the GET_STATUS request that is targeted to interface 0. For composite devices, the RemoteWake bit must be 1 for at least one of the functions. Otherwise, this flag indicates that the device reported contradictory values in here. |
| DeviceHwVerifierBusRenumeration | The device is re-enumerated on the bus. A re-enumeration can occur as a result of a reset port or system resume operation. Re-enumeration also occurs, when the device is disabled/enabled or stopped/started. |
| HubHwVerifierTooManyResets | A hub has gone through too many reset operations within a short period. Even though those resets were successful, the hub isn't processing requests and repeated errors occur. |
| HubHwVerifierControlTransferFailure | A control transfer targeted to the hub's default endpoint failed. The transfer can fail as a result of device or controller error. The hub logs indicate the USBD status code for the failure. |
| HubHwVerifierInterruptTransferFailure | A data transfer targeted to the hub's interrupt endpoint failed. The transfer can fail as a result of device or controller error. The hub logs indicate the USBD status code for the failure. If the transfer failed because of the request was canceled, the failure isn't captured. |
| HubHwVerifierNoSelectiveSuspendSupport | The RemoteWake bit isn't set to 1 in the hub's configuration descriptor. |
| HubHwVerifierPortResetTimeout | While enumerating or re-enumerating a device, the port-reset operation is timing out. A port change notification isn't received indicating that the port-reset is complete. |
| HubHwVerifierInvalidPortStatus | The port status of the target port isn't valid as per the USB specification. Certain devices can cause the hub to report the invalid status. |
| HubHwVerifierPortLinkStateSSInactive | The link between the target port and the downstream device is in an error state. |
| HubHwVerifierPortLinkStateCompliance | The link between the target port and the downstream device is in compliance mode. In some scenarios involving system sleep-resume, the compliance mode error is expected and in those cases the failure isn't captured. |
| HubHwVerifierPortDeviceDisconnected | The downstream device on the target port is no longer connected to the bus. |
| HubHwVerifierPortOverCurrent | The downstream port reported overcurrent state. |
| HubHwVerifierControllerOperationFailure | A controller operation (such as enabling device, configuring endpoints) failed for the device that is attached to the target port. Failures from SET_ADDRESS and Reset endpoint requests aren't captured. |

## Related topics

- [Overview of Microsoft USB Test Tool (MUTT) devices](./microsoft-usb-test-tool--mutt--devices.md)
