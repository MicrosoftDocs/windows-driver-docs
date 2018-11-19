---
title: Replacing the Default Property Page
description: Replacing the Default Property Page
ms.assetid: decd2f44-fb1f-41bf-b5a7-e1ca295a0bb9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Replacing the Default Property Page


If you design the custom sAPO using the **CBaseAudioProcessingObject** base class and wrap the system-supplied sAPOs, you must replace the default property page.

In Windows Vista the Sound applet in the Control Panel shows an **Enhancements** property page. This is the default property page that is associated with the system-supplied system effects sAPO. This sAPO is referred to as the Microsoft Audio Home Theater Effects sAPO. Vendors can replace this default property page with a custom page by implementing and registering a custom property page provider.

To design and implement the custom property page provider, perform the following steps.

1.  Create a custom property page. See [Creating property sheets](https://go.microsoft.com/fwlink/p/?linkid=106006) for more information.

2.  Package your property page as a DLL. See [Creating and using a DLL](https://go.microsoft.com/fwlink/p/?linkid=106014) for more information about packaging your custom page as a DLL.

3.  Modify your [INF file](https://msdn.microsoft.com/library/windows/hardware/ff549520) to install and register the DLL for the property page.

The following INF file fragment shows how to modify the INF file to register your custom property page.

```inf
[SysFx.AddReg]
...
HKR,"FX\\0",%PKEY_SYSFX_UiClsid%,,%SYSFX_UI_CLSID%
...
[Strings]
PKEY_SYSFX_UiClsid = "{D04E05A6-594B-4FB6-A80D-01AF5EED7D1D},3"
SYSFX_UI_CLSID     = "{YOUR GUID GOES HERE}"
```

And as a result of the preceding INF file instructions, the installation process modifies the appropriate registry key as follows.

```text
HKLM
 SOFTWARE
  Microsoft
  Windows
   CurrentVersion
  MMDevices
  Audio
   Render
  Endpoint
  FXProperties
   ...
  "{D04E05A6-594B-4FB6-A80D-01Af5EED7D1D},3"=
                     "{YOUR CLSID GOES HERE}"
```

The CLSID of the default property page is replaced with the CLSID of your custom property page.

 

 




