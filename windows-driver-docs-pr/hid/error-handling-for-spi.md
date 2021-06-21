---
title: Error handling for HID over SPI
description: How to handle errors that may occur in HID over SPI.
ms.date: 06/21/2021
ms.localizationpriority: medium
---

# Error handling for HID over SPI

This article covers error detection and handling procedures for HID over SPI. Errors on the SPI bus are broken into the following categories:

- Protocol Errors
- Timeout Errors

## Protocol errors

Protocol errors are further characterized into the following classifications:

- Short Packet Errors
- Bit Level Errors

### Short packet errors

Short packet errors occur when the host or the device does not return the number of bits as identified in the HID SPI protocol request and length field. The host is expected to clock in the specified number of bits. The host has no way to know if the device has stopped sending data since the host will read whatever happens to be on the bus. The host is expected to check sync fields and other fields to see if the data is reasonable. The host behavior for unexpected data or invalid data is to initiate a device reset.

### Bit-level errors

Bit-level errors may occur on the SPI bus. These errors are generally a result of noise on the bus or interference from other buses in the system. This specification does not support CRC or other detection mechanism for bit-level errors on the SPI data line.

It is possible for the host parser to identify a malformed report and discard it. It is the responsibility of the host HID driver stack to guard against a malformed report that doesn't conform to the report descriptor. The host behavior for unexpected data is to initiate a device reset.

## Timeout errors

The HID over SPI protocol is sequential with the expectation that the device must respond to host requests in a timely fashion. In most cases, the responses from device to host complete in a matter of milliseconds. In the event that the device is stuck and is unable to revert itself, there is a forced timeout delay after which the host may reset the device and restart operations.

`TIMEOUT_HostInitiatedReset = 1 second`

Hosts may allow for proprietary methods to adjust the value of this timeout for their specific devices but it is mandatory for the host to support a timeout value.

### Host initiated reset

The host may reset the device to re-establish communication with the device when an error is detected. This mechanism is intended for error recovery and should be in response to an exceptional event, such as re-establishing communication with a device that was exposed to an ESD discharge.
