---
title: IoSpy
description: IoSpy is a filter driver that records data about IOCTL and Windows Management Instrumentation (WMI) requests made to the kernel-mode driver of a device.
ms.date: 02/05/2026
ms.topic: concept-article
---

# IoSpy

IoSpy is a filter driver that records data about IOCTL and Windows Management Instrumentation (WMI) requests made to the kernel-mode driver of a device.

You can install and remove IoSpy using the [Penetration Tests (Device Fundamentals)](coverage-tests--device-fundamentals-.md) tests, **Enable I/O Spy** and **Disable I/O Spy**. The *DQ* parameter controls which devices the IoSpy filter driver is installed on. IoSpy records the details about the IOCTL and WMI requests within the [IoSpy data file](#iospy-data-file), which is used by [IoAttack](ioattack.md) to perform the fuzz tests.

> [!IMPORTANT]
> Before you run IoAttack, you must have previously run IoSpy and then removed it from the test system. For more information, see [How to Perform Fuzz tests with IoSpy and IoAttack](how-to-perform-fuzz-tests-with-iospy-and-ioattack.md).

| Term | Description |
|------|-------------|
| **Disable I/O Spy** | Disable I/O Spy on one or more devices. Uninstalls IoSpy and disables IOCTL and WMI filtering for all devices on the test system.<br><br>**Test binary:** Devfund_IOSpy_DisableSupport.wsc<br>**Test method:** DisableIoSpy<br>**Parameters:** - see [Device Fundamentals Test Parameters](../develop/how-to-select-and-configure-the-device-fundamental-tests.md#device-fundamentals-test-parameters)<br><br>*DQ* |
| **Display I/O Spy-enabled Device** | Display devices that have I/O Spy enabled on them.<br><br>**Test binary:** Devfund_IOSpy_DisplayEnabledDevices.wsc<br>**Test method:** DisplayIoSpyDevices |
| **Enable I/O Spy** | Installs IoSpy on the test system and enables IOCTL and WMI filtering on one or more devices. The DQ parameter controls which devices the IoSpy filter driver gets installed on.<br><br>**Test binary:** Devfund_IOSpy_EnableSupport.wsc<br>**Test method:** EnableIoSpy<br>**Parameters:** - see [Device Fundamentals Test Parameters](../develop/how-to-select-and-configure-the-device-fundamental-tests.md#device-fundamentals-test-parameters)<br><br>*DQ*<br><br>*DFD* - specifies the path to the IoSpy data file. The default location is %SystemDrive%\DriverTest\IoSpy |

## IoSpy data file

After IoSpy is installed in a test system, it records the data sent through IOCTL and WMI requests to the drivers for devices enabled for fuzz tests. While IoSpy doesn't analyze the payloads of these requests, it does record the details of the requests such as the length of the payload buffers.

The *DFD* parameter for the **Enable I/O Spy** test specifies the path to the IoSpy data file. The default location is %SystemDrive%\\DriverTest\\IoSpy
