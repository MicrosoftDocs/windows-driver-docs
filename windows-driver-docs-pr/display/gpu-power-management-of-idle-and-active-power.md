---
title: GPU power management of idle states and active power
description: A GPU power management infrastructure that lets Windows Display Driver Model (WDDM) 1.2 and later drivers manage power for individual devices or a set of devices.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPU power management of idle states and active power


Starting with Windows 8, an optional GPU power management infrastructure is available that lets Windows Display Driver Model (WDDM) 1.2 and later drivers manage power for individual devices or a set of devices. This infrastructure provides a standardized mechanism to support F-state and P-state power management in collaboration with Windows.

**Minimum WDDM version**: 1.2

**Minimum Windows version**: 8

**Driver implementation**: Optional

**[WHCK](/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests**: **Device.Graphics…RuntimePowerMgmt**


 

## <span id="GPU_power_management_device_driver_interface__DDI_"></span><span id="gpu_power_management_device_driver_interface__ddi_"></span><span id="GPU_POWER_MANAGEMENT_DEVICE_DRIVER_INTERFACE__DDI_"></span>GPU power management device driver interface (DDI)


These new and updated functions and structures are available starting with Windows 8 for the display miniport driver to transition the state of power components and to communicate power events with the Microsoft DirectX graphics kernel subsystem.

-   [*DxgkCbCompleteFStateTransition*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_completefstatetransition)
-   [*DxgkCbPowerRuntimeControlRequest*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_powerruntimecontrolrequest)
-   [*DxgkCbSetPowerComponentActive*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_setpowercomponentactive)
-   [*DxgkCbSetPowerComponentIdle*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_setpowercomponentidle)
-   [*DxgkCbSetPowerComponentLatency*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_setpowercomponentlatency)
-   [*DxgkCbSetPowerComponentResidency*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_setpowercomponentresidency)
-   [*DxgkDdiPowerRuntimeControlRequest*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddipowerruntimecontrolrequest)
-   [*DxgkDdiSetPowerComponentFState*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddisetpowercomponentfstate)
-   [**DXGK\_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps)
-   [**DXGK\_POWER\_COMPONENT\_FLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_power_component_flags)
-   [**DXGK\_POWER\_COMPONENT\_MAPPING**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_power_component_mapping)
-   [**DXGK\_POWER\_COMPONENT\_TYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_power_component_type)
-   [**DXGK\_POWER\_RUNTIME\_COMPONENT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_power_runtime_component)
-   [**DXGK\_QUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype)
-   [**DXGKARG\_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryadapterinfo)
-   [**DXGK\_QUERYSEGMENTOUT3**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_querysegmentout3)

## <span id="GPU_power_management_scenarios"></span><span id="gpu_power_management_scenarios"></span><span id="GPU_POWER_MANAGEMENT_SCENARIOS"></span>GPU power management scenarios


GPUs and display screens are two of the largest power consumers in laptops, mobile devices, and desktop PCs.

These are the key power management scenarios to reduce power consumption and extend battery life:

-   Mobile form factor devices can go into an idle state and save power because individual system components shut down if they are not in use.
-   Windows System on a Chip (SoC)–based devices behave like consumer devices and mobile phones that is, they turn on immediately when they are needed, thereby saving energy.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics…RuntimePowerMgmt**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

