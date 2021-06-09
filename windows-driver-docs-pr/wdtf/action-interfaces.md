---
title: Action interfaces
description: The action interfaces control an instance of the IWDTFTarget2 interface. Every plug-in must support this interface.
keywords:
- Windows Device Testing Framework WDK , action interfaces
- WDTF WDK , action interfaces
- action interfaces WDK WDTF
- COM interfaces WDK WDTF
- interfaces WDK WDTF
ms.date: 06/07/2021
ms.localizationpriority: medium
---

# Action interfaces

The action interfaces control an instance of the [IWDTFTarget2](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftarget2) interface. Every plug-in must support this interface. All action interfaces inherit from [IAction](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iaction), either directly or indirectly.

You can retrieve an action interface for a target by calling the IWDTFTarget2::GetInterface method.

There are two sets of action interfaces: device action interfaces and system action interfaces.

## Device Action Interfaces

| Interface | Description |
|-|-|
|[IWDTFDriverPackageAction2](/windows-hardware/drivers/ddi/wdtfdriverpackageaction/nn-wdtfdriverpackageaction-iwdtfdriverpackageaction2) |  Defines operations and properties that represent a driver package for imported and pre-imported driver packages. |
|[IWDTFDriverSetupAction2](/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/nn-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2) | Defines operations that control the target device during driver setup. |
|[IWDTFEnhancedDeviceTestSupportAction2](/windows-hardware/drivers/ddi/wdtfedtaction/nn-wdtfedtaction-iwdtfenhanceddevicetestsupportaction2) | Defines operations and properties that support the Enhanced Device Test (EDT) filter driver. |
|[IWDTFEnhancedDeviceTestSupportActions2](/windows-hardware/drivers/ddi/wdtfedtaction/nn-wdtfedtaction-iwdtfenhanceddevicetestsupportactions2) | Defines operations and properties that support the collection of Enhanced Device Test (EDT) actions. |
|[IWDTFPNPAction2](/windows-hardware/drivers/ddi/wdtfpnpaction/nn-wdtfpnpaction-iwdtfpnpaction2) | Defines operations and properties for the Plug and Play (PNP) device-related test interfaces. |
|[IWDTFPNPActions2](/windows-hardware/drivers/ddi/wdtfpnpaction/nn-wdtfpnpaction-iwdtfpnpactions2) |Defines operations and properties for the collection of Plug and Play (PNP) device-related test interfaces. |
|[IWDTFSimpleIOEx2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleioex2) | Defines operations for a simple synchronous I/O functionality test. |
|[IWDTFSimpleIOStressAction2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) | Defines operations for a simple asynchronous I/O functionality test. |
|[IWDTFSimpleIOStressActions2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressactions2) | Defines operations for a collection of simple asynchronous I/O functionality tests. |

## System Action Interfaces

| Interface | Description |
|-|-|
|[IWDTFDriverSetupSystemAction2](/windows-hardware/drivers/ddi/wdtfdriversetupsystemaction/nn-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2) | Defines operations that control the system during driver setup. |
|[IWDTFSystemAction2](/windows-hardware/drivers/ddi/wdtfsystemaction/nn-wdtfsystemaction-iwdtfsystemaction2) | Defines operations and properties that support driver testing. |

## Remarks

In WDTF, the [IWDTFSimpleIOStressAction2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) interface is implemented once as a wrapper around the numerous SimpleIO implementations.

SimpleIO can be easier to use directly, rather than through [IWDTFSimpleIOStressAction2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2). This is because scenario code must keep a reference to each [IWDTFSimpleIOStressAction2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) instance that it starts, and remember to stop it before closing. However, because [IWDTFSimpleIOStressAction2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) runs asynchronously, it enables you to test combinations of events. For example, an [IWDTFSimpleIOStressAction2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) instance could start I/O testing for an extended period to test hardware sleep features.

## Requirements

| Header|
|-|
| WDTFDriverPackageAction (Link Pending)|
|[WDTFDriverSetupDeviceAction.h](/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/index)|
|[WDTFInterfaces.h](/windows-hardware/drivers/ddi/wdtfinterfaces/index) |
|[WDTFEDTAction.h](/windows-hardware/drivers/ddi/wdtfedtaction/index) |
|[WDTFPNPAction.h](/windows-hardware/drivers/ddi/wdtfpnpaction/index) |

## See also

[IAction](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iaction)

[IWDTFTarget2](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftarget2)

[IWDTFTarget2::GetInterface](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtftarget2-getinterface)

[IWDTFSimpleIOStressAction2](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2)
