---
title: GPU power management of idle states and active power
description: A GPU power management infrastructure that lets Windows Display Driver Model (WDDM) 1.2 and later drivers manage power for individual devices or a set of devices.
ms.assetid: F8096F7E-39EA-45CB-8A1C-60A7A298AFEC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPU power management of idle states and active power


Starting with Windows 8, an optional GPU power management infrastructure is available that lets Windows Display Driver Model (WDDM) 1.2 and later drivers manage power for individual devices or a set of devices. This infrastructure provides a standardized mechanism to support F-state and P-state power management in collaboration with Windows.

|                                                                                   |                                        |
|-----------------------------------------------------------------------------------|----------------------------------------|
| Minimum WDDM version                                                              | 1.2                                    |
| Minimum Windows version                                                           | 8                                      |
| Driver implementation                                                             | Optional                               |
| [WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests | **Device.Graphics…RuntimePowerMgmt** |

 

## <span id="GPU_power_management_device_driver_interface__DDI_"></span><span id="gpu_power_management_device_driver_interface__ddi_"></span><span id="GPU_POWER_MANAGEMENT_DEVICE_DRIVER_INTERFACE__DDI_"></span>GPU power management device driver interface (DDI)


These new and updated functions and structures are available starting with Windows 8 for the display miniport driver to transition the state of power components and to communicate power events with the Microsoft DirectX graphics kernel subsystem.

-   [*DxgkCbCompleteFStateTransition*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkcb_completefstatetransition)
-   [*DxgkCbPowerRuntimeControlRequest*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkcb_powerruntimecontrolrequest)
-   [*DxgkCbSetPowerComponentActive*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkcb_setpowercomponentactive)
-   [*DxgkCbSetPowerComponentIdle*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkcb_setpowercomponentidle)
-   [*DxgkCbSetPowerComponentLatency*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkcb_setpowercomponentlatency)
-   [*DxgkCbSetPowerComponentResidency*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkcb_setpowercomponentresidency)
-   [*DxgkDdiPowerRuntimeControlRequest*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddipowerruntimecontrolrequest)
-   [*DxgkDdiSetPowerComponentFState*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddisetpowercomponentfstate)
-   [**DXGK\_DRIVERCAPS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps)
-   [**DXGK\_POWER\_COMPONENT\_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_power_component_flags)
-   [**DXGK\_POWER\_COMPONENT\_MAPPING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_power_component_mapping)
-   [**DXGK\_POWER\_COMPONENT\_TYPE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ne-d3dkmddi-_dxgk_power_component_type)
-   [**DXGK\_POWER\_RUNTIME\_COMPONENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_power_runtime_component)
-   [**DXGK\_QUERYADAPTERINFOTYPE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype)
-   [**DXGKARG\_QUERYADAPTERINFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryadapterinfo)
-   [**DXGK\_QUERYSEGMENTOUT3**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_querysegmentout3)

## <span id="GPU_power_management_scenarios"></span><span id="gpu_power_management_scenarios"></span><span id="GPU_POWER_MANAGEMENT_SCENARIOS"></span>GPU power management scenarios


GPUs and display screens are two of the largest power consumers in laptops, mobile devices, and desktop PCs.

These are the key power management scenarios to reduce power consumption and extend battery life:

-   Mobile form factor devices can go into an idle state and save power because individual system components shut down if they are not in use.
-   Windows System on a Chip (SoC)–based devices behave like consumer devices and mobile phones that is, they turn on immediately when they are needed, thereby saving energy.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics…RuntimePowerMgmt**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





