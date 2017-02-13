---
title: GPU power management of idle states and active power
description: Starting with Windows 8, an optional GPU power management infrastructure is available that lets Windows Display Driver Model (WDDM) 1.2 and later drivers manage power for individual devices or a set of devices.
ms.assetid: F8096F7E-39EA-45CB-8A1C-60A7A298AFEC
---

# GPU power management of idle states and active power


Starting with Windows 8, an optional GPU power management infrastructure is available that lets Windows Display Driver Model (WDDM) 1.2 and later drivers manage power for individual devices or a set of devices. This infrastructure provides a standardized mechanism to support F-state and P-state power management in collaboration with Windows.

|                                                                                   |                                        |
|-----------------------------------------------------------------------------------|----------------------------------------|
| Minimum WDDM version                                                              | 1.2                                    |
| Minimum Windows version                                                           | 8                                      |
| Driver implementation                                                             | Optional                               |
| [WHCK]( http://go.microsoft.com/fwlink/p/?linkid=258342) requirements and tests | **Device.Graphicsâ€¦RuntimePowerMgmt** |

 

## <span id="GPU_power_management_device_driver_interface__DDI_"></span><span id="gpu_power_management_device_driver_interface__ddi_"></span><span id="GPU_POWER_MANAGEMENT_DEVICE_DRIVER_INTERFACE__DDI_"></span>GPU power management device driver interface (DDI)


These new and updated functions and structures are available starting with Windows 8 for the display miniport driver to transition the state of power components and to communicate power events with the Microsoft DirectX graphics kernel subsystem.

-   [*DxgkCbCompleteFStateTransition*](https://msdn.microsoft.com/library/windows/hardware/jj128349)
-   [*DxgkCbPowerRuntimeControlRequest*](https://msdn.microsoft.com/library/windows/hardware/hh451323)
-   [*DxgkCbSetPowerComponentActive*](https://msdn.microsoft.com/library/windows/hardware/hh451331)
-   [*DxgkCbSetPowerComponentIdle*](https://msdn.microsoft.com/library/windows/hardware/hh451336)
-   [*DxgkCbSetPowerComponentLatency*](https://msdn.microsoft.com/library/windows/hardware/hh698278)
-   [*DxgkCbSetPowerComponentResidency*](https://msdn.microsoft.com/library/windows/hardware/hh698279)
-   [*DxgkDdiPowerRuntimeControlRequest*](https://msdn.microsoft.com/library/windows/hardware/hh451396)
-   [*DxgkDdiSetPowerComponentFState*](https://msdn.microsoft.com/library/windows/hardware/hh451422)
-   [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062)
-   [**DXGK\_POWER\_COMPONENT\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh464063)
-   [**DXGK\_POWER\_COMPONENT\_MAPPING**](https://msdn.microsoft.com/library/windows/hardware/hh464067)
-   [**DXGK\_POWER\_COMPONENT\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh464070)
-   [**DXGK\_POWER\_RUNTIME\_COMPONENT**](https://msdn.microsoft.com/library/windows/hardware/hh464073)
-   [**DXGK\_QUERYADAPTERINFOTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff562010)
-   [**DXGKARG\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff557621)
-   [**DXGK\_QUERYSEGMENTOUT3**](https://msdn.microsoft.com/library/windows/hardware/hh464082)

## <span id="GPU_power_management_scenarios"></span><span id="gpu_power_management_scenarios"></span><span id="GPU_POWER_MANAGEMENT_SCENARIOS"></span>GPU power management scenarios


GPUs and display screens are two of the largest power consumers in laptops, mobile devices, and desktop PCs.

These are the key power management scenarios to reduce power consumption and extend battery life:

-   Mobile form factor devices can go into an idle state and save power because individual system components shut down if they are not in use.
-   Windows System on a Chip (SoC)â€“based devices behave like consumer devices and mobile phones—that is, they turn on immediately when they are needed, thereby saving energy.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation]( http://go.microsoft.com/fwlink/p/?linkid=258342) on **Device.Graphicsâ€¦RuntimePowerMgmt**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GPU%20power%20management%20of%20idle%20states%20and%20active%20power%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




