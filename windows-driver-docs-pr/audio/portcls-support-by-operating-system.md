---
title: PortCls Support by Operating System
description: PortCls Support by Operating System
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
---

# PortCls Support by Operating System


## <span id="portcls_support_by_operating_system"></span><span id="PORTCLS_SUPPORT_BY_OPERATING_SYSTEM"></span>


The following lists contain all the functions and interfaces that the PortCls system driver (Portcls.sys) supports. If a list item is preceded by an asterisk (\*), then PortCls supports that item only in Windows XP and later. If a list item is preceded by a double asterisk (\*\*), then PortCls supports that item only in Windows Vista and later. All other list items are supported by all versions of PortCls (Windows 2000 and later, and Windows Me/98).

### <span id="Audio_Port_Class_Functions"></span><span id="audio_port_class_functions"></span><span id="AUDIO_PORT_CLASS_FUNCTIONS"></span>Audio Port Class Functions

[**PcAddAdapterDevice**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcaddadapterdevice)

\* [**PcAddContentHandlers**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcaddcontenthandlers)

[**PcCompleteIrp**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pccompleteirp)

[**PcCompletePendingPropertyRequest**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pccompletependingpropertyrequest)

\* [**PcCreateContentMixed**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pccreatecontentmixed)

\* [**PcDestroyContent**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcdestroycontent)

[**PcDispatchIrp**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcdispatchirp)

\* [**PcForwardContentToDeviceObject**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttodeviceobject)

\* [**PcForwardContentToFileObject**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttofileobject)

\* [**PcForwardContentToInterface**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttointerface)

[**PcForwardIrpSynchronous**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardirpsynchronous)

\* [**PcGetContentRights**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgetcontentrights)

[**PcGetDeviceProperty**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgetdeviceproperty)

[**PcGetTimeInterval**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgettimeinterval)

[**PcInitializeAdapterDriver**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcinitializeadapterdriver)

[**PcNewDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewdmachannel)

[**PcNewInterruptSync**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewinterruptsync)

[**PcNewMiniport**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewminiport)

[**PcNewPort**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewport)

[**PcNewRegistryKey**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewregistrykey)

[**PcNewResourceList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcelist)

[**PcNewResourceSublist**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcesublist)

[**PcNewServiceGroup**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewservicegroup)

[**PcRegisterAdapterPowerManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisteradapterpowermanagement)

[**PcRegisterIoTimeout**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisteriotimeout)

[**PcRegisterPhysicalConnection**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisterphysicalconnection)

[**PcRegisterPhysicalConnectionFromExternal**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisterphysicalconnectionfromexternal)

[**PcRegisterPhysicalConnectionToExternal**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisterphysicalconnectiontoexternal)

[**PcRegisterSubdevice**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregistersubdevice)

[**PcRequestNewPowerState**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcrequestnewpowerstate)

[**PcUnregisterIoTimeout**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcunregisteriotimeout)

### <span id="Audio_Helper_Object_Interfaces"></span><span id="audio_helper_object_interfaces"></span><span id="AUDIO_HELPER_OBJECT_INTERFACES"></span>Audio Helper Object Interfaces

[IDmaChannel](/windows-hardware/drivers/ddi/portcls/nn-portcls-idmachannel)

[IDmaChannelSlave](/windows-hardware/drivers/ddi/portcls/nn-portcls-idmachannelslave)

\* [IDrmPort](/windows-hardware/drivers/ddi/portcls/nn-portcls-idrmport)

\* [IDrmPort2](/windows-hardware/drivers/ddi/portcls/nn-portcls-idrmport2)

[IInterruptSync](/windows-hardware/drivers/ddi/portcls/nn-portcls-iinterruptsync)

[IMasterClock](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-imasterclock)

\* [IPortClsVersion](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportclsversion)

[IPortEvents](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportevents)

\* [IPreFetchOffset](/windows-hardware/drivers/ddi/portcls/nn-portcls-iprefetchoffset)

[IRegistryKey](/windows-hardware/drivers/ddi/portcls/nn-portcls-iregistrykey)

[IResourceList](/windows-hardware/drivers/ddi/portcls/nn-portcls-iresourcelist)

[IServiceGroup](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicegroup)

[IServiceSink](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicesink)

\*\* [IUnregisterPhysicalConnection](/windows-hardware/drivers/ddi/portcls/nn-portcls-iunregisterphysicalconnection)

\*\* [IUnregisterSubdevice](/windows-hardware/drivers/ddi/portcls/nn-portcls-iunregistersubdevice)

### <span id="Audio_Port_Object_Interfaces"></span><span id="audio_port_object_interfaces"></span><span id="AUDIO_PORT_OBJECT_INTERFACES"></span>Audio Port Object Interfaces

[IPort](/windows-hardware/drivers/ddi/portcls/nn-portcls-iport)

[IPortDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iportdmus)

[IPortMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportmidi)

[IPortTopology](/windows-hardware/drivers/ddi/portcls/nn-portcls-iporttopology)

[IPortWaveCyclic](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavecyclic)

[IPortWavePci](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavepci)

\*\* [IPortWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavert)

### <span id="Audio_Miniport_Object_Interfaces"></span><span id="audio_miniport_object_interfaces"></span><span id="AUDIO_MINIPORT_OBJECT_INTERFACES"></span>Audio Miniport Object Interfaces

[IMiniport](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiport)

[IMiniportDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iminiportdmus)

[IMiniportMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidi)

[IMiniportTopology](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiporttopology)

[IMiniportWaveCyclic](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavecyclic)

[IMiniportWavePci](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavepci)

\*\* [IMiniportWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavert)

### <span id="Audio_Miniport_Auxiliary_Interfaces"></span><span id="audio_miniport_auxiliary_interfaces"></span><span id="AUDIO_MINIPORT_AUXILIARY_INTERFACES"></span>Audio Miniport Auxiliary Interfaces

\* [IMusicTechnology](/windows-hardware/drivers/ddi/portcls/nn-portcls-imusictechnology)

\* [IPinCount](/windows-hardware/drivers/ddi/portcls/nn-portcls-ipincount)

### <span id="Audio_Stream_Object_Interfaces"></span><span id="audio_stream_object_interfaces"></span><span id="AUDIO_STREAM_OBJECT_INTERFACES"></span>Audio Stream Object Interfaces

[IAllocatorMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iallocatormxf)

\* [IDrmAudioStream](/windows-hardware/drivers/ddi/drmk/nn-drmk-idrmaudiostream)

[IMiniportMidiStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidistream)

[IMiniportWaveCyclicStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavecyclicstream)

[IMiniportWavePciStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavepcistream)

\*\* [IMiniportWaveRTStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertstream)

[IMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-imxf)

[IPortWavePciStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavepcistream)

\*\* [IPortWaveRTStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavertstream)

[ISynthSinkDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-isynthsinkdmus)

### <span id="Audio_Power_Management_Interfaces"></span><span id="audio_power_management_interfaces"></span><span id="AUDIO_POWER_MANAGEMENT_INTERFACES"></span>Audio Power Management Interfaces

[IAdapterPowerManagement](/windows-hardware/drivers/ddi/portcls/nn-portcls-iadapterpowermanagement)

[IPowerNotify](/windows-hardware/drivers/ddi/portcls/nn-portcls-ipowernotify)

 

