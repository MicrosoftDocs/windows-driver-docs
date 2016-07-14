---
Description: Replacing the Default Property Page
MS-HAID: 'audio.replacing\_the\_default\_property\_page'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Replacing the Default Property Page
---

# Replacing the Default Property Page


If you design the custom sAPO using the **CBaseAudioProcessingObject** base class and wrap the system-supplied sAPOs, you must replace the default property page.

In Windows Vista the Sound applet in the Control Panel shows an **Enhancements** property page. This is the default property page that is associated with the system-supplied system effects sAPO. This sAPO is referred to as the Microsoft Audio Home Theater Effects sAPO. Vendors can replace this default property page with a custom page by implementing and registering a custom property page provider.

To design and implement the custom property page provider, perform the following steps.

1.  Create a custom property page. See the [creating property sheets](http://go.microsoft.com/fwlink/p/?linkid=106006) topic on the MSDN website for more information.

2.  Package your property page as a DLL. See the [creating and using a DLL](http://go.microsoft.com/fwlink/p/?linkid=106014) topic on the MSDN website to help you package your custom page as a DLL.

3.  Modify your [INF file](devinst.overview_of_inf_files) to install and register the DLL for the property page.

The following INF file fragment shows how to modify the INF file to register your custom property page.

```
[SysFx.AddReg]
...
HKR,"FX\\0",%PKEY_SYSFX_UiClsid%,,%SYSFX_UI_CLSID%
...
[Strings]
PKEY_SYSFX_UiClsid = "{D04E05A6-594B-4FB6-A80D-01AF5EED7D1D},3"
SYSFX_UI_CLSID     = "{YOUR GUID GOES HERE}"
```

And as a result of the preceding INF file instructions, the installation process modifies the appropriate registry key as follows.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Replacing%20the%20Default%20Property%20Page%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



