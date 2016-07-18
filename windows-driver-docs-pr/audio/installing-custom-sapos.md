---
title: Installing Custom sAPOs
description: Installing Custom sAPOs
ms.assetid: fcf64691-0c75-4ad4-8485-029351a8aa93
keywords: ["CLSID WDK", "sAPO WDK", "LFX WDK", "GFX WDK", "INF files WDK audio"]
---

# Installing Custom sAPOs


When you develop your own high definition (HD) or USB audio driver and wrap or replace the system-supplied sAPOs, you must provide a driver package for installing the driver and sAPOs. The driver package must contain the following:

-   A custom HD or USB audio driver

-   Custom LFX and GFX sAPOs

-   A configuration user interface

-   An INF file

The custom sAPO and the configuration UI are packaged as separate DLLs. The device installation program or a setup program copies the DLLs to the system folders that are indicated in the associated INF file. The DLL that contains the sAPOs must register itself by including a RegisterDlls section in the INF file.

The following paragraphs and INF file fragments show the modifications that are necessary to use the standard INF file to copy and register sAPOs and the configuration UI. For a detailed look at an implementation of this approach, see the Sysfx.inf file. This can be found in the %system root%\\Winddk\\&lt;build number&gt;\\src\\audio\\sysfx\\inf\\ folder.

In the INF file, a GFX or LFX sAPO is identified by its COM class ID (CLSID). In the INF file, you must associate the PnP ID of each physical device that have only one GFX and one LFX sAPO. The following INF file fragment shows part of the registry settings for a custom driver with the GUID and the COM IDs for the LFX and GFX sAPOs.

The property keys are first defined to improve readability.

```
;; Property Keys
PKEY_FX_Association = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},0"
PKEY_FX_PreMixClsid = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},1"
PKEY_FX_PostMixClsid = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},2"
PKEY_FX_UiClsid     = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},3"
PKEY_FriendlyName   = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},4"
```

Where the PKEY\_FX\_PreMixClsid property key represents the LFX sAPO and the PKEY\_FX\_PostMixClsid represents the GFX sAPO. Be aware that the values are of the form "{GUID},ID" where the GUID in this case is D04E05A6-594B-4fb6-A80D-01AF5EED7D1D. And because the GUID is the same for all the components that are associated with the sAPO, the ID helps to further distinguish the particular component. For example, an ID value of '1' refers to the LFX sAPO. See the Audioenginebaseapo.idl file for these predefined values.

The previously defined property keys are then used to add the key value pairs to the registry. This is shown in the following INF file fragment.

```
;; Key value pairs
HKR,"FX\\0",%PKEY_FriendlyName%,,%FX_FriendlyName%
HKR,"FX\\0",%PKEY_FX_PreMixClsid%,,%FX_PREMIX_CLSID%
HKR,"FX\\0",%PKEY_FX_PostMixClsid%,,%FX_POSTMIX_CLSID%
HKR,"FX\\0",%PKEY_FX_UiClsid%,,%FX_UI_CLSID%
HKR,"FX\\0",%PKEY_FX_Association%,,%KSNODETYPE_ANY%
```

Because an audio adapter is capable of supporting multiple inputs and outputs, you must explicitly indicate the type of kernel streaming (KS) node type that your custom sAPO is compatible with. In the preceding INF file fragment, the sAPO is shown to be associated with a KS node type of %KSNODETYPE\_ANY%. Later in this INF file, KSNODETYPE\_ANY is defined as follows:

```
[Strings]
;; Define the strings used in MyINF.inf
...
KSNODETYPE_ANY      = "{00000000-0000-0000-0000-000000000000}"
KSNODETYPE_SPEAKER  = "{DFF21CE1-F70F-11D0-B917-00A0C9223196}"
...
```

A value of **NULL** for KSNODETYPE\_ANY means that this sAPO is compatible with any type of KS node type. To indicate, for example, that your sAPO is only compatible with a KS node type of KSNODETYPE\_SPEAKER, the INF file would show the KS node type and sAPO association as follows:

```
;; Key value pairs
...
HKR,"FX\\0",%PKEY_FX_Association%,,%KSNODETYPE_SPEAKER%
...
```

For more information about the GUID values for the different KS node types, see the Ksmedia.h header file.

Microsoft supplies an **Enhancements** property page for the **Sound** applet on the Control Panel. The page is associated with the Microsoft Audio Home Theater Effects sAPO. Vendors can replace this default property page with a custom page by implementing and registering a custom property page provider.

See the [Replacing the Default Property Page](replacing-the-default-property-page.md) topic for information about how to replace the **Enhancements** property page. The following INF file fragment shows how to modify the INF file to register your custom property page.

```
[SysFx.AddReg]
...
HKR,"FX\\0",%PKEY_SYSFX_UiClsid%,,%SYSFX_UI_CLSID%
...
[Strings]
PKEY_SYSFX_UiClsid = "{D04E05A6-594B-4FB6-A80D-01AF5EED7D1D},3"
SYSFX_UI_CLSID     = "{YOUR GUID GOES HERE}"
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Installing%20Custom%20sAPOs%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




