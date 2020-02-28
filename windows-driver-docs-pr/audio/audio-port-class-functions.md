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

For a list of which versions of the operating system support the various PortCls functions, see [PortCls Support by Operating System](https://docs.microsoft.com/windows-hardware/drivers/audio/portcls-support-by-operating-system).

PortCls implements the following functions:

[**PcAddAdapterDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcaddadapterdevice)

[**PcAddContentHandlers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcaddcontenthandlers)

[**PcCompleteIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pccompleteirp)

[**PcCompletePendingPropertyRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pccompletependingpropertyrequest)

[**PcCreateContentMixed**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pccreatecontentmixed)

[**PcDestroyContent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcdestroycontent)

[**PcDispatchIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcdispatchirp)

[**PcForwardContentToDeviceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttodeviceobject)

[**PcForwardContentToFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttofileobject)

[**PcForwardContentToInterface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttointerface)

[**PcForwardIrpSynchronous**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardirpsynchronous)

[**PcGetContentRights**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgetcontentrights)

[**PcGetDeviceProperty**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgetdeviceproperty)

[**PcGetPhysicalDeviceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgetphysicaldeviceobject)

[**PcGetTimeInterval**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgettimeinterval)

[**PcInitializeAdapterDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcinitializeadapterdriver)

[**PcNewDmaChannel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewdmachannel)

[**PcNewInterruptSync**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewinterruptsync)

[**PcNewMiniport**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewminiport)

[**PcNewPort**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewport)

[**PcNewRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewregistrykey)

[**PcNewResourceList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcelist)

[**PcNewResourceSublist**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcesublist)

[**PcNewServiceGroup**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewservicegroup)

[**PcRegisterAdapterPowerManagement**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisteradapterpowermanagement)

[**PcRegisterIoTimeout**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisteriotimeout)

[**PcRegisterPhysicalConnection**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisterphysicalconnection)

[**PcRegisterPhysicalConnectionFromExternal**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisterphysicalconnectionfromexternal)

[**PcRegisterPhysicalConnectionToExternal**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisterphysicalconnectiontoexternal)

[**PcRegisterSubdevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregistersubdevice)

[**PcRequestNewPowerState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcrequestnewpowerstate)

[**PcUnregisterAdapterPowerManagement**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcunregisteradapterpowermanagement)

[**PcUnregisterIoTimeout**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-pcunregisteriotimeout)

 

 





