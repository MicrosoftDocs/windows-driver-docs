---
title: Troubleshooting HID over I2C Device Issues
description: This guide presents a structured workflow specifically for troubleshooting HID I2C device issue.
ms.topic: troubleshooting-general
ms.date: 12/22/2025
ai-usage: ai-assisted
---

# Troubleshooting HID over I2C device issues

HID over I2C (also known as HID I2C) devices—such as touchpads, touchscreens, sensors, and keyboards—are widely used in modern laptops and tablets for their low power consumption and flexible integration. Diagnosing and resolving their issues can be challenging due to the complexity of interactions between HID I2C device firmware, I2C controllers, and the operating system. This guide presents a structured workflow specifically for troubleshooting HID I2C device issues. By following these steps, you can efficiently isolate issues, capture meaningful traces, and communicate actionable findings to device manufacturers or controller vendors.

## Architecture and overview

This diagram shows the typical architecture of a HID I2C device and a corresponding I2C controller.

:::image type="content" source="images/hid-i2c-architecture.png" alt-text="Screenshot of the HID I2C architecture diagram showing the device firmware, I2C controller, and operating system components.":::

This diagram shows an overview of this troubleshooting guide.

:::image type="content" source="images/troubleshoot-hid-i2c-overview.png" alt-text="Screenshot of the troubleshooting workflow overview diagram for HID over I2C devices.":::

## Common failures of HID I2C devices

| Device status | What happened | What to do next |
|--|--|--|
| "A request for the HID descriptor failed." | The HID I2C device firmware failed processing the read request for the HID descriptor from the host. | Contact the HID I2C device firmware owner to investigate the issue.<br/><br/>If the HID I2C device firmware didn't receive the read request, contact the I2C controller owner to investigate why the I2C controller didn't send the read request.<br/><br/>If you need more information on the request failure, follow the instructions in a later section to capture and analyze HIDI2C driver trace. |
| "The device returned an invalid HID descriptor." | The HID I2C device firmware returned an invalid HID descriptor to the host. The descriptor contains one or more invalid fields, such as an incorrect descriptor length or an invalid register address. | Contact the HID I2C device firmware owner to address the issue.<br/><br/>If you need more information on the validation failure, follow the instructions in a later section to capture and analyze HIDI2C driver trace. |
| "The device failed the SET_POWER command." | Writing the HID I2C command SET_POWER to the device firmware failed. | Contact the HID I2C device firmware owner to investigate the issue.<br/><br/>If the device didn't receive the write, contact the I2C controller firmware owner to investigate why the I2C controller didn't write to the HID I2C device.<br/><br/>If you need more information on the command failure, follow the instructions in a later section to capture and analyze HIDI2C driver trace. |
| "This device can't start. (Code 10)" with a message that indicates a descriptor parsing failure.<br/><br/>Here are some common parsing failure messages:<ul><li>"Report wasn't byte aligned."</li><li>"A nonconstant main item was declared without a corresponding usage."</li><li>"An unknown item was found in the report descriptor."</li><li>"Extra end collection found or end collection not found."</li></ul> | The HID I2C device firmware returned an invalid HID Report descriptor. | Contact the HID I2C device firmware owner to address the issue.<br/><br/>The OS retrieves the HID Report Descriptor based on information from the HID Descriptor. The HID Descriptor is retrieved from the device firmware earlier. Make sure that in the HID Descriptor, the wReportDescLength field at byte offset 4 is accurate. Also verify that the wReportDescRegister field at byte offset 6 is accurate.<br/><br/>You can use an I2C bus analyzer hardware to verify the actual descriptors transferred on the I2C bus. If you need more information on the descriptor validation failure, follow the instructions in a later section to capture and analyze HIDI2C driver trace. |
| The HID I2C device is missing in Device Manager. | The Advanced Configuration and Power Interface (ACPI) firmware reported incorrect device configuration, such as incorrect Compatible ID (_CID) or incorrect device presence status (_STA). | Contact your ACPI firmware owner to inspect the device configuration. |

## HID I2C devices are started in Device Manager but not working

Follow this guide to investigate.

:::image type="content" source="images/troubleshoot-hid-i2c-device-started.png" alt-text="Screenshot of the troubleshooting flowchart for started HID I2C devices that aren't working.":::

## Capture and analyze trace for HID I2C device issues

### Capture trace

