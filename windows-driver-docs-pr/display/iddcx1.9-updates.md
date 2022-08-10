---
title: Updates for IddCx versions 1.9 and later
description: IddCx version 1.9 updates for console and remote indirect display drivers
ms.date: 08/09/2022
keywords:
- IddCx version 1.9
- Console and remote indirect display driver, IddCx versions 1.9 and later
- Console and remote IDD, IddCx versions 1.9 and later
- Console indirect display driver
- Console IDD
- Remote indirect display driver
- Remote IDD
---

# Updates for IddCx versions 1.9 and later

This page describes the changes made in IddCx 1.9. A single indirect display driver (IDD) binary built against IddCx 1.9 can run on Windows 10, version 1803 and above using runtime checks to verify whether DDI changes in IddCx 1.9 are available on that system. See [Building a WDF driver for multiple versions of Windows](/windows-hardware/drivers/wdf/building-a-wdf-driver-for-multiple-versions-of-windows) for more info.

The IddCx 1.9 changes fall into the following categories:

* The [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) version was updated. See [IddCx versions](iddcx-versions.md) for a complete list of IddCx-related version information.
* A DDI was added that allows an IDD to bump video scheduler priority to the realtime priority band.
* UMDF process pooling is disallowed.

## Updated IddCxGetVersion version

The IddCx version returned by [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) on Windows 11 version 22H2 was updated to IDDCX_VERSION_SV2 (0x1900).

## IddCxSetRealtimeGPUPriority was added for raising video scheduler priority

The [**IddCxSetRealtimeGPUPriority**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxsetrealtimegpupriority) DDI was introduced to allow the IDD to raise the GPU priority of GPU devices being used in the present path to process the desktop frame. This ability is useful to avoid GPU starvation for IDD GPU work when GPU workload is high.

## Required IddCx 1.9 driver INF update to disallow UMDF process pooling

To reduce the surface for abuse of **IddCxSetRealtimeGPUPriority** for denial of service attacks, IddCx 1.9 drivers are not allowed to share process with other UMDF drivers. An IddCx 1.9 driver need to add the following in their inf file.

``` Registry
HKR, "WUDF", "DeviceGroupId", %REG_SZ%, "<DriverGroupName>" 
```

See the INF file in the [GitHub IndirectDisplay sample](https://github.com/microsoft/windows-driver-samples/tree/main/video/IndirectDisplay) for an example.

An [HLK test](/windows-hardware/test/hlk/) was added to verify an IddCx 1.9 driver's INF prior to WHQL certification.
