---
title: Device Metadata Error Codes
description: Device Metadata Error Codes
ms.date: 06/19/2025
ms.topic: error-reference
---

# Device Metadata Error Codes

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](driver-package-container-metadata.md)**.

Starting with Windows 7, the operating system logs the following error codes within events that are related to the download and processing of device metadata packages. The Event Tracing for Windows (ETW) service manages these events, which can be viewed by using Event Viewer. For more information about these events, see [Debugging Device Metadata Packages By Using Event Viewer](debugging-device-metadata-packages-by-using-event-viewer.md).

## Windows Metadata and Internet Services (WMIS) Errors (200000xx)

| Error code | Explanation |
|--|--|
| 20000021 | The request doesn't contain a device metadata request. |
| 20000022 | The request batch size exceeds the maximum allowed value. |
| 20000023 | The locale value is invalid. |
| 20000024 | The request doesn't contain valid header information. |
| 20000025 | The request format is invalid. |
| 20000031 | An error occurred at the service side when processing the request. |

## Device Metadata Retrieval Client (DMRC) Errors (0x400000xx)

| Error code | Explanation |
|--|--|
| 40000011 | There's no local metadata cache. |
| 40000012 | The structure (folders) in the local metadata cache isn't correct. |
| 40000021 | There's no local metadata store. |
| 40000022 | The structure (folders) in the local metadata store is corrupted. |
| 40000031 | The DMRC index data is missing. |
| 40000032 | The DMRC index data is corrupted. |

## Device Metadata Package Errors (0x500000xx)

| Error code | Explanation |
|--|--|
| 50000011 | The *.devicemetadata-ms* cabinet (*cab*) file is corrupted. |
| 50000012 | The *.devicemetadata-ms* cab file doesn't have correct device metadata structure. |
| 50000021 | *PackageInfo.xml* is missing. |
| 50000022 | *PackageInfo.xml* isn't well-formed and can't be parsed.<br>This error code includes the cases where either the *PackageInfo.xml* document is missing required elements, or one or more of its elements aren't valid based on the syntax of the [PackageInfo XML Schema](/previous-versions/windows/hardware/metadata/ff549614(v=vs.85)). |
| 50000031 | *DeviceInfo.xml* is missing. |
| 50000032 | *DeviceInfo.xml* isn't well-formed and can't be parsed. |
| 50000033 | *DeviceInfo.xml* is missing required elements. |
| 50000034 | Elements in *DeviceInfo.xml* aren't valid based on the XML schema definition. |
| 50000041 | *WindowsInfo.xml* is missing. |
| 50000042 | *WindowsInfo.xml* isn't well-formed and can't be parsed. |
| 50000043 | *WindowsInfo.xml* is missing required elements. |
| 50000044 | Elements in *WindowsInfo.xml* aren't valid based on the XML schema definition. |

## WMIS Query (0x7000xxxx)

| Error code | Explanation |
|--|--|
| 70000408 | The WMIS server isn't down, but the request timed out. |
| 70000500 | The WMIS server returned an internal error, but a detailed error code isn't available. |
| 70000503 | The WMIS server is busy and can't service the request. |
