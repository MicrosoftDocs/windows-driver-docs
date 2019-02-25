---
title: PortCls Support by Operating System
description: PortCls Support by Operating System
ms.assetid: 87291410-41fa-49d2-a1e2-6d5d9b90deaf
keywords:
- audio miniport drivers WDK , Port Class
- miniport drivers WDK audio , Port Class
- Port Class library WDK audio
- PortCls WDK audio , support per operating system
- audio power management interfaces WDK
- audio stream object interfaces WDK
- audio miniport auxillary interfaces WDK
- audio miniport object interfaces WDK
- audio port object interfaces WDK
- audio helper object interfaces WDK
- audio port class interfaces WDK
- interfaces WDK Port Class
- prefetch offset
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PortCls Support by Operating System


## <span id="portcls_support_by_operating_system"></span><span id="PORTCLS_SUPPORT_BY_OPERATING_SYSTEM"></span>


The following lists contain all the functions and interfaces that the PortCls system driver (Portcls.sys) supports. If a list item is preceded by an asterisk (\*), then PortCls supports that item only in Windows XP and later. If a list item is preceded by a double asterisk (\*\*), then PortCls supports that item only in Windows Vista and later. All other list items are supported by all versions of PortCls (Windows 2000 and later, and Windows Me/98).

### <span id="Audio_Port_Class_Functions"></span><span id="audio_port_class_functions"></span><span id="AUDIO_PORT_CLASS_FUNCTIONS"></span>Audio Port Class Functions

[**PcAddAdapterDevice**](https://msdn.microsoft.com/library/windows/hardware/ff537683)

\* [**PcAddContentHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff537684)

[**PcCompleteIrp**](https://msdn.microsoft.com/library/windows/hardware/ff537686)

[**PcCompletePendingPropertyRequest**](https://msdn.microsoft.com/library/windows/hardware/ff537687)

\* [**PcCreateContentMixed**](https://msdn.microsoft.com/library/windows/hardware/ff537689)

\* [**PcDestroyContent**](https://msdn.microsoft.com/library/windows/hardware/ff537690)

[**PcDispatchIrp**](https://msdn.microsoft.com/library/windows/hardware/ff537691)

\* [**PcForwardContentToDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff537696)

\* [**PcForwardContentToFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff537697)

\* [**PcForwardContentToInterface**](https://msdn.microsoft.com/library/windows/hardware/ff537698)

[**PcForwardIrpSynchronous**](https://msdn.microsoft.com/library/windows/hardware/ff537699)

\* [**PcGetContentRights**](https://msdn.microsoft.com/library/windows/hardware/ff537700)

[**PcGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff537701)

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

[**PcUnregisterIoTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff537736)

### <span id="Audio_Helper_Object_Interfaces"></span><span id="audio_helper_object_interfaces"></span><span id="AUDIO_HELPER_OBJECT_INTERFACES"></span>Audio Helper Object Interfaces

[IDmaChannel](https://msdn.microsoft.com/library/windows/hardware/ff536547)

[IDmaChannelSlave](https://msdn.microsoft.com/library/windows/hardware/ff536548)

\* [IDrmPort](https://msdn.microsoft.com/library/windows/hardware/ff536571)

\* [IDrmPort2](https://msdn.microsoft.com/library/windows/hardware/ff536573)

[IInterruptSync](https://msdn.microsoft.com/library/windows/hardware/ff536590)

[IMasterClock](https://msdn.microsoft.com/library/windows/hardware/ff536696)

\* [IPortClsVersion](https://msdn.microsoft.com/library/windows/hardware/ff536877)

[IPortEvents](https://msdn.microsoft.com/library/windows/hardware/ff536884)

\* [IPreFetchOffset](https://msdn.microsoft.com/library/windows/hardware/ff536951)

[IRegistryKey](https://msdn.microsoft.com/library/windows/hardware/ff536965)

[IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976)

[IServiceGroup](https://msdn.microsoft.com/library/windows/hardware/ff536994)

[IServiceSink](https://msdn.microsoft.com/library/windows/hardware/ff537006)

\*\* [IUnregisterPhysicalConnection](https://msdn.microsoft.com/library/windows/hardware/ff537022)

\*\* [IUnregisterSubdevice](https://msdn.microsoft.com/library/windows/hardware/ff537030)

### <span id="Audio_Port_Object_Interfaces"></span><span id="audio_port_object_interfaces"></span><span id="AUDIO_PORT_OBJECT_INTERFACES"></span>Audio Port Object Interfaces

[IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842)

[IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879)

[IPortMidi](https://msdn.microsoft.com/library/windows/hardware/ff536891)

[IPortTopology](https://msdn.microsoft.com/library/windows/hardware/ff536896)

[IPortWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536899)

[IPortWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536905)

\*\* [IPortWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536920)

### <span id="Audio_Miniport_Object_Interfaces"></span><span id="audio_miniport_object_interfaces"></span><span id="AUDIO_MINIPORT_OBJECT_INTERFACES"></span>Audio Miniport Object Interfaces

[IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698)

[IMiniportDMus](https://msdn.microsoft.com/library/windows/hardware/ff536699)

[IMiniportMidi](https://msdn.microsoft.com/library/windows/hardware/ff536703)

[IMiniportTopology](https://msdn.microsoft.com/library/windows/hardware/ff536712)

[IMiniportWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536714)

[IMiniportWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536724)

\*\* [IMiniportWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536737)

### <span id="Audio_Miniport_Auxiliary_Interfaces"></span><span id="audio_miniport_auxiliary_interfaces"></span><span id="AUDIO_MINIPORT_AUXILIARY_INTERFACES"></span>Audio Miniport Auxiliary Interfaces

\* [IMusicTechnology](https://msdn.microsoft.com/library/windows/hardware/ff536778)

\* [IPinCount](https://msdn.microsoft.com/library/windows/hardware/ff536832)

### <span id="Audio_Stream_Object_Interfaces"></span><span id="audio_stream_object_interfaces"></span><span id="AUDIO_STREAM_OBJECT_INTERFACES"></span>Audio Stream Object Interfaces

[IAllocatorMXF](https://msdn.microsoft.com/library/windows/hardware/ff536491)

\* [IDrmAudioStream](https://msdn.microsoft.com/library/windows/hardware/ff536568)

[IMiniportMidiStream](https://msdn.microsoft.com/library/windows/hardware/ff536704)

[IMiniportWaveCyclicStream](https://msdn.microsoft.com/library/windows/hardware/ff536715)

[IMiniportWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536725)

\*\* [IMiniportWaveRTStream](https://msdn.microsoft.com/library/windows/hardware/ff536738)

[IMXF](https://msdn.microsoft.com/library/windows/hardware/ff536782)

[IPortWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536907)

\*\* [IPortWaveRTStream](https://msdn.microsoft.com/library/windows/hardware/ff536922)

[ISynthSinkDMus](https://msdn.microsoft.com/library/windows/hardware/ff537011)

### <span id="Audio_Power_Management_Interfaces"></span><span id="audio_power_management_interfaces"></span><span id="AUDIO_POWER_MANAGEMENT_INTERFACES"></span>Audio Power Management Interfaces

[IAdapterPowerManagement](https://msdn.microsoft.com/library/windows/hardware/ff536485)

[IPowerNotify](https://msdn.microsoft.com/library/windows/hardware/ff536947)

 

 




