---
title: Opting Out of Volume Level Persistence
description: Opting Out of Volume Level Persistence
ms.date: 05/05/2023
---

# Opting Out of Volume Level Persistence

By default the volume level settings are maintained when you restart your computer. This default system behavior is referred to as *volume persistence*. If you do not want the volume levels to be maintained by the system after a computer restart, you can use an INF file at the time of installation of the audio adapter, to opt out of the default system behavior.

You may want your driver to opt out of volume persistence if your driver had its own registry cache and sets the levels on the hardware itself, on driver load.

To opt out of volume persistence using an INF file, use the [**AddProperty**](../install/inf-addproperty-directive.md) registry directive to set the value of the PKEY\_AudioDevice\_DontPersistControls registry key to "1". The default value is "0".

The following INF file fragment shows how to opt out of volume persistence:

```inf
;; INF file fragment to show how to use AddProperty
;; to opt out of volume persistence
;;
[Version]
...
Class = MEDIA
ClassGUID = {4d36e96c-e325-11ce-bfc1-08002be10318}
...

[Manufacturer]
%MfgName% = CompanyName,NTamd64
...

[CompanyName.NTamd64]
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

**Note**  The preceding INF file fragment, only shows the **Version** section and the sections relevant to the [**AddProperty**](../install/inf-addproperty-directive.md) directive.

The **%MfgName% = CompanyName** line entry in the **Manufacturer** section references the **CompanyName** section where the model and hardware ID (hw-id) of the audio adapter are provided. This section in an INF file, where model and hw-id information is provided, is called the *models section*. The actual title of the section is user-defined and in the preceding example it is **CompanyName**. For more information about the models section of an INF file, see [**INF Models Section**](../install/inf-models-section.md).

The models section, in turn, references the device driver install (DDInstall) section, where information is provided about other INF files that the setup program must copy. The actual title of this section is user-defined and in the preceding example it is **HdAudModel**. The **Needs=KS.Registration...** line entry provides information about the specific sections within the INF files, from which the setup program must retrieve data for installation

The **HdAudModel** section also contains references to the AddReg and AddProperty sections. The setup program retrieves data from AddReg and AddProperty to set registry keys and device properties respectively. The AddProperty section referenced here is **HdAudModel.AddProperty** and it uses the following format to provide information about the device property:

{*property-category-guid*}, *property-pid*, *type*, \[*flags*\], *value*

The **HdAudModel** section shows two line entries with the first one commented out. The line entry that is commented out sets the value of the device property to "1." The line entry that is not commented out is the one that the setup program reads. This line entry causes the value of the device property to be set to "0." When this device property is set to "0," the audio device opts out of volume persistence.

For more information about the AddProperty directive, see [**INF AddProperty Directive**](../install/inf-addproperty-directive.md).

The property name that corresponds to the property category GUID and property ID in the preceding INF file fragment is PKEY\_AudioDevice\_DontPersistControls.
