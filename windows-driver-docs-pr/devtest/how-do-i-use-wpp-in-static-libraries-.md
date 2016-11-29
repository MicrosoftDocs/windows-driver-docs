---
title: How do I use WPP in static libraries
description: How do I use WPP in static libraries
ms.assetid: 02e13837-f8c7-4824-a4db-5e8b49fdcb59
---

# How do I use WPP in static libraries?


WPP tracing can be used within a static library in such a way that provides separate control over the tracing between the static library (.lib) and binary (.exe, .dll or .sys) that uses it.

Both the binary and library have their own control GUID. This allows tracing to be enabled in the static library, the binary, or both.

The .lib file can be accessed by using WPP at several points, as shown in the following code example. Be aware that it is not important to define the actual value of the control GUID (marked in bold) because the static library is not calling the WPP\_INIT\_TRACING macro, which does the actual registration with ETW.

```
#define WPP_CONTROL_GUIDS \
WPP_DEFINE_CONTROL_GUID(mylib,(0,0,0,0,0), \
WPP_DEFINE_BIT(Error) \
WPP_DEFINE_BIT(Unusual) \
WPP_DEFINE_BIT(Noise) \
)
```

The .dll, .exe, and .sys files that use the library must call WPP\_INIT\_TRACING, which will register the provider with WPP. The binary that calls the macro WPP\_INIT\_TRACING must have a copy of the WPP control GUIDs obtained by the WPP\_CONTROL\_GUID macro. Copies of the flag values are needed only if the flags defined in the static library are planned to be also used in the binary.

In the following code sample, the static library's control GUID is declared first and control GUID's flags match the flags that are defined in the library:

```
#define WPP_CONTROL_GUIDS \
WPP_DEFINE_CONTROL_GUID(SharedStaticLibs,(81b20feb,73a8,4b62,95bc,354477c97a6f), \
WPP_DEFINE_BIT(Error) \
WPP_DEFINE_BIT(Unusual) \
WPP_DEFINE_BIT(Noise) \
) \
WPP_DEFINE_CONTROL_GUID(AppSpecificFlags,(81b20fec,73a8,4b62,95bc,354477c97a6f), \
WPP_DEFINE_BIT(EntryExit) \
WPP_DEFINE_BIT(Initialization) \
WPP_DEFINE_BIT(MemoryAllocations) \
) 
```

You can select the degree of control that you need for tracing on both your component and the static library, by specifying either a separate control GUID for the .lib and the .exe files, each with its own flags, or one control GUID for both. In the sample, the .exe file is using the same flags as the .lib file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20use%20WPP%20in%20static%20libraries?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




