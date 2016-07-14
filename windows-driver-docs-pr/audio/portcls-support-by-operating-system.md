---
Description: PortCls Support by Operating System
MS-HAID: 'audio.portcls\_support\_by\_operating\_system'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: PortCls Support by Operating System
---

# PortCls Support by Operating System


## <span id="portcls_support_by_operating_system"></span><span id="PORTCLS_SUPPORT_BY_OPERATING_SYSTEM"></span>


The following lists contain all the functions and interfaces that the PortCls system driver (Portcls.sys) supports. If a list item is preceded by an asterisk (\*), then PortCls supports that item only in Windows XP and later. If a list item is preceded by a double asterisk (\*\*), then PortCls supports that item only in Windows Vista and later. All other list items are supported by all versions of PortCls (Windows 2000 and later, and Windows Me/98).

### <span id="Audio_Port_Class_Functions"></span><span id="audio_port_class_functions"></span><span id="AUDIO_PORT_CLASS_FUNCTIONS"></span>Audio Port Class Functions

[**PcAddAdapterDevice**](audio.pcaddadapterdevice)

\* [**PcAddContentHandlers**](audio.pcaddcontenthandlers)

[**PcCompleteIrp**](audio.pccompleteirp)

[**PcCompletePendingPropertyRequest**](audio.pccompletependingpropertyrequest)

\* [**PcCreateContentMixed**](audio.pccreatecontentmixed)

\* [**PcDestroyContent**](audio.pcdestroycontent)

[**PcDispatchIrp**](audio.pcdispatchirp)

\* [**PcForwardContentToDeviceObject**](audio.pcforwardcontenttodeviceobject)

\* [**PcForwardContentToFileObject**](audio.pcforwardcontenttofileobject)

\* [**PcForwardContentToInterface**](audio.pcforwardcontenttointerface)

[**PcForwardIrpSynchronous**](audio.pcforwardirpsynchronous)

\* [**PcGetContentRights**](audio.pcgetcontentrights)

[**PcGetDeviceProperty**](audio.pcgetdeviceproperty)

[**PcGetTimeInterval**](audio.pcgettimeinterval)

[**PcInitializeAdapterDriver**](audio.pcinitializeadapterdriver)

[**PcNewDmaChannel**](audio.pcnewdmachannel)

[**PcNewInterruptSync**](audio.pcnewinterruptsync)

[**PcNewMiniport**](audio.pcnewminiport)

[**PcNewPort**](audio.pcnewport)

[**PcNewRegistryKey**](audio.pcnewregistrykey)

[**PcNewResourceList**](audio.pcnewresourcelist)

[**PcNewResourceSublist**](audio.pcnewresourcesublist)

[**PcNewServiceGroup**](audio.pcnewservicegroup)

[**PcRegisterAdapterPowerManagement**](audio.pcregisteradapterpowermanagement)

[**PcRegisterIoTimeout**](audio.pcregisteriotimeout)

[**PcRegisterPhysicalConnection**](audio.pcregisterphysicalconnection)

[**PcRegisterPhysicalConnectionFromExternal**](audio.pcregisterphysicalconnectionfromexternal)

[**PcRegisterPhysicalConnectionToExternal**](audio.pcregisterphysicalconnectiontoexternal)

[**PcRegisterSubdevice**](audio.pcregistersubdevice)

[**PcRequestNewPowerState**](audio.pcrequestnewpowerstate)

[**PcUnregisterIoTimeout**](audio.pcunregisteriotimeout)

### <span id="Audio_Helper_Object_Interfaces"></span><span id="audio_helper_object_interfaces"></span><span id="AUDIO_HELPER_OBJECT_INTERFACES"></span>Audio Helper Object Interfaces

[IDmaChannel](audio.idmachannel)

[IDmaChannelSlave](audio.idmachannelslave)

\* [IDrmPort](audio.idrmport)

\* [IDrmPort2](audio.idrmport2)

[IInterruptSync](audio.iinterruptsync)

[IMasterClock](audio.imasterclock)

\* [IPortClsVersion](audio.iportclsversion)

[IPortEvents](audio.iportevents)

\* [IPreFetchOffset](audio.iprefetchoffset)

[IRegistryKey](audio.iregistrykey)

[IResourceList](audio.iresourcelist)

[IServiceGroup](audio.iservicegroup)

[IServiceSink](audio.iservicesink)

\*\* [IUnregisterPhysicalConnection](audio.iunregisterphysicalconnection)

\*\* [IUnregisterSubdevice](audio.iunregistersubdevice)

### <span id="Audio_Port_Object_Interfaces"></span><span id="audio_port_object_interfaces"></span><span id="AUDIO_PORT_OBJECT_INTERFACES"></span>Audio Port Object Interfaces

[IPort](audio.iport)

[IPortDMus](audio.iportdmus)

[IPortMidi](audio.iportmidi)

[IPortTopology](audio.iporttopology)

[IPortWaveCyclic](audio.iportwavecyclic)

[IPortWavePci](audio.iportwavepci)

\*\* [IPortWaveRT](audio.iportwavert)

### <span id="Audio_Miniport_Object_Interfaces"></span><span id="audio_miniport_object_interfaces"></span><span id="AUDIO_MINIPORT_OBJECT_INTERFACES"></span>Audio Miniport Object Interfaces

[IMiniport](audio.iminiport)

[IMiniportDMus](audio.iminiportdmus)

[IMiniportMidi](audio.iminiportmidi)

[IMiniportTopology](audio.iminiporttopology)

[IMiniportWaveCyclic](audio.iminiportwavecyclic)

[IMiniportWavePci](audio.iminiportwavepci)

\*\* [IMiniportWaveRT](audio.iminiportwavert)

### <span id="Audio_Miniport_Auxiliary_Interfaces"></span><span id="audio_miniport_auxiliary_interfaces"></span><span id="AUDIO_MINIPORT_AUXILIARY_INTERFACES"></span>Audio Miniport Auxiliary Interfaces

\* [IMusicTechnology](audio.imusictechnology)

\* [IPinCount](audio.ipincount)

### <span id="Audio_Stream_Object_Interfaces"></span><span id="audio_stream_object_interfaces"></span><span id="AUDIO_STREAM_OBJECT_INTERFACES"></span>Audio Stream Object Interfaces

[IAllocatorMXF](audio.iallocatormxf)

\* [IDrmAudioStream](audio.idrmaudiostream)

[IMiniportMidiStream](audio.iminiportmidistream)

[IMiniportWaveCyclicStream](audio.iminiportwavecyclicstream)

[IMiniportWavePciStream](audio.iminiportwavepcistream)

\*\* [IMiniportWaveRTStream](audio.iminiportwavertstream)

[IMXF](audio.imxf)

[IPortWavePciStream](audio.iportwavepcistream)

\*\* [IPortWaveRTStream](audio.iportwavertstream)

[ISynthSinkDMus](audio.isynthsinkdmus)

### <span id="Audio_Power_Management_Interfaces"></span><span id="audio_power_management_interfaces"></span><span id="AUDIO_POWER_MANAGEMENT_INTERFACES"></span>Audio Power Management Interfaces

[IAdapterPowerManagement](audio.iadapterpowermanagement)

[IPowerNotify](audio.ipowernotify)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20PortCls%20Support%20by%20Operating%20System%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