Follow the instructions at [https://aka.ms/busestrace](https://aka.ms/busestrace) to get the __BusesTrace.cmd__ script and capture trace of Microsoft-provided drivers such as HIDI2C.SYS and HIDCLASS.SYS.

If there are multiple HID I2C devices, you might want to disable or avoid using them during the trace capture to reduce trace noise and make analysis easier.

### What type of trace to capture

__BusesTrace.cmd__ can either capture an immediate repro trace, or configure the system for boot trace (but require a system reboot first after the script run). In most cases, especially for any device failures that happen during boot-up, a boot trace is required to capture the failure point.

### View HIDI2C.sys manifested ETW trace in Windows Performance Analyzer (WPA)

To view HIDI2C.sys manifested ETW trace in [Windows Performance Analyzer](/windows-hardware/test/wpt/windows-performance-analyzer), open both __Buses-MachineInfo.etl__ and __WPR-…-InputTrace.etl__ files in WPA and choose to open them in one session.

:::image type="content" source="images/troubleshoot-hid-i2c-open-etl-files-in-wpa.png" alt-text="Screenshot showing Windows Performance Analyzer dialog to open ETL trace files in a single session.":::

You can view manifested ETW events using the "System Activities\Generic Events" graph. The name of that HIDI2C event provider is "Microsoft-Windows-SPB-HIDI2C". (This also works for other manifested ETW events, such as HIDCLASS manifested ETW events, which provider name is "Microsoft-Windows-Input-HIDCLASS".)

:::image type="content" source="images/troubleshoot-hid-i2c-view-etw-in-wpa.png" alt-text="Screenshot of Windows Performance Analyzer displaying manifested ETW trace events from the HIDI2C provider.":::

### Common HIDI2C manifested ETW events

Event Provider Name: Microsoft-Windows-SPB-HIDI2C

| Event ID | Event Name | Meaning |
|--|--|--|
| 1010 | Microsoft-Windows-SPB-HIDI2C/HIDI2C_IO/win:Start | HIDI2C.SYS receives an interrupt from the HID I2C device. |
| 1011 | Microsoft-Windows-SPB-HIDI2C/HIDI2C_IO/IoSpbReadDispatch | HIDI2C.SYS issues an I2C read request to the HID I2C device via the I2C controller. |
| 1012 | Microsoft-Windows-SPB-HIDI2C/HIDI2C_IO/IoSpbReadComplete | The I2C controller completes the I2C read request from HIDI2C.SYS successfully. |
| 1013 | Microsoft-Windows-SPB-HIDI2C/HIDI2C_IO/IoForwardToCompletionQueue | HIDI2C.SYS forwards a HID request to an internal I/O queue to complete with the HID I2C device data later. |
| 1014 | Microsoft-Windows-SPB-HIDI2C/HIDI2C_IO/win:Stop | HIDI2C.SYS completes a HID request with the HID I2C device data. |

### View HIDI2C.SYS WPP trace in WPA

Unlike manifested ETW trace, you must view WPP trace using the "System Activity\WPP Trace" graph and load symbols to format the WPP trace messages. For more information about configuring and loading symbols in WPA and the symbol path, see the following articles. (The same steps apply to any WPP trace, not just from HIDI2C.SYS.)

[Load Symbols or Configure Symbol Paths](/windows-hardware/test/wpt/load-symbols-or-configure-symbol-paths)

[Loading Symbols](/windows-hardware/test/wpt/loading-symbols)

:::image type="content" source="images/troubleshoot-hid-i2c-view-wpp-in-wpa.png" alt-text="Screenshot showing Windows Performance Analyzer with WPP trace events and symbols loaded.":::

> [!NOTE]
> The "__GUID Name__" field displays WPP trace providers, which are usually driver names such as "hidi2c". This column isn't visible by default and must be added using the "View Editor" dialog box.

## Examples

### Example 1: (Non-Repro) Interrupts are received and handled successfully

HIDI2C manifested ETW trace shows expected event sequences from ID 1010, 1011, 1012, 1013 and 1014.

:::image type="content" source="images/troubleshoot-hid-i2c-ex1-etw.png" alt-text="Screenshot showing manifested ETW trace with successful interrupt handling event IDs 1010 through 1014.":::

HIDI2C WPP trace, after grouped by provider names (the "Guid Name" column) and trace level, doesn't show any errors (only Information level trace.)

:::image type="content" source="images/troubleshoot-hid-i2c-ex1-wpp.png" alt-text="Screenshot showing WPP trace grouped by provider names with only Information level events and no errors.":::

### Example 2: Interrupts are received but I2C read requests aren't completed successfully

For each interrupt HIDI2C.SYS receives, the event sequence should be ID 1010, 1011, 1012, 1013, and 1014. If any events of ID 1011, 1012, or 1013 are missing like this example shows, something went wrong. You can then analyze the WPP trace of HIDI2C.SYS further to see if more detailed errors are logged.

HIDI2C manifested ETW trace shows events of ID 1010 and 1011 but not 1012 and others. These events mean that interrupts were received and I2C read requests were issued to the I2C controller. However, the requests weren't completed successfully.

:::image type="content" source="images/troubleshoot-hid-i2c-ex2-etw.png" alt-text="Screenshot showing manifested ETW trace with incomplete event sequence, events 1010 and 1011 present but missing subsequent events.":::

HIDI2C WPP trace, after grouping the HIDI2C WPP trace by the provider names (the "Guid Name" column) and trace level, shows that the I2C controller timed out the SPB requests. You must investigate further from the I2C controller.

:::image type="content" source="images/troubleshoot-hid-i2c-ex2-wpp.png" alt-text="Screenshot showing WPP trace with SPB request timeout errors from the I2C controller.":::

### Example 3: HID I2C device failed due to returning an invalid HID report descriptor

In this example, the HID I2C device failed with the following status in Device Manager.

:::image type="content" source="images/troubleshoot-hid-i2c-ex3-devmgmt.png" alt-text="Screenshot showing Device Manager with a failed HID I2C device and error status indicating an invalid HID Report Descriptor.":::

According to the Common Failures table, this error status indicates that the HID I2C device firmware returned an invalid HID Report Descriptor. Investigate this issue from the HID I2C device firmware first. You might want to verify that the expected HID Report Descriptor was returned. You can also use the I2C bus analyzer hardware to verify what was transferred on the I2C bus. If you need to get more information on this error, analyze the HIDCLASS.SYS trace instead of HIDI2C.SYS trace, since HIDCLASS.SYS validates the HID Report Descriptor.

After grouped by trace level, HIDCLASS WPP trace shows the same error but with the byte offset showing where the error occurred.

:::image type="content" source="images/troubleshoot-hid-i2c-ex3-wpp.png" alt-text="Screenshot showing HIDCLASS WPP trace with validation error and byte offset where the error occurred.":::
