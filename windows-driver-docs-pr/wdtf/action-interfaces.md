---
title: Action interfaces
description: The action interfaces control an instance of the IWDTFTarget2 interface. Every plug-in must support this interface.
keywords:
- Windows Device Testing Framework WDK , action interfaces
- WDTF WDK , action interfaces
- action interfaces WDK WDTF
- COM interfaces WDK WDTF
- interfaces WDK WDTF
ms.date: 04/24/2018
ms.localizationpriority: medium
---

# Action interfaces

The action interfaces control an instance of the [IWDTFTarget2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtf/nn-wdtf-iwdtftarget2) interface. Every plug-in must support this interface. All action interfaces inherit from [IAction](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtf/nn-wdtf-iaction), either directly or indirectly. 

You can retrieve an action interface for a target by calling the IWDTFTarget2::GetInterface method.

There are two sets of action interfaces: device action interfaces and system actoin interfaces.

### Device Action Interfaces

| Interface | Description |
|-|-|
|[IWDTFDriverPackageAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfdriverpackageaction/nn-wdtfdriverpackageaction-iwdtfdriverpackageaction2) |  Defines operations and properties that represent a driver package for imported and pre-imported driver packages. |
|[IWDTFDriverSetupAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfdriversetupdeviceaction/nn-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2) | Defines operations that control the target device during driver setup. |
|[IWDTFEnhancedDeviceTestSupportAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfedtaction/nn-wdtfedtaction-iwdtfenhanceddevicetestsupportaction2) | Defines operations and properties that support the Enhanced Device Test (EDT) filter driver. |
|[IWDTFEnhancedDeviceTestSupportActions2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfedtaction/nn-wdtfedtaction-iwdtfenhanceddevicetestsupportactions2) | Defines operations and properties that support the collection of Enhanced Device Test (EDT) actions. |
|[IWDTFPNPAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfpnpaction/nn-wdtfpnpaction-iwdtfpnpaction2) | Defines operations and properties for the Plug and Play (PNP) device-related test interfaces. |
|[IWDTFPNPActions2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfpnpaction/nn-wdtfpnpaction-iwdtfpnpactions2) |Defines operations and properties for the collection of Plug and Play (PNP) device-related test interfaces. |
|[IWDTFSimpleIOEx2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleioex2) | Defines operations for a simple synchronous I/O functionality test. |
|[IWDTFSimpleIOStressAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) | Defines operations for a simple asynchronous I/O functionality test. |
|[IWDTFSimpleIOStressActions2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressactions2) | Defines operations for a collection of simple asynchronous I/O functionality tests. |
 
### System Action Interfaces

| Interface | Description |
|-|-|
|[IWDTFDriverSetupSystemAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfdriversetupsystemaction/nn-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2) | Defines operations that control the system during driver setup. |
|[IWDTFSystemAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfsystemaction/nn-wdtfsystemaction-iwdtfsystemaction2) | Defines operations and properties that support driver testing. |
 

## Remarks

In WDTF, the [IWDTFSimpleIOStressAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) interface is implemented once as a wrapper around the numerous SimpleIO implementations.

SimpleIO can be easier to use directly, rather than through [IWDTFSimpleIOStressAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2). This is because scenario code must keep a reference to each [IWDTFSimpleIOStressAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) instance that it starts, and remember to stop it before closing. However, because [IWDTFSimpleIOStressAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) runs asynchronously, it enables you to test combinations of events. For example, an [IWDTFSimpleIOStressAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) instance could start I/O testing for an extended period to test hardware sleep features.

## Requirements

| Header|
|-|
|[WDTFDriverPackageAction.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfdriverpackageaction/index)|
|[WDTFDriverSetupDeviceAction.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfdriversetupdeviceaction/index)|
|[WDTFInterfaces.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/index) |
|[WDTFEDTAction.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfedtaction/index) |
|[WDTFPNPAction.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfpnpaction/index) |


## See also
[IAction](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtf/nn-wdtf-iaction)

[IWDTFTarget2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtf/nn-wdtf-iwdtftarget2) 

[IWDTFTarget2::GetInterface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtf/nf-wdtf-iwdtftarget2-getinterface)

[IWDTFSimpleIOStressAction2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) 
