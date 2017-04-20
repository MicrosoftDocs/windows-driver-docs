---
title: Opting Out of Volume Level Persistence
description: Opting Out of Volume Level Persistence
ms.assetid: e96533be-25e8-49ae-8e56-7105dfa92b5a
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Opting Out of Volume Level Persistence


By default the volume level settings are maintained when you restart your computer. This default system behavior is referred to as *volume persistence*. If you do not want the volume levels to be maintained by the system after a computer restart, you can use an INF file at the time of installation of the audio adapter, to opt out of the default system behavior.

You may want your driver to opt out of volume persistence if your driver had its own registry cache and sets the levels on the hardware itself, on driver load.

To opt out of volume persistence using an INF file, use the [**AddProperty**](https://msdn.microsoft.com/library/windows/hardware/ff546318) registry directive to set the value of the PKEY\_AudioDevice\_DontPersistControls registry key to "1". The default value is "0".

The following INF file fragment shows how to opt out of volume persistence:

```
 
;; INF file fragment to show how to use AddProperty
;; to opt out of volume persistence
;;
[Version]
Signature = "$CHICAGO$"
Class = MEDIA
ClassGUID = {...}
...
[Manufacturer]
%MfgName% = CompanyName
...
[CompanyName]
%DeviceDescription% = HdAudModel, hw-id
;; ... other device models listed here

[HdAudModel]
Include=ks.inf, wdmaudio.inf
Needs=KS.Registration, WDMAUDIO.Registration
CopyFiles = HdAudModel.CopyList, HdAudProp.CopyList, HdAudShortCut.CopyList
AddReg = HdAudModel.AddReg, HdAudProp.AddReg, HdAudShortCut.AddReg, HdAudBranding.AddReg
AddProperty = HdAudModel.AddProperty
...
[HdAudModel.AddProperty]
;; {F3E80BEF-1723-4FF2-BCC4-7F83DC5E46D4},2,7,,0
{F3E80BEF-1723-4FF2-BCC4-7F83DC5E46D4},2,7,,1
...
[Strings]
MfgName = "My Company Name Inc"
DeviceDescription = "My WDM device driver"
```

**Note**  The preceding INF file fragment, only shows the **Version** section and the sections relevant to the [**AddProperty**](https://msdn.microsoft.com/library/windows/hardware/ff546318) directive.

 

The **%MfgName% = CompanyName** line entry in the **Manufacturer** section references the **CompanyName** section where the model and hardware ID (hw-id) of the audio adapter are provided. This section in an INF file, where model and hw-id information is provided, is called the *models section*. The actual title of the section is user-defined and in the preceding example it is **CompanyName**. For more information about the models section of an INF file, see [**INF Models Section**](https://msdn.microsoft.com/library/windows/hardware/ff547456).

The models section, in turn, references the device driver install (DDInstall) section, where information is provided about other INF files that the setup program must copy. The actual title of this section is user-defined and in the preceding example it is **HdAudModel**. The **Needs=KS.Registration...** line entry provides information about the specific sections within the INF files, from which the setup program must retrieve data for installation

The **HdAudModel** section also contains references to the AddReg and AddProperty sections. The setup program retrieves data from AddReg and AddProperty to set registry keys and device properties respectively. The AddProperty section referenced here is **HdAudModel.AddProperty** and it uses the following format to provide information about the device property:

{*property-category-guid*}, *property-pid*, *type*, \[*flags*\], *value*

The **HdAudModel** section shows two line entries with the first one commented out. The line entry that is commented out sets the value of the device property to "1." The line entry that is not commented out is the one that the setup program reads. This line entry causes the value of the device property to be set to "0." When this device property is set to "0," the audio device opts out of volume persistence.

For more information about the AddProperty directive, see [**INF AddProperty Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546318).

The property name that corresponds to the property category GUID and property ID in the preceding INF file fragment is PKEY\_AudioDevice\_DontPersistControls.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Opting%20Out%20of%20Volume%20Level%20Persistence%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


