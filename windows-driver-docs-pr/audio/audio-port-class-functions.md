---
title: Audio Port Class Functions
description: Audio Port Class Functions
ms.assetid: dc8f32e8-b01c-4f06-a32f-c08f76001f79
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Port Class Functions


## <span id="ddk_audio_port_class_functions_ks"></span><span id="DDK_AUDIO_PORT_CLASS_FUNCTIONS_KS"></span>


This section describes, in alphabetic order, the general functions that the PortCls system driver (portcls.sys) provides. These functions do not belong to any interface. They are used by audio miniport drivers to perform operations of general utility such as registering with the PortCls and installing subdevices.

For a list of which versions of the operating system support the various PortCls functions, see [PortCls Support by Operating System](https://msdn.microsoft.com/library/windows/hardware/ff537762).

PortCls implements the following functions:

[**PcAddAdapterDevice**](https://msdn.microsoft.com/library/windows/hardware/ff537683)

[**PcAddContentHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff537684)

[**PcCompleteIrp**](https://msdn.microsoft.com/library/windows/hardware/ff537686)

[**PcCompletePendingPropertyRequest**](https://msdn.microsoft.com/library/windows/hardware/ff537687)

[**PcCreateContentMixed**](https://msdn.microsoft.com/library/windows/hardware/ff537689)

[**PcDestroyContent**](https://msdn.microsoft.com/library/windows/hardware/ff537690)

[**PcDispatchIrp**](https://msdn.microsoft.com/library/windows/hardware/ff537691)

[**PcForwardContentToDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff537696)

[**PcForwardContentToFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff537697)

[**PcForwardContentToInterface**](https://msdn.microsoft.com/library/windows/hardware/ff537698)

[**PcForwardIrpSynchronous**](https://msdn.microsoft.com/library/windows/hardware/ff537699)

[**PcGetContentRights**](https://msdn.microsoft.com/library/windows/hardware/ff537700)

[**PcGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff537701)

[**PcGetPhysicalDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/hh706182)

[**PcGetTimeInterval**](https://msdn.microsoft.com/library/windows/hardware/ff537702)

[**PcInitializeAdapterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff537703)

[**PcNewDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff537712)

[**PcNewInterruptSync**](https://msdn.microsoft.com/library/windows/hardware/ff537713)

[**PcNewMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff537714)

[**PcNewPort**](https://msdn.microsoft.com/library/windows/hardware/ff537715)

[**PcNewRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff537716)

[**PcNewResourceList**](https://msdn.microsoft.com/library/windows/hardware/ff537717)

[**PcNewResourceSublist**](https://msdn.microsoft.com/library/windows/hardware/ff537718)

[**PcNewServiceGroup**](https://msdn.microsoft.com/library/windows/hardware/ff537719)

[**PcRegisterAdapterPowerManagement**](https://msdn.microsoft.com/library/windows/hardware/ff537724)

[**PcRegisterIoTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff537725)

[**PcRegisterPhysicalConnection**](https://msdn.microsoft.com/library/windows/hardware/ff537726)

[**PcRegisterPhysicalConnectionFromExternal**](https://msdn.microsoft.com/library/windows/hardware/ff537728)

[**PcRegisterPhysicalConnectionToExternal**](https://msdn.microsoft.com/library/windows/hardware/ff537729)

[**PcRegisterSubdevice**](https://msdn.microsoft.com/library/windows/hardware/ff537731)

[**PcRequestNewPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff537733)

[**PcUnregisterAdapterPowerManagement**](https://msdn.microsoft.com/library/windows/hardware/ff537735)

[**PcUnregisterIoTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff537736)

 

 





